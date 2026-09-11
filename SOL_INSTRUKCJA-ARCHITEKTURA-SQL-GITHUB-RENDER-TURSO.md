# SOL — INSTRUKCJA: GitHub → WWW → Render API → Turso SQL

> **PRZED JAKĄKOLWIEK OPERACJĄ NA SQL PRZECZYTAJ TEN PLIK W CAŁOŚCI.**
>
> Nie zgaduj architektury, nie twórz nowego połączenia „na próbę”, nie obchodź istniejącego API i nie wykonuj operacji zapisu/usuwania tylko po to, żeby sprawdzić, czy połączenie działa.

## 1. Gdzie jest projekt

Repozytorium GitHub:

`maciektora-hue/maciektora-hue.github.io`

To jest jedno repozytorium zawierające m.in.:

- stronę GitHub Pages,
- katalog `piosenki/`,
- katalogi `audhd/`, `cv/`, `rosja/`,
- `.github/workflows/`,
- konfigurację Render w `render.yaml`.

Nie istnieje osobne repozytorium `maciektora-hue/piosenki`. `piosenki` jest katalogiem wewnątrz repozytorium `maciektora-hue/maciektora-hue.github.io`.

## 2. Jak działa strona WWW

Warstwa WWW jest publikowana z GitHuba jako GitHub Pages pod domeną:

`https://maciektora-hue.github.io`

HTML-y są w repozytorium. GitHub Pages jest warstwą statyczną.

## 3. GitHub Actions

Automatyzacje repozytorium znajdują się w:

`.github/workflows/`

To są workflowy GitHub Actions do operacji na plikach i automatyzacji repozytorium.

**GitHub Actions nie są API do SQL.**

Nie należy mieszać workflowów GitHub Actions z warstwą API Render/Turso.

## 4. Render

W głównym katalogu repozytorium jest plik:

`render.yaml`

Definiuje on usługę webową:

`piosenki-api`

Render uruchamia kod Python/Flask z katalogu:

`piosenki/`

Konfiguracja uruchomienia korzysta z Gunicorna i aplikacji Flask.

## 5. Turso / SQL

Baza działa w Turso przez `libsql`.

Adres bazy jest konfigurowany jako:

`TURSO_DATABASE_URL`

Token jest konfigurowany jako sekret środowiskowy Render:

`TURSO_ADMIN_TOKEN`

**Token administracyjny nie powinien być wpisywany do repozytorium GitHub ani do plików strony WWW.**

Kod backendu łączy się z Turso po stronie Rendera. Przeglądarka nie powinna łączyć się bezpośrednio z Turso.

## 6. Prawidłowy przepływ danych

`przeglądarka`

→ `GitHub Pages / HTML`

→ `HTTP /api/...`

→ `Render / Flask`

→ `libsql`

→ `Turso SQL`

→ `JSON / HTML`

→ `przeglądarka`

## 7. Istniejące API

W aplikacji Flask istnieją m.in. endpointy:

- `GET /health`
- `GET /api/techniczne/schema`
- `GET /api/piosenki`
- `GET /api/playlisty`
- `GET /api/content`
- `GET /api/content/<collection_id>`
- `GET /api/content/<collection_id>/structure`
- `GET /api/content/<collection_id>/status`
- `GET /api/content/<collection_id>/export.tsv`
- `GET /api/content/<collection_id>/explorer`

Endpointy `GET /api/playlisty` i `GET /api/content/<collection_id>/explorer` są logicznie read-only i wykonują odczyt danych.

CORS dla `/api/*` dopuszcza stronę:

`https://maciektora-hue.github.io`

## 8. WAŻNE: read-only endpoint ≠ read-only token

Obecna aplikacja backendowa używa `TURSO_ADMIN_TOKEN` do połączenia z bazą.

To oznacza:

- endpoint może wykonywać wyłącznie `SELECT`,
- ale samo połączenie z bazą może mieć większe uprawnienia.

Dlatego **nie wolno traktować obecnego tokena jako zabezpieczenia read-only**.

## 9. ZASADY DLA KOLEJNYCH CZATÓW / AGENTÓW

