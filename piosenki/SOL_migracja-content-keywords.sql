-- SOL — migracja modelu słów kluczowych sekcji
-- Status: PRZYGOTOWANA, NIEURUCHOMIONA
-- Data: 2026-09-08
--
-- Zakres:
--   1. content_keyword_concepts
--   2. content_keyword_terms
--   3. content_section_keywords
--   4. indeksy
--
-- Bez INSERT/UPDATE/DELETE.
-- Bez zmian w content_sections.
-- Bez zmian danych ROSJA/AuDHD.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE content_keyword_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_key TEXT NOT NULL UNIQUE
);

CREATE TABLE content_keyword_terms (
    keyword_id INTEGER PRIMARY KEY,
    concept_id INTEGER NOT NULL,
    lang TEXT NOT NULL,
    keyword TEXT NOT NULL,
    keyword_norm TEXT NOT NULL,
    is_preferred INTEGER NOT NULL DEFAULT 1,

    FOREIGN KEY (concept_id)
        REFERENCES content_keyword_concepts(concept_id),

    CHECK (lang IN ('pl', 'en')),
    CHECK (is_preferred IN (0, 1)),

    UNIQUE (concept_id, lang, keyword_norm)
);

CREATE TABLE content_section_keywords (
    section_id INTEGER NOT NULL,
    concept_id INTEGER NOT NULL,
    keyword_order INTEGER NOT NULL,

    PRIMARY KEY (section_id, concept_id),

    FOREIGN KEY (section_id)
        REFERENCES content_sections(section_id),

    FOREIGN KEY (concept_id)
        REFERENCES content_keyword_concepts(concept_id),

    UNIQUE (section_id, keyword_order)
);

CREATE INDEX idx_keyword_terms_norm
ON content_keyword_terms(lang, keyword_norm);

CREATE INDEX idx_section_keywords_concept
ON content_section_keywords(concept_id);

CREATE INDEX idx_section_keywords_section
ON content_section_keywords(section_id);

COMMIT;
