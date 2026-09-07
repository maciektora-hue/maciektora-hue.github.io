import os

import libsql
from flask import Flask, jsonify

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
