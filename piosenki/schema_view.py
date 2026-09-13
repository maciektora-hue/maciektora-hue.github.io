def _quote_ident(name):
    return '"' + name.replace('"', '""') + '"'


def _fetch_one_int(conn, sql, params=()):
    row = conn.execute(sql, params).fetchone()
    if not row:
        return 0
    return int(row[0] or 0)


def build_schema_snapshot(conn):
    tables = [
        row[0]
        for row in conn.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_type = 'BASE TABLE'
            ORDER BY table_name
            """
        ).fetchall()
    ]

    database_size = _fetch_one_int(conn, "SELECT pg_database_size(current_database())")

    result = []
    total_rows = 0

    for table_name in tables:
        ident = _quote_ident(table_name)

        pk_positions = {
            col: pos
            for col, pos in conn.execute(
                """
                SELECT kcu.column_name, kcu.ordinal_position
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                  ON kcu.constraint_name = tc.constraint_name
                 AND kcu.table_schema = tc.table_schema
                WHERE tc.table_schema = 'public'
                  AND tc.table_name = %s
                  AND tc.constraint_type = 'PRIMARY KEY'
                """,
                (table_name,),
            ).fetchall()
        }

        columns = []
        for cid, name, col_type, notnull, default_value in conn.execute(
            """
            SELECT ordinal_position, column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = %s
            ORDER BY ordinal_position
            """,
            (table_name,),
        ).fetchall():
            columns.append({
                "cid": cid,
                "name": name,
                "type": col_type,
                "not_null": notnull == "NO",
                "default": default_value,
                "primary_key_position": pk_positions.get(name),
            })

        foreign_keys = []
        for fk_id, seq, from_col, ref_table, to_col, on_update, on_delete in conn.execute(
            """
            SELECT
                tc.constraint_name,
                kcu.ordinal_position,
                kcu.column_name,
                ccu.table_name,
                ccu.column_name,
                rc.update_rule,
                rc.delete_rule
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
              ON kcu.constraint_name = tc.constraint_name
             AND kcu.table_schema = tc.table_schema
            JOIN information_schema.constraint_column_usage ccu
              ON ccu.constraint_name = tc.constraint_name
             AND ccu.table_schema = tc.table_schema
            JOIN information_schema.referential_constraints rc
              ON rc.constraint_name = tc.constraint_name
             AND rc.constraint_schema = tc.table_schema
            WHERE tc.table_schema = 'public'
              AND tc.table_name = %s
              AND tc.constraint_type = 'FOREIGN KEY'
            ORDER BY tc.constraint_name, kcu.ordinal_position
            """,
            (table_name,),
        ).fetchall():
            foreign_keys.append({
                "id": fk_id,
                "seq": seq,
                "from": from_col,
                "to_table": ref_table,
                "to": to_col,
                "on_update": on_update,
                "on_delete": on_delete,
                "match": None,
            })

        row_count = _fetch_one_int(conn, f"SELECT COUNT(*) FROM {ident}")
        total_rows += row_count

        size_bytes = _fetch_one_int(
            conn, "SELECT pg_total_relation_size(%s)", (f'"{table_name}"',)
        )

        result.append({
            "name": table_name,
            "row_count": row_count,
            "size_bytes": size_bytes,
            "columns": columns,
            "foreign_keys": foreign_keys,
        })

    return {
        "source": "live_supabase_postgres",
        "table_count": len(result),
        "total_rows": total_rows,
        "database": {
            "size_bytes": database_size,
        },
        "tables": result,
    }
