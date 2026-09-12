#!/usr/bin/env python3

from pathlib import Path

COMMAND_FILE = Path('.github/sol-data/supabase-single-insert.sql')


def main():
    sql = COMMAND_FILE.read_text(encoding='utf-8').strip()
    if not sql.upper().startswith('INSERT INTO '):
        raise SystemExit('Expected exactly one INSERT INTO statement')
    print('VALID_INSERT')


if __name__ == '__main__':
    main()
