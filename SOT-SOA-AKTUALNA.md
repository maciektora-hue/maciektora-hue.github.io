# SOT / SOA — ŹRÓDŁA PRAWDY CAŁEGO SYSTEMU

Wersja: 01.05 · Data: 2026-09-20
Status: **DOKUMENT NADRZĘDNY — CZYTAĆ PRZED PIERWSZĄ OPERACJĄ NA CZYMKOLWIEK**
Zakres: repozytorium `maciektora-hue/maciektora-hue.github.io` i usługi, z których korzysta

---

## 0. Po co to istnieje

Każdy model, który tu wchodzi, staje przed tym samym problemem: **w repozytorium leży
kilkadziesiąt plików wyglądających na aktualne, a część z nich nie jest.** Bez jednego
punktu odniesienia każda sesja rekonstruuje system z przypadkowych artefaktów i dochodzi
do własnych wniosków — czasem odwrotnych do poprzednich.

Dwa pojęcia, rozdzielone celowo:

- **SOT — Source of Truth.** Gdzie mieszka prawdziwa wartość. Pytasz o liczbę piosenek:
  idziesz do SQL, nie do CSV obok.
- **SOA — Source of Authority.** Co rozstrzyga, **gdy dwa źródła się nie zgadzają.**
  Nie zawsze to samo co SOT.

### Zasada nadrzędna

> **Przy sprzeczności między pamięcią a repozytorium — rozstrzyga repozytorium.**
> **Przy sprzeczności między repozytorium a usługą — rozstrzyga usługa.**
> **Przy sprzeczności między dokumentacją a tym dokumentem — rozstrzyga ten dokument.**

Środkowe zdanie jest nowe i wynika z weryfikacji przeprowadzonej 2026-09-20 — sekcja 7
pokazuje, gdzie plik konfiguracyjny w repo opisuje coś, czego na serwerze nie ma.

### Hierarchia źródeł, od najmocniejszego

| # | źródło | zakres rozstrzygania |
|---|---|---|
| 1 | **stan faktyczny usługi** (Supabase, Render, GitHub Actions) | co naprawdę działa i z czym |
| 2 | **ten dokument** | który plik jest aktualny, co jest czym |
| 2a | **`INSTRUKCJA-DLA-AGENTOW.md`** | jak pracować w tym repozytorium |
| 3 | `ZASADA-*.md` w roocie | twarde zakazy i nakazy pracy |
| 4 | `*-AKTUALNA.md`, także w `techniczne/` | reguły dziedzinowe swoich obszarów |
| 5 | strażnik CI `check_stable_www.py` | konwencja adresów, egzekwowana maszynowo |
| 6 | treść plików roboczych, komentarze w kodzie, stare notatki | nic nie rozstrzygają |

---

## 1. Dane — SOT: Supabase, projekt `maciekGithubHue`

**Jedyne źródło danych. Bez wyjątków** — patrz `ZASADA-TYLKO-SQL.md`.

| | |
|---|---|
| projekt | `maciekGithubHue` |
| ref | `uogsyhvkzirprxedurrh` |
| host | `db.uogsyhvkzirprxedurrh.supabase.co` |
| PostgreSQL | 17.6.1.166 |
| region | eu-central-1 |
| status | `ACTIVE_HEALTHY` (sprawdzone 2026-09-20) |
| tabel | 28, wszystkie z włączonym RLS |

**SOA: sama baza.** Żaden CSV, XLSX, TSV ani plik `.py` w `dane-robocze/` nie rozstrzyga
o zawartości. Pliki obok bazy są wejściem albo wyjściem, nigdy odpowiedzią.

### Tabele i role, stan 2026-09-20

**Piosenki, słowa, tagi** — `lyrics` 939 · `tag_catalog` 165 · `tag_group` 165 ·
`tag_groups` 12 · `tag_axis` 329 · `axes` 17 · `tag_valence` 76 · `families` 5 ·
`tag_snapshots` 942 · `tag_axis_polarity` **0**

**Audio** — `audio` 1040 · `audio_feature_snapshots` 1040 · `middle_end` 1058 ·
`audio_middle_end` 214 · `audio_match_details` 205

