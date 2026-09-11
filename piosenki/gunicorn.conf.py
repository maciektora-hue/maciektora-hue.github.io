import json
import os
from pathlib import Path


def when_ready(server):
    if os.environ.get("SOL_INSPECT_ISLAND_XLSX") != "1":
        return

    from playlist_importer import read_xlsx_tracks

    root = Path(__file__).resolve().parent.parent / "dane-robocze" / "csv-tsv" / "piosenki"
    files = ["Glebi 2.xlsx", "Swiatla.xlsx", "Ruchu.xlsx", "Peryferia.xlsx"]
    for filename in files:
        tracks = read_xlsx_tracks(root / filename)
        payload = {
            "file": filename,
            "positions": len(tracks),
            "distinct_ids": len({t["id"] for t in tracks}),
            "first3": tracks[:3],
            "last3": tracks[-3:],
        }
        print("ISLAND_XLSX_OK " + json.dumps(payload, ensure_ascii=False, sort_keys=True), flush=True)
