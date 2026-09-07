#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

import libsql


TURSO_DATABASE_URL = os.environ.get(
    "TURSO_DATABASE_URL",
    "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io",
)
TURSO_ADMIN_TOKEN = os.environ.get("TURSO_ADMIN_TOKEN")

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent

EXPORTS = {
    "rosja": {
        "view": "v_rosja_mapa_sekcji",
        "expected": 620,
        "columns": [
            "dokument_kod",
            "dokument_plik",
            "dokument_tytul",
            "url_stabilny",
            "poziom",
            "glebokosc",
            "kolejnosc",
            "sekcja_tytul",
            "anchor",
            "anchor_status",
            "deep_link",
            "opis",
        ],
        "default_out": REPO_ROOT / "rosja" / "SOL_mapa-sekcji-z-opisami-export-SQL.tsv",
    },
    "audhd": {
        "view": "v_audhd_mapa_sekcji",
        "expected": 338,
        "columns": [
            "dokument_kod",
            "dokument_plik",
            "dokument_tytul",
            "url_zrodlowy",
            "poziom",
            "glebokosc",
            "kolejnosc",
            "sekcja_tytul",
            "anchor",
            "anchor_status",
            "deep_link",
        ],
        "default_out": REPO_ROOT / "audhd" / "SOL_mapa-sekcji-i-anchorow-audhd-export-SQL.tsv",
    },
}


def connection():
    if not TURSO_ADMIN_TOKEN:
        raise SystemExit("STOP: brak TURSO_ADMIN_TOKEN")
    return libsql.connect(database=TURSO_DATABASE_URL, auth_token=TURSO_ADMIN_TOKEN)


def export_one(conn, collection: str, out_path: Path | None = None) -> Path:
    spec = EXPORTS[collection]
    marker = conn.execute(
        "SELECT value FROM content_meta WHERE key = 'content_initial_import_v1'"
    ).fetchone()
    if not marker or marker[0] != "done":
        raise SystemExit("STOP: content_initial_import_v1 != done")

    columns = spec["columns"]
    sql = f"SELECT {', '.join(columns)} FROM {spec['view']}"
    rows = conn.execute(sql).fetchall()
    if len(rows) != spec["expected"]:
        raise SystemExit(
            f"STOP: {collection}: oczekiwano {spec['expected']} rekordów, jest {len(rows)}"
        )

    bad_status = sum(1 for row in rows if row[columns.index("anchor_status")] != "OK")
    if bad_status:
        raise SystemExit(f"STOP: {collection}: rekordy z anchor_status != OK: {bad_status}")

    path = out_path or spec["default_out"]
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)
        writer.writerows(rows)
    tmp.replace(path)
    print(f"OK: {collection}: {len(rows)} rekordów -> {path}")
    return path


def main():
    parser = argparse.ArgumentParser(
        description="Eksportuj mapy treści z Turso/libSQL do kompatybilnego TSV. SQL pozostaje źródłem prawdy."
    )
    parser.add_argument(
        "collection",
        choices=["rosja", "audhd", "all"],
        nargs="?",
        default="all",
    )
    parser.add_argument(
        "--out",
        help="Ścieżka wyjściowa; dozwolona tylko dla pojedynczej kolekcji.",
    )
    args = parser.parse_args()

    if args.collection == "all" and args.out:
        raise SystemExit("STOP: --out można użyć tylko dla rosja albo audhd")

    conn = connection()
    try:
        if args.collection == "all":
            export_one(conn, "rosja")
            export_one(conn, "audhd")
        else:
            export_one(conn, args.collection, Path(args.out) if args.out else None)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
