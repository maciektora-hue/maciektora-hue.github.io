from pathlib import Path
import csv
import html

TARGET = Path('rosja/SOL_mapa-tematow-korpusu-rozpad-rosji-v01_01-2026-09-03.html')
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

# Wyłącznie wybory z zaakceptowanej mapy roboczej.
# Wpisy oznaczone tam jako SŁABE są celowo pominięte.
CONTINENTS = {
    'Ukraina jako projektant kampanii systemowej': [
        ('A1', 'front-spirala-opl', 'Front i spirala OPL'),
        ('A2', 'synteza-ewolucyjna', 'Progi dojrzewania kampanii'),
        ('A3', 'lista-celow', 'Chronologia i klasy celów'),
        ('A4', 'skala-hurtu', 'Przejście na skalę systemową'),
        ('A6', 'uderzenie-2806', 'Jedna fala, trzy obiekty'),
    ],
    'Spirala OPL → rafinerie → paliwo → front': [
        ('A1', 'front-spirala-opl', 'Front–OPL–rafinerie'),
        ('A2', 'front-olexandrivka-uzasadnienie', 'Skutek na froncie'),
        ('A6', 'offline-slack', 'Koniec luzu rafineryjnego'),
    ],
    'Paliwo jako układ, nie liczba baryłek': [
        ('A2', 'rynek-paliw-siedem-brakow', 'Siedem awarii paliwowych'),
        ('A4', 'przerob-dno-dwudziestolecia', 'Przerób na dnie'),
        ('A6', 'czesc-materia', 'Bilans paliw i zapasów'),
        ('A6', 'cebula-transportowa', 'Wąskie gardła transportu'),
    ],
    'Krym przekształcany z półwyspu w wyspę': [
        ('A2', 'trzy-wektory', 'Trzy kanały zaopatrzenia'),
        ('A2', 'krym-wyspa', 'Krym jako wyspa logistyczna'),
        ('A3', 'okres-16', 'Krym w najnowszej fazie'),
    ],
    'Logistyka jako anatomia państwa': [
        ('A1', 'infrastruktura-kolej-rury-samoloty', 'Kolej, rury, samoloty'),
        ('A2', 'rynek-kolej', 'Przeciążona kolej'),
        ('A4', 'kolej', 'Kolej: przewozy i kadry'),
        ('A4', 'lotnictwo', 'Lotnictwo i kanibalizacja'),
        ('A6', 'cebula-transportowa', 'Tabor i przepustowość'),
    ],
    'Energetyka i rosyjska sieć elektroenergetyczna': [
        ('A2', 'energetyka-siec-bez-redundancji', 'Sieć bez realnej redundancji'),
        ('A2', 'energetyka-ues-topologia', 'Topologia siedmiu stref UES'),
    ],
    'Klimat jako uczestnik wojny bez konta na Telegramie': [
        ('A2', 'klimat-cascade-gradient', 'Klimat → energia → logistyka'),
        ('A2', 'klimat-kaskada-lato-2026', 'Upał, susza i chłodzenie'),
    ],
    'Gospodarka w czasie teraźniejszym ciągłym': [
        ('A1', 'budzet-nwf-hormuz', 'Budżet, deficyt i NWF'),
        ('A2', 'dwa-procesy-a-b', 'Front dziś, gospodarka jutro'),
        ('A4', 'zapasc', 'Równoległa degradacja gospodarki'),
        ('A4', 'budzet', 'Deficyt ponad plan'),
    ],
    'Bankowość jako najkrótszy zapalnik': [
        ('A4', 'bankowosc', 'Utajony kryzys bankowy'),
        ('A4', 'dlaczego-najkrotszy', 'Dlaczego banki są najszybsze'),
    ],
    'Ludzie jako zasób nieodnawialny': [
        ('A1', 'spoleczenstwo-na-krawedzi', 'Brain drain i braki kadrowe'),
        ('A4', 'mobilizacja', 'Werbunek i mobilizacja'),
        ('A4', 'zabralaby-specjalistow', 'Mobilizacja zabiera specjalistów'),
    ],
    'Chiny jako patron i wierzyciel, nie sojusznik': [
        ('A1', 'steelmanning-systemu', 'Chiny jako podpora systemu'),
        ('A4', 'chinski-substytut', 'Chiński substytut'),
        ('A4', 'gaz-oba-kierunki', 'Gaz: Europa kontra Chiny'),
        ('A7', 'hierarchia', 'Rosja jako klient Chin'),
        ('A7', 'chiny-integralnosc', 'Chińska kalkulacja integralności'),
    ],
    'Przemysł wojenny i zerwane łańcuchy zastępowalności': [
        ('A2', 'po-tupolewa-do-sklepu', 'Nieodtwarzalne platformy'),
        ('A2', 'uwaga-a50-precedens', 'Precedens A-50'),
        ('A4', 'przemysl-domkniecia', 'Presja na zbrojeniówkę'),
        ('A4', 'waskie-gardlo', 'Części ważniejsze niż hale'),
    ],
    'Rosyjskie adaptacje, które naprawdę działają': [
        ('A4', 'adaptacja', 'Adaptacja pod presją'),
        ('A4', 'flota-cieni', 'Flota cieni'),
    ],
    'Putin jako osobna funkcja celu': [
        ('A1', 'nie-pytanie-o-pieniadze', 'Nie chodzi o pieniądze'),
        ('D5', 'putin-cornered-animal', 'Putin jako cornered animal'),
        ('D5', 'scenariusze-desperacji', 'Scenariusze desperacji'),
        ('A6', 'rosja-rowna-putin', 'Rosja ≠ funkcja celu Putina'),
        ('A6', 'paradoks-zapedzenia', 'Paradoks zapędzenia'),
    ],
    'Elity i moment przeliczenia lojalności': [
        ('A1', 'elity-odlaczaja-sie-od-putina', 'Kiedy elity się odłączą'),
        ('D5', 'kiedy-elity-odlacza-sie-od-putina', 'Próg kosztu lojalności'),
        ('A6', 'zablokowana-elita', 'Zablokowana elita'),
        ('A7', 'spoiwo', 'Lojalność jako kalkulacja'),
    ],
    'Jak właściwie kończą się państwa': [
        ('A7', 'osiem-trybow', 'Osiem trybów końca'),
        ('A7', 'filtr-rosyjski', 'Filtr dla współczesnej Rosji'),
    ],
    'Co naprawdę spaja Rosję': [
        ('A6', 'cztery-osie', 'Lojalność jako kurczący się zapas'),
        ('A7', 'spoiwo', 'Trzy warstwy spoiwa'),
        ('A7', 'synteza', 'Siła i wypłacalność centrum'),
    ],
    'Arsenał nuklearny i kontrola centrum': [
        ('A1', 'arsenal-nuklearny', 'Arsenał i starzenie nośników'),
        ('A7', 'filtr-rosyjski', 'Nuklearna Rosja: filtr końca'),
    ],
}


