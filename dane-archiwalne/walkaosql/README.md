# walkaosql — archiwum migracji do Supabase

Wersja 01.00 · 2026-09-19
Status: ARCHIWALNE — nic tutaj nie jest używane przez działający system

## Co to było

Narzędzia i dane jednorazowego, hurtowego importu starej bazy do Supabase:

- `happy-hue-octopus-backup.sql.zip` — zrzut starej bazy, spakowany
- `happy-hue-octopus-backup.sql` — ten sam zrzut, rozpakowany
- `rozpakowane/` — ten sam zrzut ponownie, wygenerowany przez workflow
- `tabele/`, `tabele_insert/`, `create_tables.sql` — zrzut pocięty na pliki per tabela
- trzy skrypty `split_*.py` i `extract_create_tables.py` — narzędzia tego cięcia

## Kiedy przestało być potrzebne

Import zakończył się **2026-09-12** z wynikiem: 27/27 tabel, 15071/15071 wierszy, różnica zero.
Szczegóły w `SOL-import-supabase-wynik-koncowy-2026-09-12.md`.

Obsługujący to workflow `unpack-walkaosql.yml` nie został wtedy wyłączony i przez kolejne
78 commitów odpalał się przy każdym pushu bez żadnego efektu. Usunięty 2026-09-19.
Opis w `bledy-AI/SOL/`.

## Dlaczego to nadal tu leży

Bo to zrzut bazy danych, a zrzutów bazy nie kasuje się dlatego, że akurat wyglądają na zbędne.
Katalog został przeniesiony z głównej części repozytorium do poczekalni, żeby przestał
udawać element działającego systemu.

## Do rozstrzygnięcia przy przeglądzie

**Ten sam zrzut leży tu w trzech kopiach o identycznej sumie kontrolnej** (`1c50621d…`):

| plik | rozmiar |
|---|---|
| `happy-hue-octopus-backup.sql.zip` | 2,3 MB |
| `happy-hue-octopus-backup.sql` | 6,5 MB |
| `rozpakowane/happy-hue-octopus-backup.sql.tsv` | 6,5 MB |

Do tego `tabele/` i `tabele_insert/` to ten sam materiał pocięty, kolejne 13,2 MB.
Razem katalog waży około 29 MB, z czego zdecydowana większość to powielenie jednego pliku.

Jeżeli przy przeglądzie zapadnie decyzja o zmniejszeniu: wystarczy `.zip`.
Pozostałe kopie odtwarza się z niego jednym `unzip` i trzema skryptami leżącymi obok.

## Czego NIE ruszać bez sprawdzenia

Komentarze w `piosenki/content_structure.py` i `piosenki/content_store.py` powołują się na ten
katalog jako na źródło danych, które są już w Supabase. To wyjaśnienie historyczne, nie odczyt pliku —
kod niczego stąd nie czyta. Przy zmianie nazwy katalogu trzeba jednak poprawić te komentarze,
żeby nie wskazywały donikąd.
