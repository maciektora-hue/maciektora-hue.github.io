-- SOL — playlist metadata / repeated exports
-- Jeden rekord playlist = jeden konkretny eksport/stAN playlisty w czasie.
-- playlist_series_id może łączyć kolejne eksporty tej samej logicznej playlisty.
-- Usuwamy UNIQUE(service, external_playlist_id), bo ta sama playlista może być eksportowana wielokrotnie.

PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;

CREATE TABLE playlist_new (
    playlist_id TEXT PRIMARY KEY,
    playlist_series_id TEXT,
    service TEXT NOT NULL,
    name TEXT NOT NULL,
    external_playlist_id TEXT,
    external_url TEXT,
    source_file TEXT,
    exported_at TEXT,
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tags TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(tags)),
    CHECK (service IN ('spotify', 'youtube_music', 'youtube'))
);

INSERT INTO playlist_new (
    playlist_id,
    playlist_series_id,
    service,
    name,
    external_playlist_id,
    external_url,
    source_file,
    exported_at,
    imported_at,
    tags
)
SELECT
    playlist_id,
    NULL,
    service,
    name,
    external_playlist_id,
    external_url,
    source_file,
    NULL,
    imported_at,
    '[]'
FROM playlist;

DROP TABLE playlist;
ALTER TABLE playlist_new RENAME TO playlist;

CREATE INDEX IF NOT EXISTS idx_playlist_series_id
    ON playlist(playlist_series_id);

CREATE INDEX IF NOT EXISTS idx_playlist_external_playlist_id
    ON playlist(service, external_playlist_id);

CREATE TABLE IF NOT EXISTS playlist_tag_def (
    tag TEXT PRIMARY KEY,
    description TEXT
);

COMMIT;
PRAGMA foreign_keys = ON;

-- Po migracji warto wykonać:
-- PRAGMA foreign_key_check;
-- SELECT COUNT(*) FROM playlist;
-- SELECT COUNT(*) FROM playlist_item;
