#!/usr/bin/env python3
import csv
import os
import sys
import libsql

SOURCE = "piosenki/audio_middleend_ready_0151_0200.tsv"
EXPECTED = 36


def main():
    token = os.environ.get("TURSO_AUTH_TOKEN")
    url = os.environ.get("TURSO_DATABASE_URL")
    if not token or not url:
        raise RuntimeError("Brak TURSO_DATABASE_URL lub TURSO_AUTH_TOKEN")

    with open(SOURCE, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    if len(rows) != EXPECTED:
        raise RuntimeError(f"READY ma {len(rows)} rekordow zamiast {EXPECTED}")

    utwu_ids = [r["candidate_utwu_id"] for r in rows]
    if len(set(utwu_ids)) != EXPECTED:
        raise RuntimeError("Duplikat candidate_utwu_id w READY")

    conn = libsql.connect(database=url, auth_token=token)
    conn.execute("PRAGMA foreign_keys = ON")

    cols = {r[1] for r in conn.execute("PRAGMA table_info(middle_end)").fetchall()}
    required = {"utwu_id", "audio_id", "youtube_video_id", "audio_match_quality"}
    missing = required - cols

    # Te trzy kolumny sa czescia uzgodnionego modelu. Dodajemy je tylko jesli faktycznie ich jeszcze brak.
    if "audio_id" in missing:
        conn.execute("ALTER TABLE middle_end ADD COLUMN audio_id TEXT REFERENCES audio(audio_id)")
    if "youtube_video_id" in missing:
        conn.execute("ALTER TABLE middle_end ADD COLUMN youtube_video_id TEXT")
    if "audio_match_quality" in missing:
        conn.execute("ALTER TABLE middle_end ADD COLUMN audio_match_quality TEXT")
    conn.commit()

    placeholders = ",".join("?" for _ in utwu_ids)
    existing = conn.execute(
        f"SELECT COUNT(*) FROM middle_end WHERE utwu_id IN ({placeholders})",
        utwu_ids,
    ).fetchone()[0]
    if existing != EXPECTED:
        raise RuntimeError(f"W middle_end istnieje {existing}/{EXPECTED} utwu_id z READY")

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
