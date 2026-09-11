import json
import os
from pathlib import Path


def when_ready(server):
    mode = os.environ.get("SOL_IMPORT_LIKED_SONGS_20260911")
    if mode not in {"dry-run", "apply"}:
        return

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
            dry_run=(mode == "dry-run"),
        )
        marker = "LIKED_SONGS_IMPORT_DRY_RUN" if mode == "dry-run" else "LIKED_SONGS_IMPORT_OK"
        print(marker + " " + json.dumps(summary, ensure_ascii=False, sort_keys=True), flush=True)
    finally:
        conn.close()
