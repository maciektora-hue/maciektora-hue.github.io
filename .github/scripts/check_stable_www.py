#!/usr/bin/env python3
"""
Strażnik konwencji stałych adresów WWW.

Sprawdza siedem reguł. Każde naruszenie to błąd i czerwone CI.
Reguła 4 została odwrócona 2026-09-20, reguły 6 i 7 dodane tego samego dnia —
uzasadnienia stoją przy samych regułach.
Znane, świadomie utrzymywane wyjątki mieszkają w .github/stable-www-allowlist.txt.

CZEGO TEN SKRYPT ŚWIADOMIE NIE SPRAWDZA
----------------------------------------
NIE sprawdza, czy anchor wskazywany przez link istnieje w pliku docelowym.
To decyzja projektowa, nie luka. NIE DODAWAĆ takiej reguly.

Link do `#sekcja-15`, której jeszcze nie napisano, albo anchor po przeniesionej
sekcji, to niedokończony tekst, a nie awaria: przeglądarka otworzy stronę od góry
i nikomu nic się nie stanie. Reguły sprawdzane niżej mają inną naturę — łamią się
po cichu i uderzają w kogoś z zewnątrz: 404, wyrzucenie czytelnika na górę
dokumentu, dwa rozjeżdżające się źródła prawdy.

Ten strażnik pilnuje ADRESÓW, nie kompletności tekstu. Stąd rozróżnienie:
  - przekazywanie #anchor przez przekierowanie  -> sprawdzane (mechanika adresu)
  - istnienie id="anchor" w pliku docelowym     -> nie sprawdzane (stan tekstu)

Uzasadnienie w SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md, sekcja 0.3.

Uruchomienie lokalne:
    python3 .github/scripts/check_stable_www.py
"""

import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALLOWLIST = os.path.join(ROOT, ".github", "stable-www-allowlist.txt")

SKIP_DIRS = {".git", ".github", "node_modules"}
VERSION_IN_NAME = re.compile(r"v?\d+[._-]\d+|\d{4}-\d{2}-\d{2}")
# Numer wydania w nazwie pliku: stem-01_03.html, stem-v02.00.html, stem-2_00.html.
RELEASE_IN_NAME = re.compile(r"^(?P<stem>.+?)[-_]v?(?P<xx>\d{1,2})[._](?P<yy>\d{2})(?P<ogon>.*)\.html$")
# Numer wydania w naglowku dokumentu. Szukany WYLACZNIE w <title> i w czesci przed
# pierwszym <h2>, bo w tresci zdania w rodzaju "Wersja 01.00 podawala inna liczbe"
# odnosza sie do wydan poprzednich i nie sa naglowkiem tego dokumentu.
# W <title> numer bywa podany samym separatorem: "— 01.03", "· v01.00".
RELEASE_IN_TITLE = re.compile(r"(?:Wersja\s*:?\s*|[-\u2013\u2014\u00b7]\s*v?)(\d{1,2})[.](\d{2})")
# Zapis wiazacy: "Wersja: 01.03" z dwukropkiem, w naglowku albo w stopce dokumentu.
# Dwukropek jest obowiazkowy, bo bez niego lapie zdania w rodzaju
# "Wersja 01.00 podawala inna liczbe", ktore mowia o wydaniach poprzednich.
RELEASE_DECLARED = re.compile(r"(?:Wersja|Version)\s*:\s*v?(\d{1,2})[.](\d{2})")
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
LINK = re.compile(r'(?:href|url)=["\']?([^"\'>\s]+\.html)')
JS_REDIRECT = re.compile(r"location\.replace\(\s*'([^']+)'")
META_REFRESH = re.compile(r'http-equiv=["\']refresh["\']', re.I)
BODY = re.compile(r"<body[^>]*>(.*)</body>", re.S | re.I)


def load_allowlist():
    if not os.path.exists(ALLOWLIST):
        return set()
    out = set()
    with open(ALLOWLIST, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if line:
                out.add(line)
    return out


def html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".html"):
                full = os.path.join(dirpath, name)
                yield os.path.relpath(full, ROOT).replace(os.sep, "/")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def is_stub(text):
    return bool(META_REFRESH.search(text)) or "location.replace(" in text


