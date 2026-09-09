# SOL — AUDIO — AKTUALNA DOKUMENTACJA

**Data stanu: 2026-09-09**

## 0. Status tego pliku

To jest **aktualne źródło prawdy dla warstwy AUDIO → SQL**.

Przed jakąkolwiek operacją na danych audio w SQL należy przeczytać ten plik.

Starsze pliki opisujące wcześniejszy model audio mogą pozostać w repozytorium lub Bibliotece, ale **nie mają pierwszeństwa przed tym dokumentem**.

W szczególności wcześniejszy model, w którym `audio_middle_end` był główną tabelą wszystkich powiązań audio ↔ utwór, jest historyczny. Aktualny pipeline zapisuje główne dopasowanie bezpośrednio w `middle_end`.

---

# 1. Główna zasada modelu

Są trzy różne rzeczy i nie wolno ich mieszać:

1. **główne przypisanie audio do utworu** → `middle_end`
2. **szczegół opisu nietypowego, ale zaakceptowanego dopasowania** → `audio_match_details`
3. **rejestr przypadków problematycznych / wyjątkowych** → `audio_middle_end`

Tabela `audio` przechowuje sam plik audio i jego identyfikatory techniczne.

---

# 2. `audio`

Jeden rekord = jeden konkretny plik audio.

Najważniejsze pola:

- `audio_id` — wewnętrzny stabilny identyfikator, np. `audio-0157`
- `source_filename`
- `youtube_video_id`
- parametry techniczne pliku

`audio_id` identyfikuje plik audio.

`utwu_id` identyfikuje kanoniczny rekord utworu w `middle_end`.

To są dwa różne identyfikatory i nie wolno ich zamieniać.

---

# 3. `middle_end` — GŁÓWNE DOPASOWANIE AUDIO

To jest aktualne główne miejsce powiązania utworu z zaakceptowanym audio.

Pola audio w `middle_end`:

```text
audio_id
youtube_video_id
audio_match_quality
```

## READY

Rekordy z końcowych plików `SOL_audio-SQL-READY-*.tsv` trafiają do `middle_end`.

Mapowanie:

```text
candidate_utwu_id -> middle_end.utwu_id
audio_id          -> middle_end.audio_id
youtube_video_id  -> middle_end.youtube_video_id
quality            -> middle_end.audio_match_quality
```

`quality` dla READY to głównie:

```text
exact
high
```

READY **nie trafia** do `audio_match_details` i **nie trafia** do `audio_middle_end`.

## REVIEW zaakceptowany ręcznie

Rekord REVIEW z `decision=use` również trafia do `middle_end`.

Mapowanie:

```text
utwu_id            -> middle_end.utwu_id
audio_id           -> middle_end.audio_id
youtube_video_id   -> middle_end.youtube_video_id
audio_match_quality = review
```

Czyli `middle_end` zawiera zarówno:

- pewne automatyczne dopasowania READY,
- ręcznie zaakceptowane REVIEW.

## UNMATCHED

Prawdziwy `UNMATCHED` nie ma uczciwego `utwu_id`.

Dlatego **nie wolno wciskać go do przypadkowego rekordu `middle_end`**.

---

# 4. `audio_match_details` — SZCZEGÓŁY TYLKO DLA REVIEW

Schemat:

```text
utwu_id TEXT PRIMARY KEY REFERENCES middle_end(utwu_id)
audio_id TEXT NOT NULL REFERENCES audio(audio_id)
variant_type TEXT NOT NULL
note TEXT
```

Ta tabela służy do przechowywania szczegółów **ręcznie zaakceptowanych REVIEW**, kiedy audio odpowiada utworowi, ale występuje istotna różnica wersji, wykonania, kredytów albo metadanych.

Typowe `variant_type`:

```text
live
remaster
remix
acoustic
different_performance
live_vs_studio
featured_artist_difference
metadata_difference
credits
version
```

`note` opisuje konkretną różnicę.

## Co trafia

```text
REVIEW + decision=use -> TAK
```

## Co nie trafia

```text
READY       -> NIE
UNMATCHED   -> NIE
```

Powód dla UNMATCHED jest również techniczny: tabela wymaga istniejącego `utwu_id` i `variant_type`.

Nie wolno wypełniać `variant_type` sztuczną wartością tylko po to, żeby rekord przeszedł constraint.

---

# 5. `audio_middle_end` — REJESTR PRZYPADKÓW PROBLEMATYCZNYCH

Schemat:

```text
audio_id TEXT PRIMARY KEY REFERENCES audio(audio_id)
utwu_id TEXT NULL REFERENCES middle_end(utwu_id)
match_status TEXT NOT NULL
match_note TEXT
```

Dozwolone statusy schematu:

```text
matched
out
uncertain
```

W aktualnym pipeline ta tabela **nie jest głównym miejscem mapowania wszystkich audio**.

Służy do zachowania przypadków wymagających dodatkowej informacji o jakości lub braku dopasowania.

## REVIEW rozstrzygnięty jako `decision=use`

Ma znany `utwu_id`, więc może mieć rekord w `audio_middle_end`.

Ponieważ decyzja została już ręcznie rozstrzygnięta jako `use`, semantycznie jest to dopasowanie zaakceptowane:

```text
match_status = matched
utwu_id      = właściwy utwu_id
match_note   = opis różnicy / powód REVIEW
```

Status `uncertain` jest przeznaczony dla przypadku, który **nadal nie został rozstrzygnięty**.

