from flask import jsonify

from app import app, get_connection, fetch_rows


@app.get("/api/playlisty")
def api_playlisty():
    """Read-only dane do viewera playlist. Bez heurystyk i bez modyfikacji SQL."""
    conn = None
    try:
        conn = get_connection()
        playlists = fetch_rows(conn, """
            SELECT
                p.playlist_id,
                p.playlist_series_id,
                p.service,
                p.name,
                p.external_playlist_id,
                p.external_url,
                p.source_file,
                p.exported_at,
                p.imported_at,
                p.tags,
                COUNT(i.position) AS item_count,
                SUM(CASE WHEN i.utwu_id IS NOT NULL THEN 1 ELSE 0 END) AS mapped_count
            FROM playlist AS p
            LEFT JOIN playlist_item AS i ON i.playlist_id = p.playlist_id
            GROUP BY
                p.playlist_id, p.playlist_series_id, p.service, p.name,
                p.external_playlist_id, p.external_url, p.source_file,
                p.exported_at, p.imported_at, p.tags
            ORDER BY p.name, p.playlist_id
        """, [
            "playlist_id", "playlist_series_id", "service", "name",
            "external_playlist_id", "external_url", "source_file",
            "exported_at", "imported_at", "tags", "item_count", "mapped_count"
        ])

        items = fetch_rows(conn, """
            SELECT
                i.playlist_id,
                i.position,
                i.utwu_id,
                i.external_track_id,
                i.source_name,
                i.source_artist,
                i.source_album,
                m.title_original,
                m.artist_original,
                m.album_original,
                m.spotify_id,
                m.youtube_video_id
            FROM playlist_item AS i
            LEFT JOIN middle_end AS m ON m.utwu_id = i.utwu_id
            ORDER BY i.playlist_id, i.position
        """, [
            "playlist_id", "position", "utwu_id", "external_track_id",
            "source_name", "source_artist", "source_album",
            "title_original", "artist_original", "album_original",
            "spotify_id", "youtube_video_id"
        ])

        utwory = fetch_rows(conn, """
            SELECT
                utwu_id,
                title_original,
                artist_original,
                album_original,
                spotify_id,
                youtube_video_id
            FROM middle_end
            ORDER BY artist_original, title_original, utwu_id
        """, [
            "utwu_id", "title_original", "artist_original", "album_original",
            "spotify_id", "youtube_video_id"
        ])

        return jsonify(playlists=playlists, items=items, utwory=utwory), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()
