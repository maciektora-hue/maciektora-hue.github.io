#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

READY_QUALITIES = {"exact", "high"}
REVIEW_QUALITIES = {"medium", "review"}


def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, required=True)
    ap.add_argument("--ready", type=Path, required=True)
    ap.add_argument("--review", type=Path, required=True)
    args = ap.parse_args()

    with args.input.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = reader.fieldnames or []
        rows = list(reader)

    ready, review = [], []
    unknown = []
    for row in rows:
        q = (row.get("quality") or "").strip().lower()
        if q in READY_QUALITIES:
            ready.append(row)
        elif q in REVIEW_QUALITIES:
            review.append(row)
        else:
            unknown.append((row.get("audio_number"), q))

    if unknown:
        raise SystemExit(f"Nieznane quality: {unknown}")

    write_tsv(args.ready, ready, fields)
    write_tsv(args.review, review, fields)

    print(f"TOTAL={len(rows)}")
    print(f"READY={len(ready)}")
    print(f"REVIEW={len(review)}")
    print("REVIEW_NUMBERS=" + ",".join(r["audio_number"] for r in review))


if __name__ == "__main__":
    main()
