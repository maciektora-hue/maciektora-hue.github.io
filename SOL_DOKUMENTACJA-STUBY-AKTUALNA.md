# STUBY I STAŁE ADRESY — REJESTR

Wersja: 01.00 · Data: 2026-09-20
Status: AKTUALNY SPIS WSZYSTKICH WEJŚĆ
Dokument nadrzędny: `SOT-SOA-AKTUALNA.md` · reguła: `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md` 0.1

---

## 1. Zasada w jednym zdaniu

**Stały jest adres, nie nazwa pliku.** Adres to wejście katalogowe bez wersji. Nazwa pliku
pod spodem jest wewnętrzna i może zawierać wersję, datę, autora albo `NIE-PUBLIKOWAC`.
**Tylko adres idzie na zewnątrz.**

## 2. Jak wygląda stub

```html
<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex">
  <meta http-equiv="refresh" content="0; url=../PLIK.html">
  <title>Przekierowanie</title>
  <script>location.replace('../PLIK.html' + location.hash);</script>
</head>
<body>
  <p><a href="../PLIK.html">Przejdź do tekstu</a></p>
</body>
</html>
```

Linia ze `<script>` jest **obowiązkowa**. Sam `meta refresh` gubi `#kotwicę`, więc czytelnik,
który dostał link do konkretnej sekcji, wylądowałby na górze dokumentu. Strażnik to sprawdza
(reguła 2) i bez tej linii CI jest czerwone.

## 3. Procedura przy nowym wydaniu

1. podnieś wersję w dokumencie — `<title>` oraz `Wersja: XX.YY` w nagłówku lub stopce;
2. zapisz pod nową nazwą, np. `-01_04.html`;
3. **przepnij stub** — oba adresy, w `meta refresh` i w `location.replace`;
4. stary plik usuń, chyba że ten konkretny adres poszedł komuś na zewnątrz;
5. uruchom `python3 .github/scripts/check_stable_www.py`.

Krok 3 jest ręczny i dlatego pilnuje go reguła 6. Zapomniane przepięcie nie daje 404 —
po cichu serwuje stary tekst. To jedyny błąd w tym zestawie niewidoczny z zewnątrz.

---

## 4. Wejścia stałe — 63

