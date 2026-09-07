#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://maciektora-hue.github.io/audhd"
TSV_PATH = ROOT / "SOL_mapa-sekcji-i-anchorow-audhd.tsv"
REPORT_PATH = ROOT / "SOL_raport-audyt-anchorow-audhd.txt"

DOCS = [
    ("AU01", "63-cechy-rdzen-czy-maskowanie-01_01-2026-08-26.html"),
    ("AU02", "CLAUDE_co-dziala-po-poznej-diagnozie-02_01-2026-08-26.html"),
    ("AU03", "CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html"),
    ("AU04", "CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html"),
    ("AU05", "ESEJ_architektury-pamieci-1_02-2026-04-28.html"),
    ("AU06", "POWIESC_architektury-pamieci-2_00-2026-04-29.html"),
    ("AU07", "adhd-pomaganie-kosztem-siebie-v01.00-2026-05-14.html"),
    ("AU08", "apendyks1-po-ludzku-02_01-2026-08-26.html"),
    ("AU09", "audhd-fundatorzy-it-1_00-2026-04-27.html"),
    ("AU10", "audhd-po-ludzku-v02_02-2026-07-09.html"),
    ("AU11", "audhd_opracowanie_v6_0_2026-07-01-2.html"),
    ("AU12", "autyzm-regulacja-mowienia-v01.00-2026-05-14.html"),
    ("AU13", "co-to-znaczy-audhd-v03_01-2026-07-09-2.html"),
    ("AU14", "dluga-lista-publikacji-4.01-2026-08-26.html"),
    ("AU15", "ilu-nas-jest-audhd-polska-wstep-v03_00-2026-08-10.html"),
    ("AU16", "kognitywistyka-ai-bledy-poznawcze-2_00-2026-04-28.html"),
    ("AU17", "obiektywnosc-autyzm-v01.00-2026-05-14.html"),
    ("AU18", "piec-jezykow-milosci-nd-v01.00-2026-05-18.html"),
]

HEADING_RE = re.compile(r"h([1-6])$", re.I)


def clean(parts: list[str]) -> str:
    return re.sub(r"\s+", " ", "".join(parts)).strip()


@dataclass
class Heading:
    level: int
    line: int
    ident: str | None
    text_parts: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return clean(self.text_parts)


@dataclass
class Link:
    href: str
    line: int


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.heading_stack: list[Heading] = []
        self.headings: list[Heading] = []
        self.ids: list[tuple[str, int, str]] = []
        self.links: list[Link] = []

    def handle_starttag(self, tag, attrs) -> None:
        low = tag.lower()
        attrs_d = dict(attrs)
        line, _ = self.getpos()

        if low == "title":
            self.in_title = True

        m = HEADING_RE.fullmatch(low)
        if m:
            h = Heading(int(m.group(1)), line, attrs_d.get("id"))
            self.heading_stack.append(h)
            self.headings.append(h)

        if "id" in attrs_d:
            self.ids.append((attrs_d.get("id") or "", line, low))

        if low == "a" and attrs_d.get("href") is not None:
            self.links.append(Link(attrs_d["href"], line))

    def handle_endtag(self, tag) -> None:
        low = tag.lower()
        if low == "title":
            self.in_title = False
        m = HEADING_RE.fullmatch(low)
        if m:
            level = int(m.group(1))
            for i in range(len(self.heading_stack) - 1, -1, -1):
                if self.heading_stack[i].level == level:
                    del self.heading_stack[i]
                    break

    def handle_data(self, data) -> None:
        if self.in_title:
            self.title_parts.append(data)
        for h in self.heading_stack:
            h.text_parts.append(data)

    @property
    def title(self) -> str:
        return clean(self.title_parts)


@dataclass
class Doc:
    code: str
    filename: str
    parser: Parser

    @property
    def source_url(self) -> str:
        return f"{BASE_URL}/{self.filename}"

    @property
    def targets(self) -> set[str]:
        return {ident for ident, _, _ in self.parser.ids if ident}



def parse_doc(code: str, filename: str) -> Doc:
    path = ROOT / filename
    if not path.exists():
        raise RuntimeError(f"Brak pliku źródłowego: {filename}")
    p = Parser()
    p.feed(path.read_text(encoding="utf-8"))
    p.close()
    return Doc(code, filename, p)


def hierarchy_jumps(headings: list[Heading]):
    out = []
    prev = None
    for h in headings:
        if prev is not None and h.level > prev + 1:
            out.append((h.line, prev, h.level, h.text))
        prev = h.level
    return out


def link_target(href: str, current: Doc, by_filename: dict[str, Doc]):
    parts = urlsplit(href.strip())
    if not parts.fragment:
        return None
    fragment = unquote(parts.fragment)
    if not parts.path:
        return current, fragment
    path = unquote(parts.path).replace("\\", "/")
    filename = Path(path).name
    if filename in by_filename:
        return by_filename[filename], fragment
    return None


