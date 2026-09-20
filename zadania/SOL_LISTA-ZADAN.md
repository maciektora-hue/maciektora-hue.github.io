> **Aktualizacja 2026-09-15:** integracja Turso została wycofana. Fragmenty poniżej opisujące Turso/libSQL i dawne workflowy są historyczne i nie mogą służyć jako instrukcje wykonawcze. Obecny backend korzysta wyłącznie z `SUPABASE_DATABASE_URL` (PostgreSQL). Aktualna konfiguracja: `piosenki/app.py`, `piosenki/schema_view.py`, `render.yaml`.

# Lista zadań

Wersja 01.05 · 2026-09-20

Aktualna lista zadań dla całego repozytorium.

> **2026-09-20:** źródła prawdy całego systemu zebrane w `SOT-SOA-AKTUALNA.md`,
> instrukcja pracy w `INSTRUKCJA-DLA-AGENTOW.md`, spis wszystkich wejść WWW
> w `SOL_DOKUMENTACJA-STUBY-AKTUALNA.md`.
> **Te trzy pliki czytać jako pierwsze, przed jakąkolwiek operacją.**
>
> **2026-09-19:** posprzątane adresy WWW w całym repozytorium. Uwaga: reguła nazw plików
> została 2026-09-20 odwrócona — obowiązuje `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md` 0.1.

## Ściąga: co to jest CI

**CI** = *Continuous Integration*. Robot, który po każdym zapisie do repozytorium sam odpala
sprawdzenia, zamiast liczyć na to, że ktoś zrobi je ręcznie. Tu są to GitHub Actions,
czyli pliki w `.github/workflows/`. Podgląd: zakładka **Actions** na GitHubie.

Działają trzy:

| Workflow | Co robi |
|---|---|
| `pages build and deployment` | wystawia stronę na `maciektora-hue.github.io` — to dzięki niemu zmiana w repo staje się widoczna w przeglądarce |
| `Konwencja stałych adresów WWW` | siedem reguł: martwe linki, anchory w przekierowaniach, kopie treści, stałe wejścia, aktualność wydania, zgodność numerów wersji |
| `Podtrzymanie API i bazy` | codziennie puka w `/health`, żeby darmowy Supabase nie wszedł w 7-dniową pauzę |

`unpack and split walkaosql` został usunięty 2026-09-19: był narzędziem skończonej
migracji do Supabase i odpalał się przy każdym pushu bez żadnego efektu.

**Zielone CI znaczy tylko, że deploy się udał i że sprawdzane reguły nie zostały złamane.
Nie znaczy, że treść jest dobra — tego nikt nie ocenia.**

CI **nie sprawdza, czy anchory istnieją** w plikach docelowych i nie ma tego robić.
Link do nienapisanej jeszcze sekcji to niedokończony tekst, nie awaria.
Pełne uzasadnienie: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcja 0.3.

## DO ZROBIENIA

- **PODTRZYMANIE BAZY `hue-nexus-sql` — ZADANIE DLA DRUGIEGO REPOZYTORIUM.**
  2026-09-20 przyszedł mail od Supabase: projekt `hue-nexus-sql` (`ejqturfbtghybugmizcl`,
  organizacja `maciekHUE`) jest **zaplanowany do zapauzowania** z powodu braku aktywności
  przez ponad 7 dni. Zegar zresetowano ręcznym zapytaniem — **to kupuje tydzień, nie więcej.**

  Przyczyna: ten projekt obsługuje usługę `temat-hue` z repozytorium
  `hue-nexus/happy-hue-ledger` i **nie ma odpowiednika naszego `podtrzymanie-api.yml`**.

  Czego NIE wystarczy: samo pingowanie Rendera. Dla Supabase liczy się wyłącznie ruch
  **w bazie**. Ping budzi usługę, ale jeśli trafiony endpoint nie otwiera połączenia,
  projekt i tak zapauzuje.

  Do zrobienia w `hue-nexus/happy-hue-ledger`:
  1. sprawdzić, czy aplikacja ma endpoint sięgający do bazy; jeśli nie — dodać `/health`
     robiący `SELECT 1`, wzorem `piosenki/app.py`;
  2. dodać cron w `.github/workflows/`, wzorem `podtrzymanie-api.yml`;
  3. nad endpointem postawić to samo ostrzeżenie, że zapytania do bazy nie wolno stamtąd
     usuwać, bo awaria będzie cicha.

  **Wymaga osobnej sesji** — sesja przypięta do właściciela `maciektora-hue` nie dodaje
  repozytoriów innego właściciela.

  Wariant awaryjny, gdyby pauza groziła wcześniej: ręczne zapytanie do bazy z panelu
  Supabase zeruje licznik na kolejne 7 dni.

