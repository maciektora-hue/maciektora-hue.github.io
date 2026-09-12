# Import Supabase — wynik końcowy

Data: 2026-09-12

## Wynik

- Tabele źródłowe: 27
- Tabele zgodne liczbowo: 27/27
- Wiersze w źródle: 15071
- Wiersze w Supabase: 15071
- Różnica: 0

## Faktyczny stan tabel w Supabase

- `audio` — 856
- `audio_feature_snapshots` — 856
- `audio_match_details` — 182
- `audio_middle_end` — 191
- `axes` — 17
- `content_collections` — 2
- `content_documents` — 34
- `content_keyword_concepts` — 602
- `content_keyword_terms` — 1214
- `content_meta` — 4
- `content_section_keywords` — 1298
- `content_section_metrics` — 958
- `content_sections` — 967
- `external_track` — 1033
- `external_track_utwu` — 937
- `families` — 5
- `lyrics` — 882
- `middle_end` — 977
- `playlist` — 17
- `playlist_item` — 2403
- `playlist_tag_def` — 1
- `tag_axis` — 329
- `tag_catalog` — 165
- `tag_group` — 165
- `tag_groups` — 12
- `tag_snapshots` — 888
- `tag_valence` — 76

## Co się wcześniej wysypywało

Problem nie był jedną rzeczą. Najbardziej upierdliwe były różnice pomiędzy SQL-em z SQLite a PostgreSQL-em, zwłaszcza:

- wielokrotne cudzysłowy, apostrofy i escape'y wewnątrz długich tekstów i HTML,
- sekwencje typu `\"` i podobne zapisy tekstowe,
- sqlite'owe `char(10)` zamiast postgresowego `chr(10)`,
- bardzo długie pola tekstowe z HTML i znakami wyglądającymi jak koniec polecenia,
- w `playlist_item` i `content_sections` kolejność kolumn w istniejącej tabeli PostgreSQL różniła się od kolejności wartości w źródłowym pliku SQLite, więc trzeba było jawnie wskazać kolumny.

Czyli tak: potrójne/wielokrotne cudzysłowy i podobne pierdoły były częścią problemu, ale nie jedyną. Każdy dialekt SQL ma własne drobne pomysły na to, jak utrudnić człowiekowi życie.

Osobno zdarzały się blokady warstwy OpenAI zanim polecenie w ogóle dotarło do Supabase. To nie były błędy PostgreSQL.

## Wniosek

Końcowa liczba wierszy w każdej z 27 tabel dokładnie zgadza się z plikami `walkaosql/tabele_insert/_RAPORT.txt`.

Sprawdzono zgodność liczby wierszy. Nie wykonywano końcowej kontroli integralności relacyjnej, zgodnie z przyjętym trybem importu.
