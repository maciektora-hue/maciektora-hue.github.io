#!/usr/bin/env python3
from __future__ import annotations

import csv
import html
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAP_PATH = ROOT / "SOL_mapa-sekcji-i-anchorow-audhd.tsv"

FILES = {
    "AU01": "63-cechy-rdzen-czy-maskowanie-01_01-2026-08-26.html",
    "AU02": "CLAUDE_co-dziala-po-poznej-diagnozie-02_01-2026-08-26.html",
    "AU03": "CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html",
    "AU04": "CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html",
    "AU05": "ESEJ_architektury-pamieci-1_02-2026-04-28.html",
    "AU06": "POWIESC_architektury-pamieci-2_00-2026-04-29.html",
    "AU07": "adhd-pomaganie-kosztem-siebie-v01.00-2026-05-14.html",
    "AU08": "apendyks1-po-ludzku-02_01-2026-08-26.html",
    "AU09": "audhd-fundatorzy-it-1_00-2026-04-27.html",
    "AU10": "audhd-po-ludzku-v02_02-2026-07-09.html",
    "AU11": "audhd_opracowanie_v6_0_2026-07-01-2.html",
    "AU12": "autyzm-regulacja-mowienia-v01.00-2026-05-14.html",
    "AU13": "co-to-znaczy-audhd-v03_01-2026-07-09-2.html",
    "AU14": "dluga-lista-publikacji-4.01-2026-08-26.html",
    "AU15": "ilu-nas-jest-audhd-polska-wstep-v03_00-2026-08-10.html",
    "AU16": "kognitywistyka-ai-bledy-poznawcze-2_00-2026-04-28.html",
    "AU17": "obiektywnosc-autyzm-v01.00-2026-05-14.html",
    "AU18": "piec-jezykow-milosci-nd-v01.00-2026-05-18.html",
}

HEADING_RE = re.compile(r"<h([1-6])(?P<attrs>[^>]*)>(?P<body>.*?)</h\1\s*>", re.I | re.S)
ID_RE = re.compile(r"\bid\s*=\s*([\"'])(.*?)\1", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
TRANS = str.maketrans({"ł": "l", "Ł": "L"})


def plain(s: str) -> str:
    return WS_RE.sub(" ", html.unescape(TAG_RE.sub(" ", s))).strip()


def slugify(title: str) -> str:
    s = title.translate(TRANS)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "sekcja"


def main() -> None:
    with MAP_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    if not fields or len(rows) != 338:
        raise SystemExit(f"STOP: mapa nie ma 338 wierszy: {len(rows)}")

    by_code = defaultdict(list)
    for r in rows:
        by_code[r["dokument_kod"]].append(r)
    changed_total = 0

    for code, filename in FILES.items():
        doc_rows = sorted(by_code[code], key=lambda r: int(r["kolejnosc"]))
        path = ROOT / filename
        text = path.read_text(encoding="utf-8")
        matches = list(HEADING_RE.finditer(text))
        if len(matches) != len(doc_rows):
            raise SystemExit(f"STOP: {code}: HTML {len(matches)} H, mapa {len(doc_rows)}")

        # AU11 miał przed operacją 71 istniejących id; zachowujemy je. Brakował tylko pierwszy H1.
        reserved = set()
        for idx, (r, m) in enumerate(zip(doc_rows, matches), 1):
            idm = ID_RE.search(m.group("attrs") or "")
            current = idm.group(2) if idm else ""
            if not current:
                raise SystemExit(f"STOP: {code} pozycja {idx}: po poprzednim etapie brak id")
            if code == "AU11" and idx != 1:
                reserved.add(current)

        used = set(reserved)
        replacements = []
        changes = 0

        for idx, (r, m) in enumerate(zip(doc_rows, matches), 1):
            level = f"H{m.group(1)}"
            title = plain(m.group("body"))
            if level != r["poziom"] or title != r["sekcja_tytul"]:
                raise SystemExit(f"STOP: {code} pozycja {idx}: HTML i mapa rozjechane")
            idm = ID_RE.search(m.group("attrs") or "")
            current = idm.group(2)

            preserve = code == "AU11" and idx != 1
            if preserve:
                expected = current
            else:
                base = slugify(title)
                expected = base
                n = 2
                while expected in used:
                    expected = f"{base}-{n}"
                    n += 1
            used.add(expected)

            if current != expected:
                attrs_start = m.start("attrs")
                attrs_end = m.end("attrs")
                attrs = text[attrs_start:attrs_end]
                new_attrs = ID_RE.sub(lambda mm: f'id="{expected}"', attrs, count=1)
                replacements.append((attrs_start, attrs_end, new_attrs))
                changes += 1

            r["anchor"] = expected
            r["anchor_status"] = "OK"
            r["deep_link"] = r["url_zrodlowy"].rstrip("#") + "#" + expected

        for a, b, repl in sorted(replacements, reverse=True):
            text = text[:a] + repl + text[b:]

        ids = [m.group(2) for m in ID_RE.finditer(text) if m.group(2)]
        dup = [k for k,v in Counter(ids).items() if v > 1]
        if dup:
            raise SystemExit(f"STOP: {code}: duplikaty po korekcie: {dup[:10]}")
        path.write_text(text, encoding="utf-8")
        changed_total += changes
        print(f"OK {code}: poprawionych anchorow: {changes}")

    with MAP_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)

    print(f"OK: lacznie poprawionych anchorow: {changed_total}")

if __name__ == "__main__":
    main()
