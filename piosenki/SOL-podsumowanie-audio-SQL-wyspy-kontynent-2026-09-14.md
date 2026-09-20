# SOL — uzupełnienie audio, SQL i analiza mapy brzmienia

Data prac i stanu opisanego w tym podsumowaniu: **2026-09-14**.

Ten dokument podsumowuje działania wykonane w rozmowie: pobranie brakujących nagrań, przypisanie ich do katalogu, zapis pomiarów audio, kontrolę spójności tabel oraz późniejszą ocenę nowych nagrań względem historycznych wysp i analizę kontynentu. Liczby są stanem po zakończeniu opisanych prac, nie licznikiem aktualizowanym automatycznie.

## 1. Ustalenia użytkownika

- Nie wymagamy pełnego pokrycia biblioteki audio. Pozostałe trudne przypadki mogą poczekać.
- Mocne dopasowanie wykonawcy i tytułu na poziomie około 90% jest wystarczające. To deklaracja akceptowanego poziomu pewności, a nie zmierzony wynik algorytmu.
- Same nazwy w katalogu często nie pozwalają potwierdzić konkretnej edycji w 100%.
- Oryginał/remaster nie stanowi przeszkody w dopasowaniu na potrzeby tej analizy. Nie oznacza to identyczności sygnałów obu wersji.
- Większość wyborów nagrania może wykonywać skrypt na podstawie nazwy i wykonawcy. Według obserwacji użytkownika około 90% przypadków odpowiadało pierwszemu wynikowi, a dalsze około 5% drugiemu. To obserwacja z ręcznej pracy, nie formalny benchmark.
- Istniejących wysp i przypisań nie przeliczamy ani nie nadpisujemy. Późniejsza ocena nowych nagrań jest osobną analizą porównawczą.

## 2. Pobieranie i przypisanie audio

Pobieranie wykonano lokalnie na laptopie, partiami. Pobrano **203 z 211** brakujących nagrań. Osiem niepobranych przypadków odłożono. Wszystkie pobrane pliki sprawdzono przez pełne dekodowanie; zapisano parametry techniczne i skróty SHA-256.

Zaakceptowano **199 przypisań** do istniejących utworów:

- **184 nowe pliki** dodano do tabeli audio;
- **15 istniejących plików** wykorzystano ponownie;
- **4 pobrane pliki** odłożono jako wyraźnie błędne dopasowania.

Końcowy import obejmował 176 dopasowań high i 23 zaakceptowane przypadki review. Dla review dodano opisy różnic i odpowiednie wpisy relacyjne. Nie wymuszano dodatkowych opisów dla zwykłych dopasowań.

Zaktualizowano instrukcję pobierania/przypisywania audio o powyższe zasady. Pliki dźwiękowe pozostały lokalnie; zapis metadanych i wyników w SQL nie oznacza przesłania samych nagrań do Supabase.

## 3. Ostrożny import do SQL

Import przygotowano na podstawie manifestu, z kontrolą stanu przed zmianą, kopią danych potrzebnych do audytu i możliwością wycofania opisanej partii. Wykonano próby transakcyjne zakończone ROLLBACK oraz kontrole po zapisie.

Główne przypisanie utworu do pliku znajduje się w middle_end. Tabela audio opisuje plik, audio_match_details przechowuje opis zaakceptowanych wyjątków, a audio_middle_end rejestruje przypadki wymagające dodatkowej informacji.

Stan po imporcie:

| Zakres | Liczba |
|---|---:|
| Utwory w middle_end | 1058 |
| Utwory z przypisanym audio | 1046 |
| Utwory bez audio, odłożone | 12 |
| Pliki w audio | 1040 |

Liczba utworów i plików może być różna: ten sam plik może obsługiwać więcej niż jeden rekord katalogowy.

## 4. Analiza spektralna nowych plików

Przed wykonaniem pomiarów odczytano historyczne pliki MD i HTML na GitHubie. Użyto ekstraktora **v05** i jego pełnego zestawu **185 cech/parametrów** istniejącego schematu, obejmującego widmo, pasma, amplitudę, stereo, MFCC, chromę i rytm.

Podstawowe parametry:

- dekodowanie do 48 kHz, stereo, float32;
- STFT: FFT 4096, hop 2048, okno Hann;
- chroma: FFT 16384, hop 4096;
- rytm: okno 2048, hop 256, zakres BPM 40–220.

