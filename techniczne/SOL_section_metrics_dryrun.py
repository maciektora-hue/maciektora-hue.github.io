from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import csv
import os
import re
import subprocess
import libsql

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {
    'rosja': ROOT / 'rosja' / 'SOL_mapa-sekcji-i-anchorow-rosja.tsv',
    'audhd': ROOT / 'audhd' / 'SOL_mapa-sekcji-i-anchorow-audhd.tsv',
}
WORD_RE = re.compile(r"[^\W_]+(?:[-’'][^\W_]+)*", re.UNICODE)
SKIP_TAGS = {'script', 'style', 'template'}


def clean(text):
    return re.sub(r'\s+', ' ', unescape(text or '')).strip()


def count_metrics(text):
    text = clean(text)
    return {
        'char_count': len(text),
        'letter_count': sum(ch.isalpha() for ch in text),
        'word_count': sum(1 for token in WORD_RE.findall(text) if any(ch.isalpha() for ch in token)),
    }


class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.events = []
        self.current_heading = None
        self.heading_text = []
        self.text_buf = []
        self.skip_depth = 0

    def flush_text(self):
        if self.text_buf:
            txt = clean(' '.join(self.text_buf))
            if txt:
                self.events.append(('text', txt))
        self.text_buf = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        m = re.fullmatch(r'h([1-6])', tag)
        if m:
            self.flush_text()
            attrs = dict(attrs)
            self.current_heading = {
                'level': int(m.group(1)),
                'anchor': attrs.get('id', ''),
            }
            self.heading_text = []

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if self.current_heading and tag == f"h{self.current_heading['level']}":
            self.current_heading['title'] = clean(' '.join(self.heading_text))
            self.events.append(('heading', self.current_heading))
            self.current_heading = None
            self.heading_text = []
            self.text_buf = []

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.current_heading is not None:
            self.heading_text.append(data)
        else:
            self.text_buf.append(data)

    def close(self):
        super().close()
        self.flush_text()


def parse_nodes(path):
    parser = HeadingParser()
    parser.feed(path.read_text(encoding='utf-8'))
    parser.close()

    nodes = []
    current = None
    for ev in parser.events:
        if ev[0] == 'heading':
            current = {
                **ev[1],
                'local_parts': [],
                'children': [],
                'parent': None,
            }
            nodes.append(current)
        elif ev[0] == 'text' and current is not None:
            current['local_parts'].append(ev[1])

    stack = []
    for node in nodes:
        while stack and stack[-1]['level'] >= node['level']:
            stack.pop()
        if stack:
            node['parent'] = stack[-1]
            stack[-1]['children'].append(node)
        stack.append(node)

    def aggregate(node):
        parts = []
        local = clean(' '.join(node['local_parts']))
        if local:
            parts.append(local)
        for child in node['children']:
            child_text = aggregate(child)
            if child_text:
                parts.append(child_text)
        node['aggregate_text'] = clean(' '.join(parts))
        node['metrics'] = count_metrics(node['aggregate_text'])
        return node['aggregate_text']

    for node in nodes:
        if node['parent'] is None:
            aggregate(node)

    return nodes


def git_blob_sha(path):
    return subprocess.check_output(['git', 'hash-object', str(path)], cwd=ROOT, text=True).strip()


def load_sql_sections():
    token = os.environ.get('TURSO_AUTH_TOKEN')
    if not token:
        raise RuntimeError('BRAK SECRETU TURSO_ADMIN_TOKEN')
    conn = libsql.connect(database=os.environ['TURSO_DATABASE_URL'], auth_token=token)
    rows = conn.execute('''
        SELECT d.collection_id, d.document_code, s.section_id, s.anchor, s.heading_level
        FROM content_sections s
        JOIN content_documents d ON d.document_id = s.document_id
        WHERE s.section_kind = 'heading'
        ORDER BY d.collection_id, d.document_sort_order, s.structure_order
    ''').fetchall()
    conn.close()
    out = {}
    for collection_id, document_code, section_id, anchor, heading_level in rows:
        key = (collection_id, document_code, anchor)
        if key in out:
            raise RuntimeError(f'DUPLICATE_SQL_KEY {key!r}')
        out[key] = {
            'section_id': section_id,
            'heading_level': heading_level,
        }
    return out


