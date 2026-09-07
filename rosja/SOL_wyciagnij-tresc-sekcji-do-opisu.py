from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import csv
import re

ROOT = Path(__file__).resolve().parent
MAPA = ROOT / 'SOL_mapa-sekcji-i-anchorow-rosja.tsv'
OUT = ROOT / 'SOL_tresc-sekcji-do-opisu.tsv'

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.events = []
        self.stack = []
        self.cur_heading = None
        self.cur_heading_text = []
        self.cur_heading_level = None
        self.cur_heading_id = ''
        self.text_buf = []
        self.in_script = 0
        self.in_style = 0

    def flush_text(self):
        if self.cur_heading is not None and self.text_buf:
            txt = ' '.join(self.text_buf)
            self.events.append(('text', txt))
        self.text_buf = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script':
            self.in_script += 1
            return
        if tag == 'style':
            self.in_style += 1
            return
        m = re.fullmatch(r'h([1-6])', tag)
        if m:
            self.flush_text()
            self.cur_heading = tag
            self.cur_heading_level = int(m.group(1))
            self.cur_heading_id = attrs.get('id', '')
            self.cur_heading_text = []

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = max(0, self.in_script - 1)
            return
        if tag == 'style':
            self.in_style = max(0, self.in_style - 1)
            return
        if self.cur_heading == tag:
            title = clean(' '.join(self.cur_heading_text))
            self.events.append(('heading', self.cur_heading_level, self.cur_heading_id, title))
            self.cur_heading = None
            self.cur_heading_text = []
            self.text_buf = []

    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
        if self.cur_heading is not None:
            self.cur_heading_text.append(data)
        else:
            self.text_buf.append(data)


def clean(s):
    s = unescape(s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def section_local_text(events):
    rows = []
    current = None
    buf = []
    for ev in events:
        if ev[0] == 'heading':
            if current is not None:
                rows.append((*current, clean(' '.join(buf))))
            current = ev[1:]
            buf = []
        elif ev[0] == 'text' and current is not None:
            buf.append(ev[1])
    if current is not None:
        rows.append((*current, clean(' '.join(buf))))
    return rows

with MAPA.open(encoding='utf-8', newline='') as f:
    mapa = list(csv.DictReader(f, delimiter='\t'))

by_file = {}
for r in mapa:
    by_file.setdefault(r['dokument_plik'], []).append(r)

out = []
for filename, mrows in by_file.items():
    p = ROOT / filename
    html = p.read_text(encoding='utf-8')
    parser = Parser()
    parser.feed(html)
    extracted = section_local_text(parser.events)
    by_anchor = {anchor: (level, title, text) for level, anchor, title, text in extracted if anchor}

    for r in mrows:
        anchor = r['anchor']
        if anchor not in by_anchor:
            raise SystemExit(f'STOP: brak anchoru w ekstrakcie: {filename} #{anchor}')
        level, title, text = by_anchor[anchor]
        if f'H{level}' != r['poziom']:
            raise SystemExit(f'STOP: poziom nie zgadza sie: {filename} #{anchor}')
        if clean(title) != clean(r['sekcja_tytul']):
            raise SystemExit(f'STOP: tytul nie zgadza sie: {filename} #{anchor}')
        out.append({
            'dokument_kod': r['dokument_kod'],
            'dokument_plik': filename,
            'poziom': r['poziom'],
            'glebokosc': r['glebokosc'],
            'kolejnosc': r['kolejnosc'],
            'sekcja_tytul': r['sekcja_tytul'],
            'anchor': anchor,
            'tekst_lokalny': text,
        })

if len(out) != len(mapa):
    raise SystemExit(f'STOP: liczba rekordow {len(out)} != mapa {len(mapa)}')

fields = ['dokument_kod','dokument_plik','poziom','glebokosc','kolejnosc','sekcja_tytul','anchor','tekst_lokalny']
with OUT.open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    w.writeheader()
    w.writerows(out)

print(f'OK: {len(out)} sekcji wyekstrahowanych do {OUT.name}')
