def _quote_ident(name):
    return '"' + name.replace('"', '""') + '"'


def _fetch_one_int(conn, sql):
    row = conn.execute(sql).fetchone()
    if not row:
        return 0
    return int(row[0] or 0)


def build_schema_snapshot(conn):
    tables = [
        row[0]
        for row in conn.execute(
            """
            SELECT name
            FROM sqlite_schema
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
            ORDER BY name
            """
        ).fetchall()
    ]

    page_size = _fetch_one_int(conn, "PRAGMA page_size")
    page_count = _fetch_one_int(conn, "PRAGMA page_count")

    dbstat_available = True
    try:
        conn.execute("SELECT 1 FROM dbstat LIMIT 1").fetchone()
    except Exception:
        dbstat_available = False

    result = []
    total_rows = 0

    for table_name in tables:
        ident = _quote_ident(table_name)

        columns = []
        for cid, name, col_type, notnull, default_value, pk in conn.execute(
            f"PRAGMA table_info({ident})"
        ).fetchall():
            columns.append({
                "cid": cid,
                "name": name,
                "type": col_type,
                "not_null": bool(notnull),
                "default": default_value,
                "primary_key_position": pk,
            })

        foreign_keys = []
        for row in conn.execute(f"PRAGMA foreign_key_list({ident})").fetchall():
            fk_id, seq, ref_table, from_col, to_col, on_update, on_delete, match = row[:8]
            foreign_keys.append({
                "id": fk_id,
                "seq": seq,
                "from": from_col,
                "to_table": ref_table,
                "to": to_col,
                "on_update": on_update,
                "on_delete": on_delete,
                "match": match,
            })

        row_count = _fetch_one_int(conn, f"SELECT COUNT(*) FROM {ident}")
        total_rows += row_count

        size_bytes = None
        if dbstat_available:
            try:
                size_row = conn.execute(
                    "SELECT COALESCE(SUM(pgsize), 0) FROM dbstat WHERE name = ?",
                    (table_name,),
                ).fetchone()
                size_bytes = int(size_row[0] or 0) if size_row else 0
            except Exception:
                size_bytes = None

        result.append({
            "name": table_name,
            "row_count": row_count,
            "size_bytes": size_bytes,
            "columns": columns,
            "foreign_keys": foreign_keys,
        })

    return {
        "source": "live_turso_sqlite",
        "table_count": len(result),
        "total_rows": total_rows,
        "database": {
            "page_size": page_size,
            "page_count": page_count,
            "size_bytes": page_size * page_count,
            "per_table_size_source": "dbstat" if dbstat_available else None,
        },
        "tables": result,
    }
