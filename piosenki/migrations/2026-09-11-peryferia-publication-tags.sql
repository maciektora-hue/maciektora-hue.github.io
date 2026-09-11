-- Peryferia: publikacje tej samej playlisty w Spotify i YouTube Music.
-- Aktywne tagi są zwykłym TEXT w playlist.playlist_tags.

UPDATE playlist
SET playlist_tags = 'owner:maciek-tora; wyspa=peryferia; spotify_url=https://open.spotify.com/playlist/4hPcWJRfNQjEef2Re2NRli; youtube_music_url=https://music.youtube.com/playlist?list=PLAFO32rZCzu4'
WHERE playlist_id = 'spotify:peryferia:2026-09-11';
