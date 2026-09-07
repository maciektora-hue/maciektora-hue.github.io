# SOL — SQL jako źródło prawdy dla map treści

Status: SPECYFIKACJA V1
Data: 2026-09-07

## 1. CEL

Przenieść strukturalne mapy treści ROSJA i AuDHD z roli „danych trzymanych w TSV” do wspólnego modelu w istniejącej bazie Turso/libSQL.

Po migracji:

- SQL jest źródłem prawdy dla dokumentów, sekcji, anchorów i opisów;
- TSV nie jest magazynem głównym;
- TSV może być generowany jako eksport kompatybilności;
- Flask/API i strony HTML czytają dane z SQL/widoków;
- istniejące pliki źródłowe HTML pozostają niezależnymi dokumentami i nie są przez tę migrację kasowane ani przepisywane;
- pierwszy import z TSV jest jednorazowy; kolejne restarty/deploye NIE nadpisują SQL danymi z TSV.

## 2. ZAKRES V1

Źródła pierwszego importu:

1. ROSJA: `rosja/SOL_mapa-sekcji-z-opisami.tsv`
   - 16 dokumentów
   - 620 sekcji H1–H6
   - 620 opisów

2. AuDHD: `audhd/SOL_mapa-sekcji-i-anchorow-audhd.tsv`
   - 18 dokumentów
   - 338 sekcji H1–H6
   - opisy sekcji obecnie nie są częścią źródłowego TSV

Razem oczekiwane po imporcie V1:

- kolekcje: 2
- dokumenty: 34
- sekcje typu `heading`: 958
- ROSJA: 620
- AuDHD: 338

Poza V1, ale model ma to obsłużyć:

- dodatkowe poziomy semantyczne niebędące H1–H6, np. TOMY w A1;
- nowe kolekcje;
- późniejsze dopisywanie opisów AuDHD;
- eksporty TSV/CSV;
- dodatkowe widoki analityczne.

## 3. MODEL DANYCH

### 3.1. `content_meta`

Techniczna tabela wersji i stanu migracji.

| pole | typ | NULL | klucz | znaczenie |
|---|---|---:|---|---|
| `key` | TEXT | NIE | PK | nazwa ustawienia/metadanej |
| `value` | TEXT | NIE |  | wartość |

W V1 wymagany wpis po udanym pierwszym imporcie:

- `content_initial_import_v1 = done`

Brak wpisu + niepuste tabele danych oznacza STOP, a nie automatyczne nadpisanie danych.

### 3.2. `content_collections`

Jedna pozycja = jedna logiczna kolekcja dokumentów.

| pole | typ | NULL | klucz | znaczenie |
|---|---|---:|---|---|
| `collection_id` | TEXT | NIE | PK | stabilny identyfikator, np. `rosja`, `audhd` |
| `label` | TEXT | NIE |  | etykieta dla człowieka |
| `sort_order` | INTEGER | NIE | UNIQUE | kolejność kolekcji |

V1:

- `rosja`, label `ROSJA`, sort_order 10
- `audhd`, label `AuDHD`, sort_order 20

### 3.3. `content_documents`

Jedna pozycja = jeden dokument merytoryczny.

| pole | typ | NULL | klucz/reguła | znaczenie |
|---|---|---:|---|---|
| `document_id` | INTEGER | NIE | PK | techniczny wewnętrzny ID SQL |
| `collection_id` | TEXT | NIE | FK → `content_collections` | kolekcja |
| `document_code` | TEXT | NIE | UNIQUE w kolekcji | np. `A1`, `D4`, `AU16` |
| `source_filename` | TEXT | NIE | UNIQUE w kolekcji | nazwa źródłowego HTML |
| `document_title` | TEXT | NIE |  | tytuł dokumentu |
| `canonical_url` | TEXT | NIE |  | URL używany do deep-linków |
| `source_url` | TEXT | NIE |  | bezpośredni URL źródłowego HTML |
| `sort_order` | INTEGER | NIE | UNIQUE w kolekcji | kolejność dokumentu |

Reguły URL V1:

- ROSJA: `canonical_url` = obecne `url_stabilny`; `source_url` = bezpośredni URL GitHub Pages do pliku z `dokument_plik`;
- AuDHD: obecne `url_zrodlowy` trafia do `source_url`; w V1 `canonical_url = source_url`, dopóki nie zostanie osobno przypisana kompletna mapa stabilnych URL-i.

### 3.4. `content_sections`

Jedna pozycja = jeden węzeł struktury dokumentu.

