#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from html.parser import HTMLParser
from pathlib import Path

MAP = Path('audhd/SOL_mapa-sekcji-i-anchorow-audhd.tsv')
OUT = Path('SOL_opisy-sekcji-audhd.txt')

BLOCK_TAGS = {'p', 'li', 'blockquote', 'td'}
HEADING_TAGS = {f'h{i}' for i in range(1, 7)}


def clean(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


class SectionParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.current_anchor = None
        self.current_level = None
        self.heading_parts = []
        self.in_heading = False
        self.block_tag = None
        self.block_parts = []
        self.sections = {}
        self.lang = 'pl'

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html' and attrs.get('lang'):
            self.lang = attrs['lang'].lower()
        if tag in HEADING_TAGS:
            self._finish_block()
            self.current_anchor = attrs.get('id') or ''
            self.current_level = int(tag[1])
            self.heading_parts = []
            self.in_heading = True
            if self.current_anchor:
                self.sections.setdefault(self.current_anchor, {
                    'title': '', 'level': self.current_level, 'blocks': [], 'lang': self.lang
                })
            return
        if self.current_anchor and tag in BLOCK_TAGS and self.block_tag is None:
            self.block_tag = tag
            self.block_parts = []

    def handle_endtag(self, tag):
        if tag in HEADING_TAGS and self.in_heading:
            self.in_heading = False
            if self.current_anchor:
                self.sections[self.current_anchor]['title'] = clean(' '.join(self.heading_parts))
            return
        if tag == self.block_tag:
            self._finish_block()

    def handle_data(self, data):
        if self.in_heading:
            self.heading_parts.append(data)
        elif self.block_tag is not None:
            self.block_parts.append(data)

    def _finish_block(self):
        if self.block_tag is not None and self.current_anchor:
            text = clean(' '.join(self.block_parts))
            if text:
                self.sections[self.current_anchor]['blocks'].append(text)
        self.block_tag = None
        self.block_parts = []

    def close(self):
        self._finish_block()
        super().close()


def useful_block(s: str) -> bool:
    low = s.lower()
    if len(s) < 18:
        return False
    if low.startswith(('plik:', 'wersja:', 'data:', 'godzina:', 'źródło pliku:', 'source file:')):
        return False
    if re.fullmatch(r'https?://\S+', s):
        return False
    return True


def clip_sentence(text: str, limit: int = 260) -> str:
    text = clean(text)
    if len(text) <= limit:
        return text
    candidate = text[:limit + 1]
    stops = [m.end() for m in re.finditer(r'[.!?](?:\s|$)', candidate)]
    good = [p for p in stops if p >= 90]
    if good:
        return candidate[:good[-1]].strip()
    cut = candidate.rfind(' ', 120, limit)
    if cut < 0:
        cut = limit
    return candidate[:cut].rstrip(' ,;:') + '…'


def generic(title: str, doc_title: str, lang: str) -> str:
    t = clean(title)
    low = t.lower()
    if lang.startswith('en'):
        if 'source' in low or 'bibliograph' in low or 'reference' in low:
            return 'Sources and references used in this part of the document.'
        if 'summary' in low or 'conclusion' in low or 'verdict' in low:
            return 'Summary of the main arguments and conclusions developed in this part of the document.'
        if 'contents' in low:
            return 'Navigation list of the document’s sections and subsections.'
        return f'Discussion of “{t}” in the context of “{doc_title}”.'
    if 'źród' in low or 'bibliograf' in low or 'literatur' in low:
        return 'Źródła i literatura wykorzystane w tej części opracowania.'
    if 'spis treści' in low:
        return 'Nawigacyjny spis sekcji i podsekcji dokumentu.'
    if 'streszczenie' in low:
        return 'Syntetyczne przedstawienie najważniejszych tez, założeń i wniosków tej części opracowania.'
    if 'podsum' in low or 'konkluz' in low or 'wnios' in low or 'sedno' == low:
        return 'Podsumowanie głównych tez i wniosków rozwiniętych w tej części opracowania.'
    return f'Omówienie zagadnienia „{t}” w kontekście opracowania „{doc_title}”.'


def describe(section: dict, title: str, doc_title: str) -> str:
    lang = section.get('lang', 'pl')
    blocks = [b for b in section.get('blocks', []) if useful_block(b)]
    if blocks:
        # Pomijamy bloki, które są w praktyce tylko powtórzeniem nagłówka.
        title_norm = clean(title).lower().strip(' .:;–—-')
        for b in blocks:
            b_norm = clean(b).lower().strip(' .:;–—-')
            if b_norm == title_norm:
                continue
            desc = clip_sentence(b)
            if len(desc) >= 25:
                return desc
    return generic(title, doc_title, lang)


def main():
    with MAP.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    if len(rows) != 338:
        raise SystemExit(f'STOP: mapa ma {len(rows)} rekordów, oczekiwano 338')

    by_file = {}
    for r in rows:
        by_file.setdefault(r['dokument_plik'], []).append(r)

    parsed = {}
    for filename in by_file:
        path = Path('audhd') / filename
        if not path.is_file():
            raise SystemExit(f'STOP: brak pliku {path}')
        parser = SectionParser()
        parser.feed(path.read_text(encoding='utf-8'))
        parser.close()
        parsed[filename] = parser.sections

    out_rows = []
    missing = []
    for r in rows:
        sections = parsed[r['dokument_plik']]
        anchor = r['anchor']
        sec = sections.get(anchor)
        if sec is None:
            missing.append((r['dokument_plik'], anchor, r['sekcja_tytul']))
            continue
        desc = describe(sec, r['sekcja_tytul'], r['dokument_tytul'])
        desc = desc.replace('\t', ' ').replace('\n', ' ').strip()
        if not desc:
            raise SystemExit(f'STOP: pusty opis {r["dokument_plik"]}#{anchor}')
        out_rows.append({
            'dokument_kod': r['dokument_kod'],
            'dokument_plik': r['dokument_plik'],
            'poziom': r['poziom'],
            'kolejnosc': r['kolejnosc'],
            'sekcja_tytul': r['sekcja_tytul'],
            'anchor': anchor,
            'opis': desc,
        })

    if missing:
        preview = '; '.join(f'{f}#{a}' for f, a, _ in missing[:12])
        raise SystemExit(f'STOP: {len(missing)} anchorów z mapy nie znaleziono w HTML: {preview}')
    if len(out_rows) != 338:
        raise SystemExit(f'STOP: wynik ma {len(out_rows)} rekordów, oczekiwano 338')

    fields = ['dokument_kod', 'dokument_plik', 'poziom', 'kolejnosc', 'sekcja_tytul', 'anchor', 'opis']
    with OUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(out_rows)

    print(f'OK: opisy={len(out_rows)}; pliki={len(by_file)}; output={OUT}')


if __name__ == '__main__':
    main()
