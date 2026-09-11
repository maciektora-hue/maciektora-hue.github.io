import os

import libsql


def on_starting(server):
    if os.environ.get("POPULATE_EXTERNAL_TRACK_UTWU") != "1":
        return

    url = os.environ.get("TURSO_DATABASE_URL", "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io")
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    conn = libsql.connect(database=url, auth_token=token)
    try:
        conn.execute("PRAGMA foreign_keys = ON")

        source_mapped_positions = conn.execute("""
            SELECT COUNT(*)
            FROM playlist_item
            WHERE utwu_id IS NOT NULL
              AND external_track_id IS NOT NULL
              AND trim(external_track_id) <> ''
        """).fetchone()[0]

        expected_distinct_mappings = conn.execute("""
            SELECT COUNT(*)
            FROM (
                SELECT DISTINCT e.external_track_pk, i.utwu_id
                FROM playlist_item AS i
                JOIN playlist AS p
                    ON p.playlist_id = i.playlist_id
                JOIN external_track AS e
                    ON e.service = p.service
                   AND e.external_track_id = i.external_track_id
                WHERE i.utwu_id IS NOT NULL
                  AND i.external_track_id IS NOT NULL
                  AND trim(i.external_track_id) <> ''
            )
        """).fetchone()[0]

        multi_target_external_tracks = conn.execute("""
            SELECT COUNT(*)
            FROM (
                SELECT e.external_track_pk
                FROM playlist_item AS i
                JOIN playlist AS p
                    ON p.playlist_id = i.playlist_id
                JOIN external_track AS e
                    ON e.service = p.service
                   AND e.external_track_id = i.external_track_id
                WHERE i.utwu_id IS NOT NULL
                  AND i.external_track_id IS NOT NULL
                  AND trim(i.external_track_id) <> ''
                GROUP BY e.external_track_pk
                HAVING COUNT(DISTINCT i.utwu_id) > 1
            )
        """).fetchone()[0]

        before = conn.execute("SELECT COUNT(*) FROM external_track_utwu").fetchone()[0]

        conn.execute("""
            INSERT OR IGNORE INTO external_track_utwu (
                external_track_pk,
                utwu_id
            )
            SELECT DISTINCT
                e.external_track_pk,
                i.utwu_id
            FROM playlist_item AS i
            JOIN playlist AS p
                ON p.playlist_id = i.playlist_id
            JOIN external_track AS e
                ON e.service = p.service
               AND e.external_track_id = i.external_track_id
            WHERE i.utwu_id IS NOT NULL
              AND i.external_track_id IS NOT NULL
              AND trim(i.external_track_id) <> ''
        """)
        conn.commit()

        after = conn.execute("SELECT COUNT(*) FROM external_track_utwu").fetchone()[0]
        fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
        if fk_errors:
            raise RuntimeError(f"FK errors: {fk_errors}")
        if after < expected_distinct_mappings:
            raise RuntimeError(
                f"external_track_utwu incomplete: expected={expected_distinct_mappings}, rows={after}"
            )

        print(
            "EXTERNAL_TRACK_UTWU_POPULATION_OK "
            f"source_mapped_positions={source_mapped_positions} "
            f"distinct_mappings={expected_distinct_mappings} "
            f"before={before} inserted={after-before} after={after} "
            f"multi_target_external_tracks={multi_target_external_tracks}",
            flush=True,
        )
    finally:
        conn.close()
