# Audyt osieroconych HTML — ROSJA

Status: ZAKOŃCZONY

## Zakres

Audyt dotyczy katalogu `rosja/` w repozytorium `maciektora-hue/maciektora-hue.github.io` i obejmuje statyczną osiągalność plików HTML z publicznych wejść WWW.

Korzenie publiczne:
- `rosja/index.html`
- `rosja/index-en.html`

Dynamiczne linki generowane z SQL/API przez `SOL_mapa-sekcji-z-opisami.html` nie są traktowane jako źródło statycznej osiągalności. Ten plik jest samodzielnym narzędziem technicznym do przeglądania struktury SQL/API, a nie elementem publicznej nawigacji.

## Inwentaryzacja

Stan początkowy: 51 plików HTML w `rosja/`.

Publicznie osiągalne statycznie: 38 HTML-i:
- 2 korzenie,
- 18 podkatalogowych `index*.html`,
- 18 właściwych plików docelowych.

## Wersje z anchorami

16 właściwych dokumentów to A1–A7, D1–D7, E1–E2.

11 dokumentów ma zachowaną parę:
- oryginalny zamrożony HTML,
- kopia `-anchory.html` z dodanymi `id`/anchorami bez zmiany treści merytorycznej.

Dotyczy to:
- A1,
- A5,
- D1,
- D2,
- D3,
- D4,
- D5,
- D6,
- D7,
- E1,
- E2.

Publiczne redirecty wskazują prawidłowo na wersje `-anchory.html`.

Pozostałe 5 dokumentów nie ma osobnej kopii `-anchory.html`, ponieważ ich oryginalne zamrożone HTML-e już miały komplet anchorów:
- A2,
- A3,
- A4,
- A6,
- A7.

Zwykłe zamrożone oryginały stojące obok aktywnych kopii `-anchory.html` nie są klasyfikowane jako sieroty. Są świadomie zachowanym źródłem historycznym.

## Pliki techniczne

`SOL_mapa-sekcji-z-opisami.html`

Klasyfikacja: samodzielne narzędzie techniczne SQL/API. Nie jest częścią publicznej nawigacji, ale nie jest klasyfikowane jako sierota do przeniesienia.

`SOL_test-SQL-rosja.html`

Klasyfikacja: jednorazowy techniczny test połączenia SQL API. Brak odwołań z publicznej części `rosja/`.

Plik został przeniesiony do:
`osierocone-html/rosja/SOL_test-SQL-rosja.html`

Treść pliku została zachowana bez zmian.

## Wynik końcowy

- 51 HTML-i przed audytem,
- 38 publicznie osiągalnych statycznie,
- 11 świadomie zachowanych zamrożonych oryginałów obok wersji `-anchory.html`,
- 1 samodzielne narzędzie techniczne SQL/API pozostawione w `rosja/`,
- 1 faktyczna techniczna sierota przeniesiona do `osierocone-html/rosja/`,
- 0 trwałych usunięć.

Audyt zakończony.