Wykonano **184 analizy**, wszystkie zakończone poprawnie. Dla dziewięciu nagrań trwających co najmniej 700 sekund użyto adaptera ograniczającego zużycie RAM: mapowanie zdekodowanego PCM na dysku i blokowe statystyki amplitudy. Rdzeń obliczeń spektralnych, chromy i rytmu pochodził z oryginalnego skryptu.

Porównanie adaptera z oryginałem na pliku kontrolnym przeszło dla wszystkich 188 wartości zwracanych przez analizator, przy tolerancji względnej i bezwzględnej 1e-10. Trzy z tych wartości są metadanymi, a pozostałe 185 trafia do istniejących kolumn pomiarowych.

Dodatkowa kontrola wobec starego snapshotu wykazała niewielkie różnice w 26 z 185 pól przy ścisłej tolerancji względnej 1e-6 i bezwzględnej 1e-8; przykładowa różnica spectral_flatness_p10 wynosiła około 0,32%. Nie ustalono przyczyny i nie deklarujemy bitowej identyczności z dawnym środowiskiem. Starych pomiarów nie nadpisano.

## 5. Zapis analiz i kontrola spójności

Do audio_feature_snapshots zapisano **184 nowe rekordy**:

- analyzer_version: v05;
- dataset_version: post-islands-2026-09-14.

Historyczne v08 oznacza wersję wcześniejszego, sanityzowanego zbioru, a nie wersję ekstraktora. Nowa etykieta nie sugeruje automatycznego przejścia takiej samej sanityzacji.

Zapis wykonano w dziesięciu transakcjach, poprzedzonych próbami wycofanymi. Porównano wszystkie pola nowej partii z wynikami lokalnymi oraz skrót zawartości historycznych rekordów.

**Stan końcowy: 1040 snapshotów = 856 historycznych zachowanych bez zmian + 184 nowe.**

Osobna kontrola powiązań potwierdziła:

- wszystkie 184 nowe analizy prowadzą do właściwych rekordów middle_end, zgodnie z manifestem;
- wszystkie 1046 utworów z audio mają dostęp do analizy;
- brak zerwanych odwołań i sprzecznych przypisań;
- identyfikatory YouTube są zgodne między middle_end i audio;
- audio_match_details oraz audio_middle_end są spójne z głównym przypisaniem;
- wszystkie 205 przypadków review mają wymagane opisy i wpisy matched;
- brak duplikatów tej samej wersji snapshotu;
- nie było potrzeby dodatkowej korekty danych.

Cech sygnału nie kopiuje się do middle_end. Utwór korzysta z nich przez powiązanie audio_id.

## 6. Nowe piosenki doszły po utworzeniu wysp

Historyczna mapa powstała na **856 nagraniach**:

| Obszar historyczny | Liczba |
|---|---:|
| Rdzeń Głębi | 166 |
| Rdzeń Światła | 60 |
| Rdzeń Ruchu | 117 |
| Most Głębia–Ruch | 101 |
| Most Światło–Ruch | 46 |
| Most Głębia–Światło | 2 |
| Kontynent / strefa przejściowa | 297 |
| Peryferia | 67 |

Nowe 184 nagrania **nie były wejściem do tamtej analizy**. Najpierw wykonano ich pomiary i zapis, a dopiero później — na kolejne polecenie użytkownika — ocenę podobieństwa do wysp i peryferii oraz analizę starego kontynentu.

## 7. Jak oceniono podobieństwo nowych nagrań

Odczytano zachowane listy obszarów i historyczny zbiór v08. W repozytorium nie znaleziono zapisanego modelu K-means, centrów, kompletnej listy wejściowych cech ani liczbowych progów poprzedniego wykonania.

Dlatego wykonano **nową ocenę podobieństwa do stałych historycznych rdzeni**, a nie dokładne odtworzenie dawnego klasyfikatora.

- Jawnie wybrano trzy zestawy: 22 cechy interpretowalne, 43 rozszerzone oraz 18 kompaktowych. Dobór oparto na udokumentowanych rodzinach cech. Taka sama liczba cech nie oznacza potwierdzenia identyczności z dawnym zestawem.
- Pominięto długość, stereo, surową głośność i parametry techniczne.
- Przycięcie do percentyli 1/99, RobustScaler i PCA do 90% wariancji dopasowano wyłącznie na historycznych 856 nagraniach.
- Prototypy trzech wysp wyznaczono jako średnie współrzędne ich zachowanych rdzeni.
- Nowe nagrania tylko przekształcono i porównano z dawną przestrzenią.

