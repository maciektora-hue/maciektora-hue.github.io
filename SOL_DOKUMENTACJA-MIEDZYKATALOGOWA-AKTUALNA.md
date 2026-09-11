# SOL — DOKUMENTACJA MIĘDZYKATALOGOWA — AKTUALNA

Status: AKTUALNY OPIS WARSTW WSPÓLNYCH
Data zebrania: 2026-09-10
Źródło: WYŁĄCZNIE aktualny GitHub `maciektora-hue/maciektora-hue.github.io`, branch `main`

## 0. Cel

Ten dokument opisuje elementy, które nie należą logicznie tylko do jednego katalogu:

- publiczną stronę główną,
- GitHub Pages,
- Render,
- Flask,
- Turso/libSQL,
- wspólną bazę `content_*` dla Rosja + AuDHD,
- Content Explorer,
- SQL Viewer,
- analitykę piosenek renderowaną przez ten sam backend,
- GitHub Actions.

To jest dokument o połączeniach między działami, nie o treści poszczególnych projektów.

---

# 1. Jedno repozytorium, wiele logicznych projektów

Repozytorium:

`maciektora-hue/maciektora-hue.github.io`

Nie ma osobnych repozytoriów dla `piosenki`, `audhd`, `rosja`, `cv` itd.

Publiczny root GitHub Pages prowadzi do sześciu działów:

```text
cv/
rownania/
rosja/
audhd/
piosenki/
techniczne/
```

Każdy dział może mieć własne statyczne HTML-e, ale część z nich korzysta ze wspólnej infrastruktury serwerowej i SQL.

---

# 2. GitHub Pages — warstwa statyczna

GitHub Pages publikuje HTML-e z repozytorium pod:

`https://maciektora-hue.github.io`

Do tej warstwy należą m.in.:

- root `index.html` / `index-en.html`,
- publiczne indeksy katalogów,
- stabilne aliasy w katalogach,
- `techniczne/content-explorer.html`,
- `techniczne/sql-viewer.html`,
- statyczne strony piosenek `slowa.html`, `audio.html` itd.

GitHub Pages nie jest backendem SQL.

Statyczna przeglądarka, jeżeli potrzebuje danych dynamicznych, wywołuje API Render.

---

# 3. Render — wspólny backend

Plik root:

`render.yaml`

Definiuje usługę:

`piosenki-api`

Konfiguracja:

- runtime: Python,
- `rootDir: piosenki`,
- instalacja: `pip install -r requirements.txt`,
- start: `gunicorn content_explorer_app:app`.

Baza jest wskazana przez `TURSO_DATABASE_URL`.

Sekret dostępu jest przekazywany jako zmienna środowiskowa Rendera, nie powinien znajdować się w HTML ani publicznym kodzie frontendowym.

Ważne:

**Nazwa usługi `piosenki-api` i `rootDir: piosenki` nie oznaczają, że backend służy wyłącznie piosenkom.** Ten sam backend wystawia również wspólną warstwę `content_*` dla Rosja + AuDHD oraz dane techniczne.

---

# 4. Flask — warstwa API i stron serwerowych

Główna aplikacja:

`piosenki/app.py`

Aplikacja korzysta z `libsql` i otwiera połączenia do Turso po stronie serwera.

CORS dla `/api/*` dopuszcza:

`https://maciektora-hue.github.io`

Dzięki temu statyczne strony GitHub Pages mogą odczytywać dane z backendu Render.

Aktualne endpointy obejmują m.in.:

```text
GET /health
GET /api/techniczne/schema
GET /api/piosenki
GET /api/content
GET /api/content/<collection_id>
GET /api/content/<collection_id>/structure
GET /api/content/<collection_id>/status
GET /api/content/<collection_id>/export.tsv
GET /api/content/<collection_id>/explorer
```

Są też strony statystyczne generowane serwerowo:

```text
/statystyki/
/statystyki/czas
/statystyki/kierunek
/statystyki/relacje
/statystyki/hipotezy
/statystyki/13
```

---

# 5. Główny przepływ publicznego odczytu

Dla strony statycznej, która potrzebuje SQL:

```text
przeglądarka
    ↓
GitHub Pages / HTML
    ↓ HTTP GET
Render / Flask
    ↓ libsql
Turso
    ↓
Render / JSON lub HTML
    ↓
przeglądarka
```

Przeglądarka nie powinna łączyć się bezpośrednio z administracyjnym dostępem Turso.

---

# 6. Turso / libSQL — jedna baza, kilka domen danych

W aktualnej architekturze jedna baza Turso przechowuje kilka logicznych obszarów danych.

Najważniejsze grupy to:

## 6.1. Piosenki

M.in.:

- `middle_end`,
- `lyrics`,
- `tag_snapshots`,
- `tag_catalog`,
- `families`,
- `tag_groups`,
- `axes`,
- `tag_group`,
- `tag_axis`,
- tabele audio i audio features.

Szczegóły audio są opisane osobno w:

`SOL_DOKUMENTACJA-AUDIO-AKTUALNA.md`

## 6.2. Wspólna treść Rosja + AuDHD

Model `content_*` jest osobną domeną logiczną w tej samej bazie.

Nie jest częścią modelu piosenek tylko dlatego, że kod backendu leży w katalogu `piosenki/`.

---

# 7. `content_*` — wspólna baza Rosja + AuDHD

Podstawowy model został zaprojektowany tak, aby SQL był źródłem prawdy dla:

- kolekcji,
- dokumentów,
- sekcji,
- hierarchii,
- anchorów,
- opisów,
- stabilnych i źródłowych URL-i.

Podstawowe tabele:

```text
content_meta
content_collections
content_documents
content_sections
```

## Kolekcje

Aktualne logiczne kolekcje to:

```text
rosja
audhd
```

Pierwotna migracja V1 importowała:

- Rosja: 16 dokumentów, 620 sekcji heading;
- AuDHD: 18 dokumentów, 338 sekcji heading.

Razem:

- 34 dokumenty,
- 958 sekcji heading.

Później dla Rosja/A1 dodano dodatkowo 9 węzłów typu `volume`.

---

# 8. `content_sections` — wspólny węzeł struktury

Jedna pozycja reprezentuje element struktury dokumentu.

Istotne pola obejmują m.in.:

- `document_id`,
- `parent_section_id`,
- `section_kind`,
- `heading_level`,
- `depth`,
- `section_order`,
- `structure_order`,
- `section_title`,
- `section_title_en`,
- `anchor`,
- `description`,
- `description_en`,
- `keywords_pl`,
- `keywords_en`,
- `content_html`.

`section_kind` pozwala przechowywać nie tylko H1–H6, ale też inne elementy strukturalne, np. `volume`.

W A1 Rosji TOMY są właśnie węzłami `volume`.

---

# 9. Widoki i eksporty content

Model ma widoki przeznaczone do odczytu i zgodności z dawnymi mapami, m.in.:

- `v_content_structure`,
- `v_content_map`,
- `v_content_human`,
- `v_rosja_mapa_sekcji`,
- `v_audhd_mapa_sekcji`.

Publiczne API może na ich podstawie zwracać strukturę lub generować kompatybilne eksporty TSV.

Kierunek docelowy jest:

```text
SQL → VIEW → API / HTML / TSV
```

A nie ponowne traktowanie eksportowanego TSV jako nadrzędnego źródła prawdy po migracji.

---

# 10. Wspólne słowa kluczowe sekcji

Rozszerzenie modelu treści ma trzy tabele:

```text
content_keyword_concepts
content_keyword_terms
content_section_keywords
```

Zasada:

**jedno pojęcie = jeden `concept_id`, niezależnie od języka.**

PL i EN są różnymi nazwami tego samego pojęcia, a nie dwoma niezależnymi tagami.

Relacja:

```text
content_sections
    ↓ section_id
content_section_keywords
    ↓ concept_id
content_keyword_concepts
    ↓ concept_id
content_keyword_terms
    ├── PL
    └── EN
```

Stan zapisany w dokumentacji repo po imporcie słownika:

- 544 `content_keyword_concepts`,
- 1088 `content_keyword_terms`,
- 544 PL,
- 544 EN.