def load_known_anchors():
    known = set()
    with META.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            known.add((row['dokument_kod'], row['anchor']))
    return known


def chip(code, anchor, label):
    href = f"{DIRS[code]}/#{anchor}"
    text = f"{code} · {label}"
    return (
        f'<a class="ref-chip" href="{html.escape(href, quote=True)}" '
        f'title="Otwórz sekcję: {html.escape(text, quote=True)}">'
        f'{html.escape(text)}</a>'
    )


def main():
    if len(CONTINENTS) != 18:
        raise SystemExit(f'ERROR: expected 18 continents, got {len(CONTINENTS)}')

    known = load_known_anchors()
    all_links = 0
    for title, links in CONTINENTS.items():
        if not links or len(links) > 8:
            raise SystemExit(f'ERROR: bad link count for {title}: {len(links)}')
        for code, anchor, _ in links:
            if code not in DIRS:
                raise SystemExit(f'ERROR: no stable directory for {code}')
            if (code, anchor) not in known:
                raise SystemExit(f'ERROR: anchor not in metadata map: {code} #{anchor}')
            wrapper = Path('rosja') / DIRS[code] / 'index.html'
            if not wrapper.exists():
                raise SystemExit(f'ERROR: missing stable wrapper: {wrapper}')
            all_links += 1

    text = TARGET.read_text(encoding='utf-8')
    lines = text.splitlines()
    found = set()

    for i, line in enumerate(lines):
        for title, links in CONTINENTS.items():
            marker = f'<li><strong>{title}</strong>'
            if marker not in line:
                continue
            if title in found:
                raise SystemExit(f'ERROR: duplicate continent title: {title}')
            start = line.find('<span class="refs"')
            end = line.rfind('</span></li>')
            if start < 0 or end < start:
                raise SystemExit(f'ERROR: refs block not found for: {title}')
            new_refs = (
                '<span class="refs" aria-label="Sekcje źródłowe">'
                '<span class="refs-label">Sekcje:</span>'
                + ''.join(chip(*link) for link in links)
                + '</span></li>'
            )
            lines[i] = line[:start] + new_refs
            found.add(title)
            break

    missing = set(CONTINENTS) - found
    if missing:
        raise SystemExit('ERROR: missing continent blocks: ' + ', '.join(sorted(missing)))

    out = '\n'.join(lines) + ('\n' if text.endswith('\n') else '')

    # Większe i czytelniejsze chipy. Zmiana wyłącznie CSS mapy, bez dokumentów źródłowych.
    out = out.replace(
        '      gap: 5px;\n      align-items: baseline;\n      margin-left: .28em;\n      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n      font-size: .73rem;',
        '      gap: 7px;\n      align-items: baseline;\n      margin-left: .35em;\n      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n      font-size: .82rem;'
    )
    out = out.replace(
        '      min-width: 31px;\n      justify-content: center;\n      padding: 2px 6px;',
        '      min-width: 31px;\n      justify-content: center;\n      padding: 4px 8px;'
    )

    # Walidacja końcowa wyłącznie na wygenerowanym HTML mapy.
    if out.count('aria-label="Sekcje źródłowe"') < 18:
        raise SystemExit('ERROR: not all 18 continent refs were replaced')
    for title, links in CONTINENTS.items():
        for code, anchor, _ in links:
            expected = f'href="{DIRS[code]}/#{anchor}"'
            if expected not in out:
                raise SystemExit(f'ERROR: generated href missing: {expected}')

    TARGET.write_text(out, encoding='utf-8')
    print(f'PATCH_OK continents={len(CONTINENTS)} links={all_links} weak_links_omitted=yes')


if __name__ == '__main__':
    main()
