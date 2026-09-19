> **Aktualizacja 2026-09-15:** integracja Turso została wycofana. Fragmenty poniżej opisujące Turso/libSQL i dawne workflowy są historyczne i nie mogą służyć jako instrukcje wykonawcze. Obecny backend korzysta wyłącznie z `SUPABASE_DATABASE_URL` (PostgreSQL). Aktualna konfiguracja: `piosenki/app.py`, `piosenki/schema_view.py`, `render.yaml`.

# Lista zadań

Wersja 01.00 · 2026-09-19

Aktualna lista zadań dla całego repozytorium.

## Ściąga: co to jest CI

**CI** = *Continuous Integration*. Robot, który po każdym zapisie do repozytorium sam odpala
sprawdzenia, zamiast liczyć na to, że ktoś zrobi je ręcznie. Tu są to GitHub Actions,
czyli pliki w `.github/workflows/`. Podgląd: zakładka **Actions** na GitHubie.

Działają trzy:

| Workflow | Co robi |
|---|---|
| `pages build and deployment` | wystawia stronę na `maciektora-hue.github.io` — to dzięki niemu zmiana w repo staje się widoczna w przeglądarce |
| `unpack and split walkaosql` | skrypt pomocniczy |
| `Konwencja stałych adresów WWW` | pilnuje martwych linków, anchorów w przekierowaniach, kopii treści i nazw plików |

**Zielone CI znaczy tylko, że deploy się udał i że sprawdzane reguły nie zostały złamane.
Nie znaczy, że treść jest dobra — tego nikt nie ocenia.**

CI **nie sprawdza, czy anchory istnieją** w plikach docelowych i nie ma tego robić.
Link do nienapisanej jeszcze sekcji to niedokończony tekst, nie awaria.
Pełne uzasadnienie: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md`, sekcja 0.3.

## DO ZROBIENIA

- **ZBUDOWAĆ JEDEN NADRZĘDNY SOT + SOA DLA CAŁEGO SYSTEMU.** Przejrzeć całą migrację i wszystkie aktualne elementy systemu; sprawdzić, gdzie nadal mogą istnieć dane historyczne, stare źródła, stare schematy, stare eksporty, dawne instrukcje lub pliki, które wyglądają jak aktualne, ale już nimi nie są. Ustalić dla każdego obszaru, co jest obecnie źródłem prawdy (**Source of Truth, SOT**) oraz co jest źródłem rozstrzygającym w razie sprzeczności (**Source of Authority, SOA**). Następnie zebrać to w jednym grubym, ważnym pliku Markdown w root repozytorium. Dokument ma obejmować co najmniej: aktualne źródła danych i ich lokalizacje; hierarchię ważności źródeł; rozdzielenie `AKTUALNE / HISTORYCZNE / IMPORTOWE / EKSPORTOWE / POMOCNICZE`; aktualne tabele SQL i ich role; GitHub Pages, Render, Flask, Turso i GitHub Actions; katalogi i dokumentacje podsystemów; wskazanie plików zastąpionych przez nowsze; daty/wersje tam, gdzie rozstrzygają aktualność; oraz jasną zasadę, że przy sprzeczności kolejne czaty/agenci mają czytać SOT/SOA zamiast rekonstruować system z przypadkowych artefaktów. Przed napisaniem dokumentu najpierw **posprawdzać i poustalać stan faktyczny**, a nie przepisywać istniejącą dokumentację bez weryfikacji.

## W TOKU

- 

## ZROBIONE

- 
