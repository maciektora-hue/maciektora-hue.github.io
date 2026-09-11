-- SOL — zasilenie external_track z obecnych pozycji playlist
-- Nie rusza playlist_item ani middle_end.
-- Dla jednego (service, external_track_id) wybiera pierwsze wystąpienie
-- w porządku playlist_id, position. Dane źródłowe w playlist_item pozostają bez zmian.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

WITH ranked AS (
    SELECT
        p.service AS service,
        i.external_track_id AS external_track_id,
        i.source_name AS title,
        i.source_artist AS artist,
        i.source_album AS album,
        ROW_NUMBER() OVER (
            PARTITION BY p.service, i.external_track_id
            ORDER BY i.playlist_id, i.position
        ) AS rn
    FROM playlist_item AS i
    JOIN playlist AS p ON p.playlist_id = i.playlist_id
    WHERE i.external_track_id IS NOT NULL
      AND trim(i.external_track_id) <> ''
)
INSERT OR IGNORE INTO external_track (
    service,
    external_track_id,
    title,
    artist,
    album
)
SELECT
    service,
    external_track_id,
    title,
    artist,
    album
FROM ranked
WHERE rn = 1;

COMMIT;
