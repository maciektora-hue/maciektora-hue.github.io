# SOL — DOKUMENTACJA KATALOGÓW — AKTUALNA

Status: AKTUALNY OPIS STANU REPOZYTORIUM
Data zebrania: 2026-09-10
Źródło: WYŁĄCZNIE aktualny GitHub `maciektora-hue/maciektora-hue.github.io`, branch `main`

## 0. Zakres i zasada

Ten dokument opisuje publiczne katalogi i ich aktualną rolę w jednym repozytorium GitHub Pages.

Nie korzysta z Biblioteki ChatGPT ani ze starych kopii lokalnych.

Osobna aktualna dokumentacja audio istnieje w:

`SOL_DOKUMENTACJA-AUDIO-AKTUALNA.md`

Dlatego tutaj katalog `piosenki/` jest opisany na poziomie całego działu, a nie ponownie na poziomie szczegółowego modelu audio.

Jeżeli stara notatka techniczna jest sprzeczna z aktualnym kodem lub aktualnym `index.html`, stan bieżącego repozytorium ma pierwszeństwo.

---

# 1. Root repozytorium

Repozytorium:

`maciektora-hue/maciektora-hue.github.io`

Publiczny adres GitHub Pages:

`https://maciektora-hue.github.io/`

Główny `index.html` jest bramą do sześciu publicznych wejść:

1. `cv/`
2. `rownania/`
3. `rosja/`
4. `audhd/`
5. `piosenki/`
6. `techniczne/`

Root ma także `index-en.html` jako wersję angielską.

Założenie publicznego wejścia jest proste: jedno repozytorium, sześć działów, bez wspólnego rozbudowanego menu.

---

# 2. `cv/`

## Rola

Publiczna część zawodowa.

Główny katalog ma:

- `cv/index.html`
- `cv/index-en.html`
- aktualne wersjonowane pliki CV,
- podkatalog `cv/cv/`
- podkatalog `cv/seventeen-and-seventeen/`

## Główna brama

`cv/index.html` prezentuje dwie głębokości czytania:

1. **The CV** — bezpośredni obraz zawodowy;
2. **Seventeen & Seventeen** — głębsza warstwa pojęć, metod i logiki stojącej za CV.

## Stabilne wejście do CV

`cv/cv/index.html` jest aliasem / przekierowaniem do aktualnego wersjonowanego pliku CV.

W obecnym stanie wskazuje:

`CLAUDE_Maciej-Tora-AI-CV-v07_13-2026-09-09.html`

Dzięki temu publiczny adres `/cv/cv/` może pozostać stały mimo zmiany wersjonowanego pliku źródłowego.

## Seventeen & Seventeen

`cv/seventeen-and-seventeen/index.html` jest osobnym, stabilnym wejściem do materiału pogłębiającego profil zawodowy.

## Charakter techniczny

Ten dział jest zasadniczo statyczny: HTML na GitHub Pages, bez własnej kolekcji w `content_*` i bez własnej warstwy SQL opisanej w aktualnym kodzie backendu.

---

# 3. `rownania/`

## Rola

Publiczny dział matematyka / fizyka / AI.

Aktualna główna strona:

- `rownania/index.html`
- `rownania/index-en.html`

## Dwa główne wejścia

`rownania/index.html` prowadzi obecnie do:

1. `rownania/dziesiec-rownan/`
   - polskie i angielskie wejście,
   - stabilny adres do tekstu o dziesięciu równaniach;

2. `rownania/navier-stokes/`
   - polskie i angielskie wejście,
   - stabilny adres do eseju o Navier–Stokes, AI i sporze o autorstwo.

W katalogu pozostają także wersjonowane pliki źródłowe obu tekstów.

## Charakter techniczny

To statyczny dział GitHub Pages. W aktualnym backendzie nie ma osobnej kolekcji SQL `rownania` ani endpointu dedykowanego temu katalogowi.

---

# 4. `rosja/`

## Rola

Publiczny dział strategiczny „Rosyjska Kolumbryna”.

Ma własne:

- `index.html`
- `index-en.html`
- teksty źródłowe,
- stabilne aliasy URL,
- mapy sekcji i anchorów,
- skrypty audytowe i pomocnicze,
- warstwę danych w wspólnym SQL `content_*`.

## Stabilne URL-e

Aktualna warstwa techniczna używa krótkich, stałych publicznych adresów niezależnych od wersjonowanych nazw plików.

Wśród nich są m.in.:

- `/rosja/mapa/`
- `/rosja/kolumbryna/`
- `/rosja/gradually-suddenly/`
- `/rosja/lista-celow/`
- `/rosja/przejscie-na-hurt/`
- `/rosja/audyt/`
- `/rosja/zapas-kontra-strumien/`
- `/rosja/jak-koncza-sie-panstwa/`
- `/rosja/dark-legitimacy/`
- `/rosja/disinfolklore/`
- `/rosja/disinfolklore-swot/`
- `/rosja/rosyjskie-samobojstwa/`
- `/rosja/putin-cornered/`
- `/rosja/jalta-3/`
- `/rosja/jalta-3-apendyks/`
- `/rosja/ropa-gaz/`
- `/rosja/monopole/`

