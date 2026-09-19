#!/usr/bin/env python3
from pathlib import Path
import re
import shutil

SRC = Path('walkaosql/rozpakowane/happy-hue-octopus-backup.sql.tsv')
OUT = Path('walkaosql/tabele_insert')


def statements(text: str):
    start = 0
    i = 0
    n = len(text)
    quote = None
    line_comment = False
    block_comment = False

    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ''

        if line_comment:
            if c == '\n':
                line_comment = False
            i += 1
            continue

        if block_comment:
            if c == '*' and nxt == '/':
                block_comment = False
                i += 2
            else:
                i += 1
            continue

        if quote:
            if quote == ']' and c == ']':
                quote = None
            elif c == quote:
                if i + 1 < n and text[i + 1] == quote and quote in ("'", '"', '`'):
                    i += 2
                    continue
                quote = None
            i += 1
            continue

        if c == '-' and nxt == '-':
            line_comment = True
            i += 2
            continue
        if c == '/' and nxt == '*':
            block_comment = True
            i += 2
            continue
        if c in ("'", '"', '`'):
            quote = c
            i += 1
            continue
        if c == '[':
            quote = ']'
            i += 1
            continue

        if c == ';':
            s = text[start:i + 1].strip()
            if s:
                yield s
            start = i + 1
        i += 1

    tail = text[start:].strip()
    if tail:
        yield tail


IDENT = r'(?:"[^"]+"|`[^`]+`|\[[^\]]+\]|[A-Za-z_][A-Za-z0-9_$]*)'
QUAL = rf'(?:{IDENT}\s*\.\s*)?({IDENT})'
INSERT_RE = re.compile(rf'^\s*INSERT\s+(?:OR\s+\w+\s+)?INTO\s+{QUAL}', re.I | re.S)


def clean_ident(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        raw = raw[1:-1]
    elif raw[:1] in ('"', '`') and raw[-1:] == raw[:1]:
        raw = raw[1:-1]
    return raw


def safe_name(name: str) -> str:
    s = re.sub(r'[^A-Za-z0-9._-]+', '_', name).strip('._')
    return s or 'unnamed_table'


if not SRC.exists():
    raise SystemExit(f'BRAK PLIKU: {SRC}')

text = SRC.read_text(encoding='utf-8-sig', errors='strict')

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

files = {}
counts = {}

for stmt in statements(text):
    m = INSERT_RE.search(stmt)
    if not m:
        continue

    table = clean_ident(m.group(1))
    path = OUT / f'{safe_name(table)}.sql'

    if table not in files:
        files[table] = path
        counts[table] = 0
        path.write_text('', encoding='utf-8')

    with path.open('a', encoding='utf-8', newline='\n') as f:
        f.write(stmt)
        f.write('\n\n')
    counts[table] += 1

report = OUT / '_RAPORT.txt'
with report.open('w', encoding='utf-8', newline='\n') as f:
    f.write(f'Źródło: {SRC}\n')
    f.write('Tryb: tylko INSERT\n')
    f.write(f'Liczba tabel z INSERT: {len(files)}\n\n')
    for table in sorted(files, key=str.lower):
        f.write(f'{table}\t{counts[table]} INSERT\t{files[table].name}\n')

print(f'GOTOWE: {len(files)} tabel z INSERT -> {OUT}')
for table in sorted(files, key=str.lower):
    print(f'{table}: {counts[table]} INSERT -> {files[table]}')
