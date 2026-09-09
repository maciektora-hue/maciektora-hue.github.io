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
        if artist:
            scores.append(fuzz.token_set_ratio(value, v))
        else:
            scores.append(max(fuzz.WRatio(value, v), fuzz.partial_ratio(value, v)))
    return max(scores) if scores else 0.0


def pair_scores(arow, mrow):
    _, _, _, a_artist, a_title = arow
    _, _, t0, tn, tp, ar0, arn, arp, _ = mrow
    artist_score = best_score(a_artist, (ar0, arn, arp), artist=True)
    title_score = best_score(a_title, (t0, tn, tp), artist=False)
    overall = 0.45 * artist_score + 0.55 * title_score
    return artist_score, title_score, overall


def main():
    conn = libsql.connect(
        database=os.environ['TURSO_DATABASE_URL'],
        auth_token=os.environ['TURSO_AUTH_TOKEN'],
    )
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
    middle_rows = [r for r in middle_rows if not r[8]]

    audio_rows = []
    for aid, filename, ytid in conn.execute('SELECT audio_id, source_filename, youtube_video_id FROM audio').fetchall():
        p = parse_audio(filename)
        if p:
            idx, artist, title, file_ytid = p
            audio_rows.append((aid, ytid or file_ytid, idx, artist, title))

    print(f'AUDIO_TO_COMPARE={len(audio_rows)}', flush=True)
    print(f'MIDDLE_END_TO_COMPARE={len(middle_rows)}', flush=True)

    best_for_audio = {}
    second_for_audio = {}
    best_for_middle = {}

    for ai, arow in enumerate(audio_rows):
        aid = arow[0]
        best = None
        second = None
        for mrow in middle_rows:
            utwu_id = mrow[0]
            artist_score, title_score, overall = pair_scores(arow, mrow)
            candidate = (overall, artist_score, title_score, utwu_id)
            if best is None or candidate > best:
                second = best
                best = candidate
            elif second is None or candidate > second:
                second = candidate

            mb = best_for_middle.get(utwu_id)
            reverse_candidate = (overall, artist_score, title_score, aid)
            if mb is None or reverse_candidate > mb:
                best_for_middle[utwu_id] = reverse_candidate

        if best:
            best_for_audio[aid] = best
        if second:
            second_for_audio[aid] = second
        if (ai + 1) % 100 == 0:
            print(f'POROWNANO={ai + 1}/{len(audio_rows)}', flush=True)

    matches = []
    for arow in audio_rows:
        aid, ytid, idx, a_artist, a_title = arow
        best = best_for_audio.get(aid)
        if not best:
            continue
        overall, artist_score, title_score, utwu_id = best
        second = second_for_audio.get(aid)
        margin = overall - second[0] if second else 100.0

        reverse = best_for_middle.get(utwu_id)
        if not reverse or reverse[3] != aid:
            continue

        quality = None
        if artist_score >= 95 and title_score >= 95 and overall >= 95 and margin >= 2:
            quality = 'exact'
        elif artist_score >= 85 and title_score >= 88 and overall >= 90 and margin >= 4:
            quality = 'high'

        if quality:
            matches.append((aid, ytid, quality, utwu_id, overall, margin))

    matches.sort(key=lambda x: x[3])
    print(f'AUTO_MATCHES_TO_WRITE={len(matches)}', flush=True)
    print('QUALITY_COUNTS=' + repr({q: sum(1 for x in matches if x[2] == q) for q in ('exact', 'high')}), flush=True)

    done = 0
    for start in range(0, len(matches), BATCH):
        batch = matches[start:start + BATCH]
        for aid, ytid, quality, utwu_id, overall, margin in batch:
            conn.execute('''
                UPDATE middle_end
                SET audio_id = ?, youtube_video_id = ?, audio_match_quality = ?
                WHERE utwu_id = ? AND audio_id IS NULL
            ''', (aid, ytid, quality, utwu_id))
        conn.commit()
        done += len(batch)
        print(f'{done}/{len(matches)} zapisane', flush=True)

    matched = conn.execute('SELECT COUNT(*) FROM middle_end WHERE audio_id IS NOT NULL').fetchone()[0]
    youtube = conn.execute('SELECT COUNT(*) FROM middle_end WHERE youtube_video_id IS NOT NULL').fetchone()[0]
    unmatched_audio = conn.execute('''
        SELECT COUNT(*) FROM audio a
        LEFT JOIN middle_end m ON m.audio_id = a.audio_id
        WHERE m.audio_id IS NULL
    ''').fetchone()[0]
    dangling = conn.execute('''
        SELECT COUNT(*) FROM middle_end m
        LEFT JOIN audio a ON a.audio_id = m.audio_id
        WHERE m.audio_id IS NOT NULL AND a.audio_id IS NULL
    ''').fetchone()[0]

    print(f'MIDDLE_END_AUDIO_MATCHED={matched}', flush=True)
    print(f'MIDDLE_END_YOUTUBE_FILLED={youtube}', flush=True)
    print(f'UNMATCHED_AUDIO={unmatched_audio}', flush=True)
    print(f'DANGLING_AUDIO_FK={dangling}', flush=True)
    print('AUDIO_MIDDLE_MATCH_OK', flush=True)
    conn.close()


if __name__ == '__main__':
    main()
