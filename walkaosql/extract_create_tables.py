#!/usr/bin/env python3
from pathlib import Path

SRC = Path('walkaosql/tabele')
OUT = Path('walkaosql/create_tables.sql')


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


creates = []
for path in sorted(SRC.glob('*.sql')):
    if path.name.startswith('_'):
        continue
    text = path.read_text(encoding='utf-8-sig')
    for stmt in statements(text):
        head = stmt.lstrip().upper()
        if head.startswith('CREATE TABLE'):
            creates.append(stmt)

OUT.write_text('\n\n'.join(creates) + '\n', encoding='utf-8', newline='\n')
print(f'GOTOWE: {len(creates)} CREATE TABLE -> {OUT}')
