-- Most Głębia-Ruch: jedna logiczna playlista, publikowana w Spotify i YouTube Music.
-- Aktywne tagi są zwykłym TEXT w playlist.playlist_tags.
-- Nie tworzymy kopii playlisty ani nie porównujemy różnic między serwisami.

UPDATE playlist
SET playlist_tags = 'owner:maciek-tora; most=glebia-ruch; spotify_url=https://open.spotify.com/playlist/42r40qtwg2mOoHDk5Akr9G; youtube_music_url=https://music.youtube.com/playlist?list=PLacFJ1WpA7YQ'
WHERE external_playlist_id = '42r40qtwg2mOoHDk5Akr9G'
   OR external_url = 'https://open.spotify.com/playlist/42r40qtwg2mOoHDk5Akr9G';
