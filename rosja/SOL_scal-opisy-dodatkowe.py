import csv
import io
import subprocess
from pathlib import Path

MASTER = Path('rosja/SOL_mapa-sekcji-i-anchorow-rosja.tsv')
OUT_BEZ_A1 = Path('rosja/SOL_mapa-sekcji-z-opisami-bez-A1.tsv')
OUT_ALL = Path('rosja/SOL_mapa-sekcji-z-opisami.tsv')
EXTRA_GLOB = 'SOL_opisy-sekcji-*.tsv'

# Ostatnia kompletna mapa sprzed przebudowy scalania pod A1.
# Z niej jednorazowo odzyskujemy A2 i A3, które wcześniej nie miały
# własnych plików SOL_opisy-sekcji-A2/A3.tsv.
RECOVERY_REF = '4c0b8ab3ff58870fef0aef5e23ca669e20905ea2'
RECOVERY_PATH = 'rosja/SOL_mapa-sekcji-z-opisami-bez-A1.tsv'
RECOVERY_CODES = {'A2', 'A3'}

EXPECTED_MASTER = 620
EXPECTED_BEZ_A1 = 596
EXPECTED_ALL = 620

with MASTER.open('r', encoding='utf-8', newline='') as f:
    master = list(csv.DictReader(f, delimiter='\t'))

if len(master) != EXPECTED_MASTER:
    raise SystemExit(
        f'STOP: master ma {len(master)} sekcji, oczekiwano {EXPECTED_MASTER}'
    )

master_keys_list = [(row['dokument_kod'], row['anchor']) for row in master]
master_keys = set(master_keys_list)
if len(master_keys) != len(master_keys_list):
    raise SystemExit('STOP: duplikat klucza (dokument_kod, anchor) w master mapie')

extra = {}
for path in sorted(Path('rosja').glob(EXTRA_GLOB)):
    with path.open('r', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            key = (row['dokument_kod'], row['anchor'])
            opis = (row.get('opis') or '').strip()
            if not opis:
                raise SystemExit(f'STOP: pusty opis w {path}: {key}')
            if key in extra:
                raise SystemExit(f'STOP: duplikat opisu w plikach dodatkowych: {key}')
            extra[key] = opis

# A2 i A3 powstały wcześniej bez osobnych plików opisów. Jeśli nadal ich
# brakuje, odzyskaj je z kompletnej historycznej mapy i utwórz pliki źródłowe.
missing_recovery_codes = {
    code for code in RECOVERY_CODES
    if not any(k[0] == code for k in extra)
}

if missing_recovery_codes:
    try:
        recovered_text = subprocess.check_output(
            ['git', 'show', f'{RECOVERY_REF}:{RECOVERY_PATH}'],
            text=True,
            encoding='utf-8',
        )
    except subprocess.CalledProcessError as e:
        raise SystemExit(f'STOP: nie udało się odzyskać A2/A3 z {RECOVERY_REF}: {e}')

    recovered_rows = list(csv.DictReader(io.StringIO(recovered_text), delimiter='\t'))
    recovered_by_code = {code: [] for code in missing_recovery_codes}

    for row in recovered_rows:
        code = row['dokument_kod']
        if code not in missing_recovery_codes:
            continue
        key = (code, row['anchor'])
        opis = (row.get('opis') or '').strip()
        if not opis:
            raise SystemExit(f'STOP: pusty odzyskany opis: {key}')
        if key in extra:
            raise SystemExit(f'STOP: konflikt podczas odzysku opisu: {key}')
        extra[key] = opis
        recovered_by_code[code].append({
            'dokument_kod': code,
            'anchor': row['anchor'],
            'opis': opis,
        })

    for code, rows in recovered_by_code.items():
        if not rows:
            raise SystemExit(f'STOP: brak odzyskanych opisów dla {code}')
        out_path = Path(f'rosja/SOL_opisy-sekcji-{code}.tsv')
        with out_path.open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(
                f,
                fieldnames=['dokument_kod', 'anchor', 'opis'],
                delimiter='\t',
                lineterminator='\n',
            )
            w.writeheader()
            w.writerows(rows)
        print(f'OK: odzyskano {len(rows)} opisów {code} do {out_path}')

unknown = set(extra) - master_keys
if unknown:
    raise SystemExit(f'STOP: opis bez odpowiadającej sekcji w master mapie: {sorted(unknown)}')

missing = master_keys - set(extra)
if missing:
    raise SystemExit(
        f'STOP: brakuje {len(missing)} opisów dla sekcji z master mapy: {sorted(missing)}'
    )

fields = list(master[0].keys()) + ['opis']


def build(exclude_a1=False):
    seen = set()
    out = []
    for row in master:
        if exclude_a1 and row['dokument_kod'] == 'A1':
            continue
        key = (row['dokument_kod'], row['anchor'])
        if key not in extra:
            raise SystemExit(f'STOP: brak opisu podczas budowy mapy: {key}')
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

if len(bez_a1) != EXPECTED_BEZ_A1:
    raise SystemExit(
        f'STOP: mapa bez A1 ma {len(bez_a1)} opisów, oczekiwano {EXPECTED_BEZ_A1}'
    )
if len(all_rows) != EXPECTED_ALL:
    raise SystemExit(
        f'STOP: pełna mapa ma {len(all_rows)} opisów, oczekiwano {EXPECTED_ALL}'
    )

write(OUT_BEZ_A1, bez_a1)
write(OUT_ALL, all_rows)

print(f'OK: master ma {len(master)} unikalnych sekcji')
print('OK: wszystkie opisy są niepuste i odpowiadają dokładnie sekcjom z master mapy')
print(f'OK: mapa bez A1 ma {len(bez_a1)} opisanych sekcji')
print(f'OK: pełna mapa ma {len(all_rows)} opisanych sekcji')