| pole | typ | NULL | klucz/reguła | znaczenie |
|---|---|---:|---|---|
| `section_id` | INTEGER | NIE | PK | techniczny ID SQL |
| `document_id` | INTEGER | NIE | FK → `content_documents`, ON DELETE CASCADE | dokument |
| `parent_section_id` | INTEGER | TAK | FK → `content_sections`, ON DELETE SET NULL | jawny rodzic w strukturze |
| `section_kind` | TEXT | NIE | CHECK | `heading`, `volume` albo `other` |
| `heading_level` | INTEGER | TAK | CHECK | 1–6 tylko dla `heading`; NULL dla innych rodzajów |
| `depth` | INTEGER | NIE | CHECK >= 1 | głębokość strukturalna |
| `section_order` | INTEGER | NIE | UNIQUE w dokumencie | kolejność sekcji |
| `section_title` | TEXT | NIE |  | tytuł sekcji |
| `anchor` | TEXT | TAK | UNIQUE w dokumencie | anchor bez `#`; NULL dopuszczony dla sekcji jeszcze niezakotwiczonych |
| `description` | TEXT | TAK |  | krótki opis sekcji |

Reguła `section_kind` / `heading_level`:

- `heading` → `heading_level` musi być 1–6;
- `volume` lub `other` → `heading_level` musi być NULL.

V1 importuje 958 rekordów jako `section_kind = heading`.

`parent_section_id` jest wyliczany przy imporcie na podstawie `depth` i kolejności. Dla każdego węzła rodzicem jest najbliższy wcześniejszy węzeł o mniejszej głębokości. Brak takiego węzła → NULL.

## 4. CO JEST PRZECHOWYWANE, A CO WYLICZANE

Przechowywane:

- kod dokumentu;
- nazwa pliku;
- tytuł dokumentu;
- URL kanoniczny i źródłowy;
- rodzaj sekcji;
- H1–H6 jako liczba 1–6;
- głębokość;
- kolejność;
- tytuł sekcji;
- anchor;
- opis;
- jawne rodzicielstwo.

NIE przechowujemy jako danych podstawowych:

- `anchor_status`;
- `deep_link`;
- tekstowego `H1`, `H2` itd.

Są wyliczane w widokach:

- `anchor_status = OK`, gdy anchor jest niepusty; w przeciwnym razie `BRAK`;
- `deep_link = canonical_url || '#' || anchor`, gdy anchor istnieje;
- `poziom = 'H' || heading_level` dla sekcji typu `heading`.

## 5. MAPOWANIE TSV → SQL

### 5.1. ROSJA

Źródło: `rosja/SOL_mapa-sekcji-z-opisami.tsv`

| TSV | SQL |
|---|---|
| `dokument_kod` | `content_documents.document_code` |
| `dokument_plik` | `content_documents.source_filename` |
| `dokument_tytul` | `content_documents.document_title` |
| `url_stabilny` | `content_documents.canonical_url` |
| `poziom` | `content_sections.heading_level` po usunięciu `H` |
| `glebokosc` | `content_sections.depth` |
| `kolejnosc` | `content_sections.section_order` |
| `sekcja_tytul` | `content_sections.section_title` |
| `anchor` | `content_sections.anchor` |
| `opis` | `content_sections.description` |
| `anchor_status` | NIE IMPORTOWAĆ; wyliczać |
| `deep_link` | NIE IMPORTOWAĆ; wyliczać |

`source_url` jest wyliczany z `dokument_plik` jako bezpośredni URL pliku w `/rosja/`.

### 5.2. AuDHD

Źródło: `audhd/SOL_mapa-sekcji-i-anchorow-audhd.tsv`

| TSV | SQL |
|---|---|
| `dokument_kod` | `content_documents.document_code` |
| `dokument_plik` | `content_documents.source_filename` |
| `dokument_tytul` | `content_documents.document_title` |
| `url_zrodlowy` | `content_documents.source_url` oraz tymczasowo `canonical_url` |
| `poziom` | `content_sections.heading_level` po usunięciu `H` |
| `glebokosc` | `content_sections.depth` |
| `kolejnosc` | `content_sections.section_order` |
| `sekcja_tytul` | `content_sections.section_title` |
| `anchor` | `content_sections.anchor` |
| `anchor_status` | NIE IMPORTOWAĆ; wyliczać |
| `deep_link` | NIE IMPORTOWAĆ; wyliczać |
| opis | w V1 NULL |

## 6. WIDOKI V1

### 6.1. `v_content_structure`

Pełna wspólna struktura wszystkich rodzajów sekcji.

Kolumny w kolejności:

1. `collection_id`
2. `dokument_kod`
3. `dokument_plik`
4. `dokument_tytul`
5. `canonical_url`
6. `source_url`
7. `section_kind`
8. `poziom`
9. `glebokosc`
10. `kolejnosc`
11. `sekcja_tytul`
12. `anchor`
13. `anchor_status`
14. `deep_link`
15. `opis`
16. `parent_section_id`
17. `document_sort_order`

### 6.2. `v_content_map`

Jak `v_content_structure`, ale tylko `section_kind = heading`.

### 6.3. `v_content_human`

Widok do interfejsów dla człowieka. Kolumny treści najpierw, techniczne na końcu:

1. `collection_id`
2. `sekcja_tytul`
3. `anchor`
4. `anchor_status`
5. `deep_link`
6. `opis`
7. `dokument_tytul`
8. `canonical_url`
9. `dokument_kod`
10. `poziom`
11. `glebokosc`
12. `kolejnosc`
13. `dokument_plik`
14. `source_url`
15. `document_sort_order`

