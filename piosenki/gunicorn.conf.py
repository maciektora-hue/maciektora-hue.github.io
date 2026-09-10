import os
import sqlite3
from pathlib import Path

import libsql


def _statements(sql_text):
    buf = ""
    for line in sql_text.splitlines(keepends=True):
        if line.lstrip().startswith("--"):
            continue
        buf += line
        if sqlite3.complete_statement(buf):
            stmt = buf.strip()
            buf = ""
            if stmt:
                yield stmt
    if buf.strip():
        raise RuntimeError("Niepelne polecenie SQL na koncu migracji")


def on_starting(server):
    if os.environ.get("RUN_PLAYLIST_MIGRATION") != "1":
        return

    database_url = os.environ.get(
        "TURSO_DATABASE_URL",
        "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io",
    )
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    migration = Path(__file__).parent / "migrations" / "2026-09-10-playlists-spotify-bestof.sql"
    sql_text = migration.read_text(encoding="utf-8")

    conn = libsql.connect(database=database_url, auth_token=token)
    try:
        for stmt in _statements(sql_text):
            if stmt.upper().startswith("PRAGMA FOREIGN_KEYS"):
                conn.execute("PRAGMA foreign_keys = ON")
            else:
                conn.execute(stmt)

        playlists = conn.execute("SELECT COUNT(*) FROM playlist").fetchone()[0]
        items = conn.execute("SELECT COUNT(*) FROM playlist_item").fetchone()[0]
        mapped = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE utwu_id IS NOT NULL").fetchone()[0]
        unmapped = conn.execute("SELECT COUNT(*) FROM playlist_item WHERE utwu_id IS NULL").fetchone()[0]
        print(
            f"PLAYLIST_MIGRATION_OK playlists={playlists} items={items} mapped={mapped} unmapped={unmapped}",
            flush=True,
        )
    except Exception:
        try:
            conn.execute("ROLLBACK")
        except Exception:
            pass
        raise
    finally:
        conn.close()
