from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "SOL-import-danych.sql"

TAG_CSV = BASE / "sol-definicje-tagow-CSV-v01-02.csv"
LYRICS_CSV_1 = BASE / "sol-piosenki-slowa-CSV-v07-00.csv"
LYRICS_CSV_2 = BASE / "sol-piosenki-slowa-kontynuacja-CSV-v01-08.csv"
MIDDLE_CSV = BASE / "sol-middleend-CSV-v08-11.csv"
SNAPSHOTS_CSV = BASE / "sol-piosenki-tagi-CSV-v09-14.csv"
ONTOLOGY_TXT = BASE / "sol-ontologia-tagow-TXT-v01-03.txt"

EXPECTED = {
    TAG_CSV.name: ["tag", "definition"],
    LYRICS_CSV_1.name: ["lyrics_id", "lyrics_text"],
    LYRICS_CSV_2.name: ["lyrics_id", "lyrics_text"],
    MIDDLE_CSV.name: [
        "utwu_id",
        "lyrics_id",
        "spotify_id",
        "spotify_order",
        "title_original",
        "title_normalized",
        "title_parsed",
        "artist_original",
        "artist_normalized",
        "artist_parsed",
        "album_original",
        "match_status",
        "match_candidates",
        "match_note",
        "lyrics_status",
    ],
    SNAPSHOTS_CSV.name: ["lyrics_id", "tagged_at", "tags"],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        actual = reader.fieldnames or []
        expected = EXPECTED[path.name]
        if actual != expected:
            raise RuntimeError(
                f"Zły nagłówek {path.name}: {actual!r}; oczekiwano {expected!r}"
            )
        return list(reader)


def sql_text(value: str | None, *, empty_as_null: bool = True) -> str:
    if value is None or (empty_as_null and value == ""):
        return "NULL"
    return "'" + value.replace("'", "''") + "'"


def sql_value(value) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, int):
        return str(value)
    return sql_text(str(value), empty_as_null=False)


def render_insert(table: str, columns: list[str], values: list) -> str:
    cols = ", ".join(columns)
    vals = ", ".join(sql_value(v) for v in values)
    return f"INSERT INTO {table} ({cols}) VALUES ({vals});"


def require_unique(rows: list[dict[str, str]], key: str, source: str) -> None:
    seen: set[str] = set()
    dupes: list[str] = []
    for row in rows:
        value = row[key]
        if value in seen:
            dupes.append(value)
        seen.add(value)
    if dupes:
        sample = ", ".join(sorted(set(dupes))[:10])
        raise RuntimeError(f"Duplikaty {key} w {source}: {sample}")


def ontology_rows() -> dict[str, tuple[list[str], list[tuple]]]:
    sql = ONTOLOGY_TXT.read_text(encoding="utf-8-sig")
    conn = sqlite3.connect(":memory:")
    try:
        conn.executescript(sql)
        specs = {
            "families": ["family_name", "label", "color_hex", "description", "sort_order"],
            "tag_groups": ["group_name", "label"],
            "axes": ["axis_name", "label", "description", "family_name", "sort_order"],
            "tag_group": ["tag", "group_name"],
            "tag_axis": ["tag", "axis_name"],
        }
        out = {}
        for table, columns in specs.items():
            rows = conn.execute(
                f"SELECT {', '.join(columns)} FROM {table}"
            ).fetchall()
            out[table] = (columns, rows)
        return out
    finally:
        conn.close()


def parse_snapshot_tags(value: str) -> set[str]:
    result: set[str] = set()
    for item in value.split(";"):
        item = item.strip()
        if not item:
            continue
        tag = item.split(":", 1)[0].strip()
        if tag:
            result.add(tag)
    return result


