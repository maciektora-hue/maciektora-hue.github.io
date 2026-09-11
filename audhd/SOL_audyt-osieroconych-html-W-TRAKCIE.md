# Audyt osieroconych HTML-i w `audhd/` — W TRAKCIE

Data: 2026-09-11

Status: audyt niezakończony. Ten plik zapisuje stan prac po krokach 1–4.

## Cel

Ustalić, które pliki HTML w katalogu `audhd/` są faktycznie osiągalne z publicznej strony AuDHD, a które są osierocone, czyli nie da się do nich dojść ze strony głównej ani przez kolejne lokalne przejścia.

## Krok 1 — inwentaryzacja HTML

W `audhd/` znaleziono łącznie **40 plików HTML**:

- **22** bezpośrednio w `audhd/`,
- **18** w podkatalogach.

## Krok 2 — korzenie WWW

Za faktyczne korzenie serwisu przyjęto:

- `audhd/index.html` — wejście PL,
- `audhd/index-en.html` — wejście EN.

Obie strony są osobnymi wejściami i linkują między wersjami językowymi. Nie ma automatycznego redirectu językowego.

## Krok 3 — bezpośrednie przejścia z korzeni

Z obu korzeni bezpośrednio osiągalnych jest **19 innych HTML-i**.

Razem z `index.html` i `index-en.html` daje to **21 z 40 HTML-i** osiągalnych po pierwszym poziomie przejść.

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

Anchory typu `cechy/#...` traktowane są jako wejście do tego samego pliku `cechy/index.html`, a nie jako osobne strony.

## Krok 4 — przejście rekurencyjne

Podkatalogowe `index.html` okazały się w większości redirectami do właściwych wersjonowanych HTML-i w `audhd/`.

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

Po uwzględnieniu tych redirectów statycznie osiągalnych jest **37 z 40 HTML-i**.

## Aktualni kandydaci na osierocone HTML-e

Na tym etapie statycznego audytu nie znaleziono ścieżki z korzeni WWW do trzech plików:

1. `CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html`
2. `CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html`
3. `opis-po-ludzku-20-prac-naukowych.html`

Trzeci plik jest dodatkowo jedynie starym redirectem do:

`apendyks1-po-ludzku-02_01-2026-08-26.html`

## Ważne: audyt jeszcze niezamknięty

`SOL_mapa-sekcji-i-anchorow-audhd.html` nie przechowuje wszystkich linków statycznie. Pobiera z API pola `deep_link` z endpointu:

`https://piosenki-api.onrender.com/api/content/audhd`

Dlatego przed uznaniem powyższych trzech plików za definitywnie osierocone trzeba jeszcze sprawdzić, czy którykolwiek z nich nie jest osiągalny przez dynamiczne `deep_link` z mapy SQL.

Próba weryfikacji tego endpointu w bieżącym audycie nie została zakończona z powodu ograniczenia dostępu narzędzia do tego URL-a. Zgodnie z zasadą po błędzie dalszych obejść nie wykonywano bez nowej komendy.

## Stan na teraz

- HTML łącznie: **40**
- osiągalne statycznie: **37**
- kandydaci na sieroty: **3**
- audyt dynamicznych `deep_link`: **do wykonania**
- żadnych plików HTML podczas audytu nie przeniesiono ani nie usunięto.
