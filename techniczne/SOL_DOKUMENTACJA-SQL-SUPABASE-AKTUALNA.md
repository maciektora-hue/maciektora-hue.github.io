# SOL — DOKUMENTACJA SQL / SUPABASE — AKTUALNA

Status: AKTUALNY STAN TECHNICZNY  
Data: 2026-09-12  
Repozytorium: `maciektora-hue/maciektora-hue.github.io`  
Nowa baza: Supabase / PostgreSQL 17  
Projekt Supabase: `maciekGithubHue`  
Region: `eu-central-1`

## 0. Zasada dalszej pracy

Ten plik jest bieżącą dokumentacją **nowego SQL-a w Supabase/PostgreSQL**.

Od tego etapu ustalenia dotyczące nowej bazy, jej schematu, migracji danych i późniejszych zmian SQL mają być aktualizowane właśnie tutaj.

Dla nowej bazy źródłem stanu faktycznego jest **Supabase/PostgreSQL**. Ten dokument opisuje ten stan i decyzje migracyjne.

`SQL Viewer` nie jest częścią dalszej migracji ani dokumentowania nowej bazy i nie należy go używać, modyfikować ani traktować jako źródła dla kolejnych kroków.

## 1. Najważniejszy stan

Nowa baza PostgreSQL w Supabase ma kompletny schemat i rozpoczętą ręczną kopię danych.

Aktualnie:

- 28 tabel w `public`,
- wszystkie 28 tabel mają włączone RLS,
- brak publicznych polityk RLS,
- utworzone widoki `content_*`,
- `families` zostało przeniesione i zweryfikowane: **5 rekordów**,
- pozostałych 27 tabel nie skopiowano jeszcze.

Kopiowanie odbywa się ręcznie, tabela po tabeli. Starej bazy nie modyfikujemy.

## 2. Architektura docelowa

Rozdzielone są dwie niezależne ścieżki dostępu.

### WWW — tylko odczyt

```text
GitHub Pages / WWW
        ↓
read-only API / backend
        ↓
PostgreSQL / Supabase
```

Frontend nie ma prawa wykonywać `INSERT`, `UPDATE`, `DELETE`, `ALTER`, `DROP` ani `CREATE`.

Publiczny dostęp do bazy nie korzysta z administracyjnego klucza Supabase.

### Administracja — pełny dostęp

```text
ChatGPT / Supabase connector
        ↓
PostgreSQL / Supabase
```

Ta ścieżka służy do kontrolowanych operacji administracyjnych: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, DDL i migracje schematu.

GitHub przechowuje kod i dokumentację. PostgreSQL przechowuje dane.

## 3. Tabele — 28

### Piosenki i tagi

1. `lyrics`
2. `tag_catalog`
3. `families`
4. `tag_groups`
5. `axes`
6. `tag_group`
7. `tag_axis`
8. `tag_valence`
9. `tag_axis_polarity`
10. `middle_end`
11. `tag_snapshots`

### Audio

12. `audio`
13. `audio_middle_end`
14. `audio_match_details`
15. `audio_feature_snapshots`

### Playlisty

16. `playlist`
17. `playlist_tag_def`
18. `external_track`
19. `external_track_utwu`
20. `playlist_item`

### Wspólna treść Rosja + AuDHD

21. `content_meta`
22. `content_collections`
23. `content_documents`
24. `content_sections`

### Keywordy / pojęcia

25. `content_keyword_concepts`
26. `content_keyword_terms`
27. `content_section_keywords`

### Metryki sekcji

28. `content_section_metrics`

## 4. Ważne elementy zachowane z aktualnego modelu

Schemat PostgreSQL uwzględnia późniejsze migracje i rozszerzenia, a nie tylko stary `schema.sql`.

Zachowano m.in.:

- `playlist.playlist_series_id`,
- `playlist.exported_at`,
- legacy `playlist.tags`,
- aktualne `playlist.playlist_tags`,
- `playlist_item.external_track_pk`,
- `content_sections.section_title_en`,
- `content_sections.description_en`,
- `content_sections.content_html`,
- `content_sections.structure_order`,
- pola keywordów PL/EN,
- `content_section_metrics`,
- istniejące identyfikatory rekordów bez automatycznego przeliczania ID.

`playlist.tags` pozostaje polem zgodności historycznej. `playlist_tags` jest aktualnym polem tekstowym.

