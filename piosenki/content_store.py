from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
SCHEMA_PATH = HERE / "SOL_content-schema.sql"
ROSJA_TSV = REPO_ROOT / "rosja" / "SOL_mapa-sekcji-z-opisami.tsv"
AUDHD_TSV = REPO_ROOT / "audhd" / "SOL_mapa-sekcji-i-anchorow-audhd.tsv"
IMPORT_KEY = "content_initial_import_v1"

EXPECTED = {
    "collections": 2,
    "documents": 34,
    "sections": 958,
    "rosja_documents": 16,
    "rosja_sections": 620,
    "rosja_descriptions": 620,
    "audhd_documents": 18,
    "audhd_sections": 338,
}


def _rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise RuntimeError(f"Brak pliku wejściowego: {path}")
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _execute_schema(conn) -> None:
    text = SCHEMA_PATH.read_text(encoding="utf-8")
    for raw in text.split(";"):
        statement = raw.strip()
        if statement:
            conn.execute(statement)


def _level(value: str) -> int:
    value = (value or "").strip().upper()
    if len(value) != 2 or value[0] != "H" or value[1] not in "123456":
        raise RuntimeError(f"Nieprawidłowy poziom nagłówka: {value!r}")
    return int(value[1])


def _positive_int(value: str, field: str) -> int:
    try:
        result = int((value or "").strip())
    except (TypeError, ValueError):
        raise RuntimeError(f"Nieprawidłowe {field}: {value!r}")
    if result < 1:
        raise RuntimeError(f"{field} musi być >= 1: {value!r}")
    return result


def _scalar(conn, sql: str, params=()):
    row = conn.execute(sql, params).fetchone()
    return None if row is None else row[0]


def _bulk_insert(conn, table: str, columns: list[str], rows: list[tuple], chunk_size: int = 50) -> None:
    if not rows:
        return
    one = "(" + ",".join("?" for _ in columns) + ")"
    names = ",".join(columns)
    for start in range(0, len(rows), chunk_size):
        chunk = rows[start:start + chunk_size]
        sql = f"INSERT INTO {table} ({names}) VALUES " + ",".join(one for _ in chunk)
        params = []
        for row in chunk:
            params.extend(row)
        conn.execute(sql, tuple(params))


def _validate_sources(rosja: list[dict], audhd: list[dict]) -> None:
    if len(rosja) != 620:
        raise RuntimeError(f"STOP: ROSJA: oczekiwano 620 sekcji, jest {len(rosja)}")
    if len(audhd) != 338:
        raise RuntimeError(f"STOP: AuDHD: oczekiwano 338 sekcji, jest {len(audhd)}")

    for collection, rows, expected_docs in (
        ("rosja", rosja, 16),
        ("audhd", audhd, 18),
    ):
        docs = []
        seen_docs = set()
        anchors = defaultdict(set)
        orders = defaultdict(set)
        for row in rows:
            code = (row.get("dokument_kod") or "").strip()
            filename = (row.get("dokument_plik") or "").strip()
            title = (row.get("sekcja_tytul") or "").strip()
            anchor = (row.get("anchor") or "").strip()
            if not code or not filename or not title:
                raise RuntimeError(f"STOP: {collection}: pusty kod/plik/tytuł: {row}")
            if not anchor:
                raise RuntimeError(f"STOP: {collection}/{code}: pusty anchor: {title}")
            if (row.get("anchor_status") or "").strip() != "OK":
                raise RuntimeError(f"STOP: {collection}/{code}: anchor_status != OK: {title}")
            order = _positive_int(row.get("kolejnosc"), "kolejnosc")
            _positive_int(row.get("glebokosc"), "glebokosc")
            _level(row.get("poziom"))
            if anchor in anchors[code]:
                raise RuntimeError(f"STOP: {collection}/{code}: duplikat anchor: {anchor}")
            if order in orders[code]:
                raise RuntimeError(f"STOP: {collection}/{code}: duplikat kolejnosc: {order}")
            anchors[code].add(anchor)
            orders[code].add(order)
            if code not in seen_docs:
                seen_docs.add(code)
                docs.append(code)
        if len(docs) != expected_docs:
            raise RuntimeError(
                f"STOP: {collection}: oczekiwano {expected_docs} dokumentów, jest {len(docs)}"
            )

    descriptions = sum(1 for row in rosja if (row.get("opis") or "").strip())
    if descriptions != 620:
        raise RuntimeError(f"STOP: ROSJA: oczekiwano 620 opisów, jest {descriptions}")


def _first_rows(rows: list[dict]) -> list[dict]:
    result = []
    seen = set()
    for row in rows:
        code = row["dokument_kod"].strip()
        if code not in seen:
            seen.add(code)
            result.append(row)
    return result


