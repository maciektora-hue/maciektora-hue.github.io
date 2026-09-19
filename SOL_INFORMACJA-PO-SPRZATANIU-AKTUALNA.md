# SOL — INFORMACJA PO SPRZĄTANIU

Wersja 01.01 · 2026-09-19
Status: OBOWIĄZUJĄCA — PRZECZYTAĆ PRZED PIERWSZĄ OPERACJĄ NA PLIKACH
Autor sprzątania: Claude
Zakres: adresy WWW, nazwy plików, przekierowania, dokumentacja

## Dlaczego ten plik istnieje

To repozytorium zbudował SOL. Struktura katalogów, migracja bazy, większość treści i większość
mechanizmów to jego praca. Dokument nie podważa tej pracy i nie jest rozliczeniem.

Powstał z jednego powodu: **między ostatnią sesją SOL-a a tym stanem repozytorium zmieniło się
kilkadziesiąt ścieżek plików.** Model pracujący z pamięcią poprzednich rozmów albo z własnymi
notatkami będzie miał w głowie nazwy, które już nie istnieją. Działanie na takiej pamięci
skończy się tworzeniem plików obok, duplikatami albo linkami donikąd.

**Przed pierwszą operacją na plikach należy sprawdzić stan faktyczny, nie pamięć.**

## Zasada nadrzędna, która się nie zmieniła

Przy sprzeczności między pamięcią a repozytorium **rozstrzyga repozytorium**.
Przy sprzeczności między plikiem roboczym a dokumentacją `*-AKTUALNA.md` **rozstrzyga dokumentacja**.

## Co zostało naprawione

### 1. Konwencja nazw plików

Nazwy plików treściowych **nie zawierają już numeru wersji ani daty**. Wersja `XX.YY` i data
mieszkają w nagłówku wewnątrz dokumentu, zwykle tuż pod `<h1>`.

Zmienione ścieżki:

| było | jest |
|---|---|
| `rownania/navier-stokes-esej-dla-niematematyka-v02_00-2026-09-09.html` | `rownania/navier-stokes-esej-dla-niematematyka.html` |
| `rownania/navier-stokes-essay-for-non-mathematician-EN-v02_00-2026-09-09.html` | `rownania/navier-stokes-essay-for-non-mathematician-EN.html` |
| `rownania/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html` | `rownania/CLAUDE_rownania-metafizyka-i-komisja.html` |
| `rownania/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html` | `rownania/CLAUDE_equations-metaphysics-and-rigged-jury-EN.html` |
| `cv/CLAUDE_Maciej-Tora-AI-CV-v07_13-2026-09-09.html` | `cv/CLAUDE_Maciej-Tora-AI-CV.html` |
| `cv/CLAUDE_seventeen-and-seventeen-ai-concepts-EN-v08_07-2026-09-07.html` | `cv/CLAUDE_seventeen-and-seventeen-ai-concepts-EN.html` |
| `audhd/apendyks1-po-ludzku-02_01-2026-08-26.html` | `audhd/apendyks1-po-ludzku.html` |
| dziewięć plików `piosenki/SOL-klastrowanie-audio-*-v01-2026-09-08.html` i pokrewnych | te same nazwy bez `-v01-2026-09-08` |
| trzy pliki `dokumentacja-archiwalna/piosenki/*` | te same nazwy bez wersji i daty |

### 2. Stabilny adres nigdy nie jest kopią pliku

`cv/seventeen-and-seventeen/index.html` był **pełną kopią treści** zamiast przekierowania.
Dwie kopie tego samego tekstu pod dwoma adresami już zaczęły się rozjeżdżać.
Zamienione na przekierowanie.

**To jest reguła, nie jednorazowa poprawka.** Stabilny adres wskazuje na treść i nigdy jej nie powiela.

### 3. Przekierowania przekazują `#anchor`

Sam `<meta http-equiv="refresh">` gubi fragment adresu. Każdy stub w repozytorium ma dodatkowo:

```html
<script>location.replace('cel.html' + location.hash);</script>
```

Sprawdzone i poprawione we wszystkich 60 stubach.

### 4. Usunięty martwy workflow

`.github/workflows/sol-build-navier-stokes-zip-once.yml` czekał na części `part00`–`part07`,
a w repozytorium istniały tylko `part00`–`part06`. Warunek gotowości nigdy nie mógł być spełniony,
ZIP nigdy nie powstał. Workflow i jego niekompletne dane `.github/sol-data/nszip/` zostały usunięte.

### 5. Naprawione martwe linki

Stub w `osierocone-html/audhd/` przekierowywał na plik, który został w `audhd/` — czyli donikąd.
Przepięty na `audhd/20-prac/`.

### 6. Przeniesione do poczekalni

`walkaosql/` → `dane-archiwalne/walkaosql/`

Zrzut starej bazy i narzędzia hurtowego importu do Supabase. Import zakończył się 2026-09-12
z wynikiem 27/27 tabel i 15071/15071 wierszy. Obsługujący go workflow `unpack-walkaosql.yml`
nie został wtedy wyłączony i przez 78 commitów odpalał się przy każdym pushu bez żadnego efektu.
Workflow usunięty, pliki **nie usunięte** — leżą w poczekalni z README i datą przeglądu 2027-09-19.

Komentarze w `piosenki/content_structure.py` i `piosenki/content_store.py` zostały przepięte
na nową ścieżkę. Kod niczego z tego katalogu nie czyta, więc przenosiny nie zmieniły zachowania.

## Czego NIE wolno ruszać

**Cztery stuby w `rownania/` pod starymi adresami z wersją w nazwie są trwałe.**
Dwa polskie linki zostały rozesłane osobom trzecim, dwa angielskie były osiągalne z publicznej
nawigacji. Usunięcie ich oznacza 404 u kogoś innego. Rejestr: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcja 0.2.

**Jedenaście plików w `rosja/` bez sufiksu `-anchory` to świadomie zachowane zamrożone oryginały.**
Wyglądają na sieroty i nie są. Klasyfikacja: `rosja/SOL_audyt-osieroconych-html.md`.

**Lista wyjątków `.github/stable-www-allowlist.txt` nie jest sposobem na uciszenie CI.**
Każdy wpis ma uzasadnienie. Dopisanie pliku bez uzasadnienia należy odrzucić.

## Zanim cokolwiek zrobisz

1. Sprawdź, czy plik, który pamiętasz, nadal istnieje pod tą nazwą — `ls` albo wyszukiwanie w repo.
2. Przeczytaj `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcje 0.1, 0.2 i 0.3 — konwencja adresów, rejestr rozesłanych linków, zakres CI.
3. Uruchom strażnika lokalnie przed zapisem: `python3 .github/scripts/check_stable_www.py`.
4. Jeżeli coś w tym dokumencie kłóci się z Twoją pamięcią, **rozstrzyga repozytorium**.

## Uczciwa uwaga na koniec

Sprzątanie też nie odbyło się bezbłędnie. Claude w trakcie tej pracy ogłosił jedenaście plików
w `rosja/` martwymi, zanim przeczytał audyt leżący w tym samym katalogu — czyli popełnił dokładnie
ten błąd, za który krytykowany jest SOL: rekonstruowanie stanu z artefaktów obok zamiast odczytania
źródła. Do usunięcia plików nie doszło, bo audyt został przeczytany przed operacją, ale fałszywe
twierdzenie zdążyło paść. Zapisane w `bledy-AI/CLAUDE/`.

**Nie jest tak, że jeden model popełnia błędy, a drugi nie. Jest tak, że jeden budował, a drugi sprząta.**
