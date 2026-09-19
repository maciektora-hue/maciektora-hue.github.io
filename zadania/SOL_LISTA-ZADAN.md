> **Aktualizacja 2026-09-15:** integracja Turso została wycofana. Fragmenty poniżej opisujące Turso/libSQL i dawne workflowy są historyczne i nie mogą służyć jako instrukcje wykonawcze. Obecny backend korzysta wyłącznie z `SUPABASE_DATABASE_URL` (PostgreSQL). Aktualna konfiguracja: `piosenki/app.py`, `piosenki/schema_view.py`, `render.yaml`.

# Lista zadań

Wersja 01.02 · 2026-09-19

Aktualna lista zadań dla całego repozytorium.

> **2026-09-19:** posprzątane adresy WWW i nazwy plików w całym repozytorium.
> Przed operacjami na plikach: `SOL_INFORMACJA-PO-SPRZATANIU-AKTUALNA.md`.

## Ściąga: co to jest CI

**CI** = *Continuous Integration*. Robot, który po każdym zapisie do repozytorium sam odpala
sprawdzenia, zamiast liczyć na to, że ktoś zrobi je ręcznie. Tu są to GitHub Actions,
czyli pliki w `.github/workflows/`. Podgląd: zakładka **Actions** na GitHubie.

Działają trzy:

| Workflow | Co robi |
|---|---|
| `pages build and deployment` | wystawia stronę na `maciektora-hue.github.io` — to dzięki niemu zmiana w repo staje się widoczna w przeglądarce |
| `Konwencja stałych adresów WWW` | pilnuje martwych linków, anchorów w przekierowaniach, kopii treści i nazw plików |
| `Podtrzymanie API i bazy` | codziennie puka w `/health`, żeby darmowy Supabase nie wszedł w 7-dniową pauzę |

`unpack and split walkaosql` został usunięty 2026-09-19: był narzędziem skończonej
migracji do Supabase i odpalał się przy każdym pushu bez żadnego efektu.

**Zielone CI znaczy tylko, że deploy się udał i że sprawdzane reguły nie zostały złamane.
Nie znaczy, że treść jest dobra — tego nikt nie ocenia.**

CI **nie sprawdza, czy anchory istnieją** w plikach docelowych i nie ma tego robić.
Link do nienapisanej jeszcze sekcji to niedokończony tekst, nie awaria.
Pełne uzasadnienie: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcja 0.3.

## DO ZROBIENIA

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

- **ZBUDOWAĆ JEDEN NADRZĘDNY SOT + SOA DLA CAŁEGO SYSTEMU.** Przejrzeć całą migrację i wszystkie aktualne elementy systemu; sprawdzić, gdzie nadal mogą istnieć dane historyczne, stare źródła, stare schematy, stare eksporty, dawne instrukcje lub pliki, które wyglądają jak aktualne, ale już nimi nie są. Ustalić dla każdego obszaru, co jest obecnie źródłem prawdy (**Source of Truth, SOT**) oraz co jest źródłem rozstrzygającym w razie sprzeczności (**Source of Authority, SOA**). Następnie zebrać to w jednym grubym, ważnym pliku Markdown w root repozytorium. Dokument ma obejmować co najmniej: aktualne źródła danych i ich lokalizacje; hierarchię ważności źródeł; rozdzielenie `AKTUALNE / HISTORYCZNE / IMPORTOWE / EKSPORTOWE / POMOCNICZE`; aktualne tabele SQL i ich role; GitHub Pages, Render, Flask, Turso i GitHub Actions; katalogi i dokumentacje podsystemów; wskazanie plików zastąpionych przez nowsze; daty/wersje tam, gdzie rozstrzygają aktualność; oraz jasną zasadę, że przy sprzeczności kolejne czaty/agenci mają czytać SOT/SOA zamiast rekonstruować system z przypadkowych artefaktów. Przed napisaniem dokumentu najpierw **posprawdzać i poustalać stan faktyczny**, a nie przepisywać istniejącą dokumentację bez weryfikacji.

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