- **DOKUPIĆ PŁATNY PLAN RENDER DLA `piosenki-api` — ok. 7 USD/mies. (Starter).**
  Usługa stoi dziś na planie `free`, który usypia kontener po około 15 minutach bezczynności.
  Po dłuższej przerwie pierwsze wejście czeka kilkanaście do kilkudziesięciu sekund na zimny start.
  Dotyczy **14 stron** doczytujących dane z tego API, między innymi `piosenki/playlisty.html`,
  `piosenki/slowa.html`, `techniczne/sql-viewer.html` i obu map sekcji. Strona otwiera się od razu,
  ale dane pojawiają się z opóźnieniem, co wygląda jak awaria.

  **Płatne instancje Render nie zasypiają** — to jedyne realne lekarstwo na zimny start.
  Cron `podtrzymanie-api.yml` go **nie usuwa**: chroni wyłącznie przed 7-dniową pauzą Supabase,
  bo Render i tak zaśnie kwadrans po pingu.

  Panel: https://dashboard.render.com/web/srv-daf3ji8n74is73866hd0 — zmiana planu na `Starter`.
  Cenę potwierdzić na miejscu, mogła się zmienić.

  **Czego NIE kupować przy okazji:** Supabase Pro (~25 USD/mies.). Nie przyspiesza zapytań,
  usuwa tylko pauzowanie i dodaje backupy — a pauzowanie załatwia darmowy cron.
  Oba projekty Supabase mają dziś status `ACTIVE_HEALTHY`.

  **Do decyzji osobno:** druga usługa `temat-hue` (repo `hue-nexus/happy-hue-ledger`)
  też stoi na `free` i ma tę samą przypadłość.

- ~~**ZBUDOWAĆ JEDEN NADRZĘDNY SOT + SOA DLA CAŁEGO SYSTEMU.**~~ — **zrobione 2026-09-20**,
  plik `SOT-SOA-AKTUALNA.md` w roocie. Stan faktyczny ustalony przez odpytanie Supabase
  i Render, nie przez przepisanie dokumentacji. Wykryte przy okazji cztery rozbieżności —
  sekcja 7 dokumentu — **z których żadna nie została naprawiona, wszystkie są do decyzji:**
  `render.yaml` opisuje inny startCommand niż działający serwis, dwie tabele są puste,
  obie usługi Render stoją na planie `free`, w kodzie zostały ślady po SQLite.

## W TOKU

- 

## ZROBIONE

### 2026-09-19 — sprzątanie adresów WWW i CI

- **Stałe nazwy plików** w `rownania/`, `piosenki/`, `cv/`, `audhd/` i `dokumentacja-archiwalna/`.
  Numer wersji i data przeniesione do nagłówków dokumentów.
- **Stuby pod starymi adresami** wszędzie tam, gdzie adres był publiczny; usunięte tam,
  gdzie nigdy nie wyszedł na zewnątrz. Rejestr rozesłanych linków: dokumentacja katalogów, sekcja 0.2.
- **Kopia treści pod stabilnym adresem CV** zamieniona na przekierowanie.
- **Wszystkie 60 stubów przekazuje `#anchor`** dalej.
- **Ilustracja OpenAI** w obu esejach o Navierze–Stokesie.
- **Usunięte dwa jednorazowe workflowy** pozostawione po skończonej robocie.
- **`walkaosql/` przeniesione** do `dane-archiwalne/`, z README i datą przeglądu 2027-09-19.
- **Strażnik CI** `check-stable-www.yml` pilnujący konwencji, z listą wyjątków i uzasadnieniami.
- **Cron `podtrzymanie-api.yml`** chroniący Supabase przed 7-dniową pauzą.
- **Dokumentacja**: konwencja adresów (0.1), rejestr rozesłanych linków (0.2), poczekalnie (0.2.1),
  czym jest CI i czego nie sprawdza (0.3), nota przekazania `SOL_INFORMACJA-PO-SPRZATANIU-AKTUALNA.md`.
- **Rejestr błędów**: trzy wpisy na półce SOL-a, trzy na półce Claude, kontekst tłumaczący
  różnicę długości obu list.

Kontrola końcowa: 167 HTML-i, 0 martwych linków, 0 błędów parsowania,
115 stron osiągalnych przed sprzątaniem i 116 po, zero utraconych.
