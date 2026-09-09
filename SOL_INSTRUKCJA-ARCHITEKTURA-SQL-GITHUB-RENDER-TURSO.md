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
- `GET /api/content`
- `GET /api/content/<collection_id>`
- `GET /api/content/<collection_id>/structure`
- `GET /api/content/<collection_id>/status`
- `GET /api/content/<collection_id>/export.tsv`
- `GET /api/content/<collection_id>/explorer`

Endpoint `GET /api/content/<collection_id>/explorer` jest logicznie read-only i wykonuje zapytania `SELECT`.

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
