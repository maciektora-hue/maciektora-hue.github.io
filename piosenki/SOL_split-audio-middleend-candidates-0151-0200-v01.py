#!/usr/bin/env python3
import csv
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "audio_middleend_candidates_0151_0200.tsv"
READY = ROOT / "audio_middleend_ready_0151_0200.tsv"
REVIEW = ROOT / "audio_middleend_review_0151_0200.tsv"

with SRC.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)

ready = [r for r in rows if r["quality"] in {"exact", "high"}]
review = [r for r in rows if r["quality"] not in {"exact", "high"}]

for path, data in ((READY, ready), (REVIEW, review)):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(data)

c = Counter(r["quality"] for r in rows)
print(f"TOTAL={len(rows)}")
print(f"READY={len(ready)}")
print(f"REVIEW={len(review)}")
print("QUALITY=" + ", ".join(f"{k}:{c[k]}" for k in sorted(c)))
print("REVIEW_NUMBERS=" + ",".join(r["audio_number"] for r in review))
