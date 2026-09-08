# SOL — model słów kluczowych dla sekcji treści

Status: WDROŻONE / SCHEMAT SQL + SŁOWNIK AKTYWNE
Data: 2026-09-08

Powiązane: `SOL_content-sql-specyfikacja-plan.md`
Migracja: `SOL_migracja-content-keywords.sql`
Marker wdrożenia: `content_keywords_schema_v1 = done`
Marker importu danych: `content_keywords_data_v1 = done`

## Cel

Słowa kluczowe sekcji mają być przechowywane jako uporządkowane pojęcia, a nie jako tekst typu `tag1, tag2, tag3` w jednej komórce.

Najważniejsza zasada:

**jedno pojęcie = jeden `concept_id`, niezależnie od języka.**

Polska i angielska nazwa są nazwami tego samego pojęcia, a nie dwoma niezależnymi tagami.

Przykład:

```text
concept_id = 17
PL: przeciążenie sensoryczne
EN: sensory overload
```

Anchory sekcji pozostają niezależne od tego modelu i nie są tłumaczone.

---

## 1. `content_keyword_concepts`

Jedna pozycja = jedno pojęcie semantyczne niezależne od języka.

```sql
CREATE TABLE content_keyword_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_key TEXT NOT NULL UNIQUE
);
```

### Pola

- `concept_id` — techniczny, stabilny identyfikator pojęcia.
- `concept_key` — stabilny techniczny klucz pojęcia, np. `sensory_overload`, `hyperfocus`, `executive_dysfunction`.

`concept_key` nie jest etykietą dla użytkownika. Służy do stabilnego rozpoznawania pojęcia w kodzie, imporcie i eksporcie.

Przykład:

```text
17 | sensory_overload
18 | executive_dysfunction
19 | hyperfocus
```

---

## 2. `content_keyword_terms`

Jedna pozycja = jedna nazwa językowa danego pojęcia.

```sql
CREATE TABLE content_keyword_terms (
    keyword_id INTEGER PRIMARY KEY,
    concept_id INTEGER NOT NULL,
    lang TEXT NOT NULL,
    keyword TEXT NOT NULL,
    keyword_norm TEXT NOT NULL,
    is_preferred INTEGER NOT NULL DEFAULT 1,

    FOREIGN KEY (concept_id)
        REFERENCES content_keyword_concepts(concept_id),

    CHECK (lang IN ('pl', 'en')),
    CHECK (is_preferred IN (0, 1)),

    UNIQUE (concept_id, lang, keyword_norm)
);
```

### Pola

- `keyword_id` — techniczny identyfikator konkretnej nazwy.
- `concept_id` — pojęcie, którego ta nazwa dotyczy.
- `lang` — język nazwy: obecnie `pl` albo `en`.
- `keyword` — forma prezentowana człowiekowi.
- `keyword_norm` — techniczna forma znormalizowana do wyszukiwania i wykrywania duplikatów.
- `is_preferred` — `1` dla preferowanej nazwy pojęcia w danym języku, `0` dla aliasu / synonimu.

Przykład:

```text
concept 17
PL | przeciążenie sensoryczne | preferred
EN | sensory overload         | preferred
PL | przeciążenie bodźcami    | alias
EN | sensory overstimulation  | alias
```

Dzięki temu synonim nie tworzy nowego pojęcia.

---

## 3. `content_section_keywords`

Tabela łącząca sekcje z pojęciami.

```sql
CREATE TABLE content_section_keywords (
    section_id INTEGER NOT NULL,
    concept_id INTEGER NOT NULL,
    keyword_order INTEGER NOT NULL,

    PRIMARY KEY (section_id, concept_id),

    FOREIGN KEY (section_id)
        REFERENCES content_sections(section_id),

    FOREIGN KEY (concept_id)
        REFERENCES content_keyword_concepts(concept_id),

    UNIQUE (section_id, keyword_order)
);
```

### Pola

- `section_id` — sekcja z `content_sections`.
- `concept_id` — pojęcie przypisane do sekcji.
- `keyword_order` — kolejność / ważność pojęcia dla tej sekcji; `1` oznacza najważniejsze.

Jedno pojęcie może występować w wielu sekcjach, a jedna sekcja może mieć wiele pojęć.

Przykład:

```text
section_id = 123

1 | sensory_overload
2 | sensory_regulation
3 | audhd
4 | stimulus_filtering
```

---

## Relacja między tabelami

```text
content_sections
      |
      | section_id
      v
content_section_keywords
      |
      | concept_id
      v
content_keyword_concepts
      |
      | concept_id
      v
content_keyword_terms
     / \
    PL  EN
```

Przykład logiczny:

```text
sekcja 247
   |
   v
concept_id = 17
   |
   +-- PL: przeciążenie sensoryczne
   +-- EN: sensory overload
```

Nie istnieją dwa niezależne zbiory pojęć PL i EN. Istnieje jeden zbiór pojęć z nazwami w wielu językach.

---

## Indeksy

```sql
CREATE INDEX idx_keyword_terms_norm
ON content_keyword_terms(lang, keyword_norm);

CREATE INDEX idx_section_keywords_concept
ON content_section_keywords(concept_id);

CREATE INDEX idx_section_keywords_section
ON content_section_keywords(section_id);
```

Indeksy obsługują dwa podstawowe kierunki zapytań:

- jakie pojęcia ma dana sekcja;
- które sekcje są przypisane do danego pojęcia.

---

## Reguły danych