Aliasy zachowują fragment `#anchor`.

## Mapy struktury

W repo znajdują się m.in.:

- `rosja/SOL_mapa-sekcji-z-opisami.tsv`
- `rosja/SOL_mapa-sekcji-i-anchorow-rosja.tsv`
- `rosja/SOL_mapa-sekcji-z-opisami.html`
- `rosja/SOL_mapa-struktury-A1-z-opisami.tsv`
- mapy tematów PL/EN,
- opisy sekcji A1–A7, D1–D7, E1–E2.

Historycznie TSV były źródłem importu. Po migracji `content_*` SQL jest źródłem prawdy dla wspólnej struktury treści; TSV pełnią rolę źródeł migracyjnych / eksportów / materiałów pomocniczych zależnie od pliku.

## A1 i TOMY

Dokument A1 ma dodatkowy poziom struktury:

- 9 TOMÓW,
- TOMY nie są H1–H6,
- w SQL są reprezentowane jako `section_kind = 'volume'`,
- mają własne anchory i uczestniczą we wspólnej hierarchii `content_sections`.

`content_structure.py` utrzymuje dla A1 osobny `structure_order`, żeby TOMY i nagłówki mogły istnieć w jednym porządku strukturalnym bez niszczenia pierwotnego `section_order` nagłówków.

## Wspólna baza treści

W SQL kolekcja ma identyfikator:

`rosja`

Pierwotna migracja V1 zakładała:

- 16 dokumentów,
- 620 sekcji typu `heading`.

Późniejsza struktura dodaje 9 węzłów typu `volume` w A1.

Dane `rosja` są wystawiane przez wspólne endpointy `/api/content/...` i widoczne w `techniczne/content-explorer.html`.

---

# 5. `audhd/`

## Rola

Publiczna mapa tekstów o AuDHD.

Katalog ma:

- `audhd/index.html`
- `audhd/index-en.html`
- źródłowe wersjonowane HTML-e,
- krótkie stabilne aliasy,
- mapę sekcji i anchorów,
- narzędzia audytowe,
- wspólną warstwę SQL `content_*`.

## Nawigacja publiczna

Główny `audhd/index.html` jest mapą wejść tematycznych, nie liniowym spisem książki.

Prowadzi m.in. do stabilnych wejść:

- `/audhd/co-to-znaczy/`
- `/audhd/po-ludzku/`
- `/audhd/cechy/`
- `/audhd/po-diagnozie/`
- `/audhd/20-prac/`

oraz do dalszych tekstów i bezpośrednich fragmentów przez anchory.

## Stabilne URL-e i anchory

Warstwa aliasów została zbudowana tak, aby:

- publiczny URL był niezależny od wersjonowanej nazwy pliku,
- `location.hash` zachowywał dowolny fragment,
- nie trzeba było ręcznie wpisywać wszystkich anchorów do aliasu.

## Mapa sekcji

Główny plik mapy w repo:

`audhd/SOL_mapa-sekcji-i-anchorow-audhd.tsv`

Istnieje też publiczna mapa:

`audhd/SOL_mapa-sekcji-i-anchorow-audhd.html`

## Wspólna baza treści

W SQL kolekcja ma identyfikator:

`audhd`

Pierwotna migracja V1 zakładała:

- 18 dokumentów,
- 338 sekcji typu `heading`.

Późniejsze operacje uzupełniły opisy i tłumaczenia, które są obsługiwane przez aktualny model `content_sections` i Content Explorer.

Dane `audhd` są wystawiane przez te same wspólne endpointy `/api/content/...` co `rosja`.

---

# 6. `piosenki/`

## Rola całego katalogu

Publiczny dział analizy piosenek oraz jednocześnie katalog backendu Flask/Render obsługującego wspólną bazę Turso.

To ważne rozróżnienie:

`piosenki/` jest jednocześnie:

1. publicznym działem GitHub Pages;
2. katalogiem kodu backendowego uruchamianego przez Render;
3. miejscem części schematów, migracji i kodu wspólnej warstwy SQL.

Nie jest osobnym repozytorium.

## Publiczna brama

`piosenki/index.html` ma dwie główne gałęzie:

1. `slowa.html` — tekst, semantyka, tagi, czas;
2. `audio.html` — sygnał, cechy audio, sanityzacja i mapa akustyczna.

## Gałąź Słowa

`piosenki/slowa.html` opisuje system:

- kanonicznych utworów,
- tekstów,
- tagów semantycznych,
- osi, grup i rodzin,
- zmian w czasie zdarzeniowym,
- relacji między tagami,
- hipotez analitycznych.

Dane źródłowe są w SQL, a obliczenia statystyczne wykonuje Python po stronie Rendera.

Aktualne strony serwerowe obejmują m.in.:

- `/statystyki/czas`
- `/statystyki/kierunek`
- `/statystyki/relacje`
- `/statystyki/hipotezy`
- `/statystyki/13`