Propozycja wyspy wymagała jednoznacznej bliskości prototypu, położenia w zasięgu jego historycznego rdzenia, zgodności co najmniej 12 z 15 najbliższych przykładów rdzeni oraz niewystępowania na rzadkim skraju biblioteki.

Dokładne reguły tego rozszerzenia:

1. Wyspa: stosunek odległości do pierwszego/drugiego prototypu nie większy niż historyczny percentyl 40; odległość od prototypu nie większa niż percentyl 95 jego rdzenia; zgodność sąsiadów co najmniej 80%; gęstość mieszcząca się w historycznej granicy.
2. Peryferia: odległość do 10. historycznego sąsiada większa niż historyczny percentyl 90.
3. Most: pozostały przypadek o stosunku odległości od percentyla 80 wzwyż; kierunek wynika z dwóch najbliższych prototypów.
4. Kontynent: pozostałe przypadki.
5. Wynik końcowy: zgodność co najmniej dwóch z trzech reprezentacji; przy trzech różnych propozycjach pozostawiono wynik niejednoznaczny.

Są to **reguły nowej oceny**, nie odzyskane granice dawnego modelu. Zgodność 3/3 nie jest prawdopodobieństwem, a zestawy częściowo współdzielą cechy.

Walidacja 5 × 5 na dawnych rdzeniach dała balanced accuracy 98,0–99,0%. Sprawdza ona rozpoznawanie charakteru rdzeni, nie trafność granic między wyspą, mostem, kontynentem i peryferiami.

Nie znaleziono nieskończonych ani brakujących cech. Osiem nowych nagrań miało co najmniej pięć z 22 cech poza historycznymi percentylami 1/99; oznaczono to diagnostycznie, bez odrzucania nagrań. Nie wykonano nowej pełnej sanityzacji katalogowej ani odsłuchowej. Nietypowość akustyczna nie oznacza błędnego dopasowania.

## 8. Wynik dla 184 nowych nagrań

| Propozycja | Liczba |
|---|---:|
| Głębia | 23 |
| Ruch | 25 |
| Światło | 2 |
| Most Głębia–Ruch | 18 |
| Most Ruch–Światło | 7 |
| Kontynent | 85 |
| Peryferia | 19 |
| Niejednoznaczne | 5 |
| **Razem** | **184** |

**50 kandydatów do wysp**, w tym **28 zgodnych we wszystkich trzech reprezentacjach**: Głębia 12, Ruch 15, Światło 1. Pozostałe 22 mają zgodność 2/3.

Dla wszystkich obszarów łącznie zgodność 3/3 dotyczy 80 ze 184 nagrań. Spośród 19 propozycji peryferii dziewięć ma zgodność 3/3.

Przykłady mocnego podobieństwa:

- Głębia: DakhaBrakha — Baby; Roseaux i Melissa Laveaux — You Can Discover; Meditative Mind — Ajai Alai.
- Ruch: Happysad — Bez znieczulenia; Pink Floyd — What Do You Want From Me; SMOLIK / KEV FOX — Run.
- Światło: Męskie Granie Orkiestra — Jammin.

To propozycje analityczne. **Nie zapisano ich jako nowych przypisań w SQL ani nie zmieniono playlist.**

## 9. Analiza historycznego kontynentu

Analizowano dokładnie **297 utworów ze starych list kontynentu**, bez dokładania nowych 85 propozycji.

Grafy symetrycznych 3, 5 i 10 najbliższych sąsiadów dały jeden komponent obejmujący wszystkie 297 utworów, w każdej z trzech reprezentacji. To wskazuje na ciągłość przy badanej skali sąsiedztwa, ale samo w sobie nie dowodzi jednorodności.

Najbliższy kierunek w reprezentacji interpretowalnej:

| Najbliższa wyspa | Liczba |
|---|---:|
| Ruch | 157 |
| Głębia | 122 |
| Światło | 18 |

Dla **256 z 297 utworów (86,2%)** wszystkie reprezentacje wskazują tę samą najbliższą wyspę. Kierunek nie oznacza przeniesienia utworu do rdzenia.

