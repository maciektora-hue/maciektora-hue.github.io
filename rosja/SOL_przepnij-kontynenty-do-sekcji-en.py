from pathlib import Path
import csv
import html

TARGET = Path('rosja/SOL_mapa-tematow-rozpad-rosji-EN-v01_00-2026-09-07.html')
META = Path('rosja/SOL_mapa-sekcji-z-opisami.tsv')

DIRS = {
    'A1': 'kolumbryna',
    'A2': 'gradually-suddenly',
    'A3': 'lista-celow',
    'A4': 'przejscie-na-hurt',
    'A5': 'audyt',
    'A6': 'zapas-kontra-strumien',
    'A7': 'jak-koncza-sie-panstwa',
    'D5': 'putin-cornered',
}

CONTINENTS = {
    'Ukraine as the designer of a system-level campaign': [
        ('A1', 'front-spirala-opl', 'Front and air-defence spiral'),
        ('A2', 'synteza-ewolucyjna', 'Campaign maturity thresholds'),
        ('A3', 'lista-celow', 'Chronology and target classes'),
        ('A4', 'skala-hurtu', 'Transition to system-level scale'),
        ('A6', 'uderzenie-2806', 'One wave, three facilities'),
    ],
    'The air defence → refineries → fuel → front spiral': [
        ('A1', 'front-spirala-opl', 'Front–air defence–refineries'),
        ('A2', 'front-olexandrivka-uzasadnienie', 'Effect on the front'),
        ('A6', 'offline-slack', 'Refinery slack exhausted'),
    ],
    'Fuel as a system, not a barrel count': [
        ('A2', 'rynek-paliw-siedem-brakow', 'Seven fuel-system failures'),
        ('A4', 'przerob-dno-dwudziestolecia', 'Refining at a twenty-year low'),
        ('A6', 'czesc-materia', 'Fuel and stock balance'),
        ('A6', 'cebula-transportowa', 'Transport bottlenecks'),
    ],
    'Crimea being turned from a peninsula into an island': [
        ('A2', 'trzy-wektory', 'Three supply routes'),
        ('A2', 'krym-wyspa', 'Crimea as a logistics island'),
        ('A3', 'okres-16', 'Crimea in the latest phase'),
    ],
    'Logistics as the anatomy of the state': [
        ('A1', 'infrastruktura-kolej-rury-samoloty', 'Rail, pipelines and aviation'),
        ('A2', 'rynek-kolej', 'Overloaded rail system'),
        ('A4', 'kolej', 'Rail traffic and staff'),
        ('A4', 'lotnictwo', 'Aviation cannibalisation'),
        ('A6', 'cebula-transportowa', 'Rolling stock and capacity'),
    ],
    'Energy and the Russian power grid': [
        ('A2', 'energetyka-siec-bez-redundancji', 'Grid without real redundancy'),
        ('A2', 'energetyka-ues-topologia', 'Topology of the seven UES zones'),
    ],
    'Climate as a participant in the war without a Telegram account': [
        ('A2', 'klimat-cascade-gradient', 'Climate → energy → logistics'),
        ('A2', 'klimat-kaskada-lato-2026', 'Heat, drought and cooling'),
    ],
    'The economy in the present continuous': [
        ('A1', 'budzet-nwf-hormuz', 'Budget, deficit and NWF'),
        ('A2', 'dwa-procesy-a-b', 'Front today, economy tomorrow'),
        ('A4', 'zapasc', 'Parallel economic degradation'),
        ('A4', 'budzet', 'Deficit above plan'),
    ],
    'Banking as the shortest fuse': [
        ('A4', 'bankowosc', 'Hidden banking crisis'),
        ('A4', 'dlaczego-najkrotszy', 'Why banking is the fastest fuse'),
    ],
    'People as a non-renewable resource': [
        ('A1', 'spoleczenstwo-na-krawedzi', 'Brain drain and staffing gaps'),
        ('A4', 'mobilizacja', 'Recruitment and mobilisation'),
        ('A4', 'zabralaby-specjalistow', 'Mobilisation drains specialists'),
    ],
    'China as patron and creditor, not ally': [
        ('A1', 'steelmanning-systemu', 'China as support for the system'),
        ('A4', 'chinski-substytut', 'The Chinese substitute'),
        ('A4', 'gaz-oba-kierunki', 'Gas: Europe versus China'),
        ('A7', 'hierarchia', 'Russia as China’s client'),
        ('A7', 'chiny-integralnosc', 'China’s integrity calculation'),
    ],
    'The war industry and broken chains of substitutability': [
        ('A2', 'po-tupolewa-do-sklepu', 'Irreplaceable platforms'),
        ('A2', 'uwaga-a50-precedens', 'The A-50 precedent'),
        ('A4', 'przemysl-domkniecia', 'Pressure on the war industry'),
        ('A4', 'waskie-gardlo', 'Parts matter more than halls'),
    ],
    'Russian adaptations that genuinely work': [
        ('A4', 'adaptacja', 'Adaptation under pressure'),
        ('A4', 'flota-cieni', 'The shadow fleet'),
    ],
    'Putin as a separate objective function': [
        ('A1', 'nie-pytanie-o-pieniadze', 'It is not about money'),
        ('D5', 'putin-cornered-animal', 'Putin as a cornered animal'),
        ('D5', 'scenariusze-desperacji', 'Desperation scenarios'),
        ('A6', 'rosja-rowna-putin', 'Russia ≠ Putin’s objective function'),
        ('A6', 'paradoks-zapedzenia', 'The cornering paradox'),
    ],
    'The elites and the moment when loyalty gets recalculated': [
        ('A1', 'elity-odlaczaja-sie-od-putina', 'When the elites detach'),
        ('D5', 'kiedy-elity-odlacza-sie-od-putina', 'The loyalty-cost threshold'),
        ('A6', 'zablokowana-elita', 'The blocked elite'),
        ('A7', 'spoiwo', 'Loyalty as calculation'),
    ],
    'How states actually end': [
        ('A7', 'osiem-trybow', 'Eight modes of ending'),
        ('A7', 'filtr-rosyjski', 'Filter for contemporary Russia'),
    ],
    'What actually holds Russia together': [
        ('A6', 'cztery-osie', 'Loyalty as a shrinking stock'),
        ('A7', 'spoiwo', 'Three layers of cohesion'),
        ('A7', 'synteza', 'Strength and solvency of the centre'),
    ],
    'The nuclear arsenal and control of the centre': [
        ('A1', 'arsenal-nuklearny', 'Arsenal and ageing delivery systems'),
        ('A7', 'filtr-rosyjski', 'Nuclear Russia: end-state filter'),
    ],
}


