from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"

PLAYLISTS = [
    {
        "source_file": "Glebi 2.xlsx",
        "playlist_id": "spotify:wyspa-glebi:2026-09-11",
        "playlist_series_id": "spotify:wyspa-glebi",
        "name": "Wyspa Głębi",
        "external_playlist_id": "2XlvqJZUNVjR4KGIpF39nG",
        "external_url": "https://open.spotify.com/playlist/2XlvqJZUNVjR4KGIpF39nG",
    },
    {
        "source_file": "Swiatla.xlsx",
        "playlist_id": "spotify:wyspa-swiatla:2026-09-11",
        "playlist_series_id": "spotify:wyspa-swiatla",
        "name": "Wyspa Światła",
        "external_playlist_id": None,
        "external_url": None,
    },
    {
        "source_file": "Ruchu.xlsx",
        "playlist_id": "spotify:wyspa-ruchu:2026-09-11",
        "playlist_series_id": "spotify:wyspa-ruchu",
        "name": "Wyspa Ruchu",
        "external_playlist_id": None,
        "external_url": None,
    },
    {
        "source_file": "Peryferia.xlsx",
        "playlist_id": "spotify:peryferia:2026-09-11",
        "playlist_series_id": "spotify:peryferia",
        "name": "Peryferia",
        "external_playlist_id": None,
        "external_url": None,
    },
]


def _col_idx(ref: str) -> int:
    match = re.match(r"[A-Z]+", ref or "A1")
    if not match:
        raise ValueError(f"Nieprawidłowy adres komórki XLSX: {ref!r}")
    number = 0
    for char in match.group(0):
        number = number * 26 + ord(char) - 64
    return number - 1


def _read_sheet(path: Path) -> list[list[str]]:
    ns = {"m": MAIN_NS, "p": PKG_REL_NS}
    with ZipFile(path) as archive:
        shared = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            shared = [
                "".join(node.text or "" for node in item.iterfind(".//m:t", ns))
                for item in root.findall("m:si", ns)
            ]
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        sheet = workbook.find("m:sheets", ns)[0]
        rel_id = sheet.attrib[f"{{{REL_NS}}}id"]
        rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        targets = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rels.findall("p:Relationship", ns)
        }
        target = targets[rel_id]
        sheet_path = target.lstrip("/") if target.startswith("/") else "xl/" + target.lstrip("./")
        root = ET.fromstring(archive.read(sheet_path))
        rows = []
        for row in root.findall(".//m:sheetData/m:row", ns):
            values = {}
            for cell in row.findall("m:c", ns):
                idx = _col_idx(cell.attrib.get("r", "A1"))
                typ = cell.attrib.get("t")
                value_node = cell.find("m:v", ns)
                inline_node = cell.find("m:is", ns)
                value = ""
                if typ == "s" and value_node is not None:
                    value = shared[int(value_node.text)]
                elif typ == "inlineStr" and inline_node is not None:
                    value = "".join(
                        node.text or "" for node in inline_node.iterfind(".//m:t", ns)
                    )
                elif value_node is not None:
                    value = value_node.text or ""
                values[idx] = value.strip()
            if values:
                record = [""] * (max(values) + 1)
                for idx, value in values.items():
                    record[idx] = value
                rows.append(record)
    width = max((len(row) for row in rows), default=0)
    return [row + [""] * (width - len(row)) for row in rows]


def read_playlist(path: Path) -> dict:
    rows = _read_sheet(path)
    if not rows:
        raise ValueError(f"{path.name}: pusty XLSX")
    headers = [value.strip().lower() for value in rows[0]]
    index = {name: i for i, name in enumerate(headers)}
    required = ("id", "name", "artist", "album")
    missing = [name for name in required if name not in index]
    if missing:
        raise ValueError(f"{path.name}: brak kolumn {missing}; są {headers}")

    tracks = []
    blank = []
    seen_positions = set()
    for source_row, row in enumerate(rows[1:], start=2):
        data = {name: row[index[name]].strip() for name in required}
        if not any(data.values()):
            continue
        if "index" in index and row[index["index"]].strip():
            raw_index = row[index["index"]].strip()
            try:
                position = int(float(raw_index)) + 1
            except ValueError as exc:
                raise ValueError(f"{path.name}: nieprawidłowy index {raw_index!r} w wierszu {source_row}") from exc
        else:
            position = len(tracks) + len(blank) + 1
        if position <= 0 or position in seen_positions:
            raise ValueError(f"{path.name}: nieprawidłowa lub powtórzona pozycja {position}")
        seen_positions.add(position)
        data["position"] = position
        data["source_row"] = source_row
        if not data["id"]:
            blank.append(data)
        else:
            tracks.append(data)

    return {
        "source_positions": len(tracks) + len(blank),
        "tracks": tracks,
        "blank_id_rows": blank,
    }


