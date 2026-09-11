from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
REQUIRED_HEADERS = ("id", "name", "artist", "album")
SERVICE_TO_MIDDLE_END_COLUMN = {
    "spotify": "spotify_id",
    "youtube": "youtube_video_id",
    "youtube_music": "youtube_video_id",
}


def _column_index(cell_ref: str) -> int:
    match = re.match(r"[A-Z]+", cell_ref or "A1")
    if not match:
        raise ValueError(f"Nieprawidłowy adres komórki XLSX: {cell_ref!r}")
    number = 0
    for char in match.group(0):
        number = number * 26 + ord(char) - 64
    return number - 1


def _first_sheet_path(archive: ZipFile) -> tuple[list[str], str]:
    ns = {"m": MAIN_NS, "p": PKG_REL_NS}
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
    targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels.findall("p:Relationship", ns)}
    target = targets[rel_id]
    sheet_path = target.lstrip("/") if target.startswith("/") else "xl/" + target.lstrip("./")
    return shared, sheet_path


def read_xlsx_tracks(path: str | Path) -> list[dict[str, str]]:
    ns = {"m": MAIN_NS}
    with ZipFile(Path(path)) as archive:
        shared, sheet_path = _first_sheet_path(archive)
        root = ET.fromstring(archive.read(sheet_path))
        rows = []
        for row in root.findall(".//m:sheetData/m:row", ns):
            values = {}
            for cell in row.findall("m:c", ns):
                idx = _column_index(cell.attrib.get("r", "A1"))
                typ = cell.attrib.get("t")
                value_node = cell.find("m:v", ns)
                inline_node = cell.find("m:is", ns)
                value = ""
                if typ == "s" and value_node is not None:
                    value = shared[int(value_node.text)]
                elif typ == "inlineStr" and inline_node is not None:
                    value = "".join(node.text or "" for node in inline_node.iterfind(".//m:t", ns))
                elif value_node is not None:
                    value = value_node.text or ""
                values[idx] = value.strip()
            if values:
                record = [""] * (max(values) + 1)
                for idx, value in values.items():
                    record[idx] = value
                rows.append(record)
    if not rows:
        raise ValueError("XLSX jest pusty")
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    headers = [value.strip().lower() for value in rows[0]]
    index = {name: i for i, name in enumerate(headers)}
    missing = [name for name in REQUIRED_HEADERS if name not in index]
    if missing:
        raise ValueError(f"Brak wymaganych kolumn XLSX: {missing}; znaleziono: {headers}")
    tracks = []
    for row_no, row in enumerate(rows[1:], start=2):
        track = {name: row[index[name]].strip() for name in REQUIRED_HEADERS}
        if not any(track.values()):
            continue
        if not track["id"]:
            raise ValueError(f"Wiersz {row_no}: brak id")
        tracks.append(track)
    if not tracks:
        raise ValueError("XLSX nie zawiera utworów")
    return tracks


def _tags_json(tags: list[str]) -> str:
    out = []
    for tag in tags:
        tag = tag.strip()
        if tag and tag not in out:
            out.append(tag)
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))


