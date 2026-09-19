-- tabela: playlist_tag_def
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS playlist_tag_def (
    tag TEXT PRIMARY KEY,
    description TEXT
);

INSERT INTO playlist_tag_def VALUES('owner:maciek-tora','Playlista należąca do Maćka Tory.');