## Gałąź Audio

Szczegółowa aktualna dokumentacja jest w root repo:

`SOL_DOKUMENTACJA-AUDIO-AKTUALNA.md`

Nie należy rekonstruować jej z wcześniejszych plików roboczych.

## Backend

Główna aplikacja:

`piosenki/app.py`

Dodatkowy endpoint Content Explorer jest rejestrowany przez:

`piosenki/content_explorer_app.py`

Kod wspólnego modelu treści znajduje się m.in. w:

- `piosenki/content_store.py`
- `piosenki/content_structure.py`
- `piosenki/SOL_content-schema.sql`
- `piosenki/SOL_content-sql-specyfikacja-plan.md`
- `piosenki/SOL_content-keywords-model.md`

To dlatego część „Rosja + AuDHD” technicznie mieszka w katalogu `piosenki/`: Render ma `rootDir: piosenki`, więc wspólny backend został tam umieszczony.

---

# 7. `techniczne/`

## Rola

Publiczne zaplecze przekrojowe dla całego repozytorium.

Nie jest kolejną kolekcją merytoryczną w `content_*`.

Główne pliki:

- `techniczne/index.html`
- `techniczne/index-en.html`
- `techniczne/content-explorer.html`
- `techniczne/sql-viewer.html`
- skrypty eksportu / metryk sekcji.

## `content-explorer.html`

Publiczna, read-only przeglądarka wspólnej warstwy treści `rosja + audhd`.

Czyta dane z:

`https://piosenki-api.onrender.com/api/content`

oraz endpointów kolekcji.

Pokazuje m.in.:

- dokumenty,
- hierarchię sekcji,
- tytuły PL/EN,
- opisy PL/EN,
- anchory,
- deep-linki,
- słowa kluczowe,
- metryki tekstu.

Źródłem tych danych są aktualne tabele `content_*` w Turso.

## `sql-viewer.html`

Publiczny viewer schematu działającej bazy.

Czyta:

`/api/techniczne/schema`

Pokazuje aktualne tabele, kolumny, PK, FK, liczbę rekordów i dostępne dane o rozmiarach.

Jego celem jest pokazanie stanu faktycznej bazy, a nie rekonstrukcja ze statycznego `schema.sql`.

---

# 8. `bledy-AI/`

## Rola

Rejestr błędów AI związanych z pracą nad tym repozytorium.

Aktualnie zawiera m.in.:

- `bledy-AI/index.html`
- `bledy-AI/SOL_bledy-AI-02-2026-09-09.md`

To nie jest kolekcja `content_*`, nie uczestniczy w modelu Rosja/AuDHD i nie jest częścią analitycznej bazy piosenek.

Jego rolą jest dokumentowanie błędów proceduralnych i technicznych, aby nie były ponownie wymyślane jako świeże innowacje.

---

# 9. `.github/`

## Rola

Automatyzacja repozytorium przez GitHub Actions.

Workflowy wykonują m.in. operacje na plikach, audyty, migracje i jednorazowe zadania techniczne.

GitHub Actions są warstwą automatyzacji i mogą łączyć się bezpośrednio z Turso w zadaniach administracyjnych, ale nie są publicznym API dla stron WWW.

Publiczny ruch WWW idzie przez Render/Flask.

---

# 10. Najkrótsza mapa katalogów

```text
/
├── index.html / index-en.html     publiczna brama
├── cv/                            profil zawodowy, statyczny
├── rownania/                      matematyka/fizyka/AI, statyczny
├── rosja/                         treść + anchory + content_* SQL
├── audhd/                         treść + anchory + content_* SQL
├── piosenki/                      publiczny dział + backend Flask + SQL
├── techniczne/                    publiczne viewery wspólnej infrastruktury
├── bledy-AI/                      rejestr błędów AI
└── .github/workflows/             automatyzacja
```

Najważniejszy wyjątek od intuicji katalogowej:

**kod wspólnej bazy treści Rosja/AuDHD i backend API mieszka w `piosenki/`, ponieważ właśnie ten katalog jest rootem usługi Render. Nie oznacza to, że dane `content_*` są „danymi piosenek”.**

<!-- PLAYLISTY-2026-09-11 -->
---

# Aktualizacja 2026-09-11 — playlisty w projekcie `piosenki`

Aktualna warstwa playlist jest zdefiniowana w `piosenki/schema.sql` i składa się z `playlist`, `playlist_item` oraz `playlist_tag_def`.

Historia migracji znajduje się w:

- `piosenki/migrations/2026-09-10-playlists-spotify-bestof.sql`;
- `piosenki/migrations/2026-09-11-playlist-metadata.sql`.

Robocze eksporty playlist pozostają w `dane-robocze/`, m.in. `dane-robocze/playlistyspotifybestof/`. Plik audytowy nierozwiązanych pozycji znajduje się w `dane-robocze/csv-tsv/SOL_playlisty-brak-utwu-id-95.csv`.

Po imporcie bieżący stan playlist należy odczytywać z Turso/SQL, a nie rekonstruować z XLSX/CSV.

