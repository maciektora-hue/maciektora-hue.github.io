# SOL — DOKUMENTACJA PLAYLIST — AKTUALNA

Status: AKTUALNY MODEL WARSTWY PLAYLIST
Data: 2026-09-12
Źródło prawdy dla zasad działania: ten dokument + live Turso + aktualny kod repozytorium

## 1. Cel

Ta dokumentacja opisuje aktualną warstwę playlist w projekcie `piosenki`: model SQL, mapowanie do kanonicznego `middle_end`, zasady tagów playlist, publiczny viewer oraz stan danych po imporcie testowym Liked Songs z 2026-09-11.

Migracje i pliki XLSX są historią / źródłem importu. Po imporcie stan bieżący należy czytać z live Turso.

## 2. Model SQL

Warstwa playlist składa się z pięciu istotnych elementów:

- `playlist` — jeden konkretny eksport / stan playlisty;
- `playlist_item` — pozycja na konkretnym eksporcie playlisty;
- `playlist_tag_def` — słownik tagów playlist;
- `external_track` — jeden rekord dla jednego identyfikatora utworu w zewnętrznym serwisie;
- `external_track_utwu` — jawne, rozstrzygnięte powiązanie `external_track` z kanonicznym `middle_end.utwu_id`.

```text
playlist
  ↓
playlist_item
  ↓ external_track_pk
external_track
  ↓
external_track_utwu
  ↓ utwu_id
middle_end
```

## 3. `external_track`

Kluczowa zasada:

```text
UNIQUE(service, external_track_id)
```

Ten sam Spotify ID występujący na wielu playlistach istnieje w SQL tylko raz.

Pola obejmują m.in. `external_track_pk`, `service`, `external_track_id`, `title`, `artist`, `album`.

Metadane są reprezentatywne i zachowywane niedestrukcyjnie: import może uzupełnić puste pole, ale nie nadpisuje po cichu istniejącego tytułu / artysty / albumu inną wartością z kolejnego eksportu.

Nie należy utożsamiać `external_track_id` z naszym `utwu_id`.

## 4. `external_track_utwu`

Tabela przechowuje tylko jawne, rozstrzygnięte relacje:

```text
(external_track_pk, utwu_id)
```

Interpretacja:

- brak rekordu = brak rozstrzygniętego mapowania;
- jeden rekord = jedno znane mapowanie;
- kilka rekordów jest dozwolonych, jeśli jeden zewnętrzny identyfikator rzeczywiście odpowiada kilku kanonicznym `utwu_id`.

Nie zapisujemy tutaj heurystycznych kandydatów.

## 5. `playlist_item`

Każda pozycja playlisty ma `external_track_pk` wskazujący na `external_track`.

Stare pola `utwu_id`, `external_track_id`, `source_name`, `source_artist`, `source_album` nadal istnieją przejściowo dla zgodności i audytu. Publiczny viewer/API nie opiera już logiki na tych polach.

Nie należy ich usuwać bez osobnej, jawnej migracji cleanupowej.

## 6. Aktualny stan live

Zweryfikowany przez publiczne API po imporcie Liked Songs:

- 10 playlist;
- 1861 pozycji `playlist_item`;
- 1033 różne `external_track` używane przez playlisty;
- 937 rekordów `external_track_utwu`.

Dziesiątą playlistą jest snapshot:

```text
playlist_id = spotify:liked-songs:2026-09-11
playlist_series_id = spotify:liked-songs
name = Liked Songs
service = spotify
exported_at = 2026-09-11
source_file = Liked songs spotify z dnia 2026-09-11.xlsx
```

Liked Songs nie ma `external_playlist_id` ani `external_url`, ponieważ nie jest zwykłą publicznie udostępnianą playlistą Spotify.

## 7. Tagi playlist — obowiązujący model

Jedynym aktywnym polem tagów playlist jest:

```text
playlist.playlist_tags
```

Format:

```text
TEXT
```

Tagi są zapisane jako zwykły tekst rozdzielany średnikami, np.:

```text
owner:maciek-tora; wyspa=glebi; spotify_url=https://open.spotify.com/playlist/...; youtube_music_url=https://music.youtube.com/playlist?list=...
```

Zasady:

