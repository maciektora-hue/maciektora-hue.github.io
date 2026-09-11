import os

import libsql


def on_starting(server):
    if os.environ.get("MIGRATE_PLAYLIST_ITEM_EXTERNAL_TRACK_PK") != "1":
        return

    url = os.environ.get("TURSO_DATABASE_URL", "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io")
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    conn = libsql.connect(database=url, auth_token=token)
    try:
        conn.execute("PRAGMA foreign_keys = ON")

        total_before = conn.execute("SELECT COUNT(*) FROM playlist_item").fetchone()[0]
        mapped_before = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE utwu_id IS NOT NULL").fetchone()[0]
        unresolved_before = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE utwu_id IS NULL").fetchone()[0]
        ext_tracks_before = conn.execute("SELECT COUNT(*) FROM external_track").fetchone()[0]
        links_before = conn.execute("SELECT COUNT(*) FROM external_track_utwu").fetchone()[0]

        cols = [row[1] for row in conn.execute("PRAGMA table_info(playlist_item)").fetchall()]
        if "external_track_pk" not in cols:
            conn.execute("""
                ALTER TABLE playlist_item
                ADD COLUMN external_track_pk INTEGER
                    REFERENCES external_track(external_track_pk)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT
            """)

        conn.execute("""
            UPDATE playlist_item AS i
            SET external_track_pk = (
                SELECT e.external_track_pk
                FROM playlist AS p
                JOIN external_track AS e
                  ON e.service = p.service
                 AND e.external_track_id = i.external_track_id
                WHERE p.playlist_id = i.playlist_id
            )
            WHERE i.external_track_pk IS NULL
              AND i.external_track_id IS NOT NULL
              AND trim(i.external_track_id) <> ''
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_playlist_item_external_track_pk
            ON playlist_item(external_track_pk)
        """)
        conn.commit()

        total_after = conn.execute("SELECT COUNT(*) FROM playlist_item").fetchone()[0]
        linked = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE external_track_pk IS NOT NULL").fetchone()[0]
        unlinked = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE external_track_pk IS NULL").fetchone()[0]
        distinct_linked = conn.execute("SELECT COUNT(DISTINCT external_track_pk) FROM playlist_item WHERE external_track_pk IS NOT NULL").fetchone()[0]
        mapped_after = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE utwu_id IS NOT NULL").fetchone()[0]
        unresolved_after = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE utwu_id IS NULL").fetchone()[0]
        ext_tracks_after = conn.execute("SELECT COUNT(*) FROM external_track").fetchone()[0]
        links_after = conn.execute("SELECT COUNT(*) FROM external_track_utwu").fetchone()[0]
        mismatches = conn.execute("""
            SELECT COUNT(*)
            FROM playlist_item AS i
            JOIN playlist AS p ON p.playlist_id = i.playlist_id
            JOIN external_track AS e ON e.external_track_pk = i.external_track_pk
            WHERE e.service <> p.service
               OR e.external_track_id <> i.external_track_id
        """).fetchone()[0]
        fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()

        if fk_errors:
            raise RuntimeError(f"FK errors: {fk_errors}")
        if total_before != total_after:
            raise RuntimeError(f"playlist_item count changed: {total_before} -> {total_after}")
        if linked != total_after or unlinked != 0:
            raise RuntimeError(f"external_track_pk incomplete: linked={linked}, unlinked={unlinked}, total={total_after}")
        if mismatches != 0:
            raise RuntimeError(f"external_track_pk mismatches={mismatches}")
        if mapped_before != mapped_after or unresolved_before != unresolved_after:
            raise RuntimeError("utwu_id split changed")
        if ext_tracks_before != ext_tracks_after or links_before != links_after:
            raise RuntimeError("external_track layer counts changed unexpectedly")

        cols_after = [row[1] for row in conn.execute("PRAGMA table_info(playlist_item)").fetchall()]
        print(
            "PLAYLIST_ITEM_EXTERNAL_TRACK_PK_OK "
            f"columns={len(cols_after)} total={total_after} linked={linked} unlinked={unlinked} "
            f"distinct_external_tracks={distinct_linked} mapped_utwu={mapped_after} unresolved_utwu={unresolved_after} "
            f"external_tracks={ext_tracks_after} external_track_utwu={links_after} mismatches={mismatches}",
            flush=True,
        )
    finally:
        conn.close()
