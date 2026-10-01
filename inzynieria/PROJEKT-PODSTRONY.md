# Inżynieria — projekt podstrony

**Wersja 01.00 · 2026-10-01**

Dokument projektowy, nie strona. Zbiera ustalenia z rozmowy z 1 października 2026.
Budowa zaczyna się dopiero na polecenie użytkownika. Powód: użytkownik chce najpierw
wymyślić i zaprojektować całość, a dopiero potem robić.

## 1. Decyzje użytkownika

| Sprawa | Decyzja |
|---|---|
| Miejsce w witrynie | nowe, siódme drzwi na stronie głównej, osobne od drzwi 06 „Techniczne” |
| Katalog | `inzynieria/` |
| Języki | EN i PL, para `index-en.html` i `index.html`, jak w całej witrynie |
| Podprojekty | 1) chłodzenie domu wodą ze studni, 2) prąd i rozdzielnice, 3) filtracja wody ze studni |
| Dane rozdzielnic | publikowane w całości, bez adresów domów |
| Domy | dwa: Kraków i Gdańsk; w każdym parter, 1. piętro i strych; instalację w obu przerobił użytkownik |
| Przeliczenie chłodzenia | później, osobnym etapem |

Szkic adresów, do potwierdzenia przy budowie: `inzynieria/chlodzenie/`,
`inzynieria/rozdzielnice/`, `inzynieria/filtracja/`. Na stronie głównej zmienia się
hasło „Sześć dróg do tej samej głowy” na „Siedem”, a w wersji EN „Six” na „Seven”.

Wygląd: zgodny z resztą witryny, czyli ciemne tło, bursztynowe akcenty i duży przełącznik
języka. Gatunek tekstu: jak esej o Navier-Stokesie „dla niematematyka”, czyli obliczenia
i mechanizmy pokazane krok po kroku zrozumiałym językiem.

## 2. Podprojekt: chłodzenie wodą ze studni

Źródło: projekt „Chłodzenie studzienne domu” v04.01 z 26.06.2026, w archiwum PRA-PLIKI.
Zakłada 10 kW chłodu z wody studziennej 8 °C przez istniejące grzejniki CO z wiatrakami,
przy ~0,11 kW prądu.

Zanim projekt trafi na stronę, trzeba go sprawdzić. Użytkownik podejrzewa zbyt
optymistycznie policzoną oszczędność prądu. Miejsca do sprawdzenia:

1. **Moc grzejników przy chłodzeniu.** Grzejnik zaprojektowany na różnicę temperatur
   40–50 K przy różnicy ok. 12 K daje kilkanaście procent mocy nominalnej. 10 kW z 18
   grzejników, nawet z wiatrakami, jest wątpliwe.
2. **Pominięty pobór prądu.** W bilansie brakuje trzech pomp piętrowych CO, które latem
   musiałyby pracować razem z chłodzeniem.
3. **Wydajność studni przy pracy ciągłej.** Dopływ ≥1,5 m³/h oceniono jednym testem
   (90 l w 3,5 minuty). Przy wielogodzinnej pracy woda w studni może się nagrzewać.
4. **Porównanie z klimatyzatorem** — liczyć przy tej samej faktycznej mocy chłodzenia.

## 3. Podprojekt: prąd i rozdzielnice

### 3.1. Założenie

System od zera: dane instalacji w SQL, z nich rysunki i kontrole. Strona opisuje całą
drogę — od spisania instalacji, przez przechowywanie w SQL, po rysowanie. Rysunki mają
być ładne, nie nudne jak w AutoCAD.

Punkt wyjścia już istnieje. Dokumentacja „Rozdzielnica 1. piętro” v2.10 (Kraków) ma
listę A (elementy z przyłączami), listę B (przewody: skąd, dokąd, przekrój, kolor)
i widok „ścieżka obwodu” wyliczany z obu. System formalizuje ten układ.

### 3.2. Dane w SQL

