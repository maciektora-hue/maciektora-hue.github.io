#!/usr/bin/env python3
import os, re, unicodedata
import libsql
from rapidfuzz import fuzz

BATCH = 50

def clean(s):
    s = '' if s is None else str(s)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    s = s.casefold()
    return ' '.join(''.join(ch if ch.isalnum() else ' ' for ch in s).split())

def parse_audio(filename):
    m = re.match(r'^(\d+)\s*-\s*(.*?)\s*-\s*(.*?)\s*\[([A-Za-z0-9_-]{11})\]\.[^.]+$', filename)
    if not m:
        return None
    return int(m.group(1)), m.group(2), m.group(3), m.group(4)

def best_score(value, variants, artist=False):
    value = clean(value)
    scores = []
    for v in variants:
        v = clean(v)
        if not value or not v:
            continue
        scores.append(fuzz.token_set_ratio(value, v) if artist else max(fuzz.WRatio(value, v), fuzz.partial_ratio(value, v)))
    return max(scores) if scores else 0.0

def main():
    token = os.environ['TURSO_AUTH_TOKEN']
    conn = libsql.connect(database=os.environ['TURSO_DATABASE_URL'], auth_token=token)
    conn.execute('PRAGMA foreign_keys = ON')

    cols = {r[1] for r in conn.execute('PRAGMA table_info(middle_end)').fetchall()}
    additions = [
        ('audio_id', 'ALTER TABLE middle_end ADD COLUMN audio_id TEXT REFERENCES audio(audio_id)'),
        ('youtube_video_id', 'ALTER TABLE middle_end ADD COLUMN youtube_video_id TEXT'),
        ('audio_match_quality', 'ALTER TABLE middle_end ADD COLUMN audio_match_quality TEXT'),
    ]
    for name, sql in additions:
        if name not in cols:
            conn.execute(sql)
            conn.commit()
            print(f'COLUMN_ADDED={name}', flush=True)

    middle_rows = conn.execute('''
        SELECT utwu_id, spotify_order,
               title_original, title_normalized, title_parsed,
               artist_original, artist_normalized, artist_parsed,
               audio_id
        FROM middle_end
    ''').fetchall()
    by_order = {r[1]: r for r in middle_rows if r[1] is not None}

    audio_rows = []
    for aid, filename, ytid in conn.execute('SELECT audio_id, source_filename, youtube_video_id FROM audio').fetchall():
        p = parse_audio(filename)
        if p:
            idx, artist, title, file_ytid = p
            audio_rows.append((aid, ytid or file_ytid, idx, artist, title))

    def pair_scores(arow, mrow):
        _, _, _, a_artist, a_title = arow
        _, _, t0, tn, tp, a0, an, ap, _ = mrow
        return (
            best_score(a_artist, (a0, an, ap), artist=True),
            best_score(a_title, (t0, tn, tp), artist=False),
        )

    stats = []
    for offset in range(-100, 101):
        strong = 0
        checked = 0
        total = 0.0
        for arow in audio_rows:
            mrow = by_order.get(arow[2] + offset)
            if not mrow:
                continue
            a_score, t_score = pair_scores(arow, mrow)
            checked += 1
            total += a_score + t_score
            if a_score >= 80 and t_score >= 75:
                strong += 1
        stats.append((strong, total, checked, offset))

    stats.sort(reverse=True)
    best_strong, _, best_checked, offset = stats[0]
    print('BEST_OFFSETS=' + repr([(x[3], x[0]) for x in stats[:5]]), flush=True)
    print(f'CHOSEN_OFFSET={offset}', flush=True)
    print(f'OFFSET_STRONG_MATCHES={best_strong}/{best_checked}', flush=True)
    if best_strong < 100:
        raise RuntimeError('Za malo zgodnych rekordow; nic nie zapisuje')

    matches = []
    for arow in sorted(audio_rows, key=lambda x: x[2]):
        aid, ytid, idx, _, _ = arow
        mrow = by_order.get(idx + offset)
        if not mrow or mrow[8]:
            continue
        a_score, t_score = pair_scores(arow, mrow)
        quality = None
        if a_score >= 95 and t_score >= 92:
            quality = 'exact'
        elif a_score >= 85 and t_score >= 80:
            quality = 'high'
        if quality:
            matches.append((aid, ytid, quality, mrow[0]))

    print(f'AUTO_MATCHES_TO_WRITE={len(matches)}', flush=True)
    print('QUALITY_COUNTS=' + repr({q: sum(1 for x in matches if x[2] == q) for q in ('exact','high')}), flush=True)

    done = 0
    for start in range(0, len(matches), BATCH):
        batch = matches[start:start+BATCH]
        for aid, ytid, quality, utwu_id in batch:
            conn.execute('''
                UPDATE middle_end
                SET audio_id=?, youtube_video_id=?, audio_match_quality=?
                WHERE utwu_id=? AND audio_id IS NULL
            ''', (aid, ytid, quality, utwu_id))
        conn.commit()
        done += len(batch)
        print(f'{done}/{len(matches)} zapisane', flush=True)

    print('MIDDLE_END_AUDIO_MATCHED=' + str(conn.execute('SELECT COUNT(*) FROM middle_end WHERE audio_id IS NOT NULL').fetchone()[0]), flush=True)
    print('MIDDLE_END_YOUTUBE_FILLED=' + str(conn.execute('SELECT COUNT(*) FROM middle_end WHERE youtube_video_id IS NOT NULL').fetchone()[0]), flush=True)
    print('UNMATCHED_AUDIO=' + str(conn.execute('SELECT COUNT(*) FROM audio a LEFT JOIN middle_end m ON m.audio_id=a.audio_id WHERE m.audio_id IS NULL').fetchone()[0]), flush=True)
    print('AUDIO_MIDDLE_MATCH_OK', flush=True)
    conn.close()

if __name__ == '__main__':
    main()
