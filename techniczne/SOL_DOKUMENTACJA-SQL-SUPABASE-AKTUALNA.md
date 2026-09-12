# SOL — DOKUMENTACJA SQL / SUPABASE — AKTUALNA

Status: AKTUALNY STAN TECHNICZNY  
Data: 2026-09-12  
Repozytorium: `maciektora-hue/maciektora-hue.github.io`  
Nowa baza: Supabase / PostgreSQL 17  
Projekt Supabase: `maciekGithubHue`  
Region: `eu-central-1`

## 1. Najważniejszy stan

Nowa baza PostgreSQL w Supabase została utworzona i ma kompletny pusty schemat.

Stan po migracji schematu:

- 28 tabel w `public`,
- 0 rekordów danych użytkowych,
- wszystkie 28 tabel mają włączone RLS,
- brak publicznych polityk RLS,
- utworzone widoki `content_*`,
- nie wykonano jeszcze kopiowania danych z Turso/libSQL.

Turso pozostaje na tym etapie źródłem istniejących danych. Supabase zawiera wyłącznie przygotowaną strukturę docelową.

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

Ta ścieżka służy do kontrolowanych operacji administracyjnych, m.in.:

- `SELECT`,
- `INSERT`,
- `UPDATE`,
- `DELETE`,
- `ALTER TABLE`,
- `CREATE TABLE`,
- migracje schematu.

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

## 4. Ważne elementy zachowane z aktualnego modelu Turso

Schemat PostgreSQL nie jest mechanicznym przepisaniem starego `schema.sql`. Uwzględnia późniejsze migracje i rozszerzenia.

W szczególności zachowano:

- `playlist.playlist_series_id`,
- `playlist.exported_at`,
- legacy `playlist.tags`,
- aktualne tekstowe `playlist.playlist_tags`,
- `playlist_item.external_track_pk`,
- `content_sections.section_title_en`,
- `content_sections.description_en`,
- `content_sections.content_html`,
- `content_sections.structure_order`,
- pola keywordów PL/EN,
- aktualny model pojęć i terminów,
- `content_section_metrics`,
- istniejące identyfikatory rekordów bez automatycznego przeliczania ID podczas późniejszego importu.

`playlist.tags` pozostaje polem zgodności historycznej. `playlist_tags` jest aktualnym polem tekstowym.

## 5. Typy i różnice SQLite → PostgreSQL

Przy tworzeniu nowego schematu usunięto elementy specyficzne dla SQLite/libSQL, m.in.:

- `PRAGMA`,
- `json_valid(...)`,
- składnię przebudowy tabel charakterystyczną dla SQLite.

Typy zachowano możliwie blisko semantyki źródłowej:

- identyfikatory tekstowe → `TEXT`,
- identyfikatory liczbowe → `BIGINT` / `INTEGER` zależnie od pola,
- liczby zmiennoprzecinkowe → `DOUBLE PRECISION`,
- znaczniki czasu zachowane bez automatycznej zmiany istniejących wartości podczas przyszłej kopii.

Klucze ID używane w istniejącej bazie nie zostały zamienione na `SERIAL` ani automatyczne identity, aby możliwa była migracja 1:1.

## 6. Widoki

Utworzono aktualne widoki warstwy treści:

- `v_content_structure`,
- `v_content_map`,
- `v_content_human`,
- `v_rosja_mapa_sekcji`,
- `v_audhd_mapa_sekcji`,
- `v_content_status`.

Widoki zostały utworzone z `security_invoker = true`, dzięki czemu respektują uprawnienia i RLS użytkownika wywołującego.

Kierunek pozostaje:

```text
SQL → VIEW → API / HTML / TSV
```

Eksport TSV nie jest źródłem prawdy.

## 7. RLS i bezpieczeństwo

RLS jest włączone na wszystkich 28 tabelach.

Na tym etapie nie istnieją żadne polityki RLS.

Efekt jest celowy:

- klient publiczny nie dostaje automatycznie dostępu do danych,
- przypadkowe wystawienie Supabase API nie otwiera tabel do publicznego czytania ani zapisu,
- później można jawnie dodać tylko potrzebne polityki odczytu albo pozostać przy read-only API po stronie backendu.

Supabase Security Advisor zgłasza `RLS Enabled No Policy` dla 28 tabel jako informację, nie jako błąd. W aktualnym etapie jest to pożądany stan.

## 8. Wynik kontroli po DDL

Po wykonaniu migracji sprawdzono bazę przez Supabase.

Potwierdzone:

- dokładnie 28 tabel w `public`,
- wszystkie mają `rows = 0`,
- wszystkie mają `rls_enabled = true`,
- migracje DDL zakończyły się sukcesem.

Performance Advisor zgłasza obecnie:

- kilka kluczy obcych bez osobnych indeksów,
- brak PK w `tag_snapshots`, zgodnie ze starym modelem,
- istniejące indeksy jako `unused`, co jest oczywiste przy pustej bazie.

Nie wykonywano automatycznych „optymalizacji”, żeby nie zmieniać modelu przed migracją danych i obserwacją rzeczywistych zapytań.

## 9. Czego jeszcze NIE wykonano

Nie wykonano jeszcze:

- kopiowania danych z Turso do Supabase,
- przełączenia Render/Flask na PostgreSQL,
- przełączenia stron WWW na nową bazę,
- polityk publicznego odczytu,
- wyłączenia starej bazy Turso,
- kasowania ani modyfikowania danych źródłowych w Turso.

## 10. Następny etap migracji

Następny etap powinien być wykonany oddzielnie i kontrolowanie:

1. odczytać aktualne dane z Turso,
2. przenieść je tabelami do Supabase z zachowaniem ID,
3. porównać liczby rekordów i relacje FK,
4. wykonać kontrole integralności,
5. dopiero po zgodności przełączyć backend odczytowy,
6. pozostawić starą bazę jako kopię bezpieczeństwa do czasu zakończenia weryfikacji.

Schemat Supabase jest już gotowy na ten etap. Dane nie zostały jeszcze ruszone.