def resolve(rel, target):
    return os.path.normpath(os.path.join(os.path.dirname(rel), target.split("#")[0])).replace(os.sep, "/")


def main():
    allow = load_allowlist()
    files = sorted(html_files())
    texts = {rel: read(rel) for rel in files}
    existing = set(files)
    errors = []

    # 1. Martwe linki wewnętrzne.
    for rel, text in texts.items():
        targets = set(LINK.findall(text)) | set(JS_REDIRECT.findall(text))
        for target in targets:
            if target.startswith(("http://", "https://", "//", "mailto:", "#")):
                continue
            resolved = resolve(rel, target)
            if resolved.endswith(".html") and resolved not in existing:
                errors.append(f"martwy link: {rel} -> {target}")

    # 2. Każdy stub musi przekazać #anchor dalej.
    for rel, text in texts.items():
        if is_stub(text) and "location.hash" not in text:
            errors.append(
                f"stub gubi anchor: {rel} "
                "(sam meta refresh nie przenosi fragmentu; dodaj location.replace(cel + location.hash))"
            )

    # 3. Stabilny adres nie może być kopią treści.
    by_body = {}
    for rel, text in texts.items():
        if is_stub(text):
            continue
        match = BODY.search(text)
        payload = match.group(1) if match else text
        digest = hashlib.sha256(re.sub(r"\s+", " ", payload).strip().encode()).hexdigest()
        by_body.setdefault(digest, []).append(rel)
    for group in by_body.values():
        if len(group) > 1 and not all(g in allow for g in group):
            errors.append(
                "zduplikowana tresc pod wieloma adresami: "
                + ", ".join(sorted(group))
                + " (stabilny adres ma przekierowywac, a nie kopiowac plik)"
            )

    # 4. Plik treściowy z wersją lub datą w nazwie musi mieć stałe wejście.
    #
    # Reguła odwrócona 2026-09-20. Wcześniej zabraniała wersji w nazwie, przez co
    # ogłaszała naruszeniem dominujący wzorzec repozytorium i wymagała listy 45
    # wyjątków. Wersja w nazwie sama w sobie nikomu nie szkodzi — szkodzi dopiero
    # brak stałego adresu, bo wtedy kolejne wydanie zabija rozesłany link.
    # To jest dokładnie usterka esejów o Navierze-Stokesie, od której się zaczęło.
    #
    # Stałym wejściem jest stub, który sam NIE ma wersji ani daty w nazwie —
    # w praktyce katalog z index.html. Stub pod starą, wersjonowaną nazwą pliku
    # jest łatką na rozesłany link, nie wejściem, więc się tu nie liczy.
    wejscia = {}
    for rel, text in texts.items():
        if not is_stub(text):
            continue
        if VERSION_IN_NAME.search(os.path.basename(rel)):
            continue
        for target in set(LINK.findall(text)) | set(JS_REDIRECT.findall(text)):
            if target.startswith(("http://", "https://", "//", "mailto:", "#")):
                continue
            wejscia.setdefault(resolve(rel, target), set()).add(rel)

    for rel, text in texts.items():
        if is_stub(text) or rel in allow:
            continue
        if VERSION_IN_NAME.search(os.path.basename(rel)) and rel not in wejscia:
            errors.append(
                f"wersja w nazwie bez stalego wejscia: {rel} "
                "(dodaj katalog z index.html przekierowujacym na ten plik)"
            )

    # 6. Stałe wejście wskazuje na NAJNOWSZE wydanie.
    #
    # Dziura, którą to zamyka: po podbiciu wersji powstaje nowy plik, a stub zostaje
    # przepięty ręcznie. Zapomniane przepięcie nie łamie żadnej innej reguły — adres
    # działa, anchor działa, linku nikt nie zgubił — tylko po cichu podaje czytelnikowi
    # stary tekst. Jedyny błąd w tym zestawie, którego nie widać z zewnątrz.
    wydania = {}
    for rel in files:
        m = RELEASE_IN_NAME.match(os.path.basename(rel))
        if not m or is_stub(texts[rel]):
            continue
        klucz = (os.path.dirname(rel), m.group("stem"), m.group("ogon"))
        wydania.setdefault(klucz, []).append((int(m.group("xx")), int(m.group("yy")), rel))

    for rel, text in texts.items():
        if not is_stub(text) or VERSION_IN_NAME.search(os.path.basename(rel)):
            continue
        for target in set(LINK.findall(text)) | set(JS_REDIRECT.findall(text)):
            if target.startswith(("http://", "https://", "//", "mailto:", "#")):
                continue
            cel = resolve(rel, target)
            m = RELEASE_IN_NAME.match(os.path.basename(cel))
            if not m:
                continue
            klucz = (os.path.dirname(cel), m.group("stem"), m.group("ogon"))
            rodzina = sorted(wydania.get(klucz, []))
            if rodzina and rodzina[-1][2] != cel:
                errors.append(
                    f"wejscie wskazuje na stare wydanie: {rel} -> {os.path.basename(cel)} "
                    f"(najnowsze w katalogu: {os.path.basename(rodzina[-1][2])})"
                )

    # 7. Numer wydania w nazwie pliku zgadza się z numerem w nagłówku dokumentu.
    #
    # Druga połowa tej samej dziury: wersja podniesiona w treści, nazwa pliku stara,
    # albo odwrotnie. Sprawdzane tylko tam, gdzie oba numery w ogóle istnieją —
    # plik bez numeru w nazwie i tekst bez nagłówka wersji są pomijane bez uwag.
    for rel, text in texts.items():
        if is_stub(text):
            continue
        m = RELEASE_IN_NAME.match(os.path.basename(rel))
        if not m:
            continue
        # Pierwszenstwo ma jawna deklaracja "Wersja: XX.YY" gdziekolwiek w dokumencie.
        # Numer w <title> jest tylko ozdobnikiem i bywa nieodswiezony po podbiciu.
        zadeklarowane = RELEASE_DECLARED.findall(text)
        if zadeklarowane:
            h = zadeklarowane[0]
        else:
            tytul = TITLE.search(text)
            trafienia = RELEASE_IN_TITLE.findall(tytul.group(1)) if tytul else []
            if not trafienia:
                continue
            h = trafienia[-1]
        w_nazwie = (int(m.group("xx")), int(m.group("yy")))
        w_naglowku = (int(h[0]), int(h[1]))
        if w_nazwie != w_naglowku:
            errors.append(
                f"wersja w nazwie rozni sie od naglowka: {rel} "
                f"(nazwa {w_nazwie[0]:02d}.{w_nazwie[1]:02d}, naglowek {w_naglowku[0]:02d}.{w_naglowku[1]:02d})"
            )

    # 5. Dokumentacja nie wskazuje na nieistniejące pliki.
    md_link = re.compile(r"\[[^\]]*\]\(([^)\s]+\.html)\)")
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, "/")
            for target in md_link.findall(read(rel)):
                if target.startswith(("http://", "https://", "//")):
                    continue
                if resolve(rel, target) not in existing:
                    errors.append(f"dokumentacja wskazuje na nieistniejacy plik: {rel} -> {target}")

    stubs = sum(1 for t in texts.values() if is_stub(t))
    print(f"HTML-i: {len(files)} | stubow: {stubs} | wyjatkow na liscie: {len(allow)}")

    if errors:
        print(f"\nNARUSZENIA KONWENCJI STALYCH ADRESOW: {len(errors)}\n")
        for err in sorted(set(errors)):
            print(f"  - {err}")
        print(
            "\nJezeli ktores naruszenie jest swiadoma decyzja, dopisz plik do "
            ".github/stable-www-allowlist.txt razem z uzasadnieniem."
        )
        return 1

    print("\nKonwencja stalych adresow: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
