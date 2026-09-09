#!/usr/bin/env python3
import csv
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "audio_filename_parsed_0151_0200.tsv"
MIDDLE = ROOT / "sol-middleend-CSV-v08-11.csv"
OUT = ROOT / "audio_middleend_candidates_0151_0200.tsv"

NOISE = {
    "official", "video", "audio", "music", "lyric", "lyrics", "single",
    "hd", "hq", "clip", "visualizer"
}


def tokens(s: str):
    return [x for x in re.split(r"\s+", (s or "").strip()) if x]


def core_title(s: str):
    toks = tokens(s)
    # remove only generic presentation words; keep live/remastered/version because they can matter
    return " ".join(t for t in toks if t not in NOISE)


def seq(a: str, b: str):
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def jaccard(a: str, b: str):
    aa, bb = set(tokens(a)), set(tokens(b))
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def score(audio, me):
    aa = audio["artist_parsed"]
    at = core_title(audio["title_parsed"])
    ma = me["artist_parsed"]
    mt = core_title(me["title_parsed"])

    artist_seq = seq(aa, ma)
    title_seq = seq(at, mt)
    artist_j = jaccard(aa, ma)
    title_j = jaccard(at, mt)

    artist = max(artist_seq, artist_j)
    title = max(title_seq, title_j)
    total = 0.45 * artist + 0.55 * title

    exact_artist = aa == ma and aa != ""
    exact_title = at == mt and at != ""
    return total, artist, title, exact_artist, exact_title


def main():
    with AUDIO.open("r", encoding="utf-8", newline="") as f:
        audios = list(csv.DictReader(f, delimiter="\t"))
    with MIDDLE.open("r", encoding="utf-8", newline="") as f:
        middle = list(csv.DictReader(f))

    out = []
    for a in audios:
        ranked = []
        for m in middle:
            total, artist_s, title_s, exact_artist, exact_title = score(a, m)
            ranked.append((total, artist_s, title_s, exact_artist, exact_title, m))
        ranked.sort(key=lambda x: x[0], reverse=True)
        best = ranked[0]
        second = ranked[1]
        total, artist_s, title_s, exact_artist, exact_title, m = best
        gap = total - second[0]

        if exact_artist and exact_title:
            quality = "exact"
        elif total >= 0.92 and gap >= 0.05:
            quality = "high"
        elif total >= 0.82 and gap >= 0.03:
            quality = "medium"
        else:
            quality = "review"

        n = int(a["number"])
        out.append({
            "audio_number": n,
            "audio_id": f"audio-{n:04d}",
            "youtube_video_id": a["youtube_video_id"],
            "audio_artist": a["artist_original"],
            "audio_title": a["title_original"],
            "audio_artist_parsed": a["artist_parsed"],
            "audio_title_parsed": a["title_parsed"],
            "candidate_utwu_id": m["utwu_id"],
            "candidate_spotify_order": m["spotify_order"],
            "candidate_artist": m["artist_original"],
            "candidate_title": m["title_original"],
            "candidate_artist_parsed": m["artist_parsed"],
            "candidate_title_parsed": m["title_parsed"],
            "score": f"{total:.4f}",
            "artist_score": f"{artist_s:.4f}",
            "title_score": f"{title_s:.4f}",
            "gap_to_second": f"{gap:.4f}",
            "quality": quality,
            "second_utwu_id": second[5]["utwu_id"],
            "second_artist": second[5]["artist_original"],
            "second_title": second[5]["title_original"],
            "second_score": f"{second[0]:.4f}",
        })

    fields = list(out[0].keys()) if out else []
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    counts = {}
    for r in out:
        counts[r["quality"]] = counts.get(r["quality"], 0) + 1
    print(f"ROWS={len(out)}")
    print("QUALITY=" + ", ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
    for r in out:
        print(f"{r['audio_number']}: {r['audio_artist']} | {r['audio_title']} -> {r['candidate_artist']} | {r['candidate_title']} [{r['quality']} {r['score']}]")


if __name__ == "__main__":
    main()
