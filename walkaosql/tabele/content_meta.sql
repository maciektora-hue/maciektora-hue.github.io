-- tabela: content_meta
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS content_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

INSERT INTO content_meta VALUES('content_initial_import_v1','done');

INSERT INTO content_meta VALUES('content_initial_import_v1_utc','2026-09-07T13:01:30.717249+00:00');

INSERT INTO content_meta VALUES('content_keywords_schema_v1','done');

INSERT INTO content_meta VALUES('content_keywords_data_v1','done');