def import_playlist_xlsx(
    conn,
    *,
    source_path: str | Path,
    playlist_id: str,
    playlist_series_id: str | None,
    service: str,
    name: str,
    exported_at: str | None,
    tags: list[str],
    external_playlist_id: str | None = None,
    external_url: str | None = None,
    dry_run: bool = False,
) -> dict:
    if service not in SERVICE_TO_MIDDLE_END_COLUMN:
        raise ValueError(f"Nieobsługiwany service: {service}")
    tracks = read_xlsx_tracks(source_path)
    track_ids = [track["id"] for track in tracks]
    metadata = {}
    for track in tracks:
        old = metadata.get(track["id"])
        if old is None:
            metadata[track["id"]] = dict(track)
            continue
        for field in ("name", "artist", "album"):
            if old[field] and track[field] and old[field] != track[field]:
                raise ValueError(f"Ten sam id {track['id']} ma różne {field} w XLSX")
            if not old[field] and track[field]:
                old[field] = track[field]

    summary = {
        "mode": "dry-run" if dry_run else "apply",
        "playlist_id": playlist_id,
        "positions": len(tracks),
        "distinct_external_ids": len(metadata),
        "external_track_inserted": 0,
        "external_track_existing": 0,
        "metadata_filled": 0,
        "metadata_conflicts": 0,
        "mapping_inserted": 0,
        "mapping_preexisting": 0,
        "mapping_no_candidate": 0,
        "mapping_ambiguous": 0,
        "mapping_conflicts": 0,
    }

    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("BEGIN")
    try:
        existing = conn.execute("SELECT 1 FROM playlist WHERE playlist_id=?", (playlist_id,)).fetchone()
        if existing:
            current_ids = [row[0] for row in conn.execute(
                """SELECT e.external_track_id FROM playlist_item i
                   JOIN external_track e ON e.external_track_pk=i.external_track_pk
                   WHERE i.playlist_id=? ORDER BY i.position""", (playlist_id,)).fetchall()]
            if current_ids != track_ids:
                raise RuntimeError(f"playlist_id {playlist_id} już istnieje z inną zawartością")
            summary["playlist_already_identical"] = True
        else:
            conn.execute(
                """INSERT INTO playlist(
                       playlist_id, playlist_series_id, service, name,
                       external_playlist_id, external_url, source_file, exported_at, tags
                   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (playlist_id, playlist_series_id, service, name, external_playlist_id,
                 external_url, Path(source_path).name, exported_at, _tags_json(tags)),
            )
            summary["playlist_already_identical"] = False

        pk_by_id = {}
        for external_id, track in metadata.items():
            row = conn.execute(
                "SELECT external_track_pk, title, artist, album FROM external_track WHERE service=? AND external_track_id=?",
                (service, external_id),
            ).fetchone()
            if row is None:
                cur = conn.execute(
                    "INSERT INTO external_track(service, external_track_id, title, artist, album) VALUES (?, ?, ?, ?, ?)",
                    (service, external_id, track["name"], track["artist"], track["album"]),
                )
                pk = int(cur.lastrowid)
                summary["external_track_inserted"] += 1
            else:
                pk = int(row[0])
                summary["external_track_existing"] += 1
                current = {"name": row[1] or "", "artist": row[2] or "", "album": row[3] or ""}
                sql_field = {"name": "title", "artist": "artist", "album": "album"}
                for field in ("name", "artist", "album"):
                    incoming = track[field].strip()
                    saved = current[field].strip()
                    if not saved and incoming:
                        conn.execute(f"UPDATE external_track SET {sql_field[field]}=? WHERE external_track_pk=?", (incoming, pk))
                        summary["metadata_filled"] += 1
                    elif saved and incoming and saved != incoming:
                        summary["metadata_conflicts"] += 1
            pk_by_id[external_id] = pk

        if not existing:
            conn.executemany(
                "INSERT INTO playlist_item(playlist_id, position, external_track_pk) VALUES (?, ?, ?)",
                [(playlist_id, pos, pk_by_id[track["id"]]) for pos, track in enumerate(tracks, start=1)],
            )

        middle_col = SERVICE_TO_MIDDLE_END_COLUMN[service]
        for external_id, pk in pk_by_id.items():
            bridge = [row[0] for row in conn.execute(
                "SELECT utwu_id FROM external_track_utwu WHERE external_track_pk=? ORDER BY utwu_id", (pk,)).fetchall()]
            candidates = [row[0] for row in conn.execute(
                f"SELECT utwu_id FROM middle_end WHERE {middle_col}=? ORDER BY utwu_id", (external_id,)).fetchall()]
            if bridge:
                summary["mapping_preexisting"] += 1
                if len(candidates) == 1 and candidates[0] not in bridge:
                    summary["mapping_conflicts"] += 1
            elif len(candidates) == 1:
                conn.execute("INSERT INTO external_track_utwu(external_track_pk, utwu_id) VALUES (?, ?)", (pk, candidates[0]))
                summary["mapping_inserted"] += 1
            elif len(candidates) == 0:
                summary["mapping_no_candidate"] += 1
            else:
                summary["mapping_ambiguous"] += 1

        stats = conn.execute(
            """SELECT COUNT(*),
                      SUM(CASE WHEN EXISTS(SELECT 1 FROM external_track_utwu x WHERE x.external_track_pk=i.external_track_pk) THEN 1 ELSE 0 END),
                      COUNT(DISTINCT i.external_track_pk),
                      COUNT(DISTINCT CASE WHEN NOT EXISTS(SELECT 1 FROM external_track_utwu x WHERE x.external_track_pk=i.external_track_pk) THEN i.external_track_pk END)
               FROM playlist_item i WHERE i.playlist_id=?""", (playlist_id,)).fetchone()
        summary.update(
            live_positions=int(stats[0] or 0),
            mapped_positions=int(stats[1] or 0),
            unmapped_positions=int((stats[0] or 0) - (stats[1] or 0)),
            distinct_tracks=int(stats[2] or 0),
            distinct_unmapped=int(stats[3] or 0),
        )
        coverage = conn.execute(
            """SELECT COUNT(*),
                      SUM(CASE WHEN me.lyrics_id IS NOT NULL THEN 1 ELSE 0 END),
                      SUM(CASE WHEN me.lyrics_id IS NOT NULL AND EXISTS(SELECT 1 FROM tag_snapshots ts WHERE ts.lyrics_id=me.lyrics_id) THEN 1 ELSE 0 END)
               FROM playlist_item i
               JOIN external_track_utwu x ON x.external_track_pk=i.external_track_pk
               JOIN middle_end me ON me.utwu_id=x.utwu_id
               WHERE i.playlist_id=?""", (playlist_id,)).fetchone()
        summary.update(
            mapped_position_links=int(coverage[0] or 0),
            positions_with_lyrics_id=int(coverage[1] or 0),
            positions_with_tag_snapshot=int(coverage[2] or 0),
        )
        if summary["mapping_conflicts"]:
            raise RuntimeError(f"Wykryto {summary['mapping_conflicts']} konfliktów bridge vs middle_end")
        conn.execute("ROLLBACK" if dry_run else "COMMIT")
        return summary
    except Exception:
        try:
            conn.execute("ROLLBACK")
        except Exception:
            pass
        raise
