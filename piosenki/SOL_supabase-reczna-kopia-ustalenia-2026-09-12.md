# SOL — ręczna kopia Turso → Supabase/PostgreSQL

Data: 2026-09-12
Status: USTALENIA ROBOCZE PRZED UTWORZENIEM SCHEMATU

## Cel

Przenieść obecną bazę `piosenki` z Turso/libSQL do nowej bazy Supabase/PostgreSQL jako kontrolowaną ręczną kopię logiczną.

To NIE ma być automatyczna migracja całej bazy jednym narzędziem ani bezpośredni dump SQLite → PostgreSQL.

Najpierw odtwarzamy kompletną strukturę bazy w PostgreSQL. Dopiero po jej sprawdzeniu kopiujemy dane tabela po tabeli.

## Stan nowej bazy

Supabase jest podłączony do ChatGPT.

Projekt:

- nazwa: `maciekGithubHue`
- region: `eu-central-1` / Frankfurt
- status podczas testu: `ACTIVE_HEALTHY`
- silnik: PostgreSQL 17.6

Bezpośrednie wykonywanie SQL przez integrację Supabase działa. Test `SELECT current_database(), current_user, version()` zakończył się poprawnie.

Na obecnym etapie nie przeniesiono żadnych danych i nie utworzono jeszcze docelowych tabel projektu `piosenki` w Supabase.

## Architektura docelowa

Dwa niezależne kanały dostępu:

### WWW

Publiczna warstwa WWW ma mieć wyłącznie odczyt.

Dozwolone:

- SELECT,
- widoki przeznaczone do publikacji,
- agregaty i dane potrzebne stronom.

Niedozwolone z publicznego WWW:

- INSERT,
- UPDATE,
- DELETE,
- ALTER,
- DROP.

Publiczny frontend nie może otrzymać klucza `service_role` ani innego sekretu administracyjnego.

### ChatGPT / administracja

Osobny kanał administracyjny przez integrację Supabase ma umożliwiać bezpośrednio:

- SELECT,
- INSERT,
- UPDATE,
- DELETE,
- CREATE TABLE,
- ALTER TABLE,
- pozostałe kontrolowane operacje DDL.

GitHub przechowuje kod i dokumentację. PostgreSQL przechowuje dane.

## Zasada kopiowania

Stara baza Turso pozostaje nietknięta podczas budowania kopii.

Kolejność:

1. odtworzyć cały schemat w Supabase,
2. sprawdzić schemat,
3. dopiero potem kopiować dane,
4. dane kopiować kontrolowanie, tabela po tabeli,
5. po każdej tabeli porównać liczbę rekordów i wybrane rekordy po kluczach,
6. stara baza pozostaje backupem do czasu pełnej walidacji kopii.

Nie używać CSV/XLS/XLSX/TSV jako zastępczego źródła danych. Obowiązuje zasada projektu `ZASADA-TYLKO-SQL.md`: dane pochodzą z SQL, chyba że użytkownik jawnie dopuści wyjątek.

## Źródła opisu struktury

Nie istnieje jeden kompletny plik opisujący cały aktualny model.

Do rekonstrukcji schematu trzeba użyć łącznie:

- `piosenki/schema.sql`,
- wyspecjalizowanych plików `.sql`,
- plików dokumentacji `.md`,
- wykonanych migracji w `piosenki/migrations/`,
- aktualnego kodu aplikacji, jeśli odwołuje się do kolumn lub tabel dodanych po pierwotnym schemacie.

Viewer nie jest wymagany do dalszej pracy nad rekonstrukcją schematu.

## Główny `schema.sql`

Aktualnie rozpoznano w nim 20 tabel:

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
12. `audio`
13. `audio_middle_end`
14. `audio_match_details`
15. `audio_feature_snapshots`
16. `playlist`
17. `playlist_tag_def`
18. `external_track`
19. `external_track_utwu`
20. `playlist_item`

Te 20 tabel nie stanowi jednak całej obecnej struktury projektu.

