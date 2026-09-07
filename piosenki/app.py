import os

import libsql
from flask import Flask, jsonify, render_template
from flask_cors import CORS

from statystyki import build_direction_page, build_relations_page, build_time_page, load_model


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://maciektora-hue.github.io"]}})

TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL", "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io")
TURSO_ADMIN_TOKEN = os.environ.get("TURSO_ADMIN_TOKEN")


def get_connection():
    if not TURSO_ADMIN_TOKEN:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")
    return libsql.connect(database=TURSO_DATABASE_URL, auth_token=TURSO_ADMIN_TOKEN)


def fetch_rows(conn, sql, columns):
    rows = conn.execute(sql).fetchall()
    return [dict(zip(columns, row)) for row in rows]


def load_stats_model():
    conn = get_connection()
    try:
        return load_model(conn)
    finally:
        conn.close()


@app.get("/health")
def health():
    try:
        conn = get_connection()
        value = conn.execute("SELECT 1").fetchone()[0]
        conn.close()
        return jsonify(status="ok", database=value), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500


@app.get("/api/piosenki")
def api_piosenki():
    conn = None
    try:
        conn = get_connection()
        data = {
            "middle_end": fetch_rows(conn, """
                SELECT utwu_id, lyrics_id, spotify_id, spotify_order, title_original,
                       title_normalized, title_parsed, artist_original, artist_normalized,
                       artist_parsed, album_original, match_status, match_candidates,
                       match_note, lyrics_status
                FROM middle_end
                ORDER BY spotify_order, utwu_id
                """, ["utwu_id", "lyrics_id", "spotify_id", "spotify_order", "title_original", "title_normalized", "title_parsed", "artist_original", "artist_normalized", "artist_parsed", "album_original", "match_status", "match_candidates", "match_note", "lyrics_status"]),
            "tag_snapshots": fetch_rows(conn, "SELECT lyrics_id, tagged_at, tags FROM tag_snapshots ORDER BY tagged_at, lyrics_id", ["lyrics_id", "tagged_at", "tags"]),
            "tag_catalog": fetch_rows(conn, "SELECT tag, definition FROM tag_catalog ORDER BY tag", ["tag", "definition"]),
            "families": fetch_rows(conn, "SELECT family_name, label, color_hex, description, sort_order FROM families ORDER BY sort_order", ["family_name", "label", "color_hex", "description", "sort_order"]),
            "tag_groups": fetch_rows(conn, "SELECT group_name, label FROM tag_groups ORDER BY group_name", ["group_name", "label"]),
            "axes": fetch_rows(conn, "SELECT axis_name, label, description, family_name, sort_order FROM axes ORDER BY sort_order", ["axis_name", "label", "description", "family_name", "sort_order"]),
            "tag_group": fetch_rows(conn, "SELECT tag, group_name FROM tag_group ORDER BY tag, group_name", ["tag", "group_name"]),
            "tag_axis": fetch_rows(conn, "SELECT tag, axis_name FROM tag_axis ORDER BY tag, axis_name", ["tag", "axis_name"]),
            "lyrics": fetch_rows(conn, "SELECT lyrics_id FROM lyrics ORDER BY lyrics_id", ["lyrics_id"]),
        }
        return jsonify(data), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


@app.get("/statystyki/")
def statystyki_index():
    return render_template("statystyki-index.html")


@app.get("/statystyki/czas")
def statystyki_czas():
    return render_template("czas.html", data=build_time_page(load_stats_model(), chunk_size=80))


@app.get("/statystyki/kierunek")
def statystyki_kierunek():
    return render_template("kierunek.html", data=build_direction_page(load_stats_model()))


@app.get("/statystyki/relacje")
def statystyki_relacje():
    return render_template("relacje.html", data=build_relations_page(load_stats_model(), chunk_size=80))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
