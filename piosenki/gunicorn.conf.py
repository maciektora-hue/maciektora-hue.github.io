import json
import os
from pathlib import Path


def when_ready(server):
    if os.environ.get("SOL_DRYRUN_ISLAND_PLAYLISTS") != "1":
        return

    from app import get_connection
    from island_playlist_import import import_island_playlists

    root = Path(__file__).resolve().parent.parent / "dane-robocze" / "csv-tsv" / "piosenki"
    conn = get_connection()
    try:
        result = import_island_playlists(conn, root, dry_run=True)
        print("ISLAND_PLAYLIST_IMPORT_DRY_RUN " + json.dumps(result, ensure_ascii=False, sort_keys=True), flush=True)
    finally:
        conn.close()