## Dodatkowy model `content_*`

Plik `SOL_content-schema.sql` definiuje dodatkowe aktywne tabele:

- `content_meta`
- `content_collections`
- `content_documents`
- `content_sections`

Definiuje także widoki:

- `v_content_structure`
- `v_content_map`
- `v_content_human`
- `v_rosja_mapa_sekcji`
- `v_audhd_mapa_sekcji`
- `v_content_status`

W modelu występują istotne reguły:

- `content_documents.collection_id` → `content_collections.collection_id`
  - `ON UPDATE CASCADE`
  - `ON DELETE RESTRICT`
- `content_sections.document_id` → `content_documents.document_id`
  - `ON UPDATE CASCADE`
  - `ON DELETE CASCADE`
- `content_sections.parent_section_id` → `content_sections.section_id`
  - `ON UPDATE CASCADE`
  - `ON DELETE SET NULL`
- liczne `UNIQUE` i `CHECK`, które należy zachować w PostgreSQL.

## Rozszerzenia `content_sections`

Późniejszy kod pokazuje, że pierwotny `SOL_content-schema.sql` nie jest już kompletnym opisem tabeli `content_sections`.

Na pewno później dodano lub używano kolumny:

- `structure_order`

Kod aplikacji odwołuje się również do kolumn:

- `content_html`
- `section_title_en`
- `description_en`
- `keywords_pl`
- `keywords_en`

Przed utworzeniem `content_sections` w Supabase trzeba odnaleźć dokładne DDL tych późniejszych zmian i ustalić ich typy, NULL/NOT NULL, defaulty oraz ewentualne constraints.

Nie wolno tworzyć tej tabeli wyłącznie na podstawie starego `SOL_content-schema.sql`.

## Model słów kluczowych treści

Dokument `SOL_content-keywords-model.md` oznacza ten model jako wdrożony do Turso.

Aktywne tabele:

- `content_keyword_concepts`
- `content_keyword_terms`
- `content_section_keywords`

Indeksy:

- `idx_keyword_terms_norm`
- `idx_section_keywords_concept`
- `idx_section_keywords_section`

Istotne constraints:

### `content_keyword_concepts`

- `concept_id` PK
- `concept_key` UNIQUE NOT NULL

### `content_keyword_terms`

- FK `concept_id` → `content_keyword_concepts`
- `lang IN ('pl','en')`
- `is_preferred IN (0,1)`
- UNIQUE `(concept_id, lang, keyword_norm)`

### `content_section_keywords`

- PK `(section_id, concept_id)`
- FK `section_id` → `content_sections`
- FK `concept_id` → `content_keyword_concepts`
- UNIQUE `(section_id, keyword_order)`

Uwaga dokumentacyjna: plik `SOL_migracja-content-keywords.sql` ma komentarz `PRZYGOTOWANA, NIEURUCHOMIONA`, ale późniejszy `SOL_content-keywords-model.md` stwierdza jednoznacznie, że schemat został wdrożony 2026-09-08 i używa markerów:

- `content_keywords_schema_v1 = done`
- `content_keywords_data_v1 = done`

Przy rekonstrukcji należy traktować późniejszą dokumentację i aktualny kod jako nowsze od komentarza w przygotowanym pliku migracji.

## Walencja i biegunowość

`SOL_statystyki-analityczne-struktura-SQL.md` potwierdza odrębne tabele:

- `tag_valence`
- `tag_axis_polarity`

`tag_valence`:

- PK `tag`
- FK → `tag_catalog(tag)`
- `valence` tylko `-1`, `0`, `1` lub NULL
- `status` tylko `resolved`, `contextual`, `unresolved`
- spójność `status` ↔ NULL/NOT NULL dla `valence`

`tag_axis_polarity`:

- PK `(tag, axis_name)`
- FK `tag` → `tag_catalog(tag)`
- FK `axis_name` → `axes(axis_name)`
- `polarity` tylko `-1`, `0`, `1` lub NULL
- analogiczne reguły statusu.

