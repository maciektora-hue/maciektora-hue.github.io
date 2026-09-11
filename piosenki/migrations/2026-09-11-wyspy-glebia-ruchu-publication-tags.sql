-- Publikacje tej samej logicznej playlisty w różnych serwisach.
-- Zawartość playlisty pozostaje pojedyncza w SQL; tutaj zapisujemy tylko adresy publikacji.

UPDATE playlist
SET playlist_tags = 'owner:maciek-tora; wyspa=glebi; spotify_url=https://open.spotify.com/playlist/2XlvqJZUNVjR4KGIpF39nG; youtube_music_url=https://music.youtube.com/playlist?list=PLUK_LdKYWxTk'
WHERE playlist_id = 'spotify:wyspa-glebi:2026-09-11';

UPDATE playlist
SET playlist_tags = 'owner:maciek-tora; wyspa=ruchu; spotify_url=https://open.spotify.com/playlist/3KEDfDtvGvwWyZINTWm37i; youtube_music_url=https://music.youtube.com/playlist?list=PLeop-pmwxm1w'
WHERE playlist_id = 'spotify:wyspa-ruchu:2026-09-11';
