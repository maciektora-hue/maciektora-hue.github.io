import os
import sys
from pathlib import Path

import psycopg

SQL_PATH = Path('.github/sol-data/supabase-single-insert.sql')

sql = SQL_PATH.read_text(encoding='utf-8').strip()
if not sql.lower().startswith('insert '):
    raise SystemExit('ERROR: only one INSERT statement is allowed')

body = sql[:-1].strip() if sql.endswith(';') else sql
if ';' in body:
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