| Tabela | Zawartość |
|---|---|
| `domy` | dom (miasto, bez adresu) i kondygnacje |
| `rozdzielnice` | dom, kondygnacja, obudowa (np. Hager FWB31S), rzędy, liczba modułów |
| `aparaty` | typ, parametry (np. B16, C25, 30 mA, 63 A), rząd i pozycja na szynie DIN, szerokość w modułach, **rola**, **charakterystyka** |
| `zaciski` | przyłącza aparatu w konwencji G1, G2… (góra) i D1, D2… (dół) |
| `przewody` | od zacisku do zacisku: przekrój, kolor izolacji, kabel, **długość**, **sposób ułożenia** |
| `obwody` | numer, przeznaczenie (gniazdka, światło, kuchenka), pomieszczenie, faza |

Rola aparatu (pole osobne od typu):

- **ochrona przed zwarciem** — wyłączniki B na obwodach;
- **pilnowanie obciążalności grupy** — np. C25 przed grupą: suma wyłączników za nim
  (B20 + B16 + B10 = 46 A) przekracza 25 A, więc C25 ogranicza całą grupę i chroni
  wyłącznik różnicowoprądowy 40 A, który sam nie ma zabezpieczenia nadprądowego;
- **ochrona przed upływem** — wyłącznik różnicowoprądowy 30 mA;
- **odłączanie** — rozłącznik (np. SBN 363), nie zabezpieczenie.

Widoki SQL (wyliczane, nie wpisywane ręcznie): ścieżka obwodu od zasilania do odbiornika,
drzewo zabezpieczeń, kontrole spójności i doboru (punkt 3.5).

### 3.3. Rysunki

1. **Widok z przodu rozdzielnicy** — rzędy szyny DIN w skali (moduł 18 mm), aparaty
   z opisami, przewody w prawdziwych kolorach: brązowy, czarny, szary, niebieski,
   żółto-zielony.
2. **Schemat jednokreskowy jako drzewo** — zasilanie, rozdzielnica główna, kondygnacje,
   grupy, wyłączniki różnicowoprądowe, nadprądowe, obwody.
3. **Symulacja awarii** — czytelnik klika miejsce awarii, schemat podświetla, co się
   wyłączy, a co dalej działa. Obok porównanie z typową instalacją.

Rysowanie w przeglądarce z danych (SVG), w stylu witryny. Najechanie na aparat pokazuje
jego parametry i rolę.

### 3.4. Symulacja: trzy rodzaje awarii

| Awaria | Co wykrywa | Co się wyłącza |
|---|---|---|
| Upływ (przebicie, woda) | wyłącznik różnicowoprądowy | tylko wyłącznik różnicowoprądowy grupy z tym obwodem |
| Zwarcie | wyzwalacz elektromagnetyczny (B: 3–5×In, C: 5–10×In) | gałąź od miejsca awarii w górę, do aparatu grupowego (C25) włącznie |
| Przeciążenie | wyzwalacz termiczny, z opóźnieniem | tylko aparat, którego próg przekroczono |

Uczciwie o zwarciu. Przy zwarciu zwykle wyłączają się i B, i C25 przed nim: prąd zwarcia
ma setki amperów, czyli więcej niż natychmiastowe progi obu aparatów. Selektywność w czasie
jest więc słaba. Rozłącznik nie zadziała nigdy. Zabezpieczenie przedlicznikowe zwykle nie,
bo wyłącznik przerywa zwarcie w kilka milisekund. Wyłącznik różnicowoprądowy zadziała przy
zwarciu faza–PE (prąd ucieka przez PE), a przy zwarciu faza–N nie (prąd wraca przez N).

Zysk z projektu bierze się z **podziału na grupy**, nie z szybszego zadziałania B:
przy zwarciu gaśnie jedna grupa, a nie cały dom.

### 3.5. Automatyczne kontrole

Dla każdego obwodu, z danych SQL. Wynik: zielony, żółty (na granicy) albo czerwony,
z wyjaśnieniem:

- prąd obciążenia ≤ prąd znamionowy wyłącznika ≤ obciążalność przewodu (zależna od
  przekroju i sposobu ułożenia);
