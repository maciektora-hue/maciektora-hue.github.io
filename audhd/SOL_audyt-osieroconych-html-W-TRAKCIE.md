# Audyt osieroconych HTML-i w `audhd/` — W TRAKCIE

Data: 2026-09-11

Status: audyt niezakończony. Stan po krokach 1–6.

## Cel

Ustalić, które pliki HTML w `audhd/` są osiągalne ze statycznej struktury publicznej strony AuDHD, a które są osierocone.

## Zakres audytu

Audyt dotyczy **statycznej osiągalności plików HTML w strukturze WWW `audhd/`**.

`SOL_mapa-sekcji-i-anchorow-audhd.html` pozostaje normalnym osiągalnym elementem WWW, ale jego dynamiczne linki `deep_link`, generowane z SQL/API, **nie podlegają temu audytowi i nie wpływają na klasyfikację sierot**. Mapa opisuje zawartość bazy i generuje odsyłacze w runtime, więc nie jest częścią badanego statycznego grafu plików.

Ewentualne sieroty mają być przenoszone do `osierocone-html/`, a nie trwale kasowane.

## Krok 1 — inwentaryzacja HTML

W `audhd/` znaleziono **40 plików HTML**:

- **22** bezpośrednio w `audhd/`,
- **18** w podkatalogach.

## Krok 2 — korzenie WWW

Korzenie serwisu:

- `audhd/index.html` — PL,
- `audhd/index-en.html` — EN.

Obie strony są osobnymi wejściami i linkują między wersjami językowymi. Nie ma automatycznego redirectu językowego.

## Krok 3 — bezpośrednie przejścia z korzeni

Z obu korzeni bezpośrednio osiągalnych jest **19 innych HTML-i**. Razem z dwoma korzeniami daje to **21 z 40** po pierwszym poziomie przejść.

Bezpośrednio osiągalne:

- `SOL_mapa-sekcji-i-anchorow-audhd.html`
- `20-prac/index.html`
- `cechy/index.html`
- `co-to-znaczy/index.html`
- `fundatorzy-it/index.html`
- `ilu-nas/index.html`
- `jezyki-milosci/index.html`
- `kognitywistyka-ai/index.html`
- `mowienie/index.html`
- `obiektywnosc/index.html`
- `pamiec-esej/index.html`
- `pamiec-powiesc/index.html`
- `po-diagnozie/index.html`
- `po-ludzku/index.html`
- `pomaganie/index.html`
- `publikacje/index.html`
- `rdzen-czy-maskowanie/index.html`
- `rownania/index.html`
- `rownania/index-en.html`

Anchory typu `cechy/#...` są traktowane jako wejście do tego samego HTML-a.

## Krok 4 — przejście rekurencyjne

Podkatalogowe `index.html` są w większości redirectami do właściwych wersjonowanych HTML-i w `audhd/`.

Potwierdzone redirecty:

- `20-prac/index.html` → `apendyks1-po-ludzku-02_01-2026-08-26.html`
- `cechy/index.html` → `audhd_opracowanie_v6_0_2026-07-01-2.html`
- `co-to-znaczy/index.html` → `co-to-znaczy-audhd-v03_01-2026-07-09-2.html`
- `fundatorzy-it/index.html` → `audhd-fundatorzy-it-1_00-2026-04-27.html`
- `ilu-nas/index.html` → `ilu-nas-jest-audhd-polska-wstep-v03_00-2026-08-10.html`
- `jezyki-milosci/index.html` → `piec-jezykow-milosci-nd-v01.00-2026-05-18.html`
- `kognitywistyka-ai/index.html` → `kognitywistyka-ai-bledy-poznawcze-2_00-2026-04-28.html`
- `mowienie/index.html` → `autyzm-regulacja-mowienia-v01.00-2026-05-14.html`
- `obiektywnosc/index.html` → `obiektywnosc-autyzm-v01.00-2026-05-14.html`
- `pamiec-esej/index.html` → `ESEJ_architektury-pamieci-1_02-2026-04-28.html`
- `pamiec-powiesc/index.html` → `POWIESC_architektury-pamieci-2_00-2026-04-29.html`
- `po-diagnozie/index.html` → `CLAUDE_co-dziala-po-poznej-diagnozie-02_01-2026-08-26.html`
- `po-ludzku/index.html` → `audhd-po-ludzku-v02_02-2026-07-09.html`
- `pomaganie/index.html` → `adhd-pomaganie-kosztem-siebie-v01.00-2026-05-14.html`
- `publikacje/index.html` → `dluga-lista-publikacji-4.01-2026-08-26.html`
- `rdzen-czy-maskowanie/index.html` → `63-cechy-rdzen-czy-maskowanie-01_01-2026-08-26.html`

Po uwzględnieniu redirectów statycznie osiągalnych jest **37 z 40 HTML-i**.

## Krok 5 — klasyfikacja trzech sierot

### `CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html`

Klasyfikacja: **stara kopia / poprzednia wersja publikowanego tekstu**.

Aktualna publiczna wersja PL:

`audhd/rownania/index.html`

Wniosek: **przenieść do `osierocone-html/audhd/`**.

### `CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html`

Klasyfikacja: **stara kopia / poprzednia wersja angielskiego tekstu**.

Aktualna publiczna wersja EN:

`audhd/rownania/index-en.html`

Wniosek: **przenieść do `osierocone-html/audhd/`**.

### `opis-po-ludzku-20-prac-naukowych.html`

Klasyfikacja: **zbędny, nieużywany redirect pośredni**.

Przekierowuje do `apendyks1-po-ludzku-02_01-2026-08-26.html`, do którego aktywne `audhd/20-prac/index.html` już prowadzi bezpośrednio.

Wniosek: **przenieść do `osierocone-html/audhd/`**.

## Krok 6 — dry-run przeniesienia

Sprawdzono ponownie `main` bez wykonywania żadnego ruchu.

Wszystkie trzy źródła nadal istnieją:

- `audhd/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html` — blob `62e2b7c16e36059f34d3bb76d928ecde5b8ebcdf`
- `audhd/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html` — blob `0abdfe497ca8aeaa47c81974dcfae59c50ff2963`
- `audhd/opis-po-ludzku-20-prac-naukowych.html` — blob `a8fa185863b40ff37c677b4bea2bac3fc9579247`

`osierocone-html/` istnieje i zawiera obecnie tylko `README.md`. Podkatalog `osierocone-html/audhd/` jeszcze nie istnieje, więc nie ma żadnej kolizji nazw.

Planowane ruchy, **bez zmiany zawartości plików**:

- `audhd/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html` → `osierocone-html/audhd/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html`
- `audhd/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html` → `osierocone-html/audhd/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html`
- `audhd/opis-po-ludzku-20-prac-naukowych.html` → `osierocone-html/audhd/opis-po-ludzku-20-prac-naukowych.html`

Dry-run: **OK**. Nie wykryto kolizji ani zależności wymagającej zmiany aktywnych stron WWW.

Na tym kroku **nie przeniesiono ani nie usunięto żadnego HTML-a**.

## Stan na teraz

- HTML w badanym `audhd/` przed przeniesieniem: **40**
- osiągalne statycznie: **37**
- sklasyfikowane sieroty: **3**
- dry-run przeniesienia: **OK**
- dynamiczne `deep_link` z mapy SQL: **poza zakresem audytu**
- faktyczne przeniesienie: **jeszcze niewykonane**
