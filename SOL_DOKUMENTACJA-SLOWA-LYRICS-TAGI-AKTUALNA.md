# SOL — DOKUMENTACJA SŁOWA / LYRICS / TAGI — AKTUALNA

Status: AKTUALNA DOKUMENTACJA OPERACYJNA  
Data: 2026-09-10

## 0. ZASADA PIERWSZEŃSTWA

Ten dokument opisuje aktualny model gałęzi **SŁOWA** projektu `piosenki/`.

Przy konflikcie między starymi CSV/TXT/HTML a działającym kodem i schematem SQL pierwszeństwo mają:

1. bieżący schemat `piosenki/schema.sql`,
2. działający backend `piosenki/app.py`,
3. aktualna publiczna warstwa `piosenki/slowa.html`,
4. dopiero potem starsze dokumenty operacyjne i pliki importowe.

Stare CSV/TXT pozostają ważnym źródłem historii, importów i definicji, ale nie należy z nich rekonstruować bieżącego stanu Turso, jeśli istnieje nowszy stan SQL.

---

## 1. MIEJSCE W ARCHITEKTURZE

`piosenki/` ma dwa duże podsystemy:

- **SŁOWA** — teksty, tagi, semantyka, czas zdarzeniowy i analizy;
- **AUDIO** — sygnał, cechy akustyczne, dopasowanie plików audio i mapa brzmienia.

AUDIO ma własną dokumentację:

`SOL_DOKUMENTACJA-AUDIO-AKTUALNA.md`

Ten plik dotyczy wyłącznie gałęzi SŁOWA / LYRICS / TAGI.

---

## 2. GŁÓWNY PRZEPŁYW DANYCH

```text
middle_end.utwu_id
      |
      | 0..1 lyrics_id na rekord utworu
      v
lyrics
      |
      | 1 -> 0..N
      v
tag_snapshots
      |
      | tagi zapisane w polu tags
      v
tag_catalog
      |
      +--> tag_group --> tag_groups
      |
      +--> tag_axis --> axes --> families
      |
      +--> tag_valence
      |
      +--> tag_axis_polarity
```

Najważniejsze rozdzielenie:

- `utwu_id` identyfikuje rekord utworu / nagrania w `middle_end`;
- `lyrics_id` identyfikuje tekst;
- tagowanie jest przypisane do **`lyrics_id`**, nie bezpośrednio do `utwu_id`;
- ten sam `lyrics_id` może być wskazywany przez więcej niż jeden rekord `middle_end`;
- jeden `lyrics_id` może mieć wiele historycznych snapshotów tagowania.

---

## 3. `lyrics`

Aktualny schemat:

```sql
lyrics(
    lyrics_id TEXT PRIMARY KEY,
    lyrics_text TEXT NOT NULL
)
```

`lyrics_id` jest stabilnym identyfikatorem tekstu.

`lyrics_text` przechowuje treść przypisaną do tego identyfikatora.

Relacja z `middle_end`:

```text
middle_end N -> 0..1 lyrics
lyrics 1 -> 0..N middle_end
```

`middle_end.lyrics_id` jest kluczem obcym do `lyrics.lyrics_id`.

---

## 4. `middle_end` A LYRICS

Dla gałęzi SŁOWA istotne są przede wszystkim:

```text
utwu_id
lyrics_id
spotify_order
match_status
match_candidates
match_note
lyrics_status
```

`utwu_id` pozostaje kanonicznym identyfikatorem rekordu utworu.

`lyrics_id` wskazuje tekst, jeśli tekst został przypisany.

`spotify_order` daje naturalną kolejność zdarzeń używaną później w analizach czasu.

### `lyrics_status`

W istniejącej dokumentacji używane są statusy:

- `full` — pełny tekst przypisany do konkretnej wersji;
- `canonicaltext` — kanoniczny / bazowy tekst dzieła, niekoniecznie zgodny 1:1 z konkretnym nagraniem;
- `partial` — tylko część tekstu;
- `paraphase` — robocza parafraza sensu, nie transkrypcja 1:1;
- `instrumental` — brak tekstu, bo nagranie jest instrumentalne;
- `missing` — tekst nie został znaleziony lub rozstrzygnięty.

