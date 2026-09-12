# SOL — ZADANIA SQL / SUPABASE

Data: 2026-09-12

## Zasady

- pracujemy po jednej tabeli naraz,
- priorytet mają tabele poniżej 1000 wierszy,
- dane bierzemy wyłącznie z żywej starej bazy SQL,
- nie używamy CSV, TSV, HTML, danych z GitHuba ani Library jako źródła danych,
- po każdej tabeli: zapis do Supabase, COUNT, kontrola kluczy i zawartości.

## DO ZROBIENIA

### 1. `playlist_tag_def` — UZUPEŁNIĆ

Tabela jest potrzebna, ale obecny stan jest niedokończony.

W starej bazie jest tylko 1 rekord, natomiast powinno być kilka definicji tagów więcej.

Najpierw trzeba:

1. ustalić pełny zestaw potrzebnych definicji tagów playlist,
2. uzupełnić `playlist_tag_def`,
3. sprawdzić zgodność z polami `playlist.tags` i `playlist.playlist_tags`,
4. dopiero wtedy uznać tabelę za gotową.

### 2. Kontynuować migrację małych tabel

Po jednej tabeli, wyłącznie te mające mniej niż 1000 wierszy.

### 3. Ponownie zweryfikować `families`

5 rekordów jest już w Supabase, ale wcześniejsze źródło nie spełnia obecnej zasady źródeł. Porównać bezpośrednio z żywym starym SQL.

### 4. Ponownie zweryfikować `tag_groups`

12 rekordów jest już w Supabase, ale wcześniejsze źródło nie spełnia obecnej zasady źródeł. Porównać bezpośrednio z żywym starym SQL.

### 5. Ponownie zweryfikować `audio`

856 rekordów jest już w Supabase, ale wcześniejszy transport używał TSV. Porównać bezpośrednio SQL → SQL przed uznaniem migracji za zakończoną.

## ZROBIONE

### `content_collections`

2 rekordy skopiowane z żywej starej bazy Turso do Supabase i sprawdzone po zapisie.

## NA PÓŹNIEJ — 1000+ WIERSZY

- `external_track` — 1033,
- `content_keyword_terms` — 1214,
- `content_section_keywords` — 1298,
- `playlist_item` — 2403.
