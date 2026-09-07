from __future__ import annotations

import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
A1_STRUCTURE_TSV = REPO_ROOT / "rosja" / "SOL_mapa-struktury-A1-z-opisami.tsv"
MIGRATION_KEY = "content_a1_volumes_v1"


def _scalar(conn, sql: str, params=()):
    row = conn.execute(sql, params).fetchone()
    return None if row is None else row[0]


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _has_column(conn, table: str, column: str) -> bool:
    return any(row[1] == column for row in conn.execute(f"PRAGMA table_info({table})").fetchall())


def _ensure_structure_order_column(conn) -> None:
    if not _has_column(conn, "content_sections", "structure_order"):
        conn.execute("ALTER TABLE content_sections ADD COLUMN structure_order INTEGER")
    conn.execute(
        "UPDATE content_sections SET structure_order = section_order WHERE structure_order IS NULL"
    )


def _validate_source(rows: list[dict[str, str]]) -> None:
    if len(rows) != 33:
        raise RuntimeError(f"STOP A1 STRUCTURE: oczekiwano 33 rekordów, jest {len(rows)}")
    toms = [r for r in rows if r["typ_struktury"].strip() == "TOM"]
    headings = [r for r in rows if r["typ_struktury"].strip().startswith("H")]
    if len(toms) != 9 or len(headings) != 24:
        raise RuntimeError(
            f"STOP A1 STRUCTURE: oczekiwano 9 TOM + 24 H, jest {len(toms)} TOM + {len(headings)} H"
        )
    orders = [int(r["kolejnosc"]) for r in rows]
    if sorted(orders) != list(range(1, 34)):
        raise RuntimeError("STOP A1 STRUCTURE: kolejnosc nie jest dokładnie 1..33")
    anchors = [r["anchor"].strip() for r in rows]
    if any(not a for a in anchors) or len(set(anchors)) != 33:
        raise RuntimeError("STOP A1 STRUCTURE: pusty lub zduplikowany anchor")


def _validate_database(conn, document_id: int) -> None:
    headings = int(
        _scalar(
            conn,
            "SELECT count(*) FROM content_sections WHERE document_id=? AND section_kind='heading'",
            (document_id,),
        )
        or 0
    )
    volumes = int(
        _scalar(
            conn,
            "SELECT count(*) FROM content_sections WHERE document_id=? AND section_kind='volume'",
            (document_id,),
        )
        or 0
    )
    nodes = int(
        _scalar(conn, "SELECT count(*) FROM content_sections WHERE document_id=?", (document_id,))
        or 0
    )
    distinct_structure_orders = int(
        _scalar(
            conn,
            "SELECT count(DISTINCT structure_order) FROM content_sections WHERE document_id=?",
            (document_id,),
        )
        or 0
    )
    bad_parents = int(
        _scalar(
            conn,
            """
            SELECT count(*)
            FROM content_sections s
            WHERE s.document_id=? AND s.depth>1 AND s.parent_section_id IS NULL
            """,
            (document_id,),
        )
        or 0
    )
    if (headings, volumes, nodes, distinct_structure_orders, bad_parents) != (24, 9, 33, 33, 0):
        raise RuntimeError(
            "STOP A1 STRUCTURE DB: "
            f"headings={headings}, volumes={volumes}, nodes={nodes}, "
            f"structure_orders={distinct_structure_orders}, bad_parents={bad_parents}"
        )


def ensure_content_structure_v2(conn) -> dict:
    """Dodaj osobny porządek strukturalny i 9 TOMÓW A1. Operacja jednorazowa."""
    _ensure_structure_order_column(conn)

    document_id = _scalar(
        conn,
        "SELECT document_id FROM content_documents WHERE collection_id='rosja' AND document_code='A1'",
    )
    if document_id is None:
        raise RuntimeError("STOP A1 STRUCTURE: brak dokumentu rosja/A1")
    document_id = int(document_id)

    marker = _scalar(conn, "SELECT value FROM content_meta WHERE key=?", (MIGRATION_KEY,))
    if marker == "done":
        _validate_database(conn, document_id)
        return {"status": "ready", "migrated": False, "volumes": 9, "nodes": 33}
    if marker not in (None, ""):
        raise RuntimeError(f"STOP A1 STRUCTURE: nieznany marker {marker!r}")

    rows = _rows(A1_STRUCTURE_TSV)
    _validate_source(rows)

    db_heading_anchors = {
        row[0]
        for row in conn.execute(
            "SELECT anchor FROM content_sections WHERE document_id=? AND section_kind='heading'",
            (document_id,),
        ).fetchall()
    }
    source_heading_anchors = {
        r["anchor"].strip() for r in rows if r["typ_struktury"].strip().startswith("H")
    }
    if db_heading_anchors != source_heading_anchors:
        missing = sorted(source_heading_anchors - db_heading_anchors)
        extra = sorted(db_heading_anchors - source_heading_anchors)
        raise RuntimeError(f"STOP A1 STRUCTURE: różne anchory H; missing={missing}, extra={extra}")

    conn.execute("BEGIN TRANSACTION")
    try:
        # Najpierw wpisujemy pełny porządek i głębokość dla istniejących H.
        for row in rows:
            kind = row["typ_struktury"].strip()
            if kind.startswith("H"):
                conn.execute(
                    """
                    UPDATE content_sections
                    SET structure_order=?, depth=?
                    WHERE document_id=? AND section_kind='heading' AND anchor=?
                    """,
                    (
                        int(row["kolejnosc"]),
                        int(row["glebokosc_struktury"]),
                        document_id,
                        row["anchor"].strip(),
                    ),
                )

        next_section_id = int(_scalar(conn, "SELECT COALESCE(max(section_id),0)+1 FROM content_sections") or 1)
        h1_id = int(
            _scalar(
                conn,
                "SELECT section_id FROM content_sections WHERE document_id=? AND anchor='kolumbryna'",
                (document_id,),
            )
        )

        # section_order pozostaje porządkiem H-only. TOMY dostają techniczne 1000+n.
        for row in rows:
            if row["typ_struktury"].strip() != "TOM":
                continue
            conn.execute(
                """
                INSERT INTO content_sections(
                    section_id, document_id, parent_section_id, section_kind, heading_level,
                    depth, section_order, structure_order, section_title, anchor, description
                ) VALUES (?, ?, ?, 'volume', NULL, ?, ?, ?, ?, ?, ?)
                """,
                (
                    next_section_id,
                    document_id,
                    h1_id,
                    int(row["glebokosc_struktury"]),
                    1000 + int(row["kolejnosc"]),
                    int(row["kolejnosc"]),
                    row["sekcja_tytul"].strip(),
                    row["anchor"].strip(),
                    row["opis"].strip() or None,
                ),
            )
            next_section_id += 1

        anchor_to_id = {
            anchor: int(section_id)
            for section_id, anchor in conn.execute(
                "SELECT section_id, anchor FROM content_sections WHERE document_id=?",
                (document_id,),
            ).fetchall()
        }

        # Parentage dokładnie z 33-wierszowej mapy struktury.
        for row in rows:
            anchor = row["anchor"].strip()
            parent_anchor = row["parent_anchor"].strip()
            parent_id = anchor_to_id[parent_anchor] if parent_anchor else None
            conn.execute(
                "UPDATE content_sections SET parent_section_id=? WHERE document_id=? AND anchor=?",
                (parent_id, document_id, anchor),
            )

        _validate_database(conn, document_id)
        conn.execute("INSERT INTO content_meta(key,value) VALUES (?, 'done')", (MIGRATION_KEY,))
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise

    return {"status": "ready", "migrated": True, "volumes": 9, "nodes": 33}


