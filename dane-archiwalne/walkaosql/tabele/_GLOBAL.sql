PRAGMA foreign_keys=OFF;

BEGIN TRANSACTION;

CREATE VIEW v_content_structure AS SELECT d.collection_id AS collection_id, d.document_code AS dokument_kod, d.source_filename AS dokument_plik, d.document_title AS dokument_tytul, d.canonical_url AS canonical_url, d.source_url AS source_url, s.section_kind AS section_kind, CASE WHEN s.section_kind = 'heading' THEN 'H' || CAST (s.heading_level AS TEXT) ELSE upper (s.section_kind) END AS poziom, s.depth AS glebokosc, s.section_order AS kolejnosc, s.section_title AS sekcja_tytul, COALESCE (s.anchor, '') AS anchor, CASE WHEN s.anchor IS NULL OR trim (s.anchor) = '' THEN 'BRAK' ELSE 'OK' END AS anchor_status, CASE WHEN s.anchor IS NULL OR trim (s.anchor) = '' THEN '' ELSE rtrim (d.canonical_url, '#') || '#' || s.anchor END AS deep_link, COALESCE (s.description, '') AS opis, s.parent_section_id AS parent_section_id, d.sort_order AS document_sort_order FROM content_sections s JOIN content_documents d ON d.document_id = s.document_id;

CREATE VIEW v_content_map AS SELECT * FROM v_content_structure WHERE section_kind = 'heading';

CREATE VIEW v_content_human AS SELECT collection_id, sekcja_tytul, anchor, anchor_status, deep_link, opis, dokument_tytul, canonical_url, dokument_kod, poziom, glebokosc, kolejnosc, dokument_plik, source_url, document_sort_order FROM v_content_map;

CREATE VIEW v_rosja_mapa_sekcji AS SELECT dokument_kod, dokument_plik, dokument_tytul, canonical_url AS url_stabilny, poziom, glebokosc, kolejnosc, sekcja_tytul, anchor, anchor_status, deep_link, opis FROM v_content_map WHERE collection_id = 'rosja' ORDER BY document_sort_order, kolejnosc;

CREATE VIEW v_audhd_mapa_sekcji AS SELECT dokument_kod, dokument_plik, dokument_tytul, source_url AS url_zrodlowy, poziom, glebokosc, kolejnosc, sekcja_tytul, anchor, anchor_status, deep_link FROM v_content_map WHERE collection_id = 'audhd' ORDER BY document_sort_order, kolejnosc;

CREATE VIEW v_content_status AS SELECT d.collection_id AS collection_id, count (DISTINCT d.document_id) AS documents, count (s.section_id) AS sections, sum (CASE WHEN s.anchor IS NOT NULL AND trim (s.anchor) <> '' THEN 1 ELSE 0 END) AS anchors_ok, sum (CASE WHEN s.anchor IS NULL OR trim (s.anchor) = '' THEN 1 ELSE 0 END) AS anchors_missing, sum (CASE WHEN s.description IS NOT NULL AND trim (s.description) <> '' THEN 1 ELSE 0 END) AS descriptions_present, sum (CASE WHEN s.description IS NULL OR trim (s.description) = '' THEN 1 ELSE 0 END) AS descriptions_missing FROM content_documents d LEFT JOIN content_sections s ON s.document_id = d.document_id GROUP BY d.collection_id;

COMMIT;