def main():
    sql_sections = load_sql_sections()
    results = []

    for collection_id, map_path in COLLECTIONS.items():
        base = map_path.parent
        with map_path.open(encoding='utf-8', newline='') as f:
            map_rows = list(csv.DictReader(f, delimiter='\t'))

        by_file = {}
        for row in map_rows:
            by_file.setdefault(row['dokument_plik'], []).append(row)

        collection_results = []
        for filename, mapped in by_file.items():
            path = base / filename
            if not path.is_file():
                raise RuntimeError(f'MISSING_FILE {collection_id}/{filename}')

            nodes = parse_nodes(path)
            by_anchor = {}
            for node in nodes:
                anchor = node['anchor']
                if anchor:
                    if anchor in by_anchor:
                        raise RuntimeError(f'DUPLICATE_HTML_ANCHOR {filename} #{anchor}')
                    by_anchor[anchor] = node

            source_sha = git_blob_sha(path)
            for row in mapped:
                anchor = row['anchor']
                node = by_anchor.get(anchor)
                if node is None:
                    raise RuntimeError(f'MISSING_HTML_ANCHOR {filename} #{anchor}')
                expected_level = int(row['poziom'][1:])
                if node['level'] != expected_level:
                    raise RuntimeError(f'LEVEL_MISMATCH {filename} #{anchor}: html=H{node["level"]} map=H{expected_level}')
                if clean(node['title']) != clean(row['sekcja_tytul']):
                    raise RuntimeError(f'TITLE_MISMATCH {filename} #{anchor}')

                sql_key = (collection_id, row['dokument_kod'], anchor)
                sql = sql_sections.get(sql_key)
                if sql is None:
                    raise RuntimeError(f'MISSING_SQL_SECTION {sql_key!r}')
                if sql['heading_level'] != expected_level:
                    raise RuntimeError(f'SQL_LEVEL_MISMATCH {sql_key!r}')

                result = {
                    'collection_id': collection_id,
                    'document_code': row['dokument_kod'],
                    'section_id': sql['section_id'],
                    'anchor': anchor,
                    'heading_level': expected_level,
                    'source_sha': source_sha,
                    **node['metrics'],
                }
                results.append(result)
                collection_results.append(result)

        if len(collection_results) != len(map_rows):
            raise RuntimeError(f'COUNT_MISMATCH {collection_id}: results={len(collection_results)} map={len(map_rows)}')

        levels = {}
        for r in collection_results:
            levels[r['heading_level']] = levels.get(r['heading_level'], 0) + 1
        print(f"DRYRUN_OK collection={collection_id} files={len(by_file)} sections={len(collection_results)} levels={dict(sorted(levels.items()))}")

    if len(results) != len(sql_sections):
        missing = sorted(set(sql_sections) - {(r['collection_id'], r['document_code'], r['anchor']) for r in results})
        raise RuntimeError(f'SQL_COUNT_MISMATCH results={len(results)} sql_heading_sections={len(sql_sections)} missing={missing[:10]!r}')

    for r in results:
        if not (0 <= r['word_count'] <= r['letter_count'] <= r['char_count']):
            raise RuntimeError(f'BAD_METRICS {r!r}')

    samples = sorted(results, key=lambda r: (-r['heading_level'], r['collection_id'], r['document_code'], r['section_id']))[:8]
    for r in samples:
        print(
            'SAMPLE '
            f"{r['collection_id']} {r['document_code']} H{r['heading_level']} {r['section_id']} "
            f"chars={r['char_count']} letters={r['letter_count']} words={r['word_count']}"
        )

    print(f'DRYRUN_ALL_OK sections={len(results)}')


if __name__ == '__main__':
    main()
