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

## 5. Praca równoległa w wielu czatach

### Dlaczego ten problem występuje

W praktyce projekt może być rozwijany równocześnie w kilku rozmowach. Jest to naturalne w bardzo szybkim trybie pracy, kiedy tempo kolejnych decyzji, pytań i odczytu odpowiedzi jest większe niż przepustowość pojedynczego wątku rozmowy.

Samo rozdzielenie pracy na kilka czatów nie jest problemem. Problem pojawia się wtedy, gdy kilka czatów **modyfikuje te same zasoby**: to samo repozytorium GitHub, ten sam serwis Render albo tę samą bazę Turso.

Każdy czat posiada własny lokalny kontekst roboczy. Może więc działać na podstawie stanu, który kilka sekund wcześniej był poprawny, ale po zapisie wykonanym w innym czacie jest już nieaktualny.

To jest klasyczny problem współbieżności.

### Typowy scenariusz wyścigu

Przykładowa sekwencja:

```text
czat A odczytuje stan X
czat B odczytuje stan X
czat A zapisuje zmianę A → stan X+A
czat B nadal uważa X za aktualny
czat B zapisuje zmianę B
Render zaczyna deploy A
GitHub ma już zmianę B
Render zaczyna lub kończy inny deploy
Turso jest w tym samym czasie używane przez oba procesy
```

Na poziomie użytkownika objawem może być „strona się nie otwiera”, „wróciła stara wersja”, „deploy jest niby live, ale kod wygląda inaczej” albo „przed chwilą działało”.

Na poziomie technicznym mogą wystąpić:

- zapis na podstawie nieaktualnego SHA pliku,
- nadpisanie zmiany z innego czatu,
- deploy commita starszego niż aktualny `main`,
- kilka deployów Rendera nakładających się w czasie,
- restart procesu w trakcie obsługi żądania,
- blokada, timeout albo konflikt połączeń do bazy,
- diagnozowanie błędu w komponencie, który faktycznie jest niewinny,
- różnica między stanem GitHuba, stanem wdrożonym na Renderze i stanem widocznym w przeglądarce.

### Zasada podstawowa

Najważniejsza reguła:

> **Przed każdą modyfikacją współdzielonego zasobu należy ponownie odczytać jego aktualny stan.**

Nie wystarcza stan odczytany na początku rozmowy ani kilka minut wcześniej.

Dla GitHuba oznacza to pobranie aktualnej wersji pliku i jego SHA bezpośrednio przed zapisem. Dla Rendera oznacza sprawdzenie, jaki commit faktycznie jest wdrażany i jaki jest `LIVE`. Dla Turso oznacza unikanie równoległych zmian strukturalnych i transakcji, które mogą sobie wzajemnie przeszkadzać.

### Jeden właściciel zapisu

Dla prac wymagających wielu równoległych czatów przyjmujemy zasadę **jednego właściciela zapisu**.

W danym momencie jeden czat jest właścicielem operacji zapisu dla określonego współdzielonego zasobu. Pozostałe czaty mogą w tym czasie:

- analizować dane,
- projektować rozwiązanie,
- przygotowywać treść lub kod,
- sprawdzać logikę,
- wykonywać odczyty,
- proponować kolejne kroki.

Nie powinny jednak równolegle wykonywać zapisu do tego samego zasobu.

Własność można rozdzielić bardziej szczegółowo. Przykładowo jeden czat może być właścicielem `piosenki/statystyki`, a drugi pracować nad innym, niezależnym katalogiem. Problemem nie jest liczba czatów, tylko nakładanie się zakresów zapisu.

### Reguły dla GitHuba

Przy pracy równoległej:

1. przed zmianą istniejącego pliku pobrać jego najnowszą treść i SHA,
2. nie zakładać, że SHA sprzed kilku minut jest nadal aktualne,
3. po konflikcie nie wymuszać zapisu na siłę,
4. po zmianie sprawdzić aktualny `main`,
5. przy kilku powiązanych zmianach sprawdzić, czy pomiędzy nimi nie pojawiły się obce commity,
6. nie traktować sukcesu pojedynczego zapisu jako dowodu, że cały projekt jest w oczekiwanym stanie.

### Reguły dla Rendera

Po zmianie kodu:

1. sprawdzić, czy Render zauważył nowy commit,
2. sprawdzić identyfikator commita wdrażanego przez deploy,
3. nie zakładać, że `autoDeploy=yes` oznacza, że wdrożenie rzeczywiście wystartowało,
4. nie odpalać ręcznego deploya bez sprawdzenia istniejących deployów,
5. po zakończeniu potwierdzić status `LIVE`,
6. przy równoległej pracy upewnić się, że `LIVE` odpowiada aktualnemu `main`, a nie wcześniejszemu commitowi.

### Reguły dla Turso

Baza jest najbardziej wrażliwym współdzielonym zasobem.

Przy pracy równoległej:

1. nie wykonywać z kilku czatów równocześnie zmian schematu,
2. nie zakładać, że stan tabel sprzed chwili jest nadal aktualny,
3. preferować operacje read-only tam, gdzie jest to możliwe,
4. operacje modyfikujące wykonywać możliwie krótko i jawnie,
5. przed zmianą strukturalną ustalić właściciela zapisu,
6. po operacji zweryfikować stan bazy, zamiast wnioskować o nim tylko z sukcesu komendy.

### Stan repo, stan deployu i stan aplikacji to trzy różne rzeczy

W projekcie trzeba rozróżniać trzy poziomy:

```text
GitHub main
    ↓
commit wdrożony przez Render
    ↓
proces, który faktycznie odpowiada na żądania użytkownika
```

Te trzy stany zwykle są zgodne, ale podczas równoległych zmian albo kolejnych deployów mogą przez pewien czas być różne.

Dlatego komunikat „kod jest już na GitHubie” nie oznacza jeszcze „strona działa na tym kodzie”. Analogicznie `deploy live` nie wystarcza, jeśli wdrożony został wcześniejszy commit.

### Objawy sugerujące problem współbieżności

Szczególnie podejrzane są sytuacje, gdy:

- zmiana jest widoczna w repo, ale nie na stronie,
- po odświeżeniu pojawia się wcześniejsza wersja,
- chwilę po poprawnym deployu uruchamia się następny,
- działająca strona zaczyna nagle wisieć bez zmiany w jej własnym kodzie,
- logi pokazują restarty workerów, timeouty albo kilka deployów w krótkim czasie,
- jeden czat twierdzi, że stan jest poprawny, a drugi przed chwilą wykonał zapis w tym samym obszarze.

W takim przypadku pierwszym krokiem nie powinno być automatyczne poprawianie ostatnio edytowanego pliku. Najpierw trzeba odtworzyć chronologię: aktualny `main` → kolejne commity → deploye → logi → aktualnie działający proces.

### Cel tej zasady

Nie chodzi o ograniczanie liczby równoległych rozmów. Równoległość może być bardzo efektywna i pozwala utrzymać wysokie tempo pracy.

Ograniczamy jedynie **równoległe zapisy do tego samego stanu zewnętrznego**.

Można więc prowadzić cztery równoległe analizy, projektować cztery części systemu albo przygotowywać kilka zmian jednocześnie. W momencie zapisu do wspólnego repozytorium, deployu albo bazy musi jednak istnieć świadoma synchronizacja.

W skrócie:

```text
równoległe myślenie: TAK
równoległe odczyty: TAK
równoległe przygotowywanie zmian: TAK
równoległe zapisy do tego samego zasobu: OSTROŻNIE / JEDEN WŁAŚCICIEL
```
