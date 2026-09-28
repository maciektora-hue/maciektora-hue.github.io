> **Aktualizacja 2026-09-15:** integracja Turso została wycofana. Fragmenty poniżej opisujące Turso/libSQL i dawne workflowy są historyczne i nie mogą służyć jako instrukcje wykonawcze. Obecny backend korzysta wyłącznie z `SUPABASE_DATABASE_URL` (PostgreSQL). Aktualna konfiguracja: `piosenki/app.py`, `piosenki/schema_view.py`, `render.yaml`.

# Lista zadań

Wersja 01.06 · 2026-09-28

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

- ~~**PODTRZYMANIE BAZY `hue-nexus-sql`.**~~ — **zrobione**, sprawdzone 2026-09-28.
  Repozytorium `hue-nexus/happy-hue-ledger` ma własny cron `.github/workflows/podtrzymanie-bazy.yml`:
  codziennie puka w `https://temat-hue.onrender.com/health`, a ten endpoint czyta tabelę w bazie.
  Ostatni przebieg 2026-09-28, wynik: sukces.

- ~~**DOKUPIĆ PŁATNY PLAN RENDER DLA `piosenki-api`.**~~ — **zrobione 2026-09-28.**
  API Rendera potwierdza plan `0.5c-512mb` (Starter) dla `piosenki-api`; usługa `temat-hue`
  z drugiego repozytorium też stoi na płatnym planie. Płatne instancje nie zasypiają.

  **Cron `podtrzymanie-api.yml` ZOSTAJE.** Płatny Render nie zasypia, ale cron nie służy
  budzeniu Rendera: codziennie dotyka bazy Supabase `maciekGithubHue`, która na darmowym
  planie pauzuje po 7 dniach bez ruchu. Ostatni przebieg 2026-09-28, wynik: sukces.
  Powód tej adnotacji: 2026-09-28 agent błędnie ocenił ten cron jako zbędny —
  `hue-nexus/happy-hue-ledger`, rejestr błędów, AI-027.

- ~~**ZBUDOWAĆ JEDEN NADRZĘDNY SOT + SOA DLA CAŁEGO SYSTEMU.**~~ — **zrobione 2026-09-20**,
  plik `SOT-SOA-AKTUALNA.md` w roocie. Stan faktyczny ustalony przez odpytanie Supabase
  i Render, nie przez przepisanie dokumentacji. Wykryte przy okazji cztery rozbieżności —
  sekcja 7 dokumentu — **z których żadna nie została naprawiona, wszystkie są do decyzji:**
  `render.yaml` opisuje inny startCommand niż działający serwis, dwie tabele są puste,
  obie usługi Render stoją na planie `free`, w kodzie zostały ślady po SQLite.

## KIEDYŚ — ODŁOŻONE

Zadania zapisane, żeby nie zginęły, ale świadomie odłożone przez Maćka. Nie zaczynać bez jego polecenia.

- **Teksty z telefonu na to repozytorium** — dopisane 2026-09-28:
  - eseje o modelach językowych jako dżinie (linia dżina z drugiej siedemnastki 17x17:
    LLM-as-genie, The inner genie, Sedimentation, Source amnesia);
  - teksty filozoficzne;
  - inne warte publikacji, żeby nie kurzyły się w telefonie.

  Gdy przyjdzie pora: najpierw szukać w archiwum PRA-PLIKÓW (katalog `catalog_files` w bazie
  `hue-nexus-sql`, repozytorium `hue-nexus/happy-hue-ledger`), bo tam mają trafiać pliki
  z telefonu. Stan 2026-09-28: 3933 pozycje; wyszukanie po „dżin / genie / djinn / lampa /
  życzeni” nie znalazło esejów, eseje mogą mieć inne tytuły albo nie być jeszcze w archiwum.
  Co publikować, wybiera Maciek. Każdy tekst: stały adres, stub, wersja w nagłówku, kafelek;
  na koniec link z 17x17.

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
