#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
TSV_PATH = ROOT / "SOL_mapa-sekcji-i-anchorow-rosja.tsv"
REPORT_PATH = ROOT / "SOL_raport-audyt-anchorow-rosja.txt"
BASE_URL = "https://maciektora-hue.github.io/rosja"

ORDER = [*(f"A{i}" for i in range(1, 8)),
         *(f"D{i}" for i in range(1, 8)),
         "E1", "E2"]

SLUGS = {
    "A1": "kolumbryna",
    "A2": "gradually-suddenly",
    "A3": "lista-celow",
    "A4": "przejscie-na-hurt",
    "A5": "audyt",
    "A6": "zapas-kontra-strumien",
    "A7": "jak-koncza-sie-panstwa",
    "D1": "dark-legitimacy",
    "D2": "disinfolklore",
    "D3": "disinfolklore-swot",
    "D4": "rosyjskie-samobojstwa",
    "D5": "putin-cornered",
    "D6": "jalta-3",
    "D7": "jalta-3-apendyks",
    "E1": "ropa-gaz",
    "E2": "monopole",
}
SLUG_TO_CODE = {slug: code for code, slug in SLUGS.items()}

HEADING_RE = re.compile(r"h([1-6])", re.I)
A_RE = re.compile(r"^a([1-7])(?:_|-)", re.I)
D_RE = re.compile(r"^d([1-7])(?:_|-)", re.I)


def clean_text(parts: list[str]) -> str:
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def code_for_path(path: Path) -> str | None:
    name = path.name
    m = A_RE.match(name)
    if m:
        return f"A{m.group(1)}"
    m = D_RE.match(name)
    if m:
        return f"D{m.group(1)}"
    low = name.lower()
    if low.startswith("ropa-gaz-geopolityka-") and low.endswith(".html"):
        return "E1"
    if low.startswith("monopole-moralnosc-") and low.endswith(".html"):
        return "E2"
    return None


@dataclass
class Heading:
    level: int
    text_parts: list[str] = field(default_factory=list)
    id_value: str | None = None
    line: int = 0

    @property
    def text(self) -> str:
        return clean_text(self.text_parts)


@dataclass
class Link:
    href: str
    line: int


class DocParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.heading_stack: list[Heading] = []
        self.headings: list[Heading] = []
        self.ids: list[tuple[str, int, str]] = []
        self.names: list[tuple[str, int]] = []
        self.links: list[Link] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        low = tag.lower()
        attrs_d = dict(attrs)
        line, _ = self.getpos()

        if low == "title":
            self.in_title = True

        m = HEADING_RE.fullmatch(low)
        if m:
            h = Heading(level=int(m.group(1)), id_value=attrs_d.get("id"), line=line)
            self.heading_stack.append(h)
            self.headings.append(h)

        if "id" in attrs_d:
            self.ids.append((attrs_d.get("id") or "", line, low))

        if low == "a":
            if "name" in attrs_d:
                self.names.append((attrs_d.get("name") or "", line))
            href = attrs_d.get("href")
            if href is not None:
                self.links.append(Link(href=href, line=line))

    def handle_endtag(self, tag: str) -> None:
        low = tag.lower()
        if low == "title":
            self.in_title = False
        if HEADING_RE.fullmatch(low) and self.heading_stack:
            for i in range(len(self.heading_stack) - 1, -1, -1):
                if self.heading_stack[i].level == int(low[1]):
                    del self.heading_stack[i]
                    break

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        for h in self.heading_stack:
            h.text_parts.append(data)

    @property
    def title(self) -> str:
        return clean_text(self.title_parts)


@dataclass
class Doc:
    code: str
    path: Path
    parser: DocParser

    @property
    def title(self) -> str:
        if self.parser.title:
            return self.parser.title
        if self.parser.headings:
            return self.parser.headings[0].text
        return self.path.name

    @property
    def stable_url(self) -> str:
        return f"{BASE_URL}/{SLUGS[self.code]}/"

    @property
    def targets(self) -> set[str]:
        return {v for v, _, _ in self.parser.ids if v} | {v for v, _ in self.parser.names if v}


def discover_docs() -> dict[str, Path]:
    found: dict[str, list[Path]] = defaultdict(list)
    for path in sorted(ROOT.glob("*.html")):
        code = code_for_path(path)
        if code:
            found[code].append(path)

    problems: list[str] = []
    result: dict[str, Path] = {}
    for code in ORDER:
        paths = found.get(code, [])
        if not paths:
            problems.append(f"{code}: brak pliku")
        elif len(paths) > 1:
            problems.append(f"{code}: więcej niż jeden kandydat: " + ", ".join(p.name for p in paths))
        else:
            result[code] = paths[0]

    if problems:
        raise RuntimeError("Niejednoznaczny zestaw dokumentów:\n- " + "\n- ".join(problems))
    return result