Zgodnie z istniejącą logiką:

- `full`, `canonicaltext`, `partial`, `paraphase` wymagają `lyrics_id`;
- `instrumental`, `missing` oznaczają brak `lyrics_id`.

Uwaga: zapis `paraphase` jest zachowany dokładnie tak, jak występuje w istniejącej dokumentacji. Nie poprawiać go samowolnie w danych.

---

## 5. `tag_snapshots`

Aktualny schemat:

```sql
tag_snapshots(
    lyrics_id TEXT REFERENCES lyrics(lyrics_id),
    tagged_at TEXT,
    tags TEXT
)
```

Jeden rekord oznacza **jeden snapshot tagowania jednego `lyrics_id`**.

`lyrics_id` nie jest tutaj unikalny. Historia snapshotów może więc zawierać wiele zapisów dla tego samego tekstu.

Nowy snapshot nie powinien automatycznie nadpisywać starego bez wyraźnego polecenia.

---

## 6. `tag_catalog`

Aktualny schemat:

```sql
tag_catalog(
    tag TEXT PRIMARY KEY,
    definition TEXT
)
```

Jedna pozycja = jeden dozwolony tag i jego definicja.

Tag użyty w snapshotach powinien istnieć w katalogu tagów.

Historycznym/importowym źródłem definicji jest:

`piosenki/sol-definicje-tagow-CSV-v01-02.csv`

Bieżącego stanu SQL nie należy jednak rekonstruować wyłącznie z tego CSV bez sprawdzenia aktualnego schematu/danych.

---

## 7. GRAMATYKA POLA `tags`

Udokumentowany format snapshotu:

```text
tag:kwalifikator1|kwalifikator2; drugi-tag:kwalifikator1
```

Udokumentowane kwalifikatory siły:

```text
bardzo
troche
ociupinke
```

Nazwy tagów mają postać techniczną:

```text
^[a-z0-9]+(?:-[a-z0-9]+)*$
```

Czyli:

- małe litery ASCII,
- cyfry,
- pojedynczy minus jako separator,
- bez spacji,
- bez `_`, `/`, kropek i polskich znaków.

To jest konwencja danych. Sam schemat SQL tabeli `tag_snapshots` nie rozbija pola `tags` na osobne rekordy.

---

## 8. ONTOLOGIA TAGÓW

Aktualna warstwa ontologiczna składa się z:

- `families`,
- `tag_groups`,
- `axes`,
- `tag_group`,
- `tag_axis`.

Historyczny plik opisujący tę ontologię:

`piosenki/sol-ontologia-tagow-TXT-v01-03.txt`

### `families`

```sql
families(
    family_name TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    color_hex TEXT NOT NULL,
    description TEXT NOT NULL,
    sort_order INTEGER NOT NULL UNIQUE
)
```

Udokumentowane jest 5 rodzin:

- LAPIS,
- BUTELKOWA ZIELEŃ,
- ŚLIWKA,
- OCHRA / STARE ZŁOTO,
- TERAKOTA.

### `tag_groups`

```sql
tag_groups(
    group_name TEXT PRIMARY KEY,
    label TEXT NOT NULL
)
```

Udokumentowanych jest 12 grup.

Grupy są niezależne od rodzin. Tag może należeć do wielu grup.

### `axes`

```sql
axes(
    axis_name TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    description TEXT NOT NULL,
    family_name TEXT NOT NULL REFERENCES families(family_name),
    sort_order INTEGER NOT NULL UNIQUE
)
```

Udokumentowanych jest 17 osi.

Każda oś należy do dokładnie jednej rodziny.

### `tag_group`

```sql
tag_group(
    tag TEXT NOT NULL REFERENCES tag_catalog(tag),
    group_name TEXT NOT NULL REFERENCES tag_groups(group_name),
    PRIMARY KEY(tag, group_name)
)
```

