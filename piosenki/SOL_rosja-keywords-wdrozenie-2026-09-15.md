# Rosja — keywordsy PL/EN i przypisania do sekcji

Stan SQL: wdrożone, 2026-09-15. Projekt Supabase: maciekGithubHue (uogsyhvkzirprxedurrh).

## Reguły obowiązujące

1. Każda sekcja Rosji ma od 1 do 5 keywordsów. Dotyczy to także 9 węzłów TOM oraz sekcji pomocniczych.
2. Przypisywać można wyłącznie koncepty istniejące w SQL, przez concept_id w content_section_keywords. Żadnych dowolnych tekstowych tagów.
3. keyword_order biegnie od 1 do liczby keywordsów sekcji; 1 oznacza najważniejszy koncept.
4. Jedna sekcja nie może mieć tego samego konceptu dwukrotnie. Jeden koncept może łączyć wiele sekcji i dokumentów.
5. PL/EN i synonimy są nazwami jednego konceptu. Preferowane nazwy istniejących konceptów pozostawiono; cztery zatwierdzone warianty PL dodano jako aliasy.
6. Źródłem prawdy są content_keyword_concepts, content_keyword_terms i content_section_keywords. Kolumny tekstowe keywords_pl/en nie są źródłem przypisań.

## Sposób opracowania

Najpierw powstała zatwierdzona przez użytkownika wspólna lista 300 polskich keywordsów całej analizy. Podstawą były opisy 620 sekcji wszystkich 16 dokumentów w SQL, z punktowym sprawdzaniem HTML. Lista nie była kopią słownika tłumaczeń ani sumą osobnych list generowanych dla rozdziałów.

Po zatwierdzeniu listy przygotowano tłumaczenia EN, porównano znaczenia z istniejącymi konceptami i zapisano listę w SQL. Dopiero potem opracowano przypisania, indywidualnie oceniając temat i opis każdej sekcji. Obecność tematu może oznaczać również analizę hipotezy, kontrargument albo krytykę; przypisanie nie stwierdza prawdziwości tezy.

Przy opisach zbyt ogólnych sprawdzono odpowiednie fragmenty HTML, m.in. bestiariusz, mechanizmy kryzysu, zaległości płacowe i łańcuch produkcji materiałów wybuchowych. Sekcje pomocnicze (spisy, podziękowania, bibliografie) otrzymały keyword określający zakres dokumentu lub materiałów, a nie nowy keyword techniczny.

## Wynik

- Lista: 300 konceptów, każdy z preferowaną nazwą PL i EN w SQL.
- Dodano 290 konceptów i 584 nazwy: 580 preferowanych PL/EN oraz 4 aliasy PL. Wykorzystano ponownie 10 istniejących konceptów.
- Rosja: 620 sekcji heading i 9 węzłów volume, razem 629 pozycji.
- Przypisania: 2064 do heading + 40 do volume = 2104.
- Liczba keywordsów na sekcję: 1 — 7 sekcji; 2 — 54; 3 — 327; 4 — 197; 5 — 44.
- Wykorzystano 298 konceptów. Przewaga powietrzna i Mosty pozostają w SQL bez przypisań w tej wersji; nie dopisywano ich na siłę dla osiągnięcia pełnego wykorzystania listy.
- AuDHD zachowało 1298 przypisań, 338 sekcji i 498 wykorzystywanych konceptów. Zgodność przypisań potwierdzono sumą kontrolną przed i po imporcie.
- Cała baza po uzupełnieniu: 892 koncepty i 1798 nazw językowych/aliasów.

Publiczny Content Explorer zweryfikowany po zapisie: 620/620 sekcji heading z keywordsami; sprawdzono wyświetlenie nazw PL/EN w sekcji Front i spirala OPL. Wczytanie danych odbywa się przez istniejące API; zmiana nie wymagała wdrożenia kodu backendu.

## Pliki audytowe

- [Lista PL/EN z identyfikatorami SQL](../dane-robocze/csv-tsv/rosja/SOL_keywords-300-PL-EN-SQL-2026-09-15.tsv)
- [Przypisania w kolejności ważności](../dane-robocze/csv-tsv/rosja/SOL_section-keywords-2026-09-15.tsv)

Numery list_id są numerami redakcyjnymi zatwierdzonej listy. W relacjach używać wyłącznie concept_id. Kolumny keyword_pl/en w eksporcie pokazują nazwy z listy; publiczna przeglądarka może pokazywać starszą preferowaną nazwę tego samego konceptu, np. dark legitimacy zamiast Ciemna legitymizacja.

## Kontrole zapisu

Importy wykonano w transakcjach. Przed zapisem sprawdzono istnienie konceptów, przynależność sekcji do Rosji, niezmienność opisów od chwili przeglądu, pełne pokrycie, limit 1–5 oraz kolejność bez luk. Import przypisań odmawia nadpisania istniejących przypisań Rosji. Po zapisie sprawdzono wynik i zachowanie danych AuDHD.

Reguła 1–5 jest wymogiem redakcyjnym i kontrolą importu; nie dodano nowego globalnego triggera do bazy. Przy przyszłych zmianach obowiązkowo wykonać poniższy audyt. Prawidłowy wynik to zero wierszy.

```sql
SELECT s.section_id, COUNT(sk.concept_id) AS keyword_count
FROM content_sections s
JOIN content_documents d USING (document_id)
LEFT JOIN content_section_keywords sk USING (section_id)
WHERE d.collection_id = 'rosja'
GROUP BY s.section_id
HAVING COUNT(sk.concept_id) NOT BETWEEN 1 AND 5
   OR MIN(sk.keyword_order) <> 1
   OR MAX(sk.keyword_order) <> COUNT(sk.concept_id);
```

## Powiązane

- [Model relacyjny keywordsów](SOL_content-keywords-model.md)
- [Publiczna przeglądarka treści](https://maciektora-hue.github.io/techniczne/content-explorer.html)

Historyczne informacje o braku przypisań w dokumentacji z 8 września opisują stan po utworzeniu schematu, a nie bieżący stan Rosji.
