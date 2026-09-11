import os
import sqlite3
from pathlib import Path

import libsql


EXPECTED_OLD_COLUMNS = [
    "playlist_id",
    "service",
    "name",
    "external_playlist_id",
    "external_url",
    "source_file",
    "imported_at",
]

REQUIRED_NEW_COLUMNS = {
    "playlist_id",
    "playlist_series_id",
    "service",
    "name",
    "external_playlist_id",
    "external_url",
    "source_file",
    "exported_at",
    "imported_at",
    "tags",
}


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


def _playlist_columns(conn):
    return [row[1] for row in conn.execute("PRAGMA table_info(playlist)").fetchall()]


def on_starting(server):
    if os.environ.get("RUN_PLAYLIST_METADATA_MIGRATION") != "1":
        return

    database_url = os.environ.get(
        "TURSO_DATABASE_URL",
        "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io",
    )
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    migration = Path(__file__).parent / "migrations" / "2026-09-11-playlist-metadata.sql"
    sql_text = migration.read_text(encoding="utf-8")

    conn = libsql.connect(database=database_url, auth_token=token)
    try:
        columns_before = _playlist_columns(conn)
        playlists_before = conn.execute("SELECT COUNT(*) FROM playlist").fetchone()[0]
        items_before = conn.execute("SELECT COUNT(*) FROM playlist_item").fetchone()[0]

        if REQUIRED_NEW_COLUMNS.issubset(set(columns_before)):
            print(
                f"PLAYLIST_METADATA_MIGRATION_ALREADY_DONE playlists={playlists_before} items={items_before}",
                flush=True,
            )
            return

        if columns_before != EXPECTED_OLD_COLUMNS:
            raise RuntimeError(f"Nieoczekiwany schemat playlist przed migracja: {columns_before}")

        for stmt in _statements(sql_text):
            upper = stmt.upper()
            if upper.startswith("COMMIT"):
                playlists_after = conn.execute("SELECT COUNT(*) FROM playlist").fetchone()[0]
                items_after = conn.execute("SELECT COUNT(*) FROM playlist_item").fetchone()[0]
                fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()

                if playlists_after != playlists_before:
                    raise RuntimeError(
                        f"Liczba playlist zmienila sie: {playlists_before} -> {playlists_after}"
                    )
                if items_after != items_before:
                    raise RuntimeError(
                        f"Liczba playlist_item zmienila sie: {items_before} -> {items_after}"
                    )
                if fk_errors:
                    raise RuntimeError(f"foreign_key_check: {fk_errors[:20]}")

            conn.execute(stmt)

        columns_after = _playlist_columns(conn)
        if not REQUIRED_NEW_COLUMNS.issubset(set(columns_after)):
            raise RuntimeError(f"Migracja nie utworzyla oczekiwanego schematu: {columns_after}")

        playlists_after = conn.execute("SELECT COUNT(*) FROM playlist").fetchone()[0]
        items_after = conn.execute("SELECT COUNT(*) FROM playlist_item").fetchone()[0]
        print(
            "PLAYLIST_METADATA_MIGRATION_OK "
            f"playlists={playlists_after} items={items_after} columns={','.join(columns_after)}",
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
