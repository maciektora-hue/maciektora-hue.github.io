import os

import libsql


def on_starting(server):
    if os.environ.get("MIGRATE_EXTERNAL_TRACK") != "1":
        return

    url = os.environ.get("TURSO_DATABASE_URL", "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io")
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    conn = libsql.connect(database=url, auth_token=token)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS external_track (
                external_track_pk INTEGER PRIMARY KEY,
                service TEXT NOT NULL,
                external_track_id TEXT NOT NULL,
                title TEXT,
                artist TEXT,
                album TEXT,
                CHECK (service IN ('spotify', 'youtube_music', 'youtube')),
                UNIQUE (service, external_track_id)
            )
        """)
        conn.commit()
        cols = conn.execute("PRAGMA table_info(external_track)").fetchall()
        count = conn.execute("SELECT COUNT(*) FROM external_track").fetchone()[0]
        print(f"EXTERNAL_TRACK_MIGRATION_OK columns={len(cols)} rows={count}", flush=True)
    finally:
        conn.close()
