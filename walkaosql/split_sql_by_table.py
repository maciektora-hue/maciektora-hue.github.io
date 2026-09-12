#!/usr/bin/env python3
from pathlib import Path
import re
import shutil

SRC = Path('walkaosql/rozpakowane/happy-hue-octopus-backup.sql.tsv')
OUT = Path('walkaosql/tabele')

# Rozdziela SQL po średnikach, ale nie tnie średników wewnątrz stringów/identyfikatorów/komentarzy.
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
                # SQL: podwojony apostrof/cudzysłów nie zamyka stringa/identyfikatora.
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

PATTERNS = [
    re.compile(rf'^\s*CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?{QUAL}', re.I | re.S),
    re.compile(rf'^\s*INSERT\s+(?:OR\s+\w+\s+)?INTO\s+{QUAL}', re.I | re.S),
    re.compile(rf'^\s*REPLACE\s+INTO\s+{QUAL}', re.I | re.S),
    re.compile(rf'^\s*ALTER\s+TABLE\s+{QUAL}', re.I | re.S),
    re.compile(rf'^\s*DROP\s+TABLE\s+(?:IF\s+EXISTS\s+)?{QUAL}', re.I | re.S),
    re.compile(rf'^\s*UPDATE\s+{QUAL}', re.I | re.S),
    re.compile(rf'^\s*DELETE\s+FROM\s+{QUAL}', re.I | re.S),
    re.compile(rf'^\s*CREATE\s+(?:UNIQUE\s+)?INDEX\s+.*?\s+ON\s+{QUAL}', re.I | re.S),
    re.compile(rf'^\s*CREATE\s+TRIGGER\s+.*?\s+ON\s+{QUAL}', re.I | re.S),
]

def clean_ident(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        raw = raw[1:-1]
    elif raw[:1] in ('"', '`') and raw[-1:] == raw[:1]:
        raw = raw[1:-1]
    return raw

def table_for(stmt: str):
    for p in PATTERNS:
        m = p.search(stmt)
        if m:
            return clean_ident(m.group(1))
    return None

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
unassigned = []

for stmt in statements(text):
    table = table_for(stmt)
    if table is None:
        # BEGIN/COMMIT/PRAGMA i inne globalne polecenia nie należą do konkretnej tabeli.
        unassigned.append(stmt)
        continue

    path = OUT / f'{safe_name(table)}.sql'
    if table not in files:
        files[table] = path
        path.write_text(f'-- tabela: {table}\nPRAGMA foreign_keys=OFF;\n\n', encoding='utf-8')
        counts[table] = 0

    with path.open('a', encoding='utf-8', newline='\n') as f:
        f.write(stmt)
        f.write('\n\n')
    counts[table] += 1

# Raport, żeby od razu było wiadomo, czy parser nie zrobił czegoś kreatywnego.
report = OUT / '_RAPORT.txt'
with report.open('w', encoding='utf-8', newline='\n') as f:
    f.write(f'Źródło: {SRC}\n')
    f.write(f'Liczba tabel: {len(files)}\n')
    f.write(f'Polecenia bez przypisania do tabeli: {len(unassigned)}\n\n')
    for table in sorted(files, key=str.lower):
        f.write(f'{table}\t{counts[table]} poleceń\t{files[table].name}\n')

# Zachowaj globalne polecenia osobno zamiast je gubić.
if unassigned:
    (OUT / '_GLOBAL.sql').write_text('\n\n'.join(unassigned) + '\n', encoding='utf-8')

print(f'GOTOWE: {len(files)} tabel -> {OUT}')
for table in sorted(files, key=str.lower):
    print(f'{table}: {counts[table]} poleceń -> {files[table]}')
