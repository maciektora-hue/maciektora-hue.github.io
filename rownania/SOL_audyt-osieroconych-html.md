# Audyt osieroconych HTML — RÓWNANIA

Status: ZAKOŃCZONY

## Zakres

Audyt dotyczy katalogu `rownania/` w repozytorium `maciektora-hue/maciektora-hue.github.io` i obejmuje statyczną osiągalność wszystkich plików HTML z publicznych wejść WWW.

Korzenie publiczne:
- `rownania/index.html`
- `rownania/index-en.html`

## Inwentaryzacja

Łącznie w `rownania/`: 14 plików HTML.

### Korzenie
- `rownania/index.html`
- `rownania/index-en.html`

### Redirecty podkatalogowe
- `rownania/dziesiec-rownan/index.html`
- `rownania/dziesiec-rownan/index-en.html`
- `rownania/navier-stokes/index.html`
- `rownania/navier-stokes/index-en.html`

### Stuby adresów archiwalnych
- `rownania/navier-stokes-esej-dla-niematematyka-v02_00-2026-09-09.html`
- `rownania/navier-stokes-essay-for-non-mathematician-EN-v02_00-2026-09-09.html`
- `rownania/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html`
- `rownania/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html`

### Pliki treściowe
- `rownania/CLAUDE_rownania-metafizyka-i-komisja.html`
- `rownania/CLAUDE_equations-metaphysics-and-rigged-jury-EN.html`
- `rownania/navier-stokes-esej-dla-niematematyka.html`
- `rownania/navier-stokes-essay-for-non-mathematician-EN.html`

## Osiągalność

`rownania/index.html` prowadzi do:
- `dziesiec-rownan/`
- `navier-stokes/`

`rownania/index-en.html` prowadzi do:
- `dziesiec-rownan/index-en.html`
- `navier-stokes/index-en.html`

Redirecty prowadzą dalej do czterech właściwych plików treściowych:
- `dziesiec-rownan/index.html` → `CLAUDE_rownania-metafizyka-i-komisja.html`
- `dziesiec-rownan/index-en.html` → `CLAUDE_equations-metaphysics-and-rigged-jury-EN.html`
- `navier-stokes/index.html` → `navier-stokes-esej-dla-niematematyka.html`
- `navier-stokes/index-en.html` → `navier-stokes-essay-for-non-mathematician-EN.html`

Stuby adresów archiwalnych są celowo nieosiągalne z nawigacji wewnętrznej.
Obsługują wyłącznie linki rozesłane na zewnątrz, zanim nazwy plików zostały ustabilizowane,
i przekierowują na aktualne adresy:
- `navier-stokes-esej-dla-niematematyka-v02_00-2026-09-09.html` → `navier-stokes-esej-dla-niematematyka.html`
- `navier-stokes-essay-for-non-mathematician-EN-v02_00-2026-09-09.html` → `navier-stokes-essay-for-non-mathematician-EN.html`
- `CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html` → `CLAUDE_rownania-metafizyka-i-komisja.html`
- `CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html` → `CLAUDE_equations-metaphysics-and-rigged-jury-EN.html`

Nie należy ich traktować jako osierocone HTML-e ani usuwać.

**Te cztery stuby są trwałe.** Dwa polskie adresy, `navier-stokes-esej-dla-niematematyka-v02_00-2026-09-09.html`
oraz `CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html`, zostały rozesłane osobom trzecim,
zanim nazwy plików zostały ustabilizowane. Po drugiej stronie są linki, których nikt już nie poprawi,
więc usunięcie tych plików oznaczałoby 404 u kogoś innego, a nie porządek u siebie.
Dwa odpowiedniki angielskie zostają z tego samego powodu: były osiągalne z publicznej nawigacji,
więc mogły trafić do indeksu wyszukiwarki lub czyichś zakładek.

To jest wyjątek, nie reguła. Stub pod adresem, który nigdy nie wyszedł na zewnątrz, jest śmieciem
i podlega usunięciu — tak jak stało się ze stubami CV. Zasada ogólna: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcja 0.1.

## Wynik końcowy

- 14 HTML-i w katalogu,
- 10/10 plików nawigacyjnych statycznie osiągalnych,
- 4 stuby adresów archiwalnych, celowo poza nawigacją,
- 0 osieroconych HTML-i,
- 0 plików do przeniesienia,
- 0 trwałych usunięć.

Audyt zakończony.