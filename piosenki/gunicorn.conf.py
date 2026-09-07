def post_fork(server, worker):
    import os
    import libsql

    from content_structure_fix import ensure_content_structure_v2_safe

    database_url = os.environ.get(
        "TURSO_DATABASE_URL",
        "libsql://happy-hue-octopus-maciek-hue.aws-eu-west-1.turso.io",
    )
    token = os.environ.get("TURSO_ADMIN_TOKEN")
    if not token:
        raise RuntimeError("Brak TURSO_ADMIN_TOKEN")

    conn = libsql.connect(database=database_url, auth_token=token)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        state = ensure_content_structure_v2_safe(conn)
        print(f"CONTENT A1 STRUCTURE: {state}", flush=True)
    finally:
        conn.close()
