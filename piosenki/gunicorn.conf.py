import os


def when_ready(server):
    if os.environ.get("TAG_CURRENT_PLAYLISTS_OWNER_MACIEK") != "1":
        return

    import libsql

    db = libsql.connect(
        database=os.environ["TURSO_DATABASE_URL"],
        auth_token=os.environ["TURSO_ADMIN_TOKEN"],
    )
    try:
        db.execute("PRAGMA foreign_keys = ON")
        db.execute(
            """
            INSERT OR IGNORE INTO playlist_tag_def(tag, description)
            VALUES ('owner:maciek-tora', 'Playlista należąca do Maćka Tory.')
            """
        )
        db.execute(
            """
            UPDATE playlist
            SET tags = CASE
                WHEN EXISTS (
                    SELECT 1 FROM json_each(playlist.tags)
                    WHERE value = 'owner:maciek-tora'
                ) THEN tags
                ELSE json_insert(tags, '$[#]', 'owner:maciek-tora')
            END
            """
        )
        db.commit()

        total = db.execute("SELECT COUNT(*) FROM playlist").fetchone()[0]
        tagged = db.execute(
            """
            SELECT COUNT(*)
            FROM playlist AS p
            WHERE EXISTS (
                SELECT 1 FROM json_each(p.tags)
                WHERE value = 'owner:maciek-tora'
            )
            """
        ).fetchone()[0]
        alltime = db.execute(
            "SELECT tags FROM playlist WHERE playlist_id = 'spotify:alltimebest'"
        ).fetchone()
        if tagged != total or alltime is None or 'owner:maciek-tora' not in alltime[0]:
            raise RuntimeError(
                f"Verification failed total={total} tagged={tagged} alltime={alltime!r}"
            )
        print(
            f"PLAYLIST_OWNER_TAG_OK total={total} tagged={tagged} alltime_tags={alltime[0]}",
            flush=True,
        )
    finally:
        db.close()