def fetch_content_structure(conn, collection_id: str) -> list[dict]:
    rows = conn.execute(
        """
        SELECT
            d.collection_id,
            d.document_code,
            d.document_title,
            d.canonical_url,
            d.source_filename,
            d.source_url,
            d.sort_order,
            s.section_kind,
            CASE
                WHEN s.section_kind='heading' THEN 'H' || CAST(s.heading_level AS TEXT)
                WHEN s.section_kind='volume' THEN 'TOM'
                ELSE upper(s.section_kind)
            END,
            s.depth,
            COALESCE(s.structure_order, s.section_order),
            s.section_order,
            s.section_title,
            COALESCE(s.anchor,''),
            CASE WHEN s.anchor IS NULL OR trim(s.anchor)='' THEN 'BRAK' ELSE 'OK' END,
            CASE
                WHEN s.anchor IS NULL OR trim(s.anchor)='' THEN ''
                ELSE rtrim(d.canonical_url,'#') || '#' || s.anchor
            END,
            COALESCE(s.description,''),
            COALESCE(s.content_html,'')
        FROM content_sections s
        JOIN content_documents d ON d.document_id=s.document_id
        WHERE d.collection_id=?
        ORDER BY d.sort_order, COALESCE(s.structure_order, s.section_order), s.section_id
        """,
        (collection_id,),
    ).fetchall()
    columns = [
        "collection_id", "dokument_kod", "dokument_tytul", "canonical_url",
        "dokument_plik", "source_url", "document_sort_order", "section_kind", "poziom",
        "glebokosc", "kolejnosc", "source_order", "sekcja_tytul", "anchor",
        "anchor_status", "deep_link", "opis", "content_html",
    ]
    return [dict(zip(columns, row)) for row in rows]


def fetch_content_collections_v2(conn) -> list[dict]:
    rows = conn.execute(
        """
        SELECT
            c.collection_id,
            c.label,
            c.sort_order,
            count(DISTINCT d.document_id) AS documents,
            sum(CASE WHEN s.section_kind='heading' THEN 1 ELSE 0 END) AS sections,
            count(s.section_id) AS structure_nodes,
            sum(CASE WHEN s.section_kind='volume' THEN 1 ELSE 0 END) AS volumes,
            sum(CASE WHEN s.section_kind='heading' AND s.anchor IS NOT NULL AND trim(s.anchor)<>'' THEN 1 ELSE 0 END) AS anchors_ok,
            sum(CASE WHEN s.section_kind='heading' AND (s.anchor IS NULL OR trim(s.anchor)='') THEN 1 ELSE 0 END) AS anchors_missing,
            sum(CASE WHEN s.section_kind='heading' AND s.description IS NOT NULL AND trim(s.description)<>'' THEN 1 ELSE 0 END) AS descriptions_present,
            sum(CASE WHEN s.section_kind='heading' AND (s.description IS NULL OR trim(s.description)='') THEN 1 ELSE 0 END) AS descriptions_missing
        FROM content_collections c
        LEFT JOIN content_documents d ON d.collection_id=c.collection_id
        LEFT JOIN content_sections s ON s.document_id=d.document_id
        GROUP BY c.collection_id, c.label, c.sort_order
        ORDER BY c.sort_order
        """
    ).fetchall()
    columns = [
        "collection_id", "label", "sort_order", "documents", "sections", "structure_nodes",
        "volumes", "anchors_ok", "anchors_missing", "descriptions_present", "descriptions_missing",
    ]
    return [dict(zip(columns, row)) for row in rows]


def fetch_content_status_v2(conn, collection_id: str) -> dict | None:
    rows = fetch_content_collections_v2(conn)
    for row in rows:
        if row["collection_id"] == collection_id:
            return row
    return None
