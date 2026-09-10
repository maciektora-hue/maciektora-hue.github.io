import csv
import io
import os
from pathlib import Path

import libsql


FILENAME = "SOL_playlisty-brak-utwu-id-95.csv"


def on_starting(server):
    if os.environ.get("DUMP_UNMAPPED_PLAYLISTS") != "1":
        return

    database_url = os.environ.get(
        "TURSO_DATABASE_URL",
        "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io",
    )
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    conn = libsql.connect(database=database_url, auth_token=token)
    try:
        rows = conn.execute("""
            SELECT
                p.playlist_id,
                p.name AS playlist_name,
                p.source_file,
                i.position,
                i.external_track_id AS spotify_id,
                i.source_name AS name,
                i.source_artist AS artist,
                i.source_album AS album,
                (
                    SELECT COUNT(*)
                    FROM middle_end AS m
                    WHERE m.spotify_id = i.external_track_id
                ) AS middle_end_match_count
            FROM playlist_item AS i
            JOIN playlist AS p ON p.playlist_id = i.playlist_id
            WHERE i.utwu_id IS NULL
            ORDER BY p.playlist_id, i.position
        """).fetchall()

        out = io.StringIO(newline="")
        writer = csv.writer(out, lineterminator="\n")
        writer.writerow([
            "playlist_id", "playlist_name", "source_file", "position",
            "spotify_id", "name", "artist", "album",
            "middle_end_match_count", "utwu_id"
        ])
        for row in rows:
            writer.writerow(list(row) + [""])

        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(parents=True, exist_ok=True)
        target = static_dir / FILENAME
        target.write_text(out.getvalue(), encoding="utf-8")

        distinct_tracks = conn.execute(
            "SELECT COUNT(DISTINCT external_track_id) FROM playlist_item WHERE utwu_id IS NULL"
        ).fetchone()[0]
        print(
            f"UNMAPPED_CSV_READY rows={len(rows)} distinct_spotify_ids={distinct_tracks} file={FILENAME}",
            flush=True,
        )
    finally:
        conn.close()