def parse_doc(code: str, path: Path) -> Doc:
    text = path.read_text(encoding="utf-8")
    parser = DocParser()
    parser.feed(text)
    parser.close()
    return Doc(code=code, path=path, parser=parser)


def href_target_code(href: str, current: Doc, by_filename: dict[str, str]) -> tuple[str | None, str | None, str | None]:
    href = href.strip()
    if href == "#":
        return current.code, "", "PUSTY_FRAGMENT"

    parts = urlsplit(href)
    fragment = unquote(parts.fragment) if parts.fragment else None
    if fragment is None:
        return None, None, None

    if parts.netloc and parts.netloc.lower() != "maciektora-hue.github.io":
        return None, fragment, None

    path = unquote(parts.path or "")
    if not path:
        return current.code, fragment, None

    normalized = path.replace("\\", "/")
    if normalized.lower().endswith(".html"):
        filename = Path(normalized).name
        code = by_filename.get(filename)
        if code:
            return code, fragment, None
        return None, fragment, "NIEZNANY_LOKALNY_CEL"

    segments = [s for s in normalized.split("/") if s and s not in (".", "..")]
    slug = None
    if "rosja" in segments:
        idx = segments.index("rosja")
        if idx + 1 < len(segments):
            slug = segments[idx + 1]
    elif segments:
        slug = segments[-1]

    if slug in SLUG_TO_CODE:
        return SLUG_TO_CODE[slug], fragment, None
    return None, fragment, "NIEZNANY_LOKALNY_CEL"


def hierarchy_jumps(headings: list[Heading]) -> list[tuple[int, int, int, str]]:
    jumps = []
    prev = None
    for h in headings:
        if prev is not None and h.level > prev + 1:
            jumps.append((h.line, prev, h.level, h.text))
        prev = h.level
    return jumps


