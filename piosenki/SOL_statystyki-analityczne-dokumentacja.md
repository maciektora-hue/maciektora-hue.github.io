# SOL — statystyki analityczne piosenek

Stan: 2026-09-07

## Założenie ogólne

Warstwa statystyczna nie zmienia danych źródłowych w Turso. SQL przechowuje fakty: utwór, kolejność Spotify, tagi, osie i rodziny. Analizy są liczone po stronie Pythona/Flaska, a wynik jest renderowany przez Jinja jako gotowy HTML i SVG. Brak własnego JavaScriptu po stronie przeglądarki.

Aktualne strony:

- `/statystyki/czas`
- `/statystyki/kierunek`
- `/statystyki/relacje`

## 1. Warstwa czasu zdarzeniowego

### Co oznacza czas

Oś czasu nie jest kalendarzem. Jednostką czasu jest kolejne polubienie utworu na Spotify zapisane przez `spotify_order`.

`spotify_order = 1` oznacza utwór najnowszy, czyli praktycznie „teraz”. Większa liczba oznacza coraz dalszą przeszłość. Przykładowo pozycja 523 jest 523 jednostki zdarzeniowe od teraźniejszości, niezależnie od tego, ile dni lub miesięcy kalendarzowych minęło.

To jest czas zdarzeniowy: mierzymy następstwo polubień, nie równomierny upływ czasu kalendarzowego.

### Parametry przesuwanego okna

Analiza czasu ma trzy parametry:

1. **Okno `W`** — liczba utworów użytych do jednego pomiaru.
2. **Krok `S`** — o ile pozycji przesuwamy okno przy kolejnym pomiarze.
3. **Kierunek** — domyślnie od teraźniejszości w przeszłość; można też odwrócić kolejność prezentacji.

Dla `W = 80` i `S = 30` okna są następujące:

```text
1–80
31–110
61–140
91–170
...
```

Formalnie dla kolejnego okna `k = 0,1,2,...`:

```text
start = 1 + k*S
koniec = start + W - 1
```

Na końcu szeregu ostatnie okno może być krótsze, jeśli zabraknie starszych utworów.

### Dlaczego kotwiczenie od „teraz”

Pierwszy punkt wykresu zawsze opisuje najnowszy fragment zbioru, np. „ostatnie 80 polubień”. Dzięki temu teraźniejszość ma stałe znaczenie, a nowe polubienia przesuwają wcześniejszą historię dalej wstecz.

Jeżeli `S < W`, kolejne okna nakładają się. Jest to zamierzone: wykres staje się gładszy i pokazuje zmianę profilu, zamiast skakać między całkowicie rozłącznymi paczkami.

### Co jest obecnie liczone

Na stronie czasu są trzy przykładowe poziomy:

- **Rodziny w czasie** — udział wystąpień każdej rodziny wśród wszystkich nadań tagów w danym oknie.
- **Osie w czasie** — analogiczny przebieg dla najczęściej występujących osi.
- **Przykładowy pojedynek tagów** — surowe liczby wystąpień dwóch tagów w kolejnych przesuwanych oknach.

Legenda rodzin jest jedna i zawiera równocześnie:

- kolor rodziny,
- nazwę rodziny,
- listę osi należących do tej rodziny.

Lista osi w legendzie nie jest wpisana ręcznie. Powstaje z aktualnych danych `axes` i `family_name`.

### Implementacja

Główne pliki:

- `app.py` — odczyt parametrów z URL i trasy Flask,
- `czas_okna.py` — budowanie przesuwanych okien i obliczenia,
- `templates/czas.html` — formularz i prezentacja,
- `static/statystyki.css` — wygląd,
- `statystyki.py` — wspólne funkcje do modelu danych i SVG.

Parametry strony są przekazywane w query string, np.:

```text
/statystyki/czas?okno=80&krok=30&kierunek=teraz
```

## 2. Warstwa kierunku / wartości

### Po co druga warstwa

Sama liczba wystąpień osi mówi, **jak bardzo dany temat jest obecny**, ale nie mówi, **w którą stronę** jest skierowany.

Przykład: wysoki wynik osi „sprawczość” może wynikać zarówno z `bezsilność`, jak i z `kontrola` czy `sprawczość`. Suma osi mówi więc o istotności pytania lub problemu. Dopiero rozkład tagów wewnątrz osi mówi o kierunku.

Dlatego rozdzielamy:

- **natężenie / ważność osi** — ile jest wystąpień,
- **kierunek osi** — po której stronie znaczeniowej leżą wystąpienia.

### Dane źródłowe a interpretacja