Przed pracą z SQL:

1. Przeczytaj ten plik.
2. Ustal, czy zadanie dotyczy GitHub Pages, GitHub Actions, Render API czy Turso SQL.
3. Jeśli zadanie dotyczy odczytu danych do WWW, używaj istniejącego API i istniejących endpointów GET.
4. Nie twórz nowego sposobu łączenia z Turso tylko dlatego, że nie znalazłeś istniejącego w pierwszej minucie.
5. Nie próbuj „testować” połączenia przez INSERT, UPDATE, DELETE, DROP, migrację schematu ani kasowanie danych.
6. Nie umieszczaj `TURSO_ADMIN_TOKEN` w HTML, JavaScript, repozytorium ani publicznym endpointcie.
7. Nie zakładaj, że katalog `piosenki/` jest osobnym repozytorium.
8. Nie myl GitHub Actions z API Render.
9. Jeśli trzeba zmienić schemat lub dane, najpierw jawnie ustal zakres operacji i używane połączenie.
10. Jeśli zadanie brzmi „tylko odczyt”, wykonuj wyłącznie odczyt.

## 10. Najkrótsza wersja

**GitHub przechowuje HTML i kod. GitHub Pages pokazuje WWW. Render uruchamia Flask. Flask łączy się przez libsql z Turso. WWW ma korzystać z API Render, a nie bezpośrednio z administracyjnego dostępu do SQL.**

---

## 11. Warstwa playlist — aktualny model

Pełna aktualna dokumentacja playlist znajduje się w:

`SOL_DOKUMENTACJA-PLAYLISTY-AKTUALNA.md`

Aktualny model nie składa się już tylko z `playlist` i `playlist_item`. Istotne tabele to:

- `playlist`;
- `playlist_item`;
- `playlist_tag_def`;
- `external_track`;
- `external_track_utwu`.

Podstawowy przepływ:

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

`external_track` deduplikuje zewnętrzne utwory po `(service, external_track_id)`. `external_track_utwu` przechowuje tylko jawne, rozstrzygnięte mapowania do `middle_end`.

Brak rekordu w `external_track_utwu` oznacza brak rozstrzygniętego mapowania. Nie należy tworzyć sztucznego `middle_end` ani stosować heurystyk tytuł/artysta/album bez jawnego polecenia.

`playlist_item` ma już `external_track_pk`. Stare pola zduplikowanych metadanych i stare `utwu_id` pozostają przejściowo dla zgodności i audytu; publiczny viewer/API korzysta z nowej warstwy.

Aktualny stan live po migracji 2026-09-11:

- 9 playlist;
- 919 pozycji;
- 636 `external_track`;
- 543 jawne relacje `external_track ↔ utwu_id`;
- 95 pozycji bez `utwu_id`, reprezentujących 93 różne `external_track`.

Wszystkie 9 obecnych playlist ma tag `owner:maciek-tora`. To opis stanu obecnego, nie reguła dla wszystkich przyszłych importów.

`spotify:alltimebest` / `AllTimeBestSpotify` ma potwierdzony:

```text
external_playlist_id = 5wDt92D4lFaSDIuVrdKLF9
external_url = https://open.spotify.com/playlist/5wDt92D4lFaSDIuVrdKLF9
```

Publiczny viewer:

- `piosenki/playlisty.html` — PL;
- `piosenki/playlisty-en.html` — EN;
- API: `GET /api/playlisty`;
- kod API: `piosenki/playlist_api.py`.

Viewer pokazuje tagi playlist, klikalne `external_url` oraz trzy tryby: playlista → utwory, utwór → playlisty, bez `utwu_id`.

Nowy importer zgodny z warstwą `external_track` **nie jest jeszcze gotowy** i nie należy go opisywać jako istniejącej części systemu.

`piosenki/schema.sql` ma odzwierciedlać aktualny stan schematu live. Pliki w `piosenki/migrations/` dokumentują drogę dojścia do tego stanu; nie należy uruchamiać dawnych migracji ponownie bez jawnej potrzeby.
