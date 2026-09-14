# SOL — zapis prac z czatu: teksty, tagi i spójność SQL

Data: 2026-09-14  
Repozytorium: `maciektora-hue/maciektora-hue.github.io`  
Baza operacyjna: PostgreSQL/Supabase, projekt `maciekGithubHue` (`uogsyhvkzirprxedurrh`).

Ten plik jest historycznym podsumowaniem prac i decyzji z jednego czatu. Liczby opisują stan sprawdzony w tej rozmowie; kolejne zmiany należy weryfikować w live SQL. Nie jest to pełny zapis rozmowy ani kopia bazy.

## 1. Odnalezienie skryptów

Punktem wyjścia było poszukiwanie wcześniejszego sposobu pobierania tekstów piosenek i audio. Przeczytano lokalny dokument `D:\SOL-jak-pobieralismy-teksty-i-audio.md` i odnaleziono oba skrypty w repozytorium:

- [sol-pobierz-slowa-standalone-PY-v02-03.py](sol-pobierz-slowa-standalone-PY-v02-03.py) — pobieranie tekstów, kolejno z LRCLIB, lyrics.ovh i ChartLyrics;
- [SOL_youtube-music-playlista-100.py](SOL_youtube-music-playlista-100.py) — pobieranie audio z YouTube Music przez yt-dlp, przygotowane do pracy w Termux.

Skrypt audio został zidentyfikowany i opisany. W tym czacie uruchamiano lokalnie skrypt **tekstów**; późniejsze odczyty zastanej bazy audio nie oznaczają, że jej import wykonano w tej rozmowie.

## 2. Lista 68 brakujących tekstów i wykonanie na laptopie

Live SQL wskazał 68 rekordów `middle_end` z `lyrics_status = 'missing'`. Osadzoną w skrypcie listę zastąpiono dokładnie tym zestawem, zachowując identyfikatory i metadane. Sprawdzono składnię Python oraz zgodność listy z SQL.