**Playlisty i utwory zewnętrzne** — `playlist` 17 · `playlist_item` 2403 ·
`external_track` 1033 · `external_track_utwu` 1030 · `playlist_tag_def` 1

**Korpus treści (Rosja i pozostałe)** — `content_documents` 34 · `content_sections` 967 ·
`content_section_metrics` 958 · `content_keyword_concepts` 892 · `content_keyword_terms` 1798 ·
`content_section_keywords` 3402 · `content_collections` 2 · `content_meta` 4

Dwie uwagi do przeczytania przed pracą na tagach: **`playlist_tag_def` ma jeden wiersz,
a `tag_axis_polarity` zero.** Puste nie znaczy zepsute, ale znaczy, że nic się na nich nie
opiera — zanim ktoś zbuduje na nich logikę, niech sprawdzi, czy w ogóle miały być wypełnione.

Rozróżnienie, które już raz kosztowało błąd (zapisany na półce SOL): **`playlist_tags` to
warstwa aktywna, `playlist.tags` i `external_url` to warstwa stara.** Szczegóły:
`SOL_DOKUMENTACJA-PLAYLISTY-AKTUALNA.md`.

---

## 2. Drugi projekt Supabase — NIE nasz

| | |
|---|---|
| projekt | `hue-nexus-sql`, ref `ejqturfbtghybugmizcl` |
| zawartość | teksty sanskryckie i tybetańskie, katalog plików, sesje web |
| należy do | repozytorium `hue-nexus/happy-hue-ledger` |

**To osobny system.** Nie jest źródłem prawdy dla niczego w tym repozytorium i nie wolno go
mieszać z `maciekGithubHue`. Wymieniony tu wyłącznie po to, żeby nikt go przez pomyłkę nie
uznał za naszą bazę, widząc dwa projekty na jednym koncie.

---

## 3. API — SOT: usługa `piosenki-api` na Render

| | |
|---|---|
| nazwa | `piosenki-api`, id `srv-daf3ji8n74is73866hd0` |
| URL | `https://piosenki-api.onrender.com` |
| repo / branch | to repozytorium, `main`, autodeploy przy commicie |
| region | frankfurt |
| plan | **`free`** — usypia po ~15 min bezczynności |
| baza | zmienna `SUPABASE_DATABASE_URL`, ustawiana ręcznie w panelu (`sync: false`) |

Czternaście endpointów, wśród nich `/health`, `/api/piosenki`, `/api/techniczne/schema`,
`/api/content/<collection_id>` i sześć widoków `/statystyki/*`.

### SOA dla wdrożenia: panel Render, NIE `render.yaml`

To jest najważniejsze zdanie tej sekcji i wynik weryfikacji, nie przepisania dokumentacji.
**Plik `render.yaml` w repozytorium opisuje inną konfigurację niż ta, która faktycznie
działa.** Rozbieżność w sekcji 7. Dopóki nie zostanie usunięta, `render.yaml` jest
dokumentem historycznym i nie wolno z niego wnioskować, co serwis uruchamia.

---

## 4. Strony statyczne — SOT: branch `main`

GitHub Pages serwuje `main` pod `https://maciektora-hue.github.io`. Plik w repozytorium
**jest** stroną; nie ma osobnego kroku publikacji i nie ma wersji roboczej.

**SOA dla adresów: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcja 0.1**, a pełny spis
wszystkich wejść i procedura wydania: **`SOL_DOKUMENTACJA-STUBY-AKTUALNA.md`**.
To pierwsze podaje regułę, egzekwowana
maszynowo przez `.github/scripts/check_stable_www.py` (siedem reguł).

Reguła w jednym zdaniu: **stały jest adres, nie nazwa pliku.** Każdy tekst ma wejście
katalogowe bez wersji; nazwa pliku jest wewnętrzna i może zawierać wersję, datę czy autora.
Tylko adres idzie na zewnątrz.

---

## 5. Automatyzacja — GitHub Actions

**26 plików workflow**, co myli, bo regularnie działają **trzy**:

| workflow | kiedy |
|---|---|
| `pages build and deployment` | każdy push na `main` |
| `check-stable-www.yml` | zmiany w HTML i w skrypcie strażnika |
| `podtrzymanie-api.yml` | cron, codziennie 05:17 UTC, `/health` |

Pozostałe 23 to **narzędzia jednorazowe i uruchamiane ręcznie** — anchory, ekstrakty sekcji,
rozpakowywanie ZIP-ów, jednorazowe importy. Każdy ma filtr `paths` wskazujący zwykle na
samego siebie: nieelegancka sztuczka na ręczne wyzwalanie, ale nieszkodliwa. Sprawdzone
2026-09-20: **25 z 26 ma filtr `paths`**, jedyny bez to `podtrzymanie-api.yml`, bo działa
na `schedule`.

**Dwa osobne zegary, dwa różne lekarstwa.** Render na planie `free` usypia usługę po
~15 minutach i budzi ją każdy request — crona to nie naprawia, bo usługa zaśnie kwadrans
później; na zimny start pomaga wyłącznie płatny plan. Supabase na planie `free` **pauzuje
projekt po 7 dniach bez ruchu w bazie**, a odpauzowanie jest ręczne i wygasa po 90 dniach.
Cron leczy wyłącznie to drugie.

**I leczy tylko dlatego, że `/health` otwiera połączenie i wykonuje `SELECT 1`.** Sam ping
Rendera nie jest aktywnością Supabase. To jest najbardziej krucha zależność w całym układzie:
usunięcie zapytania z health checka nie zepsuje ani jednego testu, nie zapali CI i nie zmieni
odpowiedzi API — a po tygodniu projekt będzie zapauzowany. Ostrzeżenie stoi nad endpointem
w `piosenki/app.py` i w samym workflow.

**To samo dotyczy drugiego projektu.** `hue-nexus-sql` nie ma własnego podtrzymania i
2026-09-20 dostał ostrzeżenie o zbliżającej się pauzie — zegar zresetowano ręcznym zapytaniem.
Docelowe rozwiązanie należy do repozytorium `hue-nexus/happy-hue-ledger`.

Reguła, która z tego wynika i obowiązuje: **zadanie jednorazowe musi się samo wyłączać
albo zostać usunięte po wykonaniu.** Dwa razy tak nie było i dwa razy skończyło się
workflowem-zombie.

---

## 6. Klasyfikacja katalogów

| katalog | klasa | co to jest |
|---|---|---|
| `audhd/` | **AKTUALNE** | eseje o AuDHD, 39 HTML |
| `rosja/` | **AKTUALNE** (w większości zamrożone) | korpus o rozpadzie Rosji, 50 HTML |
| `rownania/` | **AKTUALNE** | eseje o równaniach, 14 HTML |
| `cv/` | **AKTUALNE** | CV i teksty towarzyszące, 6 HTML |
| `piosenki/` | **AKTUALNE** | aplikacja Flask, widoki, dokumentacja, 22 pliki `.py` |
| `techniczne/` | **POMOCNICZE** | `sql-viewer`, `content-explorer` — narzędzia, nie publikacje |
| `bledy-AI/` | **AKTUALNE** | półka wstydu, trzy szuflady |
| `zadania/` | **AKTUALNE** | lista zadań |
| `dane-robocze/` | **IMPORTOWE** | wejście do importów; **nigdy źródło prawdy** |
| `dane-archiwalne/` | **HISTORYCZNE** | poczekalnia, m.in. `walkaosql/`; data przeglądu 2027-09-19 |
| `dokumentacja-archiwalna/` | **HISTORYCZNE** | bez publicznych wejść, celowo |
| `osierocone-html/` | **HISTORYCZNE** | cmentarz migawek; bez wejść, celowo |

Eksport: generowany przez API w locie (TSV z `/api/content/...`), **nie leży w plikach.**

---

## 7. Rozbieżności — stan po naprawie 2026-09-20

Wersja 01.00 tego dokumentu zgłaszała cztery pozycje. Po sprawdzeniu **dwie okazały się
moimi fałszywymi alarmami**, jedna jest naprawiona, jedna została otwarta. Pozostawiam
historię, bo wykreślenie własnej pomyłki z dokumentu o źródłach prawdy byłoby żartem.