Sam model dopuszcza przypisania słów kluczowych do sekcji przez `content_section_keywords`.

---

# 11. Content Explorer — strona międzykatalogowa

Plik:

`techniczne/content-explorer.html`

To publiczna przeglądarka **dwóch katalogów merytorycznych naraz**:

- Rosja,
- AuDHD.

Frontend jest statyczny na GitHub Pages.

API:

`https://piosenki-api.onrender.com/api/content`

Backend dodatkowego endpointu:

`piosenki/content_explorer_app.py`

Explorer pobiera z SQL m.in.:

- dokumenty,
- sekcje,
- hierarchię rodzic-dziecko,
- strukturę `heading` / `volume`,
- tytuły PL/EN,
- opisy PL/EN,
- anchory,
- deep-linki,
- keywordy PL/EN,
- liczbę pojęć keywordowych,
- metryki znaków/liter/słów/stron znormalizowanych.

To jest najważniejsza obecnie publiczna strona przekrojowa dla `rosja + audhd`.

---

# 12. SQL Viewer — strona przekrojowa całej bazy

Plik:

`techniczne/sql-viewer.html`

API:

`https://piosenki-api.onrender.com/api/techniczne/schema`

Viewer nie odtwarza schematu z repozytorium.

Pobiera aktualny stan działającej bazy i pokazuje:

- tabele,
- kolumny,
- typy,
- NOT NULL,
- PK,
- FK,
- wartości domyślne,
- liczby wierszy,
- dostępne informacje o rozmiarze.

Jest więc narzędziem przekrojowym dla wszystkich domen SQL, nie tylko piosenek.

---

# 13. Piosenki — analityka serwerowa w tym samym backendzie

Gałąź `piosenki/slowa.html` linkuje do stron generowanych przez Flask/Jinja.

Model działania:

```text
Turso: fakty
    ↓
Python: obliczenia
    ↓
Flask/Jinja: gotowy HTML / SVG
    ↓
przeglądarka
```

Według aktualnej dokumentacji statystycznej warstwa analityczna nie zmienia danych źródłowych w Turso.

Oś czasu jest oparta o `spotify_order`, czyli kolejność zdarzeń polubienia, nie równomierny czas kalendarzowy.

Warstwy analityczne obejmują m.in.:

- czas,
- kierunek osi,
- relacje,
- hipotezy,
- zestaw 13 analiz.

To korzysta z tego samego serwisu Render, który obsługuje także `content_*`.

---

# 14. `content_structure.py` — przykład faktycznie międzykatalogowego kodu

Plik fizycznie znajduje się w:

`piosenki/content_structure.py`

ale czyta i obsługuje dane z:

`rosja/`

oraz wspólnych tabel `content_*`.

W szczególności dla A1 czyta:

`rosja/SOL_mapa-struktury-A1-z-opisami.tsv`

oraz utrzymuje w SQL 9 TOMÓW i pełną hierarchię A1.

To dobry przykład, dlaczego położenie pliku w katalogu nie zawsze oznacza przynależność logiczną do tego działu.

---

# 15. `content_store.py` — pierwszy import dwóch katalogów

Plik:

`piosenki/content_store.py`

Pierwotnie czytał dokładnie dwa źródła:

```text
rosja/SOL_mapa-sekcji-z-opisami.tsv
audhd/SOL_mapa-sekcji-i-anchorow-audhd.tsv
```

Importował je do wspólnego modelu `content_*`.

Marker:

`content_initial_import_v1`

Po zakończeniu migracji SQL ma być źródłem prawdy, a restart backendu nie powinien ponownie nadpisywać danych z TSV.

---

# 16. GitHub Actions — druga ścieżka techniczna

Workflowy znajdują się w:

`.github/workflows/`

Ich rola jest inna niż publicznego API.

Mogą wykonywać:

- audyty repozytorium,
- operacje na plikach,
- jednorazowe migracje,
- administracyjne operacje SQL,
- inne automatyzacje.

Dla administracyjnych operacji SQL workflow może łączyć się bezpośrednio przez `libsql` z Turso z użyciem sekretu GitHub Actions.

