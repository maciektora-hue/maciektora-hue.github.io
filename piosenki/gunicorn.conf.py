import json
import threading
from pathlib import Path


def _run_import():
    from app import get_connection
    from island_playlist_import import import_island_playlists

    root = Path(__file__).resolve().parent.parent / "dane-robocze" / "csv-tsv" / "piosenki"
    conn = get_connection()
    try:
        result = import_island_playlists(conn, root, dry_run=False)
        print("ISLAND_PLAYLIST_IMPORT_OK " + json.dumps(result, ensure_ascii=False, sort_keys=True), flush=True)
    except Exception as exc:
        print("ISLAND_PLAYLIST_IMPORT_ERROR " + repr(exc), flush=True)
        raise
    finally:
        conn.close()


def when_ready(server):
    threading.Thread(target=_run_import, name="island-playlist-import-once", daemon=True).start()