def import_island_playlists(conn, root: Path, dry_run: bool) -> dict:
    parsed = {}
    all_metadata = {}
    input_metadata_conflicts = 0
    all_ids = set()

    for config in PLAYLISTS:
        data = read_playlist(root / config["source_file"])
        parsed[config["playlist_id"]] = data
        for track in data["tracks"]:
            external_id = track["id"]
            all_ids.add(external_id)
            previous = all_metadata.get(external_id)
            if previous is None:
                all_metadata[external_id] = dict(track)
            else:
                for field in ("name", "artist", "album"):
                    a = (previous.get(field) or "").strip()
                    b = (track.get(field) or "").strip()
                    if a and b and a != b:
                        input_metadata_conflicts += 1
                    elif not a and b:
                        previous[field] = b

    summaries = {}
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("BEGIN")
    try:
        existing_tracks = {
            row[1]: {
                "pk": int(row[0]),
                "title": row[2] or "",
                "artist": row[3] or "",
                "album": row[4] or "",
            }
            for row in conn.execute(
                "SELECT external_track_pk, external_track_id, title, artist, album FROM external_track WHERE service='spotify'"
            ).fetchall()
        }

        missing_ids = sorted(all_ids - set(existing_tracks))
        if missing_ids:
            conn.executemany(
                "INSERT INTO external_track(service, external_track_id, title, artist, album) VALUES ('spotify', ?, ?, ?, ?)",
                [
                    (
                        external_id,
                        all_metadata[external_id]["name"],
                        all_metadata[external_id]["artist"],
                        all_metadata[external_id]["album"],
                    )
                    for external_id in missing_ids
                ],
            )

        track_rows = conn.execute(
            "SELECT external_track_pk, external_track_id, title, artist, album FROM external_track WHERE service='spotify'"
        ).fetchall()
        track_by_id = {
            row[1]: {
                "pk": int(row[0]),
                "title": row[2] or "",
                "artist": row[3] or "",
                "album": row[4] or "",
            }
            for row in track_rows
        }

        metadata_conflicts = 0
        for external_id in all_ids:
            saved = track_by_id[external_id]
            incoming = all_metadata[external_id]
            for source_field, saved_field in (("name", "title"), ("artist", "artist"), ("album", "album")):
                a = (saved[saved_field] or "").strip()
                b = (incoming[source_field] or "").strip()
                if a and b and a != b:
                    metadata_conflicts += 1

        middle = defaultdict(list)
        lyrics_by_utwu = {}
        for spotify_id, utwu_id, lyrics_id in conn.execute(
            "SELECT spotify_id, utwu_id, lyrics_id FROM middle_end WHERE spotify_id IS NOT NULL"
        ).fetchall():
            middle[spotify_id].append(utwu_id)
            lyrics_by_utwu[utwu_id] = lyrics_id

        bridge = defaultdict(set)
        for external_id, utwu_id in conn.execute(
            """
            SELECT e.external_track_id, x.utwu_id
            FROM external_track e
            JOIN external_track_utwu x ON x.external_track_pk=e.external_track_pk
            WHERE e.service='spotify'
            """
        ).fetchall():
            bridge[external_id].add(utwu_id)

        mapping_insert_rows = []
        mapping_no_candidate = 0
        mapping_ambiguous = 0
        mapping_preexisting = 0
        mapping_conflicts = 0
        for external_id in sorted(all_ids):
            candidates = middle.get(external_id, [])
            existing = bridge.get(external_id, set())
            if existing:
                mapping_preexisting += 1
                if len(candidates) == 1 and candidates[0] not in existing:
                    mapping_conflicts += 1
                continue
            if len(candidates) == 1:
                mapping_insert_rows.append((track_by_id[external_id]["pk"], candidates[0]))
                bridge[external_id].add(candidates[0])
            elif len(candidates) == 0:
                mapping_no_candidate += 1
            else:
                mapping_ambiguous += 1

        if mapping_conflicts:
            raise RuntimeError(f"Konflikty external_track_utwu vs middle_end: {mapping_conflicts}")
        if mapping_insert_rows:
            conn.executemany(
                "INSERT INTO external_track_utwu(external_track_pk, utwu_id) VALUES (?, ?)",
                mapping_insert_rows,
            )

        tagged_lyrics = {
            row[0]
            for row in conn.execute("SELECT DISTINCT lyrics_id FROM tag_snapshots").fetchall()
            if row[0] is not None
        }

        for config in PLAYLISTS:
            playlist_id = config["playlist_id"]
            data = parsed[playlist_id]
            expected_pairs = [
                (track["position"], track["id"])
                for track in data["tracks"]
            ]
            exists = conn.execute(
                "SELECT 1 FROM playlist WHERE playlist_id=?",
                (playlist_id,),
            ).fetchone() is not None

            if exists:
                current_pairs = [
                    (int(row[0]), row[1])
                    for row in conn.execute(
                        """
                        SELECT i.position, e.external_track_id
                        FROM playlist_item i
                        JOIN external_track e ON e.external_track_pk=i.external_track_pk
                        WHERE i.playlist_id=?
                        ORDER BY i.position
                        """,
                        (playlist_id,),
                    ).fetchall()
                ]
                if current_pairs != expected_pairs:
                    raise RuntimeError(f"{playlist_id}: istnieje z inną zawartością")
                already_identical = True
            else:
                conn.execute(
                    """
                    INSERT INTO playlist(
                        playlist_id, playlist_series_id, service, name,
                        external_playlist_id, external_url, source_file,
                        exported_at, tags
                    ) VALUES (?, ?, 'spotify', ?, ?, ?, ?, NULL, ?)
                    """,
                    (
                        playlist_id,
                        config["playlist_series_id"],
                        config["name"],
                        config["external_playlist_id"],
                        config["external_url"],
                        config["source_file"],
                        json.dumps(["owner:maciek-tora"], ensure_ascii=False, separators=(",", ":")),
                    ),
                )
                conn.executemany(
                    "INSERT INTO playlist_item(playlist_id, position, external_track_pk) VALUES (?, ?, ?)",
                    [
                        (playlist_id, track["position"], track_by_id[track["id"]]["pk"])
                        for track in data["tracks"]
                    ],
                )
                already_identical = False

            mapped_positions = 0
            positions_with_lyrics = 0
            positions_with_tags = 0
            distinct_unmapped = set()
            for track in data["tracks"]:
                targets = bridge.get(track["id"], set())
                if targets:
                    mapped_positions += 1
                    lyrics_ids = {
                        lyrics_by_utwu.get(utwu_id)
                        for utwu_id in targets
                        if lyrics_by_utwu.get(utwu_id)
                    }
                    if lyrics_ids:
                        positions_with_lyrics += 1
                    if any(lyrics_id in tagged_lyrics for lyrics_id in lyrics_ids):
                        positions_with_tags += 1
                else:
                    distinct_unmapped.add(track["id"])

            summaries[playlist_id] = {
                "name": config["name"],
                "source_file": config["source_file"],
                "source_positions": data["source_positions"],
                "imported_positions": len(data["tracks"]),
                "omitted_blank_ids": len(data["blank_id_rows"]),
                "blank_id_source_rows": [row["source_row"] for row in data["blank_id_rows"]],
                "distinct_external_ids": len({track["id"] for track in data["tracks"]}),
                "mapped_positions": mapped_positions,
                "unmapped_positions": len(data["tracks"]) - mapped_positions,
                "distinct_unmapped": len(distinct_unmapped),
                "positions_with_lyrics_id": positions_with_lyrics,
                "positions_with_tag_snapshot": positions_with_tags,
                "already_identical": already_identical,
                "external_playlist_id": config["external_playlist_id"],
                "external_url": config["external_url"],
            }

        result = {
            "mode": "dry-run" if dry_run else "apply",
            "playlists": summaries,
            "aggregate": {
                "source_positions": sum(v["source_positions"] for v in summaries.values()),
                "imported_positions": sum(v["imported_positions"] for v in summaries.values()),
                "omitted_blank_ids": sum(v["omitted_blank_ids"] for v in summaries.values()),
                "external_track_inserted": len(missing_ids),
                "mapping_inserted": len(mapping_insert_rows),
                "mapping_preexisting": mapping_preexisting,
                "mapping_no_candidate": mapping_no_candidate,
                "mapping_ambiguous": mapping_ambiguous,
                "metadata_conflicts": metadata_conflicts,
                "input_metadata_conflicts": input_metadata_conflicts,
            },
        }

        conn.execute("ROLLBACK" if dry_run else "COMMIT")
        return result
    except Exception:
        try:
            conn.execute("ROLLBACK")
        except Exception:
            pass
        raise
