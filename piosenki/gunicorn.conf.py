import json
import os
import threading
from pathlib import Path


def _run_liked_songs_import():
    from app import get_connection
    from playlist_importer import import_playlist_xlsx

    source = (
        Path(__file__).resolve().parent.parent
        / "dane-robocze"
        / "playlistyspotifybestof"
        / "Liked songs spotify z dnia 2026-09-11.xlsx"
    )
    conn = get_connection()
    try:
        summary = import_playlist_xlsx(
            conn,
            source_path=source,
            playlist_id="spotify:liked-songs:2026-09-11",
            playlist_series_id="spotify:liked-songs",
            service="spotify",
            name="Liked Songs",
            exported_at="2026-09-11",
            tags=["owner:maciek-tora"],
            dry_run=False,
        )
        print(
            "LIKED_SONGS_IMPORT_OK "
            + json.dumps(summary, ensure_ascii=False, sort_keys=True),
            flush=True,
        )
    except Exception as exc:
        print(f"LIKED_SONGS_IMPORT_ERROR {type(exc).__name__}: {exc}", flush=True)
    finally:
        conn.close()


def when_ready(server):
    if os.environ.get("SOL_IMPORT_LIKED_SONGS_20260911") != "1":
        return
    threading.Thread(
        target=_run_liked_songs_import,
        name="liked-songs-import-20260911",
        daemon=True,
    ).start()
