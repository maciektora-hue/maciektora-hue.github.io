#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIT_TSV = ROOT / "SOL_mapa-sekcji-i-anchorow-rosja.tsv"
MANIFEST = ROOT / "SOL_reczne-anchory-rosja.tsv"

SOURCES = {
    "A1": "a1_POCZATEK_ZAMROZONE_kolumbryna-v3_5-2026-03-31.html",
    "A5": "a5_ZAMROZONE-audyt-2rewizje-v03_00-2026-06-23.html",
    "D1": "d1-zamrozone-narzedzie-dark-legitimacy-horbyk-v01_00-2026-03-25.html",
    "D2": "d2-zamrozone-narzedzie-disinfolklore-kompilacja-v01_00-2026-03-25.html",
    "D3": "d3-zamrozone-narzedzie-disinfolklore-swot-advocatus-v01_00-2026-03-25.html",
    "D4": "d4-zamrozone-rosyjskie-samobojstwa-taksonomia-v08_01-2026-06-13.html",
    "D5": "d5-zamrozone-putin-cornered-animal-v03_00-2026-03-24.html",
    "D6": "d6-zamrozone-jalta-3-analiza-strategiczna-v01_00-2026-03-08.html",
    "D7": "d7-zamrozone-jalta-3-apendyks-v01_00-2026-03-08.html",
    "E1": "ropa-gaz-geopolityka-analiza-v01_00-2026-03-17.html",
    "E2": "monopole-moralnosc-transformacja-zrodla-v01_00-2026-03-17.html",
}

WRAPPERS = {
    "A1": "kolumbryna/index.html",
    "A5": "audyt/index.html",
    "D1": "dark-legitimacy/index.html",
    "D2": "disinfolklore/index.html",
    "D3": "disinfolklore-swot/index.html",
    "D4": "rosyjskie-samobojstwa/index.html",
    "D5": "putin-cornered/index.html",
    "D6": "jalta-3/index.html",
    "D7": "jalta-3-apendyks/index.html",
    "E1": "ropa-gaz/index.html",
    "E2": "monopole/index.html",
}

