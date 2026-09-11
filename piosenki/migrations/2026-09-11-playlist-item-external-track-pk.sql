-- SOL — playlist_item -> external_track
-- Dodaje jawny FK do external_track i zasila go z obecnych (service, external_track_id).
-- Stare pola pozostają na razie bez zmian jako warstwa przejściowa/audytowa.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

ALTER TABLE playlist_item
ADD COLUMN external_track_pk INTEGER
    REFERENCES external_track(external_track_pk)
    ON UPDATE CASCADE
    ON DELETE RESTRICT;

UPDATE playlist_item AS i
SET external_track_pk = (
    SELECT e.external_track_pk
    FROM playlist AS p
    JOIN external_track AS e
      ON e.service = p.service
     AND e.external_track_id = i.external_track_id
    WHERE p.playlist_id = i.playlist_id
)
WHERE i.external_track_id IS NOT NULL
  AND trim(i.external_track_id) <> '';

CREATE INDEX IF NOT EXISTS idx_playlist_item_external_track_pk
    ON playlist_item(external_track_pk);

COMMIT;
