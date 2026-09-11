-- SOL — zasilenie external_track_utwu z obecnych rozstrzygniętych mapowań playlist
-- Zero heurystyk: używamy wyłącznie istniejącego playlist_item.utwu_id.
-- Ten sam external_track może mieć więcej niż jedno jawne utwu_id.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

INSERT OR IGNORE INTO external_track_utwu (
    external_track_pk,
    utwu_id
)
SELECT DISTINCT
    e.external_track_pk,
    i.utwu_id
FROM playlist_item AS i
JOIN playlist AS p
    ON p.playlist_id = i.playlist_id
JOIN external_track AS e
    ON e.service = p.service
   AND e.external_track_id = i.external_track_id
WHERE i.utwu_id IS NOT NULL
  AND i.external_track_id IS NOT NULL
  AND trim(i.external_track_id) <> '';

COMMIT;
