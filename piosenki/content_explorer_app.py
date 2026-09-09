from __future__ import annotations

from flask import jsonify

from app import app, get_connection


def fetch_explorer_rows(conn, collection_id: str) -> list[dict]:
    rows = conn.execute(
        """
        WITH ordered_terms AS (
            SELECT
                sk.section_id,
                sk.keyword_order,
                kt.lang,
                kt.keyword
            FROM content_section_keywords sk
            JOIN content_keyword_terms kt
              ON kt.concept_id = sk.concept_id
             AND kt.is_preferred = 1
            ORDER BY sk.section_id, sk.keyword_order, kt.lang
        ),
        keywords AS (
            SELECT
                section_id,
                group_concat(CASE WHEN lang='pl' THEN keyword END, ' · ') AS keywords_pl,
                group_concat(CASE WHEN lang='en' THEN keyword END, ' · ') AS keywords_en
            FROM ordered_terms
            GROUP BY section_id
        ),
        keyword_counts AS (
            SELECT section_id, count(*) AS keyword_concepts
            FROM content_section_keywords
            GROUP BY section_id
        )
        SELECT
            d.collection_id,
            d.document_id,
            d.document_code,
            d.document_title,
            d.canonical_url,
            d.source_filename,
            d.source_url,
            d.sort_order AS document_sort_order,
            s.section_id,
            s.parent_section_id,
            s.section_kind,
            s.heading_level,
            s.depth,
            COALESCE(s.structure_order, s.section_order) AS structure_order,
            s.section_order AS source_order,
            s.section_title,
            COALESCE(s.section_title_en, ''),
            COALESCE(s.anchor, ''),
            CASE
                WHEN s.anchor IS NULL OR trim(s.anchor)='' THEN ''
                ELSE rtrim(d.canonical_url, '#') || '#' || s.anchor
            END AS deep_link,
            COALESCE(s.description, ''),
            COALESCE(s.description_en, ''),
            COALESCE(NULLIF(trim(k.keywords_pl), ''), NULLIF(trim(s.keywords_pl), ''), ''),
            COALESCE(NULLIF(trim(k.keywords_en), ''), NULLIF(trim(s.keywords_en), ''), ''),
            COALESCE(kc.keyword_concepts, 0),
            m.char_count,
            m.letter_count,
            m.word_count,
            CASE
                WHEN m.char_count IS NULL THEN NULL
                ELSE m.char_count / 1800.0
            END AS normalized_pages
        FROM content_sections s
        JOIN content_documents d ON d.document_id = s.document_id
        LEFT JOIN keywords k ON k.section_id = s.section_id
        LEFT JOIN keyword_counts kc ON kc.section_id = s.section_id
        LEFT JOIN content_section_metrics m ON m.section_id = s.section_id
        WHERE d.collection_id = ?
        ORDER BY
            d.sort_order,
            COALESCE(s.structure_order, s.section_order),
            s.section_id
        """,
        (collection_id,),
    ).fetchall()

    columns = [
        "collection_id",
        "document_id",
        "document_code",
        "document_title",
        "canonical_url",
        "source_filename",
        "source_url",
        "document_sort_order",
        "section_id",
        "parent_section_id",
        "section_kind",
        "heading_level",
        "depth",
        "structure_order",
        "source_order",
        "section_title",
        "section_title_en",
        "anchor",
        "deep_link",
        "description",
        "description_en",
        "keywords_pl",
        "keywords_en",
        "keyword_concepts",
        "char_count",
        "letter_count",
        "word_count",
        "normalized_pages",
    ]
    return [dict(zip(columns, row)) for row in rows]


def build_stats(rows: list[dict]) -> dict:
    headings = [row for row in rows if row["section_kind"] == "heading"]
    return {
        "documents": len({row["document_id"] for row in rows}),
        "sections": len(headings),
        "structure_nodes": len(rows),
        "anchors": sum(1 for row in headings if row["anchor"]),
        "translated_titles": sum(1 for row in headings if row["section_title_en"]),
        "translated_descriptions": sum(1 for row in headings if row["description_en"]),
        "keyworded_sections": sum(
            1
            for row in headings
            if row["keywords_pl"] or row["keywords_en"] or row["keyword_concepts"]
        ),
        "keyword_links": sum(int(row["keyword_concepts"] or 0) for row in headings),
    }


@app.get("/api/content/<collection_id>/explorer")
def api_content_explorer(collection_id):
    conn = None
    try:
        conn = get_connection()
        collection = conn.execute(
            "SELECT label FROM content_collections WHERE collection_id=?",
            (collection_id,),
        ).fetchone()
        if collection is None:
            return jsonify(status="not_found", collection_id=collection_id), 404

        rows = fetch_explorer_rows(conn, collection_id)
        return jsonify(
            status="ok",
            source="live Turso / content_*",
            collection_id=collection_id,
            label=collection[0],
            stats=build_stats(rows),
            rows=rows,
        ), 200
    except Exception as exc:
        return jsonify(status="error", error=str(exc)), 500
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
