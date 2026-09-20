# INSTRUKCJA DLA AGENTÓW — CLAUDE I SOL

Wersja: 01.00 · Data: 2026-09-20
Status: **OBOWIĄZUJĄCA — PRZECZYTAĆ PRZED PIERWSZĄ OPERACJĄ**
Dotyczy: Claude (Anthropic) i SOL (ChatGPT), oraz każdego innego modelu pracującego tu w przyszłości

---

## 0. Zanim cokolwiek zrobisz

Przeczytaj w tej kolejności. Nie na wyrywki, nie po tytułach.

| # | plik | po co |
|---|---|---|
| 1 | `SOT-SOA-AKTUALNA.md` | gdzie są źródła prawdy i co rozstrzyga przy sprzeczności |
| 2 | `ZASADA-TYLKO-SQL.md` | jedyne dozwolone źródło danych |
| 3 | `ZASADA-BEZ-DODATKOWYCH-SPRAWDZEN.md` | zakaz rozszerzania zakresu |
| 4 | `SOL_DOKUMENTACJA-KATALOGI-AKTUALNA.md` 0.1 | konwencja adresów |
| 5 | `SOL_DOKUMENTACJA-STUBY-AKTUALNA.md` | spis wszystkich wejść i procedura wydania |

**Stan faktyczny bije pamięć.** Ścieżki zapamiętane z poprzednich rozmów bywają nieaktualne
— między sesjami zmieniło się już kilkadziesiąt. Sprawdź, zanim zapiszesz.

---

## 1. Adresy — reguła, którą najłatwiej złamać

**Stały jest ADRES, nie nazwa pliku.**

To zdanie ma swoją historię: przez jeden dzień obowiązywało odwrotne, bo przekazano je
jako „nazwy plików zostają stałe". Kosztowało 19 przemianowanych plików, 45 wpisów na
liście wyjątków CI i dwie dokumentacje opisujące regułę na opak. Opis:
`bledy-AI/MACIEK/` wpis 01 i `bledy-AI/CLAUDE/` wpis 06.

W praktyce:

- adres publiczny to **katalog bez wersji**, np. `audhd/psychodynamika-cbt/`;
- nazwa pliku jest **wewnętrzna** — może mieć wersję, datę, autora, `NIE-PUBLIKOWAC`;
- **tylko adres idzie na zewnątrz**, nigdy nazwa pliku;
- przy nowym wydaniu **przepnij stub**, krok po kroku w dokumentacji stubów.

---

## 2. Wersjonowanie dokumentów

Numer `XX.YY` i data `yyyy-mm-dd` **w nagłówku dokumentu**, nie tylko w nazwie pliku.
Drobna korekta podnosi `YY`, przebudowa `XX`. Wiążący jest jawny zapis `Wersja: XX.YY`
z dwukropkiem — numer doklejony do `<title>` to ozdobnik i bywa nieodświeżony.

Podnoś wersję **przy każdej zmianie treści.** Także wtedy, gdy zmiana wydaje się drobna.

---

## 3. Dane

Jedynym źródłem jest **SQL** — Supabase, projekt `maciekGithubHue`. CSV, XLSX, TSV i pliki
`.py` obok bazy są wejściem albo wyjściem, **nigdy odpowiedzią**. Bez wyraźnej zgody
użytkownika nie wolno ich nawet otwierać jako źródła.

Drugi projekt na koncie, `hue-nexus-sql`, **nie jest nasz**. Należy do innego repozytorium.

---

## 4. Zakres

**Rób to, o co poproszono. Nic więcej.**

Żadnych audytów „przy okazji", żadnych dodatkowych sprawdzeń „na wszelki wypadek", żadnego
porządkowania sąsiednich plików, bo akurat się nawinęły. Jeśli widzisz problem poza
zakresem — **zgłoś go, nie naprawiaj**. Tak powstały cztery rozbieżności w sekcji 7
dokumentu SOT/SOA: wypisane, nie ruszone.

---

## 5. Sprzeczność = pytanie, nie wybór

To jest reguła, której złamanie kosztowało najwięcej.

**Jeśli polecenie jest sprzeczne z wcześniej zapisaną zasadą tego samego człowieka —
zapytaj, które obowiązuje.** Nie wybieraj. Nie wykonuj tego, co brzmi świeżej. Nie buduj
uzasadnienia dla wykonanego polecenia.

Znasz brzmienie obu zdań i nie znasz intencji. Zauważenie sprzeczności i wykonanie mimo to
jest **gorsze niż przeoczenie**, bo dowodzi, że informacja była i została odłożona.

Nie chodzi o dopytywanie przy każdym poleceniu. Chodzi o przypadek, w którym **dwa zdania
tego samego człowieka nie mogą być prawdziwe naraz.**

---

## 6. Deklaracja o własnej pracy jest twierdzeniem empirycznym

„Przeczytałem", „sprawdziłem", „zweryfikowałem" — to są liczby, nie wrażenia. Gdy pomiaru
nie ma, właściwą odpowiedzią jest **„nie wiem, ile przeczytałem"**.

Nie raportuj jako zrobione czegoś, czego nie zmierzyłeś. `bledy-AI/CLAUDE/` wpis 01 opisuje,
jak wygląda „przeczytane w całości" przy 20,4% przeczytanego.

---

## 7. Przed zapisem

- [ ] `python3 .github/scripts/check_stable_www.py` — musi być zielone;
- [ ] obejrzyj listę plików, które faktycznie idą do commita, zwłaszcza po `git add -A`;
- [ ] wersja podniesiona, jeśli zmieniła się treść;
- [ ] stub przepięty, jeśli powstało nowe wydanie;
- [ ] nic poza zakresem zadania.

Strażnik sprawdza **siedem reguł**: martwe linki, przekazywanie `#kotwicy`, kopie treści pod
dwoma adresami, wejście dla pliku z wersją w nazwie, aktualność wydania, zgodność numerów
oraz linki w dokumentacji.

**Zielone CI znaczy tylko, że reguły nie zostały złamane. Nie znaczy, że treść jest dobra
— tego nie ocenia nikt.**

---

## 8. Zadania jednorazowe

Workflow, skrypt albo import wykonany raz **musi się sam wyłączyć albo zostać usunięty**.
Dwa razy tak nie było i dwa razy skończyło się zadaniem-zombie: jedno odpalało się przy
każdym pushu bez efektu przez 78 commitów, drugie czekało na warunek, który nie mógł zajść.

---

## 9. Półka wstydu

`bledy-AI/` — trzy szuflady: Claude, SOL i Maciek. Rejestr jest jawny i prowadzony
z liczbami, nie z przeprosinami.

**Gdy popełnisz błąd, który kosztował czas albo wymagał cofania zmian — dopisz go.**
Z liczbą, z cytatem polecenia w brzmieniu, w jakim padło, i z regułą, która z niego wynika.
Rejestr bez liczb osuwa się w gatunek literacki, w którym autor wypada sympatycznie.

---

Stworzono z pomocą Claude (Anthropic), wariant: Claude Opus 5.
