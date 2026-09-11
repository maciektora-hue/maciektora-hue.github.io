-- Plain-text playlist tags. Existing playlist.tags remains legacy for compatibility.
ALTER TABLE playlist ADD COLUMN playlist_tags TEXT NOT NULL DEFAULT '';

UPDATE playlist
SET playlist_tags = COALESCE(
    (SELECT group_concat(value, '; ') FROM json_each(playlist.tags)),
    ''
)
WHERE json_valid(playlist.tags);

UPDATE playlist
SET playlist_tags = 'owner:maciek-tora; wyspa=swiatla; spotify_url=https://open.spotify.com/playlist/272wzPwVUjxBmqJ8eNQsTW; youtube_music_url=https://music.youtube.com/playlist?list=PLdqONEJClykk'
WHERE playlist_id = 'spotify:wyspa-swiatla:2026-09-11';
