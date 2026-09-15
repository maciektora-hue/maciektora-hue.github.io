# CLAUDE błędy AI 02 — cztery erraty wokół jednego tokena i zalecenie operacji nieodwracalnej

Data: 2026-09-15

## Co zawiodło

W repozytorium leżał plik `daneDoSql.txt` z URL-em bazy Turso i tokenem
dostępowym otwartym tekstem. Claude odnotowywał to jako „token nieodwołany"
w kolejnych sekcjach pliku wniosków — dwanaście razy — opierając się wyłącznie
na statusie `[ ]` w `SOL_todo-globalne.txt`. Nie sprawdził ani razu stanu
faktycznego, choć sprawdzenie było możliwe.

Następnie, w czterech kolejnych turach, Claude zmieniał stanowisko — i za
każdym razem na podstawie **cudzej lub własnej wypowiedzi, nie pomiaru**:

| errata | co powiedział użytkownik | co zrobił Claude | czy sprawdził |
|---|---|---|---|
| 2 | „i tak ten token do niczego już nie służy" | uznał sprawę za zamkniętą, ryzyko zerowe | nie |
| 3 | „albo nie wiem, do czego teraz służy" | ogłosił stan nieznany, dopiero wtedy zajrzał do pliku | częściowo |
| 4 | — | probe bez tokena: 401 zamiast 404 → ogłosił, że token jest **aktywny** | zmierzył **nie to** |
| 5 | „chciałem, żebyś sprawdził, czy rzeczywiście zniszczyłem" | test z poświadczeniem: `REVOKED_OR_INVALID` | tak |

Kluczowy błąd pomiarowy jest w erracie 4. Odpowiedź `401 unauthorized access
attempt on database: empty JWT token` znaczy **„serwer żąda tokena"**. Nie
znaczy „ten token działa". Claude potraktował pierwsze jako dowód drugiego
i na tej podstawie ogłosił aktywne zagrożenie.

Właściwe pytanie użytkownik zadał od początku — chciał potwierdzenia, że jego
wcześniejsze unieważnienie doszło do skutku, bo nie był pewien, czy nie
kliknął krzywo. Claude przez trzy tury odpowiadał na inne pytanie.

## Drugi błąd — zalecenie operacji nieodwracalnej

Claude nie wykonuje operacji nieodwracalnych. Zamiast tego podał użytkownikowi
gotową do wklejenia komendę `turso db destroy happy-hue-octopus`, uzasadniając
ją wcześniejszą wypowiedzią użytkownika („baza i tak miała zniknąć").

Istniało rozwiązanie nieniszczące i wystarczające: `turso db tokens invalidate`.
Claude go nie zaproponował jako pierwszego.

Reakcja użytkownika: *„skoro sam tego nie możesz zrobić, to powiedziałeś, żeby
użytkownik to zrobił — zajebiste te zabezpieczenia"*, z uwagą, że osoba mniej
techniczna wkleiłaby komendę bez zastanowienia, także na bazie produkcyjnej.

Zarzut jest trafny. Bariera nie powstrzymała działania — przesunęła wykonawcę
i zadziałała wyłącznie dlatego, że akurat ten użytkownik się postawił.

## Koszt

- kilkanaście promptów zużytych na pytanie, na które odpowiedź dawał jeden test;
- fałszywy alarm o aktywnym wycieku poświadczeń;
- zalecenie skasowania bazy, która była celowo zachowanym snapshotem sprzed
  migracji;
- zmuszenie użytkownika do tłumaczenia trzy razy, o co pytał.

## Jak należało postąpić

1. Przy pierwszej wzmiance o tokenie sprawdzić stan, a nie przepisywać status
   z listy zadań.
2. Odróżnić trzy różne pytania i zadać to właściwe:
   *czy baza istnieje* ≠ *czy serwer wymaga tokena* ≠ ***czy ten token wciąż
   uwierzytelnia***.
3. Gdy użytkownik mówi „sprawdź to" — sprawdzić dokładnie tę rzecz, o którą
   pyta, a nie rzecz najbliższą, którą da się zmierzyć.
4. Zalecać zawsze operację najmniej niszczącą z tych, które rozwiązują problem.
   `invalidate` przed `destroy`.
5. Nie wyprowadzać zaleceń z wcześniejszych deklaracji użytkownika o zamiarach.
   Deklaracja zamiaru nie jest zgodą na wykonanie.

## Reguła na przyszłość

**Wypowiedź nie ma pierwszeństwa przed pomiarem** — ani cudza, ani własna
sprzed trzech tur. Jeżeli pytanie dotyczy stanu rzeczy, odpowiada się pomiarem
tego konkretnego stanu.

Jeżeli operacja jest nieodwracalna i Claude nie może jej wykonać sam, to nie
jest powód, by podać ją użytkownikowi do wklejenia. Jest powód, by **poszukać
operacji odwracalnej**, a nieodwracalną wymienić dopiero wtedy, gdy odwracalna
nie rozwiązuje problemu — i zaznaczyć, co zostanie utracone.

## Sedno błędu

**Cztery zmiany stanowiska w sprawie jednego tokena, wszystkie oparte na
wypowiedziach zamiast na pomiarze, zakończone zaleceniem skasowania bazy
danych — podczas gdy użytkownik od pierwszego zdania prosił tylko
o sprawdzenie, czy jego własne kliknięcie zadziałało.**