### 7.1. `render.yaml` — NAPRAWIONE

Plik deklarował `gunicorn content_explorer_app:app`, a usługa od początku uruchamiała
`gunicorn app:app`. Różnica nie była kosmetyczna: **endpointy definiuje wyłącznie
`piosenki/app.py`**, bo `content_explorer_app.py` nie ma ani jednej trasy — wdrożenie
według tego pliku dałoby serwis bez API.

Naprawione przez doprowadzenie `render.yaml` do stanu odczytanego z Render, tak żeby jego
ewentualne zastosowanie niczego nie zmieniło. W pliku stoi komentarz wyjaśniający, że
**SOA dla wdrożenia pozostaje panel Render** — bo skoro rozjazd przeżył wszystkie
wdrożenia, to dowód, że ten plik nie jest przy deployu czytany.

### 7.2. Puste tabele — JEDNA OTWARTA, NIE NOWA

`playlist_tag_def` z jednym wierszem **nie jest zagadką** — to zadanie zgłoszone
2026-09-12 w `techniczne/SOL_ZADANIA-SQL-SUPABASE.md`, pozycja 1: *„Tabela jest potrzebna,
ale obecny stan jest niedokończony. W starej bazie jest tylko 1 rekord, natomiast powinno
być kilka definicji tagów więcej."* Zgłaszając ją jako nowe odkrycie, powtórzyłem cudzą
pracę zamiast ją przeczytać.

**`tag_axis_polarity` — ROZSTRZYGNIĘTE 2026-09-20.** Pustka jest stanem projektowym,
nie błędem. Tabela to bliźniak `tag_valence` o drobniejszym ziarnie: ten sam CHECK na
wartości (−1/0/1 albo NULL), ten sam słownik statusów, klucz rozszerzony o `axis_name`.
Oba klucze obce podpięte.

Rozstrzyga rozkład danych. Wszystkie 76 wpisów w `tag_valence` ma status `resolved` —
ani jednego `contextual`, choć CHECK go dopuszcza. Czyli wpisano tam **wyłącznie tagi
rozstrzygalne globalnie**, a pozostałych 89 świadomie pominięto. Z tych 89 **żaden nie leży
poza osiami, a 70 (79%) leży na więcej niż jednej** — czyli dokładnie w sytuacji, w której
jeden globalny znak jest niemożliwy, bo tag ma inną biegunowość na różnych osiach.

`tag_axis_polarity` jest przygotowanym miejscem na **172 pary (tag, oś)**. Nie jest
duplikatem `tag_valence`, nie jest nieudaną migracją, nie jest martwa. Zadanie wypełnienia:
`techniczne/SOL_ZADANIA-SQL-SUPABASE.md`.

### 7.3. Obie usługi Render na planie `free` — OTWARTE, poza zasięgiem agenta

`piosenki-api` i `temat-hue` usypiają po kwadransie. Dla `piosenki-api` dotyczy to 14 stron
doczytujących dane. Jedynym lekarstwem jest płatny plan `Starter` — cron
`podtrzymanie-api.yml` chroni wyłącznie Supabase przed 7-dniową pauzą i zimnego startu nie
usuwa. Zadanie stoi w `zadania/SOL_LISTA-ZADAN.md` i **wymaga decyzji finansowej człowieka.**

### 7.4. Ślady po SQLite — FAŁSZYWY ALARM

Zgłosiłem `sqlite_master` w projekcie na PostgreSQL jako prawdopodobny martwy kod po
migracji. **Jest odwrotnie.** W `piosenki/sol-sprawdz-integralnosc-PY-v01-03.py` SQLite
w pamięci jest użyty celowo: skrypt wykonuje plik SQL z ontologią tagów w jednorazowej
bazie i sprawdza, czy powstały oczekiwane tabele. To narzędzie walidacyjne, które nie
dotyka Supabase i **nie wolno go usuwać.**

Komentarze o SQLite/libsql/Turso w `content_store.py` i `content_structure.py` też są
w porządku: same oznaczają tamte funkcje jako napisane pod poprzedni silnik.

