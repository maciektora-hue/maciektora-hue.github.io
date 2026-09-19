#!/usr/bin/env python3
"""
Strażnik konwencji stałych adresów WWW.

Sprawdza pięć reguł. Każde naruszenie to błąd i czerwone CI.
Znane, świadomie utrzymywane wyjątki mieszkają w .github/stable-www-allowlist.txt.

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

    # 4. Pliki treściowe nie mają wersji ani daty w nazwie.
    for rel, text in texts.items():
        if is_stub(text) or rel in allow:
            continue
        if VERSION_IN_NAME.search(os.path.basename(rel)):
            errors.append(
                f"wersja lub data w nazwie pliku tresciowego: {rel} "
                "(nazwa ma byc stala, wersja zyje w naglowku dokumentu)"
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
