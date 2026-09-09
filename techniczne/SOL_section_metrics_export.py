from datetime import datetime, timezone
import csv
import os
import libsql

from SOL_section_metrics_dryrun import (
    COLLECTIONS,
    clean,
    git_blob_sha,
    load_sql_sections,
    parse_nodes,
)

METRIC_VERSION = 1


def collect_results():
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
                    raise RuntimeError(
                        f'LEVEL_MISMATCH {filename} #{anchor}: '
                        f'html=H{node["level"]} map=H{expected_level}'
                    )
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
                    'section_id': sql['section_id'],
                    'source_sha': source_sha,
                    **node['metrics'],
                }
                results.append(result)
                collection_results.append(result)

        if len(collection_results) != len(map_rows):
            raise RuntimeError(
                f'COUNT_MISMATCH {collection_id}: '
                f'results={len(collection_results)} map={len(map_rows)}'
            )

    if len(results) != len(sql_sections):
        raise RuntimeError(
            f'SQL_COUNT_MISMATCH results={len(results)} '
            f'sql_heading_sections={len(sql_sections)}'
        )

    for r in results:
        if not (0 <= r['word_count'] <= r['letter_count'] <= r['char_count']):
            raise RuntimeError(f'BAD_METRICS {r!r}')

    return results


def main():
    results = collect_results()
    token = os.environ.get('TURSO_AUTH_TOKEN')
    if not token:
        raise RuntimeError('BRAK SECRETU TURSO_ADMIN_TOKEN')

    calculated_at = datetime.now(timezone.utc).isoformat()
    conn = libsql.connect(
        database=os.environ['TURSO_DATABASE_URL'],
        auth_token=token,
    )

    conn.executemany(
        '''
        INSERT INTO content_section_metrics (
            section_id,
            char_count,
            letter_count,
            word_count,
            source_sha,
            metric_version,
            calculated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(section_id) DO UPDATE SET
            char_count = excluded.char_count,
            letter_count = excluded.letter_count,
            word_count = excluded.word_count,
            source_sha = excluded.source_sha,
            metric_version = excluded.metric_version,
            calculated_at = excluded.calculated_at
        ''',
        [
            (
                r['section_id'],
                r['char_count'],
                r['letter_count'],
                r['word_count'],
                r['source_sha'],
                METRIC_VERSION,
                calculated_at,
            )
            for r in results
        ],
    )
    conn.commit()

    total = conn.execute(
        'SELECT COUNT(*) FROM content_section_metrics'
    ).fetchone()[0]
    complete = conn.execute(
        '''
        SELECT COUNT(*)
        FROM content_section_metrics
        WHERE char_count IS NOT NULL
          AND letter_count IS NOT NULL
          AND word_count IS NOT NULL
          AND source_sha IS NOT NULL
        '''
    ).fetchone()[0]
    by_collection = conn.execute(
        '''
        SELECT d.collection_id, COUNT(*)
        FROM content_section_metrics m
        JOIN content_sections s ON s.section_id = m.section_id
        JOIN content_documents d ON d.document_id = s.document_id
        GROUP BY d.collection_id
        ORDER BY d.collection_id
        '''
    ).fetchall()

    if total != 958 or complete != 958:
        raise RuntimeError(f'EXPORT_COUNT_BAD total={total} complete={complete}')

    expected = {'audhd': 338, 'rosja': 620}
    actual = {collection_id: count for collection_id, count in by_collection}
    if actual != expected:
        raise RuntimeError(f'EXPORT_COLLECTION_COUNTS_BAD {actual!r}')

    print(
        f'SECTION_METRICS_EXPORT_OK total={total} complete={complete} '
        f'audhd={actual["audhd"]} rosja={actual["rosja"]} '
        f'metric_version={METRIC_VERSION}'
    )

    samples = conn.execute(
        '''
        SELECT m.section_id, d.collection_id, s.heading_level,
               m.char_count, m.letter_count, m.word_count
        FROM content_section_metrics m
        JOIN content_sections s ON s.section_id = m.section_id
        JOIN content_documents d ON d.document_id = s.document_id
        ORDER BY s.heading_level DESC, m.section_id
        LIMIT 5
        '''
    ).fetchall()
    for row in samples:
        print('DB_SAMPLE', row)

    conn.close()


if __name__ == '__main__':
    main()