Końcowy plik `SOL_audio-SQL-REVIEW-*.tsv` ma być już rozstrzygnięty, więc nie powinien być automatycznie traktowany jako nadal `uncertain` tylko dlatego, że pochodził z etapu REVIEW.

## UNMATCHED

```text
match_status = out
utwu_id      = NULL
match_note   = reason z pliku UNMATCHED
```

## READY

```text
READY -> NIE TRAFIA do audio_middle_end
```

READY jest już wystarczająco dobrze opisany przez główne pola audio w `middle_end`.

---

# 6. `audio_feature_snapshots`

Ta tabela przechowuje wyniki analizy sygnału audio.

Snapshot opisuje **konkretny plik audio**, nie abstrakcyjny utwór.

Klucz relacji:

```text
audio_feature_snapshots.audio_id -> audio.audio_id
```

Nie należy przepisywać do snapshotu `utwu_id` tylko dla wygody.

Połączenie do utworu należy wykonywać przez `audio_id` i warstwę mapowania.

---

# 7. Końcowe pliki TSV

Dla całego obecnego zestawu wygenerowano:

```text
READY     665
REVIEW    182
UNMATCHED   9
RAZEM     856
```

## READY

`SOL_audio-SQL-READY-*.tsv`

Znaczenie:

- automatycznie dobre dopasowanie,
- gotowe bez ręcznego opisu wariantu.

SQL:

```text
middle_end: TAK
audio_match_details: NIE
audio_middle_end: NIE
```

## REVIEW

`SOL_audio-SQL-REVIEW-*.tsv`

Znaczenie:

- automat nie był wystarczająco pewny,
- rekord został ręcznie rozstrzygnięty,
- `decision=use`,
- ma właściwy `utwu_id`, `variant_type`, `note`.

SQL:

```text
middle_end: TAK
audio_match_details: TAK
audio_middle_end: TAK jako przypadek opisany/problemowy
```

## UNMATCHED

`SOL_audio-SQL-UNMATCHED-*.tsv`

Znaczenie:

- brak uczciwego odpowiednika w `middle_end`,
- nie wolno przypisywać losowego `utwu_id`.

SQL:

```text
middle_end: NIE
audio_match_details: NIE
audio_middle_end: TAK, status out, utwu_id NULL
```

---

# 8. Obowiązujące updatery

## READY

```text
piosenki/SOL_update-middleend-audio-ready-v02.py
```

Updater zapisuje tylko:

```sql
UPDATE middle_end
SET audio_id=?, youtube_video_id=?, audio_match_quality=?
WHERE utwu_id=?
```

## REVIEW

```text
piosenki/SOL_update-middleend-audio-review-v02.py
```

Updater robi dwie rzeczy:

1. aktualizuje `middle_end`, ustawiając `audio_match_quality='review'`,
2. dodaje rekord do `audio_match_details` z `variant_type` i `note`.

To jest ważny dowód rozdziału ról obu tabel.

---

# 9. Znane dzisiejsze odchylenie w bazie

Podczas operacji 2026-09-09 wykonano błędny workflow, który wypełnił `audio_middle_end` następująco:

```text
REVIEW    -> uncertain
UNMATCHED -> out
READY     -> brak
```

Część `READY -> brak` oraz `UNMATCHED -> out` jest zgodna z aktualną zasadą.

**REVIEW zapisane jako `uncertain` jest semantycznie niezgodne z finalnym `decision=use`.**

Jeżeli ten stan nie został później poprawiony, wymaga osobnej korekty:

```text
finalny REVIEW + decision=use: uncertain -> matched
```

Nie wykonywać tej korekty automatycznie bez wyraźnego polecenia użytkownika.

---

# 10. Błędna próba dotycząca `audio_match_details`

2026-09-09 była próba uzupełnienia `audio_match_details` wszystkimi rekordami z `middle_end` mającymi `audio_id`.

Próba była błędna, ponieważ próbowała wpisać:

```text
variant_type = NULL
```

a schemat wymaga:

```text
variant_type NOT NULL
```

Transakcja się nie powiodła.

Z tego nie wolno wyciągać wniosku, że `audio_match_details` ma zawierać READY.

Aktualna zasada pozostaje:

```text
audio_match_details = tylko ręcznie zaakceptowane REVIEW z prawdziwym variant_type/note
```

---

# 11. Kolejność źródeł prawdy

Przy sprzeczności informacji stosować kolejność:

1. **ten plik** — `SOL_DOKUMENTACJA-AUDIO-AKTUALNA.md`
2. aktualny schemat SQL i aktualne skrypty updaterów w repozytorium
3. świeże końcowe pliki `SOL_audio-SQL-*.tsv`
4. historia commitów, jeśli trzeba ustalić, co faktycznie wykonano
5. starsze dokumenty z Biblioteki i wcześniejsze opisy architektury — wyłącznie historycznie

Nie wolno ustalać roli tabel na podstawie samej nazwy tabeli.

---

# 12. Reguła operacyjna dla AI

Przed zmianą danych audio w SQL:

1. przeczytać ten plik,
2. ustalić kategorię rekordu: READY / REVIEW / UNMATCHED,
3. zapisać tylko do tabel przewidzianych dla tej kategorii,
4. nie zmieniać schematu,
5. nie tworzyć nowej semantyki statusów,
6. nie wypełniać wymaganych pól fikcyjnymi wartościami,
7. nie rozszerzać zakresu operacji poza polecenie użytkownika.

Najkrócej:

```text
READY:
  middle_end

REVIEW + decision=use:
  middle_end
  audio_match_details
  audio_middle_end (matched)

UNMATCHED:
  audio_middle_end (out, utwu_id=NULL)
```
