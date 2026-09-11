import os

import libsql


def on_starting(server):
    if os.environ.get("MIGRATE_EXTERNAL_TRACK_UTWU") != "1":
        return

    url = os.environ.get("TURSO_DATABASE_URL", "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io")
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    conn = libsql.connect(database=url, auth_token=token)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS external_track_utwu (
                external_track_pk INTEGER NOT NULL
                    REFERENCES external_track(external_track_pk)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE,
                utwu_id TEXT NOT NULL
                    REFERENCES middle_end(utwu_id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                PRIMARY KEY (external_track_pk, utwu_id)
            )
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_external_track_utwu_utwu_id
            ON external_track_utwu(utwu_id)
        """)
        fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
        if fk_errors:
            raise RuntimeError(f"FK errors: {fk_errors}")
        conn.commit()
        cols = conn.execute("PRAGMA table_info(external_track_utwu)").fetchall()
        count = conn.execute("SELECT COUNT(*) FROM external_track_utwu").fetchone()[0]
        print(f"EXTERNAL_TRACK_UTWU_MIGRATION_OK columns={len(cols)} rows={count}", flush=True)
    finally:
        conn.close()
