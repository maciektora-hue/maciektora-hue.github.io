-- LikedSongsWrzesien26: jedna logiczna playlista, publikowana w Spotify i YouTube Music.
-- Aktywne tagi są zwykłym TEXT w playlist.playlist_tags.
-- Nie tworzymy kopii playlisty ani nie porównujemy różnic między serwisami.

UPDATE playlist
SET playlist_tags = 'owner:maciek-tora; spotify_url=https://open.spotify.com/playlist/2YlZZSyoSy7Qv18czLiyS8; youtube_music_url=https://music.youtube.com/playlist?list=PLTg92mmd7R7U'
WHERE playlist_id = 'spotify:liked-songs:2026-09-11'
   OR external_playlist_id = '2YlZZSyoSy7Qv18czLiyS8'
   OR external_url = 'https://open.spotify.com/playlist/2YlZZSyoSy7Qv18czLiyS8';