## Dodatkowa tabela używana przez aktualny kod

`content_explorer_app.py` wykonuje JOIN do:

- `content_section_metrics`

oraz używa kolumn:

- `char_count`
- `letter_count`
- `word_count`

Dokładne DDL tabeli `content_section_metrics` nie zostało jeszcze odnalezione w dotychczas przejrzanych plikach. Trzeba je znaleźć przed tworzeniem pełnego schematu Supabase.

## Liczba znanych tabel

Na obecnym etapie dokumentacji znamy co najmniej:

- 20 tabel z głównego `schema.sql`,
- 4 podstawowe tabele `content_*`,
- 3 tabele modelu słów kluczowych,
- `content_section_metrics` używaną przez działający kod.

Czyli co najmniej 28 nazw tabel występujących w obecnym modelu/działającym kodzie.

To NIE jest jeszcze certyfikowana liczba wszystkich aktywnych tabel w Turso. Przed wykonaniem DDL w Supabase trzeba domknąć przegląd późniejszych migracji i plików opisujących rozszerzenia struktury.

## PostgreSQL: zasady translacji

Nie kopiować ślepo DDL SQLite/libSQL.

Przy przepisywaniu do PostgreSQL:

- usunąć `PRAGMA`,
- jawnie dobrać typy PostgreSQL,
- zachować PK, FK, UNIQUE, CHECK, DEFAULT i NULL/NOT NULL,
- zachować semantykę `ON DELETE` i `ON UPDATE`,
- przepisać funkcje lub składnię specyficzną dla SQLite,
- wartości logiczne przechowywane jako `0/1` mogą pozostać integerem dla zgodności albo zostać świadomie zmienione na boolean wyłącznie po decyzji; nie zmieniać semantyki przy okazji kopiowania,
- identyfikatory techniczne należy zachować tak, aby późniejsza kopia danych utrzymała obecne ID.

Na etapie ręcznej kopii preferowana jest zgodność semantyczna z obecną bazą, a nie „upiększanie” modelu.

## Kolejność tworzenia schematu

Planowany sposób:

### Przebieg A

Utworzyć wszystkie tabele wraz z:

- kolumnami,
- typami,
- PRIMARY KEY,
- NOT NULL,
- DEFAULT,
- UNIQUE,
- CHECK.

### Przebieg B

Dodać po utworzeniu wszystkich tabel:

- FOREIGN KEY,
- indeksy.

Dzięki temu zależności między tabelami nie wymuszają ryzykownej kolejności CREATE TABLE.

### Przebieg C

Utworzyć widoki dopiero po tabelach i relacjach.

### Przebieg D

Porównać strukturę Supabase z kompletnym opisem starej bazy.

Dopiero po pozytywnej kontroli zaczyna się kopiowanie danych.

## Czego nie robić

- nie wykonywać automatycznej migracji Turso → PostgreSQL,
- nie ładować całej bazy jednym wielkim dumpem,
- nie traktować starego CSV jako źródła prawdy,
- nie kopiować `schema.sql` do PostgreSQL bez translacji,
- nie zaczynać kopiowania danych przed zamknięciem schematu,
- nie zmieniać modelu danych przy okazji przenoszenia,
- nie usuwać starej bazy po pierwszym udanym imporcie.

## Najbliższy następny krok

Dokończyć rekonstrukcję aktualnego DDL, przede wszystkim:

1. znaleźć wszystkie późniejsze zmiany `content_sections`,
2. znaleźć DDL `content_section_metrics`,
3. przejrzeć migracje z 2026-09-10 i 2026-09-11 pod kątem zmian strukturalnych playlist i tabel zewnętrznych,
4. złożyć jeden docelowy schemat PostgreSQL,
5. dopiero wtedy utworzyć puste tabele w Supabase.

Do chwili wykonania tego kroku: **nie tworzyć jeszcze tabel i nie kopiować danych.**