- typowe pułapki: 1,5 mm² za B16 na granicy przy niekorzystnym ułożeniu, za B20 za mało;
- suma za aparatem grupowym a jego prąd znamionowy;
- wyłącznik różnicowoprądowy nie mniejszy niż ochrona przed nim;
- prąd zwarcia na końcu obwodu wystarczający do natychmiastowego zadziałania B
  (wymaga długości przewodu; bez niej kontrola szacunkowa);
- **N każdego obwodu wraca przez ten sam wyłącznik różnicowoprądowy co jego faza**
  (punkt 3.6).

### 3.6. Dlaczego każda faza ma własny wyłącznik różnicowoprądowy

W domach nie ma prawdziwych odbiorników trójfazowych. Płyta „trójfazowa” to trzy osobne
pola jednofazowe. Wystarczą więc trzy wyłączniki różnicowoprądowe dwubiegunowe
(faza + N), po jednym na fazę, zamiast jednego czterobiegunowego. Upływ na jednej fazie
wyłącza jedną grupę, a nie wszystkie trzy fazy.

Warunek, który strona musi podać wprost, żeby nikt nie skopiował rozwiązania na ślepo:
każda faza ma **własny przewód N**, prowadzony przez ten sam wyłącznik różnicowoprądowy
co ona. Wspólny N dla kilku faz (np. zworki N w zacisku płyty indukcyjnej) powoduje
wybijanie wyłączników bez awarii. Zworki trzeba wtedy zdjąć i podłączyć osobne N,
zgodnie z instrukcją producenta.

### 3.7. Rozdział na stronie: „Co się dzieje, gdy coś pójdzie nie tak”

Dla czytelnika bez wykształcenia elektrycznego, każdy punkt powiązany z symulacją:

1. trzy rodzaje awarii i trzech różnych strażników;
2. kto pilnuje czego: B, aparat grupowy, wyłącznik różnicowoprądowy, rozłącznik;
3. uczciwie o zwarciu i o tym, skąd naprawdę bierze się zysk;
4. zwarcie faza–N a faza–PE;
5. dlaczego wyłącznik różnicowoprądowy na każdą fazę i warunek osobnego N;
6. porównanie z typową instalacją: jeden wyłącznik różnicowoprądowy na dom, ciemno wszędzie.

### 3.8. Materiały

W archiwum PRA-PLIKI:

- Kraków, rozdzielnica główna: „Dom Mamy — arkusz obciążenia i schemat rozdzielnicy”,
  „Dom Mamy — schemat rozdzielnicy elektrycznej”, „Dom Mamy — specyfikacja i widoki
  rozdzielnicy”;
- Kraków, 1. piętro: „Rozdzielnica pierwszego piętra” — wersje 1.0, 1.2, 2.5, 2.6, 2.10
  (najpełniejsza 2.10 z 13.04.2026, część zacisków nadal „—”).

Brakuje: Kraków — strych (jest tylko kabel 5×2,5 mm² do tamtejszej rozdzielnicy);
Gdańsk — wszystkie trzy kondygnacje.

Przy przenoszeniu na stronę usuń z dokumentów adresy i imiona osób, bo dane są
publiczne, a użytkownik zgodził się na publikację wyłącznie bez adresów.

## 4. Podprojekt: filtracja wody ze studni

Materiałów jeszcze nie ma — w PRA-PLIKI brak dokumentu o filtracji wody. Dostarczy je
użytkownik.

## 5. Otwarte decyzje użytkownika

1. Która baza dla danych rozdzielnic: baza pierwszego repozytorium czy `hue-nexus-sql`
   drugiego. Danych między bazami nie przenosi się bez polecenia użytkownika.
2. Od której rozdzielnicy zacząć (najpełniejsze dane: Kraków, 1. piętro).
3. Czy symulacja awarii wchodzi do pierwszej wersji.
4. Podpis domów na stronie: miasto (Kraków, Gdańsk) czy neutralnie (dom A, dom B).
5. Ostateczne nazwy adresów podstron.

## 6. Kolejność prac

1. Decyzje z punktu 5.
2. Sprawdzenie obliczeń chłodzenia.
3. Zebranie brakujących materiałów rozdzielnic i filtracji.
4. Projekt wyglądu.
5. Budowa — na polecenie użytkownika, etapami, każdy etap do akceptacji.