**Reguła, która z tego wynika:** zanim zgłosisz kod jako martwy, przeczytaj, co robi.
Nazwa z poprzedniej epoki nie jest dowodem.

## 7a. Rejestr dokumentów rozstrzygających

Trzynaście plików, które o czymś rozstrzygają. Trzy z nich **nie leżą w roocie** i dlatego
łatwo je przeoczyć — wersja 01.00 tego dokumentu je przeoczyła.

| plik | rozstrzyga o |
|---|---|
| `SOT-SOA-AKTUALNA.md` | źródła prawdy, hierarchia — **nadrzędny** |
| `INSTRUKCJA-DLA-AGENTOW.md` | jak pracować w tym repozytorium |
| `ZASADA-TYLKO-SQL.md` | jedyne dozwolone źródło danych |
| `piosenki/ZASADA-TYLKO-SQL.md` | ta sama zasada, kopia w katalogu aplikacji |
| `ZASADA-BEZ-DODATKOWYCH-SPRAWDZEN.md` | zakaz rozszerzania zakresu |
| `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md` | konwencja adresów, sekcja 0.1 |
| `SOL_DOKUMENTACJA-STUBY-AKTUALNA.md` | spis wejść, procedura wydania |
| `SOL_INFORMACJA-PO-SPRZATANIU-AKTUALNA.md` | co zmieniono 2026-09-19; sekcja 1 **odwrócona** |
| `SOL_DOKUMENTACJA-AUDIO-AKTUALNA.md` | warstwa audio |
| `SOL_DOKUMENTACJA-PLAYLISTY-AKTUALNA.md` | warstwa playlist |
| `SOL_DOKUMENTACJA-SLOWA-LYRICS-TAGI-AKTUALNA.md` | słowa, lyrics, tagi |
| `SOL_DOKUMENTACJA-MIEDZYKATALOGOWA-AKTUALNA.md` | warstwy wspólne |
| `techniczne/SOL_DOKUMENTACJA-SQL-SUPABASE-AKTUALNA.md` | **schemat SQL** — pełny opis tabel |
| `techniczne/SOL_ZADANIA-SQL-SUPABASE.md` | **otwarte zadania na bazie** |
| `zadania/SOL_LISTA-ZADAN.md` | zadania całego repozytorium |

Dwa ostatnie w `techniczne/` czytać **przed zgłoszeniem czegokolwiek jako problem w bazie**.
Połowa moich uwag z wersji 01.00 była tam już opisana.

Historyczne, **nie instrukcje**: `SOL_INSTRUKCJA-ARCHITEKTURA-SQL-GITHUB-RENDER-TURSO.md`
i wszystko, co wspomina Turso — integracja wycofana 2026-09-15.

---

## 8. Czego ten dokument NIE rozstrzyga

- **Czy treść jest dobra.** Zielone CI znaczy tylko, że deploy przeszedł i że sprawdzane
  reguły nie zostały złamane. Jakości tekstu nie ocenia nic i nikt.
- **Reguł dziedzinowych.** Audio, playlisty, słowa/lyrics/tagi i relacje międzykatalogowe
  mają własne `*-AKTUALNA.md` i tam należy szukać szczegółów.
- **Zawartości drugiego systemu** (`hue-nexus/happy-hue-ledger`).

---

## 9. Jak utrzymywać ten dokument

Podnosić wersję przy każdej zmianie treści: drobna korekta `YY`, przebudowa `XX`.
Nazwa pliku zostaje stała — ten dokument jest czytany po ścieżce, nie po adresie WWW,
więc konwencja wejść katalogowych go nie dotyczy.

**Przy każdej większej zmianie systemu sprawdzić stan faktyczny na nowo**, odpytując usługi,
a nie przepisując tę tabelę. Dokument opisujący stan sprzed pół roku jest gorszy niż jego
brak, bo wygląda na aktualny.

---

Zweryfikowano 2026-09-20 przez odpytanie Supabase i Render oraz inwentaryzację repozytorium.
Stworzono z pomocą Claude (Anthropic), wariant: Claude Opus 5.
