# SOL — instrukcja importu playlist z XLSX/CSV do SQL

## Zakres

Tylko ten przypadek: Maciek wrzuca XLSX albo CSV z playlistą, a SOL ma ją zaimportować do SQL/Turso. Nie wymyślać mechaniki od nowa.

## Procedura

1. Pobierz najnowszy plik z GitHuba.
2. Odczytaj kolumny `id`, `name`, `artist`, `album`; opcjonalnie `index`.
3. Wiersze bez `id` pomiń, policz i pokaż w raporcie. Nie twórz dla nich `external_track`.
4. Ustal `playlist_id`, `playlist_series_id`, `service`, `name`, `source_file`, datę eksportu, a jeśli Maciek podał link także `external_playlist_id` i `external_url`. Dla playlist Maćka dodaj tag `owner:maciek-tora`.
5. Mapuj do `utwu_id` tylko po ID serwisu: Spotify przez `middle_end.spotify_id`, YouTube przez `middle_end.youtube_video_id`.
6. Automatyczne mapowanie tylko dla dokładnie jednego kandydata. Zero kandydatów = nierozpoznane. Więcej niż jeden = niejednoznaczne. Nigdy nie mapuj po tytule, artyście ani albumie.
7. Najpierw dry-run w transakcji zakończonej ROLLBACK. Raport: pozycje źródłowe, importowane, pominięte bez ID, istniejące/nowe `external_track`, istniejące/nowe mapowania, nierozpoznane, niejednoznaczne, konflikty metadanych.
8. Jeżeli dry-run jest czysty, uruchom ten sam importer z `dry_run=False`.
9. Jednorazowy import uruchamiaj przez GitHub Actions z bezpośrednim połączeniem `libsql` do Turso, używając repozytoryjnego sekretu `TURSO_ADMIN_TOKEN`. Nie używaj Render/Gunicorn jako transportu do jednorazowego importu playlist.
10. Docelowy zapis: `playlist → playlist_item → external_track → external_track_utwu → middle_end`.
11. Nie twórz sztucznych rekordów `middle_end`. `external_track` deduplikuj po `(service, external_track_id)`.
12. Istniejących metadanych `external_track` nie nadpisuj po cichu. Puste pole można uzupełnić, różnice tylko raportować.
13. Po COMMIT sprawdź live: istnienie `playlist_id`, liczbę pozycji, liczbę zmapowanych i nierozpoznanych oraz ID/URL playlisty, jeżeli były podane.
14. Dopiero po tej weryfikacji zgłoś zakończenie importu.
15. Jednorazowy workflow usuń po wykonaniu. Plik źródłowy XLSX/CSV zostaje w `dane-robocze` jako materiał historyczny.

## Skrót

**plik → dry-run → czysty wynik → GitHub Actions → Turso COMMIT → live verify → usuń workflow.**