| adres | plik docelowy | tytuł |
|---|---|---|
| `audhd/20-prac/` | `apendyks1-po-ludzku.html` | Co mówi Appendix 1 — po ludzku — 02.01 |
| `audhd/cechy/` | `audhd_opracowanie_v6_0_2026-07-01-2.html` | AuDHD u dorosłych — cechy i wzorce funkcjonowania (v6.0) |
| `audhd/co-to-znaczy/` | `co-to-znaczy-audhd-v03_01-2026-07-09-2.html` | Co to znaczy, że mam AuDHD — krótki przewodnik dla bliskich |
| `audhd/fundatorzy-it/` | `audhd-fundatorzy-it-1_00-2026-04-27.html` | AuDHD a osoby fundatorskie w IT — hipoteza i jej cztery warstw |
| `audhd/ilu-nas/` | `ilu-nas-jest-audhd-polska-wstep-v03_00-2026-08-10.html` | Ilu w Polsce jest osób z AuDHD? Wstęp do oszacowania - v03.00 |
| `audhd/jezyki-milosci/` | `piec-jezykow-milosci-nd-v01.00-2026-05-18.html` | Pięć neurodywergentnych języków miłości — i dlaczego nie są wa |
| `audhd/kognitywistyka-ai/` | `kognitywistyka-ai-bledy-poznawcze-2_00-2026-04-28.html` | Kognitywistyka, AI i błędy poznawcze — obserwacje o pamięci, k |
| `audhd/mapa/` | `SOL_mapa-sekcji-i-anchorow-audhd.html` | Mapa sekcji i anchorów AuDHD |
| `audhd/mowienie/` | `autyzm-regulacja-mowienia-v01.00-2026-05-14.html` | Autyzm i regulacja mówienia — teza i mechanizm |
| `audhd/obiektywnosc/` | `obiektywnosc-autyzm-v01.00-2026-05-14.html` | Obiektywność osoby autystycznej — teza i mechanizm |
| `audhd/pamiec-esej/` | `ESEJ_architektury-pamieci-1_02-2026-04-28.html` | Architektury pamięci — od pamięci RAM lat 80. do mózgów neuror |
| `audhd/pamiec-powiesc/` | `POWIESC_architektury-pamieci-2_00-2026-04-29.html` | Architektury pamięci — opowieść o tym, kto naprawdę zbudował I |
| `audhd/po-diagnozie/` | `CLAUDE_co-dziala-po-poznej-diagnozie-02_01-2026-08-26.html` | Co działa po późnej diagnozie — 02.01 |
| `audhd/po-ludzku/` | `audhd-po-ludzku-v02_02-2026-07-09.html` | AuDHD po ludzku — v02.02 |
| `audhd/pomaganie/` | `adhd-pomaganie-kosztem-siebie-v01.00-2026-05-14.html` | ADHD i pomaganie kosztem siebie — teza i mechanizm |
| `audhd/psychodynamika-cbt/` | `psychodynamika-kopie-cbt-tresuje-01_03.html` | Psychodynamika kopie, CBT tresuje, pacjent płaci — 01.03 |
| `audhd/publikacje/` | `dluga-lista-publikacji-4.01-2026-08-26.html` | Długa lista publikacji — 4.01 |
| `audhd/rdzen-czy-maskowanie/` | `63-cechy-rdzen-czy-maskowanie-01_01-2026-08-26.html` | 63 cechy — rdzeń czy maskowanie — 01.01 |
| `cv/cv/` | `CLAUDE_Maciej-Tora-AI-CV.html` | Maciej Tora — CV |
| `cv/seventeen-and-seventeen/` | `CLAUDE_seventeen-and-seventeen-ai-concepts-EN.html` | Seventeen &amp; Seventeen — AI concepts from the postings and  |
| `piosenki/brzmienie/index-en.html` | `audio-en.html` | Sound map — Depth, Light and Motion |
| `piosenki/brzmienie/` | `audio.html` | Mapa brzmienia — Głębia, Światło i Ruch |
| `piosenki/dlaczego-trzy-wyspy/` | `SOL-klastrowanie-audio-dlaczego-3-wyspy.html` | Dlaczego trzy wyspy? — mapa brzmienia |
| `piosenki/dwa-modele-mapy/` | `SOL-klastrowanie-audio-hipotezy-robocze.html` | Dwa modele mapy brzmienia |
| `piosenki/kamien-milowy-audio/` | `SOL-kamien-milowy-piosenki-audio-sanityzacja.html` | Kamień milowy — dwa zbiory piosenek / sanityzacja audio 1.0 |
| `piosenki/mapa-brzmienia/` | `SOL-klastrowanie-audio-mapa-3-wysp-opis.html` | Mapa brzmienia — 3 wyspy |
| `piosenki/osie/` | `osie-sumy.html` | Osie znaczeniowe — wystąpienia |
| `piosenki/playlisty/index-en.html` | `playlisty-en.html` | Playlists |
| `piosenki/playlisty/` | `playlisty.html` | Playlisty |
| `piosenki/porownanie-hipotez/` | `SOL-klastrowanie-audio-analiza-hipotez.html` | Krajobraz zamiast klastrów — porównanie hipotez |
| `piosenki/rodziny/` | `rodziny-sumy.html` | Rodziny znaczeniowe — wystąpienia |
| `piosenki/slowa/index-en.html` | `slowa-en.html` | Lyrics — song text analysis |
| `piosenki/slowa/` | `slowa.html` | Słowa — analiza tekstów piosenek |
| `piosenki/sygnatury-wysp-metoda/` | `SOL-klastrowanie-audio-sygnatury-wysp-metoda.html` | Jak opisano trzy wyspy brzmienia |
| `piosenki/sygnatury-wysp/` | `SOL-klastrowanie-audio-sygnatury-wysp-analiza.html` | Sygnatury trzech wysp — Głębia, Światło i Ruch |
| `piosenki/tagi/` | `tagi-sumy.html` | Tagi semantyczne — wystąpienia |
| `piosenki/wyniki-dwa-glosy/index-en.html` | `SOL-audio-clustering-three-island-signatures-two-voices-en.html` | Three-island signatures — results in two voices |
| `piosenki/wyniki-dwa-glosy/` | `SOL-klastrowanie-audio-wyniki-dwa-glosy.html` | Sygnatury 3 wysp — wyniki na dwa głosy |
| `rosja/audyt/` | `a5_ZAMROZONE-audyt-2rewizje-v03_00-2026-06-23-anchory.html` | ZAMROZONE · audyt kolumbryny — dwie rewizje · v03.00 |
| `rosja/dark-legitimacy/` | `d1-zamrozone-narzedzie-dark-legitimacy-horbyk-v01_00-2026-03-25-anchory.html` | ZAMROZONE · Dark legitimacy: What Russia and Ukraine reveal ab |
| `rosja/disinfolklore-swot/` | `d3-zamrozone-narzedzie-disinfolklore-swot-advocatus-v01_00-2026-03-25-anchory.html` | ZAMROZONE · Disinfolklore — Analiza SWOT · Advocatus Diaboli · |
| `rosja/disinfolklore/` | `d2-zamrozone-narzedzie-disinfolklore-kompilacja-v01_00-2026-03-25-anchory.html` | ZAMROZONE · Disinfolklore — Kompilacja Głównych Tez · v01.00 |
| `rosja/gradually-suddenly/` | `a2_ZAMROZONE-maj-2026-gradually-stalo-sie-suddenly-v25_00-2026-06-25.html` | ZAMROZONE · maj 2026. gradually stalo sie suddenly · v25.00 |
| `rosja/jak-koncza-sie-panstwa/` | `a7_ZAMROZONE-jak-koncza-sie-panstwa-v02_00-2026-06-28.html` | ZAMROZONE · jak koncza sie panstwa · v02.00 |
| `rosja/jalta-3-apendyks/` | `d7-zamrozone-jalta-3-apendyks-v01_00-2026-03-08-anchory.html` | ZAMROZONE · Jałta 3.0 — Apendyks: Dlaczego to zadziała(ć może) |
| `rosja/jalta-3/` | `d6-zamrozone-jalta-3-analiza-strategiczna-v01_00-2026-03-08-anchory.html` | ZAMROZONE · Jałta 3.0 — Analiza Strategiczna · v01.00 |
| `rosja/kolumbryna/` | `a1_POCZATEK_ZAMROZONE_kolumbryna-v3_5-2026-03-31-anchory.html` | Kolumbryna — Wielka analiza systemowa · v3.5 · 31 marca 2026 |
| `rosja/lista-celow/` | `a3_ZAMROZONE-lista-celow-v19_00-2026-06-25.html` | ZAMROZONE · lista celów · v19.00 |
| `rosja/mapa-sekcji/` | `SOL_mapa-sekcji-z-opisami.html` | Mapa sekcji z opisami |
| `rosja/mapa/index-en.html` | `SOL_mapa-tematow-rozpad-rosji-EN-v01_00-2026-09-07.html` | Topic map of the “Collapse of Russia” corpus |
| `rosja/mapa/` | `SOL_mapa-tematow-korpusu-rozpad-rosji-v01_01-2026-09-03.html` | Mapa tematów korpusu „Rozpad Rosji” |
| `rosja/monopole/` | `monopole-moralnosc-transformacja-zrodla-v01_00-2026-03-17-anchory.html` | Monopole, moralność i transformacja: analiza źródłowa aspektów |
| `rosja/przejscie-na-hurt/` | `a4_lipiec-2026-przejscie-na-hurt-v20_11-2026-08-01.html` | lipiec 2026. przejscie na hurt — v20.11 |
| `rosja/putin-cornered/` | `d5-zamrozone-putin-cornered-animal-v03_00-2026-03-24-anchory.html` | ZAMROZONE · Putin — chytry plan? cornered animal edition · v03 |
| `rosja/ropa-gaz/` | `ropa-gaz-geopolityka-analiza-v01_00-2026-03-17-anchory.html` | Ropa, gaz i geopolityka: analiza strukturalna popytu i trwałoś |
| `rosja/rosyjskie-samobojstwa/` | `d4-zamrozone-rosyjskie-samobojstwa-taksonomia-v08_01-2026-06-13-anchory.html` | ZAMROZONE · Taksonomia rosyjskiego samobójstwa — katalog metod |
| `rosja/zapas-kontra-strumien/` | `a6_ZAMROZONE-zapas-kontra-strumien-v02_00-2026-07-03.html` | ZAMROZONE · zapas kontra strumień · v02.00 |
| `rownania/dziesiec-rownan/index-en.html` | `CLAUDE_equations-metaphysics-and-rigged-jury-EN.html` | Ten equations, metaphysics, and a jury packed with friends — w |
| `rownania/dziesiec-rownan/` | `CLAUDE_rownania-metafizyka-i-komisja.html` | Dziesięć równań, metafizyka i komisja po znajomości — z uwagam |
| `rownania/navier-stokes/index-en.html` | `navier-stokes-essay-for-non-mathematician-EN.html` | Navier–Stokes, AI, and the Dispute over Credit — an Essay for  |
| `rownania/navier-stokes/` | `navier-stokes-esej-dla-niematematyka.html` | Navier–Stokes, AI i spór o autorstwo — esej dla niematematyka |
| `techniczne/explorer/` | `content-explorer.html` | Content Explorer · Rosja + AuDHD |
| `techniczne/sql/` | `sql-viewer.html` | Techniczne · viewer SQL |