Relacja wiele-do-wielu:

```text
tag_catalog N <-> M tag_groups
```

### `tag_axis`

```sql
tag_axis(
    tag TEXT NOT NULL REFERENCES tag_catalog(tag),
    axis_name TEXT NOT NULL REFERENCES axes(axis_name),
    PRIMARY KEY(tag, axis_name)
)
```

Relacja wiele-do-wielu:

```text
tag_catalog N <-> M axes
```

Nie istnieje osobna tabela `tag_family`.

Rodzina taga wynika pośrednio:

```text
tag -> tag_axis -> axes -> families
```

---

## 9. WALENCJA

Walencja jest osobną warstwą semantyczną.

Aktualny schemat:

```sql
tag_valence(
    tag TEXT PRIMARY KEY REFERENCES tag_catalog(tag),
    valence INTEGER,
    status TEXT NOT NULL
)
```

Dozwolone wartości:

```text
-1
 0
+1
NULL
```

Status:

```text
resolved
contextual
unresolved
```

Reguła:

- `resolved` -> `valence` musi mieć -1, 0 lub +1;
- `contextual` / `unresolved` -> `valence` pozostaje NULL.

Walencja nie jest tym samym co kierunek ani biegun osi.

---

## 10. BIEGUNOWOŚĆ TAGA NA OSI

Aktualny schemat:

```sql
tag_axis_polarity(
    tag TEXT NOT NULL REFERENCES tag_catalog(tag),
    axis_name TEXT NOT NULL REFERENCES axes(axis_name),
    polarity INTEGER,
    status TEXT NOT NULL,
    PRIMARY KEY(tag, axis_name)
)
```

Dozwolone wartości `polarity`:

```text
-1
 0
+1
NULL
```

Status działa analogicznie jak w `tag_valence`.

Najważniejsze: biegunowość należy do **pary `(tag, axis)`**, nie do samego taga.

Ten sam tag może więc mieć różne znaczenie kierunkowe na różnych osiach.

---

## 11. CO JEST FAKTEM, A CO INTERPRETACJĄ

Warstwa SQL przechowuje fakty i jawne przypisania:

- tekst,
- identyfikator tekstu,
- snapshot tagowania,
- definicję taga,
- przynależność do grup,
- przynależność do osi,
- rodzinę osi,
- walencję i jej status,
- biegunowość `(tag, axis)` i jej status.

Analizy statystyczne są liczone po stronie Python/Flask.

Nie należy mieszać:

```text
częstość wystąpień
walencja
biegunowość osi
kierunek zmiany w czasie
współwystępowanie
```

To są różne warstwy.

---

## 12. CZAS ZDARZENIOWY

Gałąź SŁOWA używa `middle_end.spotify_order` jako osi czasu zdarzeniowego.

To nie jest czas kalendarzowy.

`spotify_order = 1` oznacza najnowszy element zbioru, a większe wartości oznaczają coraz dalszą przeszłość w kolejności polubień.

Analizy używają m.in. przesuwanych okien:

```text
1–80
31–110
61–140
...
```

Dzięki temu można analizować zmianę profilu tagów, osi i rodzin w kolejnych fragmentach historii zbioru.

---

## 13. WARSTWA ANALITYCZNA

Publiczna strona:

`piosenki/slowa.html`

prowadzi do analiz serwerowych na Renderze, m.in.:

```text
/statystyki/13
/statystyki/czas
/statystyki/relacje
/statystyki/hipotezy
/statystyki/kierunek
```

Backend:

`piosenki/app.py`

czyta dane z Turso/libSQL i oblicza analizy w Pythonie.

Warstwa statystyczna nie powinna zmieniać danych źródłowych tylko dlatego, że renderuje analizę.

---

## 14. PUBLICZNE API

`GET /api/piosenki`

zwraca obecnie m.in.:

- `middle_end`,
- `tag_snapshots`,
- `tag_catalog`,
- `families`,
- `tag_groups`,
- `axes`,
- `tag_group`,
- `tag_axis`,
- listę `lyrics_id`.

Endpoint jest przeznaczony do odczytu.

Nie należy traktować publicznego API jako sposobu modyfikacji systemu tagów.

---

## 15. ZASADY TAGOWANIA

Z istniejącej dokumentacji operacyjnej wynikają następujące reguły:

1. Tagujemy na poziomie `lyrics_id`.
2. Każdy tekst trzeba czytać osobno i w całości.
3. Nie tagujemy na podstawie tytułu, wykonawcy ani podobnego utworu.
4. Nie kopiujemy automatycznie poprzednich tagów.
5. Nie wprowadzamy nowej heurystyki bez jawnej decyzji.
6. Nowe tagowanie tworzy nowy snapshot.
7. Historycznych snapshotów nie nadpisujemy bez wyraźnego polecenia.
8. Każdy tag musi istnieć w `tag_catalog`.
9. Jeśli nowy tag ma wejść do systemu, trzeba określić jego relacje ontologiczne, a nie tylko dopisać nazwę do tekstu.

---

## 16. DODAWANIE NOWEGO TAGA

Docelowy porządek:

1. dodać tag i definicję do `tag_catalog`;
2. sprawdzić poprawność i unikalność nazwy;
3. przypisać co najmniej jedną grupę w `tag_group`;
4. przypisać co najmniej jedną oś w `tag_axis`;
5. jeśli potrzebne, uzupełnić `tag_valence`;
6. jeśli potrzebne, uzupełnić `tag_axis_polarity` dla odpowiednich osi;
7. dopiero potem używać taga w nowych snapshotach.

Nie dodawać `tag_family`. Rodzina wynika z osi.

---

## 17. ŹRÓDŁA HISTORYCZNE / IMPORTOWE W `piosenki/`

Istnieją m.in.:

- `sol-middleend-CSV-v08-11.csv`,
- `sol-piosenki-slowa-CSV-v07-00.csv`,
- `sol-piosenki-slowa-kontynuacja-CSV-v01-08.csv`,
- `sol-piosenki-tagi-CSV-v09-14.csv`,
- `sol-definicje-tagow-CSV-v01-02.csv`,
- `sol-ontologia-tagow-TXT-v01-03.txt`,
- `sol-o-co-kaman-HTML-v01-00.html`.

Są ważne jako dokumentacja historii i źródła importów.

**Nie traktować ich automatycznie jako bieżącego stanu bazy.**

Bieżący stan systemu operacyjnego jest w Turso/SQL i kodzie obsługującym ten SQL.

---

## 18. CO NALEŻY TRAKTOWAĆ JAKO ODDZIELNE PODSYSTEMY

Nie mieszać w jednej operacji:

### SŁOWA

- `lyrics`,
- `middle_end.lyrics_id`,
- `tag_snapshots`,
- `tag_catalog`,
- ontologia tagów,
- walencja,
- biegunowość,
- statystyki tekstowe.

### AUDIO

- `audio`,
- `audio_middle_end`,
- `audio_match_details`,
- `audio_feature_snapshots`,
- pola audio w `middle_end`.

Łączy je `middle_end`, ale są to dwa różne systemy danych i dwie różne dokumentacje.

---

## 19. NAJKRÓTSZY MODEL

```text
UTWÓR
middle_end.utwu_id
    |
    +--> lyrics_id --> LYRICS --> SNAPSHOTY TAGÓW
    |                              |
    |                              +--> TAGI
    |                                   |
    |                                   +--> GRUPY
    |                                   +--> OSIE --> RODZINY
    |                                   +--> WALENCJA
    |                                   +--> BIEGUNOWOŚĆ NA OSI
    |
    +--> audio_id --> osobny podsystem AUDIO
```

**SŁOWA opisują znaczenie tekstu. AUDIO opisuje sygnał. `middle_end` jest mostem, nie miejscem do mieszania obu ontologii.**