def known_anchors():
    out = set()
    with META.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            out.add((row['dokument_kod'], row['anchor']))
    return out


def chip(code, anchor, label):
    href = f"{DIRS[code]}/#{anchor}"
    text = f"{code} · {label}"
    return (
        f'<a class="ref-chip" href="{html.escape(href, quote=True)}" '
        f'title="Open section: {html.escape(text, quote=True)}">'
        f'{html.escape(text)}</a>'
    )


def main():
    if len(CONTINENTS) != 18:
        raise SystemExit(f'ERROR: expected 18 continents, got {len(CONTINENTS)}')
    known = known_anchors()
    total = 0
    for title, links in CONTINENTS.items():
        if not links or len(links) > 8:
            raise SystemExit(f'ERROR: bad link count for {title}: {len(links)}')
        for code, anchor, _ in links:
            if (code, anchor) not in known:
                raise SystemExit(f'ERROR: anchor not in metadata map: {code} #{anchor}')
            if not (Path('rosja') / DIRS[code] / 'index.html').exists():
                raise SystemExit(f'ERROR: missing stable wrapper for {code}')
            total += 1

    text = TARGET.read_text(encoding='utf-8')
    lines = text.splitlines()
    found = set()
    for i, line in enumerate(lines):
        for title, links in CONTINENTS.items():
            marker = f'<li><strong>{title}</strong>'
            if marker not in line:
                continue
            start = line.find('<span class="refs"')
            end = line.rfind('</span></li>')
            if start < 0 or end < start:
                raise SystemExit(f'ERROR: refs block not found for {title}')
            refs = (
                '<span class="refs" aria-label="Source sections">'
                '<span class="refs-label">Sections:</span>'
                + ''.join(chip(*link) for link in links)
                + '</span></li>'
            )
            lines[i] = line[:start] + refs
            found.add(title)
            break

    missing = set(CONTINENTS) - found
    if missing:
        raise SystemExit('ERROR: missing continent blocks: ' + ', '.join(sorted(missing)))

    out = '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
    out = out.replace(
        '      gap: 5px;\n      align-items: baseline;\n      margin-left: .28em;\n      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n      font-size: .73rem;',
        '      gap: 7px;\n      align-items: baseline;\n      margin-left: .35em;\n      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n      font-size: .82rem;'
    )
    out = out.replace(
        '      min-width: 31px;\n      justify-content: center;\n      padding: 2px 6px;',
        '      min-width: 31px;\n      justify-content: center;\n      padding: 4px 8px;'
    )

    if out.count('aria-label="Source sections"') < 18:
        raise SystemExit('ERROR: not all 18 continent refs were replaced')
    TARGET.write_text(out, encoding='utf-8')
    print(f'PATCH_EN_OK continents=18 links={total} weak_links_omitted=yes')


if __name__ == '__main__':
    main()
