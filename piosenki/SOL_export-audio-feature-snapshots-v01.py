#!/usr/bin/env python3
import csv
import os
import re
import sys
import libsql

SOURCE = "piosenki/audio_features_v08.csv"
BATCH_SIZE = 50
ANALYZER_VERSION = "v05"
DATASET_VERSION = "v08"

META_CSV = [
    "plik", "sciezka_wzgledna", "rozmiar_mb", "czas_s",
    "sample_rate_hz", "channels",
]
TECH_SQL = {
    "snapshot_id", "audio_id", "analyzer_version",
    "dataset_version", "analyzed_at",
}
PREFIX_RE = re.compile(r"^(\d{4})\b")


def convert(value, sql_type, column):
    if value is None or value == "":
        raise RuntimeError(f"Pusta wartosc w kolumnie {column}")
    t = (sql_type or "").upper()
    if "INT" in t:
        return int(float(value))
    if any(x in t for x in ("REAL", "FLOA", "DOUB")):
        return float(value)
    return value


def main():
    token = os.environ.get("TURSO_AUTH_TOKEN")
    url = os.environ.get("TURSO_DATABASE_URL")
    if not token or not url:
        raise RuntimeError("Brak TURSO_DATABASE_URL lub TURSO_AUTH_TOKEN")

    conn = libsql.connect(database=url, auth_token=token)
    conn.execute("PRAGMA foreign_keys = ON")

    table_info = conn.execute("PRAGMA table_info(audio_feature_snapshots)").fetchall()
    if not table_info:
        raise RuntimeError("Brak tabeli audio_feature_snapshots")

    sql_columns = [row[1] for row in table_info]
    type_map = {row[1]: row[2] for row in table_info}
    feature_columns = [c for c in sql_columns if c not in TECH_SQL]

    with open(SOURCE, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        csv_columns = reader.fieldnames or []
        if csv_columns[:6] != META_CSV:
            raise RuntimeError(f"Nieoczekiwane pierwsze 6 kolumn CSV: {csv_columns[:6]}")
        csv_features = csv_columns[6:]
        if len(csv_features) != 185 or set(csv_features) != set(feature_columns):
            raise RuntimeError(
                f"Niezgodne kolumny cech: CSV={len(csv_features)} SQL={len(feature_columns)}"
            )

        source_rows = list(reader)

    existing = {
        row[0]
        for row in conn.execute(
            "SELECT audio_id FROM audio_feature_snapshots "
            "WHERE analyzer_version=? AND dataset_version=?",
            (ANALYZER_VERSION, DATASET_VERSION),
        ).fetchall()
    }

    rows = []
    for r in source_rows:
        filename = r["plik"].strip()
        m = PREFIX_RE.search(filename)
        if not m:
            raise RuntimeError(f"Nie moge odczytac audio_id z: {filename}")
        audio_id = f"audio-{m.group(1)}"
        if audio_id in existing:
            continue

        row = [audio_id, ANALYZER_VERSION, DATASET_VERSION, None]
        row.extend(convert(r[col], type_map[col], col) for col in feature_columns)
        rows.append(tuple(row))

    insert_columns = [
        "audio_id", "analyzer_version", "dataset_version", "analyzed_at",
        *feature_columns,
    ]
    cols_sql = ", ".join(insert_columns)
    one_row = "(" + ",".join("?" for _ in insert_columns) + ")"

    already = len(existing)
    total = len(source_rows)
    print(f"START: {already}/{total} juz zapisane, {len(rows)} do eksportu", flush=True)

    for start in range(0, len(rows), BATCH_SIZE):
        batch = rows[start:start + BATCH_SIZE]
        values_sql = ",".join(one_row for _ in batch)
        params = [value for row in batch for value in row]
        try:
            conn.execute("BEGIN TRANSACTION")
            conn.execute(
                f"INSERT INTO audio_feature_snapshots ({cols_sql}) VALUES {values_sql}",
                params,
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise

        done = already + min(start + len(batch), len(rows))
        print(f"{done}/{total} zapisane", flush=True)

    final_count = conn.execute(
        "SELECT COUNT(*) FROM audio_feature_snapshots "
        "WHERE analyzer_version=? AND dataset_version=?",
        (ANALYZER_VERSION, DATASET_VERSION),
    ).fetchone()[0]
    distinct_audio = conn.execute(
        "SELECT COUNT(DISTINCT audio_id) FROM audio_feature_snapshots "
        "WHERE analyzer_version=? AND dataset_version=?",
        (ANALYZER_VERSION, DATASET_VERSION),
    ).fetchone()[0]

    print(f"SNAPSHOTS={final_count}", flush=True)
    print(f"DISTINCT_AUDIO_ID={distinct_audio}", flush=True)

    if final_count != total or distinct_audio != total:
        raise RuntimeError(
            f"Kontrola koncowa nie przeszla: rows={final_count}, audio={distinct_audio}, expected={total}"
        )

    print(f"AUDIO_FEATURE_SNAPSHOTS_EXPORT_OK={final_count}", flush=True)
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
