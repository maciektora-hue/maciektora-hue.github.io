#!/usr/bin/env python3
import argparse
import csv
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_MIDDLE = ROOT / "sol-middleend-CSV-v08-11.csv"

NOISE = {
    "official", "video", "audio", "music", "lyric", "lyrics", "hd", "hq",
    "clip", "visualizer", "visualiser"
}


def tidy(s: str) -> str:
    s = (s or "").casefold()
    s = s.replace("|", " ").replace("&", " and ")
    s = re.sub(r"\b(feat|ft|featuring)\b\.?", " ", s)
    s = re.sub(r"[^a-z0-9ąćęłńóśźż]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def title_core(s: str) -> str:
    words = [w for w in tidy(s).split() if w not in NOISE]
    return " ".join(words)


def seq(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def token_score(a: str, b: str) -> float:
    aa, bb = set(a.split()), set(b.split())
    if not aa or not bb:
        return 0.0
    inter = len(aa & bb)
    return 2.0 * inter / (len(aa) + len(bb))


def similarity(a: str, b: str) -> float:
    return max(seq(a, b), token_score(a, b))


def artist_similarity(a: str, b: str) -> float:
    a, b = tidy(a), tidy(b)
    s = similarity(a, b)
    # Jeden artysta vs lista artystów z feat. nie powinien przegrywać z przypadkowym podobnym tekstem.
    if a and b and (a in b or b in a):
        s = max(s, min(len(a), len(b)) / max(len(a), len(b)), 0.75)
    return min(s, 1.0)


def title_similarity(a: str, b: str) -> float:
    raw = similarity(tidy(a), tidy(b))
    core = similarity(title_core(a), title_core(b))
    return max(raw, core)


def quality(score: float, gap: float, a_artist: str, a_title: str, c_artist: str, c_title: str) -> str:
    if tidy(a_artist) == tidy(c_artist) and title_core(a_title) == title_core(c_title):
        return "exact"
    if score >= 0.90 and gap >= 0.08:
        return "high"
    if score >= 0.80 and gap >= 0.04:
        return "medium"
    return "review"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", type=Path, required=True)
    ap.add_argument("--middle", type=Path, default=DEFAULT_MIDDLE)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    with args.audio.open("r", encoding="utf-8-sig", newline="") as f:
        audio_rows = list(csv.DictReader(f, delimiter="\t"))
    with args.middle.open("r", encoding="utf-8-sig", newline="") as f:
        middle_rows = list(csv.DictReader(f))

    out = []
    for a in audio_rows:
        scored = []
        for m in middle_rows:
            ars = artist_similarity(a["artist_parsed"], m.get("artist_parsed") or m.get("artist_normalized") or m.get("artist_original", ""))
            tis = title_similarity(a["title_parsed"], m.get("title_parsed") or m.get("title_normalized") or m.get("title_original", ""))
            total = 0.45 * ars + 0.55 * tis
            scored.append((total, ars, tis, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        best = scored[0]
        second = scored[1]
        gap = best[0] - second[0]
        m = best[3]
        sm = second[3]
        q = quality(best[0], gap, a["artist_parsed"], a["title_parsed"],
                    m.get("artist_parsed") or m.get("artist_original", ""),
                    m.get("title_parsed") or m.get("title_original", ""))
        n = int(a["number"])
        out.append({
            "audio_number": n,
            "audio_id": f"audio-{n:04d}",
            "youtube_video_id": a["youtube_video_id"],
            "audio_artist": a["artist_original"],
            "audio_title": a["title_original"],
            "audio_artist_parsed": a["artist_parsed"],
            "audio_title_parsed": a["title_parsed"],
            "candidate_utwu_id": m.get("utwu_id", ""),
            "candidate_spotify_order": m.get("spotify_order", ""),
            "candidate_artist": m.get("artist_original", ""),
            "candidate_title": m.get("title_original", ""),
            "candidate_artist_parsed": m.get("artist_parsed", ""),
            "candidate_title_parsed": m.get("title_parsed", ""),
            "score": f"{best[0]:.4f}",
            "artist_score": f"{best[1]:.4f}",
            "title_score": f"{best[2]:.4f}",
            "gap_to_second": f"{gap:.4f}",
            "quality": q,
            "second_utwu_id": sm.get("utwu_id", ""),
            "second_artist": sm.get("artist_original", ""),
            "second_title": sm.get("title_original", ""),
            "second_score": f"{second[0]:.4f}",
        })

    fields = list(out[0].keys()) if out else []
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    counts = {}
    for r in out:
        counts[r["quality"]] = counts.get(r["quality"], 0) + 1
    print(f"ROWS={len(out)}")
    print("QUALITY=" + ",".join(f"{k}:{counts[k]}" for k in sorted(counts)))
    for r in out[:8]:
        print(f"CHECK {r['audio_number']}: {r['audio_artist']} | {r['audio_title']} -> {r['candidate_artist']} | {r['candidate_title']} | {r['quality']} {r['score']}")


if __name__ == "__main__":
    main()
