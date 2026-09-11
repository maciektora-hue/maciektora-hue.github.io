import json
import threading
from pathlib import Path

BRIDGES = [
    {"source_file": "glebia-ruch.xlsx", "playlist_id": "spotify:most-glebia-ruch:2026-09-11", "playlist_series_id": "spotify:most-glebia-ruch", "name": "Most Głębia-Ruch", "external_playlist_id": None, "external_url": None},
    {"source_file": "glebia-swiatlo.xlsx", "playlist_id": "spotify:most-glebia-swiatlo:2026-09-11", "playlist_series_id": "spotify:most-glebia-swiatlo", "name": "Most Głębia-Światło", "external_playlist_id": None, "external_url": None},
    {"source_file": "swiatlo-ruch.xlsx", "playlist_id": "spotify:most-swiatlo-ruch:2026-09-11", "playlist_series_id": "spotify:most-swiatlo-ruch", "name": "Most Światło-Ruch", "external_playlist_id": None, "external_url": None},
]


def _run():
    from app import get_connection
    import island_playlist_import as importer
    root = Path(__file__).resolve().parent.parent / "dane-robocze" / "csv-tsv" / "piosenki"
    conn = get_connection()
    original = importer.PLAYLISTS
    try:
        importer.PLAYLISTS = BRIDGES
        result = importer.import_island_playlists(conn, root, dry_run=True)
        print("BRIDGE_PLAYLIST_IMPORT_DRY_RUN " + json.dumps(result, ensure_ascii=False, sort_keys=True), flush=True)
    except Exception as exc:
        print("BRIDGE_PLAYLIST_IMPORT_DRY_RUN_ERROR " + repr(exc), flush=True)
        raise
    finally:
        importer.PLAYLISTS = original
        conn.close()


def when_ready(server):
    threading.Thread(target=_run, name="bridge-playlist-dry-run-once", daemon=True).start()