def audit(docs: dict[str, Doc]):
    by_filename = {doc.path.name: code for code, doc in docs.items()}
    results = {}

    for code in ORDER:
        doc = docs[code]
        headings = doc.parser.headings
        heading_missing = [h for h in headings if h.id_value is None or h.id_value == ""]
        heading_with_id = [h for h in headings if h.id_value not in (None, "")]

        id_counts = Counter(v for v, _, _ in doc.parser.ids if v)
        duplicates = {k: v for k, v in sorted(id_counts.items()) if v > 1}
        empty_ids = [(line, tag) for value, line, tag in doc.parser.ids if value == ""]

        broken_links = []
        unknown_local_links = []
        empty_fragments = []
        for link in doc.parser.links:
            target_code, fragment, problem = href_target_code(link.href, doc, by_filename)
            if problem == "PUSTY_FRAGMENT":
                empty_fragments.append((link.line, link.href))
                continue
            if problem == "NIEZNANY_LOKALNY_CEL":
                unknown_local_links.append((link.line, link.href))
                continue
            if target_code is None or fragment is None:
                continue
            if fragment not in docs[target_code].targets:
                broken_links.append((link.line, link.href, target_code, fragment))

        jumps = hierarchy_jumps(headings)

        if headings and not heading_missing and not duplicates and not empty_ids and not broken_links:
            group = "ANCHORY WYGLĄDAJĄ NA KOMPLETNE"
        elif not headings or len(heading_with_id) <= max(1, len(headings) // 10):
            group = "ANCHORÓW BRAK LUB PRAWIE BRAK"
        else:
            group = "ANCHORY SĄ, ALE WYMAGAJĄ AUDYTU KOMPLETNOŚCI"

        results[code] = {
            "doc": doc,
            "headings": headings,
            "heading_missing": heading_missing,
            "heading_with_id": heading_with_id,
            "duplicates": duplicates,
            "empty_ids": empty_ids,
            "broken_links": broken_links,
            "unknown_local_links": unknown_local_links,
            "empty_fragments": empty_fragments,
            "jumps": jumps,
            "group": group,
        }
    return results


def write_tsv(results) -> None:
    header = ["dokument_kod", "dokument_plik", "dokument_tytul", "url_stabilny", "poziom", "glebokosc", "kolejnosc", "sekcja_tytul", "anchor", "anchor_status", "deep_link"]
    with TSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        for code in ORDER:
            r = results[code]
            doc = r["doc"]
            for idx, h in enumerate(r["headings"], 1):
                anchor = h.id_value or ""
                w.writerow([code, doc.path.name, doc.title, doc.stable_url, f"H{h.level}", h.level, idx, h.text, anchor, "OK" if anchor else "BRAK", f"{doc.stable_url}#{anchor}" if anchor else ""])


def write_report(results) -> None:
    total_h = sum(len(results[c]["headings"]) for c in ORDER)
    with_id = sum(len(results[c]["heading_with_id"]) for c in ORDER)
    missing = sum(len(results[c]["heading_missing"]) for c in ORDER)
    broken = sum(len(results[c]["broken_links"]) for c in ORDER)
    duplicate_groups = sum(len(results[c]["duplicates"]) for c in ORDER)
    empty_ids = sum(len(results[c]["empty_ids"]) for c in ORDER)
    jumps = sum(len(results[c]["jumps"]) for c in ORDER)

    lines = [
        "ROSJA — RAPORT AUDYTU ANCHORÓW",
        f"Wygenerowano UTC: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        "ZAKRES",
        "16 merytorycznych dokumentów: A1–A7, D1–D7, E1–E2.",
        "Źródłowe HTML-e nie są modyfikowane.",
        "",
        "PODSUMOWANIE",
        f"H1–H6 sprawdzone: {total_h}",
        f"Nagłówki z id: {with_id}",
        f"Nagłówki bez id: {missing}",
        f"Powielone wartości id (grupy): {duplicate_groups}",
        f"Puste id: {empty_ids}",
        f"Niedziałające audytowalne linki #fragment: {broken}",
        f"Skoki hierarchii H o więcej niż 1 poziom: {jumps}",
        "",
        "PLIK PO PLIKU",
    ]

    for code in ORDER:
        r = results[code]
        doc = r["doc"]
        lines.extend([
            "",
            f"{code} — {doc.path.name}",
            f"STATUS: {r['group']}",
            f"H1–H6: {len(r['headings'])}; z id: {len(r['heading_with_id'])}; bez id: {len(r['heading_missing'])}",
            f"duplikaty id: {len(r['duplicates'])}; puste id: {len(r['empty_ids'])}; błędne #fragment: {len(r['broken_links'])}; skoki H: {len(r['jumps'])}",
        ])

        if r["heading_missing"]:
            lines.append("BRAK ID PRZY NAGŁÓWKACH:")
            for h in r["heading_missing"]:
                lines.append(f"  - linia {h.line}: H{h.level} | {h.text}")

        if r["duplicates"]:
            lines.append("POWIELONE ID:")
            for ident, count in r["duplicates"].items():
                lines.append(f"  - {ident!r}: {count} razy")

        if r["empty_ids"]:
            lines.append("PUSTE ID:")
            for line, tag in r["empty_ids"]:
                lines.append(f"  - linia {line}: <{tag} id=\"\">")

        if r["broken_links"]:
            lines.append("BŁĘDNE LINKI DO FRAGMENTÓW:")
            for line, href, target, fragment in r["broken_links"]:
                lines.append(f"  - linia {line}: {href!r} -> {target} brak #{fragment}")

        if r["empty_fragments"]:
            lines.append("PUSTE FRAGMENTY href=\"#\":")
            for line, href in r["empty_fragments"]:
                lines.append(f"  - linia {line}: {href!r}")

        if r["unknown_local_links"]:
            lines.append("LOKALNE LINKI Z FRAGMENTEM POZA 16 DOKUMENTAMI (nie oceniono celu):")
            for line, href in r["unknown_local_links"]:
                lines.append(f"  - linia {line}: {href!r}")

        if r["jumps"]:
            lines.append("SKOKI HIERARCHII:")
            for line, prev, cur, text in r["jumps"]:
                lines.append(f"  - linia {line}: H{prev} -> H{cur} | {text}")

    largest = sorted(((len(results[c]["heading_missing"]), c, results[c]["doc"].path.name) for c in ORDER), reverse=True)
    lines.extend(["", "NAJWIĘKSZE BRAKI ID"])
    for count, code, filename in largest:
        if count:
            lines.append(f"- {code}: {count} | {filename}")
    if not any(count for count, _, _ in largest):
        lines.append("- brak")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    paths = discover_docs()
    docs = {code: parse_doc(code, paths[code]) for code in ORDER}
    results = audit(docs)
    write_tsv(results)
    write_report(results)

    total_h = sum(len(results[c]["headings"]) for c in ORDER)
    missing = sum(len(results[c]["heading_missing"]) for c in ORDER)
    broken = sum(len(results[c]["broken_links"]) for c in ORDER)
    print(f"OK: 16 dokumentów; H1–H6={total_h}; bez id={missing}; błędne fragmenty={broken}")
    print(TSV_PATH)
    print(REPORT_PATH)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"AUDYT NIE WYKONANY: {exc}", file=sys.stderr)
        raise
