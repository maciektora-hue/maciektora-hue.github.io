#!/usr/bin/env python3
import argparse
import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT / "audio_features_v08.csv"

FILE_RE = re.compile(
    r"^(?P<number>\d{4})\s+-\s+(?P<uploader>.*?)\s+-\s+(?P<video_title>.*?)\s+\[(?P<yt>[A-Za-z0-9_-]{11})\]\.webm$"
)
POLISH = str.maketrans({"ł": "l", "Ł": "L"})


def clean_space(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip()


def normalized(s: str) -> str:
    return clean_space(s).casefold()


def parsed(s: str) -> str:
    s = clean_space(s).translate(POLISH).casefold()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def split_artist_title(uploader: str, video_title: str):
    u = clean_space(uploader)
    v = clean_space(video_title)

    if ":" in v:
        left, right = v.split(":", 1)
        if parsed(left) == parsed(u) and right.strip():
            return left.strip(), right.strip()

    for pattern in (r"\s+-\s+", r"\s*[—–]\s*", r"\s*⧸\s*"):
        parts = re.split(pattern, v, maxsplit=1)
        if len(parts) == 2 and parts[0].strip() and parts[1].strip():
            return parts[0].strip(), parts[1].strip()

    return u, v


def parse_filename(filename: str):
    m = FILE_RE.match(clean_space(filename))
    if not m:
        raise ValueError(f"Nie rozpoznaję nazwy pliku: {filename}")
    number = int(m.group("number"))
    uploader = m.group("uploader")
    video_title = m.group("video_title")
    yt = m.group("yt")
    artist, title = split_artist_title(uploader, video_title)
    return number, artist, title, yt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if args.start > args.end:
        raise SystemExit("start > end")

    out = []
    with args.source.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if "plik" not in (reader.fieldnames or []):
            raise SystemExit("Brak kolumny 'plik' w źródłowym CSV")
        for row in reader:
            filename = (row.get("plik") or "").strip()
            if not filename:
                continue
            m = re.match(r"^(\d{4})\s+-\s+", filename)
            if not m:
                continue
            number = int(m.group(1))
            if not (args.start <= number <= args.end):
                continue
            number, artist, title, yt = parse_filename(filename)
            out.append({
                "number": number,
                "source_filename": filename,
                "artist_original": artist,
                "artist_normalized": normalized(artist),
                "artist_parsed": parsed(artist),
                "title_original": title,
                "title_normalized": normalized(title),
                "title_parsed": parsed(title),
                "youtube_video_id": yt,
            })

    out.sort(key=lambda r: r["number"])
    nums = [r["number"] for r in out]
    if len(nums) != len(set(nums)):
        raise SystemExit("Duplikat numeru audio w batchu")

    fields = [
        "number", "source_filename",
        "artist_original", "artist_normalized", "artist_parsed",
        "title_original", "title_normalized", "title_parsed",
        "youtube_video_id",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    missing = [n for n in range(args.start, args.end + 1) if n not in set(nums)]
    print(f"RANGE={args.start}-{args.end}")
    print(f"ROWS={len(out)}")
    print(f"MISSING={missing}")
    for r in out[:5]:
        print(f"CHECK {r['number']}: {r['artist_original']} | {r['title_original']} | {r['youtube_video_id']}")


if __name__ == "__main__":
    main()
