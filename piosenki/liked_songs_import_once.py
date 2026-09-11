from __future__ import annotations

import hmac
import os
from pathlib import Path

from flask import jsonify, request

from app import app, get_connection
from playlist_importer import import_playlist_xlsx


@app.get("/internal/liked-songs-20260911")
def liked_songs_import_once():
    expected = os.environ.get("SOL_LIKED_SONGS_NONCE") or ""
    supplied = request.args.get("nonce", "")
    if not expected or not hmac.compare_digest(expected, supplied):
        return jsonify(status="not_found"), 404

    if os.environ.get("SOL_IMPORT_LIKED_SONGS_20260911") != "apply":
        return jsonify(status="disabled"), 409

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
        return jsonify(status="ok", summary=summary), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        conn.close()