SQL przechowuje relację:

```text
tag → oś → rodzina
```

Nie przechowuje natomiast semantycznej informacji typu:

```text
bezsilność = lewa strona osi sprawczości
kontrola = prawa strona osi sprawczości
```

Ta informacja jest warstwą interpretacyjną i dlatego pozostaje poza SQL-em.

Plik:

```text
dane-analityczne/tag-wartosci.json
```

jest osobną konfiguracją analityczną. Nie zmienia ontologii ani danych źródłowych.

### Docelowy model kierunku

Najbezpieczniejszy model to przypisanie kierunku do pary:

```text
(tag, oś)
```

a nie tylko do samego tagu, ponieważ jeden tag może należeć do więcej niż jednej osi i w różnych osiach mieć inne znaczenie kierunkowe.

Dla każdej pary można użyć prostego kodowania:

```text
-1 = lewy biegun osi
 0 = środek / neutralne / brak kierunku
+1 = prawy biegun osi
```

Dodatkowo można utrzymywać niezależną walencję tagu:

```text
-1 = nieprzyjemne
 0 = neutralne
+1 = przyjemne
```

Walencja i kierunek osi są dwiema różnymi rzeczami. Na przykład `ucieczka` może mieć określony kierunek na osi „ruch / cel”, ale jej ocena przyjemne/nieprzyjemne jest osobnym pytaniem.

### Bilans osi

Dla wystąpień, którym przypisano kierunek, można liczyć prosty bilans:

```text
bilans = suma(kierunek × liczba_wystąpień) / suma(liczba_wystąpień)
```

Wynik leży w zakresie `[-1,+1]`:

- okolice `-1` — przewaga lewego bieguna,
- okolice `0` — równowaga albo przewaga tagów neutralnych,
- okolice `+1` — przewaga prawego bieguna.

Sama wartość bilansu nie zastępuje liczby wystąpień. Dwie osie mogą mieć ten sam bilans, ale zupełnie różną wagę w całym materiale.

### Tagi niejednoznaczne

Jeżeli znaczenie tagu nie jest wystarczająco jednoznaczne na podstawie jego definicji i opisu osi, nie należy wymuszać `-1`, `0` ani `+1`.

Takie pozycje powinny pozostać oznaczone jako nierozstrzygnięte do ręcznej decyzji. Przykładowo szczególnej ostrożności wymagają tagi typu `pogoń`, `kontrola`, `substancje`, `przetrwanie`, `euforia-napęd` czy `cykliczność-wzorzec`.

### Stan aktualny

`tag-wartosci.json` zawiera obecnie **demonstracyjny prototyp**:

- prostą walencję dla wybranych tagów,
- kilka ręcznie zdefiniowanych kontrastów, m.in. sprawczość, ruch/cel i afekt.

To pokazuje mechanikę strony `/statystyki/kierunek`, ale nie jest jeszcze pełną mapą całej ontologii.

Następny krok to przejście od demonstracyjnych kontrastów do pełnej mapy `(tag, oś) → kierunek`, zbudowanej na podstawie aktualnych definicji `tag_catalog.definition` i `axes.description`, z pozostawieniem pozycji niejednoznacznych do ręcznego rozstrzygnięcia.

## 3. Relacja między warstwami

Docelowa architektura analityczna ma trzy poziomy:

```text
SQL: fakty
  ↓
CZAS: kiedy w czasie zdarzeniowym pojawia się dane zjawisko
  ↓
KIERUNEK: w którą stronę znaczeniową przesuwa się dana oś
  ↓
RELACJE: które zjawiska poruszają się razem, rozchodzą się lub przecinają
```

Najważniejsza zasada interpretacyjna:

**suma na osi mierzy znaczenie / obecność problemu, a rozkład po biegunach mierzy jego kierunek.**

Dzięki temu płaski wynik osi nie musi oznaczać braku zmiany. Łączna liczba wystąpień może pozostać stała, podczas gdy skład tagów wewnątrz osi zmieni się całkowicie.

## 4. Zasady techniczne

- nie zmieniamy schematu Turso dla potrzeb tych analiz,
- surowe `lyrics_text` nie są potrzebne do renderowania tych stron,
- obliczenia wykonuje Python po stronie Rendera,
- Jinja tworzy HTML,
- wykresy powstają jako SVG generowane po stronie serwera,
- brak własnego JavaScriptu,
- zmiany w repo mogą uruchamiać deploy Rendera; przy pracy równoległej w kilku czatach należy uważać na wzajemne nadpisywanie lub nakładanie deployów.
