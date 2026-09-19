-- tabela: content_collections
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS content_collections (
    collection_id TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    sort_order INTEGER NOT NULL UNIQUE,
    CHECK (length(trim(collection_id)) > 0),
    CHECK (length(trim(label)) > 0)
);

INSERT INTO content_collections VALUES('rosja','ROSJA',10);

INSERT INTO content_collections VALUES('audhd','AuDHD',20);

