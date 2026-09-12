import os
from pathlib import Path

import psycopg

SQL_PATH = Path('.github/sol-data/supabase-single-insert.sql')

sql = SQL_PATH.read_text(encoding='utf-8').strip()
if not sql.lower().startswith('insert '):
    raise SystemExit('ERROR: only one INSERT statement is allowed')

# Count semicolons only outside SQL string literals.
in_string = False
statement_terminators = 0
i = 0
while i < len(sql):
    ch = sql[i]
    if ch == "'":
        if in_string and i + 1 < len(sql) and sql[i + 1] == "'":
            i += 2
            continue
        in_string = not in_string
    elif ch == ';' and not in_string:
        statement_terminators += 1
    i += 1

if in_string:
    raise SystemExit('ERROR: unterminated SQL string literal')
if statement_terminators > 1:
    raise SystemExit('ERROR: exactly one SQL statement is allowed')

password = os.environ['POSGRESPASS']

with psycopg.connect(
    host='db.uogsyhvkzirprxedurrh.supabase.co',
    port=5432,
    dbname='postgres',
    user='postgres',
    password=password,
    sslmode='require',
    autocommit=True,
) as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        print(f'INSERT_OK rowcount={cur.rowcount}')
