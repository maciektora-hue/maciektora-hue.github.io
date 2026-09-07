#!/usr/bin/env python3
from __future__ import annotations

import csv
import html
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAP_PATH = ROOT / "SOL_mapa-sekcji-i-anchorow-audhd.tsv"
MANIFEST_PATH = ROOT / "SOL_reczne-anchory-audhd.tsv"

HEADING_RE = re.compile(r"<h([1-6])(?P<attrs>[^>]*)>(?P<body>.*?)</h\1\s*>", re.I | re.S)
ID_RE = re.compile(r"\bid\s*=\s*([\"'])(.*?)\1", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def plain(s: str) -> str:
    return WS_RE.sub(" ", html.unescape(TAG_RE.sub(" ", s))).strip()


def load_manifest():
    with MANIFEST_PATH.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    required = {"dokument_kod", "dokument_plik", "poziom", "sekcja_tytul", "anchor"}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit("STOP: zly lub pusty manifest anchorow")
    seen = set()
    for r in rows:
        key = (r["dokument_kod"], r["dokument_plik"], r["poziom"], r["sekcja_tytul"])
        if key in seen:
            raise SystemExit(f"STOP: duplikat wpisu w manifeście: {key}")
        seen.add(key)
        if not r["anchor"].strip():
            raise SystemExit(f"STOP: pusty anchor w manifeście: {key}")
    return rows


def apply_to_file(path: Path, mappings: list[dict]) -> None:
    text = path.read_text(encoding="utf-8")
    existing_ids = [m.group(2) for m in ID_RE.finditer(text) if m.group(2)]
    counts = Counter(existing_ids)
    dupes = [k for k, v in counts.items() if v > 1]
    if dupes:
        raise SystemExit(f"STOP: plik juz ma duplikaty id {path.name}: {dupes[:10]}")

    desired = [r["anchor"] for r in mappings]
    if len(desired) != len(set(desired)):
        raise SystemExit(f"STOP: manifest tworzy duplikaty anchorow w {path.name}")

    matches = list(HEADING_RE.finditer(text))
    replacements = []

    for r in mappings:
        level = r["poziom"].upper()
        if not re.fullmatch(r"H[1-6]", level):
            raise SystemExit(f"STOP: zly poziom {level} w manifeście")
        n = level[1]
        title = r["sekcja_tytul"]
        anchor = r["anchor"]

        candidates = [m for m in matches if m.group(1) == n and plain(m.group("body")) == title]
        if len(candidates) != 1:
            raise SystemExit(f"STOP: {path.name} | {level} | {title!r}: znaleziono {len(candidates)} naglowkow")
        m = candidates[0]
        attrs = m.group("attrs") or ""
        idm = ID_RE.search(attrs)
        if idm:
            current = idm.group(2)
            if current != anchor:
                raise SystemExit(f"STOP: istniejący id inny niz manifest: {path.name} | {title!r} | {current!r} != {anchor!r}")
            continue

        if anchor in counts:
            raise SystemExit(f"STOP: anchor {anchor!r} juz istnieje gdzie indziej w {path.name}")

        start_tag_end = m.start("body")
        opening = text[m.start():start_tag_end]
        if not opening.endswith(">"):
            raise SystemExit(f"STOP: nie umiem wstawic id do {path.name} | {title!r}")
        new_opening = opening[:-1] + f' id="{anchor}">'
        replacements.append((m.start(), start_tag_end, new_opening))
        counts[anchor] += 1

    for a, b, repl in sorted(replacements, reverse=True):
        text = text[:a] + repl + text[b:]

    # walidacja po zmianie
    ids_after = [m.group(2) for m in ID_RE.finditer(text) if m.group(2)]
    dup_after = [k for k, v in Counter(ids_after).items() if v > 1]
    if dup_after:
        raise SystemExit(f"STOP: po zmianie powstaly duplikaty id w {path.name}: {dup_after[:10]}")

    for r in mappings:
        anchor = r["anchor"]
        if ids_after.count(anchor) != 1:
            raise SystemExit(f"STOP: po zmianie anchor {anchor!r} nie wystepuje dokladnie raz w {path.name}")

    path.write_text(text, encoding="utf-8")
    print(f"OK HTML: {path.name} | mapowanych anchorow: {len(mappings)} | nowych: {len(replacements)}")


def update_map(manifest: list[dict]) -> None:
    with MAP_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    if not fields:
        raise SystemExit("STOP: mapa TSV bez naglowka")
    if len(rows) != 338:
        raise SystemExit(f"STOP: oczekiwano 338 wierszy mapy, jest {len(rows)}")

    for r in manifest:
        candidates = [x for x in rows if x["dokument_kod"] == r["dokument_kod"] and x["dokument_plik"] == r["dokument_plik"] and x["poziom"] == r["poziom"] and x["sekcja_tytul"] == r["sekcja_tytul"]]
        if len(candidates) != 1:
            raise SystemExit(f"STOP: mapa TSV: dla wpisu manifestu znaleziono {len(candidates)} wierszy: {r}")
        x = candidates[0]
        if x["anchor"] and x["anchor"] != r["anchor"]:
            raise SystemExit(f"STOP: mapa ma inny anchor: {x['anchor']!r} != {r['anchor']!r}")
        x["anchor"] = r["anchor"]
        x["anchor_status"] = "OK"
        x["deep_link"] = x["url_stabilny"].rstrip("#") + "#" + r["anchor"]

    with MAP_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    ok = sum(1 for x in rows if x["anchor_status"] == "OK" and x["anchor"])
    brak = sum(1 for x in rows if not x["anchor"])
    print(f"OK TSV: 338 wierszy | z anchorami: {ok} | bez anchorow: {brak}")


def main() -> None:
    manifest = load_manifest()
    by_file = defaultdict(list)
    for r in manifest:
        by_file[r["dokument_plik"]].append(r)

    for filename, mappings in by_file.items():
        path = ROOT / filename
        if not path.exists():
            raise SystemExit(f"STOP: brak pliku {filename}")
        apply_to_file(path, mappings)

    update_map(manifest)


if __name__ == "__main__":
    main()