- `playlist_tags` jest jedynym polem do zapisu i odczytu tagów playlist;
- nie używamy JSON do tagów playlist;
- nie tworzymy drugiego równoległego pola tagów;
- nazwa `playlist_tags` pozostaje nazwą kolumny SQL;
- adresy publikacji Spotify / YouTube Music / YouTube są tagami w `playlist_tags`;
- `playlist_tag_def` może służyć jako słownik znaczeń tagów, ale nie przechowuje przypisania tagów do konkretnej playlisty.

Stara kolumna:

```text
playlist.tags
```

jest legacy i nie należy jej używać. Nie wolno do niej zapisywać, czytać z niej jako fallbacku ani przywracać jej do logiki importu lub API. Jeżeli fizycznie jeszcze występuje w konkretnej wersji schematu, jest wyłącznie pozostałością do usunięcia, a nie elementem modelu danych.

## 8. AllTimeBestSpotify

```text
playlist_id = spotify:alltimebest
name = AllTimeBestSpotify
service = spotify
external_playlist_id = 5wDt92D4lFaSDIuVrdKLF9
external_url = https://open.spotify.com/playlist/5wDt92D4lFaSDIuVrdKLF9
```

Identyfikacja została potwierdzona linkiem Spotify i screenshotem aplikacji.

## 9. Publiczny viewer

Polski viewer:

```text
piosenki/playlisty.html
```

Angielski viewer:

```text
piosenki/playlisty-en.html
```

Obie wersje mają tę samą funkcjonalność i są podlinkowane z `piosenki` oraz `techniczne`.

Viewer ma trzy tryby:

1. playlista → utwory;
2. utwór (`utwu_id`) → playlisty;
3. pozycje bez rozstrzygniętego `utwu_id`.

W trybie **utwór → playlisty** viewer ma lokalne wyszukiwanie po tytule, artyście i `utwu_id` oraz filtr utworów występujących na więcej niż jednej playliście.

Viewer czyta publikacje z tagów `spotify_url=...`, `youtube_music_url=...` i `youtube_url=...` zapisanych w `playlist.playlist_tags` i pokazuje osobny klikalny przycisk dla każdego istniejącego adresu. Może więc pokazać Spotify, YouTube Music, oba albo żaden. Dla starszych rekordów może nadal istnieć `playlist.external_url`, ale nie jest to pole tagów.

## 10. API

Publiczny read-only endpoint:

```text
GET /api/playlisty
```

Kod:

```text
piosenki/playlist_api.py
```

API odczytuje metadane `playlist`, pozycje przez `playlist_item → external_track`, jawne mapowania `external_track_utwu` oraz dane kanonicznych utworów z `middle_end`.

Źródłem tagów playlist dla API ma być wyłącznie:

```text
playlist.playlist_tags
```

Dla zgodności z istniejącym viewerem wartość może być wystawiana w JSON pod kluczem `tags`, ale ten klucz jest tylko nazwą pola odpowiedzi API. Nie oznacza kolumny SQL `playlist.tags` i nie może być fallbackiem do starej kolumny.

API nie wykonuje heurystycznego mapowania i nie modyfikuje SQL.

## 11. Zasady mapowania

Nie tworzymy sztucznych rekordów `middle_end` tylko dlatego, że utwór pojawił się na zewnętrznej playliście.

Automatyczne mapowanie jest dopuszczalne tylko wtedy, gdy zewnętrzny identyfikator daje dokładnie jedno istniejące `utwu_id`.

Jeżeli dopasowanie jest zerowe lub niejednoznaczne, `external_track` pozostaje bez rekordu w `external_track_utwu`.

Bez jawnego polecenia nie stosujemy heurystyk tytuł/artysta/album.

## 12. Import playlist

W repozytorium nie ma obecnie aktywnego, zatwierdzonego importera playlist w Pythonie.

Wcześniejsze importery zostały uznane za wadliwe i usunięte. Nie wolno odtwarzać ich z historii GitHub ani używać zapamiętanej wcześniejszej wersji bez osobnej, wyraźnej zgody użytkownika.

Każdy przyszły import musi zachować model:

```text
playlist → playlist_item → external_track → external_track_utwu → middle_end
```

oraz bezwzględnie:

- nie tworzyć `middle_end` dla nierozpoznanego utworu;
- mapować automatycznie tylko po dokładnym ID serwisu;
- zapisywać tagi wyłącznie do `playlist.playlist_tags`;
- nigdy nie zapisywać do legacy `playlist.tags`;
- pozostawiać nierozpoznane zewnętrzne utwory jako `external_track` bez wymuszonego mapowania.

Szczegółowe reguły zgody na użycie importerów są w:

```text
piosenki/SOL_PLAYLISTY-IMPORTERY-ZAKAZ-UZYCIA.md
```

## 13. Pierwszy test bojowy: Liked Songs 2026-09-11

Plik zawiera 942 pozycje i 942 różne Spotify ID.

Potwierdzony wynik importu:

- 545 `external_track` już istniało;
- 397 dodano jako nowe;
- 543 mapowania `external_track_utwu` już istniały;
- 394 nowe mapowania dodano;
- 937 / 942 pozycji ma rozstrzygnięte `utwu_id`;
- 5 / 942 pozostaje nierozstrzygniętych;
- 0 przypadków niejednoznacznych;
- 0 konfliktów mapowania bridge ↔ `middle_end`;
- 869 / 942 pozycji ma `lyrics_id`;
- 869 / 942 ma snapshot tagów;
- wykryto 33 różnice pól metadanych dla już znanych Spotify ID; istniejących metadanych nie nadpisano.

Pięć nierozstrzygniętych pozycji:

```text
1   Wichita Vortex Sutra — Philip Glass
2   Nieprzysiadalność — Swietliki
3   Filandia — Swietliki
154 Ja pas! — Nosowska
201 Miłość Miłość — Krzysztof Zalewski
```

## 14. Migracje i historia

Istotne migracje historii playlist obejmują m.in.:

- `2026-09-10-playlists-spotify-bestof.sql`;
- `2026-09-11-playlist-metadata.sql`;
- `2026-09-11-external-track.sql`;
- `2026-09-11-external-track-utwu.sql`;
- `2026-09-11-populate-external-track.sql`;
- `2026-09-11-populate-external-track-utwu.sql`;
- `2026-09-11-playlist-item-external-track-pk.sql`;
- `2026-09-11-alltimebestspotify-external-id.sql`;
- `2026-09-11-tag-current-playlists-owner-maciek-tora.sql`;
- `piosenki/migrations/2026-09-11-playlist-plain-tags.sql`.

Pliki migracji opisują historię zmian. Nie wolno na ich podstawie przywracać legacy `playlist.tags` do bieżącego modelu.

## 15. Najkrótsza wersja dla kolejnych czatów

```text
playlist = jeden zapis treści playlisty
playlist_item = zawartość playlisty, bez kopiowania jej dla każdego serwisu
playlist.playlist_tags = JEDYNE aktywne tagi playlist; TEXT rozdzielany średnikami
playlist.tags = LEGACY; nie czytać, nie zapisywać, nie używać jako fallbacku
external_track = jeden utwór zewnętrznego serwisu, deduplikowany po service + ID
external_track_utwu = tylko jawne, rozstrzygnięte mapowania do middle_end
middle_end = kanoniczne utwory projektu
```

Nie cofaj modelu do kopiowania title/artist/album na każdej pozycji playlisty. Nie twórz `middle_end` dla nierozpoznanych utworów tylko po to, żeby zapełnić FK. Nie mapuj po tytule / artyście / albumie bez jawnej decyzji. Nie przywracaj starego systemu tagów JSON.

## 16. Publikacje tej samej playlisty w różnych serwisach

Dla playlist tworzonych przez nas SQL przechowuje zawartość **jeden raz**. Spotify, YouTube Music i ewentualne kolejne serwisy są publikacjami tej samej, mniej więcej zgodnej playlisty, a nie kolejnymi kopiami `playlist_item`.

Adresy publikacji zapisujemy w `playlist.playlist_tags` jako zwykłe tagi tekstowe:

```text
spotify_url=https://open.spotify.com/playlist/...
youtube_music_url=https://music.youtube.com/playlist?list=...
youtube_url=https://www.youtube.com/playlist?list=...
```

Nie sprawdzamy ani nie przechowujemy różnic typu „na YouTube brakuje trzech utworów”. Transfer może być nieidealny i jest to cecha publikacji zewnętrznej, nie osobna wersja treści w SQL.

Dla **Wyspy Światła** aktywny zapis jest:

```text
owner:maciek-tora; wyspa=swiatla; spotify_url=https://open.spotify.com/playlist/272wzPwVUjxBmqJ8eNQsTW; youtube_music_url=https://music.youtube.com/playlist?list=PLdqONEJClykk
```

Viewer interpretuje nazwy tagów URL, więc wie, który adres jest Spotify, który YouTube Music, i wyświetla odpowiednie przyciski. URL-e nie są pokazywane jako zwykłe tagi tekstowe.
