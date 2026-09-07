# SOL — struktura SQL dla walencji i biegunowości

Stan: 2026-09-07

Ten dokument zapisuje decyzję projektową dla dwóch nowych warstw semantycznych. Zastępuje wcześniejsze założenie, że walencja i biegunowość mają pozostać wyłącznie w pliku JSON.

## 1. Walencja

Walencja ma własną tabelę. Nie dokładamy jej do `tag_catalog` ani do `tag_axis`.

```sql
CREATE TABLE tag_valence (
    tag TEXT PRIMARY KEY,
    valence INTEGER,
    status TEXT NOT NULL,
    FOREIGN KEY (tag) REFERENCES tag_catalog(tag),
    CHECK (valence IN (-1, 0, 1) OR valence IS NULL),
    CHECK (status IN ('resolved', 'contextual', 'unresolved')),
    CHECK (
        (status = 'resolved' AND valence IS NOT NULL)
        OR
        (status IN ('contextual', 'unresolved') AND valence IS NULL)
    )
);
```

Znaczenie `valence`:

- `-1` = nieprzyjemna,
- `0` = neutralna,
- `1` = przyjemna,
- `NULL` = brak jednej stałej wartości.

Znaczenie `status`:

- `resolved` = walencja rozstrzygnięta,
- `contextual` = zależy od kontekstu,
- `unresolved` = jeszcze nierozstrzygnięta.

Tabela nie ma pola `note`.

## 2. Biegunowość tagu na osi

Biegunowość nie jest własnością samego tagu. Jest własnością pary `(tag, axis_name)`, ponieważ ten sam tag może mieć inne znaczenie kierunkowe na różnych osiach.

```sql
CREATE TABLE tag_axis_polarity (
    tag TEXT NOT NULL,
    axis_name TEXT NOT NULL,
    polarity INTEGER,
    status TEXT NOT NULL,
    PRIMARY KEY (tag, axis_name),
    FOREIGN KEY (tag) REFERENCES tag_catalog(tag),
    FOREIGN KEY (axis_name) REFERENCES axes(axis_name),
    CHECK (polarity IN (-1, 0, 1) OR polarity IS NULL),
    CHECK (status IN ('resolved', 'contextual', 'unresolved')),
    CHECK (
        (status = 'resolved' AND polarity IS NOT NULL)
        OR
        (status IN ('contextual', 'unresolved') AND polarity IS NULL)
    )
);
```

Znaczenie `polarity`:

- `-1` = jeden biegun osi,
- `0` = środek / brak kierunku na tej osi,
- `1` = drugi biegun osi,
- `NULL` = brak jednej stałej wartości.

## 3. Rozdzielenie odpowiedzialności

```text
tag_catalog         co oznacza tag
tag_axis            do jakich osi należy tag
tag_valence         jaka jest walencja tagu
tag_axis_polarity   jaki biegun ma tag na konkretnej osi
```

Nie tworzymy ogólnej tabeli typu `tag_properties`. Walencja i biegunowość mają różną semantykę i różne klucze, więc pozostają oddzielone.

## 4. Stan obecny

Aktualna klasyfikacja walencji istnieje jeszcze w:

```text
dane-analityczne/tag-wartosci.json
```

JSON jest obecnie źródłem roboczym dla działających analiz. Docelowo dane walencji mają zostać przeniesione do `tag_valence`, a biegunowość do `tag_axis_polarity`. Samo przeniesienie danych należy wykonać dopiero po sprawdzeniu aktualnego schematu Turso i relacji kluczy obcych.