Zmiana na GitHubie:
[836dc24dd4bb207fd87db5bd1c337deed8431aa1](https://github.com/maciektora-hue/maciektora-hue.github.io/commit/836dc24dd4bb207fd87db5bd1c337deed8431aa1).

Skrypt uruchomiono na laptopie. Pierwsze wykonanie nie miało dostępu do sieci; po udzieleniu dostępu uruchomiono go ponownie. Wykonanie zakończyło się poprawnie.

Plik wynikowy:
`szukamy-slow-pobrane-2pass-20260914-020257.csv`.

| Wynik automatu | Liczba |
|---|---:|
| found | 55 |
| instrumental | 3 |
| missing | 10 |
| Razem | 68 |

55 trafień zawierało 54 różne teksty: „Kokon” i „Kokon - Live” otrzymały ten sam tekst źródłowy. Wynik automatu był materiałem do przeglądu, nie automatyczną decyzją o statusie w bazie.

## 3. Przegląd i import tekstów do SQL

Przed zapisem przeczytano dokumentację i przygotowano manifest, kontrolę stanu wejściowego oraz transakcję. Wykonano próbę z ROLLBACK, następnie zapis i niezależny odczyt kontrolny.

Rezultat:

- dodano 54 rekordy `lyrics`, od `lyrics-000886` do `lyrics-000939`;
- powiązano teksty z 55 istniejącymi rekordami `middle_end`;
- ustawiono 51 statusów `full`, 3 `canonicaltext` i 1 `partial`;
- liczba tekstów wzrosła z 885 do 939;
- nie dodawano w tej operacji nowych rekordów `middle_end`; uzupełniano już istniejące utwory;
- wcześniej istniejące teksty i pozostałe pola utworów zachowano.

Decyzje wymagające pamięci:

| Utwór | Decyzja |
|---|---|
| Artur Rojek — Kokon - Live | `canonicaltext`; współdzieli `lyrics-000900` z wersją studyjną |
| Massive Attack — Girl I Love You - She Is Danger Remix | `canonicaltext`, `lyrics-000916`; metadane źródła nie potwierdzały remiksu |
| The Smashing Pumpkins — 1979 - Remastered 2012 | `canonicaltext`, `lyrics-000917`; źródło wskazywało tekst bazowy |
| Diablo Swing Orchestra — Pink Noise Waltz | `partial`, `lyrics-000915`; zachowano niepewny fragment oznaczony (?) |
| Jools Holland / Tom Jones — St. James' Infirmary Blues | Przed importem usunięto trzy początkowe linie kredytów, zachowując źródłowy CSV |

Przegląd obejmował treść i metadane źródeł. Nie wykonano odsłuchu i transkrypcji każdego nagrania 1:1. Status `partial` przy „Pink Noise Waltz” był ostrożną decyzją wobec niepewnego zapisu; nie rozstrzygano go ponownie w dalszej części czatu.

## 4. Dokumentacja, HTML i tagowanie

Przeczytano aktualne dokumenty SŁOWA / LYRICS / TAGI, dokumentację SQL oraz strony HTML opisujące obsługę, historię i założenia projektu. Odróżniono historyczne materiały od bieżącego schematu i kodu.

Każdy z 54 nowych tekstów przeczytano w całości. Tagi dobrano indywidualnie według live `tag_catalog`, bez tworzenia nowych tagów i bez kopiowania starych snapshotów.

Zapisano:

- 54 nowe rekordy `tag_snapshots`;
- 419 przypisań tagów;
- 106 różnych istniejących tagów;
- timestamp partii: `2026-09-14T00:44:54.362756Z`.

Liczba snapshotów wzrosła z 888 do 942. Próba z ROLLBACK i weryfikacja po COMMIT potwierdziły poprawność zapisu. Kontrola wykazała, że stare snapshoty, teksty i rekordy utworów nie zostały zmienione przez tagowanie.

Tagowanie pozostaje przypisane do `lyrics_id`. Wspólny tekst kilku wykonań nie wymaga osobnego snapshotu dla każdego `utwu_id`.

## 5. Trzy wyniki „instrumental” i decyzja o pozostawieniu braków

Sprawdzono źródła dotyczące trzech wskazań automatu. Znaleziono potwierdzenie, że „Prayer” ma śpiew i polski tekst, oraz opis „Les marionnettes” jako utworu na fortepian solo. Dla nagrania Gypsy Swing Revue źródła tekstowe nie dały jednoznacznego rozstrzygnięcia.

Następnie użytkownik wydał jawną decyzję, którą zapisano i sprawdzono w SQL:

| utwu_id | Utwór | Ostateczny status w tym czacie |
|---|---|---|
| utwu-001024 | Zbigniew Preisner — Les marionnettes | instrumental |
| utwu-001017 | Gypsy Swing Revue — Puttin' On the Ritz | instrumental |
| utwu-000987 | Zbigniew Preisner — Prayer | missing |

We wszystkich trzech `lyrics_id` pozostał NULL. Użytkownik zaakceptował pozostawienie **11 braków tekstów na dłużej** i nie chce dążyć do 100% kompletności. Dalsze poszukiwanie tych tekstów nie jest zadaniem do samoczynnego kontynuowania.

Stan statusów całej bazy po tych decyzjach:

| lyrics_status | Liczba |
|---|---:|
| full | 893 |
| canonicaltext | 25 |
| partial | 1 |
| paraphase | 50 |
| instrumental | 78 |
| missing | 11 |
| Razem middle_end | 1058 |

Pisownia `paraphase` jest nazwą statusu istniejącą w modelu.

## 6. Audyt spójności pozostałych tabel

Sprawdzono ostatnią partię 68 utworów oraz wszystkie 28 zadeklarowanych relacji kluczy obcych w publicznym schemacie.

Wyniki:

- 0 osieroconych odwołań w sprawdzonych relacjach;
- zgodność 68 powiązań i statusów z manifestem oraz późniejszymi decyzjami użytkownika;
- wszystkie 54 nowe teksty niepuste i posiadające snapshot tagów;
- poprawna składnia 419 przypisań, istniejące tagi oraz prawidłowe relacje do grup, osi i rodzin;
- 68/68 utworów powiązanych z rekordami Spotify i pozycjami playlist;
- 67/68 utworów miało przypisane audio; identyfikatory YouTube i istniejące wpisy wyjątków były zgodne.

Zastane ograniczenia kompletności, których nie uzupełniano:

- brak audio dla `utwu-001000` — fragment Carmen „Les voici! voici la quadrille!”;
- brak `audio_feature_snapshots` dla 67 przypisanych plików tej partii, przy 856 analizach innych plików w bazie;
- 11 utworów z partii bez `spotify_order` (50 globalnie), pomijanych przez model analiz czasu;
- 76 wpisów `tag_valence` przy 165 tagach katalogu; 67 ze 106 tagów użytych w nowej partii bez wpisu walencji;
- pusta globalnie `tag_axis_polarity` przy 329 parach tag–oś.

Nie utożsamiano tych braków z uszkodzeniem relacji. Zgodnie z dokumentacją AUDIO `audio_middle_end` i `audio_match_details` opisują wyjątki; zwykłe dopasowania nie wymagają dodatkowych wpisów w tych tabelach.

Audyt był odczytowy. Nie obejmował pełnego testu interfejsu ani fizycznej dostępności każdego pliku audio.

## 7. Wyjaśnienie mapowania playlist i porównanie historyczne

Po pytaniach użytkownika przeczytano całą aktualną dokumentację playlist i instrukcję importu. Kluczowe rozróżnienie:

```text
playlist → playlist_item → external_track → external_track_utwu → middle_end
```

- `external_track` zachowuje zewnętrzny utwór także po dopasowaniu;
- `external_track_utwu` zawiera **rozstrzygnięte przypisania**, więc przy rozpoznawaniu nowych utworów przybywa jej wpisów;
- maleje liczba `external_track` bez wpisu w tabeli powiązań;
- legacy `playlist_item.utwu_id` nie jest miarą aktualnej kompletności mapowania.

Początkowo zbyt mocno skupiono się na pustych polach legacy. Pełna kontrola i dokumentacja wyjaśniły, że 1576 pozycji ma puste bezpośrednie `utwu_id`, a mimo to poprawne mapowanie przez tabelę pośrednią. Nie należało tego „naprawiać” przez kopiowanie ID.

| Miara | Stan historyczny opisany po imporcie 11.09 | Stan sprawdzony 14.09 |
|---|---:|---:|
| Playlisty | 10 | 17 |
| Pozycje playlist | 1861 | 2403 |
| external_track | 1033 | 1033 |
| external_track_utwu | 937 | 1030 |
| Zewnętrzne utwory bez mapowania | 96 | 3 |

**2400/2403 pozycji wszystkich 17 playlist zapisanych w SQL ma jednoznaczne przypisanie do utwu_id — 99,88%.** Nie stwierdzono sprzecznych ani wieloznacznych mapowań w sprawdzonych pozycjach.

Sprawdzono także, czy pozostały niezmapowane pozycje z dokładnym Spotify ID już obecnym w `middle_end`: **0 takich przypadków**.

Trzy pozycje bez mapowania, wszystkie w Liked Songs:

| Pozycja | external_track_pk | Wykonawca | Utwór | Spotify ID |
|---|---:|---|---|---|
| 1 | 637 | Philip Glass | Wichita Vortex Sutra | 2KUxukmQbrKzhuG7kk0iRX |
| 2 | 638 | Świetliki | Nieprzysiadalność | 3lnd7vPIVVHyngZMcgfhLm |
| 3 | 639 | Świetliki | Filandia | 1FH1SrrTRWypTOUBGsVB88 |

Dawne braki w Liked Songs „Ja pas!” i „Miłość Miłość” mają już przypisania do `utwu-000176` i `utwu-000742`. Porównanie historyczne opisuje rozwój całego systemu; nie oznacza, że wszystkie 93 dodatkowe mapowania lub nowe rekordy utworów utworzono w tym czacie.

## 8. Zapisany kamień milowy i intencja użytkownika

Na prośbę użytkownika zaktualizowano [SOL_DOKUMENTACJA-PLAYLISTY-AKTUALNA.md](../SOL_DOKUMENTACJA-PLAYLISTY-AKTUALNA.md), dodając sekcję 17 o udanej pracy po migracji, aktualne liczby i wyraźną zasadę, że kompletność 100% nie jest celem.

Commit:
[3cebbe2e68050470264e321578ae290db743c1b7](https://github.com/maciektora-hue/maciektora-hue.github.io/commit/3cebbe2e68050470264e321578ae290db743c1b7).

Wniosek użytkownika: system po przejściu na „dorosły SQL” działa dobrze lub bardzo dobrze. Udało się kontynuować rozbudowę katalogu i zachować spójność. Zapis dokumentacyjny rozróżnia tę ocenę i pozytywny audyt danych od pełnego testu każdej funkcji aplikacji.

Użytkownik planuje dodawać cudze playlisty. Mogą one zwiększyć liczbę nierozpoznanych utworów i obniżyć procent mapowania. To naturalny efekt rozszerzenia zbioru. Nie wymuszać dopasowań ani nowych rekordów kanonicznych wyłącznie dla poprawiania statystyk.

## 9. Lokalne materiały z czatu

Materiały zapisano na laptopie w katalogu:
`D:\CODEXMACKOWY\2026-09-13\czy\outputs`.

Najważniejsze pliki:

- `sol-pobierz-slowa-standalone-PY-v02-03.py`;
- `szukamy-slow-pobrane-2pass-20260914-020257.csv`;
- `lyrics-import-before-20260914.json`;
- `lyrics-import-manifest-20260914.json`;
- `lyrics-import-after-20260914.json`;
- `lyrics-import-20260914.sql`;
- `lyrics-rollback-20260914.sql`;
- `lyrics-import-raport-20260914.md`;
- `tagowanie-54-tekstow-20260914.md`;
- `spojnosc-sql-20260914.md`.

Pliki przed/po imporcie są materiałem kontrolnym, nie pełną kopią bazy. Manifest opisuje moment importu; późniejsze decyzje o dwóch instrumentalach są zapisane w live SQL i tym podsumowaniu. Skrypt rollbacku ma zabezpieczenia i po późniejszym tagowaniu nie powinien być uruchamiany jako prosty sposób cofnięcia całej pracy.

Ten zapis MD nie publikuje pełnych tekstów piosenek ani lokalnych danych dostępowych.

## 10. Stan na koniec

Prace zlecone w czacie zostały wykonane. Teksty i tagi są zapisane, dwa instrumentale rozstrzygnięte, zaakceptowane braki pozostawione, a sprawdzone relacje SQL spójne. Nie uruchomiono automatycznego dalszego uzupełniania braków.
