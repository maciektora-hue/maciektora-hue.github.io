# SOL — instrukcja tworzenia plików audio do SQL

## Cel
Dla kolejnych zakresów po 50 numerów przygotować końcowe pliki TSV gotowe do późniejszego zapisu do SQL.

## Zakres pracy
Pracować paczkami po 50 numerów, np.:
- 0001–0050
- 0051–0100
- 0251–0300
- 0901–0950

Dziury w numeracji są normalne.

## Skrypty

### 1. Parser nazw plików audio
`SOL_parse-audio-filenames-v03.py`

Przykład:
```bash
python piosenki/SOL_parse-audio-filenames-v03.py \
  --start 251 \
  --end 300 \
  --source piosenki/audio_features_v08.csv \
  --output piosenki/audio_filename_parsed_0251_0300.tsv
```

Jeśli parser ewidentnie pomyli artystę i tytuł, użyć pliku override, np.:
```bash
python piosenki/SOL_parse-audio-filenames-v03.py \
  --start 251 \
  --end 300 \
  --source piosenki/audio_features_v08.csv \
  --output piosenki/audio_filename_parsed_0251_0300.tsv \
  --overrides piosenki/audio_filename_overrides_0251_0300.tsv
```

Nie zmieniać skryptu parsera. Poprawki robić wyłącznie przez override.

### 2. Matcher do `middle_end`
`SOL_match-audio-middleend-v02.py`

```bash
python piosenki/SOL_match-audio-middleend-v02.py \
  --audio piosenki/audio_filename_parsed_0251_0300.tsv \
  --output piosenki/audio_middleend_candidates_0251_0300.tsv
```

### 3. Podział READY / REVIEW
`SOL_split-audio-middleend-candidates-v01.py`

```bash
python piosenki/SOL_split-audio-middleend-candidates-v01.py \
  --input piosenki/audio_middleend_candidates_0251_0300.tsv \
  --ready piosenki/audio_middleend_ready_0251_0300.tsv \
  --review piosenki/audio_middleend_review_0251_0300.tsv
```

## REVIEW
Każdy rekord REVIEW rozstrzygnąć ręcznie.

Jeśli to ten sam utwór, ale inna wersja, wykonanie lub metadata, ustawić:
- właściwy `utwu_id`
- `decision=use`
- `variant_type` — jeśli potrzebne, np. `live`, `remaster`, `remix`, `acoustic`
- `note` — krótki opis różnicy

Jeżeli nie ma uczciwego odpowiednika w `middle_end`, rekord trafia do `UNMATCHED`. Nie przypisywać losowego kandydata.

## Końcowe pliki
Dla każdej paczki utworzyć:

### READY
`SOL_audio-SQL-READY-0251-0300.tsv`

Zawiera rekordy automatycznie pewnie dopasowane i gotowe do SQL.

### REVIEW
`SOL_audio-SQL-REVIEW-0251-0300.tsv`

Zawiera ręcznie rozstrzygnięte rekordy REVIEW, także gotowe do SQL.

### UNMATCHED
`SOL_audio-SQL-UNMATCHED-0251-0300.tsv`

Tworzyć tylko wtedy, gdy rzeczywiście są rekordy bez odpowiadającego `utwu_id`.

## Zasady
1. Jedna paczka = 50 numerów.
2. Nie zmieniać istniejących skryptów.
3. Parser poprawiać tylko przez override.
4. Nie robić dodatkowych analiz poza koniecznymi do poprawnego przypisania.
5. REVIEW rozstrzygać ręcznie.
6. Brak dopasowania = `UNMATCHED`, nie losowy `utwu_id`.
7. Końcowe pliki mają być gotowe do późniejszego zapisu do SQL, ale samo tworzenie tych plików nie zapisuje niczego do bazy.

## Dobór nagrań przy pobieraniu — ustalenie z 2026-09-14

Przy kolejnych pobraniach agent lub skrypt ma sam wybierać nagrania, gdy tytuł, wykonawca i wersja pozwalają na pewne dopasowanie. Użytkownik nie powinien zatwierdzać każdej oczywistej pozycji osobno. Do użytkownika trafiają tylko przypadki niejednoznaczne.

Według oceny użytkownika z tej sesji około 95% wyborów dało się rozstrzygnąć na podstawie nazw: około 90% stanowił wynik nr 1, a około 5% wynik nr 2. To obserwacja z tej partii, nie zmierzona skuteczność algorytmu ani reguła automatycznego wybierania pierwszego wyniku.

Przy dopasowaniu:
- porównać tytuł i wykonawcę, uwzględniając wielkość liter, interpunkcję, diakrytykę i techniczne dopiski;
- zachować znaczące różnice wersji: live, remix, cover, remaster oraz konkretne wykonanie lub część utworu klasycznego;
- wykorzystać kanał i długość nagrania jako dodatkowe wskazówki;
- zapisać wybrany identyfikator YouTube, powiązany utwu_id i uzasadnienie wyboru;
- przy braku pewnego kandydata pozostawić pozycję do wyjaśnienia, bez wymuszania dopasowania.

To zasada przyszłego doboru nagrań. Obecna wersja skryptu `piosenki/SOL_youtube-music-playlista-100.py` z tej sesji nadal pyta o wybór każdego nowego nagrania; wdrożenie automatycznego doboru wymaga zmiany skryptu.

Pobranie pliku i jego zgodność z oczekiwanym nagraniem to osobne kwestie. Status `downloaded` wraz z istnieniem pliku potwierdza ukończenie pobrania, a nie niezależną weryfikację poprawności muzycznej. Samo pobranie nie uzupełnia przypisania audio w SQL.