def main() -> None:
    tags = read_csv(TAG_CSV)
    lyrics_1 = read_csv(LYRICS_CSV_1)
    lyrics_2 = read_csv(LYRICS_CSV_2)
    middle = read_csv(MIDDLE_CSV)
    snapshots = read_csv(SNAPSHOTS_CSV)
    ontology = ontology_rows()

    require_unique(tags, "tag", TAG_CSV.name)
    require_unique(lyrics_1, "lyrics_id", LYRICS_CSV_1.name)
    require_unique(lyrics_2, "lyrics_id", LYRICS_CSV_2.name)
    require_unique(middle, "utwu_id", MIDDLE_CSV.name)

    lyrics = lyrics_1 + lyrics_2
    require_unique(lyrics, "lyrics_id", "oba pliki lyrics razem")

    tag_ids = {r["tag"] for r in tags}
    lyrics_ids = {r["lyrics_id"] for r in lyrics}

    missing_middle_lyrics = sorted(
        {
            r["lyrics_id"]
            for r in middle
            if r["lyrics_id"] and r["lyrics_id"] not in lyrics_ids
        }
    )
    if missing_middle_lyrics:
        raise RuntimeError(
            "middle_end wskazuje brakujące lyrics_id: "
            + ", ".join(missing_middle_lyrics[:20])
        )

    missing_snapshot_lyrics = sorted(
        {r["lyrics_id"] for r in snapshots if r["lyrics_id"] not in lyrics_ids}
    )
    if missing_snapshot_lyrics:
        raise RuntimeError(
            "tag_snapshots wskazuje brakujące lyrics_id: "
            + ", ".join(missing_snapshot_lyrics[:20])
        )

    ontology_tags = {
        row[0]
        for table in ("tag_group", "tag_axis")
        for row in ontology[table][1]
    }
    missing_ontology_tags = sorted(ontology_tags - tag_ids)
    if missing_ontology_tags:
        raise RuntimeError(
            "Ontologia wskazuje tagi nieobecne w tag_catalog: "
            + ", ".join(missing_ontology_tags[:20])
        )

    snapshot_tags: set[str] = set()
    for row in snapshots:
        snapshot_tags.update(parse_snapshot_tags(row["tags"]))
    missing_snapshot_tags = sorted(snapshot_tags - tag_ids)
    if missing_snapshot_tags:
        raise RuntimeError(
            "Snapshoty używają tagów nieobecnych w tag_catalog: "
            + ", ".join(missing_snapshot_tags[:20])
        )

    lines: list[str] = [
        "-- SOL — dane do schema.sql",
        "-- Wygenerowane z aktywnych CSV i sol-ontologia-tagow-TXT-v01-03.txt.",
        "-- Źródłowe pliki nie są modyfikowane.",
        "PRAGMA foreign_keys = ON;",
        "BEGIN TRANSACTION;",
        "",
        "-- tag_catalog",
    ]

    for row in tags:
        lines.append(
            "INSERT INTO tag_catalog (tag, definition) VALUES ("
            + sql_text(row["tag"], empty_as_null=False)
            + ", "
            + sql_text(row["definition"])
            + ");"
        )

    for table in ("families", "tag_groups", "axes", "tag_group", "tag_axis"):
        columns, rows = ontology[table]
        lines.append("")
        lines.append(f"-- {table}")
        for row in rows:
            lines.append(render_insert(table, columns, list(row)))

    lines.append("")
    lines.append("-- lyrics: oba pliki CSV w jednej tabeli")
    for row in lyrics:
        lines.append(
            "INSERT INTO lyrics (lyrics_id, lyrics_text) VALUES ("
            + sql_text(row["lyrics_id"], empty_as_null=False)
            + ", "
            + sql_text(row["lyrics_text"], empty_as_null=False)
            + ");"
        )

    middle_columns = EXPECTED[MIDDLE_CSV.name]
    lines.append("")
    lines.append("-- middle_end")
    for row in middle:
        values = []
        for col in middle_columns:
            if col == "spotify_order":
                values.append(int(row[col]) if row[col] else None)
            else:
                values.append(row[col] if row[col] != "" else None)
        lines.append(render_insert("middle_end", middle_columns, values))

    lines.append("")
    lines.append("-- tag_snapshots")
    for row in snapshots:
        lines.append(
            render_insert(
                "tag_snapshots",
                ["lyrics_id", "tagged_at", "tags"],
                [row["lyrics_id"], row["tagged_at"], row["tags"]],
            )
        )

    lines.extend(["", "COMMIT;", ""])
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"OK: {OUTPUT.name}")
    print(f"tag_catalog: {len(tags)}")
    print(f"lyrics: {len(lyrics)}")
    print(f"middle_end: {len(middle)}")
    print(f"tag_snapshots: {len(snapshots)}")
    for table in ("families", "tag_groups", "axes", "tag_group", "tag_axis"):
        print(f"{table}: {len(ontology[table][1])}")


if __name__ == "__main__":
    main()