To nie zmienia przepływu publicznej strony WWW:

```text
WWW → Render API → Turso
```

GitHub Actions działają obok jako warstwa automatyzacji.

---

# 17. Ważna granica: read-only endpoint a uprawnienia tokena

Publiczny endpoint może w kodzie wykonywać wyłącznie `SELECT`, ale backend obecnie korzysta z połączenia tworzonego przy użyciu sekretu administracyjnego.

Dlatego:

**read-only zachowanie endpointu nie jest tym samym co kryptograficznie/read-only ograniczony token SQL.**

Publiczny frontend nie otrzymuje tokena Turso.

---

# 18. Mapa zależności

```text
                         ┌──────────────┐
                         │ GitHub repo  │
                         └──────┬───────┘
                                │
                  ┌─────────────┴─────────────┐
                  │                           │
          GitHub Pages                  GitHub Actions
                  │                           │
       statyczne HTML-e                 automatyzacje
                  │                           │
                  │ HTTP GET                  └──────→ Turso
                  ▼
          Render / Flask
                  │
                  │ libsql
                  ▼
                Turso
          ┌───────┴────────┐
          │                │
      piosenki          content_*
                         │
                  ┌──────┴──────┐
                  │             │
                Rosja         AuDHD
```

Publiczne strony przekrojowe:

```text
techniczne/content-explorer.html
    → Rosja + AuDHD / content_*

techniczne/sql-viewer.html
    → cała baza / schema endpoint
```

---

# 19. Co NIE jest wspólną bazą content

Na podstawie aktualnego kodu i indeksów repo nie należy automatycznie wkładać do `content_*`:

- `cv/`,
- `rownania/`,
- `bledy-AI/`,
- całego `piosenki/` jako kolekcji treści.

Obecny `content_*` ma kolekcje `rosja` i `audhd`.

Rozszerzenie modelu na inne katalogi byłoby osobną zmianą architektoniczną, nie stanem obecnym.

---

# 20. Najkrótsza wersja

```text
GitHub = pliki i historia
GitHub Pages = statyczny WWW
Render = wspólny backend Python/Flask
Turso = wspólna baza SQL

piosenki/* = piosenki + fizyczna lokalizacja backendu
content_* = wspólne dane Rosja + AuDHD
techniczne/content-explorer.html = wspólny viewer Rosja + AuDHD
techniczne/sql-viewer.html = viewer całej bazy
GitHub Actions = automatyzacja i operacje administracyjne
```

Najważniejsza zasada interpretacyjna:

**nie wnioskuj o domenie danych wyłącznie z katalogu, w którym leży kod. `piosenki/` jest rootem Rendera i dlatego zawiera także kod wspólny dla Rosja/AuDHD oraz narzędzi technicznych.**

<!-- PLAYLISTY-2026-09-11 -->
---

# Aktualizacja 2026-09-11 — warstwa playlist

W domenie piosenek działa obecnie także warstwa playlist:

- `playlist` — jeden rekord oznacza jeden konkretny eksport / stan playlisty w określonym momencie;
- `playlist_item` — utwory należące do tego eksportu wraz z kolejnością;
- `playlist_tag_def` — prosty słownik opcjonalnych tagów opisujących playlisty.

`playlist_series_id` może łączyć kolejne eksporty tej samej logicznej playlisty, także gdy zmieni się jej nazwa lub zawartość. Nie ma osobnej tabeli snapshotów.

`exported_at` oznacza moment eksportu ze Spotify / YouTube do pliku źródłowego. `imported_at` oznacza moment zaimportowania tego konkretnego eksportu do SQL.

Opcjonalne informacje opisowe, np. właściciel, sposób powstania, przeznaczenie czy program eksportujący, mogą być przechowywane w `playlist.tags` jako lista JSON. Tagi playlist są niezależne od systemu tagów `lyrics`.

Aktualny stan po migracji: 9 rekordów `playlist` i 919 rekordów `playlist_item`. SQL jest źródłem prawdy; migracje w `piosenki/migrations/` są historią zmian, nie źródłem do ponownego automatycznego importu.

