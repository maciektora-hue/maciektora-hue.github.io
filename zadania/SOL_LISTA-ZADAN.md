# Lista zadań

Aktualna lista zadań dla całego repozytorium.

## DO ZROBIENIA

- **ZBADAĆ INTEGRALNOŚĆ DANYCH W CZĘŚCI "TEKSTY PIOSENEK"** (lyrics / tag_snapshots / powiązania z middle_end), szczególnie w kontekście analiz w czasie utworów prezentowanych na stronach WWW (`/statystyki/*`). Znaleziony przy okazji duplikat "Ja pas!" (utwu-000176 i utwu-000299, ten sam tekst) niekoniecznie jest błędem, ale skłania do sprawdzenia szerzej. Konkretne ryzyko do zbadania: czy gdzieś w liczeniu średnich/agregatów wartości `NULL` są przypadkiem traktowane jak `ZERO` zamiast być pomijane (typ błędu, który zaniża wynik) — sprawdzić to w kodzie budującym analizy czasowe (`statystyki.py`, `czas_okna.py`, `hipotezy_okna.py`, `relacje_okna.py`) oraz w samych danych.

- **ZBUDOWAĆ JEDEN NADRZĘDNY SOT + SOA DLA CAŁEGO SYSTEMU.** Przejrzeć całą migrację i wszystkie aktualne elementy systemu; sprawdzić, gdzie nadal mogą istnieć dane historyczne, stare źródła, stare schematy, stare eksporty, dawne instrukcje lub pliki, które wyglądają jak aktualne, ale już nimi nie są. Ustalić dla każdego obszaru, co jest obecnie źródłem prawdy (**Source of Truth, SOT**) oraz co jest źródłem rozstrzygającym w razie sprzeczności (**Source of Authority, SOA**). Następnie zebrać to w jednym grubym, ważnym pliku Markdown w root repozytorium. Dokument ma obejmować co najmniej: aktualne źródła danych i ich lokalizacje; hierarchię ważności źródeł; rozdzielenie `AKTUALNE / HISTORYCZNE / IMPORTOWE / EKSPORTOWE / POMOCNICZE`; aktualne tabele SQL i ich role; GitHub Pages, Render, Flask, Turso i GitHub Actions; katalogi i dokumentacje podsystemów; wskazanie plików zastąpionych przez nowsze; daty/wersje tam, gdzie rozstrzygają aktualność; oraz jasną zasadę, że przy sprzeczności kolejne czaty/agenci mają czytać SOT/SOA zamiast rekonstruować system z przypadkowych artefaktów. Przed napisaniem dokumentu najpierw **posprawdzać i poustalać stan faktyczny**, a nie przepisywać istniejącą dokumentację bez weryfikacji.

## W TOKU

- 

## ZROBIONE

- 
