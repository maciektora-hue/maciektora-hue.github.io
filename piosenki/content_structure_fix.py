from __future__ import annotations

from content_structure import (
    A1_STRUCTURE_TSV,
    MIGRATION_KEY,
    _ensure_structure_order_column,
    _rows,
    _scalar,
    _validate_database,
    _validate_source,
)


def ensure_content_structure_v2_safe(conn) -> dict:
    """Jednorazowo dodaj 9 TOMOW A1. Bez zagniezdzonego BEGIN."""
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
        raise RuntimeError(f"STOP A1 STRUCTURE: rozne anchory H; missing={missing}, extra={extra}")

    # SAVEPOINT dziala takze wtedy, gdy driver ma juz otwarta transakcje implicit.
    conn.execute("SAVEPOINT content_a1_volumes_v1")
    try:
        _ensure_structure_order_column(conn)

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
        conn.execute("RELEASE SAVEPOINT content_a1_volumes_v1")
    except Exception:
        conn.execute("ROLLBACK TO SAVEPOINT content_a1_volumes_v1")
        conn.execute("RELEASE SAVEPOINT content_a1_volumes_v1")
        raise

    return {"status": "ready", "migrated": True, "volumes": 9, "nodes": 33}
