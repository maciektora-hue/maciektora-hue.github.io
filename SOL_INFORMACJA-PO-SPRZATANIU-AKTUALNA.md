# SOL — INFORMACJA PO SPRZĄTANIU

Wersja 01.04 · 2026-09-19
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

### 7. Drugi jednorazowy workflow, tym razem odwrotny

`.github/workflows/unpack-walkaosql.yml` usunięty. Jako **jedyny w repozytorium** miał gołe
`on: push` bez filtra ścieżek i gałęzi, więc budził się przy każdym pushu na każdą gałąź,
trzymając `contents: write` dla zadania bez pracy.

Przegląd wszystkich pozostałych workflowów: **każdy ma filtr `paths`**, więc żaden nie uruchamia się
przy zwykłym pushu. Większość ma filtr wskazujący na samego siebie — to celowa sztuczka na ręczne
wyzwalanie, nieelegancka, ale nieszkodliwa. Nie ruszane.

Reguła, która z tego wynika i obowiązuje dalej:
**zadanie jednorazowe musi się samo wyłączać albo zostać usunięte po wykonaniu.**
To był drugi taki przypadek: `sol-build-navier-stokes-zip-once` miał usterkę odwrotną
i nie uruchomił się nigdy.

### 8. Nowy cron podtrzymujący bazę

`.github/workflows/podtrzymanie-api.yml` — codziennie o 05:17 UTC puka w
`https://piosenki-api.onrender.com/health`, który otwiera połączenie i wykonuje `SELECT 1`.

**Po co:** darmowy Supabase pauzuje projekt po 7 dniach bez ruchu, a wyjście z pauzy wymaga
ręcznego przywracania. Cron temu zapobiega.

**Czego NIE robi:** nie usuwa zimnego startu dla odwiedzającego. Render i tak zaśnie kwadrans
po pingu. Na to jest osobne zadanie w `zadania/SOL_LISTA-ZADAN.md` — płatny plan usługi.

Przetestowany uruchomieniem ręcznym: `HTTP 200`, `{"database":1,"status":"ok"}`.

### 9. `.gitignore` i artefakty kompilacji

Dwa pliki `.pyc` trafiły do repozytorium przez `git add -A` po uruchomieniu `py_compile`.
Usunięte, `.gitignore` uzupełniony o `__pycache__/` i `*.py[cod]`.
Audyt wszystkich plików dodanych w tej sesji potwierdził, że poza tymi dwoma nic
niezamierzonego nie weszło. Zapisane w `bledy-AI/CLAUDE/` jako błąd 05.

## Stan końcowy repozytorium

| Miara | Wartość |
|---|---|
| plików HTML | 167 |
| stubów przekierowujących | 60 |
| stubów zachowujących `#anchor` | **60 / 60** |
| martwych linków wewnętrznych | **0** |
| błędów parsowania HTML | **0** |
| martwych linków w dokumentacji | **0** |
| działających workflowów | 3 |
| wyjątków na liście strażnika | 45 |

Osiągalność stron z publicznych korzeni porównana ze stanem sprzed sprzątania:
**115 przed, 116 po, zero utraconych**. Integralność przeniesionych plików potwierdzona
porównaniem sum blobów git: zero zmienionych, zero brakujących.

## Czego NIE wolno ruszać

**Cztery stuby w `rownania/` pod starymi adresami z wersją w nazwie są trwałe.**
Dwa polskie linki zostały rozesłane osobom trzecim, dwa angielskie były osiągalne z publicznej
nawigacji. Usunięcie ich oznacza 404 u kogoś innego. Rejestr: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcja 0.2.

**Jedenaście plików w `rosja/` bez sufiksu `-anchory` to świadomie zachowane zamrożone oryginały.**
Wyglądają na sieroty i nie są. Klasyfikacja: `rosja/SOL_audyt-osieroconych-html.md`.

**Lista wyjątków `.github/stable-www-allowlist.txt` nie jest sposobem na uciszenie CI.**
Każdy wpis ma uzasadnienie. Dopisanie pliku bez uzasadnienia należy odrzucić.

