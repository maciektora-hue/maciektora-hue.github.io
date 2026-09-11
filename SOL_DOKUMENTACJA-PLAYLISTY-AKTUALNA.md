# SOL — DOKUMENTACJA PLAYLIST — AKTUALNA

Status: AKTUALNY STAN WARSTWY PLAYLIST
Data: 2026-09-11
Źródło prawdy dla stanu bieżącego: live Turso + aktualny kod repozytorium

## 1. Cel

Ta dokumentacja opisuje aktualną warstwę playlist w projekcie `piosenki`: model SQL, mapowanie do kanonicznego `middle_end`, importer, publiczny viewer oraz stan danych po imporcie testowym Liked Songs z 2026-09-11.

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

Metadane są reprezentatywne i zachowywane niedestrukcyjnie: importer może uzupełnić puste pole, ale nie nadpisuje po cichu istniejącego tytułu / artysty / albumu inną wartością z kolejnego eksportu.

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

## 7. Właściciel obecnych playlist

Wszystkie 10 playlist obecnie załadowanych do SQL są playlistami Maćka Tory i mają tag:

```text
owner:maciek-tora
```

Tag znajduje się w `playlist.tags`, a jego definicja w `playlist_tag_def`.

To opis obecnego zbioru, nie globalna reguła dla każdej przyszłej playlisty.

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

W trybie **utwór → playlisty** nie trzeba już wybierać utworu z pełnej, długiej listy. Viewer ma lokalne wyszukiwanie po:

- tytule;
- artyście;
- `utwu_id`.

Wyniki zawężają się podczas pisania. Jest też filtr:

```text
tylko utwory występujące na więcej niż jednej playliście
```

Przy każdym wyniku viewer pokazuje liczbę playlist, na których dany kanoniczny utwór występuje. Po wybraniu utworu podsumowanie pokazuje liczbę różnych playlist, liczbę zapisanych pozycji oraz liczbę zewnętrznych identyfikatorów prowadzących do tego `utwu_id`.

Wyszukiwanie i filtr są zaimplementowane po stronie statycznego frontendu w JavaScript i działają na danych już pobranych z `GET /api/playlisty`. Nie wymagają dodatkowego endpointu ani zapisu do SQL.

Dla playlist z `external_url` viewer pokazuje klikalny link do serwisu zewnętrznego. Pokazuje też `playlist.tags`.

Liked Songs pojawia się automatycznie z SQL jako nowy snapshot, ale bez przycisku Spotify, ponieważ `external_url` jest `NULL`.

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

Nie wykonuje heurystycznego mapowania i nie modyfikuje SQL.

Wyszukiwanie utworów i filtr „więcej niż jedna playlista” są obecnie funkcją viewera, nie API.

## 11. Zasady mapowania

Nie tworzymy sztucznych rekordów `middle_end` tylko dlatego, że utwór pojawił się na zewnętrznej playliście.

Automatyczne mapowanie jest dopuszczalne tylko wtedy, gdy zewnętrzny identyfikator daje dokładnie jedno istniejące `utwu_id`.

Jeżeli dopasowanie jest zerowe lub niejednoznaczne, `external_track` pozostaje bez rekordu w `external_track_utwu`.

Bez jawnego polecenia nie stosujemy heurystyk tytuł/artysta/album.

## 12. Importer

Importer zgodny ze znormalizowanym modelem istnieje w:

```text
piosenki/playlist_importer.py
```

Czyta XLSX z kolumnami:

```text
id | name | artist | album
```

i wykonuje:

- utworzenie rekordu `playlist` dla snapshotu;
- deduplikację po `(service, external_track_id)`;
- dodanie nowych `external_track`;
- niedestrukcyjne traktowanie metadanych;
- utworzenie `playlist_item` przez `external_track_pk`;
- dokładne mapowanie provider-ID → `middle_end` tylko dla jednego kandydata;
- zapis jawnych relacji do `external_track_utwu`;
- tryb `dry_run`.

### Znane ograniczenie operacyjne

Pierwszy import 942 pozycji ujawnił problem wydajnościowy: obecna implementacja wykonuje dużo kolejnych operacji na Turso. Podczas importu publiczne API zostało chwilowo przyblokowane, wystąpił timeout workera Gunicorna i jedno zewnętrzne zapytanie dostało HTTP 502. Sam import zakończył się poprawnie i transakcja została zatwierdzona.

Wniosek: **logika importera jest poprawna, ale przed regularnymi dużymi importami należy zbatchować zapytania / skrócić transakcję.** Nie uruchamiać dużego importu synchronicznie w ścieżce startowej Gunicorna.

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

To oznacza, że względem obecnego Liked Songs brakuje pokrycia tagami dla 73 pozycji: 68 jest już kanonicznie rozpoznanych, ale nie ma przypiętego `lyrics_id` / tagów, a 5 nie ma jeszcze nawet mapowania do `utwu_id`.

Pięć nierozstrzygniętych pozycji:

```text
1   Wichita Vortex Sutra — Philip Glass
2   Nieprzysiadalność — Swietliki
3   Filandia — Swietliki
154 Ja pas! — Nosowska
201 Miłość Miłość — Krzysztof Zalewski
```

To są fakty z live API po imporcie, nie heurystyczna lista kandydatów.

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
- `2026-09-11-tag-current-playlists-owner-maciek-tora.sql`.

Import Liked Songs był wykonany przez `playlist_importer.py`; nie jest migracją schematu.

## 15. Najkrótsza wersja dla kolejnych czatów

```text
playlist = konkretny eksport / snapshot playlisty
playlist_item = pozycja w tym eksporcie
external_track = jeden utwór zewnętrznego serwisu, deduplikowany po service + ID
external_track_utwu = tylko jawne, rozstrzygnięte mapowania do middle_end
middle_end = kanoniczne utwory projektu
playlist_importer.py = importer XLSX do powyższego modelu
playlisty*.html = viewer z wyszukiwaniem title/artist/utwu_id i filtrem >1 playlista
```

Nie cofaj modelu do kopiowania title/artist/album na każdej pozycji playlisty. Nie twórz `middle_end` dla nierozpoznanych utworów tylko po to, żeby zapełnić FK. Nie mapuj po tytule / artyście / albumie bez jawnej decyzji.
