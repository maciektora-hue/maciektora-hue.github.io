import os

import libsql


def on_starting(server):
    if os.environ.get("POPULATE_EXTERNAL_TRACK") != "1":
        return

    url = os.environ.get("TURSO_DATABASE_URL", "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io")
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    conn = libsql.connect(database=url, auth_token=token)
    try:
        conn.execute("PRAGMA foreign_keys = ON")

        source_positions = conn.execute("""
            SELECT COUNT(*)
            FROM playlist_item AS i
            JOIN playlist AS p ON p.playlist_id = i.playlist_id
            WHERE i.external_track_id IS NOT NULL
              AND trim(i.external_track_id) <> ''
        """).fetchone()[0]

        distinct_keys = conn.execute("""
            SELECT COUNT(*)
            FROM (
                SELECT p.service, i.external_track_id
                FROM playlist_item AS i
                JOIN playlist AS p ON p.playlist_id = i.playlist_id
                WHERE i.external_track_id IS NOT NULL
                  AND trim(i.external_track_id) <> ''
                GROUP BY p.service, i.external_track_id
            )
        """).fetchone()[0]

        metadata_conflicts = conn.execute("""
            SELECT COUNT(*)
            FROM (
                SELECT service, external_track_id
                FROM (
                    SELECT
                        p.service AS service,
                        i.external_track_id AS external_track_id,
                        COALESCE(i.source_name, '') AS source_name,
                        COALESCE(i.source_artist, '') AS source_artist,
                        COALESCE(i.source_album, '') AS source_album
                    FROM playlist_item AS i
                    JOIN playlist AS p ON p.playlist_id = i.playlist_id
                    WHERE i.external_track_id IS NOT NULL
                      AND trim(i.external_track_id) <> ''
                    GROUP BY
                        p.service,
                        i.external_track_id,
                        COALESCE(i.source_name, ''),
                        COALESCE(i.source_artist, ''),
                        COALESCE(i.source_album, '')
                )
                GROUP BY service, external_track_id
                HAVING COUNT(*) > 1
            )
        """).fetchone()[0]

        before = conn.execute("SELECT COUNT(*) FROM external_track").fetchone()[0]

        conn.execute("""
            WITH ranked AS (
                SELECT
                    p.service AS service,
                    i.external_track_id AS external_track_id,
                    i.source_name AS title,
                    i.source_artist AS artist,
                    i.source_album AS album,
                    ROW_NUMBER() OVER (
                        PARTITION BY p.service, i.external_track_id
                        ORDER BY i.playlist_id, i.position
                    ) AS rn
                FROM playlist_item AS i
                JOIN playlist AS p ON p.playlist_id = i.playlist_id
                WHERE i.external_track_id IS NOT NULL
                  AND trim(i.external_track_id) <> ''
            )
            INSERT OR IGNORE INTO external_track (
                service, external_track_id, title, artist, album
            )
            SELECT service, external_track_id, title, artist, album
            FROM ranked
            WHERE rn = 1
        """)
        conn.commit()

        after = conn.execute("SELECT COUNT(*) FROM external_track").fetchone()[0]
        fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
        if fk_errors:
            raise RuntimeError(f"FK errors: {fk_errors}")
        if after < distinct_keys:
            raise RuntimeError(
                f"external_track incomplete: distinct_keys={distinct_keys}, rows={after}"
            )

        print(
            "EXTERNAL_TRACK_POPULATION_OK "
            f"source_positions={source_positions} distinct_keys={distinct_keys} "
            f"before={before} inserted={after-before} after={after} "
            f"metadata_conflicts={metadata_conflicts}",
            flush=True,
        )
    finally:
        conn.close()
