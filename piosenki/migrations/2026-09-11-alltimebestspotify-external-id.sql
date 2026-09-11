-- SOL — identyfikator Spotify dla AllTimeBestSpotify
-- Potwierdzone przez link Spotify i screenshot aplikacji 2026-09-11.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

UPDATE playlist
SET external_playlist_id = '5wDt92D4lFaSDIuVrdKLF9',
    external_url = 'https://open.spotify.com/playlist/5wDt92D4lFaSDIuVrdKLF9'
WHERE playlist_id = 'spotify:alltimebest'
  AND service = 'spotify'
  AND name = 'AllTimeBestSpotify';

COMMIT;