Mediany brzmienia według najbliższego kierunku:

| Kierunek | Bas 20–250 Hz | Góra 4–20 kHz | Centroid | Entropia chroma |
|---|---:|---:|---:|---:|
| Głębia | 58,8% | 0,71% | 1871 Hz | 0,285 |
| Ruch | 54,6% | 1,88% | 2594 Hz | 0,376 |
| Światło | 51,4% | 4,06% | 3278 Hz | 0,402 |

Widać gradient od większej masy basowej i skupienia harmonii do jaśniejszego, bardziej rozproszonego brzmienia. To opis tych samych danych, nie niezależny dowód grup.

Sprawdzono podziały K-means na 2–6 regionów i stabilność w 20 losowaniach 80% zbioru. Dla k=2:

| Reprezentacja | Silhouette | Stabilność ARI |
|---|---:|---:|
| Interpretowalna | 0,176 | 0,935 |
| Rozszerzona | 0,339 | 0,973 |

Mimo wysokiej stabilności wewnątrz reprezentacji, **zgodność obu podziałów k=2 wynosi tylko ARI 0,037**. Dla k=3–6 zgodność między tymi reprezentacjami wynosi 0,307–0,465.

Wniosek: kontynent warto opisywać przez kierunki podobieństwa i lokalne sąsiedztwo. Testowane podziały nie dają wystarczającej podstawy do ogłaszania nowych, odpornych wysp.

## 10. Co zachowano i co pozostaje do decyzji

Zachowano:

- 856 wcześniejszych snapshotów bez zmian;
- historyczne wyspy, mosty, kontynent i peryferia;
- istniejące przypisania i playlisty;
- surowe pomiary nowych nagrań.

Wykonano zapis pomiarów do SQL, ale **późniejsza ocena wysp i kontynentu była tylko analizą**. Ewentualne zatwierdzenie kandydatów, utworzenie playlist czy trwały zapis nowych przynależności pozostają osobnym krokiem. Pozostałe 12 braków audio odłożono zgodnie z decyzją użytkownika.

## 11. Artefakty lokalne i dokumentacja

W katalogu outputs tej rozmowy zachowano:

- audio-import-report.md i manifest importu;
- spectral-v05/report.md, wyniki pomiarów, odczyt kontrolny z SQL i related-tables-audit.json;
- SQL importu i wycofania nowej partii;
- islands-2026-09-14/raport.html — raport z wyszukiwarką i mapą;
- islands-2026-09-14/raport.md — metoda, wyniki i ograniczenia;
- islands-2026-09-14/nowe-piosenki.csv — komplet 184 propozycji;
- islands-2026-09-14/kontynent-297.csv — kierunki i powinowactwa 297 dawnych utworów;
- islands-2026-09-14/summary.json — zestawy cech, progi i wyniki testów.

Nazwy powyżej opisują lokalne artefakty; nie są linkami do plików opublikowanych w repozytorium. Powinowactwa liczbowe są znormalizowanym odwrotnym kwadratem odległości, nie prawdopodobieństwami.

Wcześniej uzupełniono aktualną dokumentację audio o informację, że nowe piosenki doszły po utworzeniu wysp, oraz o potwierdzenie spójności tabel. Automatyczna kontrola publikacji odrzuciła wówczas szczegółowy wpis o bazie; opublikowano krótszy opis, zachowując szczegółowy audyt lokalnie. Niniejszy plik powstał na późniejsze, wyraźne polecenie zapisania podsumowania tej rozmowy w nowym MD na GitHubie.

## 12. Źródła historycznej metody

- [Aktualna dokumentacja audio](../SOL_DOKUMENTACJA-AUDIO-AKTUALNA.md)
- [Ekstraktor v05](SOL_audio-analysis-05.md)
- [Mapa trzech wysp](SOL-klastrowanie-audio-mapa-3-wysp-opis.html)
- [Dlaczego trzy wyspy](SOL-klastrowanie-audio-dlaczego-3-wyspy.html)
- [Porównanie hipotez](SOL-klastrowanie-audio-analiza-hipotez.html)
- [Metoda opisu sygnatur](SOL-klastrowanie-audio-sygnatury-wysp-metoda.html)
- [Sanityzacja historycznego zbioru](kamien-milowy-audio/index.html)
