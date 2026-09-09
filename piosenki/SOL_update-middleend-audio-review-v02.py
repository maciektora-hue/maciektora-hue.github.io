#!/usr/bin/env python3
import argparse
import csv
import os
import sys
import libsql


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--expected", type=int, required=True)
    args = ap.parse_args()

    with open(args.source, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    if len(rows) != args.expected:
        raise RuntimeError(f"Resolved REVIEW ma {len(rows)} rekordow zamiast {args.expected}")
    if any(r.get("decision") != "use" for r in rows):
        raise RuntimeError("Resolved REVIEW zawiera rekord decision != use")

    ids = [r["utwu_id"] for r in rows]
    if len(set(ids)) != args.expected:
        raise RuntimeError("Duplikat utwu_id w resolved REVIEW")

    url = os.environ["TURSO_DATABASE_URL"]
    token = os.environ["TURSO_AUTH_TOKEN"]
    conn = libsql.connect(database=url, auth_token=token)
    conn.execute("PRAGMA foreign_keys = ON")

    placeholders = ",".join("?" for _ in ids)
    existing = conn.execute(
        f"SELECT COUNT(*) FROM middle_end WHERE utwu_id IN ({placeholders})", ids
    ).fetchone()[0]
    if existing != args.expected:
        raise RuntimeError(f"W middle_end istnieje {existing}/{args.expected} utwu_id")

    try:
        conn.execute("BEGIN TRANSACTION")
        for r in rows:
            conn.execute(
                "UPDATE middle_end SET audio_id=?, youtube_video_id=?, audio_match_quality='review' WHERE utwu_id=?",
                (r["audio_id"], r["youtube_video_id"], r["utwu_id"]),
            )
            conn.execute(
                "INSERT INTO audio_match_details (utwu_id, audio_id, variant_type, note) VALUES (?, ?, ?, ?)",
                (r["utwu_id"], r["audio_id"], r["variant_type"], r["note"]),
            )
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    got = conn.execute(
        f"SELECT utwu_id, audio_id, youtube_video_id, audio_match_quality FROM middle_end WHERE utwu_id IN ({placeholders})",
        ids,
    ).fetchall()
    actual = {r[0]: (r[1], r[2], r[3]) for r in got}
    expected = {
        r["utwu_id"]: (r["audio_id"], r["youtube_video_id"], "review") for r in rows
    }
    detail_count = conn.execute(
        f"SELECT COUNT(*) FROM audio_match_details WHERE utwu_id IN ({placeholders})",
        ids,
    ).fetchone()[0]

    if actual != expected or detail_count != args.expected:
        raise RuntimeError(
            f"Verification failed: middle_end={len(actual)}/{args.expected}, details={detail_count}/{args.expected}"
        )

    print(f"MIDDLE_END_AUDIO_REVIEW_UPDATE_OK={len(actual)}", flush=True)
    print(f"AUDIO_MATCH_DETAILS_OK={detail_count}", flush=True)
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