1. `concept_id` jest językowo neutralny i stabilny.
2. Sekcja jest łączona z `concept_id`, nie z tekstem słowa kluczowego.
3. Preferowana nazwa PL i EN tego samego pojęcia wskazuje ten sam `concept_id`.
4. Synonimy i aliasy nie tworzą nowych pojęć, jeśli znaczenie jest to samo.
5. `keyword_order` opisuje ważność pojęcia w konkretnej sekcji.
6. Dla jednej sekcji ten sam `concept_id` może wystąpić tylko raz.
7. Anchory pozostają wyłącznie w obecnej formie i nie są częścią modelu tłumaczeń.
8. Model nie modyfikuje treści `content_html`.

---

## Słowa kluczowe dwu- i wielowyrazowe

Jedno pojęcie pozostaje jednym słowem kluczowym niezależnie od liczby wyrazów.

Przykłady:

```text
przeciążenie sensoryczne
funkcje wykonawcze
pamięć robocza
wrażliwość na niesprawiedliwość
potrzeba bycia zrozumianym
```

Takich nazw nie rozbijamy na pojedyncze wyrazy. `pamięć robocza` jest jednym terminem i jednym pojęciem, a nie dwoma słowami kluczowymi `pamięć` + `robocza`.

W `content_keyword_terms`:

```text
keyword      = przeciążenie sensoryczne
keyword_norm = przeciążenie sensoryczne
```

Reguły normalizacji `keyword_norm`:

- małe litery,
- usunięcie spacji z początku i końca,
- wiele kolejnych spacji zamienione na jedną,
- polskie znaki pozostają bez zmian.

Spacje są częścią nazwy słowa kluczowego. Nie zamieniamy ich w `-`, `_` ani inne separatory w `keyword` lub `keyword_norm`.

`concept_key` pozostaje osobnym identyfikatorem technicznym i może używać zapisu technicznego, np.:

```text
keyword:     przeciążenie sensoryczne
concept_key: sensory_overload
```

Długość nazwy nie wpływa na relację z sekcją. `content_section_keywords` nadal przechowuje wyłącznie `concept_id`.

Zasada kanoniczna:

**jedno pojęcie = jeden rekord, bez względu na liczbę słów; spacje są częścią keywordu.**

---

## Obecne kolumny `keywords_pl` i `keywords_en`

W `content_sections` istnieją obecnie kolumny:

```text
keywords_pl
keywords_en
```

Na tym etapie pozostają nietknięte.

Docelowo **nie powinny być źródłem prawdy** dla słów kluczowych. Źródłem prawdy są trzy tabele opisane powyżej.

Jeśli kiedyś będą używane, mogą pełnić rolę cache / gotowego tekstu do API lub eksportu. Nie należy na ich podstawie odtwarzać relacji semantycznych.

---

## Przykładowe zapytania docelowe

Sekcje przypisane do pojęcia:

```sql
SELECT sk.section_id
FROM content_section_keywords sk
WHERE sk.concept_id = ?
ORDER BY sk.section_id;
```

Pojęcia danej sekcji z nazwami PL i EN:

```sql
SELECT
    sk.keyword_order,
    c.concept_id,
    pl.keyword AS keyword_pl,
    en.keyword AS keyword_en
FROM content_section_keywords sk
JOIN content_keyword_concepts c
  ON c.concept_id = sk.concept_id
LEFT JOIN content_keyword_terms pl
  ON pl.concept_id = c.concept_id
 AND pl.lang = 'pl'
 AND pl.is_preferred = 1
LEFT JOIN content_keyword_terms en
  ON en.concept_id = c.concept_id
 AND en.lang = 'en'
 AND en.is_preferred = 1
WHERE sk.section_id = ?
ORDER BY sk.keyword_order;
```

---

## Stan wdrożenia

Schemat został wdrożony do Turso/libSQL 2026-09-08.

Utworzono:

- `content_keyword_concepts`,
- `content_keyword_terms`,
- `content_section_keywords`,
- indeks `idx_keyword_terms_norm`,
- indeks `idx_section_keywords_concept`,
- indeks `idx_section_keywords_section`.

Relacje FK zostały zweryfikowane po migracji.

Marker w `content_meta`:

```text
content_keywords_schema_v1 = done
```

Stan bezpośrednio po wdrożeniu:

- `content_keyword_concepts`: 0 rekordów,
- `content_keyword_terms`: 0 rekordów,
- `content_section_keywords`: 0 rekordów,
- AuDHD: 18 dokumentów, 338 sekcji heading, 338/338 opisów,
- ROSJA: 16 dokumentów, 620 sekcji heading, 9 TOMÓW, 620/620 opisów,
- `content_sections` bez zmian podczas migracji,
- `content_documents` bez zmian podczas migracji.

## Stan po imporcie słownika PL/EN

Import słownika wykonano 2026-09-08.

Marker w `content_meta`:

```text
content_keywords_data_v1 = done
```

Stan po imporcie:

- `content_keyword_concepts`: 544 rekordy,
- `content_keyword_terms`: 1088 rekordów,
- terminy PL: 544,
- terminy EN: 544,
- aliasy (`is_preferred = 0`): 0,
- `content_section_keywords`: 0 rekordów,
- słowa kluczowe nie są jeszcze przypisane do sekcji,
- `content_sections` bez zmian podczas importu,
- `content_documents` bez zmian podczas importu,
- AuDHD: 18 dokumentów, 338 sekcji heading, 338/338 opisów,
- ROSJA: 16 dokumentów, 620 sekcji heading, 9 TOMÓW, 620/620 opisów.