def _build_import_rows(rosja: list[dict], audhd: list[dict]):
    collection_rows = [
        ("rosja", "ROSJA", 10),
        ("audhd", "AuDHD", 20),
    ]

    document_rows = []
    doc_id_by_key = {}
    next_doc_id = 1

    for collection, rows in (("rosja", rosja), ("audhd", audhd)):
        for sort_order, row in enumerate(_first_rows(rows), start=1):
            code = row["dokument_kod"].strip()
            filename = row["dokument_plik"].strip()
            title = row["dokument_tytul"].strip()
            if collection == "rosja":
                canonical_url = row["url_stabilny"].strip()
                source_url = "https://maciektora-hue.github.io/rosja/" + quote(filename)
            else:
                source_url = row["url_zrodlowy"].strip()
                canonical_url = source_url
            if not title or not canonical_url or not source_url:
                raise RuntimeError(f"STOP: {collection}/{code}: brak tytułu lub URL")
            document_rows.append(
                (
                    next_doc_id,
                    collection,
                    code,
                    filename,
                    title,
                    canonical_url,
                    source_url,
                    sort_order,
                )
            )
            doc_id_by_key[(collection, code)] = next_doc_id
            next_doc_id += 1

    grouped = defaultdict(list)
    for collection, rows in (("rosja", rosja), ("audhd", audhd)):
        for row in rows:
            grouped[(collection, row["dokument_kod"].strip())].append(row)
    for key in grouped:
        grouped[key].sort(key=lambda r: _positive_int(r["kolejnosc"], "kolejnosc"))

    section_rows = []
    next_section_id = 1
    for document in document_rows:
        document_id, collection, code = document[0], document[1], document[2]
        stack: list[tuple[int, int]] = []
        for row in grouped[(collection, code)]:
            depth = _positive_int(row["glebokosc"], "glebokosc")
            order = _positive_int(row["kolejnosc"], "kolejnosc")
            while stack and stack[-1][0] >= depth:
                stack.pop()
            parent_id = stack[-1][1] if stack else None
            description = None
            if collection == "rosja":
                description = (row.get("opis") or "").strip() or None
            section_rows.append(
                (
                    next_section_id,
                    document_id,
                    parent_id,
                    "heading",
                    _level(row["poziom"]),
                    depth,
                    order,
                    row["sekcja_tytul"].strip(),
                    row["anchor"].strip(),
                    description,
                )
            )
            stack.append((depth, next_section_id))
            next_section_id += 1

    if len(collection_rows) != 2 or len(document_rows) != 34 or len(section_rows) != 958:
        raise RuntimeError(
            "STOP: generator importu dał złe liczby: "
            f"collections={len(collection_rows)}, documents={len(document_rows)}, sections={len(section_rows)}"
        )
    return collection_rows, document_rows, section_rows


def _validate_database_v1(conn) -> None:
    checks = {
        "collections": "SELECT count(*) FROM content_collections",
        "documents": "SELECT count(*) FROM content_documents",
        "sections": "SELECT count(*) FROM content_sections WHERE section_kind = 'heading'",
        "rosja_documents": "SELECT count(*) FROM content_documents WHERE collection_id = 'rosja'",
        "rosja_sections": """
            SELECT count(*) FROM content_sections s
            JOIN content_documents d ON d.document_id = s.document_id
            WHERE d.collection_id = 'rosja' AND s.section_kind = 'heading'
        """,
        "rosja_descriptions": """
            SELECT count(*) FROM content_sections s
            JOIN content_documents d ON d.document_id = s.document_id
            WHERE d.collection_id = 'rosja'
              AND s.section_kind = 'heading'
              AND s.description IS NOT NULL AND trim(s.description) <> ''
        """,
        "audhd_documents": "SELECT count(*) FROM content_documents WHERE collection_id = 'audhd'",
        "audhd_sections": """
            SELECT count(*) FROM content_sections s
            JOIN content_documents d ON d.document_id = s.document_id
            WHERE d.collection_id = 'audhd' AND s.section_kind = 'heading'
        """,
    }
    for name, sql in checks.items():
        actual = int(_scalar(conn, sql) or 0)
        if actual != EXPECTED[name]:
            raise RuntimeError(f"STOP DB: {name}: oczekiwano {EXPECTED[name]}, jest {actual}")

    missing_anchors = int(
        _scalar(
            conn,
            "SELECT count(*) FROM content_sections WHERE section_kind='heading' AND (anchor IS NULL OR trim(anchor)='')",
        )
        or 0
    )
    if missing_anchors:
        raise RuntimeError(f"STOP DB: brakujące anchory: {missing_anchors}")

    duplicate_anchors = int(
        _scalar(
            conn,
            """
            SELECT count(*) FROM (
                SELECT document_id, anchor, count(*)
                FROM content_sections
                WHERE anchor IS NOT NULL AND trim(anchor) <> ''
                GROUP BY document_id, anchor
                HAVING count(*) > 1
            )
            """,
        )
        or 0
    )
    if duplicate_anchors:
        raise RuntimeError(f"STOP DB: grupy duplikatów anchorów: {duplicate_anchors}")


