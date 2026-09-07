#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAP_PATH = ROOT / "SOL_mapa-sekcji-i-anchorow-audhd.tsv"
MANIFEST_PATH = ROOT / "SOL_reczne-anchory-audhd.tsv"

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


def plain(s: str) -> str:
    return WS_RE.sub(" ", html.unescape(TAG_RE.sub(" ", s))).strip()


def slugify(title: str) -> str:
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "sekcja"


def code_from_manifest() -> str:
    with MANIFEST_PATH.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows or not rows[0].get("dokument_kod"):
        raise SystemExit("STOP: nie podano --code i manifest nie wskazuje dokumentu")
    return rows[0]["dokument_kod"]


def load_map():
    with MAP_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    if not fields:
        raise SystemExit("STOP: mapa TSV bez naglowka")
    if len(rows) != 338:
        raise SystemExit(f"STOP: oczekiwano 338 wierszy mapy, jest {len(rows)}")
    required = {"dokument_kod", "dokument_plik", "poziom", "kolejnosc", "sekcja_tytul", "anchor", "anchor_status", "deep_link", "url_zrodlowy"}
    if not required.issubset(fields):
        raise SystemExit(f"STOP: mapa TSV nie ma wymaganych kolumn: {sorted(required - set(fields))}")
    return fields, rows


def process(code: str) -> None:
    if code not in FILES:
        raise SystemExit(f"STOP: nieznany kod dokumentu: {code}")
    filename = FILES[code]
    path = ROOT / filename
    if not path.exists():
        raise SystemExit(f"STOP: brak pliku {filename}")

    fields, rows = load_map()
    doc_rows = [r for r in rows if r["dokument_kod"] == code]
    doc_rows.sort(key=lambda r: int(r["kolejnosc"]))
    if not doc_rows:
        raise SystemExit(f"STOP: brak wierszy {code} w mapie")
    if any(r["dokument_plik"] != filename for r in doc_rows):
        raise SystemExit(f"STOP: mapa {code} wskazuje inny plik")

    text = path.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    if len(matches) != len(doc_rows):
        raise SystemExit(f"STOP: {code}: HTML ma {len(matches)} H1-H6, mapa ma {len(doc_rows)}")

    existing_ids = [m.group(2) for m in ID_RE.finditer(text) if m.group(2)]
    dupes = [k for k, v in Counter(existing_ids).items() if v > 1]
    if dupes:
        raise SystemExit(f"STOP: {code}: istnieja duplikaty id: {dupes[:10]}")
    used = set(existing_ids)
    replacements = []
    added = 0
    preserved = 0

    for idx, (r, m) in enumerate(zip(doc_rows, matches), 1):
        html_level = f"H{m.group(1)}"
        html_title = plain(m.group("body"))
        if html_level != r["poziom"] or html_title != r["sekcja_tytul"]:
            raise SystemExit(
                f"STOP: {code} pozycja {idx}: HTML=({html_level}, {html_title!r}) mapa=({r['poziom']}, {r['sekcja_tytul']!r})"
            )

        attrs = m.group("attrs") or ""
        idm = ID_RE.search(attrs)
        current = idm.group(2) if idm else ""

        if current:
            if r["anchor"] and r["anchor"] != current:
                raise SystemExit(f"STOP: {code} pozycja {idx}: mapa ma {r['anchor']!r}, HTML ma {current!r}")
            anchor = current
            preserved += 1
        else:
            if r["anchor"]:
                anchor = r["anchor"]
            else:
                base = slugify(r["sekcja_tytul"])
                anchor = base
                n = 2
                while anchor in used:
                    anchor = f"{base}-{n}"
                    n += 1
            if anchor in used:
                raise SystemExit(f"STOP: {code}: nowy anchor {anchor!r} juz istnieje")
            opening = text[m.start():m.start("body")]
            if not opening.endswith(">"):
                raise SystemExit(f"STOP: {code} pozycja {idx}: nie umiem wstawic id")
            replacements.append((m.start(), m.start("body"), opening[:-1] + f' id="{anchor}">'))
            used.add(anchor)
            added += 1

        r["anchor"] = anchor
        r["anchor_status"] = "OK"
        r["deep_link"] = r["url_zrodlowy"].rstrip("#") + "#" + anchor

    for a, b, repl in sorted(replacements, reverse=True):
        text = text[:a] + repl + text[b:]

    ids_after = [m.group(2) for m in ID_RE.finditer(text) if m.group(2)]
    dup_after = [k for k, v in Counter(ids_after).items() if v > 1]
    if dup_after:
        raise SystemExit(f"STOP: {code}: po zmianie duplikaty id: {dup_after[:10]}")
    for r in doc_rows:
        if ids_after.count(r["anchor"]) != 1:
            raise SystemExit(f"STOP: {code}: anchor {r['anchor']!r} nie wystepuje dokladnie raz")

    path.write_text(text, encoding="utf-8")
    with MAP_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    ok = sum(1 for r in rows if r["anchor_status"] == "OK" and r["anchor"])
    brak = sum(1 for r in rows if not r["anchor"])
    print(f"OK {code}: {filename} | sekcji: {len(doc_rows)} | zachowane id: {preserved} | dodane id: {added}")
    print(f"OK TSV: 338 wierszy | z anchorami: {ok} | bez anchorow: {brak}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--code")
    args = ap.parse_args()
    code = args.code or code_from_manifest()
    process(code)


if __name__ == "__main__":
    main()