# RĘCZNIE DOBRANE ANCHORY. Ta lista NIE jest generowana z tytułów.
MANUAL = {
    "A1": [
        "kolumbryna",
        "front-spirala-opl",
        "arsenal-nuklearny",
        "budzet-nwf-hormuz",
        "eksport-dewizy-majatek",
        "infrastruktura-kolej-rury-samoloty",
        "spoleczenstwo-na-krawedzi",
        "bestiariusz-szare-nosorozce",
        "patologia-informacyjna",
        "chemia-pozarow-uzaleznienie-sezonowosc",
        "za-pozno-konkluzja-czesci-i",
        "nie-pytanie-o-pieniadze",
        "zasoby-skreslenia-scenariusze-desperacji",
        "elity-odlaczaja-sie-od-putina",
        "rozpad-iranu-koncepcja-operacyjna",
        "mapa-aktorow-ryzyka-krytyczne",
        "hanza-2-0",
        "od-ormuzu-do-panelu",
        "monopole-topologia-wladzy",
        "disinfolklore-dark-legitimacy",
        "zrodla-etyka-granice-poznania",
        "steelmanning-systemu",
        "disinfolklore-swot-przesluchanie",
        "zrewidowana-konkluzja",
    ],
    "A5": [
        "kolumbryna-kontra-rzeczywistosc",
        "jak-czytac",
        "licznik-rewizji",
        "nosorozce-stan-31-05",
    ],
    "D1": [
        "dark-legitimacy-authoritarianism",
        "abstract",
        "affirmative-concept-legitimacy",
        "governmentality-affirmative-legitimacy",
        "legitimacy-crisis-soviet-post-soviet",
        "dark-legitimacy-bad-is-good",
        "russia-ukraine-war-over-legitimacy",
        "consequences-dark-legitimacy",
        "acknowledgments",
        "references",
    ],
    "D2": [
        "disinfolklore",
        "spis-tresci",
        "geneza-most-trolle-folklor",
        "definicja-i-zakres",
        "dwanascie-narzedzi",
        "archetypal-disinfolklore-literacy",
        "troll-radars",
        "mana-in-the-meme",
        "archetypal-structures",
        "trigger-experience-reaction",
        "code-of-positive-trolls",
        "accusation-in-a-mirror",
        "provocation-logic-cycle",
        "witch-switch",
        "coercive-control",
        "re-archetyping",
        "rashist-construction",
        "trzy-archetypy",
        "druidy-don",
        "duncey-putin",
        "komik-zelenski",
        "mana-energia-w-memach",
        "accusation-in-a-mirror-i-provocation-logic",
        "oskarzenie-w-lustrze",
        "cykl-logiki-prowokacji",
        "witch-switch-przelacznik-czarownicy",
        "data-resistant-archetypes",
        "finding-manuland",
        "finding-manuland-glowne-tezy",
        "disinfolklore-fimi",
        "fimi-co-robi-dobrze",
        "fimi-czego-nie-widzi",
        "counter-disinfolklore",
        "wnioski-i-kierunki",
    ],
    "D3": [
        "disinfolklore-swot-advocatus-przesluchanie",
        "analiza-swot",
        "strengths-sily",
        "weaknesses-slabosci",
        "opportunities-szanse",
        "threats-zagrozenia",
        "synteza-strategiczna",
        "advocatus-diaboli",
        "archetypowanie-jako-bron",
        "obserwator-w-polu-bitwy",
        "mana-falsyfikowalnosc",
        "ukraina-jako-disinfolklore",
        "indoeuropocentryzm",
        "problem-skali",
        "narzedzie-czy-system-wierzen",
        "demokratyczna-bron-i-wyborca",
        "trzy-postacie-redukcja-geopolityki",
        "postnarracyjne-narzedzie-z-narracji",
        "przesluchanie-bieglego",
        "publikacja-i-recenzja-metody",
        "powtarzalnosc-klasyfikacji",
        "mana-kryterium-falsyfikacji",
        "kwalifikacje-bieglego",
        "bezstronnosc-bieglego",
        "operacyjna-definicja-archetypu",
        "dane-empiryczne-odpornosc-na-dezinformacje",
        "m-n-poparcie-lingwistow",
        "falszywie-pozytywny",
        "accusation-in-a-mirror-kryterium",
        "walor-dowodowy",
        "warunki-obalenia-metody",
    ],
    "D4": [
        "taksonomia-rosyjskiego-samobojstwa",
        "defenestracja",
        "bron-palna",
        "powieszenie-uduszenie",
        "utoniecie-upadek-z-jednostki",
        "nagly-zawal-niewydolnosc",
        "trucizny-substancje-egzotyczne",
        "smierc-w-wiezieniu",
        "znaleziony-martwy",
        "katastrofa-lotnicza",
        "dekapitacja",
        "metoda-podwojna",
        "metaanaliza-taksonomii",
    ],
    "D5": [
        "putin-cornered-animal",
        "nie-pytanie-o-pieniadze",
        "co-mu-zostaje",
        "co-nie-dziala",
        "ukryty-majatek-dark-money",
        "scenariusze-desperacji",
        "kiedy-elity-odlacza-sie-od-putina",
        "projekt-zycia-mu-nie-wyszedl",
    ],
    "D6": [
        "jalta-3-0",
        "spis-tresci",
        "wizja-synteza",
        "filary-wizji",
        "koncepcja-operacyjna",
        "rzeka-aras",
        "pas-30-km",
        "zagros-domena-kurdyjska",
        "wielki-deal-wladywostok-za-kaukaz",
        "hanza-2-0",
        "mapa-driverow",
        "analizy-przeprowadzone",
        "rozpad-iranskiej-panstwowosci",
        "argumenty-za-rozpadem",
        "argumenty-przeciw-rozpadowi",
        "utrata-aury-strachu-irgc",
        "wnioski-irgc",
        "operacja-azerska",
        "feasibility-operacji-azerskiej",
        "konwergencja-interesow-sojusznikow",
        "zbieznosci-sojusznikow",
        "sprzecznosci-sojusznikow",
        "rola-rosji",
        "dlaczego-rosja-sie-nie-liczy",
        "model-finansowania",
        "zrodla-kapitalu",
        "szok-jako-akcelerator",
        "precedensy-historyczne",
        "dziury-i-ryzyka",
        "ryzyko-uran-440-kg",
        "ryzyko-globalny-szok-naftowy",
        "ryzyko-pakistan-beludzystan",
        "ryzyko-tozsamosc-iranskich-azerow",
        "ryzyko-mission-creep-eskalacja",
        "ryzyko-fragmentacja-kurdyjska",
        "ryzyko-sekwencja-zdarzen",
        "werdykt-koncowy",
        "ocena-analityka",
    ],
    "D7": [
        "jalta-3-0",
        "warstwa-kognitywna",
        "hipoteza-warstwa-kognitywna",
        "trump-profil-adhd",
        "aliyev-audhd-strategiczne",
        "izrael-panstwo-z-audhd",
        "warstwa-tozsamosciowa",
        "fundament-koalicji",
        "panstwo-jako-projekt",
        "wzajemne-rozpoznanie",
        "samowystarczalnosc-przetrwanie",
        "trzy-tysiace-lat-historii",
        "abraham-w-zagros",
        "warstwa-paradoksu",
        "teza-nieufnosc-stabilizator",
        "precedensy-zdrady",
        "piec-mechanizmow-nieufnosci",
        "autonomia-dzialania",
        "struktury-niezalezne-od-patrona",
        "niezaleznosc-od-attention-spanu-trumpa",
        "eliminacja-pulapki-zaleznosci",
        "legitymacja-wewnetrzna",
        "warstwa-matematyczna",
        "definicja-rownowagi-nasha",
        "nash-trojkat-zydzi-azerowie-kurdowie",
        "izrael-defektuje",
        "azerbejdzan-defektuje",
        "kurdowie-defektuja",
        "nash-czworokat-z-usa",
        "usa-defektuja",
        "trojkat-defektuje-wobec-usa",
        "nash-pelny-system",
        "turcja-defektuje",
        "armenia-defektuje",
        "ue-defektuje",
        "gcc-defektuje",
        "chiny-defektuja",
        "trzy-zagniezdzone-rownowagi",
        "warstwa-epistemologiczna",
        "odwrocona-metoda-naukowa",
        "synteza-dlaczego-moze-zadzialac",
        "piec-warstw-piec-powodow",
        "ostatnie-zdanie",
    ],
    "E1": [
        "ropa-gaz-geopolityka",
        "globalny-popyt-ropa-gaz-2024",
        "transport-podzial-wewnetrzny",
        "substytucja-juz-teraz",
        "transport-drogi-prad-cieplo",
        "surowiec-procesy-przemyslowe",
        "nawozy-feedstock",
        "scenariusz-ormuz",
        "szok-cenowy-vs-fizyczny-brak",
        "skala-szoku-lehman-dot-com",
        "paradoks-szybkiego-szoku",
        "geopolityka-energii-topologia-wladzy",
        "elektryfikacja-transportu-i-generacji",
        "centralizacja-vs-decentralizacja",
        "panel-capital-good-barylka-consumable",
        "monopole-surowcowe",
        "saudyjska-dzwignia-autoimmunologia",
        "chinski-monopol-surowcow-krytycznych",
        "chinski-opec-zegar-samozniszczenia",
        "wymiar-etyczny-transformacji",
        "tani-surowiec-moralny-hazard",
        "kryzys-warunek-substytut",
        "kto-przyspieszyl-dekarbonizacje",
        "energia-sprawiedliwosc",
        "podsumowanie-tez",
    ],
    "E2": [
        "monopole-moralnosc-transformacja",
        "saudyjska-dzwignia-samolikwidacja",
        "chinski-monopol-ree-lit",
        "strategia-processing",
        "erozja-zegar-samozniszczenia",
        "wandel-durch-handel-moralny-hazard",
        "niemiecka-zaleznosc-rosyjski-gaz",
        "nowe-vs-stare-kraje-czlonkowskie",
        "kryzysy-moralnosc-solidarnosc-sauve-qui-peut",
        "1973-vs-2022",
        "asymetria-kosztow-transformacji",
        "podsumowanie-korekt",
    ],
}

