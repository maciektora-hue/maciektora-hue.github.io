-- SOL — external_track, krok 1 normalizacji playlist
-- Jeden rekord = jeden utwór zewnętrznego serwisu, niezależnie od liczby playlist.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS external_track (
    external_track_pk INTEGER PRIMARY KEY,
    service TEXT NOT NULL,
    external_track_id TEXT NOT NULL,
    title TEXT,
    artist TEXT,
    album TEXT,
    CHECK (service IN ('spotify', 'youtube_music', 'youtube')),
    UNIQUE (service, external_track_id)
);

COMMIT;
