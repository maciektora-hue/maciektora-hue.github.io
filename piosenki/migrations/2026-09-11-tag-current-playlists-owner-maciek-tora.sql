-- SOL — owner tag dla wszystkich playlist obecnych w SQL 2026-09-11
-- Użytkownik potwierdził, że wszystkie obecnie załadowane playlisty są jego playlistami.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

INSERT OR IGNORE INTO playlist_tag_def(tag, description)
VALUES ('owner:maciek-tora', 'Playlista należąca do Maćka Tory.');

UPDATE playlist
SET tags = CASE
    WHEN EXISTS (
        SELECT 1 FROM json_each(playlist.tags)
        WHERE value = 'owner:maciek-tora'
    ) THEN tags
    ELSE json_insert(tags, '$[#]', 'owner:maciek-tora')
END;

COMMIT;
