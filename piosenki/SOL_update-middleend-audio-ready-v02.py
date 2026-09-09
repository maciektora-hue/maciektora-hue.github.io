#!/usr/bin/env python3
import argparse
import csv
import os
import sys
import libsql


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--expected", required=True, type=int)
    return p.parse_args()


def main():
    args = parse_args()
    token = os.environ.get("TURSO_AUTH_TOKEN")
    url = os.environ.get("TURSO_DATABASE_URL")
    if not token or not url:
        raise RuntimeError("Brak TURSO_DATABASE_URL lub TURSO_AUTH_TOKEN")

    with open(args.source, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    if len(rows) != args.expected:
        raise RuntimeError(f"READY ma {len(rows)} rekordow zamiast {args.expected}")

    utwu_ids = [r["candidate_utwu_id"] for r in rows]
    if len(set(utwu_ids)) != args.expected:
        raise RuntimeError("Duplikat candidate_utwu_id w READY")

    conn = libsql.connect(database=url, auth_token=token)
    conn.execute("PRAGMA foreign_keys = ON")

    placeholders = ",".join("?" for _ in utwu_ids)
    existing = conn.execute(
        f"SELECT COUNT(*) FROM middle_end WHERE utwu_id IN ({placeholders})",
        utwu_ids,
    ).fetchone()[0]
    if existing != args.expected:
        raise RuntimeError(f"W middle_end istnieje {existing}/{args.expected} utwu_id z READY")

    try:
        conn.execute("BEGIN TRANSACTION")
        for r in rows:
            conn.execute(
                "UPDATE middle_end SET audio_id=?, youtube_video_id=?, audio_match_quality=? WHERE utwu_id=?",
                (
                    r["audio_id"],
                    r["youtube_video_id"],
                    r["quality"],
                    r["candidate_utwu_id"],
                ),
            )
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    got = conn.execute(
        f"SELECT utwu_id, audio_id, youtube_video_id, audio_match_quality FROM middle_end WHERE utwu_id IN ({placeholders})",
        utwu_ids,
    ).fetchall()
    actual = {r[0]: (r[1], r[2], r[3]) for r in got}
    expected = {
        r["candidate_utwu_id"]: (r["audio_id"], r["youtube_video_id"], r["quality"])
        for r in rows
    }

    bad = [k for k, v in expected.items() if actual.get(k) != v]
    if bad:
        raise RuntimeError(f"Weryfikacja po zapisie nie przeszla dla: {bad}")

    print(f"MIDDLE_END_AUDIO_UPDATE_OK={len(actual)}", flush=True)
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
