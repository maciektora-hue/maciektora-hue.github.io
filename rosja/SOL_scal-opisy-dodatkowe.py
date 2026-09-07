import csv
from pathlib import Path

MASTER = Path('rosja/SOL_mapa-sekcji-i-anchorow-rosja.tsv')
OUT_BEZ_A1 = Path('rosja/SOL_mapa-sekcji-z-opisami-bez-A1.tsv')
OUT_ALL = Path('rosja/SOL_mapa-sekcji-z-opisami.tsv')
EXTRA_GLOB = 'SOL_opisy-sekcji-*.tsv'

with MASTER.open('r', encoding='utf-8', newline='') as f:
    master = list(csv.DictReader(f, delimiter='\t'))

extra = {}
for path in sorted(Path('rosja').glob(EXTRA_GLOB)):
    with path.open('r', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            key = (row['dokument_kod'], row['anchor'])
            if key in extra:
                raise SystemExit(f'STOP: duplikat opisu w plikach dodatkowych: {key}')
            extra[key] = row['opis']

master_keys = {(row['dokument_kod'], row['anchor']) for row in master}
unknown = set(extra) - master_keys
if unknown:
    raise SystemExit(f'STOP: opis bez odpowiadającej sekcji w master mapie: {sorted(unknown)}')

fields = list(master[0].keys()) + ['opis']


def build(exclude_a1=False):
    seen = set()
    out = []
    for row in master:
        if exclude_a1 and row['dokument_kod'] == 'A1':
            continue
        key = (row['dokument_kod'], row['anchor'])
        if key not in extra:
            continue
        if key in seen:
            raise SystemExit(f'STOP: duplikat klucza w mapie źródłowej: {key}')
        seen.add(key)
        r = dict(row)
        r['opis'] = extra[key]
        out.append(r)
    return out


def write(path, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


bez_a1 = build(exclude_a1=True)
all_rows = build(exclude_a1=False)
write(OUT_BEZ_A1, bez_a1)
write(OUT_ALL, all_rows)

print(f'OK: mapa bez A1 ma {len(bez_a1)} opisanych sekcji')
print(f'OK: pełna mapa ma {len(all_rows)} opisanych sekcji')