def ensure_content_storage(conn) -> dict:
    conn.execute("PRAGMA foreign_keys = ON")
    _execute_schema(conn)

    marker = _scalar(conn, "SELECT value FROM content_meta WHERE key = ?", (IMPORT_KEY,))
    if marker == "done":
        return {"status": "ready", "imported": False}
    if marker not in (None, ""):
        raise RuntimeError(f"STOP: nieznana wartość {IMPORT_KEY}: {marker!r}")

    existing_docs = int(_scalar(conn, "SELECT count(*) FROM content_documents") or 0)
    existing_sections = int(_scalar(conn, "SELECT count(*) FROM content_sections") or 0)
    if existing_docs or existing_sections:
        raise RuntimeError(
            "STOP: brak znacznika pierwszego importu, ale content_* nie są puste: "
            f"documents={existing_docs}, sections={existing_sections}"
        )

    rosja = _rows(ROSJA_TSV)
    audhd = _rows(AUDHD_TSV)
    _validate_sources(rosja, audhd)
    collection_rows, document_rows, section_rows = _build_import_rows(rosja, audhd)

    conn.execute("BEGIN TRANSACTION")
    try:
        _bulk_insert(
            conn,
            "content_collections",
            ["collection_id", "label", "sort_order"],
            collection_rows,
        )
        _bulk_insert(
            conn,
            "content_documents",
            [
                "document_id", "collection_id", "document_code", "source_filename",
                "document_title", "canonical_url", "source_url", "sort_order",
            ],
            document_rows,
        )
        _bulk_insert(
            conn,
            "content_sections",
            [
                "section_id", "document_id", "parent_section_id", "section_kind",
                "heading_level", "depth", "section_order", "section_title", "anchor",
                "description",
            ],
            section_rows,
            chunk_size=40,
        )

        _validate_database_v1(conn)
        conn.execute(
            "INSERT INTO content_meta(key, value) VALUES (?, 'done')",
            (IMPORT_KEY,),
        )
        conn.execute(
            "INSERT INTO content_meta(key, value) VALUES ('content_initial_import_v1_utc', ?)",
            (datetime.now(timezone.utc).isoformat(),),
        )
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise

    return {"status": "ready", "imported": True}


def fetch_content_collections(conn) -> list[dict]:
    rows = conn.execute(
        """
        SELECT c.collection_id, c.label, c.sort_order,
               COALESCE(s.documents, 0), COALESCE(s.sections, 0),
               COALESCE(s.anchors_ok, 0), COALESCE(s.anchors_missing, 0),
               COALESCE(s.descriptions_present, 0), COALESCE(s.descriptions_missing, 0)
        FROM content_collections c
        LEFT JOIN v_content_status s ON s.collection_id = c.collection_id
        ORDER BY c.sort_order
        """
    ).fetchall()
    columns = [
        "collection_id", "label", "sort_order", "documents", "sections",
        "anchors_ok", "anchors_missing", "descriptions_present", "descriptions_missing",
    ]
    return [dict(zip(columns, row)) for row in rows]


def fetch_content_rows(conn, collection_id: str) -> list[dict]:
    rows = conn.execute(
        """
        SELECT collection_id, sekcja_tytul, anchor, anchor_status, deep_link, opis,
               dokument_tytul, canonical_url, dokument_kod, poziom, glebokosc,
               kolejnosc, dokument_plik, source_url, document_sort_order
        FROM v_content_human
        WHERE collection_id = ?
        ORDER BY document_sort_order, kolejnosc
        """,
        (collection_id,),
    ).fetchall()
    columns = [
        "collection_id", "sekcja_tytul", "anchor", "anchor_status", "deep_link", "opis",
        "dokument_tytul", "canonical_url", "dokument_kod", "poziom", "glebokosc",
        "kolejnosc", "dokument_plik", "source_url", "document_sort_order",
    ]
    return [dict(zip(columns, row)) for row in rows]


def fetch_content_status(conn, collection_id: str) -> dict | None:
    row = conn.execute(
        """
        SELECT collection_id, documents, sections, anchors_ok, anchors_missing,
               descriptions_present, descriptions_missing
        FROM v_content_status
        WHERE collection_id = ?
        """,
        (collection_id,),
    ).fetchone()
    if row is None:
        return None
    columns = [
        "collection_id", "documents", "sections", "anchors_ok", "anchors_missing",
        "descriptions_present", "descriptions_missing",
    ]
    return dict(zip(columns, row))