---

## 5. Łatki na adresy rozesłane — 4

Stuby stojące pod **starą, wersjonowaną nazwą pliku**. Nie są wejściami i strażnik ich
za wejścia nie liczy. Istnieją wyłącznie dlatego, że te konkretne adresy zostały wysłane
ludziom, zanim powstały wejścia katalogowe — i nie mogą umrzeć.

**Nowych takich nie tworzymy.** Pozostałe 17 zostało skasowanych 2026-09-20, bo tamtych
adresów nikt nigdy nie dostał.

| stary adres | prowadzi do |
|---|---|
| `rownania/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html` | `CLAUDE_equations-metaphysics-and-rigged-jury-EN.html` |
| `rownania/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html` | `CLAUDE_rownania-metafizyka-i-komisja.html` |
| `rownania/navier-stokes-esej-dla-niematematyka-v02_00-2026-09-09.html` | `navier-stokes-esej-dla-niematematyka.html` |
| `rownania/navier-stokes-essay-for-non-mathematician-EN-v02_00-2026-09-09.html` | `navier-stokes-essay-for-non-mathematician-EN.html` |

---

## 6. Co celowo NIE ma wejścia

| co | ile | dlaczego |
|---|---|---|
| szablony Jinja `piosenki/templates/` | 7 | to nie są strony, tylko fragmenty renderowane przez Flaska |
| `osierocone-html/` | 4 | cmentarz migawek; nie publikujemy archiwum |
| `dokumentacja-archiwalna/` | 3 | decyzja autora 2026-09-20: archiwum bez publicznego wejścia |
| oryginały bez kotwic w `rosja/` | 11 | bliźniaki `-anchory` mają już adresy; drugi łamałby regułę 3 |

Te z nich, które reguła 4 mimo to łapie, siedzą na `.github/stable-www-allowlist.txt`
z uzasadnieniem — obecnie 12 pozycji.

---

## 7. Jak odtworzyć ten spis

Nie przepisywać ręcznie. Tabele w sekcjach 4 i 5 są **wygenerowane ze stanu faktycznego**
przez przejście po wszystkich plikach HTML i odczytanie celu z `location.replace`.
Przy większej zmianie adresów wygenerować na nowo, a nie poprawiać wiersz po wierszu.

---

Stan na 2026-09-20: 176 plików HTML, 67 stubów, 63 wejść stałych, 4 łatek.
Stworzono z pomocą Claude (Anthropic), wariant: Claude Opus 5.