**Nie jest też listą zaległości.** 44 pliki treściowe w `rosja/` i `audhd/` mają wersje w nazwach
i **tak ma zostać**. Wersja w nazwie szkodzi tylko wtedy, gdy treść bywa aktualizowana — bo wtedy
powstaje plik o nowej nazwie i rozesłany link umiera. Te teksty są zamknięte: rosyjskie formalnie
zamrożone, a w `audhd/` żaden nie ma więcej niż jeden commit w historii. Wszystkie mają działające
stabilne wejścia katalogowe. **Nie przerabiać ich „dla porządku”.**

## Zanim cokolwiek zrobisz

1. Sprawdź, czy plik, który pamiętasz, nadal istnieje pod tą nazwą — `ls` albo wyszukiwanie w repo.
2. Przeczytaj `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcje 0.1, 0.2 i 0.3 — konwencja adresów, rejestr rozesłanych linków, zakres CI.
3. Uruchom strażnika lokalnie przed zapisem: `python3 .github/scripts/check_stable_www.py`.
   Ten sam strażnik chodzi w CI przy każdym PR i pushu na `main`, więc i tak złapie naruszenie —
   lepiej zobaczyć je u siebie niż na czerwono na GitHubie.
4. Jeżeli coś w tym dokumencie kłóci się z Twoją pamięcią, **rozstrzyga repozytorium**.

## Dlaczego sprzątał ktoś bez kontekstu

Sprzątanie przeprowadził model, który **nie zna historii rozmów** z budowy tego repozytorium.
Nie pamięta, co było ustalane w czacie, co miało powstać, co zostało świadomie odpuszczone
ani dlaczego któryś plik wygląda, jak wygląda. Ta niewiedza okazała się **zaletą**, i warto rozumieć dlaczego.

**Co daje brak kontekstu.** Nie ma z czego halucynować intencji. Nie da się powiedzieć
„przecież ustaliliśmy, że tak ma być”, bo nie ma czego pamiętać. Każde twierdzenie o stanie systemu
musi być **odczytane z repozytorium albo zmierzone**, inaczej nie istnieje.
Dzięki temu luki w dokumentacji stają się widoczne zamiast być nieświadomie łatane pamięcią.
To jest audyt przeprowadzony przez obcego — jedyny rodzaj, który znajduje to, czego autor przestał widzieć.

**Czego brak kontekstu NIE załatwia.** Nie chroni przed zgadywaniem. Gdy dokumentacji się nie przeczyta,
pamięć zastępuje się **wnioskowaniem z artefaktów**, a to jest równie zawodne.
Dokładnie tak poszło z jedenastoma plikami w `rosja/`: zostały ogłoszone martwymi na podstawie analizy
linków, podczas gdy dokument klasyfikujący je jako świadomie zamrożone leżał w tym samym katalogu.
Nie uratował ich brak pamięci, tylko **przeczytanie pliku przed operacją**.

**Wniosek najważniejszy, i to nie o modelu.** To sprzątanie udało się dlatego, że dokumentacja SOL-a
była **wystarczająco dobra, żeby przetrwać kontakt z kimś obcym**. Audyty osieroconych HTML-i,
opisy katalogów i raporty z migracji zawierały wszystko, co było potrzebne do podejmowania decyzji.
Gdyby klasyfikacja plików w `rosja/` żyła wyłącznie w czacie, zostałyby przeniesione do poczekalni
jako sieroty — i nikt by się nie zorientował.

**Stąd reguła na przyszłość:** intencja, która istnieje tylko w rozmowie, **nie istnieje**.
Kolejny agent jej nie odziedziczy i pierwsze porządki ją skasują.
Jeżeli coś ma zostać tak, jak jest, musi być napisane w repozytorium razem z powodem.
Sprawdzianem dokumentacji nie jest to, czy autor ją rozumie, tylko czy rozumie ją ktoś,
kto nie był przy tej rozmowie.

## Uczciwa uwaga na koniec

Sprzątanie też nie odbyło się bezbłędnie. Claude w trakcie tej pracy ogłosił jedenaście plików
w `rosja/` martwymi, zanim przeczytał audyt leżący w tym samym katalogu — czyli popełnił dokładnie
ten błąd, za który krytykowany jest SOL: rekonstruowanie stanu z artefaktów obok zamiast odczytania
źródła. Do usunięcia plików nie doszło, bo audyt został przeczytany przed operacją, ale fałszywe
twierdzenie zdążyło paść. Zapisane w `bledy-AI/CLAUDE/`.

**Nie jest tak, że jeden model popełnia błędy, a drugi nie. Jest tak, że jeden budował, a drugi sprząta.**
