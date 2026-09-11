import json
import threading


def _run_playlist_tags_migration():
    from app import get_connection

    conn = get_connection()
    try:
        columns = [row[1] for row in conn.execute("PRAGMA table_info(playlist)").fetchall()]
        if "playlist_tags" not in columns:
            conn.execute("ALTER TABLE playlist ADD COLUMN playlist_tags TEXT NOT NULL DEFAULT ''")

        for playlist_id, raw in conn.execute("SELECT playlist_id, tags FROM playlist").fetchall():
            try:
                parsed = json.loads(raw or "")
            except Exception:
                parsed = None
            if isinstance(parsed, list):
                plain = "; ".join(str(x).strip() for x in parsed if str(x).strip())
                conn.execute(
                    "UPDATE playlist SET playlist_tags=? WHERE playlist_id=? AND playlist_tags=''",
                    (plain, playlist_id),
                )

        tags = (
            "owner:maciek-tora; wyspa=swiatla; "
            "spotify_url=https://open.spotify.com/playlist/272wzPwVUjxBmqJ8eNQsTW; "
            "youtube_music_url=https://music.youtube.com/playlist?list=PLdqONEJClykk"
        )
        conn.execute(
            "UPDATE playlist SET playlist_tags=? WHERE playlist_id=?",
            (tags, "spotify:wyspa-swiatla:2026-09-11"),
        )
        conn.commit()

        row = conn.execute(
            "SELECT playlist_id, name, playlist_tags FROM playlist WHERE playlist_id=?",
            ("spotify:wyspa-swiatla:2026-09-11",),
        ).fetchone()
        if row is None or "spotify_url=" not in row[2] or "youtube_music_url=" not in row[2]:
            raise RuntimeError("playlist_tags verification failed")
        print("PLAYLIST_PLAIN_TAGS_OK " + repr(row), flush=True)
    finally:
        conn.close()


def when_ready(server):
    threading.Thread(
        target=_run_playlist_tags_migration,
        name="playlist-plain-tags-once",
        daemon=True,
    ).start()
