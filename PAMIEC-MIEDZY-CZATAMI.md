# Pamięć między czatami — ustalenia użytkownika

Wersja: 01.00 · Data: 2026-09-23
Status: zapis preferencji i ustaleń z rozmowy; automatyzacja odczytu i zapisu pozostaje do skonfigurowania.

## Decyzja użytkownika

> pamiec krotkotrwala u openai/atropic jest OK
> mozliwosc zagladania do wszystkich czatow jest OK
>
> a dlugotrwala na githubie jest OK bardzo

Użytkownik akceptuje bieżący kontekst rozmów u OpenAI i Anthropic oraz odszukiwanie informacji we wcześniejszych czatach. Trwała pamięć ma znajdować się na GitHubie, pod kontrolą użytkownika, i być dostępna dla różnych agentów niezależnie od dostawcy modelu.

## Podział odpowiedzialności

| Warstwa | Rola |
|---|---|
| Bieżący czat i kontekst modelu | Pamięć krótkotrwała potrzebna do wykonania zadania. |
| Historie wcześniejszych czatów | Materiał do odszukania szczegółów i pochodzenia ustaleń, w granicach faktycznego dostępu danego narzędzia. |
| Dokumentacja na GitHubie | Trwały zapis preferencji, zasad pracy, decyzji, zadań i stanu prac, możliwy do odczytu przez Codexa, Claude i kolejnych agentów. |

Traktuj aktualne dokumenty właściwego repozytorium jako trwały zapis ustaleń, ponieważ użytkownik chce zachować ciągłość pracy przy zmianie czatu, aplikacji lub dostawcy AI. Intencją jest kontrola nad wiedzą i jej przenośność.

Odczytuj właściwe dokumenty przy podejmowaniu pracy i zapisuj istotne nowe ustalenia w przewidzianych dla nich miejscach, zgodnie z zakresem zadania oraz zasadami repozytorium, ponieważ sama obecność plików na GitHubie nie zapewnia ich wykorzystania przez kolejnego agenta.

Rozróżniaj decyzję, plan i wykonanie, ponieważ zapis preferencji nie potwierdza uruchomienia automatycznego mechanizmu pamięci. Zachowuj dotychczasowe źródła danych aplikacji i granice prywatności: ta decyzja dotyczy dokumentacji i ustaleń, a nie przenoszenia danych z SQL ani sekretów do GitHuba.

## Organizacja rozmów

Użytkownik preferuje brak podziału rozmów na projekty: chce mieć wszystkie tematy „w jednym worku”. Podaje konkretny powód: ma ASD i ADHD; podczas pracy nad jednym tematem przypominają mu się sprawy dotyczące drugiego. Konieczność pilnowania osobnych czatów projektowych prowadziłaby w jego sposobie pracy do mieszania tematów i bałaganu.

Obsługuj przechodzenie między tematami w ramach rozmowy, ponieważ użytkownik chce zapisywać pojawiające się sprawy od razu, bez obowiązku zmiany projektu lub czatu. Intencją jest dopasowanie narzędzia do sposobu pracy użytkownika, a nie narzucanie mu organizacji rozmów według projektów.

Przypisuj trwałe ustalenia i zmiany do właściwego repozytorium oraz zasobu, ponieważ wspólny tok rozmowy może dotyczyć różnych systemów. Ta preferencja dotyczy organizacji czatów; repozytoria, bazy danych i ich granice pozostają odrębne.

Możliwość odczytu wcześniejszego czatu jest czymś innym niż automatyczne otrzymanie pełnej historii wszystkich rozmów. Zgoda na zaglądanie do czatów nie tworzy technicznego dostępu do rozmów w innej usłudze.

## Kontekst tej rozmowy i granice ustaleń

Rozmowę wywołał widok „Projekty” w zdalnym sterowaniu na telefonie. Część widocznych nazw odpowiadała folderom roboczym z laptopa, a narzędzie listujące zapisane projekty zwróciło pustą listę. Przyczyny różnego grupowania w telefonie i na desktopie nie ustalono. Wcześniejsze kategoryczne objaśnienia asystenta były zbyt daleko idące i nie stanowią potwierdzonego opisu działania aplikacji.

Kontrola lokalnej konfiguracji 2026-09-23 nie wykazała wpisu włączającego pamięć ani katalogu lokalnych wspomnień. Była to obserwacja konkretnej konfiguracji, a nie gwarancja stanu wszystkich klientów lub ustawień. W tej rozmowie ustawień pamięci nie zmieniano.

Notatki odczytane z GitHuba mogą wejść do kontekstu modelu OpenAI lub Anthropic; użytkownik akceptuje taki krótkotrwały kontekst. GitHub jest miejscem trwałego zapisu, a nie mechanizmem wyłączenia przetwarzania treści przez dostawcę modelu.

## Zakres zapisu w dwóch repozytoriach

Użytkownik polecił zapisać te ustalenia w nowym pliku Markdown w obu repozytoriach osobno. Każdy plik dokumentuje tę samą preferencję w kontekście swojego repozytorium. Ten zapis nie uruchamia synchronizacji pozostałej zawartości ani scalania systemów.
