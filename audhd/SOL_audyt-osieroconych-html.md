# Audyt osieroconych HTML-i w `audhd/` — ZAKOŃCZONY

Data: 2026-09-11

Status: **audyt zakończony, sieroty przeniesione, kontrola po operacji OK**.

## Cel

Ustalić, które pliki HTML w `audhd/` są osiągalne ze statycznej struktury publicznej strony AuDHD, a które są osierocone, a następnie przenieść potwierdzone sieroty do `osierocone-html/audhd/` bez trwałego kasowania.

## Zakres

Audyt dotyczył **statycznej osiągalności plików HTML w strukturze WWW `audhd/`**.

`SOL_mapa-sekcji-i-anchorow-audhd.html` pozostaje normalnym osiągalnym elementem WWW, ale dynamiczne linki `deep_link`, generowane z SQL/API, **nie podlegały audytowi i nie wpływały na klasyfikację sierot**. Mapa sekcji jest widokiem danych z bazy, a nie elementem badanego statycznego grafu plików.

## Wynik inwentaryzacji

Przed przeniesieniem w `audhd/` było **40 plików HTML**:

- **22** bezpośrednio w `audhd/`,
- **18** w podkatalogach.

Korzenie WWW:

- `audhd/index.html` — PL,
- `audhd/index-en.html` — EN.

Po przejściu statycznego grafu linków i redirectów osiągalnych było **37 z 40 HTML-i**.

## Osiągalne redirecty podkatalogowe

Potwierdzono m.in. następujące aktywne przejścia:

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

## Potwierdzone sieroty

### 1. `CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html`

Klasyfikacja: **stara kopia / poprzednia wersja publikowanego tekstu**.

Aktywna wersja PL:

`audhd/rownania/index.html`

Blob przed i po przeniesieniu:

`0abdfe497ca8aeaa47c81974dcfae59c50ff2963`

### 2. `CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html`

Klasyfikacja: **stara kopia / poprzednia wersja angielskiego tekstu**.

Aktywna wersja EN:

`audhd/rownania/index-en.html`

Blob przed i po przeniesieniu:

`62e2b7c16e36059f34d3bb76d928ecde5b8ebcdf`

### 3. `opis-po-ludzku-20-prac-naukowych.html`

Klasyfikacja: **zbędny, nieużywany redirect pośredni**.

Plik przekierowywał do `apendyks1-po-ludzku-02_01-2026-08-26.html`, do którego aktywne `audhd/20-prac/index.html` prowadzi już bezpośrednio.

Blob przed i po przeniesieniu:

`a8fa185863b40ff37c677b4bea2bac3fc9579247`

## Krok 6 — dry-run

Przed przeniesieniem potwierdzono:

- wszystkie 3 źródła istniały na `main`,
- `osierocone-html/` istniał,
- `osierocone-html/audhd/` jeszcze nie istniał,
- brak kolizji nazw,
- aktywne wersje treści pozostawały dostępne.

Dry-run: **OK**.

## Krok 7 — wykonane przeniesienie

Trzy pliki przeniesiono atomowo, z zachowaniem tych samych blobów:

- `audhd/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html` → `osierocone-html/audhd/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html`
- `audhd/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html` → `osierocone-html/audhd/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html`
- `audhd/opis-po-ludzku-20-prac-naukowych.html` → `osierocone-html/audhd/opis-po-ludzku-20-prac-naukowych.html`

Commit przeniesienia:

`93f6dce546945420c486bbc5e8686e85699c4a84`

Po operacji katalog `osierocone-html/audhd/` zawiera dokładnie te trzy pliki i ich blob SHA są identyczne z SHA źródeł sprzed przeniesienia.

## Krok 8 — kontrola po operacji

Kontrolę wykonano ponownie na świeżym `main` po późniejszych, równoległych commitach w innych częściach repo.

Punkt odniesienia kontroli: commit `c1685029bf26b5ebb6704dfb2e1c8f0b37a118b1`.

Wynik:

- rekurencyjne drzewo `audhd/` jest kompletne (`truncated: false`),
- w `audhd/` pozostało dokładnie **37 HTML-i**: **19** bezpośrednio w `audhd/` i **18** w podkatalogach,
- wszystkie 37 to ten sam zestaw, który w audycie przed przeniesieniem został potwierdzony jako statycznie osiągalny,
- subtree `audhd/` ma SHA `332f39f0fc0535de6e69143e10d1b3b71cf45941`, identyczny jak przy zamknięciu audytu, więc późniejsze równoległe commity nie zmieniły żadnego pliku w `audhd/`,
- dokładne wyszukiwanie trzech starych nazw nie wykazało odwołań z bieżącej aktywnej zawartości,
- `osierocone-html/audhd/` zawiera dokładnie **3 pliki** i żadnego dodatkowego pliku,
- trzy pliki w `osierocone-html/audhd/` nadal mają te same blob SHA co przed przeniesieniem,
- trwałe usunięcia treści: **0**.

Kontrola po operacji: **OK**.

## Stan końcowy

- HTML w `audhd/` przed audytem: **40**
- HTML w `audhd/` po przeniesieniu: **37**
- aktywnie osiągalne statycznie: **37 / 37**
- potwierdzone sieroty: **3**
- przeniesione do `osierocone-html/audhd/`: **3 / 3**
- trwałe usunięcia treści: **0**
- dynamiczne `deep_link` z mapy SQL: **poza zakresem audytu**
- kontrola po operacji: **OK**
- audyt: **ZAKOŃCZONY**
