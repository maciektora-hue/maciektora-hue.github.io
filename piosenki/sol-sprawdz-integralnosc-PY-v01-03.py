#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SOL — kontrola integralności danych serwera piosenek.

Uruchomienie:
    python sol-sprawdz-integralnosc-PY-v01-03.py /sciezka/do/katalogu

Jeśli katalog nie jest podany, skrypt sprawdza bieżący katalog.
Wybiera najwyższą wersję każdego aktywnego pliku danych.
Lyrics może być fizycznie podzielone na kilka rodzin plików
sol-piosenki-slowa[-NAZWA]-CSV-vNN-NN.csv; z każdej rodziny wybierana
jest najwyższa wersja, a wszystkie wybrane fragmenty tworzą jedną
logiczną tabelę Lyrics.

Skrypt niczego nie zmienia. Tylko czyta, sprawdza i zwraca kod:
    0 = brak błędów integralności
    1 = są błędy integralności
    2 = brak wymaganych plików / problem uruchomieniowy

Tylko Python standard library. Bez pandas, bez SQLite na dysku.
"""

from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
UTWU_RE = re.compile(r"^utwu-\d{6}$")
LYRICS_RE = re.compile(r"^lyrics-\d{6}$")
VERSION_RE = re.compile(r"-v(\d+)-(\d+)\.(?:csv|txt)$", re.IGNORECASE)

FILES = {
    "middle": re.compile(r"^sol-middleend-CSV-v\d+-\d+\.csv$", re.IGNORECASE),
    "snapshots": re.compile(r"^sol-piosenki-tagi-CSV-v\d+-\d+\.csv$", re.IGNORECASE),
    "tagdefs": re.compile(r"^sol-definicje-tagow-CSV-v\d+-\d+\.csv$", re.IGNORECASE),
    "ontology": re.compile(r"^sol-ontologia-tagow-TXT-v\d+-\d+\.txt$", re.IGNORECASE),
}

LYRICS_FRAGMENT_RE = re.compile(
    r"^(sol-piosenki-slowa(?:-[A-Za-z0-9_-]+)?)-CSV-v\d+-\d+\.csv$",
    re.IGNORECASE,
)

TEXT_STATUSES = {"full", "canonicaltext", "partial", "paraphase"}
NO_TEXT_STATUSES = {"missing", "instrumental"}
KNOWN_LYRICS_STATUSES = TEXT_STATUSES | NO_TEXT_STATUSES

HEADERS = {
    "middle": [
        "utwu_id", "lyrics_id", "spotify_id", "spotify_order",
        "title_original", "title_normalized", "title_parsed",
        "artist_original", "artist_normalized", "artist_parsed",
        "album_original", "match_status", "match_candidates",
        "match_note", "lyrics_status",
    ],
    "lyrics": ["lyrics_id", "lyrics_text"],
    "snapshots": ["lyrics_id", "tagged_at", "tags"],
    "tagdefs": ["tag", "definition"],
}


@dataclass
class Row:
    line: int
    data: dict[str, str]


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def note(self, msg: str) -> None:
        self.info.append(msg)

    def print(self) -> None:
        print("\n=== SOL: KONTROLA INTEGRALNOŚCI ===")
        for msg in self.info:
            print(f"[INFO] {msg}")
        for msg in self.warnings:
            print(f"[WARN] {msg}")
        for msg in self.errors:
            print(f"[ERROR] {msg}")
        print("\n--- PODSUMOWANIE ---")
        print(f"błędy: {len(self.errors)}")
        print(f"ostrzeżenia: {len(self.warnings)}")
        if self.errors:
            print("WYNIK: FAIL")
        else:
            print("WYNIK: OK")


def version_of(path: Path) -> tuple[int, int]:
    m = VERSION_RE.search(path.name)
    if not m:
        return (-1, -1)
    return int(m.group(1)), int(m.group(2))


def latest_matching(folder: Path, rx: re.Pattern[str]) -> tuple[Path | None, list[Path]]:
    matches = [p for p in folder.iterdir() if p.is_file() and rx.fullmatch(p.name)]
    matches.sort(key=lambda p: (version_of(p), p.name))
    return (matches[-1] if matches else None, matches)


def latest_lyrics_fragments(folder: Path) -> tuple[list[Path], dict[str, list[Path]]]:
    """Wybierz najwyższą wersję z każdej fizycznej rodziny Lyrics."""
    families: dict[str, list[Path]] = collections.defaultdict(list)
    for p in folder.iterdir():
        if not p.is_file():
            continue
        m = LYRICS_FRAGMENT_RE.fullmatch(p.name)
        if m:
            families[m.group(1).casefold()].append(p)

    selected: list[Path] = []
    for family in sorted(families):
        versions = sorted(families[family], key=lambda p: (version_of(p), p.name))
        selected.append(versions[-1])
        families[family] = versions
    return selected, dict(families)


def load_csv(path: Path, expected_header: list[str], report: Report) -> list[Row]:
    rows: list[Row] = []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
            except StopIteration:
                report.error(f"{path.name}: pusty plik CSV")
                return rows
            if header != expected_header:
                report.error(
                    f"{path.name}: zły nagłówek. Jest {header!r}, oczekiwano {expected_header!r}"
                )
            for line, values in enumerate(reader, start=2):
                if len(values) != len(header):
                    report.error(
                        f"{path.name}:{line}: {len(values)} pól zamiast {len(header)}"
                    )
                    continue
                if any("\x00" in v for v in values):
                    report.error(f"{path.name}:{line}: znak NUL w danych")
                rows.append(Row(line, dict(zip(header, values))))
    except (OSError, UnicodeError, csv.Error) as e:
        report.error(f"{path.name}: nie da się poprawnie odczytać CSV: {e}")
    return rows


def duplicates(values: Iterable[str]) -> dict[str, int]:
    c = collections.Counter(v for v in values if v != "")
    return {k: n for k, n in c.items() if n > 1}


def sample(items: Iterable[str], limit: int = 8) -> str:
    vals = list(items)
    shown = vals[:limit]
    s = ", ".join(shown)
    if len(vals) > limit:
        s += f", ... (+{len(vals) - limit})"
    return s


def parse_iso_datetime(value: str) -> bool:
    if not value:
        return True
    try:
        dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        try:
            dt.date.fromisoformat(value)
            return True
        except ValueError:
            return False


def parse_tag_cell(cell: str, where: str, report: Report) -> list[tuple[str, list[str]]]:
    if not cell:
        return []
    if re.search(r";(?! )", cell):
        report.error(f"{where}: separator tagów musi być dokładnie '; '")
    out: list[tuple[str, list[str]]] = []
    for raw in cell.split("; "):
        if not raw:
            report.error(f"{where}: pusty element na liście tagów")
            continue
        if raw.count(":") > 1:
            report.error(f"{where}: więcej niż jeden ':' w elemencie {raw!r}")
            continue
        if ":" in raw:
            tag, qtext = raw.split(":", 1)
            quals = qtext.split("|") if qtext else []
            if not quals:
                report.error(f"{where}: ':' bez kwalifikatora dla taga {tag!r}")
        else:
            tag, quals = raw, []
        if not TAG_RE.fullmatch(tag):
            report.error(f"{where}: niedozwolona nazwa taga {tag!r}")
        for q in quals:
            if not TAG_RE.fullmatch(q):
                report.error(f"{where}: niedozwolony kwalifikator {q!r} przy tagu {tag!r}")
        out.append((tag, quals))
    return out


def check_tagdefs(rows: list[Row], report: Report) -> set[str]:
    tags = [r.data.get("tag", "") for r in rows]
    for r in rows:
        tag = r.data.get("tag", "")
        if not tag:
            report.error(f"tagdefs:{r.line}: pusty tag")
        elif not TAG_RE.fullmatch(tag):
            report.error(f"tagdefs:{r.line}: nazwa poza regułą literki/cyfry/minusy: {tag!r}")
    dup = duplicates(tags)
    if dup:
        report.error(f"tagdefs: duplikaty klucza tag: {sample(sorted(dup))}")
    blanks = sum(1 for r in rows if not r.data.get("definition", ""))
    report.note(f"słownik tagów: {len(rows)} rekordów, {blanks} bez opisu")
    return set(tags)


def check_lyrics(rows: list[Row], report: Report) -> tuple[set[str], dict[str, Row]]:
    ids = [r.data.get("lyrics_id", "") for r in rows]
    by_id: dict[str, Row] = {}
    for r in rows:
        lid = r.data.get("lyrics_id", "")
        text = r.data.get("lyrics_text", "")
        if not LYRICS_RE.fullmatch(lid):
            report.error(f"lyrics:{r.line}: zły lyrics_id {lid!r}")
        if not text:
            report.error(f"lyrics:{r.line}: pusty lyrics_text dla {lid!r}")
        by_id[lid] = r
    dup_ids = duplicates(ids)
    if dup_ids:
        report.error(f"lyrics: duplikaty PRIMARY KEY lyrics_id: {sample(sorted(dup_ids))}")
    text_counts = collections.Counter(r.data.get("lyrics_text", "") for r in rows if r.data.get("lyrics_text", ""))
    dup_texts = sum(1 for n in text_counts.values() if n > 1)
    if dup_texts:
        report.error(f"lyrics: {dup_texts} dokładnych tekstów zapisanych pod więcej niż jednym lyrics_id")
    report.note(f"lyrics: {len(rows)} unikalnych rekordów tekstu")
    return set(ids), by_id


def check_middle(rows: list[Row], lyrics_ids: set[str], report: Report) -> set[str]:
    utwu = [r.data.get("utwu_id", "") for r in rows]
    spotify = [r.data.get("spotify_id", "") for r in rows]
    orders = [r.data.get("spotify_order", "") for r in rows]
    referenced_lyrics: set[str] = set()

    for r in rows:
        d = r.data
        uid = d.get("utwu_id", "")
        lid = d.get("lyrics_id", "")
        status = d.get("lyrics_status", "")
        sid = d.get("spotify_id", "")
        order = d.get("spotify_order", "")
        if not UTWU_RE.fullmatch(uid):
            report.error(f"middle:{r.line}: zły utwu_id {uid!r}")
        if lid:
            referenced_lyrics.add(lid)
            if not LYRICS_RE.fullmatch(lid):
                report.error(f"middle:{r.line}: zły lyrics_id {lid!r}")
            elif lid not in lyrics_ids:
                report.error(f"middle:{r.line}: lyrics_id {lid!r} nie istnieje w tabeli lyrics")
        if status in TEXT_STATUSES and not lid:
            report.error(f"middle:{r.line}: lyrics_status={status!r}, ale lyrics_id jest pusty")
        if status in NO_TEXT_STATUSES and lid:
            report.error(f"middle:{r.line}: lyrics_status={status!r}, ale lyrics_id={lid!r}")
        if status not in KNOWN_LYRICS_STATUSES:
            report.warn(f"middle:{r.line}: nieznany lyrics_status {status!r}")
        if order:
            try:
                if int(order) <= 0:
                    raise ValueError
            except ValueError:
                report.error(f"middle:{r.line}: spotify_order nie jest dodatnią liczbą całkowitą: {order!r}")
        if bool(sid) != bool(order):
            report.warn(f"middle:{r.line}: spotify_id i spotify_order nie są jednocześnie puste/niepuste")

    if duplicates(utwu):
        report.error(f"middle: duplikaty PRIMARY KEY utwu_id: {sample(sorted(duplicates(utwu)))}")
    if duplicates(spotify):
        report.error(f"middle: powtórzony niepusty spotify_id: {sample(sorted(duplicates(spotify)))}")
    if duplicates(orders):
        report.error(f"middle: powtórzony niepusty spotify_order: {sample(sorted(duplicates(orders)))}")
    report.note(
        f"middle end: {len(rows)} rekordów, {len(referenced_lyrics)} różnych niepustych lyrics_id"
    )
    return referenced_lyrics


def check_snapshots(rows: list[Row], lyrics_ids: set[str], tagdefs: set[str], report: Report) -> None:
    exact_rows: collections.Counter[tuple[str, str, str]] = collections.Counter()
    same_moment: collections.Counter[tuple[str, str]] = collections.Counter()
    used_tags: set[str] = set()
    total_assignments = 0

    for r in rows:
        d = r.data
        lid = d.get("lyrics_id", "")
        when = d.get("tagged_at", "")
        cell = d.get("tags", "")
        where = f"snapshots:{r.line} ({lid or 'brak lyrics_id'})"

        if not LYRICS_RE.fullmatch(lid):
            report.error(f"{where}: zły lyrics_id {lid!r}")
        elif lid not in lyrics_ids:
            report.error(f"{where}: lyrics_id nie istnieje w lyrics")
        if cell and not when:
            report.error(f"{where}: są tagi, ale tagged_at jest pusty")
        if when and not cell:
            report.error(f"{where}: tagged_at jest ustawiony, ale tags jest puste")
        if when and not parse_iso_datetime(when):
            report.error(f"{where}: tagged_at nie jest ISO date/datetime: {when!r}")

        assignments = parse_tag_cell(cell, where, report)
        total_assignments += len(assignments)
        tags_here = [tag for tag, _ in assignments]
        used_tags.update(tags_here)

        dup_here = duplicates(tags_here)
        if dup_here:
            report.error(
                f"{where}: ten sam tag występuje wielokrotnie w jednym snapshotcie: "
                f"{sample(sorted(dup_here))}"
            )

        unknown = sorted({tag for tag in tags_here if tag not in tagdefs})
        if unknown:
            report.error(f"{where}: tagi bez definicji w słowniku: {sample(unknown)}")

        exact_rows[(lid, when, cell)] += 1
        if when:
            same_moment[(lid, when)] += 1

    exact_dups = [k for k, n in exact_rows.items() if n > 1]
    if exact_dups:
        report.warn(
            f"snapshots: {len(exact_dups)} identycznych rekordów występuje więcej niż raz "
            "(to nie jest automatycznie błąd, bo snapshot nie ma formalnego PK)"
        )
    same_time_dups = [k for k, n in same_moment.items() if n > 1]
    if same_time_dups:
        report.note(
            f"snapshots: {len(same_time_dups)} par (lyrics_id, tagged_at) występuje więcej niż raz; "
            "to jest dozwolone, bo jeden lyrics_id może mieć wiele snapshotów, a historyczne tagged_at "
            "może zawierać tylko datę"
        )

    report.note(
        f"snapshots: {len(rows)} rekordów, {total_assignments} przypisań tagów, "
        f"{len(used_tags)} różnych użytych tagów"
    )


def check_ontology(path: Path, tagdefs: set[str], report: Report) -> None:
    try:
        sql = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as e:
        report.error(f"{path.name}: nie da się odczytać TXT/SQL: {e}")
        return

    con = sqlite3.connect(":memory:")
    try:
        con.execute("PRAGMA foreign_keys=ON")
        con.executescript(sql)
    except sqlite3.Error as e:
        report.error(f"{path.name}: SQL nie wykonuje się w SQLite: {e}")
        con.close()
        return

    expected = {"families", "tag_groups", "axes", "tag_group", "tag_axis"}
    actual = {
        r[0]
        for r in con.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
    }
    missing = sorted(expected - actual)
    if missing:
        report.error(f"ontologia: brak tabel: {sample(missing)}")

    fk_violations = con.execute("PRAGMA foreign_key_check").fetchall()
    if fk_violations:
        report.error(f"ontologia: {len(fk_violations)} naruszeń wewnętrznych FOREIGN KEY")

    if "tag_group" in actual:
        tg_tags = {r[0] for r in con.execute("SELECT tag FROM tag_group")}
        unknown = sorted(tg_tags - tagdefs)
        missing_rel = sorted(tagdefs - tg_tags)
        if unknown:
            report.error(f"ontologia/tag_group: tagi nieistniejące w słowniku CSV: {sample(unknown)}")
        if missing_rel:
            report.error(f"ontologia/tag_group: tagi bez żadnej grupy: {sample(missing_rel)}")

    if "tag_axis" in actual:
        ta_tags = {r[0] for r in con.execute("SELECT tag FROM tag_axis")}
        unknown = sorted(ta_tags - tagdefs)
        missing_rel = sorted(tagdefs - ta_tags)
        if unknown:
            report.error(f"ontologia/tag_axis: tagi nieistniejące w słowniku CSV: {sample(unknown)}")
        if missing_rel:
            report.error(f"ontologia/tag_axis: tagi bez żadnej osi: {sample(missing_rel)}")

    counts = {}
    for table in sorted(expected & actual):
        counts[table] = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    if counts:
        report.note("ontologia SQL: " + ", ".join(f"{k}={v}" for k, v in counts.items()))
    con.close()


def main() -> int:
    ap = argparse.ArgumentParser(description="SOL — kontrola integralności danych piosenek")
    ap.add_argument("folder", nargs="?", default=".", help="katalog z aktywnymi plikami danych")
    args = ap.parse_args()
    folder = Path(args.folder).expanduser().resolve()

    if not folder.is_dir():
        print(f"BŁĄD: nie ma katalogu: {folder}", file=sys.stderr)
        return 2

    report = Report()
    selected: dict[str, Path] = {}
    for key, rx in FILES.items():
        latest, all_matches = latest_matching(folder, rx)
        if latest is None:
            print(f"BŁĄD: brak pliku dla {key} w {folder}", file=sys.stderr)
            return 2
        selected[key] = latest
        report.note(f"{key}: {latest.name}")
        if len(all_matches) > 1:
            older = [p.name for p in all_matches[:-1]]
            report.note(f"{key}: pomijam starsze wersje: {sample(older)}")

    lyrics_files, lyrics_families = latest_lyrics_fragments(folder)
    if not lyrics_files:
        print(f"BŁĄD: brak fizycznych plików Lyrics w {folder}", file=sys.stderr)
        return 2

    lyrics_rows: list[Row] = []
    for p in lyrics_files:
        report.note(f"lyrics fragment: {p.name}")
        family = LYRICS_FRAGMENT_RE.fullmatch(p.name).group(1).casefold()
        older = [q.name for q in lyrics_families[family][:-1]]
        if older:
            report.note(f"lyrics fragment {family}: pomijam starsze wersje: {sample(older)}")
        lyrics_rows.extend(load_csv(p, HEADERS["lyrics"], report))

    tagdef_rows = load_csv(selected["tagdefs"], HEADERS["tagdefs"], report)
    middle_rows = load_csv(selected["middle"], HEADERS["middle"], report)
    snapshot_rows = load_csv(selected["snapshots"], HEADERS["snapshots"], report)

    tagdefs = check_tagdefs(tagdef_rows, report)
    lyrics_ids, _ = check_lyrics(lyrics_rows, report)
    referenced_lyrics = check_middle(middle_rows, lyrics_ids, report)
    check_snapshots(snapshot_rows, lyrics_ids, tagdefs, report)
    check_ontology(selected["ontology"], tagdefs, report)

    orphan_lyrics = sorted(lyrics_ids - referenced_lyrics)
    if orphan_lyrics:
        report.note(
            f"lyrics: {len(orphan_lyrics)} tekstów nie jest obecnie wskazywanych przez Middle End "
            f"(dozwolone w modelu Lyrics 1 -> 0..N Middle End): {sample(orphan_lyrics)}"
        )

    report.print()
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
