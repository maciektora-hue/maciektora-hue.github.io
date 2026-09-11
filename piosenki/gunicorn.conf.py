import json
import threading


def _old_tags(raw):
    try:
        value = json.loads(raw or "[]")
    except Exception:
        return []
    if not isinstance(value, list):
        return []
    return [str(x).strip() for x in value if str(x).strip()]


def _plain_tags(raw):
    return [x.strip() for x in str(raw or "").split(";") if x.strip()]


def _merge_tags(current, legacy, service, external_url):
    out = []
    for tag in [*current, *legacy]:
        if tag and tag not in out:
            out.append(tag)
    url = str(external_url or "").strip()
    if url:
        prefix = {
            "spotify": "spotify_url=",
            "youtube_music": "youtube_music_url=",
            "youtube": "youtube_url=",
        }.get(service)
        if prefix:
            tag = prefix + url
            if tag not in out:
                out.append(tag)
    return out


def _run_playlist_tags_migration():
    from app import get_connection

    conn = get_connection()
    try:
        columns = [row[1] for row in conn.execute("PRAGMA table_info(playlist)").fetchall()]
        if "playlist_tags" not in columns:
            conn.execute("ALTER TABLE playlist ADD COLUMN playlist_tags TEXT NOT NULL DEFAULT ''")

        rows = conn.execute(
            "SELECT playlist_id, service, tags, playlist_tags, external_url FROM playlist ORDER BY playlist_id"
        ).fetchall()
        changed = 0
        for playlist_id, service, raw_old, raw_new, external_url in rows:
            merged = _merge_tags(
                _plain_tags(raw_new),
                _old_tags(raw_old),
                service,
                external_url,
            )
            normalized = "; ".join(merged)
            if normalized != str(raw_new or "").strip():
                conn.execute(
                    "UPDATE playlist SET playlist_tags=? WHERE playlist_id=?",
                    (normalized, playlist_id),
                )
                changed += 1
        conn.commit()

        verify = conn.execute(
            "SELECT playlist_id, service, tags, playlist_tags, external_url FROM playlist ORDER BY playlist_id"
        ).fetchall()
        problems = []
        for playlist_id, service, raw_old, raw_new, external_url in verify:
            new_tags = _plain_tags(raw_new)
            missing = [tag for tag in _old_tags(raw_old) if tag not in new_tags]
            url = str(external_url or "").strip()
            if url:
                prefix = {
                    "spotify": "spotify_url=",
                    "youtube_music": "youtube_music_url=",
                    "youtube": "youtube_url=",
                }.get(service)
                if prefix and prefix + url not in new_tags:
                    missing.append(prefix + url)
            if missing:
                problems.append((playlist_id, missing))

        if problems:
            raise RuntimeError("playlist_tags verification failed: " + repr(problems))

        print(
            f"PLAYLIST_TAGS_MIGRATION_OK playlists={len(verify)} changed={changed}",
            flush=True,
        )
        for playlist_id, _service, _old, plain, _url in verify:
            print(f"PLAYLIST_TAGS {playlist_id} :: {plain}", flush=True)
    finally:
        conn.close()


def when_ready(server):
    threading.Thread(
        target=_run_playlist_tags_migration,
        name="playlist-tags-legacy-to-current-once",
        daemon=True,
    ).start()
