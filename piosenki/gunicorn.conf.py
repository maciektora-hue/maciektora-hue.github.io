import os


def when_ready(server):
    if os.environ.get("SET_ALLTIMEBEST_SPOTIFY_ID") != "1":
        return

    import libsql

    db = libsql.connect(
        database=os.environ["TURSO_DATABASE_URL"],
        auth_token=os.environ["TURSO_ADMIN_TOKEN"],
    )
    try:
        db.execute("PRAGMA foreign_keys = ON")
        rows = db.execute(
            """
            SELECT playlist_id, service, name, external_playlist_id, external_url
            FROM playlist
            WHERE playlist_id = 'spotify:alltimebest'
            """
        ).fetchall()
        if len(rows) != 1:
            raise RuntimeError(f"Expected exactly one spotify:alltimebest row, got {len(rows)}")

        before = rows[0]
        if before[1] != "spotify" or before[2] != "AllTimeBestSpotify":
            raise RuntimeError(f"Unexpected playlist identity: {before!r}")
        if before[3] not in (None, "", "5wDt92D4lFaSDIuVrdKLF9"):
            raise RuntimeError(f"Conflicting external_playlist_id: {before[3]!r}")
        expected_url = "https://open.spotify.com/playlist/5wDt92D4lFaSDIuVrdKLF9"
        if before[4] not in (None, "", expected_url):
            raise RuntimeError(f"Conflicting external_url: {before[4]!r}")

        db.execute(
            """
            UPDATE playlist
            SET external_playlist_id = ?, external_url = ?
            WHERE playlist_id = 'spotify:alltimebest'
              AND service = 'spotify'
              AND name = 'AllTimeBestSpotify'
            """,
            ("5wDt92D4lFaSDIuVrdKLF9", expected_url),
        )
        db.commit()

        after = db.execute(
            """
            SELECT playlist_id, service, name, external_playlist_id, external_url
            FROM playlist
            WHERE playlist_id = 'spotify:alltimebest'
            """
        ).fetchone()
        if after[3] != "5wDt92D4lFaSDIuVrdKLF9" or after[4] != expected_url:
            raise RuntimeError(f"Verification failed: {after!r}")

        print(
            "ALLTIMEBEST_SPOTIFY_ID_OK "
            f"playlist_id={after[0]} external_playlist_id={after[3]} external_url={after[4]}",
            flush=True,
        )
    finally:
        db.close()
