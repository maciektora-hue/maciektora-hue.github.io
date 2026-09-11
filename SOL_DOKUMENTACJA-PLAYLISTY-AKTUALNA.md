# SOL — DOKUMENTACJA PLAYLIST — AKTUALNA

Status: AKTUALNY STAN WARSTWY PLAYLIST
Data: 2026-09-11
Źródło prawdy dla stanu bieżącego: live Turso + aktualny kod repozytorium

## 1. Cel

Ta dokumentacja opisuje aktualną warstwę playlist w projekcie `piosenki`: model SQL, mapowanie do kanonicznego `middle_end`, publiczny viewer oraz stan danych po migracjach z 2026-09-11.

Migracje w `piosenki/migrations/` są historią zmian. Po wykonaniu migracji stan bieżący należy czytać z live Turso, nie rekonstruować ze starych XLSX/CSV.

## 2. Model SQL

Warstwa playlist składa się obecnie z pięciu istotnych elementów:

- `playlist` — jeden konkretny eksport / stan playlisty;
- `playlist_item` — pozycja na konkretnym eksporcie playlisty;
- `playlist_tag_def` — słownik tagów playlist;
- `external_track` — jeden rekord dla jednego identyfikatora utworu w zewnętrznym serwisie;
- `external_track_utwu` — jawne, rozstrzygnięte powiązanie `external_track` z kanonicznym `middle_end.utwu_id`.

Docelowy przepływ od playlisty do kanonicznego utworu wygląda tak:

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

`external_track` normalizuje dane zewnętrznych serwisów.

Kluczowa zasada:

```text
UNIQUE(service, external_track_id)
```

Ten sam Spotify ID występujący na wielu playlistach istnieje więc w SQL tylko raz.

Pola obejmują:

- `external_track_pk` — techniczny PK;
- `service`;
- `external_track_id`;
- `title`;
- `artist`;
- `album`.

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

Każda pozycja playlisty ma już `external_track_pk` wskazujący na `external_track`.

Stare pola zduplikowanych metadanych (`external_track_id`, `source_name`, `source_artist`, `source_album`, a także stare `utwu_id`) nadal istnieją przejściowo dla zgodności i audytu. Publiczny viewer/API nie opiera już logiki na tych polach.

Nie należy ich usuwać bez osobnej, jawnej migracji cleanupowej.

## 6. Aktualny stan danych

Stan po migracji:

- 9 playlist;
- 919 pozycji `playlist_item`;
- 636 różnych `external_track`;
- 543 rozstrzygnięte relacje `external_track ↔ utwu_id`;
- 824 pozycje playlist mają rozstrzygnięte `utwu_id` przez nową warstwę;
- 95 pozycji pozostaje bez `utwu_id`;
- te 95 pozycji reprezentuje 93 różne `external_track`.

Różnica 95 pozycji vs 93 różne zewnętrzne utwory wynika z powtórzeń tych samych zewnętrznych utworów na więcej niż jednej pozycji/playlistach.

## 7. Właściciel obecnych playlist

Wszystkie 9 playlist obecnie załadowanych do SQL są playlistami Maćka Tory.

Jest to zapisane jako tag:

```text
owner:maciek-tora
```

Tag znajduje się w `playlist.tags`, a jego definicja w `playlist_tag_def`.

Ta informacja opisuje stan obecnych 9 playlist. Nie jest globalnym założeniem, że każda przyszła importowana playlista musi należeć do Maćka.

## 8. AllTimeBestSpotify

Playlista:

```text
playlist_id = spotify:alltimebest
name = AllTimeBestSpotify
service = spotify
```

ma potwierdzony zewnętrzny identyfikator Spotify:

```text
external_playlist_id = 5wDt92D4lFaSDIuVrdKLF9
```

oraz URL:

```text
https://open.spotify.com/playlist/5wDt92D4lFaSDIuVrdKLF9
```

Identyfikacja została potwierdzona linkiem Spotify oraz screenshotem aplikacji, na którym widoczna była nazwa `AllTimeBestSpotify`, właściciel `Maciek Tora` i początek kolejności utworów zgodny z zapisanym eksportem.

## 9. Publiczny viewer

Polski viewer:

```text
piosenki/playlisty.html
```

Angielski viewer:

```text
piosenki/playlisty-en.html
```

Viewer jest podlinkowany z:

- `piosenki/index.html` / `piosenki/index-en.html`;
- `techniczne/index.html` / `techniczne/index-en.html`.

Viewer ma trzy tryby:

1. playlista → utwory;
2. utwór (`utwu_id`) → playlisty;
3. pozycje bez rozstrzygniętego `utwu_id`.

Dla playlist z `external_url` pokazuje klikalny przycisk do serwisu zewnętrznego. Dla `AllTimeBestSpotify` jest to bezpośredni link do Spotify.

Viewer pokazuje też `playlist.tags`, w tym `owner:maciek-tora` jako czytelną etykietę właściciela.

## 10. API

Publiczny read-only endpoint:

```text
GET /api/playlisty
```

Kod:

```text
piosenki/playlist_api.py
```

API odczytuje:

- metadane `playlist`;
- pozycje przez `playlist_item → external_track`;
- jawne mapowania z `external_track_utwu`;
- dane kanonicznych utworów z `middle_end`.

Nie wykonuje heurystycznego mapowania i nie modyfikuje SQL.

## 11. Zasady mapowania

Nie tworzymy sztucznych rekordów `middle_end` tylko dlatego, że utwór pojawił się na zewnętrznej playliście.

Automatyczne mapowanie jest dopuszczalne tylko wtedy, gdy zewnętrzny identyfikator daje jednoznaczne istniejące `utwu_id`.

Jeżeli dopasowanie jest zerowe lub niejednoznaczne, `external_track` pozostaje bez rekordu w `external_track_utwu`.

Bez jawnego polecenia nie stosujemy heurystyk tytuł/artysta/album.

## 12. Importer

Nowy importer zgodny z modelem `external_track` nie został jeszcze przygotowany. To jest celowo odłożone.

Nie należy więc opisywać importera jako gotowej części obecnego systemu.

## 13. Migracje

Istotne migracje historii playlist obejmują:

- `2026-09-10-playlists-spotify-bestof.sql`;
- `2026-09-11-playlist-metadata.sql`;
- `2026-09-11-external-track.sql`;
- `2026-09-11-external-track-utwu.sql`;
- `2026-09-11-populate-external-track.sql`;
- `2026-09-11-populate-external-track-utwu.sql`;
- `2026-09-11-playlist-item-external-track-pk.sql`;
- `2026-09-11-alltimebestspotify-external-id.sql`;
- `2026-09-11-tag-current-playlists-owner-maciek-tora.sql`.

## 14. Najkrótsza wersja dla kolejnych czatów

```text
playlist = konkretny eksport playlisty
playlist_item = pozycja w tym eksporcie
external_track = jeden utwór zewnętrznego serwisu, deduplikowany po service + ID
external_track_utwu = tylko jawne, rozstrzygnięte mapowania do middle_end
middle_end = kanoniczne utwory projektu
```

Nie cofaj modelu do kopiowania title/artist/album na każdej pozycji playlisty i nie twórz `middle_end` dla nierozpoznanych utworów tylko po to, żeby zapełnić FK.