### 6.4. `v_rosja_mapa_sekcji`

Kompatybilny logicznie odpowiednik obecnego TSV ROSJA. Filtr `collection_id = 'rosja'`.

### 6.5. `v_audhd_mapa_sekcji`

Kompatybilny logicznie odpowiednik obecnego TSV AuDHD. Filtr `collection_id = 'audhd'`.

## 7. API V1

Read-only.

### `GET /api/content`

Lista kolekcji + liczba dokumentów i sekcji.

### `GET /api/content/<collection_id>`

Zwraca rekordy z `v_content_human` dla kolekcji, w kolejności dokumentów i sekcji.

### `GET /api/content/<collection_id>/status`

Zwraca co najmniej:

- `documents`;
- `sections`;
- `anchors_ok`;
- `anchors_missing`;
- `descriptions_present`;
- `descriptions_missing`.

V1 jest tylko do odczytu przez publiczne API.

## 8. PLAN MIGRACJI KROK PO KROKU

### KROK 0 — stan wejściowy

- NIE kasować TSV;
- NIE zmieniać źródłowych HTML-i;
- potwierdzić aktualne liczby ROSJA 620 i AuDHD 338;
- potwierdzić działanie Turso i Render.

STOP jeśli liczby wejściowe się nie zgadzają.

### KROK 1 — model SQL

- utworzyć `content_meta`;
- utworzyć `content_collections`;
- utworzyć `content_documents`;
- utworzyć `content_sections`;
- utworzyć indeksy i widoki V1.

Wyłącznie operacje addytywne. Żadnego DROP istniejących tabel piosenek.

### KROK 2 — jednorazowy importer

- importer czyta dokładnie dwa wskazane TSV;
- w jednej transakcji importuje 2 kolekcje, 34 dokumenty i 958 sekcji;
- wylicza rodziców;
- waliduje liczby i unikalność;
- dopiero po pełnym sukcesie zapisuje `content_initial_import_v1 = done`;
- COMMIT następuje dopiero po wszystkich walidacjach.

STOP + ROLLBACK przy dowolnym błędzie.

### KROK 3 — odcięcie TSV jako źródła prawdy

Po `content_initial_import_v1 = done`:

- aplikacja NIE importuje TSV przy kolejnych startach;
- SQL jest źródłem prawdy;
- TSV zostają jako archiwum/eksport przejściowy.

### KROK 4 — read-only API

Dodać trzy endpointy z sekcji 7.

Sprawdzić:

- ROSJA: 16 dokumentów / 620 sekcji;
- AuDHD: 18 dokumentów / 338 sekcji;
- 958 anchorów OK;
- ROSJA 620 opisów;
- AuDHD 0 opisów w V1.

### KROK 5 — przełączenie viewerów

Najpierw ROSJA, potem AuDHD.

- viewer pobiera dane z API/SQL zamiast TSV;
- wygląd i zwijanie pozostają niezależne od magazynu danych;
- po przełączeniu porównać liczbę i klucze rekordów 1:1.

STOP przy jakiejkolwiek różnicy.

### KROK 6 — eksport TSV z SQL

Dodać mechaniczny eksport:

- `v_rosja_mapa_sekcji` → TSV kompatybilny z dotychczasowym formatem;
- `v_audhd_mapa_sekcji` → TSV kompatybilny z dotychczasowym formatem.

Od tego momentu kierunek jest:

SQL → VIEW → API / HTML / TSV

Nie:

TSV → SQL przy każdym uruchomieniu.

### KROK 7 — TOMY A1 i inne węzły semantyczne

Dodać TOMY A1 jako `section_kind = volume`, `heading_level = NULL`.

Następnie przepiąć odpowiednie rozdziały A1 przez `parent_section_id` pod TOMY.

To nie zmienia H1–H6 ani anchorów dokumentu.

### KROK 8 — dalsze opisy AuDHD

Opisy dopisywać bezpośrednio do `content_sections.description`.

Nie tworzyć 18 osobnych TSV jako głównego magazynu opisów.

## 9. WARUNKI SUKCESU V1

Migracja V1 jest zakończona dopiero gdy jednocześnie:

- `content_initial_import_v1 = done`;
- kolekcje = 2;
- dokumenty = 34;
- sekcje = 958;
- ROSJA = 620;
- AuDHD = 338;
- brak duplikatów `(document_id, section_order)`;
- brak duplikatów niepustych `(document_id, anchor)`;
- ROSJA: 620 niepustych anchorów i 620 opisów;
- AuDHD: 338 niepustych anchorów;
- API zwraca te same liczby;
- istniejące tabele piosenek działają bez zmian;
- obecne endpointy piosenek i statystyk nadal działają.

## 10. ZASADA BEZPIECZEŃSTWA

Każdy etap jest addytywny i odwracalny do momentu przełączenia viewerów.

Nie usuwamy obecnych TSV ani starych ścieżek w tym etapie.
Nie wykonujemy destrukcyjnych migracji istniejących tabel piosenek.
Nie zapisujemy tokenów Turso w repozytorium.