def audit_doc(doc: Doc, by_filename: dict[str, Doc]):
    hs = doc.parser.headings
    with_id = [h for h in hs if h.ident not in (None, "")]
    missing = [h for h in hs if h.ident in (None, "")]
    all_id_counts = Counter(i for i, _, _ in doc.parser.ids if i)
    duplicates = {i: n for i, n in sorted(all_id_counts.items()) if n > 1}
    empty_ids = [(line, tag) for ident, line, tag in doc.parser.ids if ident == ""]
    broken = []
    for link in doc.parser.links:
        target = link_target(link.href, doc, by_filename)
        if target is None:
            continue
        target_doc, fragment = target
        if fragment not in target_doc.targets:
            broken.append((link.line, link.href, target_doc.code, fragment))
    counts = Counter(h.level for h in hs)
    return {
        "headings": hs,
        "with_id": with_id,
        "missing": missing,
        "duplicates": duplicates,
        "empty_ids": empty_ids,
        "broken": broken,
        "jumps": hierarchy_jumps(hs),
        "counts": counts,
    }


def write_tsv(docs: list[Doc], results: dict[str, dict]) -> None:
    header = [
        "dokument_kod", "dokument_plik", "dokument_tytul", "url_zrodlowy",
        "poziom", "glebokosc", "kolejnosc", "sekcja_tytul",
        "anchor", "anchor_status", "deep_link"
    ]
    with TSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        for doc in docs:
            title = doc.parser.title or (doc.parser.headings[0].text if doc.parser.headings else doc.filename)
            for n, h in enumerate(results[doc.code]["headings"], 1):
                anchor = h.ident or ""
                w.writerow([
                    doc.code, doc.filename, title, doc.source_url,
                    f"H{h.level}", h.level, n, h.text,
                    anchor, "OK" if anchor else "BRAK",
                    f"{doc.source_url}#{anchor}" if anchor else ""
                ])


def write_report(docs: list[Doc], results: dict[str, dict]) -> None:
    total_h = sum(len(results[d.code]["headings"]) for d in docs)
    total_with = sum(len(results[d.code]["with_id"]) for d in docs)
    total_missing = sum(len(results[d.code]["missing"]) for d in docs)
    duplicate_groups = sum(len(results[d.code]["duplicates"]) for d in docs)
    empty_ids = sum(len(results[d.code]["empty_ids"]) for d in docs)
    broken = sum(len(results[d.code]["broken"]) for d in docs)
    jumps = sum(len(results[d.code]["jumps"]) for d in docs)
    by_level = Counter()
    by_level_with = Counter()
    for d in docs:
        for h in results[d.code]["headings"]:
            by_level[h.level] += 1
            if h.ident not in (None, ""):
                by_level_with[h.level] += 1

    lines = [
        "AUDHD — RAPORT AUDYTU ANCHORÓW",
        f"Wygenerowano UTC: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        "ZAKRES",
        f"{len(docs)} merytorycznych dokumentów HTML w audhd/.",
        "Wykluczone: audhd/index.html, index-en.html, redirecty/stabilne wrappery, SOL_*, ZIP.",
        "Źródłowe HTML-e NIE są modyfikowane przez ten audyt.",
        "",
        "PODSUMOWANIE",
        f"H1–H6 sprawdzone: {total_h}",
        f"Nagłówki z id: {total_with}",
        f"Nagłówki bez id: {total_missing}",
        f"Powielone wartości id (grupy): {duplicate_groups}",
        f"Puste id: {empty_ids}",
        f"Niedziałające sprawdzalne linki #fragment: {broken}",
        f"Skoki hierarchii H o więcej niż 1 poziom: {jumps}",
        "",
        "ROZKŁAD POZIOMÓW",
    ]
    for level in range(1, 7):
        lines.append(
            f"H{level}: {by_level[level]}  | z id: {by_level_with[level]} | bez id: {by_level[level]-by_level_with[level]}"
        )

    lines += ["", "PLIK PO PLIKU"]
    for doc in docs:
        r = results[doc.code]
        c = r["counts"]
        lines += [
            "",
            f"{doc.code} — {doc.filename}",
            f"H1:{c[1]} H2:{c[2]} H3:{c[3]} H4:{c[4]} H5:{c[5]} H6:{c[6]}",
            f"RAZEM: {len(r['headings'])}; z id: {len(r['with_id'])}; bez id: {len(r['missing'])}",
            f"duplikaty id: {len(r['duplicates'])}; puste id: {len(r['empty_ids'])}; błędne #fragment: {len(r['broken'])}; skoki H: {len(r['jumps'])}",
        ]
        if r["missing"]:
            lines.append("BRAK ID PRZY NAGŁÓWKACH:")
            for h in r["missing"]:
                lines.append(f"  - linia {h.line}: H{h.level} | {h.text}")
        if r["duplicates"]:
            lines.append("POWIELONE ID:")
            for ident, n in r["duplicates"].items():
                lines.append(f"  - {ident!r}: {n} razy")
        if r["empty_ids"]:
            lines.append("PUSTE ID:")
            for line, tag in r["empty_ids"]:
                lines.append(f"  - linia {line}: <{tag} id=\"\">")
        if r["broken"]:
            lines.append("BŁĘDNE SPRAWDZALNE LINKI DO FRAGMENTÓW:")
            for line, href, target_code, fragment in r["broken"]:
                lines.append(f"  - linia {line}: {href!r} -> {target_code} brak #{fragment}")
        if r["jumps"]:
            lines.append("SKOKI HIERARCHII > 1:")
            for line, prev, cur, text in r["jumps"]:
                lines.append(f"  - linia {line}: H{prev} -> H{cur} | {text}")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    docs = [parse_doc(code, filename) for code, filename in DOCS]
    by_filename = {d.filename: d for d in docs}
    results = {d.code: audit_doc(d, by_filename) for d in docs}
    write_tsv(docs, results)
    write_report(docs, results)
    print(REPORT_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
