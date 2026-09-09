#!/usr/bin/env python3
import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INOUT = ROOT / "audio_filename_parsed_0151_0200.tsv"

FILE_RE = re.compile(
    r"^(?P<number>\d{4})\s+-\s+(?P<uploader>.*?)\s+-\s+(?P<video_title>.*?)\s+\[(?P<yt>[A-Za-z0-9_-]{11})\]\.webm$"
)

POLISH = str.maketrans({"ł":"l","Ł":"L"})


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

    # Normal YouTube title conventions: ARTIST - TITLE, ARTIST — TITLE, ARTIST ⧸ TITLE.
    for pattern in (r"\s+-\s+", r"\s*[—–]\s*", r"\s*⧸\s*"):
        parts = re.split(pattern, v, maxsplit=1)
        if len(parts) == 2 and parts[0].strip() and parts[1].strip():
            return parts[0].strip(), parts[1].strip()

    # Fullwidth colon is sometimes used as artist/title separator, but also occurs inside titles.
    # Accept it only when the left side is the uploader itself.
    if "：" in video_title:
        left, right = video_title.split("：", 1)
        if parsed(left) == parsed(u) and right.strip():
            return clean_space(left), clean_space(right)

    # NFKC converts fullwidth colon to ':', so cover that spelling too, under the same safeguard.
    if ":" in v:
        left, right = v.split(":", 1)
        if parsed(left) == parsed(u) and right.strip():
            return left.strip(), right.strip()

    # If video title does not contain an artist prefix, uploader is the best available artist.
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
    with INOUT.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    out = []
    for row in rows:
        number, artist, title, yt = parse_filename(row["source_filename"])
        out.append({
            "number": number,
            "source_filename": row["source_filename"],
            "artist_original": artist,
            "artist_normalized": normalized(artist),
            "artist_parsed": parsed(artist),
            "title_original": title,
            "title_normalized": normalized(title),
            "title_parsed": parsed(title),
            "youtube_video_id": yt,
        })

    fields = [
        "number", "source_filename",
        "artist_original", "artist_normalized", "artist_parsed",
        "title_original", "title_normalized", "title_parsed",
        "youtube_video_id",
    ]
    with INOUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    nums = [r["number"] for r in out]
    missing = [n for n in range(151, 201) if n not in nums]
    print(f"ROWS={len(out)}")
    print(f"MISSING={missing}")
    for n in (151,153,156,163,165,170,189,196,199,200):
        r = next((x for x in out if x["number"] == n), None)
        if r:
            print(f"CHECK {n}: {r['artist_original']} | {r['title_original']} | {r['youtube_video_id']}")


if __name__ == "__main__":
    main()
