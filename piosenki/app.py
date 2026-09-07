import os

import libsql
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": ["https://maciektora-hue.github.io"],
        }
    },
)

TURSO_DATABASE_URL = os.environ.get(
    "TURSO_DATABASE_URL",
    "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io",
)
TURSO_ADMIN_TOKEN = os.environ.get("TURSO_ADMIN_TOKEN")


def get_connection():
    if not TURSO_ADMIN_TOKEN:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    return libsql.connect(
        database=TURSO_DATABASE_URL,
        auth_token=TURSO_ADMIN_TOKEN,
    )


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
        rows = conn.execute(
            """
            SELECT
                utwu_id,
                spotify_id,
                spotify_order,
                title_original,
                artist_original,
                album_original,
                lyrics_status
            FROM middle_end
            ORDER BY spotify_order, utwu_id
            """
        ).fetchall()

        data = [
            {
                "utwu_id": row[0],
                "spotify_id": row[1],
                "spotify_order": row[2],
                "title": row[3],
                "artist": row[4],
                "album": row[5],
                "lyrics_status": row[6],
            }
            for row in rows
        ]

        return jsonify(data), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