## 5. Typy i różnice SQLite → PostgreSQL

Usunięto elementy specyficzne dla SQLite/libSQL, m.in. `PRAGMA`, `json_valid(...)` i składnię przebudowy tabel właściwą SQLite.

Typy zachowano możliwie blisko semantyki źródłowej:

- identyfikatory tekstowe → `TEXT`,
- identyfikatory liczbowe → `BIGINT` / `INTEGER`,
- liczby zmiennoprzecinkowe → `DOUBLE PRECISION`,
- istniejące ID nie zostały zamienione na `SERIAL` ani identity.

## 6. Widoki

Utworzono:

- `v_content_structure`,
- `v_content_map`,
- `v_content_human`,
- `v_rosja_mapa_sekcji`,
- `v_audhd_mapa_sekcji`,
- `v_content_status`.

Widoki mają `security_invoker = true`.

## 7. RLS i bezpieczeństwo

RLS jest włączone na wszystkich 28 tabelach. Na tym etapie nie istnieją publiczne polityki RLS.

Efekt jest celowy: klient publiczny nie dostaje automatycznie dostępu do tabel, a później można jawnie wystawić tylko potrzebny odczyt.

## 8. Wynik kontroli schematu

Po utworzeniu DDL potwierdzono:

- dokładnie 28 tabel w `public`,
- wszystkie mają `rls_enabled = true`,
- migracje DDL zakończyły się sukcesem.

Performance Advisor zgłasza kilka FK bez osobnych indeksów, brak PK w `tag_snapshots` zgodnie ze starym modelem oraz nieużywane indeksy przy prawie pustej bazie. Nie wykonywano automatycznych optymalizacji.

## 9. Stan migracji danych

Migracja danych **rozpoczęta**.

### ZROBIONE: `families`

Źródło użyte do ręcznej kopii: aktualny plik SQL ontologii na GitHubie:

`piosenki/sol-ontologia-tagow-TXT-v01-03.txt`

Nie był to CSV, lokalna kopia ani SQL Viewer. Publiczny endpoint starej bazy nie odpowiedział na czas, dlatego dla tej małej tabeli użyto kompletnego jawnego seeda SQL z repozytorium.

Do Supabase wpisano 5 rekordów:

- `lapis`,
- `butelkowa-zielen`,
- `sliwka`,
- `ochra`,
- `terakota`.

Kontrola bezpośrednio w Supabase: `COUNT(*) = 5`. Wszystkie pięć rekordów zostało odczytane po zapisie i ma oczekiwane wartości.

Nie wykonano jeszcze przełączenia Render/Flask, WWW, publicznych polityk odczytu ani wyłączenia starej bazy.

## 10. Zasada ręcznej kopii

Dla każdej kolejnej tabeli:

1. ustalić źródło danych,
2. odczytać komplet rekordów,
3. wpisać je do Supabase z zachowaniem ID,
4. porównać liczbę rekordów,
5. sprawdzić zawartość i FK,
6. dopisać wynik tutaj.

Jeśli kontrola nie przejdzie, zatrzymujemy się na tej tabeli.

## 11. Kolejność ręcznego kopiowania danych

### A. Tabele bazowe

1. `lyrics`
2. `tag_catalog`
3. `families` — **ZROBIONE: 5 rekordów**
4. `tag_groups` — **NASTĘPNE**
5. `audio`
6. `playlist`
7. `playlist_tag_def`
8. `external_track`
9. `content_meta`
10. `content_collections`
11. `content_keyword_concepts`

### B. Pierwsza warstwa zależności

12. `axes`
13. `tag_group`
14. `tag_axis`
15. `tag_valence`
16. `tag_axis_polarity`
17. `middle_end`
18. `tag_snapshots`
19. `audio_feature_snapshots`
20. `content_documents`
21. `content_keyword_terms`

### C. Tabele relacyjne

22. `audio_middle_end`
23. `audio_match_details`
24. `external_track_utwu`
25. `playlist_item`
26. `content_sections`
27. `content_section_keywords`
28. `content_section_metrics`

`content_sections` ma relację do samej siebie, więc rodzice muszą być kopiowani przed dziećmi. `tag_snapshots` nie ma PK, więc jego kontrola musi obejmować zawartość, nie tylko liczbę rekordów.
