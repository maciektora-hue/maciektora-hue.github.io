import base64
import csv
import io
import os

import libsql


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

        payload = base64.b64encode(out.getvalue().encode("utf-8")).decode("ascii")
        chunk_size = 3000
        chunks = [payload[i:i+chunk_size] for i in range(0, len(payload), chunk_size)]
        distinct_tracks = conn.execute(
            "SELECT COUNT(DISTINCT external_track_id) FROM playlist_item WHERE utwu_id IS NULL"
        ).fetchone()[0]
        print(
            f"UNMAPPED_CSV_META rows={len(rows)} distinct_spotify_ids={distinct_tracks} chunks={len(chunks)}",
            flush=True,
        )
        for idx, chunk in enumerate(chunks):
            print(f"UNMAPPED_CSV_CHUNK_{idx:03d}={chunk}", flush=True)
        print("UNMAPPED_CSV_END", flush=True)
    finally:
        conn.close()