ANCHOR_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"h([1-6])", re.I)


def clean_text(parts: list[str]) -> str:
    return re.sub(r"\s+", " ", "".join(parts)).strip()


@dataclass
class Heading:
    level: int
    id_value: str | None
    line: int
    col: int
    starttag: str
    text_parts: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return clean_text(self.text_parts)


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.headings: list[Heading] = []
        self.stack: list[Heading] = []
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        low = tag.lower()
        attrs_d = dict(attrs)
        if "id" in attrs_d:
            self.ids.append(attrs_d.get("id") or "")
        m = HEADING_RE.fullmatch(low)
        if m:
            line, col = self.getpos()
            h = Heading(
                level=int(m.group(1)),
                id_value=attrs_d.get("id"),
                line=line,
                col=col,
                starttag=self.get_starttag_text(),
            )
            self.headings.append(h)
            self.stack.append(h)

    def handle_endtag(self, tag: str) -> None:
        low = tag.lower()
        m = HEADING_RE.fullmatch(low)
        if not m:
            return
        level = int(m.group(1))
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].level == level:
                del self.stack[i]
                break

    def handle_data(self, data: str) -> None:
        for h in self.stack:
            h.text_parts.append(data)


def parse(text: str) -> Parser:
    p = Parser()
    p.feed(text)
    p.close()
    return p


