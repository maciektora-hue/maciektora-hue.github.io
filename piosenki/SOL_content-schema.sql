-- SOL — wspolny model map tresci ROSJA / AuDHD
-- V1, 2026-09-07
-- Operacje addytywne. Bez DROP istniejacych tabel piosenek.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS content_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS content_collections (
    collection_id TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    sort_order INTEGER NOT NULL UNIQUE,
    CHECK (length(trim(collection_id)) > 0),
    CHECK (length(trim(label)) > 0)
);

CREATE TABLE IF NOT EXISTS content_documents (
    document_id INTEGER PRIMARY KEY,
    collection_id TEXT NOT NULL
        REFERENCES content_collections(collection_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    document_code TEXT NOT NULL,
    source_filename TEXT NOT NULL,
    document_title TEXT NOT NULL,
    canonical_url TEXT NOT NULL,
    source_url TEXT NOT NULL,
    sort_order INTEGER NOT NULL,
    UNIQUE (collection_id, document_code),
    UNIQUE (collection_id, source_filename),
    UNIQUE (collection_id, sort_order),
    CHECK (length(trim(document_code)) > 0),
    CHECK (length(trim(source_filename)) > 0),
    CHECK (length(trim(document_title)) > 0),
    CHECK (length(trim(canonical_url)) > 0),
    CHECK (length(trim(source_url)) > 0),
    CHECK (sort_order >= 1)
);

CREATE TABLE IF NOT EXISTS content_sections (
    section_id INTEGER PRIMARY KEY,
    document_id INTEGER NOT NULL
        REFERENCES content_documents(document_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    parent_section_id INTEGER
        REFERENCES content_sections(section_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL,
    section_kind TEXT NOT NULL DEFAULT 'heading',
    heading_level INTEGER,
    depth INTEGER NOT NULL,
    section_order INTEGER NOT NULL,
    section_title TEXT NOT NULL,
    anchor TEXT,
    description TEXT,
    UNIQUE (document_id, section_order),
    UNIQUE (document_id, anchor),
    CHECK (section_kind IN ('heading', 'volume', 'other')),
    CHECK (
        (section_kind = 'heading' AND heading_level BETWEEN 1 AND 6)
        OR
        (section_kind <> 'heading' AND heading_level IS NULL)
    ),
    CHECK (depth >= 1),
    CHECK (section_order >= 1),
    CHECK (length(trim(section_title)) > 0),
    CHECK (anchor IS NULL OR length(trim(anchor)) > 0)
);

CREATE INDEX IF NOT EXISTS idx_content_documents_collection_order
    ON content_documents(collection_id, sort_order);

CREATE INDEX IF NOT EXISTS idx_content_sections_document_order
    ON content_sections(document_id, section_order);

CREATE INDEX IF NOT EXISTS idx_content_sections_parent
    ON content_sections(parent_section_id);

CREATE VIEW IF NOT EXISTS v_content_structure AS
SELECT
    d.collection_id AS collection_id,
    d.document_code AS dokument_kod,
    d.source_filename AS dokument_plik,
    d.document_title AS dokument_tytul,
    d.canonical_url AS canonical_url,
    d.source_url AS source_url,
    s.section_kind AS section_kind,
    CASE
        WHEN s.section_kind = 'heading' THEN 'H' || CAST(s.heading_level AS TEXT)
        ELSE upper(s.section_kind)
    END AS poziom,
    s.depth AS glebokosc,
    s.section_order AS kolejnosc,
    s.section_title AS sekcja_tytul,
    COALESCE(s.anchor, '') AS anchor,
    CASE
        WHEN s.anchor IS NULL OR trim(s.anchor) = '' THEN 'BRAK'
        ELSE 'OK'
    END AS anchor_status,
    CASE
        WHEN s.anchor IS NULL OR trim(s.anchor) = '' THEN ''
        ELSE rtrim(d.canonical_url, '#') || '#' || s.anchor
    END AS deep_link,
    COALESCE(s.description, '') AS opis,
    s.parent_section_id AS parent_section_id,
    d.sort_order AS document_sort_order
FROM content_sections s
JOIN content_documents d
    ON d.document_id = s.document_id;

CREATE VIEW IF NOT EXISTS v_content_map AS
SELECT *
FROM v_content_structure
WHERE section_kind = 'heading';

CREATE VIEW IF NOT EXISTS v_content_human AS
SELECT
    collection_id,
    sekcja_tytul,
    anchor,
    anchor_status,
    deep_link,
    opis,
    dokument_tytul,
    canonical_url,
    dokument_kod,
    poziom,
    glebokosc,
    kolejnosc,
    dokument_plik,
    source_url,
    document_sort_order
FROM v_content_map;

CREATE VIEW IF NOT EXISTS v_rosja_mapa_sekcji AS
SELECT
    dokument_kod,
    dokument_plik,
    dokument_tytul,
    canonical_url AS url_stabilny,
    poziom,
    glebokosc,
    kolejnosc,
    sekcja_tytul,
    anchor,
    anchor_status,
    deep_link,
    opis
FROM v_content_map
WHERE collection_id = 'rosja'
ORDER BY document_sort_order, kolejnosc;

CREATE VIEW IF NOT EXISTS v_audhd_mapa_sekcji AS
SELECT
    dokument_kod,
    dokument_plik,
    dokument_tytul,
    source_url AS url_zrodlowy,
    poziom,
    glebokosc,
    kolejnosc,
    sekcja_tytul,
    anchor,
    anchor_status,
    deep_link
FROM v_content_map
WHERE collection_id = 'audhd'
ORDER BY document_sort_order, kolejnosc;

CREATE VIEW IF NOT EXISTS v_content_status AS
SELECT
    d.collection_id AS collection_id,
    count(DISTINCT d.document_id) AS documents,
    count(s.section_id) AS sections,
    sum(CASE WHEN s.anchor IS NOT NULL AND trim(s.anchor) <> '' THEN 1 ELSE 0 END) AS anchors_ok,
    sum(CASE WHEN s.anchor IS NULL OR trim(s.anchor) = '' THEN 1 ELSE 0 END) AS anchors_missing,
    sum(CASE WHEN s.description IS NOT NULL AND trim(s.description) <> '' THEN 1 ELSE 0 END) AS descriptions_present,
    sum(CASE WHEN s.description IS NULL OR trim(s.description) = '' THEN 1 ELSE 0 END) AS descriptions_missing
FROM content_documents d
LEFT JOIN content_sections s
    ON s.document_id = d.document_id
GROUP BY d.collection_id;
