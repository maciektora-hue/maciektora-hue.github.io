import csv
from pathlib import Path

MASTER = Path('rosja/SOL_mapa-sekcji-i-anchorow-rosja.tsv')
OUT = Path('rosja/SOL_mapa-sekcji-z-opisami-bez-A1.tsv')
EXTRA_GLOB = 'SOL_opisy-sekcji-*.tsv'

with MASTER.open('r', encoding='utf-8', newline='') as f:
    master = list(csv.DictReader(f, delimiter='\t'))

existing = {}
if OUT.exists():
    with OUT.open('r', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            existing[(row['dokument_kod'], row['anchor'])] = row['opis']

extra = {}
for path in sorted(Path('rosja').glob(EXTRA_GLOB)):
    with path.open('r', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            key = (row['dokument_kod'], row['anchor'])
            if key in extra:
                raise SystemExit(f'STOP: duplikat opisu w plikach dodatkowych: {key}')
            extra[key] = row['opis']

all_desc = dict(existing)
all_desc.update(extra)

seen = set()
out = []
for row in master:
    if row['dokument_kod'] == 'A1':
        continue
    key = (row['dokument_kod'], row['anchor'])
    if key not in all_desc:
        continue
    if key in seen:
        raise SystemExit(f'STOP: duplikat klucza w mapie źródłowej: {key}')
    seen.add(key)
    r = dict(row)
    r['opis'] = all_desc[key]
    out.append(r)

unknown = set(all_desc) - seen
if unknown:
    raise SystemExit(f'STOP: opis bez odpowiadającej sekcji w master mapie: {sorted(unknown)}')

fields = list(master[0].keys()) + ['opis']
with OUT.open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    w.writeheader()
    w.writerows(out)

print(f'OK: wspólna mapa ma {len(out)} opisanych sekcji; A1 pominięte')