def target_name(source: str) -> str:
    if not source.endswith(".html"):
        raise RuntimeError(source)
    return source[:-5] + "-anchory.html"


def line_starts(text: str) -> list[int]:
    starts = [0]
    for m in re.finditer("\n", text):
        starts.append(m.end())
    return starts


def load_missing_rows():
    grouped = defaultdict(list)
    with AUDIT_TSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            if row["anchor_status"] == "BRAK":
                grouped[row["dokument_kod"]].append(row)
    return grouped


def validate_manual() -> None:
    if set(MANUAL) != set(SOURCES):
        raise RuntimeError("MANUAL i SOURCES mają różne kody")
    total = sum(len(v) for v in MANUAL.values())
    if total != 242:
        raise RuntimeError(f"Ręczna lista ma {total} anchorów zamiast 242")
    for code, anchors in MANUAL.items():
        if len(anchors) != len(set(anchors)):
            raise RuntimeError(f"{code}: duplikat w ręcznej liście anchorów")
        bad = [a for a in anchors if not ANCHOR_RE.fullmatch(a)]
        if bad:
            raise RuntimeError(f"{code}: niedozwolone nazwy anchorów: {bad}")


def make_one(code: str, audit_rows: list[dict[str, str]]) -> list[list[str]]:
    source_name = SOURCES[code]
    source_path = ROOT / source_name
    target = target_name(source_name)
    target_path = ROOT / target

    if not source_path.exists():
        raise RuntimeError(f"{code}: brak źródła {source_name}")

    if any(row["dokument_plik"] != source_name for row in audit_rows):
        raise RuntimeError(f"{code}: TSV wskazuje inny plik niż zamrożone źródło")

    anchors = MANUAL[code]
    if len(audit_rows) != len(anchors):
        raise RuntimeError(f"{code}: TSV ma {len(audit_rows)} braków, lista ręczna {len(anchors)}")

    source = source_path.read_text(encoding="utf-8")
    p = parse(source)
    missing = [h for h in p.headings if h.id_value is None]

    if len(missing) != len(anchors):
        raise RuntimeError(f"{code}: żywy HTML ma {len(missing)} nagłówków bez id, oczekiwano {len(anchors)}")
    if any(h.id_value == "" for h in p.headings):
        raise RuntimeError(f"{code}: znaleziono pusty id w źródle")

    tsv_titles = [row["sekcja_tytul"] for row in audit_rows]
    live_titles = [h.text for h in missing]
    if live_titles != tsv_titles:
        for i, (live, old) in enumerate(zip(live_titles, tsv_titles), 1):
            if live != old:
                raise RuntimeError(f"{code}: pozycja {i}: HTML={live!r}, TSV={old!r}")
        raise RuntimeError(f"{code}: lista nagłówków różni się od audytu")

    existing = {x for x in p.ids if x}
    collision = existing.intersection(anchors)
    if collision:
        raise RuntimeError(f"{code}: kolizja z istniejącym id: {sorted(collision)}")

    starts = line_starts(source)
    replacements = []
    manifest_rows = []
    for h, row, anchor in zip(missing, audit_rows, anchors):
        pos = starts[h.line - 1] + h.col
        old = h.starttag
        if not old.endswith(">") or old.endswith("/>"):
            raise RuntimeError(f"{code}: nietypowy tag nagłówka w linii {h.line}: {old!r}")
        if source[pos:pos + len(old)] != old:
            raise RuntimeError(f"{code}: nie zgadza się pozycja tagu w linii {h.line}")
        new = old[:-1] + f' id="{anchor}">'
        replacements.append((pos, pos + len(old), new))
        manifest_rows.append([
            code,
            source_name,
            target,
            row["kolejnosc"],
            row["poziom"],
            row["sekcja_tytul"],
            anchor,
        ])

    generated = source
    for start, end, new in reversed(replacements):
        generated = generated[:start] + new + generated[end:]

    q = parse(generated)
    if len(q.headings) != len(p.headings):
        raise RuntimeError(f"{code}: po zmianie zmieniła się liczba nagłówków")
    if [(h.level, h.text) for h in q.headings] != [(h.level, h.text) for h in p.headings]:
        raise RuntimeError(f"{code}: po zmianie zmieniła się treść lub hierarchia nagłówków")
    if any(h.id_value in (None, "") for h in q.headings):
        raise RuntimeError(f"{code}: po zmianie nadal istnieje nagłówek bez id")

    expected_ids = []
    it = iter(anchors)
    for h in p.headings:
        expected_ids.append(h.id_value if h.id_value is not None else next(it))
    actual_ids = [h.id_value for h in q.headings]
    if actual_ids != expected_ids:
        raise RuntimeError(f"{code}: końcowe id nie odpowiadają jawnej liście")

    counts = Counter(x for x in q.ids if x)
    dup = [x for x, n in counts.items() if n > 1]
    if dup:
        raise RuntimeError(f"{code}: po zmianie powstały duplikaty id: {dup}")

    target_path.write_text(generated, encoding="utf-8")

    wrapper_path = ROOT / WRAPPERS[code]
    wrapper = wrapper_path.read_text(encoding="utf-8")
    old_rel = "../" + source_name
    new_rel = "../" + target
    if old_rel in wrapper:
        wrapper = wrapper.replace(old_rel, new_rel)
        wrapper_path.write_text(wrapper, encoding="utf-8")
    elif new_rel not in wrapper:
        raise RuntimeError(f"{code}: wrapper nie wskazuje ani źródła, ani pliku -anchory")

    print(f"{code}: {len(anchors)} ręcznych anchorów -> {target}")
    return manifest_rows


def main() -> None:
    validate_manual()
    grouped = load_missing_rows()
    if set(grouped) != set(SOURCES):
        raise RuntimeError(f"TSV ma braki dla kodów {sorted(grouped)}, oczekiwano {sorted(SOURCES)}")

    all_rows = []
    for code in SOURCES:
        all_rows.extend(make_one(code, grouped[code]))

    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["dokument_kod", "plik_zamrozony", "plik_anchory", "kolejnosc", "poziom", "sekcja_tytul", "anchor"])
        w.writerows(all_rows)

    if len(all_rows) != 242:
        raise RuntimeError(f"Manifest ma {len(all_rows)} wierszy zamiast 242")
    print(f"OK: zapisano {len(all_rows)} ręcznych anchorów; żadnych anchorów nie wygenerowano heurystycznie")
    print(MANIFEST)


if __name__ == "__main__":
    main()
