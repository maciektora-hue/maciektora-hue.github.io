-- tabela: tag_snapshots
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS tag_snapshots (
  lyrics_id TEXT REFERENCES lyrics(lyrics_id),
  tagged_at TEXT,
  tags TEXT
);

INSERT INTO tag_snapshots VALUES('lyrics-000790','2026-09-06','przemiana:bardzo; cialo:bardzo; seks:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:bardzo; nigdy-dosc:bardzo; wstret:bardzo; do-innych:bardzo; ku-swiatu:bardzo; sprawczosc:bardzo; taniec:troche; bunt:troche; innosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000791','2026-09-06','substancje:bardzo; intensywna-percepcja:bardzo; sensoryka-metafora:bardzo; przemiana:bardzo; cialo:troche; pogon:troche; ku-swiatu:troche; innosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000792','2026-09-06','wspomnienia:bardzo; ku-przeszlosci:bardzo; milosc:bardzo; utrata:bardzo; samotnosc:bardzo; smutek:bardzo; melancholia:troche; zal:bardzo; gniew:bardzo; frustracja:bardzo; komunikacja-problem:bardzo; analiza-po-kontakcie:bardzo; od-kogos:bardzo; do-innych:bardzo; sprzeczne-emocje:bardzo; wina:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000793','2026-09-06','wspomnienia:bardzo; ku-przeszlosci:bardzo; milosc:bardzo; utrata:bardzo; samotnosc:bardzo; smutek:bardzo; melancholia:bardzo; zal:bardzo; gniew:bardzo; frustracja:bardzo; komunikacja-problem:bardzo; analiza-po-kontakcie:bardzo; od-kogos:bardzo; do-innych:bardzo; sprzeczne-emocje:bardzo; wina:troche; cyklicznosc-wzorzec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000794','2026-09-06','milosc:bardzo; pozadanie:bardzo; cialo:troche; czulosc:troche; radosc:bardzo; nadzieja:bardzo; ku-komus:bardzo; przemiana:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000795','2026-09-06','droga-podroz:bardzo; latanie-spadanie:bardzo; samotnosc:bardzo; bezsilnosc:bardzo; komunikacja-problem:bardzo; od-swiata:bardzo; milosc:troche; intensywna-percepcja:bardzo; przemiana:troche; utrata:troche; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000796','2026-09-06','cyklicznosc-wzorzec:bardzo; czas:troche; przemiana:bardzo; bezsilnosc:bardzo; rozpad:bardzo; smutek:bardzo; zal:bardzo; frustracja:bardzo; rozpacz:troche; do-swiata:bardzo; utrata:bardzo; wysokie-pobudzenie:troche; nic-pustka:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000001','2026-09-03','deszcz:bardzo; woda:bardzo; noc:bardzo; ciemnosc:troche; ogien:troche; strach:bardzo; smierc:troche; schronienie:bardzo; przetrwanie:bardzo; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000002','2026-09-03','prawda:bardzo; milosc:bardzo; utrata:bardzo; zal:bardzo; gniew:bardzo; frustracja:bardzo; komunikacja-problem:bardzo; od-kogos:bardzo; sprawczosc:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000003','2026-09-03','ucieczka:bardzo; droga-podroz:bardzo; samotnosc:bardzo; schronienie:bardzo; dom:bardzo; noc:bardzo; deszcz:bardzo; woda:bardzo; przetrwanie:bardzo; utrata:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; smierc:bardzo; strach:bardzo; cialo:troche; sensoryka-przytloczenie:bardzo; milosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000004','2026-09-03','sen:bardzo; pamiec:troche; smutek:bardzo; ciemnosc:bardzo; do-siebie:bardzo; prawda:bardzo; sensoryka-metafora:bardzo; nierozpoznanie-siebie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000005','2026-09-03','prawda:bardzo; ciemnosc:bardzo; do-siebie:bardzo; sprawczosc:bardzo; przemiana:bardzo; samotnosc:troche; milosc:bardzo; cialo:bardzo; smierc:troche; ku-przyszlosci:bardzo; sensoryka-metafora:bardzo; bunt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000006','2026-09-03','pozadanie:bardzo; milosc:bardzo; substancje:troche; sensoryka-szukanie:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; impulsywnosc:bardzo; nigdy-dosc:bardzo; cialo:bardzo; noc:troche; ciemnosc:troche; woda:bardzo; wolnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000007','2026-09-03','noc:bardzo; ciemnosc:bardzo; droga-podroz:bardzo; samotnosc:bardzo; dom:bardzo; nadzieja:bardzo; przemiana:bardzo; odrodzenie:troche; przetrwanie:bardzo; sensoryka-metafora:bardzo; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000008','2026-09-03','droga-podroz:bardzo; woda:bardzo; wolnosc:bardzo; sensoryka-szukanie:bardzo; euforia-naped:troche; wysokie-pobudzenie:troche; marzenie:troche; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000009','2026-09-03','czas:bardzo; ku-komus:bardzo; frustracja:bardzo; potrzeba-zapewnienia:bardzo; zablokowanie:bardzo; cyklicznosc-wzorzec:bardzo; sprawczosc:bardzo; zamartwianie:troche; noc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000010','2026-09-03','bunt:bardzo; gniew:bardzo; wysokie-pobudzenie:bardzo; racing-thoughts:bardzo; bezsennosc-restless:troche; substancje:troche; dom:bardzo; droga-podroz:bardzo; ucieczka:bardzo; cialo:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo; noc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000011','2026-09-03','noc:bardzo; ciemnosc:troche; wolnosc:bardzo; droga-podroz:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; impulsywnosc:bardzo; sprawczosc:bardzo; smierc-wlasna:troche; cialo:troche; euforia-naped:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000012','2026-09-03','dom:bardzo; schronienie:bardzo; milosc:bardzo; pozadanie:troche; czulosc:bardzo; ku-komus:bardzo; droga-podroz:troche; sensoryka-szukanie:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000013','2026-09-03','utrata:bardzo; zal:bardzo; wina:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; smierc:bardzo; gniew:bardzo; frustracja:bardzo; cyklicznosc-wzorzec:bardzo; od-kogos:bardzo; sprawczosc:bardzo; wystarczy:bardzo; oddech-powietrze:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000014','2026-09-03','milosc:bardzo; ku-komus:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; nigdy-dosc:troche; potrzeba-zapewnienia:troche; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000015','2026-09-03','noc:bardzo; czas:bardzo; przetrwanie:bardzo; nadzieja:bardzo; ulga-odroczona:bardzo; ku-przyszlosci:bardzo; ogien:bardzo; prawda:bardzo; zablokowanie:troche; wyczerpanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000016','2026-09-03','czas:bardzo; powrot-do:bardzo; sen:bardzo; smierc:bardzo; latanie-spadanie:bardzo; wina:bardzo; prawda:bardzo; samotnosc:bardzo; strach:bardzo; gniew:bardzo; nierozpoznanie-siebie:bardzo; wspomnienia:bardzo; pamiec:troche; do-siebie:bardzo; zablokowanie:bardzo; sensoryka-metafora:bardzo; rozpad:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000017','2026-09-03','gniew:bardzo; bunt:bardzo; do-swiata:bardzo; strach:bardzo; wolnosc:bardzo; smierc:bardzo; ogien:bardzo; substancje:troche; sprawczosc:bardzo; wysokie-pobudzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000018','2026-09-03','ku-komus:bardzo; samotnosc:bardzo; noc:bardzo; dom:bardzo; brak-nadziei:troche; nadzieja:bardzo; ulga-z-zewnatrz:bardzo; potrzeba-zapewnienia:bardzo; sensoryka-metafora:troche; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000019','2026-09-03','sensoryka-przytloczenie:bardzo; wysokie-pobudzenie:bardzo; cialo:bardzo; rutyna-repetycja:bardzo; performowanie-roli:bardzo; maska:bardzo; noc:bardzo; sen:bardzo; sensoryka-szukanie:bardzo; cyklicznosc-wzorzec:bardzo; frustracja:troche; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000020','2026-09-03','do-swiata:bardzo; gniew:bardzo; frustracja:bardzo; niedopasowanie-spoleczne:bardzo; bunt:bardzo; wolnosc:bardzo; hiperczujnosc:bardzo; kontrola:bardzo; substancje:troche; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo; prawda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000021','2026-09-03','lek:bardzo; lek-antycypacyjny:bardzo; niepewnosc-nie-do-zniesienia:bardzo; milosc:bardzo; utrata:bardzo; ku-komus:bardzo; ogien:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo; sprzeczne-emocje:troche; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000022','2026-09-03','dom:bardzo; czas:bardzo; smutek:bardzo; noc:bardzo; samotnosc:bardzo; dotyk:bardzo; niskie-pobudzenie:bardzo; spowolnienie:bardzo; przemiana:bardzo; odrodzenie:bardzo; woda:bardzo; wspomnienia:bardzo; pamiec:bardzo; niepewnosc-nie-do-zniesienia:troche; czulosc:bardzo; milosc:bardzo; radosc:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000023','2026-09-03','pozadanie:bardzo; zazdrosc:troche; taniec:bardzo; sensoryka-szukanie:bardzo; ku-komus:bardzo; wysokie-pobudzenie:bardzo; cialo:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000024','2026-09-03','sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; cialo:bardzo; woda:bardzo; noc:bardzo; latanie-spadanie:troche; radosc:bardzo; spokoj:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; taniec:bardzo; euforia-naped:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000025','2026-09-03','hiperczujnosc:bardzo; dom:bardzo; schronienie:bardzo; bunt:bardzo; wolnosc:bardzo; kontrola:bardzo; gniew:bardzo; zablokowanie:bardzo; do-swiata:bardzo; przemiana:bardzo; sprawczosc:bardzo; frustracja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000026','2026-09-03','noc:bardzo; strach:bardzo; hiperczujnosc:bardzo; kontrola:bardzo; schronienie:bardzo; przetrwanie:bardzo; rutyna-repetycja:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-przytloczenie:bardzo; niskie-pobudzenie:troche; do-swiata:bardzo; dom:bardzo; sen:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000027','2026-09-03','milosc:bardzo; sprzeczne-potrzeby:bardzo; zablokowanie:bardzo; potrzeba-zapewnienia:bardzo; woda:bardzo; ogien:bardzo; dom:bardzo; smierc-wlasna:bardzo; ku-komus:bardzo; od-kogos:troche; sensoryka-metafora:bardzo; wysokie-pobudzenie:troche; bezsilnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000028','2026-09-03','noc:bardzo; przemiana:bardzo; pozadanie:bardzo; cialo:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; impulsywnosc:bardzo; innosc:bardzo; sprawczosc:bardzo; euforia-naped:bardzo; do-innych:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000029','2026-09-03','milosc:bardzo; nigdy-dosc:bardzo; ku-komus:bardzo; specjalne-zainteresowanie-osoba:troche; sensoryka-metafora:bardzo; droga-podroz:troche; ulga-z-zewnatrz:bardzo; euforia-naped:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000030','2026-09-03','milosc:bardzo; utrata:bardzo; zal:bardzo; gniew:bardzo; frustracja:bardzo; ogien:bardzo; latanie-spadanie:bardzo; sprzeczne-emocje:bardzo; ku-komus:bardzo; impulsywnosc:bardzo; sprawczosc:bardzo; zablokowanie:bardzo; rozpad:bardzo; prawda:bardzo; wysokie-pobudzenie:bardzo; cialo:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000031','2026-09-03','milosc:bardzo; pozadanie:bardzo; kontrola:bardzo; zablokowanie:bardzo; potrzeba-zapewnienia:bardzo; sprawczosc:bardzo; wolnosc:bardzo; komunikacja-problem:bardzo; frustracja:bardzo; sprzeczne-potrzeby:bardzo; cialo:troche; ku-komus:bardzo; bezsilnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000032','2026-09-03','milosc:bardzo; utrata:bardzo; rozpad:bardzo; noc:bardzo; ciemnosc:bardzo; ogien:bardzo; substancje:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; cyklicznosc-wzorzec:bardzo; brak-nadziei:bardzo; smutek:bardzo; zal:bardzo; sensoryka-metafora:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000033','2026-09-03','marzenie:bardzo; utrata:bardzo; przemiana:bardzo; droga-podroz:bardzo; ucieczka:bardzo; smierc:bardzo; deszcz:bardzo; woda:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; sprzeczne-emocje:bardzo; sensoryka-metafora:bardzo; ku-przyszlosci:troche; wysokie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000034','2026-09-03','milosc:bardzo; utrata:bardzo; rozpad:bardzo; noc:bardzo; ciemnosc:bardzo; ogien:bardzo; substancje:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; cyklicznosc-wzorzec:bardzo; brak-nadziei:bardzo; smutek:bardzo; zal:bardzo; sensoryka-metafora:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000035','2026-09-03','milosc:bardzo; pozadanie:bardzo; kontrola:bardzo; zazdrosc:bardzo; niemoznosc-odpuszczenia:bardzo; sprzeczne-emocje:bardzo; ku-komus:bardzo; gniew:bardzo; potrzeba-zapewnienia:troche; specjalne-zainteresowanie-osoba:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000036','2026-09-03','milosc:bardzo; pozadanie:bardzo; frustracja:bardzo; cialo:bardzo; dotyk:bardzo; potrzeba-zapewnienia:troche; sprzeczne-emocje:bardzo; komunikacja-problem:bardzo; gniew:bardzo; do-innych:bardzo; bezsilnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000037','2026-09-03','milosc:bardzo; pozadanie:bardzo; czulosc:bardzo; dotyk:bardzo; smierc:bardzo; cialo:bardzo; woda:bardzo; strach:bardzo; smutek:bardzo; utrata:bardzo; droga-podroz:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000038','2026-09-03','kontrola:bardzo; bunt:bardzo; wolnosc:bardzo; przemiana:bardzo; odrodzenie:bardzo; sprawczosc:bardzo; ogien:bardzo; przetrwanie:bardzo; gniew:bardzo; od-kogos:bardzo; wysokie-pobudzenie:bardzo; cialo:bardzo; dopasowanie-roli:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000039','2026-09-03','taniec:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; noc:bardzo; substancje:bardzo; radosc:bardzo; cialo:troche; ku-swiatu:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000040','2026-09-03','zazdrosc:bardzo; lek-antycypacyjny:bardzo; potrzeba-zapewnienia:bardzo; milosc:bardzo; strach:bardzo; komunikacja-problem:bardzo; bezsilnosc:bardzo; ku-komus:bardzo; do-innych:bardzo; smutek:bardzo; tesknota:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000041','2026-09-03','zazdrosc:bardzo; lek-antycypacyjny:bardzo; potrzeba-zapewnienia:bardzo; milosc:bardzo; strach:bardzo; komunikacja-problem:bardzo; bezsilnosc:bardzo; ku-komus:bardzo; do-innych:bardzo; smutek:bardzo; tesknota:troche; innosc:bardzo; wolnosc:bardzo; do-siebie:bardzo; przemiana:bardzo; odrodzenie:troche; sprzeczne-emocje:bardzo; ku-przyszlosci:bardzo; marzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000013','','');

INSERT INTO tag_snapshots VALUES('lyrics-000042','2026-09-03','marzenie:bardzo; sen:bardzo; milosc:bardzo; ku-komus:bardzo; nadzieja:bardzo; niedopasowanie-spoleczne:troche; dom:troche; ku-przeszlosci:bardzo; wspomnienia:bardzo; przemiana:bardzo; sprawczosc:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000043','2026-09-03','bezsennosc-restless:bardzo; hiperfokus:bardzo; zablokowanie:bardzo; samotnosc:bardzo; ciemnosc:bardzo; smierc-wlasna:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; hiperczujnosc:bardzo; cyklicznosc-wzorzec:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; dotyk:bardzo; ulga-z-zewnatrz:bardzo; wysokie-pobudzenie:bardzo; pogon:bardzo; do-siebie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000044','2026-09-03','pozadanie:bardzo; frustracja:bardzo; cialo:bardzo; dotyk:bardzo; zazdrosc:troche; komunikacja-problem:troche; czas:bardzo; gniew:troche; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000045','2026-09-03','droga-podroz:bardzo; latanie-spadanie:bardzo; ucieczka:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; gniew:bardzo; przemiana:bardzo; odrodzenie:bardzo; ulga:bardzo; marzenie:bardzo; nadzieja:bardzo; wolnosc:bardzo; ku-przyszlosci:bardzo; sprawczosc:bardzo; cialo:bardzo; sensoryka-metafora:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000046','2026-09-03','prawda:bardzo; milosc:bardzo; utrata:bardzo; zal:bardzo; gniew:bardzo; frustracja:bardzo; komunikacja-problem:bardzo; od-kogos:bardzo; sprawczosc:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000047','2026-09-03','do-swiata:bardzo; bunt:bardzo; gniew:bardzo; frustracja:bardzo; nic-pustka:bardzo; prawda:bardzo; sprawczosc:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000048','2026-09-03','pozadanie:bardzo; noc:bardzo; droga-podroz:bardzo; cyklicznosc-wzorzec:bardzo; ulga:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000049','2026-09-03','kontrola:bardzo; zablokowanie:bardzo; substancje:bardzo; noc:bardzo; cialo:troche; nierozpoznanie-siebie:troche; do-swiata:bardzo; prawda:bardzo; cyklicznosc-wzorzec:bardzo; bezsilnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000050','2026-09-03','pozadanie:bardzo; milosc:bardzo; specjalne-zainteresowanie-osoba:bardzo; nigdy-dosc:bardzo; dotyk:bardzo; cialo:bardzo; ulga-z-zewnatrz:bardzo; spokoj:bardzo; lek:troche; strach:troche; sen:bardzo; marzenie:troche; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; przemiana:bardzo; euforia-naped:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000781','2026-09-03','maskowanie:bardzo; performowanie-roli:bardzo; ukrywanie-reakcji:bardzo; strach:bardzo; hiperczujnosc:bardzo; spokoj:bardzo; ulga:bardzo; oddech-powietrze:bardzo; cialo:bardzo; prawda:bardzo; sprzeczne-potrzeby:bardzo; wyczerpanie:bardzo; do-siebie:bardzo; gniew:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000051','2026-09-03','prawda:bardzo; maska:bardzo; nierozpoznanie-siebie:bardzo; milosc:bardzo; nigdy-dosc:bardzo; ku-komus:bardzo; niepewnosc-nie-do-zniesienia:bardzo; marzenie:troche; potrzeba-zapewnienia:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000052','2026-09-03','pozadanie:bardzo; od-kogos:bardzo; komunikacja-problem:bardzo; niskie-pobudzenie:bardzo; sensoryka-metafora:bardzo; smutek:troche; samotnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000784','2026-09-03','latanie-spadanie:bardzo; brak-nadziei:bardzo; rozpacz:bardzo; smutek:bardzo; noc:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; wysokie-pobudzenie:bardzo; sprzeczne-emocje:bardzo; ukrywanie-reakcji:bardzo; oddech-powietrze:bardzo; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:bardzo; milosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000053','2026-09-03','wina:bardzo; zal:bardzo; bezsennosc-restless:bardzo; droga-podroz:bardzo; dom:bardzo; powrot-do:bardzo; prawda:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; milosc:bardzo; ku-komus:bardzo; sprawczosc:bardzo; przemiana:bardzo; czas:bardzo; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000054','2026-09-03','pozadanie:bardzo; nigdy-dosc:bardzo; cialo:bardzo; milosc:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; do-swiata:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo; wysokie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000055','2026-09-03','sen:troche; noc:bardzo; ciemnosc:bardzo; droga-podroz:bardzo; substancje:troche; gniew:bardzo; utrata:bardzo; od-kogos:bardzo; smierc:bardzo; ogien:bardzo; przemiana:bardzo; do-siebie:bardzo; wysokie-pobudzenie:bardzo; sprzeczne-emocje:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000056','2026-09-03','lek:bardzo; cialo:bardzo; ciemnosc:bardzo; sensoryka-metafora:bardzo; od-kogos:bardzo; wolnosc:bardzo; do-siebie:bardzo; przemiana:bardzo; odrodzenie:troche; duma:bardzo; sprawczosc:bardzo; samokontrola-spoleczna:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000787','2026-09-03','marzenie:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:bardzo; maska:bardzo; niedopasowanie-spoleczne:bardzo; innosc:bardzo; nuda-nietolerancja:troche; wolnosc:bardzo; do-siebie:bardzo; rutyna-repetycja:troche; radosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000057','2026-09-03','noc:bardzo; substancje:bardzo; substancja-regulacja:bardzo; sen:bardzo; nic-pustka:bardzo; schronienie:bardzo; ulga-z-zewnatrz:bardzo; wyczerpanie:bardzo; wycofanie:bardzo; niskie-pobudzenie:bardzo; od-swiata:bardzo; wstyd:bardzo; spokoj:bardzo; zablokowanie:troche; smutek:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000058','2026-09-03','czas:bardzo; smierc:bardzo; wspomnienia:bardzo; pamiec:bardzo; taniec:bardzo; droga-podroz:bardzo; milosc:bardzo; dotyk:bardzo; cialo:bardzo; wstyd:bardzo; do-siebie:bardzo; niepewnosc-nie-do-zniesienia:bardzo; marzenie:bardzo; prawda:bardzo; sprawczosc:bardzo; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000059','2026-09-03','ucieczka:bardzo; wstyd:bardzo; milosc:bardzo; dotyk:bardzo; woda:troche; zal:bardzo; wina:bardzo; nic-pustka:bardzo; komunikacja-problem:bardzo; utrata:bardzo; marzenie:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; od-kogos:bardzo; tesknota:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000060','2026-09-03','milosc:bardzo; specjalne-zainteresowanie-osoba:bardzo; tesknota:bardzo; zamartwianie:bardzo; nadzieja:bardzo; marzenie:bardzo; bezsennosc-restless:bardzo; woda:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000061','2026-09-03','sen:bardzo; noc:bardzo; substancje:bardzo; smierc:troche; melancholia:bardzo; smutek:troche; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000062','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; radosc:bardzo; chaos-balagan:bardzo; rutyna-repetycja:bardzo; marzenie:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000063','2026-09-03','smierc:bardzo; odrodzenie:bardzo; przemiana:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; przetrwanie:bardzo; ziemia:bardzo; ogien:troche; dom:bardzo; schronienie:bardzo; wspomnienia:troche; czas:bardzo; radosc:troche; smutek:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000064','2026-09-03','czas:bardzo; utrata:bardzo; smutek:bardzo; nuda:bardzo; komunikacja-problem:bardzo; wycofanie:bardzo; od-kogos:bardzo; ku-przeszlosci:bardzo; cyklicznosc-wzorzec:troche; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000056','','');

INSERT INTO tag_snapshots VALUES('lyrics-000065','2026-09-03','sprawczosc:bardzo; wina:bardzo; wolnosc:bardzo; bunt:bardzo; do-siebie:bardzo; prawda:bardzo; sprzeczne-potrzeby:bardzo; bezsilnosc:troche; nadzieja:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000066','2026-09-03','lek:bardzo; lek-antycypacyjny:bardzo; hiperczujnosc:bardzo; napiecie-ciala:bardzo; emocja-przez-cialo:bardzo; sensoryka-przytloczenie:bardzo; noc:bardzo; sen:bardzo; bezsennosc-restless:troche; wysokie-pobudzenie:bardzo; potrzeba-zapewnienia:troche; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000774','2026-09-03','za-duzo-i-za-malo:bardzo; impulsywnosc:bardzo; wyczerpanie:bardzo; wysokie-pobudzenie:bardzo; emocjonalna-dysregulacja:bardzo; zamartwianie:bardzo; przeciazenie-przyszloscia:bardzo; performowanie-roli:troche; samotnosc:bardzo; cialo:bardzo; sprawczosc:troche; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000067','2026-09-03','przemiana:bardzo; odrodzenie:bardzo; nadzieja:bardzo; sprawczosc:bardzo; ku-przyszlosci:bardzo; droga-podroz:bardzo; strach:bardzo; wysokie-pobudzenie:troche; cel-nieosiagniety:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000068','2026-09-03','smutek:bardzo; rozpacz:bardzo; smierc:bardzo; utrata:bardzo; samotnosc:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; przetrwanie:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000069','2026-09-03','samotnosc:bardzo; radosc:bardzo; nadzieja:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; potrzeba-zapewnienia:bardzo; ku-swiatu:bardzo; marzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000070','2026-09-03','milosc:bardzo; marzenie:bardzo; woda:bardzo; noc:bardzo; czulosc:bardzo; ku-komus:bardzo; wspomnienia:troche; pamiec:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000071','2026-09-03','katastrofizacja:bardzo; przeciazenie-przyszloscia:bardzo; lek-antycypacyjny:bardzo; smierc:bardzo; nic-pustka:bardzo; czas:bardzo; oddech-powietrze:bardzo; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000072','2026-09-03','sen:bardzo; marzenie:bardzo; utrata:bardzo; smutek:bardzo; zal:bardzo; milosc:bardzo; woda:bardzo; innosc:bardzo; dopasowanie-roli:troche; performowanie-roli:troche; ku-komus:bardzo; smierc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000073','2026-09-03','maskowanie:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:bardzo; wstyd:bardzo; ja-publiczne-ja-prywatne:bardzo; komunikacja-problem:bardzo; milosc:bardzo; prawda:bardzo; niedopasowanie-spoleczne:bardzo; sprzeczne-potrzeby:troche; do-innych:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000074','2026-09-03','milosc:bardzo; potrzeba-zapewnienia:bardzo; droga-podroz:bardzo; wyczerpanie:bardzo; strach:bardzo; marzenie:bardzo; ku-komus:bardzo; czulosc:bardzo; zablokowanie:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000075','2026-09-03','milosc:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; wstret:bardzo; od-kogos:bardzo; zablokowanie:bardzo; sensoryka-metafora:bardzo; sprzeczne-emocje:troche; pozadanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000076','2026-09-03','ogien:bardzo; milosc:bardzo; pozadanie:bardzo; strach:bardzo; wysokie-pobudzenie:bardzo; cialo:bardzo; oddech-powietrze:bardzo; euforia-naped:bardzo; smierc:troche; sprzeczne-emocje:bardzo; kontrola:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000077','2026-09-03','cialo:bardzo; strach:bardzo; dotyk:bardzo; pozadanie:troche; zablokowanie:bardzo; nadzieja:troche; oddech-powietrze:troche; sensoryka-metafora:bardzo; prawda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000078','2026-09-03','cialo:ociupinke; spokoj:ociupinke');

INSERT INTO tag_snapshots VALUES('lyrics-000079','2026-09-03','milosc:bardzo; czulosc:bardzo; ku-komus:bardzo; do-innych:bardzo; sprawczosc:bardzo; duma:troche; nadzieja:troche; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000080','2026-09-03','gniew:bardzo; bunt:bardzo; hiperczujnosc:bardzo; racing-thoughts:bardzo; noc:bardzo; substancje:troche; cialo:bardzo; dom:bardzo; powrot-do:bardzo; droga-podroz:bardzo; ucieczka:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000081','2026-09-03','chaos-balagan:bardzo; sensoryka-przytloczenie:bardzo; emocjonalna-dysregulacja:bardzo; wysokie-pobudzenie:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; wina:bardzo; do-siebie:bardzo; zablokowanie:bardzo; woda:bardzo; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000082','2026-09-03','czas:bardzo; smierc:bardzo; odrodzenie:bardzo; przemiana:bardzo; ziemia:bardzo; smutek:bardzo; radosc:bardzo; taniec:bardzo; milosc:bardzo; spokoj:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000083','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; maskowanie:bardzo; kontrola-wizerunku:bardzo; ja-publiczne-ja-prywatne:bardzo; bezwartosciowosc:bardzo; wstyd:bardzo; milosc:bardzo; sprzeczne-potrzeby:bardzo; komunikacja-problem:bardzo; od-kogos:troche; ku-komus:bardzo; cyklicznosc-wzorzec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000084','2026-09-03','racing-thoughts:bardzo; hiperczujnosc:bardzo; sensoryka-przytloczenie:bardzo; chaos-balagan:bardzo; zablokowanie:troche; wysokie-pobudzenie:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000609','2026-09-03','sen:bardzo; wspomnienia:bardzo; pamiec:bardzo; przemiana:bardzo; odrodzenie:bardzo; nadzieja:bardzo; radosc:bardzo; ku-przyszlosci:bardzo; czas:bardzo; wolnosc:troche; bunt:troche; droga-podroz:troche; sensoryka-metafora:bardzo; wysokie-pobudzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000085','2026-09-03','milosc:bardzo; zazdrosc:bardzo; kontrola:bardzo; lek-antycypacyjny:troche; sprzeczne-emocje:bardzo; gniew:troche; od-kogos:bardzo; ku-komus:bardzo; potrzeba-zapewnienia:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000086','2026-09-03','droga-podroz:bardzo; czas:bardzo; sen:bardzo; deszcz:bardzo; smutek:bardzo; strach:bardzo; wyczerpanie:bardzo; brak-nadziei:bardzo; zablokowanie:bardzo; sensoryka-metafora:bardzo; katastrofizacja:bardzo; przeciazenie-przyszloscia:bardzo; dom:troche; utrata:bardzo; ku-przyszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000087','2026-09-03','milosc:bardzo; pozadanie:bardzo; utrata:bardzo; brak-nadziei:bardzo; prawda:bardzo; komunikacja-problem:bardzo; sprzeczne-emocje:bardzo; cyklicznosc-wzorzec:bardzo; od-kogos:bardzo; zal:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000088','2026-09-03','milosc:bardzo; pozadanie:bardzo; cialo:bardzo; ogien:bardzo; kontrola:bardzo; dotyk:bardzo; dom:bardzo; schronienie:troche; ku-komus:bardzo; sensoryka-metafora:bardzo; nigdy-dosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000089','2026-09-03','cialo:bardzo; emocja-przez-cialo:bardzo; intensywna-percepcja:bardzo; sensoryka-szukanie:bardzo; woda:bardzo; strach:bardzo; ciemnosc:bardzo; nadzieja:bardzo; przemiana:bardzo; spokoj:bardzo; dotarcie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000090','2026-09-03','gniew:bardzo; utrata:bardzo; czas:bardzo; substancje:bardzo; substancja-regulacja:bardzo; sen:troche; ogien:bardzo; smutek:bardzo; cyklicznosc-wzorzec:bardzo; zobojetnienie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000091','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; znikniecie:bardzo; nic-pustka:bardzo; samotnosc:bardzo; smutek:bardzo; bezwartosciowosc:bardzo; nierozpoznanie-siebie:bardzo; cialo:bardzo; substancje:troche; sensoryka-metafora:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000092','2026-09-03','komunikacja-problem:bardzo; samotnosc:bardzo; niedopasowanie-spoleczne:bardzo; kontrola-wizerunku:troche; ja-publiczne-ja-prywatne:troche; wspomnienia:bardzo; ku-przeszlosci:bardzo; czas:bardzo; zablokowanie:bardzo; do-innych:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000093','2026-09-03','milosc:bardzo; pozadanie:troche; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; sen:bardzo; gniew:bardzo; utrata:bardzo; od-kogos:bardzo; ku-komus:bardzo; sprzeczne-emocje:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000095','2026-09-03','lek:bardzo; lek-antycypacyjny:bardzo; napiecie-ciala:bardzo; emocja-przez-cialo:bardzo; milosc:bardzo; komunikacja-problem:bardzo; wysokie-pobudzenie:bardzo; zamartwianie:bardzo; czas:bardzo; niemoznosc-odpuszczenia:bardzo; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000096','2026-09-03','maskowanie:bardzo; performowanie-roli:bardzo; maskowanie-koszt:bardzo; ja-publiczne-ja-prywatne:bardzo; samotnosc-preferowana:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; droga-podroz:bardzo; sprawczosc:bardzo; do-siebie:bardzo; noc:bardzo; bezsennosc-restless:bardzo; sensoryka-szukanie:bardzo; wolnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000097','2026-09-03','noc:bardzo; substancje:bardzo; cialo:bardzo; dotyk:bardzo; pozadanie:bardzo; sen:bardzo; ukrywanie-reakcji:troche; sensoryka-szukanie:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000098','2026-09-03','nadzieja:bardzo; strach:troche; do-swiata:bardzo; ku-przyszlosci:bardzo; czas:bardzo; utrata:bardzo; samotnosc:troche; duma:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000099','2026-09-03','marzenie:bardzo; latanie-spadanie:bardzo; strach:bardzo; lek-antycypacyjny:troche; wolnosc:bardzo; przemiana:bardzo; odrodzenie:bardzo; ku-przyszlosci:bardzo; oddech-powietrze:bardzo; ciemnosc:bardzo; do-swiata:bardzo; zazdrosc:troche; sprawczosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000100','2026-09-03','brak-nadziei:bardzo; sen:bardzo; marzenie:bardzo; przemiana:bardzo; odrodzenie:bardzo; czas:bardzo; zablokowanie:bardzo; samotnosc:troche; cialo:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000101','2026-09-03','sprzeczne-potrzeby:bardzo; komunikacja-problem:bardzo; prawda:bardzo; ukrywanie-reakcji:troche; frustracja:bardzo; milosc:troche; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000102','2026-09-03','maskowanie:bardzo; performowanie-roli:bardzo; ukrywanie-reakcji:bardzo; gniew:bardzo; frustracja:bardzo; komunikacja-problem:bardzo; wycofanie:bardzo; samotnosc-preferowana:bardzo; dom:bardzo; powrot-do:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000103','2026-09-03','specjalne-zainteresowanie-osoba:bardzo; hiperfokus:bardzo; milosc:bardzo; pozadanie:bardzo; ku-komus:bardzo; potrzeba-zapewnienia:bardzo; kontrola:troche; sprawdzanie:troche; latanie-spadanie:bardzo; droga-podroz:bardzo; ogien:troche; taniec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000104','2026-09-03','smierc:bardzo; czas:bardzo; przemiana:bardzo; droga-podroz:bardzo; spokoj:bardzo; sensoryka-metafora:bardzo; oddech-powietrze:troche; do-siebie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000105','2026-09-03','substancje:bardzo; substancja-regulacja:troche; do-swiata:bardzo; kontrola:bardzo; cialo:bardzo; dysfunkcja-wykonawcza:troche; zablokowanie:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000674','','');

INSERT INTO tag_snapshots VALUES('lyrics-000106','2026-09-03','pozadanie:bardzo; milosc:bardzo; latanie-spadanie:bardzo; wolnosc:bardzo; cialo:bardzo; dotyk:bardzo; wystarczy:bardzo; ku-komus:bardzo; sprawczosc:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000107','2026-09-03','milosc:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; czas:bardzo; sen:bardzo; noc:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; tesknota:bardzo; nadzieja:bardzo; droga-podroz:troche; cyklicznosc-wzorzec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000108','2026-09-03','rutyna-repetycja:bardzo; sensoryka-przytloczenie:bardzo; droga-podroz:bardzo; pamiec:bardzo; zablokowanie:bardzo; niedopasowanie-spoleczne:troche; smutek:bardzo; ziemia:bardzo; do-swiata:bardzo; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000109','2026-09-03','czas:bardzo; wspomnienia:bardzo; pamiec:bardzo; milosc:bardzo; substancje:bardzo; czulosc:bardzo; radosc:bardzo; samotnosc:troche; woda:bardzo; niepewnosc-nie-do-zniesienia:bardzo; kontrola:bardzo; ku-przyszlosci:troche; przemiana:bardzo; znikniecie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000110','2026-09-03','wolnosc:bardzo; ulga:bardzo; samotnosc-preferowana:bardzo; sprawczosc:bardzo; od-kogos:bardzo; kontrola:bardzo; przemiana:bardzo; odrodzenie:troche; duma:bardzo; wiem-co-czuje:bardzo; noc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000111','2026-09-03','racing-thoughts:bardzo; sensoryka-przytloczenie:bardzo; komunikacja-problem:bardzo; samotnosc:bardzo; rutyna-repetycja:bardzo; hiperczujnosc:troche; zablokowanie:bardzo; wysokie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000775','2026-09-03','wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; impulsywnosc:bardzo; nuda-nietolerancja:bardzo; bezsennosc-restless:bardzo; euforia-naped:bardzo; nigdy-dosc:bardzo; rutyna-repetycja:bardzo; cialo:bardzo; sprawczosc:bardzo; intensywna-percepcja:troche; emocjonalna-dysregulacja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000112','2026-09-03','prawda:bardzo; czas:bardzo; milosc:bardzo; smutek:bardzo; dom:bardzo; cyklicznosc-wzorzec:bardzo; nadzieja:bardzo; przetrwanie:bardzo; sprawczosc:bardzo; droga-podroz:troche; ku-przyszlosci:bardzo; smierc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000114','2026-09-03','rutyna-repetycja:bardzo; czas:bardzo; marzenie:bardzo; milosc:bardzo; ku-komus:bardzo; sen:bardzo; spokoj:bardzo; nadzieja:bardzo; sensoryka-szukanie:bardzo; pozadanie:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000115','2026-09-03','do-swiata:bardzo; niedopasowanie-spoleczne:bardzo; performowanie-roli:troche; wstret:bardzo; sen:bardzo; nadzieja:bardzo; cel-nieosiagniety:bardzo; droga-podroz:troche; przetrwanie:bardzo; bunt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000116','2026-09-03','samotnosc-preferowana:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; sensoryka-przytloczenie:bardzo; intensywna-percepcja:bardzo; strach:bardzo; czas:bardzo; bezsilnosc:bardzo; sen:bardzo; droga-podroz:bardzo; nadzieja:bardzo; zablokowanie:bardzo; do-siebie:bardzo; ciemnosc:bardzo; wycofanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000117','2026-09-03','milosc:bardzo; czas:bardzo; ogien:bardzo; cialo:troche; emocja-przez-cialo:troche; sprzeczne-emocje:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000118','2026-09-03','milosc:bardzo; radosc:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; taniec:bardzo; sen:bardzo; marzenie:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; pozadanie:bardzo; ku-komus:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000119','2026-09-03','droga-podroz:bardzo; deszcz:bardzo; latanie-spadanie:bardzo; wolnosc:bardzo; ku-komus:bardzo; dom:bardzo; nic-pustka:troche; cialo:bardzo; sprzeczne-potrzeby:bardzo; sensoryka-szukanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000120','2026-09-03','milosc:bardzo; pozadanie:bardzo; sprzeczne-emocje:bardzo; komunikacja-problem:bardzo; kontrola:bardzo; zablokowanie:troche; marzenie:bardzo; smutek:troche; od-kogos:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000121','2026-09-03','milosc:bardzo; czulosc:bardzo; cialo:bardzo; schronienie:bardzo; odrodzenie:bardzo; przemiana:bardzo; latanie-spadanie:bardzo; droga-podroz:bardzo; oddech-powietrze:bardzo; ogien:bardzo; znikniecie:bardzo; ku-komus:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; wyczerpanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000122','2026-09-03','smutek:bardzo; zal:bardzo; milosc:bardzo; dotyk:bardzo; sen:bardzo; wspomnienia:bardzo; pamiec:bardzo; wstyd:bardzo; komunikacja-problem:bardzo; zablokowanie:bardzo; czas:bardzo; ku-przeszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000123','2026-09-03','woda:bardzo; cialo:bardzo; zablokowanie:bardzo; substancje:troche; sensoryka-metafora:bardzo; sprzeczne-emocje:bardzo; intensywna-percepcja:bardzo; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000124','2026-09-03','maskowanie:bardzo; performowanie-roli:bardzo; maskowanie-koszt:bardzo; ja-publiczne-ja-prywatne:bardzo; samotnosc-preferowana:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; droga-podroz:bardzo; sprawczosc:bardzo; do-siebie:bardzo; noc:bardzo; bezsennosc-restless:bardzo; sensoryka-szukanie:bardzo; wolnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000125','2026-09-03','gniew:bardzo; do-siebie:bardzo; wstyd:bardzo; prawda:bardzo; nierozpoznanie-siebie:bardzo; kontrola-wizerunku:bardzo; samotnosc-preferowana:troche; dom:bardzo; woda:bardzo; przemiana:bardzo; bezsennosc-restless:bardzo; frustracja:bardzo; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000126','2026-09-03','do-siebie:bardzo; przemiana:bardzo; odrodzenie:bardzo; wolnosc:bardzo; wystarczy:bardzo; milosc:bardzo; pozadanie:bardzo; cialo:bardzo; sen:bardzo; droga-podroz:bardzo; woda:bardzo; ku-komus:troche; od-kogos:troche; racing-thoughts:troche; impulsywnosc:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000127','2026-09-03','pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; komunikacja-problem:troche; ku-komus:bardzo; nigdy-dosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000128','2026-09-03','strach:bardzo; latanie-spadanie:bardzo; sensoryka-szukanie:bardzo; wstyd:bardzo; nie-wiem-co-czuje:troche; marzenie:bardzo; sprawczosc:bardzo; prawda:bardzo; do-swiata:bardzo; czas:bardzo; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000129','2026-09-03','lek:bardzo; strach:bardzo; emocjonalna-dysregulacja:bardzo; wysokie-pobudzenie:bardzo; milosc:bardzo; pozadanie:bardzo; sprzeczne-emocje:bardzo; gniew:bardzo; substancje:troche; cialo:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000130','2026-09-03','milosc:bardzo; komunikacja-problem:bardzo; sen:bardzo; ogien:bardzo; gniew:bardzo; frustracja:bardzo; potrzeba-zapewnienia:bardzo; napiecie-ciala:bardzo; emocja-przez-cialo:bardzo; wysokie-pobudzenie:bardzo; zablokowanie:bardzo; sprzeczne-potrzeby:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000131','2026-09-03','zablokowanie:bardzo; ukrywanie-potrzeb:troche; nie-wiem-co-czuje:bardzo; komunikacja-problem:bardzo; sprzeczne-potrzeby:troche; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000132','2026-09-03','latanie-spadanie:bardzo; wolnosc:bardzo; milosc:bardzo; impulsywnosc:bardzo; racing-thoughts:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; noc:bardzo; czas:bardzo; zapominanie-gubienie:bardzo; strach:troche; smierc:troche; sensoryka-szukanie:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000133','2026-09-03','wspomnienia:bardzo; ku-przeszlosci:bardzo; utrata:bardzo; samotnosc:bardzo; czas:bardzo; performowanie-roli:bardzo; maskowanie:bardzo; kontrola-wizerunku:bardzo; bunt:bardzo; wycofanie:troche; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000134','2026-09-03','oddech-powietrze:bardzo; ziemia:bardzo; woda:bardzo; sensoryka-metafora:bardzo; utrata:bardzo; od-kogos:bardzo; droga-podroz:bardzo; ucieczka:bardzo; zablokowanie:bardzo; sprawczosc:bardzo; nadzieja:troche; intensywna-percepcja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000135','2026-09-03','marzenie:bardzo; schronienie:bardzo; spokoj:bardzo; noc:bardzo; czas:bardzo; niskie-pobudzenie:bardzo; wycofanie:bardzo; powrot-do:bardzo; tesknota:bardzo; znikniecie:troche; do-siebie:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000136','2026-09-03','ogien:bardzo; noc:bardzo; ciemnosc:bardzo; nic-pustka:bardzo; samotnosc:bardzo; dom:bardzo; droga-podroz:bardzo; wysokie-pobudzenie:bardzo; emocjonalna-dysregulacja:troche; zobojetnienie:troche; cialo:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000137','2026-09-03','wspomnienia:bardzo; pogon:bardzo; oddech-powietrze:bardzo; strach:bardzo; sensoryka-przytloczenie:bardzo; wysokie-pobudzenie:bardzo; chaos-balagan:bardzo; wycofanie:bardzo; komunikacja-problem:bardzo; dysfunkcja-wykonawcza:bardzo; dom:bardzo; maskowanie:bardzo; kontrola-wizerunku:bardzo; zapominanie-gubienie:bardzo; utrata:bardzo; emocjonalna-dysregulacja:bardzo; zablokowanie:bardzo; smierc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000138','2026-09-03','milosc:bardzo; zazdrosc:bardzo; gniew:bardzo; wysokie-pobudzenie:bardzo; noc:bardzo; bezsennosc-restless:bardzo; samotnosc:bardzo; smutek:bardzo; strach:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; smierc:bardzo; cialo:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000139','2026-09-03','droga-podroz:bardzo; powrot-do:bardzo; do-siebie:bardzo; wolnosc:bardzo; sprawczosc:bardzo; cyklicznosc-wzorzec:bardzo; strach:bardzo; nierozpoznanie-siebie:bardzo; zablokowanie:bardzo; sprzeczne-potrzeby:bardzo; ku-przyszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000140','2026-09-03','marzenie:bardzo; deszcz:bardzo; komunikacja-problem:bardzo; potrzeba-zapewnienia:bardzo; kontrola-wizerunku:bardzo; maska:bardzo; cialo:troche; sensoryka-metafora:bardzo; do-swiata:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000141','2026-09-03','sen:bardzo; noc:bardzo; bezsennosc-restless:bardzo; droga-podroz:bardzo; cialo:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; wysokie-pobudzenie:bardzo; milosc:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; unikanie-z-leku:bardzo; emocja-przez-cialo:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000142','2026-09-03','milosc:bardzo; oddech-powietrze:bardzo; ulga-z-zewnatrz:bardzo; zapominanie-gubienie:troche; nigdy-dosc:bardzo; czas:bardzo; komunikacja-problem:bardzo; woda:troche; ku-komus:bardzo; sprzeczne-potrzeby:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000143','2026-09-03','komunikacja-problem:bardzo; sprawdzanie:bardzo; frustracja:bardzo; sensoryka-przytloczenie:bardzo; chaos-balagan:bardzo; zablokowanie:bardzo; taniec:troche; cialo:troche; sensoryka-metafora:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000144','2026-09-03','pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; ogien:bardzo; oddech-powietrze:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; gniew:bardzo; czas:bardzo; latanie-spadanie:troche; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; nigdy-dosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000145','2026-09-03','do-swiata:bardzo; wstret:bardzo; gniew:bardzo; sensoryka-przytloczenie:bardzo; substancje:bardzo; noc:bardzo; czas:bardzo; droga-podroz:bardzo; rutyna-repetycja:bardzo; cyklicznosc-wzorzec:bardzo; smierc:troche; innosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000146','2026-09-03','dom:bardzo; powrot-do:bardzo; prawda:bardzo; komunikacja-problem:bardzo; do-siebie:bardzo; innosc:bardzo; sprawczosc:bardzo; pozadanie:troche; kontrola:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000147','2026-09-03','dom:bardzo; cialo:bardzo; ja-publiczne-ja-prywatne:bardzo; sprzeczne-potrzeby:bardzo; noc:bardzo; bezsennosc-restless:bardzo; nadmierny-sen:troche; sensoryka-przytloczenie:bardzo; hiperczujnosc:bardzo; zablokowanie:bardzo; cyklicznosc-wzorzec:bardzo; ciemnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000148','2026-09-03','smierc:bardzo; pozadanie:bardzo; cialo:bardzo; woda:bardzo; czulosc:troche; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:bardzo; czas:troche; intensywna-percepcja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000149','2026-09-03','wycofanie:bardzo; niskie-pobudzenie:bardzo; anhedonia:bardzo; zobojetnienie:bardzo; sensoryka-przytloczenie:bardzo; cialo:bardzo; dotyk:bardzo; ukrywanie-reakcji:bardzo; maska:bardzo; noc:bardzo; ciemnosc:bardzo; przemiana:bardzo; odrodzenie:bardzo; komunikacja-problem:bardzo; gniew:bardzo; ogien:bardzo; czas:bardzo; zablokowanie:bardzo; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000150','2026-09-03','nic-pustka:bardzo; cyklicznosc-wzorzec:bardzo; nuda-nietolerancja:troche; cialo:bardzo; droga-podroz:bardzo; przemiana:bardzo; odrodzenie:bardzo; ulga-z-zewnatrz:bardzo; czulosc:bardzo; czas:bardzo; przetrwanie:bardzo; nadzieja:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000151','2026-09-03','wysokie-pobudzenie:bardzo; impulsywnosc:bardzo; czas:bardzo; ogien:bardzo; wina:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; frustracja:bardzo; strach:troche; sprawczosc:bardzo; przemiana:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000152','2026-09-03','wyczerpanie:bardzo; bezsilnosc:bardzo; czas:bardzo; deszcz:bardzo; racing-thoughts:troche; wspomnienia:bardzo; ku-przeszlosci:bardzo; przemiana:bardzo; odrodzenie:bardzo; droga-podroz:bardzo; nadzieja:bardzo; sensoryka-metafora:bardzo; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000153','2026-09-03','strach:bardzo; schronienie:bardzo; ulga-z-zewnatrz:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; ciemnosc:bardzo; zapominanie-gubienie:bardzo; nierozpoznanie-siebie:troche; potrzeba-zapewnienia:bardzo; przetrwanie:bardzo; nadzieja:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000154','2026-09-03','czas:bardzo; wstyd:bardzo; marzenie:bardzo; latanie-spadanie:bardzo; sen:bardzo; nadmierny-sen:bardzo; zobojetnienie:troche; wycofanie:bardzo; znikniecie:bardzo; ku-przyszlosci:bardzo; droga-podroz:bardzo; sprzeczne-potrzeby:bardzo; smutek:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000155','2026-09-03','sensoryka-przytloczenie:bardzo; sensoryka-szukanie:bardzo; maskowanie:bardzo; dopasowanie-roli:bardzo; woda:bardzo; cyklicznosc-wzorzec:bardzo; wycofanie:bardzo; spokoj:bardzo; ulga:bardzo; do-siebie:bardzo; do-swiata:troche; przemiana:bardzo; odrodzenie:troche; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000156','2026-09-03','milosc:bardzo; komunikacja-problem:bardzo; rutyna-repetycja:bardzo; zapominanie-gubienie:bardzo; wina:bardzo; dotyk:bardzo; ku-komus:bardzo; nadzieja:bardzo; droga-podroz:troche; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000157','2026-09-03','strach:bardzo; milosc:bardzo; deszcz:bardzo; smutek:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; przemiana:bardzo; znikniecie:bardzo; taniec:bardzo; radosc:troche; wysokie-pobudzenie:troche; utrata:bardzo; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000158','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; marzenie:bardzo; droga-podroz:bardzo; czas:bardzo; racing-thoughts:bardzo; sen:bardzo; cyklicznosc-wzorzec:bardzo; nigdy-dosc:bardzo; woda:bardzo; noc:bardzo; tesknota:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000159','2026-09-03','oddech-powietrze:bardzo; ziemia:bardzo; woda:bardzo; sensoryka-metafora:bardzo; utrata:bardzo; od-kogos:bardzo; droga-podroz:bardzo; ucieczka:bardzo; zablokowanie:bardzo; sprawczosc:bardzo; nadzieja:troche; intensywna-percepcja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000160','2026-09-03','milosc:bardzo; ukrywanie-potrzeb:bardzo; komunikacja-problem:bardzo; przemiana:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:troche; wolnosc:bardzo; sprzeczne-potrzeby:troche; czas:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000161','2026-09-03','sensoryka-przytloczenie:bardzo; samotnosc:bardzo; komunikacja-problem:bardzo; brak-nadziei:bardzo; wyczerpanie:bardzo; emocjonalna-dysregulacja:bardzo; przemiana:bardzo; odrodzenie:bardzo; nierozpoznanie-siebie:bardzo; do-swiata:bardzo; lek:bardzo; przeciazenie-przyszloscia:bardzo; pozadanie:troche; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000162','2026-09-03','rutyna-repetycja:bardzo; droga-podroz:bardzo; cialo:bardzo; wina:troche; komunikacja-problem:bardzo; cyklicznosc-wzorzec:bardzo; zablokowanie:bardzo; ku-komus:troche; frustracja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000163','2026-09-03','droga-podroz:bardzo; sprawczosc:bardzo; czas:bardzo; smutek:bardzo; substancje:bardzo; ukrywanie-reakcji:bardzo; maska:bardzo; kontrola-wizerunku:troche; wyczerpanie:bardzo; utrata:bardzo; od-kogos:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000164','2026-09-03','niskie-pobudzenie:bardzo; wycofanie:bardzo; samotnosc-preferowana:bardzo; sensoryka-szukanie:bardzo; deszcz:bardzo; strach:troche; napiecie-ciala:bardzo; do-swiata:troche; droga-podroz:troche; zobojetnienie:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000165','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; sen:bardzo; marzenie:bardzo; smutek:bardzo; melancholia:bardzo; utrata:bardzo; tesknota:bardzo; znikniecie:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000167','2026-09-03','komunikacja-problem:bardzo; unikanie-z-leku:bardzo; lek-antycypacyjny:bardzo; niepewnosc-nie-do-zniesienia:bardzo; nadzieja:troche; przeciazenie-przyszloscia:bardzo; kontrola:bardzo; hiperczujnosc:troche; pozadanie:troche; utrata:bardzo; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000168','2026-09-03','milosc:bardzo; ukrywanie-potrzeb:bardzo; komunikacja-problem:bardzo; marzenie:bardzo; latanie-spadanie:bardzo; droga-podroz:bardzo; woda:bardzo; noc:bardzo; samotnosc:bardzo; tesknota:bardzo; czas:bardzo; strach:troche; wstyd:troche; ku-komus:bardzo; od-kogos:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000780','2026-09-03','cialo:bardzo; emocja-przez-cialo:bardzo; wstyd:bardzo; strach:bardzo; unikanie-z-leku:bardzo; zablokowanie:bardzo; komunikacja-problem:bardzo; ukrywanie-reakcji:bardzo; pozadanie:troche; sprzeczne-emocje:bardzo; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000169','2026-09-03','sen:bardzo; nadmierny-sen:bardzo; marzenie:bardzo; niskie-pobudzenie:bardzo; brak-napedu:bardzo; wycofanie:bardzo; strach:bardzo; przemiana:bardzo; odrodzenie:bardzo; do-siebie:bardzo; zablokowanie:bardzo; nierozpoznanie-siebie:troche; cialo:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000170','2026-09-03','ukrywanie-potrzeb:bardzo; samokontrola-spoleczna:bardzo; maskowanie:bardzo; komunikacja-problem:bardzo; nierozpoznanie-siebie:bardzo; zapominanie-gubienie:bardzo; pamiec:troche; oddech-powietrze:bardzo; cialo:troche; zablokowanie:bardzo; do-siebie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000171','2026-09-03','wolnosc:bardzo; kontrola:bardzo; ogien:bardzo; cialo:bardzo; ciemnosc:bardzo; nic-pustka:bardzo; droga-podroz:bardzo; sensoryka-metafora:bardzo; emocja-przez-cialo:bardzo; sprawczosc:bardzo; zablokowanie:bardzo; wysokie-pobudzenie:bardzo; przemiana:bardzo; do-siebie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000172','2026-09-03','samotnosc:bardzo; wstyd:bardzo; milosc:bardzo; pozadanie:bardzo; cialo:bardzo; utrata:bardzo; bezwartosciowosc:troche; zobojetnienie:bardzo; brak-nadziei:bardzo; bezsennosc-restless:troche; maska:bardzo; od-kogos:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000173','2026-09-03','droga-podroz:bardzo; dom:bardzo; ku-przyszlosci:bardzo; czas:bardzo; wspomnienia:troche; milosc:troche; oddech-powietrze:bardzo; ziemia:bardzo; sensoryka-metafora:bardzo; innosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000779','2026-09-03','dom:bardzo; ogien:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; do-swiata:bardzo; prawda:bardzo; wolnosc:troche; sensoryka-metafora:bardzo; bezsilnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000174','2026-09-03','cel-nieosiagniety:bardzo; droga-podroz:bardzo; sprawczosc:bardzo; niedopasowanie-spoleczne:bardzo; innosc:bardzo; wstyd:bardzo; nierozpoznanie-siebie:bardzo; nie-wiem-co-czuje:bardzo; maskowanie-koszt:bardzo; bunt:bardzo; wolnosc:bardzo; demand-avoidance:bardzo; do-siebie:bardzo; do-swiata:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000438','','');

INSERT INTO tag_snapshots VALUES('lyrics-000175','2026-09-03','droga-podroz:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; strach:bardzo; zamartwianie:bardzo; dom:bardzo; milosc:bardzo; tesknota:bardzo; sen:bardzo; cyklicznosc-wzorzec:bardzo; od-kogos:bardzo; przemiana:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000176','2026-09-03','nadzieja:bardzo; smutek:bardzo; ku-przyszlosci:bardzo; odrodzenie:bardzo; przemiana:bardzo; milosc:bardzo; droga-podroz:bardzo; latanie-spadanie:bardzo; czas:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000177','2026-09-03','milosc:bardzo; zazdrosc:bardzo; ciemnosc:bardzo; sen:bardzo; sprzeczne-emocje:bardzo; od-kogos:bardzo; ku-komus:bardzo; cyklicznosc-wzorzec:bardzo; wysokie-pobudzenie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000178','2026-09-03','performowanie-roli:bardzo; kontrola-wizerunku:bardzo; ja-publiczne-ja-prywatne:troche; znikniecie:bardzo; wspomnienia:troche; ku-przeszlosci:troche; innosc:bardzo; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000179','2026-09-03','powrot-do:troche; utrata:troche; ziemia:troche; dotyk:ociupinke');

INSERT INTO tag_snapshots VALUES('lyrics-000180','2026-09-03','sen:bardzo; bezsennosc-restless:bardzo; ucieczka:bardzo; droga-podroz:bardzo; nic-pustka:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; ogien:bardzo; pamiec:bardzo; wspomnienia:troche; ku-przyszlosci:bardzo; ku-przeszlosci:bardzo; dom:troche; sensoryka-szukanie:bardzo; zablokowanie:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000181','2026-09-03','droga-podroz:bardzo; sprawczosc:bardzo; przemiana:bardzo; odrodzenie:troche; ku-przyszlosci:bardzo; nadzieja:bardzo; prawda:troche; duma:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000182','2026-09-03','nic-pustka:bardzo; nierozpoznanie-siebie:bardzo; komunikacja-problem:bardzo; prawda:bardzo; strach:troche; zobojetnienie:bardzo; ogien:bardzo; smierc:bardzo; sprzeczne-emocje:bardzo; sensoryka-metafora:bardzo; do-siebie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000183','2026-09-03','prawda:bardzo; maska:bardzo; kontrola-wizerunku:bardzo; milosc:bardzo; pozadanie:bardzo; cialo:bardzo; substancje:bardzo; substancja-regulacja:troche; noc:bardzo; woda:bardzo; droga-podroz:bardzo; przetrwanie:bardzo; pamiec:troche; zapominanie-gubienie:troche; deszcz:bardzo; utrata:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000184','2026-09-03','hiperczujnosc:bardzo; zamartwianie:bardzo; racing-thoughts:bardzo; napiecie-ciala:bardzo; czas:bardzo; time-blindness:bardzo; cyklicznosc-wzorzec:bardzo; zablokowanie:bardzo; ziemia:bardzo; droga-podroz:bardzo; sensoryka-metafora:bardzo; nierozpoznanie-siebie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000185','2026-09-03','droga-podroz:troche; sprzeczne-emocje:troche; radosc:troche; smutek:troche; impulsywnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000186','2026-09-03','milosc:bardzo; pogon:bardzo; cel-nieosiagniety:bardzo; droga-podroz:bardzo; samotnosc:bardzo; niedopasowanie-spoleczne:troche; czas:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-komus:bardzo; tesknota:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000187','2026-09-03','noc:bardzo; czas:bardzo; utrata:bardzo; smutek:bardzo; tesknota:bardzo; woda:bardzo; droga-podroz:bardzo; ku-komus:bardzo; czulosc:bardzo; ciemnosc:bardzo; wspomnienia:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000188','2026-09-03','strach:bardzo; lek:bardzo; katastrofizacja:bardzo; przeciazenie-przyszloscia:bardzo; do-swiata:bardzo; milosc:bardzo; czulosc:bardzo; nadzieja:bardzo; wolnosc:bardzo; sprawczosc:bardzo; noc:bardzo; czas:bardzo; droga-podroz:bardzo; do-siebie:bardzo; spokoj:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000189','2026-09-03','specjalne-zainteresowanie-osoba:bardzo; hiperfokus:bardzo; milosc:bardzo; czulosc:bardzo; komunikacja-problem:troche; ku-komus:bardzo; cyklicznosc-wzorzec:bardzo; odrodzenie:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000190','2026-09-03','milosc:bardzo; komunikacja-problem:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; ulga-odroczona:bardzo; czas:bardzo; przemiana:bardzo; odrodzenie:troche; cyklicznosc-wzorzec:bardzo; potrzeba-zapewnienia:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000191','2026-09-03','milosc:bardzo; utrata:bardzo; odrodzenie:bardzo; przemiana:bardzo; dom:bardzo; droga-podroz:bardzo; marzenie:bardzo; sen:bardzo; substancje:troche; ciemnosc:bardzo; sensoryka-metafora:bardzo; ku-przyszlosci:bardzo; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000192','2026-09-03','czas:bardzo; cyklicznosc-wzorzec:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; komunikacja-problem:troche; spokoj:troche; sensoryka-szukanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000193','2026-09-03','dom:bardzo; ucieczka:bardzo; od-kogos:bardzo; kontrola:bardzo; komunikacja-problem:bardzo; maskowanie:bardzo; kontrola-wizerunku:bardzo; znikniecie:bardzo; droga-podroz:bardzo; unikanie-z-leku:troche; sprawczosc:bardzo; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000194','2026-09-03','smutek:bardzo; samotnosc:bardzo; niedopasowanie-spoleczne:bardzo; komunikacja-problem:bardzo; bezsilnosc:bardzo; do-siebie:bardzo; nierozpoznanie-siebie:bardzo; przemiana:bardzo; odrodzenie:bardzo; nadzieja:bardzo; czulosc:troche; wyczerpanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000195','2026-09-03','sensoryka-szukanie:bardzo; pozadanie:bardzo; komunikacja-problem:bardzo; zablokowanie:troche; intensywna-percepcja:troche; maska:troche; ku-komus:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000786','2026-09-03','milosc:bardzo; czulosc:bardzo; dotyk:bardzo; sen:bardzo; schronienie:bardzo; dom:bardzo; woda:bardzo; droga-podroz:bardzo; pogon:bardzo; ku-komus:bardzo; noc:bardzo; czas:bardzo; niepewnosc-nie-do-zniesienia:troche; ulga-z-zewnatrz:bardzo; tesknota:bardzo; sensoryka-metafora:bardzo; cialo:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000196','2026-09-03','marzenie:bardzo; ucieczka:bardzo; droga-podroz:bardzo; dom:bardzo; wysokie-pobudzenie:bardzo; sensoryka-przytloczenie:bardzo; sensoryka-szukanie:bardzo; przemiana:bardzo; odrodzenie:bardzo; deszcz:bardzo; strach:troche; zablokowanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000197','2026-09-03','milosc:bardzo; wolnosc:bardzo; nigdy-dosc:bardzo; pozadanie:bardzo; przemiana:bardzo; odrodzenie:troche; sensoryka-szukanie:bardzo; do-swiata:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000789','2026-09-03','do-swiata:bardzo; smierc:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; marzenie:bardzo; prawda:bardzo; gniew:bardzo; zal:bardzo; bezsilnosc:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000198','2026-09-03','samotnosc:bardzo; anhedonia:bardzo; deszcz:bardzo; sprawdzanie:bardzo; kontrola:troche; milosc:troche; czulosc:troche; sprawczosc:bardzo; do-swiata:bardzo; zablokowanie:troche; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000199','2026-09-03','prawda:bardzo; maska:bardzo; ucieczka:bardzo; milosc:bardzo; ogien:bardzo; cialo:bardzo; nic-pustka:troche; duma:bardzo; radosc:bardzo; czas:bardzo; wspomnienia:troche; zal:bardzo; przemiana:bardzo; odrodzenie:troche; sprawczosc:bardzo; do-siebie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000200','2026-09-03','zamartwianie:bardzo; lek-antycypacyjny:bardzo; katastrofizacja:bardzo; przeciazenie-przyszloscia:bardzo; bezwartosciowosc:bardzo; samotnosc:bardzo; substancje:troche; wspomnienia:bardzo; pamiec:bardzo; marzenie:bardzo; smierc-wlasna:bardzo; woda:bardzo; komunikacja-problem:bardzo; ukrywanie-reakcji:bardzo; sprawczosc:troche; czas:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; niepewnosc-nie-do-zniesienia:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000201','2026-09-03','marzenie:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; substancje:bardzo; droga-podroz:bardzo; ziemia:bardzo; radosc:bardzo; smutek:bardzo; sprzeczne-emocje:bardzo; wolnosc:bardzo; ku-komus:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000202','2026-09-03','innosc:bardzo; niedopasowanie-spoleczne:bardzo; bunt:bardzo; marzenie:bardzo; substancje:bardzo; duma:bardzo; kontrola-wizerunku:troche; performowanie-roli:bardzo; wolnosc:troche; radosc:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000203','2026-09-03','smierc:bardzo; sen:bardzo; wspomnienia:bardzo; pamiec:bardzo; racing-thoughts:bardzo; wina:bardzo; smutek:bardzo; zal:bardzo; utrata:bardzo; czas:bardzo; ku-przeszlosci:bardzo; zablokowanie:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000204','2026-09-03','racing-thoughts:bardzo; nuda-nietolerancja:bardzo; anhedonia:bardzo; brak-nadziei:bardzo; zablokowanie:bardzo; samotnosc:bardzo; niedopasowanie-spoleczne:bardzo; potrzeba-zapewnienia:bardzo; bezwartosciowosc:troche; do-swiata:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000205','2026-09-03','strach:bardzo; lek-antycypacyjny:bardzo; komunikacja-problem:bardzo; milosc:bardzo; potrzeba-zapewnienia:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; droga-podroz:bardzo; ucieczka:bardzo; ciemnosc:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000206','2026-09-03','impulsywnosc:bardzo; wysokie-pobudzenie:bardzo; do-swiata:bardzo; gniew:bardzo; smierc:bardzo; strach:bardzo; sprawczosc:bardzo; droga-podroz:bardzo; bunt:bardzo; czas:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000207','2026-09-03','maskowanie:bardzo; kontrola-wizerunku:bardzo; wstyd:bardzo; lek:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; sen:bardzo; marzenie:bardzo; latanie-spadanie:bardzo; przeciazenie-przyszloscia:bardzo; niedopasowanie-spoleczne:bardzo; performowanie-roli:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000208','2026-09-03','bunt:bardzo; kontrola:bardzo; do-swiata:bardzo; gniew:bardzo; niedopasowanie-spoleczne:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000209','2026-09-03','droga-podroz:bardzo; dom:bardzo; noc:bardzo; ciemnosc:bardzo; strach:bardzo; wstyd:bardzo; nadzieja:bardzo; samotnosc:bardzo; utrata:bardzo; wspomnienia:bardzo; woda:bardzo; przemiana:troche; wyczerpanie:bardzo; przetrwanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000210','2026-09-03','utrata:bardzo; anhedonia:bardzo; samotnosc:bardzo; wolnosc:bardzo; od-kogos:bardzo; przemiana:bardzo; odrodzenie:troche; ku-przyszlosci:bardzo; zal:bardzo; milosc:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000211','2026-09-03','droga-podroz:bardzo; ziemia:bardzo; woda:bardzo; deszcz:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; samotnosc-preferowana:bardzo; pamiec:bardzo; wspomnienia:troche; smutek:bardzo; wolnosc:bardzo; czas:bardzo; do-siebie:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000212','2026-09-03','innosc:bardzo; niedopasowanie-spoleczne:bardzo; duma:bardzo; do-swiata:bardzo; sprawczosc:bardzo; noc:bardzo; droga-podroz:bardzo; prawda:bardzo; kontrola-wizerunku:troche; performowanie-roli:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000213','2026-09-03','milosc:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; wina:bardzo; dotyk:bardzo; noc:bardzo; utrata:bardzo; od-kogos:bardzo; czulosc:troche; komunikacja-problem:troche; zapominanie-gubienie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000214','2026-09-03','smierc:bardzo; wysokie-pobudzenie:bardzo; gniew:bardzo; strach:bardzo; cialo:bardzo; utrata:bardzo; samotnosc:bardzo; sprawczosc:bardzo; droga-podroz:bardzo; cyklicznosc-wzorzec:bardzo; do-innych:bardzo; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000215','2026-09-03','milosc:bardzo; pozadanie:bardzo; dotyk:bardzo; czulosc:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; ukrywanie-reakcji:bardzo; czas:bardzo; ku-komus:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000216','2026-09-03','noc:bardzo; sensoryka-metafora:bardzo; droga-podroz:bardzo; cyklicznosc-wzorzec:bardzo; pozadanie:bardzo; zablokowanie:troche; czas:bardzo; intensywna-percepcja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000217','2026-09-03','marzenie:bardzo; woda:bardzo; droga-podroz:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; milosc:bardzo; dotyk:bardzo; czulosc:bardzo; deszcz:bardzo; noc:bardzo; wolnosc:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; sprawczosc:bardzo; sensoryka-szukanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000218','2026-09-03','samotnosc:bardzo; ogien:bardzo; znikniecie:bardzo; smierc:bardzo; wysokie-pobudzenie:bardzo; sensoryka-przytloczenie:bardzo; sensoryka-szukanie:bardzo; cialo:troche; cyklicznosc-wzorzec:bardzo; do-swiata:troche; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000219','2026-09-03','milosc:bardzo; utrata:bardzo; samotnosc:bardzo; ciemnosc:bardzo; dom:bardzo; zamartwianie:bardzo; niepewnosc-nie-do-zniesienia:bardzo; niemoznosc-odpuszczenia:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; od-kogos:bardzo; tesknota:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000220','2026-09-03','sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; deszcz:bardzo; noc:bardzo; taniec:troche; performowanie-roli:bardzo; rutyna-repetycja:bardzo; czas:bardzo; substancje:troche; do-swiata:bardzo; dom:troche; spokoj:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000221','2026-09-03','samotnosc:bardzo; strach:bardzo; potrzeba-zapewnienia:bardzo; milosc:bardzo; komunikacja-problem:bardzo; ukrywanie-potrzeb:bardzo; ku-komus:bardzo; czas:bardzo; przeciazenie-przyszloscia:troche; schronienie:bardzo; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000222','2026-09-03','milosc:bardzo; wina:bardzo; duma:bardzo; smierc-wlasna:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; komunikacja-problem:bardzo; ciemnosc:bardzo; droga-podroz:bardzo; do-siebie:bardzo; sprzeczne-emocje:bardzo; impulsywnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000223','2026-09-03','cialo:bardzo; emocja-przez-cialo:bardzo; kontrola:bardzo; zablokowanie:bardzo; wolnosc:bardzo; od-kogos:bardzo; strach:troche; substancje:troche; sensoryka-metafora:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000224','2026-09-03','do-swiata:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; bunt:bardzo; bezsilnosc:bardzo; sprawczosc:troche; gniew:bardzo; smierc:troche; prawda:bardzo; przeciazenie-przyszloscia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000225','2026-09-03','milosc:bardzo; komunikacja-problem:bardzo; racing-thoughts:bardzo; strach:troche; samotnosc:bardzo; ciemnosc:bardzo; potrzeba-zapewnienia:bardzo; ogien:bardzo; sen:bardzo; czulosc:bardzo; ku-komus:bardzo; cyklicznosc-wzorzec:bardzo; wysokie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000226','2026-09-03','utrata:bardzo; milosc:bardzo; nierozpoznanie-siebie:bardzo; noc:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; wstyd:bardzo; duma:bardzo; dotyk:bardzo; czas:bardzo; woda:bardzo; ziemia:bardzo; oddech-powietrze:bardzo; znikniecie:bardzo; tesknota:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000227','2026-09-03','utrata:bardzo; milosc:bardzo; nierozpoznanie-siebie:bardzo; noc:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; wstyd:bardzo; duma:bardzo; dotyk:bardzo; czas:bardzo; woda:bardzo; ziemia:bardzo; oddech-powietrze:bardzo; znikniecie:bardzo; tesknota:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000228','2026-09-03','milosc:bardzo; pozadanie:bardzo; sprzeczne-emocje:bardzo; wina:troche; ogien:bardzo; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:bardzo; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000229','2026-09-03','milosc:bardzo; potrzeba-zapewnienia:bardzo; komunikacja-problem:bardzo; prawda:bardzo; ciemnosc:bardzo; latanie-spadanie:bardzo; wspomnienia:bardzo; pamiec:bardzo; sen:bardzo; ucieczka:bardzo; kontrola:bardzo; cyklicznosc-wzorzec:bardzo; lek-antycypacyjny:troche; czas:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000230','2026-09-03','samotnosc:bardzo; rozpacz:bardzo; komunikacja-problem:bardzo; nadzieja:bardzo; czas:bardzo; milosc:bardzo; woda:bardzo; dom:bardzo; potrzeba-zapewnienia:bardzo; cyklicznosc-wzorzec:bardzo; do-swiata:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000231','2026-09-03','droga-podroz:bardzo; przemiana:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; cialo:bardzo; pozadanie:bardzo; substancje:bardzo; impulsywnosc:bardzo; wysokie-pobudzenie:bardzo; sprawczosc:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000232','2026-09-03','substancje:bardzo; chaos-balagan:bardzo; wysokie-pobudzenie:bardzo; smierc:bardzo; odrodzenie:bardzo; bunt:bardzo; do-swiata:bardzo; sensoryka-przytloczenie:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000233','2026-09-03','samotnosc:bardzo; strach:bardzo; sprawczosc:bardzo; wolnosc:bardzo; do-siebie:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; przemiana:bardzo; odrodzenie:bardzo; niepewnosc-nie-do-zniesienia:troche; zablokowanie:troche; duma:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000234','2026-09-03','od-kogos:bardzo; komunikacja-problem:bardzo; gniew:bardzo; zablokowanie:bardzo; czas:bardzo; racing-thoughts:troche; sensoryka-metafora:bardzo; sprawczosc:bardzo; utrata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000235','2026-09-03','droga-podroz:bardzo; dom:bardzo; samotnosc:bardzo; smierc:bardzo; pamiec:bardzo; utrata:bardzo; milosc:bardzo; dotyk:bardzo; cialo:bardzo; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo; przetrwanie:bardzo; strach:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000236','2026-09-03','sensoryka-przytloczenie:bardzo; intensywna-percepcja:bardzo; cialo:bardzo; taniec:bardzo; komunikacja-problem:bardzo; kontrola-wizerunku:bardzo; performowanie-roli:bardzo; hiperczujnosc:bardzo; substancje:bardzo; innosc:bardzo; niedopasowanie-spoleczne:troche; wstyd:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000237','2026-09-03','nigdy-dosc:bardzo; nuda-nietolerancja:bardzo; frustracja:bardzo; sensoryka-przytloczenie:bardzo; pozadanie:bardzo; droga-podroz:bardzo; cyklicznosc-wzorzec:bardzo; substancje:troche; do-swiata:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000238','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; droga-podroz:bardzo; substancje:bardzo; taniec:bardzo; smierc:bardzo; przetrwanie:bardzo; wysokie-pobudzenie:bardzo; chaos-balagan:bardzo; woda:bardzo; do-swiata:bardzo; sensoryka-przytloczenie:bardzo; cyklicznosc-wzorzec:bardzo; innosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000239','2026-09-03','prawda:bardzo; ogien:bardzo; noc:bardzo; milosc:bardzo; pozadanie:bardzo; czas:bardzo; smierc:troche; wysokie-pobudzenie:bardzo; sprawczosc:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000240','2026-09-03','samotnosc:bardzo; wolnosc:bardzo; smierc:bardzo; cialo:bardzo; smutek:bardzo; zal:bardzo; bezsilnosc:bardzo; zablokowanie:bardzo; ciemnosc:troche; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000241','2026-09-03','milosc:bardzo; noc:bardzo; droga-podroz:bardzo; taniec:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; tesknota:bardzo; ku-komus:bardzo; dotyk:bardzo; pozadanie:troche; pogon:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000242','2026-09-03','substancje:bardzo; sensoryka-przytloczenie:bardzo; intensywna-percepcja:bardzo; nie-wiem-co-czuje:bardzo; time-blindness:bardzo; cialo:bardzo; pozadanie:troche; ku-komus:bardzo; lek:bardzo; wysokie-pobudzenie:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000243','2026-09-03','ciemnosc:bardzo; utrata:bardzo; milosc:bardzo; smutek:bardzo; anhedonia:bardzo; pustka-emocjonalna:bardzo; znikniecie:bardzo; wycofanie:bardzo; do-siebie:bardzo; woda:troche; noc:bardzo; czas:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000244','2026-09-03','milosc:bardzo; samotnosc:bardzo; zamartwianie:bardzo; potrzeba-zapewnienia:bardzo; ulga-z-zewnatrz:bardzo; ku-komus:bardzo; pozadanie:bardzo; sprzeczne-potrzeby:troche; lek-antycypacyjny:troche; zablokowanie:bardzo; komunikacja-problem:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000245','2026-09-03','prawda:bardzo; milosc:bardzo; samotnosc:bardzo; smutek:bardzo; potrzeba-zapewnienia:bardzo; ku-komus:bardzo; komunikacja-problem:bardzo; cialo:troche; utrata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000246','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; noc:bardzo; dom:bardzo; impulsywnosc:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; cyklicznosc-wzorzec:bardzo; chaos-balagan:troche; ja-publiczne-ja-prywatne:bardzo; dopasowanie-roli:troche; rutyna-repetycja:bardzo; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000247','2026-09-03','smierc:bardzo; cialo:bardzo; gniew:bardzo; bunt:bardzo; do-swiata:bardzo; strach:bardzo; czulosc:bardzo; schronienie:bardzo; woda:troche; sprawczosc:bardzo; przetrwanie:bardzo; komunikacja-problem:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000248','2026-09-03','noc:bardzo; dom:bardzo; substancje:bardzo; niedopasowanie-spoleczne:bardzo; rutyna-repetycja:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-szukanie:troche; do-swiata:bardzo; chaos-balagan:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000249','2026-09-03','marzenie:bardzo; cel-nieosiagniety:bardzo; czas:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; ogien:bardzo; gniew:bardzo; sensoryka-metafora:bardzo; euforia-naped:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000250','2026-09-03','do-swiata:bardzo; nigdy-dosc:bardzo; duma:bardzo; marzenie:troche; droga-podroz:troche; substancje:troche; gniew:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000251','2026-09-03','cialo:bardzo; smutek:bardzo; przemiana:bardzo; odrodzenie:bardzo; gniew:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; sensoryka-metafora:bardzo; sprawczosc:bardzo; do-swiata:bardzo; nadzieja:bardzo; deszcz:bardzo; ogien:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000252','2026-09-03','do-siebie:bardzo; wina:bardzo; prawda:bardzo; nadzieja:bardzo; nierozpoznanie-siebie:bardzo; komunikacja-problem:bardzo; emocjonalna-dysregulacja:troche; marzenie:bardzo; wspomnienia:troche; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000253','2026-09-03','noc:bardzo; substancje:bardzo; substancja-regulacja:bardzo; impulsywnosc:bardzo; emocjonalna-dysregulacja:bardzo; wysokie-pobudzenie:bardzo; pozadanie:troche; taniec:bardzo; cialo:bardzo; dosc-przesyt:troche; rozpad:bardzo; sprzeczne-emocje:bardzo; samotnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000254','2026-09-03','milosc:bardzo; maska:bardzo; ukrywanie-reakcji:bardzo; kontrola-wizerunku:bardzo; ja-publiczne-ja-prywatne:bardzo; noc:bardzo; ciemnosc:bardzo; droga-podroz:bardzo; smierc:bardzo; sprzeczne-potrzeby:bardzo; ku-komus:bardzo; woda:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000255','2026-09-03','pozadanie:bardzo; cialo:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; milosc:troche; substancje:troche; noc:troche; do-swiata:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000256','2026-09-03','milosc:bardzo; utrata:bardzo; od-kogos:bardzo; zal:bardzo; wina:bardzo; substancje:bardzo; substancja-regulacja:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; sprawczosc:bardzo; gniew:bardzo; komunikacja-problem:bardzo; droga-podroz:bardzo; oddech-powietrze:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000257','2026-09-03','droga-podroz:bardzo; wolnosc:bardzo; sprawczosc:bardzo; ku-przyszlosci:bardzo; samotnosc:troche; dom:troche; do-swiata:bardzo; sensoryka-szukanie:bardzo; nadzieja:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000259','2026-09-03','cialo:bardzo; milosc:bardzo; ku-komus:bardzo; sprawczosc:troche; komunikacja-problem:bardzo; wina:troche; cyklicznosc-wzorzec:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000260','2026-09-03','wolnosc:bardzo; droga-podroz:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; impulsywnosc:bardzo; smierc:troche; sprawczosc:bardzo; noc:bardzo; cialo:troche; euforia-naped:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000261','2026-09-03','milosc:bardzo; wolnosc:bardzo; sprzeczne-potrzeby:bardzo; utrata:bardzo; samotnosc:bardzo; tesknota:bardzo; potrzeba-zapewnienia:bardzo; lek-antycypacyjny:bardzo; bezsennosc:bardzo; cialo:bardzo; dom:bardzo; zablokowanie:bardzo; kontrola:bardzo; zazdrosc:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000262','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; wstyd:bardzo; maskowanie:bardzo; ukrywanie-reakcji:bardzo; ja-publiczne-ja-prywatne:bardzo; cialo:bardzo; strach:bardzo; dom:bardzo; ucieczka:bardzo; droga-podroz:troche; wina:bardzo; prawda:bardzo; nierozpoznanie-siebie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000263','2026-09-03','milosc:bardzo; schronienie:bardzo; ucieczka:bardzo; od-swiata:bardzo; dotyk:bardzo; cialo:bardzo; czulosc:bardzo; ulga-z-zewnatrz:bardzo; spokoj:bardzo; woda:bardzo; maska:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000264','2026-09-03','sen:bardzo; marzenie:bardzo; ziemia:bardzo; noc:bardzo; taniec:bardzo; radosc:bardzo; milosc:bardzo; ogien:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; innosc:bardzo; ku-komus:troche; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000265','2026-09-03','hiperfokus:bardzo; specjalne-zainteresowanie-osoba:bardzo; bezsennosc-restless:bardzo; niemoznosc-odpuszczenia:bardzo; smutek:bardzo; cyklicznosc-wzorzec:bardzo; ku-komus:bardzo; zablokowanie:bardzo; czas:bardzo; niskie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000266','2026-09-03','cialo:bardzo; milosc:bardzo; ku-komus:bardzo; komunikacja-problem:bardzo; wina:troche; cyklicznosc-wzorzec:troche; sensoryka-metafora:bardzo; ulga:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000267','2026-09-03','przemiana:bardzo; czas:bardzo; brak-nadziei:bardzo; prawda:bardzo; komunikacja-problem:bardzo; cyklicznosc-wzorzec:bardzo; zablokowanie:bardzo; sprawczosc:troche; do-swiata:troche; smutek:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000268','2026-09-03','smierc:bardzo; wina:bardzo; zal:bardzo; do-swiata:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; przetrwanie:bardzo; sprawczosc:troche; radosc:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000269','2026-09-03','lek:bardzo; maskowanie:bardzo; ukrywanie-reakcji:bardzo; samokontrola-spoleczna:bardzo; hiperczujnosc:bardzo; bezsennosc:bardzo; sen:bardzo; sprzeczne-emocje:bardzo; do-siebie:bardzo; sprawczosc:bardzo; prawda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000270','2026-09-03','strach:bardzo; przetrwanie:bardzo; droga-podroz:bardzo; noc:bardzo; woda:bardzo; ciemnosc:bardzo; czulosc:bardzo; dotyk:bardzo; ku-komus:bardzo; smierc:troche; nadzieja:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000271','2026-09-03','przemiana:bardzo; milosc:bardzo; do-swiata:bardzo; do-innych:bardzo; sprawczosc:bardzo; bunt:troche; komunikacja-problem:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000272','2026-09-03','czas:bardzo; smierc:bardzo; lek-antycypacyjny:troche; ku-przyszlosci:bardzo; sprawczosc:bardzo; cyklicznosc-wzorzec:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000273','2026-09-03','milosc:bardzo; cialo:bardzo; dotyk:bardzo; czulosc:bardzo; oddech-powietrze:bardzo; strach:bardzo; droga-podroz:bardzo; woda:bardzo; ku-komus:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000274','2026-09-03','sen:bardzo; droga-podroz:bardzo; zablokowanie:bardzo; wysokie-pobudzenie:bardzo; lek:bardzo; chaos-balagan:troche; komunikacja-problem:bardzo; sensoryka-metafora:bardzo; noc:bardzo; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000275','2026-09-03','ciemnosc:bardzo; droga-podroz:bardzo; sen:bardzo; marzenie:bardzo; time-blindness:troche; nierozpoznanie-siebie:bardzo; czas:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; milosc:bardzo; cialo:troche; sprawczosc:bardzo; wolnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000276','2026-09-03','rutyna-repetycja:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; do-innych:bardzo; ku-komus:troche; euforia-naped:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000277','2026-09-03','rutyna-repetycja:bardzo; ku-komus:bardzo; do-innych:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000278','2026-09-03','milosc:bardzo; pozadanie:bardzo; dotyk:bardzo; cialo:bardzo; deszcz:bardzo; woda:bardzo; ziemia:bardzo; intensywna-percepcja:bardzo; sensoryka-szukanie:bardzo; znikniecie:bardzo; czas:bardzo; noc:bardzo; wspomnienia:troche; pamiec:troche; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000279','2026-09-03','milosc:bardzo; pozadanie:bardzo; sprzeczne-emocje:bardzo; nie-wiem-co-czuje:troche; maska:bardzo; ukrywanie-reakcji:bardzo; noc:bardzo; ku-komus:bardzo; przemiana:bardzo; od-kogos:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000280','2026-09-03','droga-podroz:bardzo; substancje:troche; maska:bardzo; kontrola-wizerunku:bardzo; prawda:bardzo; marzenie:bardzo; ku-przyszlosci:bardzo; przemiana:bardzo; odrodzenie:troche; sprawczosc:bardzo; do-siebie:bardzo; czas:bardzo; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000281','2026-09-03','milosc:bardzo; marzenie:bardzo; tesknota:bardzo; czulosc:bardzo; dotyk:bardzo; ku-komus:bardzo; samotnosc:bardzo; droga-podroz:bardzo; nadzieja:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000282','2026-09-03','milosc:bardzo; utrata:bardzo; samotnosc:bardzo; smutek:bardzo; ukrywanie-reakcji:bardzo; prawda:bardzo; dom:bardzo; od-kogos:bardzo; zablokowanie:bardzo; wycofanie:bardzo; sprzeczne-potrzeby:bardzo; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000283','2026-09-03','noc:bardzo; taniec:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; droga-podroz:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; dom:troche; nuda-nietolerancja:troche; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000284','2026-09-03','milosc:bardzo; samotnosc:bardzo; sen:troche; dom:bardzo; niedopasowanie-spoleczne:bardzo; tesknota:bardzo; ku-komus:bardzo; droga-podroz:bardzo; nadzieja:bardzo; cialo:troche; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000285','2026-09-03','niepewnosc-nie-do-zniesienia:troche; lek-antycypacyjny:bardzo; przeciazenie-przyszloscia:bardzo; czas:bardzo; smierc:bardzo; deszcz:bardzo; droga-podroz:bardzo; milosc:troche; sprzeczne-potrzeby:troche; ku-przyszlosci:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000286','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; schronienie:bardzo; milosc:bardzo; gniew:troche; radosc:bardzo; smutek:bardzo; sprzeczne-emocje:bardzo; noc:bardzo; wspomnienia:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; nadzieja:bardzo; czulosc:bardzo; euforia-naped:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000287','2026-09-03','sen:bardzo; marzenie:bardzo; noc:bardzo; milosc:bardzo; dotyk:bardzo; czulosc:bardzo; samotnosc:bardzo; smutek:bardzo; tesknota:bardzo; ku-komus:bardzo; ulga:bardzo; nadzieja:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000288','2026-09-03','bunt:bardzo; sprawczosc:bardzo; czas:bardzo; ku-przeszlosci:bardzo; wspomnienia:troche; milosc:bardzo; utrata:troche; nadzieja:troche; marzenie:troche; cyklicznosc-wzorzec:bardzo; euforia-naped:bardzo; impulsywnosc:troche; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000289','2026-09-03','przemiana:bardzo; odrodzenie:bardzo; radosc:bardzo; wolnosc:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; spokoj:bardzo; sen:troche; do-swiata:bardzo; nadzieja:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000290','2026-09-03','cialo:bardzo; wstyd:bardzo; bezsennosc:bardzo; wycofanie:bardzo; niskie-pobudzenie:bardzo; brak-napedu:bardzo; wyczerpanie:bardzo; dosc-przesyt:bardzo; emocja-przez-cialo:bardzo; samotnosc:bardzo; znikniecie:bardzo; woda:bardzo; lek-antycypacyjny:troche; do-siebie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000291','2026-09-03','noc:bardzo; samotnosc:bardzo; niedopasowanie-spoleczne:bardzo; racing-thoughts:bardzo; sensoryka-przytloczenie:bardzo; gniew:bardzo; frustracja:bardzo; cialo:bardzo; ogien:bardzo; wysokie-pobudzenie:bardzo; prawda:bardzo; maska:bardzo; komunikacja-problem:bardzo; smierc:bardzo; droga-podroz:bardzo; przetrwanie:bardzo; potrzeba-zapewnienia:troche; oddech-powietrze:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000292','2026-09-03','przetrwanie:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; noc:bardzo; odrodzenie:bardzo; przemiana:bardzo; nadzieja:bardzo; prawda:bardzo; marzenie:bardzo; czas:bardzo; cialo:bardzo; ku-komus:bardzo; do-swiata:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000293','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; nierozpoznanie-siebie:bardzo; sprzeczne-emocje:bardzo; kontrola:bardzo; do-siebie:bardzo; smierc:bardzo; marzenie:bardzo; wysokie-pobudzenie:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000294','2026-09-03','noc:bardzo; woda:bardzo; oddech-powietrze:bardzo; droga-podroz:bardzo; cialo:bardzo; ogien:bardzo; milosc:bardzo; nadzieja:bardzo; przetrwanie:bardzo; wspomnienia:troche; ku-przeszlosci:bardzo; czulosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000295','2026-09-03','noc:bardzo; samotnosc:bardzo; niedopasowanie-spoleczne:bardzo; milosc:bardzo; tesknota:bardzo; dotyk:bardzo; czulosc:bardzo; potrzeba-zapewnienia:bardzo; droga-podroz:bardzo; ku-komus:bardzo; marzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000296','2026-09-03','wina:bardzo; wstyd:bardzo; smutek:bardzo; do-siebie:bardzo; strach:bardzo; wspomnienia:troche; cyklicznosc-wzorzec:bardzo; bezwartosciowosc:troche; komunikacja-problem:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000297','2026-09-03','wina:bardzo; zal:bardzo; milosc:bardzo; od-kogos:bardzo; droga-podroz:bardzo; cyklicznosc-wzorzec:bardzo; czas:bardzo; nadzieja:bardzo; komunikacja-problem:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000298','2026-09-03','brak-napedu:bardzo; wyczerpanie:bardzo; niskie-pobudzenie:bardzo; cialo:bardzo; dosc-przesyt:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; odrodzenie:bardzo; przemiana:bardzo; ogien:troche; znikniecie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000299','2026-09-03','taniec:bardzo; ogien:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; do-swiata:bardzo; bunt:troche; cialo:bardzo; dom:bardzo; radosc:bardzo; rutyna-repetycja:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000300','2026-09-03','milosc:bardzo; dom:bardzo; przemiana:bardzo; sprzeczne-potrzeby:bardzo; ku-komus:bardzo; dotyk:bardzo; potrzeba-zapewnienia:bardzo; droga-podroz:bardzo; sprawczosc:bardzo; utrata:troche; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000301','2026-09-03','milosc:bardzo; deszcz:bardzo; cialo:bardzo; chaos-balagan:bardzo; droga-podroz:bardzo; dom:bardzo; sen:troche; czas:bardzo; ku-komus:bardzo; czulosc:bardzo; przetrwanie:bardzo; potrzeba-zapewnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000302','2026-09-03','strach:bardzo; ciemnosc:bardzo; bunt:bardzo; sprawczosc:bardzo; do-swiata:bardzo; droga-podroz:troche; przemiana:bardzo; odrodzenie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000303','2026-09-03','milosc:bardzo; zazdrosc:bardzo; pozadanie:bardzo; wina:bardzo; zal:bardzo; utrata:bardzo; cyklicznosc-wzorzec:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; komunikacja-problem:bardzo; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000304','2026-09-03','czas:bardzo; sen:bardzo; marzenie:bardzo; noc:bardzo; samotnosc:bardzo; strach:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; nigdy-dosc:bardzo; czulosc:bardzo; tesknota:bardzo; substancje:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000305','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; cialo:bardzo; wycofanie:bardzo; komunikacja-problem:bardzo; samotnosc:bardzo; droga-podroz:bardzo; niskie-pobudzenie:bardzo; wstyd:troche; zablokowanie:bardzo; ulga-z-zewnatrz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000306','2026-09-03','milosc:bardzo; utrata:bardzo; samotnosc:bardzo; taniec:bardzo; substancje:bardzo; noc:bardzo; komunikacja-problem:bardzo; smutek:bardzo; zablokowanie:bardzo; ku-komus:bardzo; cyklicznosc-wzorzec:bardzo; tesknota:bardzo; niemoznosc-odpuszczenia:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000307','2026-09-03','strach:bardzo; bunt:bardzo; do-swiata:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; schronienie:bardzo; przetrwanie:bardzo; komunikacja-problem:bardzo; woda:troche; odrodzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000308','2026-09-03','milosc:bardzo; noc:bardzo; ziemia:bardzo; smierc:troche; odrodzenie:troche; dotyk:bardzo; czulosc:bardzo; ku-komus:bardzo; wspomnienia:troche; prawda:troche; ukrywanie-reakcji:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000309','2026-09-03','dom:bardzo; milosc:bardzo; czulosc:bardzo; droga-podroz:bardzo; woda:bardzo; wspomnienia:bardzo; pamiec:bardzo; cialo:bardzo; dotyk:bardzo; substancje:troche; radosc:bardzo; ku-komus:bardzo; powrot-do:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000310','2026-09-03','milosc:bardzo; strach:bardzo; cialo:bardzo; kontrola:bardzo; ucieczka:bardzo; potrzeba-zapewnienia:bardzo; substancje:troche; pozadanie:bardzo; wysokie-pobudzenie:bardzo; emocjonalna-dysregulacja:bardzo; ku-komus:bardzo; sprzeczne-emocje:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000311','2026-09-03','milosc:bardzo; pozadanie:bardzo; hiperfokus:bardzo; specjalne-zainteresowanie-osoba:bardzo; bezsennosc-restless:bardzo; sen:bardzo; marzenie:bardzo; cialo:bardzo; ku-komus:bardzo; nigdy-dosc:bardzo; wysokie-pobudzenie:bardzo; cyklicznosc-wzorzec:bardzo; niemoznosc-odpuszczenia:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000312','2026-09-03','milosc:bardzo; strach:bardzo; lek:bardzo; sen:bardzo; dotyk:bardzo; cialo:bardzo; pozadanie:bardzo; potrzeba-zapewnienia:bardzo; ku-komus:bardzo; ciemnosc:troche; cyklicznosc-wzorzec:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000313','2026-09-03','sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; komunikacja-problem:bardzo; niepewnosc-nie-do-zniesienia:troche; innosc:bardzo; rutyna-repetycja:bardzo; hiperfokus:troche; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000314','2026-09-03','znikniecie:bardzo; time-blindness:bardzo; wyczerpanie:bardzo; emocjonalna-dysregulacja:bardzo; shutdown-meltdown:bardzo; ulga-z-zewnatrz:bardzo; schronienie:bardzo; dom:bardzo; bezsilnosc:bardzo; pogon:troche; pamiec:bardzo; czas:bardzo; spokoj:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000315','2026-09-03','sensoryka-przytloczenie:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; hiperfokus:bardzo; sen:troche; spokoj:bardzo; ulga:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000316','2026-09-03','woda:bardzo; droga-podroz:bardzo; ogien:bardzo; oddech-powietrze:bardzo; czas:bardzo; ku-komus:troche; sprawczosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000317','2026-09-03','pustka-emocjonalna:bardzo; samotnosc:bardzo; znikniecie:bardzo; wolnosc:bardzo; brak-nadziei:bardzo; smierc-wlasna:bardzo; smierc:bardzo; smutek:bardzo; bezsilnosc:bardzo; cialo:bardzo; wycofanie:bardzo; sensoryka-metafora:bardzo; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000318','2026-09-03','milosc:bardzo; czulosc:bardzo; komunikacja-problem:bardzo; ku-komus:bardzo; rutyna-repetycja:bardzo; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000319','2026-09-03','milosc:bardzo; pozadanie:bardzo; cialo:bardzo; ogien:bardzo; noc:bardzo; smutek:bardzo; wyczerpanie:bardzo; ulga-z-zewnatrz:bardzo; potrzeba-zapewnienia:bardzo; bezsilnosc:bardzo; ku-komus:bardzo; niemoznosc-odpuszczenia:bardzo; smierc:troche; wysokie-pobudzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000320','2026-09-03','milosc:bardzo; hiperfokus:bardzo; specjalne-zainteresowanie-osoba:bardzo; substancje:troche; zobojetnienie:bardzo; woda:bardzo; czas:bardzo; wspomnienia:troche; ku-przeszlosci:troche; droga-podroz:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000321','2026-09-03','milosc:bardzo; utrata:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; woda:bardzo; droga-podroz:bardzo; dotyk:bardzo; czulosc:bardzo; tesknota:bardzo; ku-komus:bardzo; czas:bardzo; samotnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000322','2026-09-03','milosc:bardzo; dom:bardzo; czas:bardzo; wspomnienia:bardzo; pamiec:troche; prawda:bardzo; cialo:bardzo; samokontrola-spoleczna:troche; nadzieja:bardzo; ku-przyszlosci:bardzo; ku-komus:bardzo; czulosc:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000323','2026-09-03','ucieczka:bardzo; droga-podroz:bardzo; wolnosc:bardzo; przetrwanie:bardzo; smierc:bardzo; dom:bardzo; noc:bardzo; woda:bardzo; strach:bardzo; ku-przyszlosci:bardzo; milosc:bardzo; sprawczosc:bardzo; bunt:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000324','2026-09-03','milosc:bardzo; cialo:bardzo; dotyk:bardzo; pozadanie:bardzo; smierc:bardzo; ziemia:bardzo; dom:bardzo; substancje:bardzo; wina:troche; sen:bardzo; wolnosc:bardzo; czulosc:bardzo; powrot-do:bardzo; ogien:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000325','2026-09-03','milosc:bardzo; prawda:bardzo; smutek:bardzo; zobojetnienie:troche; potrzeba-zapewnienia:bardzo; dom:bardzo; ucieczka:bardzo; droga-podroz:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; niemoznosc-odpuszczenia:bardzo; ku-komus:bardzo; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000326','2026-09-03','milosc:bardzo; droga-podroz:bardzo; wspomnienia:bardzo; pamiec:bardzo; samotnosc:bardzo; woda:bardzo; sen:bardzo; marzenie:bardzo; wolnosc:bardzo; strach:bardzo; ciemnosc:bardzo; zablokowanie:bardzo; pogon:bardzo; znikniecie:bardzo; do-siebie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000327','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; sen:bardzo; droga-podroz:bardzo; dom:bardzo; innosc:bardzo; niedopasowanie-spoleczne:troche; tesknota:bardzo; cialo:bardzo; sensoryka-przytloczenie:bardzo; schronienie:bardzo; odrodzenie:bardzo; przemiana:bardzo; czas:bardzo; noc:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000328','2026-09-03','wyczerpanie:bardzo; droga-podroz:bardzo; woda:bardzo; wspomnienia:bardzo; pamiec:bardzo; sensoryka-przytloczenie:bardzo; schronienie:bardzo; smierc:bardzo; sen:bardzo; radosc:troche; smutek:troche; cyklicznosc-wzorzec:bardzo; spokoj:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000329','2026-09-03','sprawczosc:bardzo; wolnosc:bardzo; woda:bardzo; droga-podroz:bardzo; ucieczka:bardzo; prawda:bardzo; samotnosc-preferowana:bardzo; deszcz:bardzo; strach:troche; utrata:bardzo; od-kogos:bardzo; duma:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000330','2026-09-03','innosc:bardzo; niedopasowanie-spoleczne:bardzo; bezwartosciowosc:bardzo; wstyd:bardzo; cialo:bardzo; kontrola:bardzo; potrzeba-zapewnienia:bardzo; pozadanie:bardzo; samotnosc:bardzo; ucieczka:bardzo; ku-komus:bardzo; do-siebie:bardzo; znikniecie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000331','2026-09-03','pozadanie:bardzo; cialo:bardzo; ogien:bardzo; noc:bardzo; ciemnosc:bardzo; hiperczujnosc:bardzo; strach:troche; wysokie-pobudzenie:bardzo; droga-podroz:troche; smierc:troche; ku-komus:bardzo; sensoryka-szukanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000332','2026-09-03','milosc:bardzo; ulga-z-zewnatrz:bardzo; potrzeba-zapewnienia:bardzo; wyczerpanie:bardzo; bezsilnosc:bardzo; utrata:bardzo; czas:bardzo; brak-nadziei:troche; przetrwanie:bardzo; nadzieja:bardzo; ku-komus:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000333','2026-09-03','cialo:bardzo; smutek:bardzo; strach:bardzo; brak-nadziei:bardzo; do-swiata:bardzo; marzenie:bardzo; ku-przyszlosci:bardzo; cyklicznosc-wzorzec:bardzo; zablokowanie:bardzo; przetrwanie:troche; sensoryka-metafora:bardzo; latanie-spadanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000334','2026-09-03','maskowanie:bardzo; ukrywanie-reakcji:bardzo; wstyd:bardzo; performowanie-roli:bardzo; dopasowanie-roli:bardzo; ja-publiczne-ja-prywatne:bardzo; nierozpoznanie-siebie:bardzo; prawda:bardzo; milosc:bardzo; komunikacja-problem:bardzo; do-siebie:bardzo; przemiana:bardzo; odrodzenie:troche; czas:bardzo; samotnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000335','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; noc:bardzo; substancje:troche; utrata:bardzo; melancholia:bardzo; smutek:bardzo; droga-podroz:bardzo; czas:bardzo; milosc:bardzo; znikniecie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000336','2026-09-03','komunikacja-problem:bardzo; ukrywanie-reakcji:bardzo; cialo:bardzo; sprzeczne-potrzeby:bardzo; strach:troche; sprawczosc:bardzo; wina:bardzo; sensoryka-metafora:bardzo; samokontrola-spoleczna:bardzo; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000337','2026-09-03','droga-podroz:bardzo; utrata:bardzo; noc:bardzo; substancje:troche; wspomnienia:bardzo; pamiec:bardzo; marzenie:bardzo; brak-nadziei:bardzo; samotnosc:bardzo; powrot-do:bardzo; ku-przeszlosci:bardzo; czas:bardzo; milosc:bardzo; znikniecie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000338','2026-09-03','wolnosc:bardzo; bunt:bardzo; radosc:bardzo; dom:bardzo; noc:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; do-swiata:bardzo; sprawczosc:bardzo; cyklicznosc-wzorzec:bardzo; ukrywanie-reakcji:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000339','2026-09-03','sen:bardzo; marzenie:bardzo; droga-podroz:bardzo; woda:bardzo; do-swiata:bardzo; kontrola:troche; sprawczosc:bardzo; rutyna-repetycja:bardzo; pogon:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000340','2026-09-03','milosc:bardzo; ucieczka:bardzo; droga-podroz:bardzo; bezsennosc:bardzo; noc:bardzo; smutek:bardzo; utrata:bardzo; dotyk:bardzo; sprzeczne-potrzeby:bardzo; od-kogos:bardzo; cialo:bardzo; zal:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000341','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; przemiana:bardzo; nierozpoznanie-siebie:bardzo; ukrywanie-reakcji:bardzo; samotnosc:bardzo; tesknota:bardzo; czas:bardzo; znikniecie:bardzo; do-siebie:bardzo; wyczerpanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000342','2026-09-03','czas:bardzo; radosc:troche; smutek:troche; strach:bardzo; smierc:bardzo; cialo:bardzo; wspomnienia:bardzo; pamiec:bardzo; sprawczosc:bardzo; cyklicznosc-wzorzec:bardzo; nadzieja:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000343','2026-09-03','milosc:bardzo; czulosc:bardzo; schronienie:bardzo; ulga-z-zewnatrz:bardzo; oddech-powietrze:bardzo; ukrywanie-reakcji:bardzo; dom:bardzo; do-swiata:bardzo; ku-komus:bardzo; spokoj:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000344','2026-09-03','noc:bardzo; deszcz:bardzo; substancje:troche; pozadanie:troche; sensoryka-przytloczenie:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; do-swiata:bardzo; rutyna-repetycja:bardzo; melancholia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000346','2026-09-03','do-swiata:bardzo; bunt:troche; gniew:bardzo; kontrola:bardzo; wina:troche; sprawczosc:bardzo; komunikacja-problem:bardzo; cyklicznosc-wzorzec:bardzo; wysokie-pobudzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000347','2026-09-03','droga-podroz:bardzo; czas:bardzo; wstyd:bardzo; noc:bardzo; zamartwianie:bardzo; do-swiata:bardzo; przemiana:bardzo; sprawczosc:troche; chaos-balagan:troche; cialo:troche; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000348','2026-09-03','smierc:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; marzenie:bardzo; utrata:bardzo; zal:bardzo; smutek:bardzo; cialo:troche; dom:bardzo; przetrwanie:bardzo; bezsilnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000349','2026-09-03','ucieczka:bardzo; droga-podroz:bardzo; przemiana:bardzo; odrodzenie:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; deszcz:bardzo; strach:bardzo; pogon:bardzo; brak-nadziei:bardzo; marzenie:bardzo; spokoj:bardzo; czas:bardzo; nierozpoznanie-siebie:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000350','2026-09-03','prawda:bardzo; bunt:bardzo; wolnosc:bardzo; do-swiata:bardzo; substancje:troche; wstyd:bardzo; sprawczosc:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; gniew:bardzo; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000351','2026-09-03','droga-podroz:bardzo; woda:bardzo; milosc:bardzo; cialo:bardzo; czas:bardzo; time-blindness:bardzo; marzenie:bardzo; noc:bardzo; sensoryka-metafora:bardzo; do-swiata:bardzo; sprawczosc:troche; znikniecie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000352','2026-09-03','strach:bardzo; czas:bardzo; smierc:bardzo; milosc:bardzo; utrata:bardzo; wspomnienia:bardzo; pamiec:bardzo; dotyk:bardzo; nadzieja:bardzo; deszcz:bardzo; cyklicznosc-wzorzec:bardzo; ku-przyszlosci:bardzo; znikniecie:bardzo; smutek:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000353','2026-09-03','milosc:bardzo; prawda:bardzo; ogien:bardzo; cialo:bardzo; strach:bardzo; wysokie-pobudzenie:bardzo; komunikacja-problem:bardzo; potrzeba-zapewnienia:bardzo; sprzeczne-potrzeby:bardzo; utrata:bardzo; zablokowanie:bardzo; ku-komus:bardzo; dosc-przesyt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000354','2026-09-03','substancje:bardzo; substancja-regulacja:troche; noc:bardzo; droga-podroz:bardzo; dom:bardzo; rutyna-repetycja:bardzo; impulsywnosc:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; deszcz:bardzo; chaos-balagan:bardzo; nuda-nietolerancja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000355','2026-09-03','droga-podroz:bardzo; woda:bardzo; oddech-powietrze:bardzo; marzenie:bardzo; nadzieja:bardzo; sprawczosc:bardzo; bezsilnosc:bardzo; sprzeczne-potrzeby:bardzo; sensoryka-metafora:bardzo; zablokowanie:troche; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000356','2026-09-03','wspomnienia:troche; smutek:bardzo; zal:bardzo; cialo:troche; strach:bardzo; ucieczka:bardzo; zablokowanie:bardzo; bezsilnosc:bardzo; do-swiata:bardzo; performowanie-roli:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000357','2026-09-03','ukrywanie-reakcji:bardzo; komunikacja-problem:bardzo; maska:bardzo; strach:bardzo; niedopasowanie-spoleczne:bardzo; samotnosc:bardzo; smierc:bardzo; wspomnienia:troche; do-swiata:bardzo; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000358','2026-09-03','komunikacja-problem:bardzo; ukrywanie-reakcji:bardzo; zal:bardzo; smutek:bardzo; zablokowanie:bardzo; czas:bardzo; sprzeczne-emocje:troche; wycofanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000359','2026-09-03','radosc:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; deszcz:bardzo; wspomnienia:bardzo; do-swiata:bardzo; nadzieja:bardzo; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000360','2026-09-03','innosc:bardzo; wolnosc:bardzo; noc:bardzo; droga-podroz:bardzo; znikniecie:bardzo; nigdy-dosc:bardzo; sprawczosc:bardzo; ku-przyszlosci:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000361','2026-09-03','do-swiata:bardzo; gniew:bardzo; smierc:bardzo; czas:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; ku-przyszlosci:bardzo; strach:bardzo; prawda:bardzo; odrodzenie:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000362','2026-09-03','cialo:bardzo; smierc:bardzo; wspomnienia:bardzo; pamiec:bardzo; noc:bardzo; ciemnosc:bardzo; prawda:bardzo; ukrywanie-reakcji:bardzo; wina:bardzo; zal:bardzo; sprzeczne-emocje:bardzo; przetrwanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000363','2026-09-03','milosc:bardzo; deszcz:bardzo; radosc:bardzo; smutek:bardzo; sprzeczne-emocje:bardzo; cyklicznosc-wzorzec:bardzo; dom:bardzo; emocjonalna-dysregulacja:troche; ku-komus:bardzo; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000364','2026-09-03','samotnosc:bardzo; strach:bardzo; lek:bardzo; ciemnosc:bardzo; wspomnienia:bardzo; pamiec:bardzo; komunikacja-problem:bardzo; wycofanie:bardzo; cialo:troche; sensoryka-przytloczenie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000365','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; pozadanie:troche; milosc:bardzo; utrata:bardzo; smutek:bardzo; taniec:bardzo; noc:bardzo; euforia-naped:bardzo; cyklicznosc-wzorzec:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000366','2026-09-03','wyczerpanie:bardzo; droga-podroz:bardzo; smierc:bardzo; strach:bardzo; czas:bardzo; zal:bardzo; wolnosc:bardzo; sprawczosc:bardzo; zamartwianie:bardzo; nierozpoznanie-siebie:bardzo; nadzieja:bardzo; marzenie:troche; przetrwanie:bardzo; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000367','2026-09-03','milosc:bardzo; utrata:bardzo; czas:bardzo; wspomnienia:bardzo; pamiec:troche; komunikacja-problem:bardzo; smutek:bardzo; gniew:troche; od-kogos:bardzo; znikniecie:bardzo; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000368','2026-09-03','brak-nadziei:bardzo; ciemnosc:bardzo; noc:bardzo; bezsennosc-restless:bardzo; droga-podroz:bardzo; samotnosc:bardzo; sensoryka-przytloczenie:bardzo; wspomnienia:bardzo; pamiec:bardzo; dotyk:troche; tesknota:bardzo; wycofanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000369','2026-09-03','milosc:bardzo; woda:bardzo; taniec:bardzo; tesknota:bardzo; potrzeba-zapewnienia:bardzo; komunikacja-problem:bardzo; utrata:bardzo; ku-komus:bardzo; samotnosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000370','2026-09-03','milosc:bardzo; pozadanie:bardzo; cialo:bardzo; smutek:bardzo; samotnosc:bardzo; performowanie-roli:bardzo; nierozpoznanie-siebie:bardzo; komunikacja-problem:bardzo; ku-komus:bardzo; wstyd:troche; sprzeczne-emocje:bardzo; emocja-przez-cialo:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000371','2026-09-03','hiperfokus:bardzo; specjalne-zainteresowanie-osoba:bardzo; niemoznosc-odpuszczenia:bardzo; potrzeba-zapewnienia:bardzo; milosc:bardzo; samotnosc:bardzo; komunikacja-problem:bardzo; zablokowanie:bardzo; wina:troche; sprawczosc:bardzo; wycofanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000372','2026-09-03','innosc:bardzo; milosc:bardzo; oddech-powietrze:bardzo; znikniecie:bardzo; smierc:bardzo; sen:bardzo; marzenie:bardzo; latanie-spadanie:bardzo; taniec:bardzo; cialo:bardzo; ku-komus:bardzo; potrzeba-zapewnienia:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000373','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; maskowanie:bardzo; ukrywanie-reakcji:bardzo; ucieczka:bardzo; niedopasowanie-spoleczne:bardzo; bezwartosciowosc:bardzo; do-siebie:bardzo; prawda:bardzo; zablokowanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000374','2026-09-03','milosc:bardzo; smierc:bardzo; czas:bardzo; utrata:bardzo; wspomnienia:bardzo; zal:bardzo; sprawczosc:bardzo; ku-komus:bardzo; cialo:troche; czulosc:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000375','2026-09-03','strach:bardzo; lek-antycypacyjny:bardzo; smierc:bardzo; czas:bardzo; rozpad:bardzo; znikniecie:bardzo; do-swiata:bardzo; latanie-spadanie:bardzo; sensoryka-metafora:bardzo; przeciazenie-przyszloscia:bardzo; bezsilnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000376','2026-09-03','dom:bardzo; utrata:bardzo; deszcz:bardzo; woda:bardzo; wspomnienia:bardzo; pamiec:bardzo; czas:bardzo; time-blindness:bardzo; znikniecie:bardzo; smutek:bardzo; droga-podroz:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000377','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; milosc:bardzo; utrata:bardzo; ucieczka:bardzo; noc:bardzo; komunikacja-problem:bardzo; nadzieja:bardzo; ulga-z-zewnatrz:bardzo; ku-komus:bardzo; sprawczosc:bardzo; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000378','2026-09-03','utrata:bardzo; smutek:bardzo; deszcz:bardzo; droga-podroz:bardzo; cialo:bardzo; woda:bardzo; substancje:bardzo; substancja-regulacja:troche; ucieczka:bardzo; do-swiata:bardzo; bezsilnosc:troche; sensoryka-przytloczenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000379','2026-09-03','milosc:bardzo; samotnosc:bardzo; marzenie:bardzo; sen:bardzo; schronienie:bardzo; droga-podroz:bardzo; ucieczka:bardzo; zablokowanie:bardzo; czas:bardzo; wspomnienia:troche; pamiec:troche; ku-komus:bardzo; niemoznosc-odpuszczenia:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000380','2026-09-03','do-swiata:bardzo; strach:bardzo; sen:bardzo; latanie-spadanie:bardzo; smierc:bardzo; wysokie-pobudzenie:bardzo; brak-nadziei:bardzo; lek-antycypacyjny:bardzo; ku-przyszlosci:bardzo; sensoryka-przytloczenie:bardzo; sensoryka-metafora:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000381','2026-09-03','droga-podroz:bardzo; dom:bardzo; spokoj:bardzo; czas:bardzo; ku-przyszlosci:bardzo; sprawczosc:bardzo; nadzieja:bardzo; odrodzenie:bardzo; przemiana:bardzo; marzenie:bardzo; wolnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000382','2026-09-03','droga-podroz:bardzo; oddech-powietrze:bardzo; znikniecie:bardzo; dotyk:bardzo; cialo:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; ku-przyszlosci:bardzo; czas:bardzo; woda:bardzo; utrata:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000383','2026-09-03','milosc:bardzo; woda:bardzo; cialo:bardzo; dotyk:bardzo; pozadanie:bardzo; sensoryka-szukanie:bardzo; ku-komus:bardzo; nigdy-dosc:troche; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000384','2026-09-03','marzenie:bardzo; droga-podroz:bardzo; schronienie:bardzo; ucieczka:troche; ukrywanie-reakcji:troche; ku-przyszlosci:bardzo; czas:bardzo; wycofanie:troche; spokoj:bardzo; sensoryka-metafora:bardzo; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000385','2026-09-03','niepewnosc-nie-do-zniesienia:troche; lek-antycypacyjny:bardzo; przeciazenie-przyszloscia:bardzo; czas:bardzo; smierc:bardzo; deszcz:bardzo; droga-podroz:bardzo; milosc:troche; sprzeczne-potrzeby:troche; ku-przyszlosci:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000386','2026-09-03','milosc:bardzo; taniec:bardzo; schronienie:bardzo; strach:bardzo; ukrywanie-reakcji:troche; dom:bardzo; noc:bardzo; wyczerpanie:troche; czulosc:bardzo; do-swiata:bardzo; sprawczosc:bardzo; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000387','2026-09-03','milosc:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; tesknota:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; potrzeba-zapewnienia:bardzo; pozadanie:bardzo; sen:bardzo; ku-komus:bardzo; niemoznosc-odpuszczenia:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000388','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; czas:bardzo; ku-przyszlosci:bardzo; niepewnosc-nie-do-zniesienia:troche; zamartwianie:bardzo; wolnosc:bardzo; spokoj:bardzo; milosc:bardzo; przemiana:bardzo; odrodzenie:troche; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000389','2026-09-03','czas:bardzo; samotnosc:bardzo; cialo:bardzo; noc:bardzo; dom:bardzo; bezsennosc:bardzo; zablokowanie:bardzo; nic-pustka:bardzo; niskie-pobudzenie:troche; wyczerpanie:bardzo; do-siebie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000390','2026-09-03','taniec:bardzo; ogien:bardzo; ziemia:bardzo; cialo:bardzo; smierc:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; brak-nadziei:bardzo; do-swiata:bardzo; rutyna-repetycja:bardzo; sensoryka-szukanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000391','2026-09-03','racing-thoughts:bardzo; dysfunkcja-wykonawcza:bardzo; przeciazenie-przyszloscia:bardzo; sen:bardzo; sensoryka-przytloczenie:troche; do-swiata:bardzo; gniew:bardzo; bezsilnosc:bardzo; cyklicznosc-wzorzec:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000392','2026-09-03','sprzeczne-emocje:bardzo; latanie-spadanie:bardzo; sen:bardzo; pamiec:bardzo; oddech-powietrze:bardzo; emocja-przez-cialo:bardzo; cialo:bardzo; strach:bardzo; do-siebie:bardzo; wiem-co-czuje:troche; intensywna-percepcja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000393','2026-09-03','niepewnosc-nie-do-zniesienia:bardzo; potrzeba-zapewnienia:bardzo; samotnosc:bardzo; cyklicznosc-wzorzec:bardzo; strach:bardzo; ucieczka:bardzo; komunikacja-problem:bardzo; sprzeczne-potrzeby:bardzo; samokontrola-spoleczna:troche; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000394','2026-09-03','dom:bardzo; droga-podroz:bardzo; wolnosc:bardzo; cialo:bardzo; utrata:bardzo; noc:bardzo; innosc:bardzo; samotnosc-preferowana:bardzo; przetrwanie:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000395','2026-09-03','do-swiata:bardzo; nic-pustka:bardzo; cyklicznosc-wzorzec:bardzo; brak-napedu:bardzo; przemiana:bardzo; odrodzenie:bardzo; milosc:bardzo; czas:bardzo; droga-podroz:bardzo; woda:bardzo; sprawczosc:bardzo; zobojetnienie:troche; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000396','2026-09-03','dom:bardzo; powrot-do:bardzo; droga-podroz:bardzo; samotnosc:bardzo; milosc:bardzo; wolnosc:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; sprawczosc:bardzo; komunikacja-problem:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000397','2026-09-03','przemiana:bardzo; odrodzenie:bardzo; wolnosc:bardzo; droga-podroz:bardzo; noc:bardzo; ciemnosc:bardzo; ku-przeszlosci:bardzo; ku-przyszlosci:bardzo; sprawczosc:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; duma:bardzo; bunt:bardzo; wysokie-pobudzenie:bardzo; prawda:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000398','2026-09-03','do-swiata:bardzo; bunt:bardzo; strach:bardzo; sprawczosc:bardzo; nadzieja:bardzo; marzenie:bardzo; ku-przyszlosci:bardzo; przetrwanie:bardzo; wysokie-pobudzenie:bardzo; duma:bardzo; komunikacja-problem:troche; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000399','2026-09-03','dosc-przesyt:bardzo; sensoryka-przytloczenie:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; przemiana:bardzo; dotyk:bardzo; cialo:bardzo; milosc:bardzo; czas:bardzo; wspomnienia:bardzo; pamiec:troche; komunikacja-problem:bardzo; chaos-balagan:troche; sprawczosc:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000400','2026-09-03','marzenie:bardzo; prawda:bardzo; maska:troche; noc:bardzo; dom:bardzo; wspomnienia:bardzo; pamiec:bardzo; deszcz:bardzo; woda:bardzo; ziemia:bardzo; milosc:bardzo; do-swiata:bardzo; niepewnosc-nie-do-zniesienia:troche; sensoryka-metafora:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000401','2026-09-03','droga-podroz:bardzo; ku-komus:bardzo; sprawczosc:bardzo; komunikacja-problem:bardzo; marzenie:troche; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000402','2026-09-03','czas:bardzo; woda:bardzo; radosc:bardzo; do-swiata:bardzo; sprawczosc:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000403','2026-09-03','noc:bardzo; komunikacja-problem:bardzo; zal:troche; droga-podroz:troche; do-innych:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000404','2026-09-03','droga-podroz:bardzo; przetrwanie:bardzo; samotnosc:bardzo; milosc:bardzo; utrata:bardzo; nierozpoznanie-siebie:bardzo; niepewnosc-nie-do-zniesienia:troche; sensoryka-metafora:bardzo; ku-komus:bardzo; zablokowanie:bardzo; smutek:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000405','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ukrywanie-reakcji:bardzo; maskowanie:bardzo; ciemnosc:bardzo; znikniecie:bardzo; wycofanie:bardzo; komunikacja-problem:bardzo; do-swiata:bardzo; nierozpoznanie-siebie:bardzo; zablokowanie:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000406','2026-09-03','smierc:bardzo; strach:bardzo; wina:bardzo; prawda:troche; komunikacja-problem:bardzo; wyczerpanie:bardzo; sen:bardzo; shutdown-meltdown:troche; ukrywanie-reakcji:bardzo; performowanie-roli:bardzo; nierozpoznanie-siebie:troche; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000407','2026-09-03','bezsennosc-restless:bardzo; time-blindness:bardzo; dom:bardzo; wspomnienia:bardzo; pamiec:bardzo; cialo:bardzo; sen:bardzo; strach:bardzo; sensoryka-przytloczenie:bardzo; utrata:bardzo; zablokowanie:bardzo; dotyk:bardzo; nierozpoznanie-siebie:bardzo; powrot-do:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000251','2026-09-03','smutek:bardzo; przemiana:bardzo; odrodzenie:bardzo; gniew:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; sensoryka-metafora:bardzo; sprawczosc:bardzo; do-swiata:bardzo; nadzieja:bardzo; deszcz:bardzo; ogien:bardzo; cialo:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000408','2026-09-03','milosc:bardzo; utrata:bardzo; woda:bardzo; wolnosc:bardzo; smierc:bardzo; smutek:bardzo; radosc:troche; noc:bardzo; ciemnosc:bardzo; znikniecie:bardzo; ku-komus:bardzo; dotyk:troche; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000409','2026-09-03','lek:bardzo; nierozpoznanie-siebie:bardzo; sensoryka-przytloczenie:bardzo; wspomnienia:bardzo; ziemia:bardzo; milosc:bardzo; ulga-z-zewnatrz:bardzo; schronienie:bardzo; ciemnosc:bardzo; przemiana:bardzo; odrodzenie:bardzo; nadzieja:bardzo; do-swiata:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000410','2026-09-03','milosc:bardzo; pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; taniec:bardzo; ogien:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; nigdy-dosc:bardzo; ku-komus:bardzo; czulosc:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000411','2026-09-03','komunikacja-problem:bardzo; milosc:bardzo; dotyk:bardzo; cialo:bardzo; smutek:bardzo; sprzeczne-emocje:bardzo; intensywna-percepcja:bardzo; ku-komus:bardzo; ukrywanie-reakcji:troche; pamiec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000412','2026-09-03','droga-podroz:bardzo; noc:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; wolnosc:bardzo; do-swiata:bardzo; ku-komus:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000413','2026-09-03','zazdrosc:bardzo; sen:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; emocjonalna-dysregulacja:bardzo; wina:bardzo; zal:bardzo; niepewnosc-nie-do-zniesienia:bardzo; potrzeba-zapewnienia:bardzo; cialo:bardzo; ukrywanie-reakcji:bardzo; milosc:bardzo; smutek:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000414','2026-09-03','pozadanie:bardzo; ogien:bardzo; cialo:bardzo; oddech-powietrze:bardzo; noc:bardzo; nigdy-dosc:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; znikniecie:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000415','2026-09-03','milosc:bardzo; prawda:bardzo; wstyd:bardzo; maska:bardzo; kontrola-wizerunku:bardzo; kontrola:bardzo; cialo:bardzo; ogien:troche; czas:bardzo; cyklicznosc-wzorzec:troche; sprzeczne-emocje:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000416','2026-09-03','milosc:bardzo; nigdy-dosc:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:bardzo; maska:bardzo; potrzeba-zapewnienia:bardzo; ku-komus:bardzo; wstyd:troche; cyklicznosc-wzorzec:bardzo; niemoznosc-odpuszczenia:bardzo; sprzeczne-potrzeby:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000417','2026-09-03','deszcz:bardzo; sensoryka-metafora:bardzo; komunikacja-problem:bardzo; substancje:troche; substancja-regulacja:troche; melancholia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000419','2026-09-03','taniec:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; schronienie:bardzo; dom:troche; ogien:bardzo; cialo:bardzo; ku-komus:bardzo; czas:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000420','2026-09-03','nierozpoznanie-siebie:bardzo; sprzeczne-potrzeby:bardzo; zablokowanie:bardzo; bezsilnosc:bardzo; wolnosc:bardzo; sprawczosc:troche; czas:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000421','2026-09-03','performowanie-roli:bardzo; kontrola-wizerunku:bardzo; pozadanie:bardzo; substancje:troche; do-innych:bardzo; duma:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000422','2026-09-03','pogon:bardzo; gniew:bardzo; strach:bardzo; latanie-spadanie:bardzo; ogien:bardzo; cialo:bardzo; wysokie-pobudzenie:bardzo; sprawczosc:bardzo; ku-komus:bardzo; pozadanie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000424','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:troche; woda:bardzo; cialo:bardzo; latanie-spadanie:bardzo; wina:bardzo; milosc:troche; czulosc:troche; sensoryka-metafora:bardzo; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000425','2026-09-03','czas:bardzo; zal:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; smierc:bardzo; ogien:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo; smutek:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000426','2026-09-03','schronienie:bardzo; strach:troche; nadzieja:bardzo; przetrwanie:bardzo; przemiana:bardzo; woda:bardzo; ziemia:bardzo; sensoryka-metafora:bardzo; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000427','2026-09-03','czas:bardzo; wyczerpanie:bardzo; brak-nadziei:bardzo; bezsilnosc:bardzo; przetrwanie:bardzo; nadzieja:troche; noc:bardzo; do-swiata:bardzo; sensoryka-metafora:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000428','2026-09-03','pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; ogien:bardzo; sen:bardzo; smutek:bardzo; sprzeczne-emocje:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000431','2026-09-03','pozadanie:bardzo; cialo:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:bardzo; do-innych:bardzo; sprawczosc:bardzo; duma:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000432','2026-09-03','droga-podroz:bardzo; woda:bardzo; cialo:bardzo; wyczerpanie:bardzo; substancje:bardzo; sensoryka-przytloczenie:bardzo; intensywna-percepcja:bardzo; bezsilnosc:bardzo; przetrwanie:bardzo; czas:bardzo; zablokowanie:bardzo; wina:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000434','2026-09-03','milosc:bardzo; marzenie:bardzo; droga-podroz:bardzo; woda:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; radosc:bardzo; ku-komus:bardzo; sprawczosc:bardzo; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000435','2026-09-03','wspomnienia:bardzo; sprzeczne-potrzeby:bardzo; do-siebie:bardzo; sprawczosc:bardzo; przemiana:bardzo; czas:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000436','2026-09-03','droga-podroz:bardzo; noc:bardzo; smierc:bardzo; ziemia:bardzo; odrodzenie:bardzo; przemiana:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; dom:bardzo; schronienie:bardzo; taniec:bardzo; wspomnienia:bardzo; czas:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000437','2026-09-03','dom:bardzo; powrot-do:bardzo; droga-podroz:bardzo; innosc:bardzo; duma:bardzo; prawda:bardzo; do-siebie:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000438','2026-09-03','milosc:bardzo; czulosc:bardzo; ku-komus:bardzo; woda:bardzo; oddech-powietrze:bardzo; powrot-do:bardzo; droga-podroz:bardzo; dom:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000439','2026-09-03','milosc:bardzo; cialo:bardzo; taniec:bardzo; dotyk:bardzo; pozadanie:bardzo; ogien:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; sensoryka-szukanie:bardzo; ku-komus:bardzo; radosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000440','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; melancholia:bardzo; pozadanie:troche; cialo:troche; substancje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000441','2026-09-03','czas:bardzo; smierc:bardzo; droga-podroz:bardzo; wspomnienia:bardzo; pamiec:bardzo; zal:troche; milosc:bardzo; smutek:bardzo; radosc:bardzo; duma:bardzo; do-siebie:bardzo; sprawczosc:bardzo; prawda:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000442','2026-09-03','do-swiata:bardzo; nigdy-dosc:bardzo; marzenie:bardzo; sprawczosc:bardzo; gniew:troche; duma:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000443','2026-09-03','droga-podroz:bardzo; substancje:bardzo; substancja-regulacja:bardzo; utrata:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; tesknota:bardzo; ucieczka:bardzo; od-kogos:bardzo; woda:bardzo; czas:bardzo; sprawczosc:bardzo; smutek:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000444','2026-09-03','woda:bardzo; cialo:bardzo; dotyk:bardzo; milosc:bardzo; ku-komus:bardzo; pamiec:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000445','2026-09-03','woda:bardzo; droga-podroz:bardzo; sprawczosc:bardzo; od-kogos:bardzo; wolnosc:bardzo; do-swiata:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000446','2026-09-03','sprawczosc:bardzo; kontrola:bardzo; do-innych:bardzo; gniew:bardzo; wysokie-pobudzenie:bardzo; pogon:bardzo; smierc:bardzo; strach:bardzo; bunt:bardzo; duma:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000447','2026-09-03','lek:bardzo; lek-antycypacyjny:bardzo; maska:bardzo; ukrywanie-reakcji:bardzo; samotnosc:bardzo; czulosc:bardzo; dotyk:bardzo; ku-komus:bardzo; deszcz:bardzo; droga-podroz:bardzo; odrodzenie:bardzo; nadzieja:bardzo; przetrwanie:bardzo; sensoryka-metafora:bardzo; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000448','2026-09-03','komunikacja-problem:bardzo; prawda:bardzo; milosc:troche; ku-komus:bardzo; sprawczosc:bardzo; bunt:troche; kontrola-wizerunku:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000449','2026-09-03','sensoryka-przytloczenie:bardzo; wysokie-pobudzenie:bardzo; komunikacja-problem:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; milosc:bardzo; dotyk:bardzo; ku-komus:bardzo; sprzeczne-potrzeby:bardzo; zablokowanie:bardzo; nadzieja:bardzo; bunt:bardzo; duma:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000450','2026-09-03','droga-podroz:bardzo; marzenie:bardzo; wolnosc:bardzo; bunt:bardzo; sprawczosc:bardzo; latanie-spadanie:bardzo; czas:bardzo; pozadanie:troche; wysokie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000451','2026-09-03','taniec:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; substancje:bardzo; smutek:bardzo; zal:bardzo; wolnosc:bardzo; przemiana:bardzo; odrodzenie:troche; czas:bardzo; sensoryka-szukanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000452','2026-09-03','zablokowanie:bardzo; rutyna-repetycja:bardzo; ku-komus:bardzo; dotyk:bardzo; czulosc:bardzo; czas:bardzo; substancje:troche; sensoryka-przytloczenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000453','2026-09-03','marzenie:bardzo; droga-podroz:bardzo; woda:bardzo; ku-przyszlosci:bardzo; substancje:bardzo; pozadanie:troche; radosc:bardzo; sensoryka-szukanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000454','2026-09-03','pozadanie:bardzo; milosc:bardzo; ku-komus:bardzo; nigdy-dosc:bardzo; rutyna-repetycja:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; cyklicznosc-wzorzec:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000455','2026-09-03','dom:bardzo; schronienie:bardzo; droga-podroz:bardzo; marzenie:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; ziemia:bardzo; wolnosc:bardzo; spokoj:bardzo; sprawczosc:bardzo; czulosc:bardzo; radosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000457','2026-09-03','milosc:bardzo; pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; woda:bardzo; sprzeczne-emocje:bardzo; rutyna-repetycja:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000458','2026-09-03','smierc:bardzo; taniec:bardzo; samotnosc:bardzo; milosc:troche; strach:bardzo; noc:bardzo; bezsennosc-restless:bardzo; woda:bardzo; droga-podroz:bardzo; zal:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000459','2026-09-03','zamartwianie:bardzo; rutyna-repetycja:bardzo; substancje:bardzo; substancja-regulacja:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:bardzo; potrzeba-zapewnienia:bardzo; wysokie-pobudzenie:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000460','2026-09-03','droga-podroz:bardzo; wolnosc:bardzo; bunt:bardzo; do-swiata:bardzo; woda:bardzo; smierc:bardzo; znikniecie:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; przemiana:bardzo; sprawczosc:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000461','2026-09-03','droga-podroz:bardzo; smutek:bardzo; wyczerpanie:bardzo; samotnosc:bardzo; utrata:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; deszcz:bardzo; czas:bardzo; od-kogos:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000462','2026-09-03','utrata:bardzo; smutek:bardzo; wyczerpanie:bardzo; od-kogos:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; sprawczosc:bardzo; przemiana:bardzo; wolnosc:bardzo; zal:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000463','2026-09-03','pogon:bardzo; gniew:bardzo; ogien:bardzo; wysokie-pobudzenie:bardzo; strach:bardzo; oddech-powietrze:bardzo; prawda:bardzo; zablokowanie:bardzo; sprawczosc:bardzo; woda:bardzo; milosc:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000464','2026-09-03','droga-podroz:bardzo; intensywna-percepcja:bardzo; sensoryka-szukanie:bardzo; smutek:bardzo; zablokowanie:bardzo; wyczerpanie:troche; przemiana:bardzo; nadzieja:bardzo; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000465','2026-09-03','do-swiata:bardzo; sprawczosc:bardzo; gniew:bardzo; ziemia:bardzo; woda:bardzo; ogien:troche; smierc:bardzo; cialo:bardzo; bunt:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000466','2026-09-03','sprzeczne-potrzeby:bardzo; sprawczosc:bardzo; bunt:bardzo; prawda:bardzo; komunikacja-problem:bardzo; niemoznosc-odpuszczenia:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000467','2026-09-03','ucieczka:bardzo; droga-podroz:bardzo; zablokowanie:bardzo; milosc:bardzo; ku-komus:bardzo; komunikacja-problem:bardzo; sprawczosc:troche; czas:bardzo; marzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000468','2026-09-03','sen:bardzo; marzenie:bardzo; pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; noc:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000469','2026-09-03','deszcz:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; woda:bardzo; ziemia:bardzo; ku-komus:bardzo; rutyna-repetycja:bardzo; pamiec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000470','2026-09-03','droga-podroz:bardzo; przemiana:bardzo; innosc:bardzo; pozadanie:bardzo; cialo:bardzo; substancje:bardzo; impulsywnosc:troche; wysokie-pobudzenie:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000471','2026-09-03','noc:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; hiperczujnosc:bardzo; samotnosc:bardzo; sen:bardzo; bezsennosc-restless:bardzo; sensoryka-przytloczenie:bardzo; katastrofizacja:bardzo; potrzeba-zapewnienia:bardzo; schronienie:bardzo; ciemnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000472','2026-09-03','milosc:bardzo; bezwartosciowosc:bardzo; ulga-z-zewnatrz:bardzo; marzenie:bardzo; nigdy-dosc:bardzo; racing-thoughts:bardzo; woda:bardzo; radosc:bardzo; ku-komus:bardzo; potrzeba-zapewnienia:bardzo; cialo:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000473','2026-09-03','radosc:bardzo; nadzieja:bardzo; ciemnosc:bardzo; sen:bardzo; odrodzenie:bardzo; przemiana:bardzo; ku-przyszlosci:bardzo; droga-podroz:bardzo; milosc:bardzo; lek:troche; czulosc:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000474','2026-09-03','droga-podroz:bardzo; milosc:bardzo; strach:bardzo; samotnosc:troche; ku-komus:bardzo; sen:bardzo; marzenie:bardzo; cialo:bardzo; wysokie-pobudzenie:bardzo; przetrwanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000475','2026-09-03','milosc:bardzo; czulosc:troche; smierc:bardzo; strach:bardzo; substancje:troche; sprawczosc:bardzo; ucieczka:bardzo; oddech-powietrze:bardzo; wysokie-pobudzenie:bardzo; samotnosc:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000476','2026-09-03','ukrywanie-reakcji:bardzo; komunikacja-problem:bardzo; kontrola:bardzo; strach:bardzo; wysokie-pobudzenie:bardzo; zablokowanie:bardzo; przemiana:bardzo; odrodzenie:bardzo; nadzieja:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000477','2026-09-03','nierozpoznanie-siebie:bardzo; samotnosc:bardzo; wycofanie:bardzo; utrata:bardzo; wyczerpanie:bardzo; zobojetnienie:bardzo; pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; performowanie-roli:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000478','2026-09-03','milosc:bardzo; czulosc:bardzo; dotyk:bardzo; czas:bardzo; radosc:bardzo; cyklicznosc-wzorzec:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000479','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; tesknota:bardzo; dom:bardzo; ku-przeszlosci:bardzo; samotnosc:bardzo; innosc:troche; noc:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; milosc:bardzo; czulosc:bardzo; droga-podroz:troche; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000480','2026-09-03','sensoryka-przytloczenie:bardzo; komunikacja-problem:bardzo; niedopasowanie-spoleczne:bardzo; zobojetnienie:bardzo; do-swiata:bardzo; nic-pustka:bardzo; zablokowanie:bardzo; maska:bardzo; performowanie-roli:bardzo; substancje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000481','2026-09-03','od-kogos:bardzo; droga-podroz:bardzo; utrata:bardzo; milosc:troche; komunikacja-problem:bardzo; sprawczosc:bardzo; bunt:bardzo; potrzeba-zapewnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000482','2026-09-03','pozadanie:bardzo; milosc:bardzo; substancje:bardzo; ucieczka:bardzo; wolnosc:bardzo; pogon:bardzo; ku-komus:bardzo; sprzeczne-potrzeby:bardzo; droga-podroz:bardzo; noc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000483','2026-09-03','prawda:bardzo; nierozpoznanie-siebie:bardzo; bunt:bardzo; sprawczosc:bardzo; ciemnosc:bardzo; smierc:bardzo; ku-przyszlosci:bardzo; milosc:bardzo; samotnosc:troche; przemiana:bardzo; nadzieja:bardzo; gniew:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000484','2026-09-03','milosc:bardzo; do-swiata:bardzo; substancje:bardzo; wspomnienia:bardzo; pamiec:troche; dom:bardzo; droga-podroz:bardzo; radosc:bardzo; sensoryka-szukanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000485','2026-09-03','performowanie-roli:bardzo; kontrola-wizerunku:bardzo; cialo:bardzo; innosc:bardzo; bunt:bardzo; latanie-spadanie:bardzo; marzenie:bardzo; sensoryka-przytloczenie:bardzo; strach:bardzo; bezsennosc-restless:troche; gniew:bardzo; wysokie-pobudzenie:bardzo; smierc:bardzo; odrodzenie:bardzo; sprawczosc:bardzo; duma:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000486','2026-09-03','droga-podroz:bardzo; samotnosc-preferowana:bardzo; wolnosc:bardzo; od-kogos:bardzo; utrata:bardzo; wspomnienia:troche; czas:bardzo; do-siebie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000487','2026-09-03','droga-podroz:bardzo; rutyna-repetycja:bardzo; cyklicznosc-wzorzec:bardzo; taniec:bardzo; czas:bardzo; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000488','2026-09-03','radosc:bardzo; samotnosc-preferowana:bardzo; taniec:bardzo; ciemnosc:bardzo; czas:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; latanie-spadanie:bardzo; milosc:bardzo; odrodzenie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000489','2026-09-03','komunikacja-problem:bardzo; prawda:bardzo; utrata:bardzo; smutek:bardzo; zal:bardzo; od-kogos:bardzo; niedopasowanie-spoleczne:bardzo; sprawczosc:bardzo; przemiana:troche; milosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000490','2026-09-03','wspomnienia:bardzo; sen:bardzo; milosc:bardzo; substancje:bardzo; bunt:bardzo; taniec:bardzo; dotyk:bardzo; czulosc:bardzo; niedopasowanie-spoleczne:troche; radosc:bardzo; wysokie-pobudzenie:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000491','2026-09-03','pamiec:bardzo; milosc:bardzo; nadzieja:bardzo; bezsennosc-restless:bardzo; bezsilnosc:bardzo; sprawczosc:bardzo; rutyna-repetycja:bardzo; do-swiata:bardzo; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000492','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; utrata:bardzo; pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; nierozpoznanie-siebie:bardzo; pustka-emocjonalna:bardzo; samotnosc:bardzo; ogien:bardzo; smierc:bardzo; rozpacz:bardzo; bezwartosciowosc:bardzo; performowanie-roli:bardzo; ja-publiczne-ja-prywatne:bardzo; ku-przeszlosci:bardzo; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000493','2026-09-03','komunikacja-problem:bardzo; prawda:bardzo; utrata:bardzo; smutek:bardzo; zal:bardzo; od-kogos:bardzo; niedopasowanie-spoleczne:bardzo; sprawczosc:bardzo; przemiana:troche; milosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000494','2026-09-03','milosc:bardzo; odrodzenie:bardzo; przemiana:bardzo; nadzieja:bardzo; radosc:bardzo; ku-komus:bardzo; ku-przyszlosci:bardzo; noc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000495','2026-09-03','wolnosc:bardzo; cialo:bardzo; dotyk:bardzo; woda:bardzo; noc:bardzo; ciemnosc:bardzo; oddech-powietrze:bardzo; taniec:bardzo; droga-podroz:bardzo; ku-komus:bardzo; czulosc:bardzo; sprzeczne-potrzeby:bardzo; sensoryka-metafora:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000496','2026-09-03','milosc:bardzo; taniec:bardzo; noc:bardzo; pozadanie:bardzo; nigdy-dosc:bardzo; smierc:bardzo; latanie-spadanie:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000497','2026-09-03','wolnosc:bardzo; ucieczka:bardzo; droga-podroz:bardzo; woda:bardzo; ziemia:bardzo; smutek:bardzo; sensoryka-metafora:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000498','2026-09-03','milosc:bardzo; cialo:bardzo; komunikacja-problem:bardzo; ukrywanie-reakcji:bardzo; noc:bardzo; sensoryka-szukanie:bardzo; ziemia:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000499','2026-09-03','sen:bardzo; marzenie:bardzo; woda:bardzo; ciemnosc:bardzo; przemiana:bardzo; odrodzenie:bardzo; ziemia:bardzo; powrot-do:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000500','2026-09-03','sensoryka-przytloczenie:bardzo; intensywna-percepcja:bardzo; gniew:bardzo; pogon:bardzo; kontrola:bardzo; zablokowanie:bardzo; ucieczka:bardzo; wysokie-pobudzenie:bardzo; od-kogos:bardzo; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000501','2026-09-03','komunikacja-problem:bardzo; zablokowanie:bardzo; bezsennosc-restless:bardzo; brak-napedu:bardzo; wyczerpanie:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; od-kogos:bardzo; sprawczosc:bardzo; prawda:bardzo; frustracja:bardzo; wycofanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000502','2026-09-03','mocne-kobiety:bardzo; duma:bardzo; sprawczosc:bardzo; bunt:troche; do-swiata:bardzo; noc:bardzo; radosc:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000503','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; chaos-balagan:bardzo; pamiec:bardzo; cyklicznosc-wzorzec:bardzo; taniec:bardzo; od-kogos:bardzo; ulga-odroczona:bardzo; zablokowanie:bardzo; gniew:bardzo; zal:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000504','2026-09-03','lek:bardzo; strach:bardzo; smierc:bardzo; bunt:bardzo; wolnosc:bardzo; bezsilnosc:bardzo; przeciazenie-przyszloscia:bardzo; do-swiata:bardzo; przetrwanie:bardzo; wina:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000505','2026-09-03','sensoryka-przytloczenie:bardzo; cialo:bardzo; smierc:bardzo; odrodzenie:troche; ogien:bardzo; noc:bardzo; sen:bardzo; lek:bardzo; strach:bardzo; hiperczujnosc:bardzo; do-swiata:bardzo; chaos-balagan:bardzo; wysokie-pobudzenie:bardzo; zablokowanie:bardzo; ulga-z-zewnatrz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000506','2026-09-03','pozadanie:bardzo; dotyk:bardzo; cialo:bardzo; noc:bardzo; milosc:troche; sprzeczne-emocje:bardzo; ukrywanie-reakcji:bardzo; kontrola-wizerunku:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000507','2026-09-03','droga-podroz:bardzo; utrata:bardzo; tesknota:bardzo; smutek:bardzo; komunikacja-problem:bardzo; ku-komus:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; ziemia:bardzo; samotnosc:bardzo; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000508','2026-09-03','milosc:bardzo; czulosc:bardzo; utrata:bardzo; smierc-wlasna:bardzo; smierc:bardzo; rozpacz:bardzo; smutek:bardzo; zal:bardzo; woda:troche; taniec:bardzo; wina:bardzo; gniew:bardzo; od-kogos:bardzo; ku-komus:bardzo; cialo:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000509','2026-09-03','czas:bardzo; droga-podroz:bardzo; pogon:bardzo; ucieczka:bardzo; cyklicznosc-wzorzec:bardzo; wysokie-pobudzenie:bardzo; intensywnosc-potem-crash:bardzo; wyczerpanie:bardzo; marzenie:bardzo; latanie-spadanie:bardzo; zablokowanie:bardzo; sensoryka-metafora:bardzo; przetrwanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000510','2026-09-03','innosc:bardzo; niedopasowanie-spoleczne:bardzo; deszcz:bardzo; droga-podroz:bardzo; utrata:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; czas:bardzo; odrodzenie:bardzo; przemiana:bardzo; nadzieja:bardzo; wolnosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000511','2026-09-03','droga-podroz:bardzo; milosc:bardzo; czulosc:bardzo; przetrwanie:bardzo; brak-nadziei:bardzo; schronienie:bardzo; marzenie:bardzo; noc:bardzo; wolnosc:bardzo; sensoryka-szukanie:bardzo; czas:bardzo; bezsilnosc:bardzo; niskie-pobudzenie:bardzo; sprzeczne-emocje:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000777','2026-09-03','rutyna-repetycja:bardzo; cyklicznosc-wzorzec:bardzo; substancje:bardzo; performowanie-roli:bardzo; maska:bardzo; czas:bardzo; prawda:bardzo; zablokowanie:bardzo; nierozpoznanie-siebie:troche; przetrwanie:bardzo; do-swiata:bardzo; droga-podroz:troche; wstyd:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000512','2026-09-03','sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; oddech-powietrze:bardzo; ziemia:bardzo; do-swiata:bardzo; innosc:bardzo; komunikacja-problem:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000513','2026-09-03','performowanie-roli:bardzo; kontrola-wizerunku:bardzo; substancje:bardzo; pozadanie:troche; czas:bardzo; sensoryka-przytloczenie:troche; duma:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000514','2026-09-03','milosc:bardzo; pozadanie:bardzo; utrata:bardzo; smutek:bardzo; bezsennosc-restless:bardzo; sen:bardzo; ku-komus:bardzo; dotyk:bardzo; czulosc:bardzo; odrodzenie:bardzo; przemiana:bardzo; noc:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000515','2026-09-03','do-swiata:bardzo; prawda:bardzo; komunikacja-problem:bardzo; zablokowanie:bardzo; przeciazenie-przyszloscia:bardzo; droga-podroz:bardzo; marzenie:bardzo; sprawczosc:bardzo; nadzieja:bardzo; bunt:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000516','2026-09-03','marzenie:bardzo; przemiana:bardzo; latanie-spadanie:bardzo; czas:bardzo; duma:bardzo; euforia-naped:bardzo; intensywnosc-potem-crash:bardzo; utrata:bardzo; cyklicznosc-wzorzec:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000517','2026-09-03','taniec:bardzo; sensoryka-szukanie:bardzo; radosc:bardzo; rutyna-repetycja:bardzo; performowanie-roli:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000518','2026-09-03','droga-podroz:bardzo; przemiana:bardzo; innosc:bardzo; pozadanie:bardzo; cialo:bardzo; substancje:bardzo; impulsywnosc:troche; wysokie-pobudzenie:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000519','2026-09-03','ciemnosc:bardzo; sen:bardzo; samotnosc:bardzo; komunikacja-problem:bardzo; niedopasowanie-spoleczne:bardzo; sensoryka-przytloczenie:bardzo; sensoryka-metafora:bardzo; noc:bardzo; intensywna-percepcja:bardzo; do-swiata:bardzo; pamiec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000520','2026-09-03','lek:bardzo; hiperczujnosc:bardzo; sen:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; napiecie-ciala:bardzo; sensoryka-przytloczenie:bardzo; schronienie:bardzo; potrzeba-zapewnienia:bardzo; niepewnosc-nie-do-zniesienia:bardzo; zablokowanie:bardzo; ku-komus:bardzo; ciemnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000521','2026-09-03','schronienie:bardzo; droga-podroz:bardzo; dom:bardzo; przetrwanie:bardzo; czas:bardzo; marzenie:bardzo; zablokowanie:bardzo; innosc:bardzo; niedopasowanie-spoleczne:troche; wycofanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000522','2026-09-03','lek:bardzo; milosc:bardzo; ukrywanie-reakcji:bardzo; czulosc:bardzo; dotyk:bardzo; deszcz:bardzo; smierc-wlasna:bardzo; sprzeczne-potrzeby:bardzo; od-kogos:bardzo; zal:bardzo; smutek:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000523','2026-09-03','droga-podroz:bardzo; dom:bardzo; schronienie:bardzo; ku-komus:bardzo; cel-nieosiagniety:bardzo; pogon:bardzo; ogien:bardzo; milosc:troche; marzenie:bardzo; ku-przyszlosci:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000524','2026-09-03','sen:bardzo; droga-podroz:bardzo; woda:bardzo; latanie-spadanie:bardzo; strach:bardzo; milosc:bardzo; komunikacja-problem:bardzo; cialo:bardzo; zablokowanie:bardzo; bezsilnosc:bardzo; przetrwanie:bardzo; przemiana:bardzo; emocja-przez-cialo:bardzo; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000525','2026-09-03','samotnosc:bardzo; droga-podroz:bardzo; noc:bardzo; zablokowanie:bardzo; brak-nadziei:bardzo; sen:bardzo; melancholia:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000526','2026-09-03','przetrwanie:bardzo; nadzieja:bardzo; radosc:bardzo; taniec:bardzo; wolnosc:bardzo; cialo:bardzo; ziemia:bardzo; zamartwianie:bardzo; ku-przyszlosci:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000527','2026-09-03','milosc:bardzo; pozadanie:bardzo; dotyk:bardzo; cialo:bardzo; sprzeczne-potrzeby:bardzo; zablokowanie:bardzo; emocja-przez-cialo:bardzo; wysokie-pobudzenie:bardzo; ku-komus:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000528','2026-09-03','nic-pustka:bardzo; pustka-emocjonalna:bardzo; smierc:bardzo; utrata:bardzo; wspomnienia:bardzo; pamiec:bardzo; do-swiata:bardzo; gniew:bardzo; woda:bardzo; deszcz:bardzo; ciemnosc:bardzo; smutek:bardzo; bezsilnosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000529','2026-09-03','wolnosc:bardzo; ucieczka:bardzo; droga-podroz:bardzo; wyczerpanie:bardzo; niskie-pobudzenie:bardzo; radosc:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; nadzieja:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000530','2026-09-03','maskowanie:bardzo; samokontrola-spoleczna:bardzo; ukrywanie-reakcji:bardzo; ukrywanie-potrzeb:bardzo; kontrola-wizerunku:bardzo; cialo:bardzo; performowanie-roli:bardzo; ja-publiczne-ja-prywatne:bardzo; komunikacja-problem:bardzo; sprzeczne-potrzeby:bardzo; dotyk:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000531','2026-09-03','mocne-kobiety:bardzo; duma:bardzo; sprawczosc:bardzo; pozadanie:troche; taniec:troche; sensoryka-szukanie:bardzo; do-innych:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000532','2026-09-03','marzenie:bardzo; noc:bardzo; deszcz:bardzo; latanie-spadanie:bardzo; samotnosc:bardzo; tesknota:bardzo; ku-komus:bardzo; czas:bardzo; nadzieja:bardzo; droga-podroz:bardzo; wina:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000533','2026-09-03','gniew:bardzo; emocjonalna-dysregulacja:bardzo; kontrola:bardzo; zamartwianie:bardzo; nierozpoznanie-siebie:bardzo; smierc:bardzo; ukrywanie-reakcji:bardzo; samokontrola-spoleczna:bardzo; samotnosc:bardzo; wysokie-pobudzenie:bardzo; sprzeczne-emocje:bardzo; wstyd:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000534','2026-09-03','droga-podroz:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; komunikacja-problem:bardzo; milosc:bardzo; pozadanie:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000535','2026-09-03','deszcz:bardzo; droga-podroz:bardzo; latanie-spadanie:bardzo; czas:bardzo; do-swiata:bardzo; gniew:bardzo; marzenie:bardzo; wysokie-pobudzenie:bardzo; cyklicznosc-wzorzec:bardzo; brak-nadziei:bardzo; smutek:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000536','2026-09-03','tesknota:bardzo; milosc:troche; ku-komus:bardzo; cel-nieosiagniety:troche; smierc:troche; sensoryka-metafora:troche; noc:ociupinke; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000537','2026-09-03','samotnosc:bardzo; niedopasowanie-spoleczne:bardzo; komunikacja-problem:bardzo; wycofanie:bardzo; utrata:bardzo; cel-nieosiagniety:bardzo; pogon:troche; sensoryka-metafora:bardzo; cialo:troche; smierc:troche; wina:troche; brak-nadziei:troche; droga-podroz:bardzo; przemiana:troche; odrodzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000538','2026-09-03','pogon:bardzo; ku-przyszlosci:bardzo; sprawczosc:bardzo; marzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000539','2026-09-03','noc:bardzo; ciemnosc:bardzo; milosc:bardzo; substancje:bardzo; sensoryka-metafora:bardzo; latanie-spadanie:troche; do-innych:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000540','2026-09-03','cialo:bardzo; smierc:bardzo; pozadanie:bardzo; dotyk:bardzo; milosc:bardzo; taniec:bardzo; substancje:bardzo; euforia-naped:bardzo; eskalacja:bardzo; powrot-do:bardzo; czas:bardzo; sensoryka-szukanie:bardzo; sensoryka-metafora:bardzo; niskie-pobudzenie:troche; zablokowanie:troche; sprawczosc:bardzo; przetrwanie:troche; maska:ociupinke; noc:troche; przemiana:bardzo; odrodzenie:bardzo; wspomnienia:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000541','2026-09-03','strach:bardzo; intensywna-percepcja:bardzo; sensoryka-metafora:bardzo; potrzeba-zapewnienia:bardzo; ulga-z-zewnatrz:bardzo; dotyk:bardzo; czulosc:bardzo; nadzieja:bardzo; ulga-odroczona:bardzo; czas:bardzo; ku-przyszlosci:troche; noc:troche; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000542','2026-09-03','smutek:bardzo; zamartwianie:bardzo; sprawczosc:bardzo; cel-nieosiagniety:bardzo; sensoryka-metafora:bardzo; woda:bardzo; milosc:troche; utrata:troche; czas:troche; przetrwanie:troche; pogon:troche; noc:troche; nadzieja:troche; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000543','2026-09-03','wstyd:bardzo; potrzeba-zapewnienia:bardzo; milosc:bardzo; noc:bardzo; taniec:bardzo; substancje:bardzo; wysokie-pobudzenie:bardzo; bezsilnosc:troche; cel-nieosiagniety:troche; sensoryka-przytloczenie:troche; do-siebie:troche; wina:troche; pogon:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000544','2026-09-03','cyklicznosc-wzorzec:bardzo; niedopasowanie-spoleczne:bardzo; bunt:bardzo; innosc:troche; zablokowanie:troche; sprawczosc:troche; ku-przeszlosci:troche; do-innych:troche; dom:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000545','2026-09-03','sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; milosc:bardzo; dom:bardzo; powrot-do:bardzo; ku-komus:bardzo; od-kogos:bardzo; wstyd:bardzo; czulosc:bardzo; prawda:bardzo; komunikacja-problem:troche; potrzeba-zapewnienia:troche; zablokowanie:troche; ku-przyszlosci:troche; samotnosc:troche; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000546','2026-09-03','czas:bardzo; noc:bardzo; milosc:bardzo; czulosc:troche; ku-przyszlosci:troche; sensoryka-metafora:bardzo; smierc:troche; wspomnienia:bardzo; pamiec:troche; marzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000547','2026-09-03','rutyna-repetycja:bardzo; sensoryka-metafora:troche; sen:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000548','2026-09-03','milosc:bardzo; czulosc:bardzo; dotyk:bardzo; cialo:bardzo; nadzieja:bardzo; radosc:bardzo; czas:bardzo; dom:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo; dotarcie:troche; marzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000549','2026-09-03','utrata:bardzo; samotnosc:bardzo; smutek:bardzo; tesknota:bardzo; milosc:bardzo; ku-przeszlosci:bardzo; anhedonia:bardzo; zal:bardzo; nadmierny-sen:troche; wina:troche; noc:troche; sen:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000550','2026-09-03','wysokie-pobudzenie:bardzo; impulsywnosc:bardzo; sprzeczne-potrzeby:bardzo; smierc:bardzo; sensoryka-metafora:bardzo; do-siebie:troche; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000551','2026-09-03','noc:bardzo; ciemnosc:bardzo; sensoryka-metafora:bardzo; intensywna-percepcja:bardzo; oddech-powietrze:troche; nie-wiem-co-czuje:troche; sen:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000552','2026-09-03','sensoryka-metafora:bardzo; ogien:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000553','2026-09-03','milosc:bardzo; tesknota:bardzo; czulosc:bardzo; cialo:bardzo; oddech-powietrze:bardzo; woda:bardzo; sensoryka-metafora:bardzo; sprzeczne-potrzeby:bardzo; potrzeba-zapewnienia:bardzo; ulga-z-zewnatrz:bardzo; ku-komus:bardzo; czas:bardzo; niepewnosc-nie-do-zniesienia:troche; nadzieja:troche; noc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000554','2026-09-03','utrata:bardzo; zal:bardzo; gniew:bardzo; do-innych:bardzo; od-kogos:bardzo; dom:bardzo; pustka-emocjonalna:bardzo; sprawczosc:bardzo; bunt:troche; wycofanie:troche; ogien:troche; milosc:troche; droga-podroz:troche; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000555','2026-09-03','noc:bardzo; deszcz:bardzo; bezsennosc:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; substancje:bardzo; radosc:bardzo; prawda:troche; ku-przeszlosci:troche; utrata:troche; sensoryka-metafora:troche; sen:bardzo; pamiec:bardzo; wspomnienia:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000556','2026-09-03','noc:bardzo; ciemnosc:bardzo; smutek:bardzo; milosc:bardzo; sprzeczne-potrzeby:bardzo; ku-komus:bardzo; dotyk:bardzo; ogien:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000557','2026-09-03','ciemnosc:bardzo; czas:bardzo; sensoryka-metafora:bardzo; intensywna-percepcja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000558','2026-09-03','zazdrosc:bardzo; milosc:bardzo; gniew:bardzo; zal:bardzo; strach:bardzo; smierc:bardzo; noc:bardzo; do-innych:bardzo; sprzeczne-emocje:bardzo; komunikacja-problem:troche; cialo:troche; przemiana:bardzo; odrodzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000559','2026-09-03','zablokowanie:bardzo; oddech-powietrze:bardzo; sensoryka-metafora:bardzo; cel-nieosiagniety:troche; komunikacja-problem:troche; niskie-pobudzenie:troche; ku-komus:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000560','2026-09-03','schronienie:bardzo; dom:bardzo; sensoryka-przytloczenie:bardzo; sensoryka-metafora:bardzo; zablokowanie:bardzo; innosc:bardzo; wysokie-pobudzenie:bardzo; milosc:troche; latanie-spadanie:troche; do-siebie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000561','2026-09-03','rutyna-repetycja:bardzo; komunikacja-problem:bardzo; milosc:troche; ku-komus:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000562','2026-09-03','schronienie:bardzo; dom:bardzo; wycofanie:bardzo; ukrywanie-reakcji:bardzo; smutek:bardzo; bezsennosc-restless:bardzo; sensoryka-metafora:bardzo; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000563','2026-09-03','milosc:bardzo; pozadanie:bardzo; utrata:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; ku-komus:bardzo; do-innych:bardzo; ogien:bardzo; ulga-z-zewnatrz:troche; zal:troche; marzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000564','2026-09-03','milosc:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; komunikacja-problem:bardzo; zablokowanie:bardzo; frustracja:bardzo; cyklicznosc-wzorzec:bardzo; do-innych:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000565','2026-09-03','sensoryka-metafora:bardzo; zal:troche; smutek:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000566','2026-09-03','radosc:bardzo; ziemia:bardzo; czas:troche; przemiana:ociupinke; odrodzenie:ociupinke');

INSERT INTO tag_snapshots VALUES('lyrics-000567','2026-09-03','milosc:bardzo; utrata:bardzo; wyczerpanie:bardzo; zablokowanie:bardzo; smutek:bardzo; sprzeczne-potrzeby:bardzo; bezsilnosc:bardzo; ku-komus:bardzo; cialo:troche; zal:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000568','2026-09-03','milosc:bardzo; utrata:bardzo; wyczerpanie:bardzo; zablokowanie:bardzo; smutek:bardzo; sprzeczne-potrzeby:bardzo; bezsilnosc:bardzo; ku-komus:bardzo; cialo:troche; zal:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000569','2026-09-03','utrata:bardzo; ku-przeszlosci:bardzo; ku-przyszlosci:bardzo; czas:bardzo; woda:bardzo; sensoryka-metafora:bardzo; ucieczka:bardzo; sprawczosc:bardzo; dotyk:troche; milosc:troche; cialo:troche; droga-podroz:bardzo; przemiana:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000570','2026-09-03','milosc:bardzo; tesknota:bardzo; samotnosc:bardzo; ku-komus:bardzo; ku-przeszlosci:troche; czulosc:troche; sen:bardzo; marzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000571','2026-09-03','milosc:bardzo; czulosc:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000572','2026-09-07','milosc:ociupinke; do-innych:ociupinke');

INSERT INTO tag_snapshots VALUES('lyrics-000573','2026-09-03','ciemnosc:bardzo; ucieczka:bardzo; bezsennosc-restless:bardzo; cialo:bardzo; sensoryka-metafora:bardzo; racing-thoughts:troche; wysokie-pobudzenie:troche; czas:troche; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000574','2026-09-03','milosc:bardzo; radosc:bardzo; latanie-spadanie:bardzo; ku-komus:bardzo; pozadanie:troche; euforia-naped:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000575','2026-09-03','pozadanie:bardzo; dotyk:bardzo; milosc:bardzo; sprzeczne-potrzeby:bardzo; lek-antycypacyjny:bardzo; ku-komus:bardzo; zablokowanie:troche; noc:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000576','2026-09-03','milosc:bardzo; pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; ciemnosc:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo; oddech-powietrze:troche; strach:troche; sprzeczne-emocje:troche; wolnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000577','2026-09-03','samotnosc:bardzo; wycofanie:bardzo; ku-komus:bardzo; smutek:bardzo; od-swiata:troche; brak-napedu:troche; komunikacja-problem:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000578','2026-09-03','milosc:bardzo; samotnosc:bardzo; smutek:bardzo; przetrwanie:bardzo; noc:bardzo; sprawczosc:bardzo; substancje:troche; zal:troche; cialo:troche; sensoryka-metafora:troche; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000579','2026-09-03','ucieczka:bardzo; strach:bardzo; unikanie-z-leku:bardzo; wysokie-pobudzenie:bardzo; sprawczosc:bardzo; wolnosc:bardzo; bunt:bardzo; do-innych:bardzo; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000580','2026-09-03','gniew:bardzo; do-innych:bardzo; komunikacja-problem:bardzo; do-swiata:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000581','2026-09-03','powrot-do:bardzo; dom:bardzo; dotarcie:bardzo; pogon:bardzo; do-innych:bardzo; sprawczosc:bardzo; pozadanie:troche; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000582','2026-09-03','radosc:bardzo; smutek:bardzo; samotnosc:bardzo; sprzeczne-emocje:bardzo; ku-swiatu:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000583','2026-09-03','milosc:bardzo; samotnosc:bardzo; czulosc:bardzo; czas:bardzo; taniec:bardzo; ku-komus:bardzo; ukrywanie-reakcji:troche; dotyk:troche; smutek:troche; sensoryka-metafora:troche; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000584','2026-09-03','schronienie:bardzo; nadzieja:bardzo; czulosc:bardzo; milosc:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo; ciemnosc:troche; ku-swiatu:troche; droga-podroz:bardzo; wspomnienia:bardzo; pamiec:troche; przemiana:bardzo; odrodzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000585','2026-09-03','taniec:bardzo; radosc:bardzo; bunt:bardzo; sprawczosc:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; milosc:troche; pozadanie:troche; wolnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000587','2026-09-03','niedopasowanie-spoleczne:bardzo; bunt:bardzo; komunikacja-problem:troche; smutek:troche; do-innych:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000588','2026-09-03','wolnosc:bardzo; bunt:bardzo; gniew:bardzo; do-swiata:bardzo; ogien:bardzo; sprawczosc:bardzo; strach:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000589','2026-09-03','smutek:bardzo; lek:bardzo; wysokie-pobudzenie:bardzo; napiecie-ciala:bardzo; emocja-przez-cialo:bardzo; sensoryka-przytloczenie:bardzo; niemoznosc-odpuszczenia:bardzo; substancje:bardzo; substancja-regulacja:troche; hiperczujnosc:troche; zamartwianie:troche; cialo:troche; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000590','2026-09-03','zazdrosc:bardzo; lek-antycypacyjny:bardzo; potrzeba-zapewnienia:bardzo; bezsilnosc:bardzo; milosc:bardzo; smutek:bardzo; ku-komus:bardzo; do-innych:bardzo; niepewnosc-nie-do-zniesienia:troche; komunikacja-problem:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000591','2026-09-03','ku-przeszlosci:bardzo; czas:bardzo; utrata:bardzo; melancholia:bardzo; smutek:bardzo; tesknota:bardzo; sensoryka-metafora:bardzo; czulosc:troche; wspomnienia:bardzo; pamiec:bardzo; marzenie:bardzo; sen:troche; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000592','2026-09-03','pozadanie:bardzo; milosc:bardzo; nigdy-dosc:bardzo; euforia-naped:bardzo; sprzeczne-emocje:bardzo; wysokie-pobudzenie:bardzo; dotyk:bardzo; ku-komus:bardzo; gniew:bardzo; impulsywnosc:troche; sensoryka-szukanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000593','2026-09-03','noc:bardzo; samotnosc:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; taniec:bardzo; ku-komus:bardzo; radosc:bardzo; dotarcie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000594','2026-09-03','utrata:bardzo; gniew:bardzo; sprawczosc:bardzo; od-kogos:bardzo; do-innych:bardzo; substancje:bardzo; duma:bardzo; sensoryka-metafora:bardzo; deszcz:troche; ogien:troche; bunt:troche; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000595','2026-09-03','noc:bardzo; czas:bardzo; woda:bardzo; ogien:bardzo; utrata:bardzo; ku-przeszlosci:bardzo; smierc:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo; przetrwanie:bardzo; taniec:troche; milosc:troche; tesknota:troche; ku-swiatu:troche; droga-podroz:bardzo; przemiana:bardzo; odrodzenie:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000596','2026-09-03','milosc:bardzo; woda:bardzo; ku-komus:bardzo; pogon:bardzo; sensoryka-metafora:bardzo; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000597','2026-09-03','nic-pustka:bardzo; pustka-emocjonalna:bardzo; zobojetnienie:bardzo; samotnosc:bardzo; bezsilnosc:troche; wspomnienia:troche; ku-komus:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000598','2026-09-03','sen:bardzo; marzenie:bardzo; noc:bardzo; ogien:bardzo; sensoryka-metafora:bardzo; intensywna-percepcja:bardzo; wysokie-pobudzenie:bardzo; smierc:bardzo; odrodzenie:troche; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000599','2026-09-03','przemiana:bardzo; odrodzenie:bardzo; smierc:bardzo; bunt:bardzo; wolnosc:bardzo; innosc:bardzo; cialo:bardzo; duma:bardzo; sprawczosc:bardzo; gniew:bardzo; do-swiata:bardzo; wysokie-pobudzenie:bardzo; ogien:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000600','2026-09-03','samotnosc:bardzo; przemiana:bardzo; odrodzenie:bardzo; ulga:bardzo; spokoj:troche; powrot-do:troche; czas:bardzo; sensoryka-metafora:bardzo; ku-przyszlosci:bardzo; radosc:troche; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000601','2026-09-03','milosc:bardzo; utrata:bardzo; smutek:bardzo; zal:bardzo; tesknota:bardzo; ku-przeszlosci:bardzo; wspomnienia:bardzo; pamiec:troche; czas:bardzo; smierc:troche; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000602','2026-09-03','milosc:bardzo; dom:bardzo; samotnosc:bardzo; niedopasowanie-spoleczne:bardzo; substancje:bardzo; cialo:bardzo; dotyk:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; ciemnosc:bardzo; do-swiata:bardzo; sensoryka-przytloczenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000603','2026-09-03','utrata:bardzo; milosc:bardzo; smutek:bardzo; tesknota:bardzo; ku-komus:bardzo; od-kogos:bardzo; ku-przeszlosci:bardzo; czas:bardzo; noc:bardzo; pamiec:troche; wspomnienia:troche; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000604','2026-09-03','milosc:bardzo; woda:bardzo; cialo:troche; sensoryka-metafora:bardzo; wystarczy:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000605','2026-09-03','woda:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; spokoj:bardzo; lek-antycypacyjny:troche; droga-podroz:bardzo; czulosc:troche; radosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000606','2026-09-03','milosc:bardzo; utrata:bardzo; cyklicznosc-wzorzec:bardzo; wspomnienia:bardzo; pamiec:bardzo; przemiana:troche; zal:bardzo; do-swiata:troche; ku-przeszlosci:bardzo; komunikacja-problem:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000607','2026-09-03','milosc:bardzo; czulosc:bardzo; dotyk:bardzo; dom:bardzo; sen:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; zamartwianie:bardzo; ku-przyszlosci:troche; sensoryka-szukanie:bardzo; ulga-z-zewnatrz:bardzo; gniew:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000608','2026-09-03','wysokie-pobudzenie:bardzo; euforia-naped:bardzo; bunt:bardzo; gniew:bardzo; ogien:bardzo; sensoryka-metafora:bardzo; intensywna-percepcja:bardzo; sprzeczne-emocje:bardzo; pustka-emocjonalna:bardzo; milosc:bardzo; do-swiata:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000610','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; niedopasowanie-spoleczne:bardzo; innosc:bardzo; samotnosc:bardzo; smutek:bardzo; tesknota:bardzo; czas:bardzo; noc:bardzo; brak-napedu:troche; wyczerpanie:troche; utrata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000611','2026-09-03','sen:bardzo; marzenie:bardzo; ku-przyszlosci:bardzo; milosc:bardzo; samotnosc:bardzo; noc:bardzo; smutek:bardzo; tesknota:bardzo; sensoryka-metafora:bardzo; intensywna-percepcja:bardzo; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000612','2026-09-03','smierc:bardzo; noc:bardzo; milosc:bardzo; strach:bardzo; czulosc:troche; ku-komus:bardzo; dotyk:bardzo; sensoryka-metafora:bardzo; sprzeczne-emocje:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000613','2026-09-03','wspomnienia:bardzo; ku-przeszlosci:bardzo; utrata:bardzo; samotnosc:bardzo; ciemnosc:bardzo; smierc:bardzo; substancje:bardzo; substancja-regulacja:bardzo; smutek:bardzo; rozpacz:bardzo; sensoryka-metafora:bardzo; marzenie:troche; do-swiata:bardzo; czas:bardzo; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000614','2026-09-03','gniew:bardzo; milosc:bardzo; utrata:bardzo; zal:bardzo; wspomnienia:bardzo; pamiec:troche; ogien:bardzo; wysokie-pobudzenie:bardzo; sprawczosc:bardzo; do-swiata:troche; od-kogos:bardzo; cialo:troche; sensoryka-metafora:bardzo; przemiana:bardzo; bunt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000615','2026-09-03','do-swiata:bardzo; samotnosc:troche; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000616','2026-09-03','wolnosc:bardzo; od-kogos:bardzo; droga-podroz:bardzo; przemiana:bardzo; milosc:troche; utrata:troche; oddech-powietrze:bardzo; sprawczosc:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000617','2026-09-03','smutek:bardzo; brak-nadziei:bardzo; do-swiata:bardzo; woda:bardzo; sensoryka-metafora:bardzo; smierc:bardzo; cyklicznosc-wzorzec:bardzo; gniew:troche; rozpacz:bardzo; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000618','2026-09-03','do-swiata:bardzo; gniew:bardzo; brak-nadziei:bardzo; ogien:bardzo; woda:bardzo; smierc:bardzo; sensoryka-metafora:bardzo; wysokie-pobudzenie:bardzo; strach:troche; bunt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000619','2026-09-03','performowanie-roli:bardzo; maskowanie-koszt:bardzo; ja-publiczne-ja-prywatne:troche; przemiana:bardzo; odrodzenie:bardzo; wolnosc:bardzo; milosc:bardzo; czulosc:bardzo; do-siebie:bardzo; ku-przyszlosci:bardzo; wyczerpanie:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000620','2026-09-03','niedopasowanie-spoleczne:bardzo; samotnosc:bardzo; ucieczka:bardzo; droga-podroz:bardzo; dom:bardzo; smutek:bardzo; ukrywanie-reakcji:bardzo; deszcz:bardzo; innosc:bardzo; wolnosc:troche; od-kogos:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000621','2026-09-03','ciemnosc:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; sensoryka-metafora:bardzo; ogien:bardzo; sen:bardzo; marzenie:bardzo; sprawczosc:bardzo; droga-podroz:troche; maska:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000523','2026-09-03','droga-podroz:bardzo; dom:bardzo; ku-komus:bardzo; cel-nieosiagniety:bardzo; pogon:troche; ogien:bardzo; milosc:troche; schronienie:troche; sensoryka-metafora:bardzo; marzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000622','2026-09-03','cialo:bardzo; nic-pustka:bardzo; pustka-emocjonalna:bardzo; emocja-przez-cialo:bardzo; smutek:bardzo; utrata:bardzo; samotnosc:bardzo; wspomnienia:bardzo; pamiec:bardzo; przemiana:bardzo; bezwartosciowosc:bardzo; wina:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000623','2026-09-03','smierc:bardzo; ucieczka:bardzo; lek-antycypacyjny:bardzo; strach:bardzo; ciemnosc:bardzo; czas:bardzo; sprawczosc:bardzo; do-swiata:troche; sensoryka-metafora:bardzo; noc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000624','2026-09-03','bunt:bardzo; wolnosc:bardzo; ucieczka:bardzo; schronienie:bardzo; przetrwanie:bardzo; utrata:bardzo; smierc:bardzo; droga-podroz:bardzo; przemiana:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; samotnosc:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000625','2026-09-03','milosc:bardzo; pozadanie:bardzo; maska:bardzo; performowanie-roli:bardzo; dopasowanie-roli:bardzo; ku-komus:bardzo; dotyk:bardzo; cialo:bardzo; potrzeba-zapewnienia:bardzo; droga-podroz:troche; kontrola-wizerunku:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000626','2026-09-03','taniec:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; schronienie:bardzo; dom:troche; ogien:bardzo; sensoryka-metafora:bardzo; cialo:troche; ku-komus:bardzo; czas:bardzo; odrodzenie:troche; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000627','2026-09-03','ciemnosc:bardzo; sen:bardzo; samotnosc:bardzo; komunikacja-problem:bardzo; niedopasowanie-spoleczne:bardzo; sensoryka-przytloczenie:bardzo; sensoryka-metafora:bardzo; noc:bardzo; intensywna-percepcja:bardzo; do-swiata:bardzo; pamiec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000628','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; milosc:bardzo; tesknota:bardzo; wina:bardzo; zal:bardzo; komunikacja-problem:bardzo; ku-komus:bardzo; od-kogos:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; droga-podroz:troche; cel-nieosiagniety:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000629','2026-09-03','pozadanie:bardzo; milosc:bardzo; ogien:bardzo; taniec:bardzo; cialo:bardzo; dotyk:bardzo; sensoryka-metafora:bardzo; sprzeczne-potrzeby:bardzo; bezsilnosc:bardzo; lek-antycypacyjny:troche; droga-podroz:bardzo; smierc:troche; wysokie-pobudzenie:bardzo; euforia-naped:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000630','2026-09-03','innosc:bardzo; niedopasowanie-spoleczne:bardzo; sprzeczne-potrzeby:troche; droga-podroz:bardzo; noc:bardzo; czas:bardzo; sensoryka-metafora:bardzo; do-siebie:bardzo; ku-przyszlosci:troche; zablokowanie:troche; dopasowanie-roli:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000631','2026-09-03','maska:bardzo; ukrywanie-reakcji:bardzo; sprzeczne-emocje:bardzo; milosc:bardzo; pozadanie:troche; dotyk:bardzo; komunikacja-problem:troche; ja-publiczne-ja-prywatne:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000632','2026-09-03','brak-nadziei:troche; nadzieja:bardzo; wyczerpanie:bardzo; brak-napedu:troche; bezwartosciowosc:troche; wstyd:bardzo; schronienie:bardzo; ulga-z-zewnatrz:bardzo; dom:bardzo; droga-podroz:bardzo; przemiana:bardzo; ku-przyszlosci:bardzo; woda:bardzo; zamartwianie:bardzo; przetrwanie:bardzo; samotnosc:troche; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000633','2026-09-03','utrata:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; smutek:bardzo; ulga-z-zewnatrz:bardzo; potrzeba-zapewnienia:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; od-kogos:bardzo; przemiana:bardzo; latanie-spadanie:troche; czas:bardzo; zal:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000634','2026-09-03','milosc:bardzo; maska:bardzo; kontrola-wizerunku:troche; wolnosc:bardzo; znikniecie:bardzo; prawda:bardzo; ku-komus:bardzo; wspomnienia:troche; ku-przeszlosci:troche; sprzeczne-emocje:troche; do-swiata:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000635','2026-09-03','utrata:bardzo; milosc:bardzo; od-kogos:bardzo; przemiana:bardzo; odrodzenie:troche; wolnosc:bardzo; sprawczosc:bardzo; czulosc:troche; zal:troche; wspomnienia:troche; czas:bardzo; latanie-spadanie:troche; spokoj:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000636','2026-09-03','marzenie:bardzo; utrata:bardzo; bezsilnosc:bardzo; brak-nadziei:bardzo; maska:bardzo; sprzeczne-potrzeby:troche; cialo:troche; przemiana:bardzo; smutek:bardzo; do-swiata:troche; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000637','2026-09-03','milosc:bardzo; utrata:bardzo; nic-pustka:bardzo; pustka-emocjonalna:bardzo; smutek:bardzo; zablokowanie:bardzo; czas:bardzo; noc:bardzo; bezsilnosc:bardzo; cel-nieosiagniety:bardzo; wyczerpanie:troche; ku-przeszlosci:troche; wspomnienia:troche; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000638','2026-09-03','bunt:bardzo; smierc:bardzo; ucieczka:bardzo; droga-podroz:bardzo; strach:bardzo; cialo:troche; ku-przyszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000639','2026-09-03','milosc:bardzo; pozadanie:bardzo; ogien:bardzo; ciemnosc:bardzo; noc:bardzo; cialo:bardzo; dotyk:bardzo; czulosc:bardzo; latanie-spadanie:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo; przemiana:bardzo; wystarczy:bardzo; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000640','2026-09-03','wysokie-pobudzenie:bardzo; sensoryka-przytloczenie:bardzo; unikanie-z-leku:bardzo; samotnosc:bardzo; noc:bardzo; rozpad:bardzo; cyklicznosc-wzorzec:bardzo; droga-podroz:bardzo; przemiana:bardzo; wyczerpanie:troche; ciemnosc:troche; lek-antycypacyjny:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000641','2026-09-03','pozadanie:bardzo; milosc:troche; droga-podroz:bardzo; ku-przyszlosci:bardzo; marzenie:bardzo; nadzieja:bardzo; smierc:bardzo; cialo:troche; samotnosc:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000642','2026-09-03','milosc:bardzo; tesknota:bardzo; ku-komus:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; cialo:bardzo; sensoryka-metafora:bardzo; smutek:bardzo; czulosc:troche; pozadanie:troche; zablokowanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000643','2026-09-03','milosc:bardzo; ucieczka:bardzo; latanie-spadanie:bardzo; droga-podroz:bardzo; wolnosc:bardzo; zablokowanie:bardzo; ciemnosc:bardzo; lek-antycypacyjny:troche; oddech-powietrze:bardzo; sprzeczne-potrzeby:bardzo; sensoryka-metafora:bardzo; wysokie-pobudzenie:bardzo; od-kogos:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000644','2026-09-03','droga-podroz:bardzo; ku-komus:bardzo; lek-antycypacyjny:troche; wysokie-pobudzenie:troche; sensoryka-metafora:bardzo; cel-nieosiagniety:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000645','2026-09-03','milosc:bardzo; droga-podroz:bardzo; ucieczka:bardzo; pogon:bardzo; ku-komus:bardzo; marzenie:bardzo; woda:bardzo; ku-przyszlosci:bardzo; sensoryka-metafora:bardzo; wolnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000646','2026-09-03','droga-podroz:bardzo; milosc:bardzo; ku-komus:bardzo; marzenie:bardzo; tesknota:bardzo; smierc:bardzo; odrodzenie:troche; sensoryka-metafora:bardzo; czas:bardzo; nadzieja:bardzo; latanie-spadanie:troche; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000647','2026-09-03','znikniecie:bardzo; rozpad:bardzo; deszcz:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo; wysokie-pobudzenie:troche; utrata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000648','2026-09-03','noc:bardzo; czas:bardzo; ku-przyszlosci:bardzo; marzenie:troche; lek-antycypacyjny:troche; milosc:troche; cyklicznosc-wzorzec:bardzo; wysokie-pobudzenie:troche; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000649','2026-09-03','milosc:bardzo; rutyna-repetycja:bardzo; cyklicznosc-wzorzec:bardzo; czulosc:troche; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000650','2026-09-03','droga-podroz:bardzo; ucieczka:bardzo; przemiana:bardzo; odrodzenie:bardzo; wspomnienia:bardzo; pamiec:troche; ku-przeszlosci:bardzo; ku-przyszlosci:bardzo; marzenie:bardzo; smutek:bardzo; zamartwianie:bardzo; sprzeczne-potrzeby:bardzo; zablokowanie:troche; deszcz:troche; od-kogos:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000651','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; sprzeczne-emocje:bardzo; milosc:bardzo; wina:bardzo; nic-pustka:bardzo; nierozpoznanie-siebie:bardzo; czas:bardzo; wolnosc:troche; zablokowanie:troche; od-kogos:troche; zobojetnienie:troche; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000652','2026-09-03','przemiana:bardzo; nierozpoznanie-siebie:troche; samotnosc:troche; czas:bardzo; smutek:troche; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000653','2026-09-03','milosc:bardzo; utrata:bardzo; przemiana:bardzo; od-kogos:bardzo; wyczerpanie:bardzo; maska:bardzo; czas:bardzo; smutek:bardzo; zal:troche; smierc:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000654','2026-09-03','milosc:bardzo; lek:bardzo; lek-antycypacyjny:troche; sprzeczne-emocje:bardzo; od-kogos:bardzo; utrata:bardzo; sprawczosc:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000655','2026-09-03','samotnosc:bardzo; deszcz:bardzo; smutek:bardzo; noc:bardzo; substancje:troche; substancja-regulacja:troche; spokoj:bardzo; od-swiata:bardzo; przetrwanie:troche; nadzieja:troche; sensoryka-szukanie:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000656','2026-09-03','milosc:bardzo; czulosc:bardzo; cialo:bardzo; smutek:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; komunikacja-problem:bardzo; ciemnosc:bardzo; rozpacz:troche; wina:troche; przetrwanie:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000657','2026-09-03','milosc:bardzo; woda:bardzo; ku-komus:bardzo; pogon:bardzo; sensoryka-metafora:bardzo; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000658','2026-09-03','milosc:bardzo; taniec:bardzo; noc:bardzo; sen:troche; marzenie:troche; wspomnienia:bardzo; ku-przeszlosci:bardzo; czulosc:bardzo; radosc:bardzo; ku-komus:bardzo; czas:bardzo; sensoryka-szukanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000659','2026-09-03','droga-podroz:bardzo; wspomnienia:bardzo; pamiec:bardzo; marzenie:bardzo; lek-antycypacyjny:bardzo; katastrofizacja:bardzo; czas:bardzo; utrata:bardzo; ogien:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo; od-kogos:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000660','2026-09-03','pamiec:bardzo; wspomnienia:troche; droga-podroz:bardzo; woda:bardzo; samotnosc-preferowana:bardzo; cialo:bardzo; przemiana:bardzo; nadzieja:bardzo; schronienie:bardzo; dom:bardzo; sensoryka-metafora:bardzo; czas:bardzo; przetrwanie:bardzo; od-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000661','2026-09-03','milosc:bardzo; ku-komus:bardzo; do-swiata:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; deszcz:troche; sensoryka-szukanie:bardzo; radosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000662','2026-09-03','pozadanie:bardzo; cialo:bardzo; dotyk:bardzo; pogon:bardzo; utrata:bardzo; smierc:troche; noc:troche; sensoryka-metafora:bardzo; ku-komus:bardzo; sprawczosc:bardzo; tesknota:troche; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000663','2026-09-03','smierc:bardzo; cialo:bardzo; milosc:bardzo; taniec:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; utrata:bardzo; smutek:bardzo; zal:bardzo; sprawczosc:bardzo; czulosc:bardzo; pogon:bardzo; droga-podroz:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000664','2026-09-03','smierc:bardzo; czas:bardzo; sen:bardzo; marzenie:bardzo; przemiana:bardzo; odrodzenie:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; sprzeczne-emocje:bardzo; sprawczosc:bardzo; lek-antycypacyjny:troche; nadzieja:bardzo; przetrwanie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000665','2026-09-03','nigdy-dosc:bardzo; euforia-naped:bardzo; cyklicznosc-wzorzec:bardzo; sen:bardzo; marzenie:bardzo; time-blindness:troche; nic-pustka:troche; innosc:bardzo; wysokie-pobudzenie:bardzo; intensywnosc-potem-crash:bardzo; przetrwanie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000666','2026-09-03','taniec:bardzo; pozadanie:bardzo; dotyk:bardzo; cialo:bardzo; noc:bardzo; woda:troche; sensoryka-szukanie:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; ku-komus:bardzo; czas:bardzo; sprzeczne-emocje:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000667','2026-09-03','wolnosc:bardzo; do-siebie:bardzo; nierozpoznanie-siebie:troche; prawda:bardzo; maska:bardzo; przemiana:bardzo; odrodzenie:troche; sprawczosc:bardzo; innosc:troche; ulga:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000783','2026-09-03','milosc:bardzo; ku-komus:bardzo; powrot-do:bardzo; droga-podroz:bardzo; komunikacja-problem:bardzo; czas:bardzo; sprzeczne-emocje:troche; prawda:troche; cel-nieosiagniety:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000668','2026-09-03','samotnosc:bardzo; ucieczka:bardzo; latanie-spadanie:bardzo; droga-podroz:bardzo; utrata:bardzo; ogien:bardzo; przemiana:bardzo; od-kogos:troche; sprawczosc:bardzo; ulga:troche; pamiec:bardzo; wycofanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000669','2026-09-03','smierc:bardzo; cyklicznosc-wzorzec:bardzo; przemiana:bardzo; odrodzenie:bardzo; czas:bardzo; utrata:bardzo; smutek:bardzo; do-swiata:bardzo; droga-podroz:troche; sensoryka-metafora:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000670','2026-09-03','sen:bardzo; marzenie:bardzo; noc:bardzo; droga-podroz:bardzo; prawda:bardzo; sensoryka-metafora:bardzo; czas:bardzo; sprawczosc:troche; ku-przyszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000671','2026-09-03','milosc:bardzo; utrata:bardzo; samotnosc:bardzo; smutek:bardzo; tesknota:bardzo; ku-przeszlosci:bardzo; ku-przyszlosci:bardzo; czas:bardzo; droga-podroz:bardzo; brak-nadziei:bardzo; od-kogos:bardzo; sensoryka-metafora:bardzo; pustka-emocjonalna:troche; cel-nieosiagniety:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000672','2026-09-03','od-kogos:bardzo; wolnosc:bardzo; zablokowanie:bardzo; sprzeczne-potrzeby:bardzo; samotnosc:bardzo; milosc:bardzo; wspomnienia:troche; droga-podroz:bardzo; sprawczosc:bardzo; przemiana:bardzo; nierozpoznanie-siebie:troche; sensoryka-metafora:bardzo; cyklicznosc-wzorzec:troche; ku-przeszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000673','2026-09-03','komunikacja-problem:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; pamiec:troche; utrata:bardzo; znikniecie:bardzo; wina:troche; sensoryka-metafora:bardzo; niepewnosc-nie-do-zniesienia:troche; prawda:troche; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000674','2026-09-03','sensoryka-przytloczenie:bardzo; od-swiata:bardzo; ucieczka:bardzo; droga-podroz:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; dom:bardzo; schronienie:bardzo; ulga-z-zewnatrz:bardzo; sensoryka-szukanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000675','2026-09-03','sen:bardzo; marzenie:bardzo; cialo:bardzo; nic-pustka:bardzo; bezsilnosc:bardzo; smierc:bardzo; czas:bardzo; lek-antycypacyjny:bardzo; ucieczka:bardzo; droga-podroz:bardzo; rozpad:bardzo; wysokie-pobudzenie:bardzo; do-swiata:bardzo; brak-nadziei:bardzo; cyklicznosc-wzorzec:bardzo; sensoryka-metafora:bardzo; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000676','2026-09-03','przemiana:bardzo; odrodzenie:troche; czas:bardzo; euforia-naped:troche; nadzieja:bardzo; substancje:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000677','2026-09-03','milosc:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; bunt:bardzo; substancje:bardzo; droga-podroz:bardzo; znikniecie:bardzo; duma:bardzo; wolnosc:troche; ku-komus:bardzo; do-swiata:bardzo; sprawczosc:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000678','2026-09-03','milosc:bardzo; samotnosc:bardzo; droga-podroz:bardzo; przemiana:bardzo; nadzieja:bardzo; potrzeba-zapewnienia:bardzo; ku-komus:bardzo; ku-przyszlosci:bardzo; wspomnienia:troche; czas:bardzo; zablokowanie:troche; sensoryka-metafora:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000679','2026-09-03','do-swiata:bardzo; gniew:bardzo; sensoryka-przytloczenie:bardzo; emocjonalna-dysregulacja:bardzo; niedopasowanie-spoleczne:bardzo; dopasowanie-roli:bardzo; zobojetnienie:bardzo; bezsilnosc:bardzo; bunt:bardzo; droga-podroz:troche; nadzieja:troche; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000680','2026-09-03','milosc:bardzo; czulosc:bardzo; ku-komus:bardzo; czas:bardzo; latanie-spadanie:bardzo; przetrwanie:bardzo; sensoryka-metafora:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000681','2026-09-03','droga-podroz:bardzo; ucieczka:bardzo; milosc:bardzo; utrata:bardzo; tesknota:bardzo; wspomnienia:bardzo; pamiec:troche; woda:bardzo; substancje:bardzo; substancja-regulacja:bardzo; noc:bardzo; smierc:bardzo; samotnosc:bardzo; nierozpoznanie-siebie:bardzo; ku-przeszlosci:bardzo; od-kogos:bardzo; bezsilnosc:troche; sensoryka-metafora:bardzo; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000682','2026-09-03','taniec:bardzo; radosc:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; do-swiata:bardzo; dotyk:bardzo; ulga:bardzo; cialo:troche; bunt:troche; wystarczy:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000683','2026-09-03','droga-podroz:bardzo; sprawczosc:bardzo; zablokowanie:troche; prawda:bardzo; samokontrola-spoleczna:troche; lek:troche; latanie-spadanie:troche; do-swiata:bardzo; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000684','2026-09-03','cialo:bardzo; substancje:bardzo; substancja-regulacja:troche; przetrwanie:bardzo; odrodzenie:bardzo; droga-podroz:bardzo; milosc:bardzo; oddech-powietrze:bardzo; sensoryka-szukanie:bardzo; sensoryka-metafora:bardzo; smierc:troche; radosc:bardzo; sprawczosc:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000685','2026-09-03','marzenie:bardzo; przemiana:bardzo; odrodzenie:troche; wolnosc:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; bunt:bardzo; droga-podroz:troche; sprawczosc:bardzo; duma:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; ku-przyszlosci:bardzo; przetrwanie:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000686','2026-09-03','utrata:bardzo; milosc:bardzo; tesknota:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; noc:bardzo; sen:bardzo; smutek:bardzo; zal:bardzo; od-kogos:bardzo; czas:bardzo; sensoryka-metafora:bardzo; dom:troche; dotyk:troche; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000687','2026-09-03','gniew:bardzo; wysokie-pobudzenie:bardzo; bunt:bardzo; do-swiata:bardzo; milosc:bardzo; sprawczosc:bardzo; sensoryka-metafora:bardzo; wstyd:troche; prawda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000688','2026-09-03','wstyd:bardzo; kontrola-wizerunku:bardzo; niedopasowanie-spoleczne:bardzo; substancje:troche; do-innych:bardzo; nierozpoznanie-siebie:troche; frustracja:bardzo; gniew:troche; komunikacja-problem:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000689','2026-09-03','kontrola-wizerunku:bardzo; performowanie-roli:bardzo; ja-publiczne-ja-prywatne:troche; milosc:troche; potrzeba-zapewnienia:bardzo; komunikacja-problem:troche; prawda:troche; sprawczosc:bardzo; ku-komus:troche; maska:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000690','2026-09-03','substancje:bardzo; pozadanie:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; cialo:bardzo; dotyk:troche; zablokowanie:bardzo; nigdy-dosc:bardzo; utrata:bardzo; bezsilnosc:bardzo; niskie-pobudzenie:bardzo; emocja-przez-cialo:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000691','2026-09-03','substancje:bardzo; pozadanie:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; cialo:bardzo; dotyk:troche; zablokowanie:bardzo; nigdy-dosc:bardzo; utrata:bardzo; bezsilnosc:bardzo; niskie-pobudzenie:bardzo; emocja-przez-cialo:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000692','2026-09-03','do-siebie:bardzo; nierozpoznanie-siebie:bardzo; prawda:bardzo; milosc:bardzo; komunikacja-problem:bardzo; kontrola-wizerunku:troche; sprawczosc:troche; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000693','2026-09-03','milosc:bardzo; cialo:bardzo; kontrola:bardzo; od-swiata:bardzo; nierozpoznanie-siebie:troche; wina:bardzo; bezsilnosc:bardzo; zablokowanie:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; samotnosc:bardzo; dotyk:troche; prawda:bardzo; sprzeczne-emocje:bardzo; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000694','2026-09-03','sen:bardzo; noc:bardzo; zablokowanie:bardzo; cialo:bardzo; lek:bardzo; sensoryka-przytloczenie:bardzo; zamartwianie:bardzo; przemiana:bardzo; droga-podroz:troche; wysokie-pobudzenie:bardzo; emocja-przez-cialo:bardzo; zamrozenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000695','2026-09-03','substancje:bardzo; pozadanie:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; cialo:bardzo; dotyk:troche; zablokowanie:bardzo; nigdy-dosc:bardzo; utrata:bardzo; bezsilnosc:bardzo; niskie-pobudzenie:bardzo; emocja-przez-cialo:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000696','2026-09-03','woda:bardzo; samotnosc-preferowana:bardzo; droga-podroz:bardzo; ucieczka:troche; sensoryka-szukanie:bardzo; sensoryka-metafora:bardzo; cialo:bardzo; wycofanie:bardzo; od-swiata:bardzo; latanie-spadanie:troche; bezsilnosc:troche; przemiana:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000697','2026-09-03','latanie-spadanie:bardzo; wolnosc:bardzo; droga-podroz:bardzo; od-swiata:bardzo; komunikacja-problem:bardzo; smierc:bardzo; cialo:troche; wysokie-pobudzenie:bardzo; zablokowanie:bardzo; przemiana:bardzo; samotnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000698','2026-09-03','przemiana:bardzo; odrodzenie:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; droga-podroz:bardzo; cialo:bardzo; taniec:bardzo; sprzeczne-potrzeby:bardzo; milosc:bardzo; utrata:bardzo; radosc:bardzo; sprawczosc:bardzo; czas:bardzo; substancje:troche; czulosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000699','2026-09-03','do-swiata:bardzo; gniew:bardzo; bunt:bardzo; komunikacja-problem:bardzo; prawda:troche; sprawczosc:bardzo; ogien:bardzo; wysokie-pobudzenie:bardzo; cyklicznosc-wzorzec:bardzo; do-innych:bardzo; frustracja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000700','2026-09-03','smierc:bardzo; milosc:bardzo; ku-komus:bardzo; czulosc:bardzo; dotyk:bardzo; potrzeba-zapewnienia:bardzo; ulga-z-zewnatrz:bardzo; ogien:bardzo; ciemnosc:bardzo; smutek:bardzo; lek-antycypacyjny:bardzo; cialo:bardzo; czas:bardzo; sensoryka-metafora:bardzo; schronienie:bardzo; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000701','2026-09-03','marzenie:bardzo; droga-podroz:bardzo; zablokowanie:bardzo; milosc:bardzo; dotyk:bardzo; oddech-powietrze:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; intensywna-percepcja:bardzo; sensoryka-metafora:bardzo; ku-przyszlosci:bardzo; cel-nieosiagniety:troche; latanie-spadanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000702','2026-09-03','marzenie:bardzo; wolnosc:bardzo; bezsilnosc:bardzo; nierozpoznanie-siebie:bardzo; niedopasowanie-spoleczne:bardzo; do-siebie:bardzo; gniew:bardzo; smutek:bardzo; przemiana:bardzo; utrata:bardzo; komunikacja-problem:bardzo; sensoryka-metafora:bardzo; prawda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000703','2026-09-03','droga-podroz:bardzo; odrodzenie:bardzo; przemiana:bardzo; sprawczosc:bardzo; przetrwanie:bardzo; cialo:bardzo; smierc:troche; strach:troche; ku-przyszlosci:bardzo; sensoryka-metafora:bardzo; czas:bardzo; bunt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000704','2026-09-03','cialo:bardzo; woda:bardzo; sensoryka-metafora:bardzo; rutyna-repetycja:bardzo; ulga:bardzo; spokoj:bardzo; sensoryka-szukanie:bardzo; marzenie:bardzo; ku-komus:troche; sprawczosc:bardzo; przemiana:bardzo; odrodzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000705','2026-09-03','milosc:bardzo; sprzeczne-potrzeby:bardzo; ja-publiczne-ja-prywatne:bardzo; nierozpoznanie-siebie:bardzo; maska:bardzo; potrzeba-zapewnienia:bardzo; ulga-z-zewnatrz:bardzo; samotnosc:bardzo; ku-komus:bardzo; od-kogos:bardzo; zablokowanie:bardzo; komunikacja-problem:bardzo; prawda:bardzo; kontrola-wizerunku:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000706','2026-09-03','pozadanie:bardzo; milosc:bardzo; cialo:bardzo; emocja-przez-cialo:bardzo; ku-komus:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; cyklicznosc-wzorzec:bardzo; spokoj:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000707','2026-09-03','milosc:bardzo; ku-komus:bardzo; cyklicznosc-wzorzec:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; czas:bardzo; niepewnosc-nie-do-zniesienia:troche; pozadanie:troche; bunt:troche; innosc:troche; kontrola:troche; sprawczosc:troche; tesknota:bardzo; ku-przyszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000708','2026-09-03','milosc:bardzo; pozadanie:bardzo; nigdy-dosc:bardzo; noc:bardzo; ciemnosc:bardzo; ku-komus:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000776','2026-09-03','substancje:bardzo; substancja-regulacja:bardzo; dom:bardzo; strach:troche; do-swiata:bardzo; cialo:troche; cyklicznosc-wzorzec:bardzo; sensoryka-przytloczenie:troche; zablokowanie:bardzo; rutyna-repetycja:bardzo; frustracja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000709','2026-09-03','smierc:bardzo; utrata:bardzo; smutek:bardzo; rozpacz:bardzo; gniew:bardzo; wysokie-pobudzenie:bardzo; sprawczosc:bardzo; bezsilnosc:bardzo; cialo:bardzo; milosc:bardzo; do-innych:bardzo; przetrwanie:troche; emocjonalna-dysregulacja:bardzo; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000710','2026-09-03','zazdrosc:bardzo; kontrola:bardzo; potrzeba-zapewnienia:bardzo; lek-antycypacyjny:bardzo; milosc:bardzo; pozadanie:bardzo; sprzeczne-emocje:bardzo; ku-komus:bardzo; nigdy-dosc:bardzo; przemiana:bardzo; wspomnienia:troche; ku-przeszlosci:troche; zablokowanie:bardzo; wstyd:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000711','2026-09-03','sen:bardzo; marzenie:bardzo; noc:bardzo; ciemnosc:bardzo; strach:bardzo; lek:bardzo; sprzeczne-emocje:bardzo; utrata:bardzo; przemiana:bardzo; odrodzenie:troche; dotyk:bardzo; sensoryka-metafora:bardzo; zablokowanie:bardzo; emocja-przez-cialo:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000712','2026-09-03','sen:bardzo; komunikacja-problem:bardzo; prawda:bardzo; ucieczka:bardzo; droga-podroz:bardzo; maska:bardzo; wolnosc:bardzo; bunt:bardzo; sprawczosc:bardzo; ogien:bardzo; wysokie-pobudzenie:bardzo; do-swiata:bardzo; strach:troche; przemiana:bardzo; odrodzenie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000713','2026-09-03','milosc:bardzo; pozadanie:bardzo; samotnosc:bardzo; noc:bardzo; bezsennosc-restless:bardzo; substancje:troche; lek-antycypacyjny:troche; niepewnosc-nie-do-zniesienia:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo; woda:bardzo; ogien:bardzo; wysokie-pobudzenie:bardzo; cialo:troche; sprzeczne-emocje:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000714','2026-09-03','milosc:bardzo; samotnosc:bardzo; czulosc:bardzo; czas:bardzo; taniec:bardzo; ku-komus:bardzo; ukrywanie-reakcji:troche; dotyk:troche; smutek:troche; sensoryka-metafora:bardzo; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000715','2026-09-03','milosc:bardzo; ukrywanie-reakcji:bardzo; potrzeba-zapewnienia:troche; schronienie:bardzo; ulga-z-zewnatrz:bardzo; woda:bardzo; droga-podroz:bardzo; czulosc:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo; lek-antycypacyjny:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000716','2026-09-03','od-kogos:bardzo; ucieczka:bardzo; droga-podroz:bardzo; milosc:troche; przemiana:bardzo; odrodzenie:bardzo; znikniecie:troche; prawda:bardzo; cel-nieosiagniety:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000717','2026-09-03','cialo:bardzo; zablokowanie:bardzo; taniec:bardzo; milosc:bardzo; strach:bardzo; wstyd:bardzo; performowanie-roli:bardzo; ja-publiczne-ja-prywatne:troche; komunikacja-problem:bardzo; ciemnosc:bardzo; noc:bardzo; wolnosc:bardzo; do-siebie:bardzo; przemiana:bardzo; sensoryka-metafora:bardzo; emocja-przez-cialo:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000718','2026-09-03','ucieczka:bardzo; droga-podroz:bardzo; nigdy-dosc:bardzo; milosc:bardzo; cel-nieosiagniety:troche; sprzeczne-potrzeby:troche; bezsilnosc:troche; prawda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000719','2026-09-03','pamiec:bardzo; utrata:bardzo; milosc:bardzo; ukrywanie-reakcji:bardzo; komunikacja-problem:bardzo; wyczerpanie:troche; czas:bardzo; marzenie:bardzo; brak-nadziei:troche; nadzieja:troche; sprzeczne-emocje:troche; cyklicznosc-wzorzec:troche; niskie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000720','2026-09-03','od-kogos:bardzo; wolnosc:bardzo; droga-podroz:bardzo; noc:bardzo; ciemnosc:bardzo; ucieczka:bardzo; wspomnienia:bardzo; pamiec:bardzo; czas:bardzo; cel-nieosiagniety:bardzo; sprawczosc:bardzo; ku-przeszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000721','2026-09-03','performowanie-roli:bardzo; dopasowanie-roli:bardzo; maska:bardzo; ucieczka:bardzo; znikniecie:bardzo; sprzeczne-potrzeby:bardzo; dotyk:bardzo; noc:bardzo; milosc:bardzo; pozadanie:troche; smierc:bardzo; dom:bardzo; niedopasowanie-spoleczne:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000722','2026-09-03','intensywna-percepcja:bardzo; sensoryka-szukanie:bardzo; sensoryka-metafora:bardzo; nie-wiem-co-czuje:bardzo; marzenie:bardzo; ogien:bardzo; deszcz:bardzo; cialo:bardzo; wysokie-pobudzenie:bardzo; nadzieja:bardzo; pozadanie:troche; radosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000723','2026-09-03','taniec:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; radosc:bardzo; do-siebie:bardzo; wolnosc:bardzo; cialo:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000724','2026-09-03','taniec:bardzo; maska:bardzo; smierc:bardzo; cyklicznosc-wzorzec:bardzo; strach:bardzo; brak-nadziei:bardzo; czas:bardzo; dom:troche; cialo:bardzo; do-swiata:bardzo; sensoryka-metafora:bardzo; wysokie-pobudzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000725','2026-09-03','milosc:bardzo; impulsywnosc:bardzo; nigdy-dosc:bardzo; maska:bardzo; kontrola-wizerunku:bardzo; performowanie-roli:bardzo; ja-publiczne-ja-prywatne:bardzo; noc:bardzo; ciemnosc:bardzo; pozadanie:troche; wysokie-pobudzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000726','2026-09-03','zablokowanie:bardzo; nierozpoznanie-siebie:troche; ulga-z-zewnatrz:bardzo; spokoj:bardzo; czulosc:bardzo; dotyk:bardzo; woda:bardzo; deszcz:bardzo; przetrwanie:bardzo; ciemnosc:bardzo; gniew:bardzo; frustracja:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000727','2026-09-03','pogon:bardzo; cel-nieosiagniety:bardzo; milosc:bardzo; pozadanie:bardzo; cyklicznosc-wzorzec:bardzo; nigdy-dosc:bardzo; sprzeczne-potrzeby:bardzo; sprawczosc:bardzo; przetrwanie:bardzo; ku-komus:bardzo; rutyna-repetycja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000728','2026-09-03','nic-pustka:bardzo; strach:bardzo; wstyd:bardzo; nadzieja:bardzo; przemiana:bardzo; odrodzenie:bardzo; prawda:bardzo; wolnosc:bardzo; do-siebie:bardzo; sprawczosc:bardzo; przetrwanie:bardzo; droga-podroz:bardzo; sensoryka-metafora:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000729','2026-09-03','czas:bardzo; milosc:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; dotyk:bardzo; czulosc:bardzo; ku-komus:bardzo; smierc:troche; nadzieja:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000730','2026-09-03','radosc:bardzo; ucieczka:bardzo; schronienie:troche; substancje:troche; substancja-regulacja:troche; przemiana:bardzo; odrodzenie:bardzo; przetrwanie:bardzo; droga-podroz:bardzo; wysokie-pobudzenie:bardzo; milosc:bardzo; tesknota:bardzo; od-kogos:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000731','2026-09-03','milosc:bardzo; wina:bardzo; zal:bardzo; potrzeba-zapewnienia:bardzo; ku-komus:bardzo; powrot-do:bardzo; komunikacja-problem:troche; sprzeczne-emocje:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000732','2026-09-03','milosc:bardzo; pozadanie:bardzo; dotyk:bardzo; czulosc:bardzo; wystarczy:bardzo; ku-komus:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000733','2026-09-03','przemiana:bardzo; odrodzenie:bardzo; sprawczosc:bardzo; marzenie:bardzo; ogien:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; duma:bardzo; wolnosc:bardzo; ku-przyszlosci:bardzo; radosc:bardzo; bunt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000734','2026-09-03','wstyd:bardzo; maskowanie:bardzo; kontrola-wizerunku:bardzo; ja-publiczne-ja-prywatne:bardzo; niedopasowanie-spoleczne:bardzo; innosc:bardzo; ucieczka:bardzo; do-siebie:bardzo; wolnosc:bardzo; bunt:bardzo; duma:bardzo; strach:bardzo; przemiana:bardzo; odrodzenie:bardzo; performowanie-roli:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000735','2026-09-03','deszcz:bardzo; woda:bardzo; latanie-spadanie:bardzo; przemiana:bardzo; marzenie:bardzo; intensywna-percepcja:bardzo; sensoryka-metafora:bardzo; nierozpoznanie-siebie:bardzo; do-siebie:bardzo; do-swiata:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000736','2026-09-03','brak-napedu:bardzo; wycofanie:bardzo; niskie-pobudzenie:bardzo; smutek:bardzo; melancholia:bardzo; ciemnosc:bardzo; czas:bardzo; deszcz:troche; sensoryka-przytloczenie:bardzo; schronienie:bardzo; nadzieja:bardzo; ulga-odroczona:bardzo; zablokowanie:bardzo; tesknota:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000737','2026-09-03','do-siebie:bardzo; prawda:bardzo; sprawczosc:troche; bezsilnosc:troche; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000738','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; utrata:bardzo; przetrwanie:bardzo; wyczerpanie:bardzo; smierc-wlasna:bardzo; cialo:bardzo; czas:bardzo; zal:bardzo; czulosc:bardzo; bezsilnosc:bardzo; sprzeczne-potrzeby:bardzo; niskie-pobudzenie:troche; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000739','2026-09-03','ucieczka:bardzo; przetrwanie:bardzo; dom:bardzo; substancje:bardzo; substancja-regulacja:bardzo; zamartwianie:bardzo; hiperczujnosc:bardzo; lek-antycypacyjny:bardzo; do-swiata:bardzo; bezsilnosc:troche; sprawczosc:bardzo; wolnosc:bardzo; droga-podroz:bardzo; cialo:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000740','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; czas:bardzo; tesknota:bardzo; czulosc:troche; sensoryka-szukanie:bardzo; nadzieja:bardzo; utrata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000741','2026-09-03','chaos-balagan:bardzo; nierozpoznanie-siebie:bardzo; intensywna-percepcja:bardzo; sensoryka-metafora:bardzo; rozpad:bardzo; wysokie-pobudzenie:troche; cialo:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000742','2026-09-03','wolnosc:bardzo; przemiana:bardzo; odrodzenie:bardzo; sen:bardzo; marzenie:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; utrata:bardzo; zal:bardzo; do-swiata:bardzo; wspomnienia:troche; czas:bardzo; milosc:troche; ulga:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000743','2026-09-03','milosc:bardzo; pozadanie:bardzo; gniew:bardzo; kontrola:bardzo; sprawdzanie:bardzo; potrzeba-zapewnienia:bardzo; komunikacja-problem:bardzo; ogien:bardzo; ciemnosc:bardzo; woda:bardzo; sensoryka-metafora:bardzo; niepewnosc-nie-do-zniesienia:bardzo; niemoznosc-odpuszczenia:bardzo; lek-antycypacyjny:troche; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000744','2026-09-03','noc:bardzo; sen:bardzo; droga-podroz:bardzo; latanie-spadanie:bardzo; milosc:bardzo; ogien:bardzo; przetrwanie:bardzo; smierc:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo; czas:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000745','2026-09-03','substancje:bardzo; taniec:bardzo; performowanie-roli:bardzo; kontrola-wizerunku:bardzo; ja-publiczne-ja-prywatne:bardzo; maska:bardzo; do-swiata:bardzo; cialo:troche; czas:bardzo; sensoryka-przytloczenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000746','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; wina:bardzo; samotnosc:bardzo; noc:bardzo; milosc:bardzo; tesknota:bardzo; droga-podroz:bardzo; sensoryka-metafora:bardzo; czas:bardzo; sprzeczne-potrzeby:bardzo; spokoj:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000747','2026-09-03','milosc:bardzo; czulosc:bardzo; dotyk:bardzo; pozadanie:troche; sensoryka-szukanie:bardzo; marzenie:troche; radosc:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000094','2026-09-03','czas:bardzo; ku-przeszlosci:bardzo; wspomnienia:bardzo; milosc:bardzo; sen:bardzo; substancje:bardzo; substancja-regulacja:bardzo; smutek:bardzo; pozadanie:bardzo; taniec:bardzo; cialo:bardzo; impulsywnosc:troche; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000113','2026-09-03','strach:bardzo; sensoryka-przytloczenie:bardzo; pogon:bardzo; sen:bardzo; dom:bardzo; znikniecie:bardzo; tesknota:bardzo; samotnosc:bardzo; przetrwanie:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; czas:bardzo; czulosc:bardzo; potrzeba-zapewnienia:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000166','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; ku-przyszlosci:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; milosc:bardzo; tesknota:bardzo; sprzeczne-potrzeby:bardzo; sprzeczne-emocje:bardzo; strach:bardzo; komunikacja-problem:bardzo; wina:bardzo; zal:bardzo; emocja-przez-cialo:bardzo; od-kogos:bardzo; ku-komus:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000258','2026-09-03','sprzeczne-emocje:bardzo; radosc:troche; smutek:troche; wspomnienia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000345','2026-09-03','milosc:bardzo; utrata:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; tesknota:bardzo; substancje:bardzo; substancja-regulacja:troche; zal:bardzo; potrzeba-zapewnienia:bardzo; sprzeczne-emocje:bardzo; od-kogos:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000418','2026-09-03','zobojetnienie:bardzo; utrata:bardzo; smutek:bardzo; zal:bardzo; wina:bardzo; wstyd:troche; czas:bardzo; ku-przyszlosci:bardzo; od-kogos:bardzo; sprzeczne-emocje:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000423','2026-09-03','przemiana:bardzo; ku-komus:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000430','2026-09-03','droga-podroz:bardzo; woda:bardzo; pozadanie:bardzo; substancje:bardzo; sprawczosc:bardzo; wysokie-pobudzenie:troche; cyklicznosc-wzorzec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000433','2026-09-03','marzenie:bardzo; ku-przeszlosci:bardzo; czas:bardzo; milosc:bardzo; czulosc:bardzo; dom:bardzo; woda:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000456','2026-09-03','samotnosc:bardzo; wyczerpanie:bardzo; substancje:bardzo; substancja-regulacja:bardzo; ucieczka:bardzo; droga-podroz:bardzo; marzenie:bardzo; maska:bardzo; wolnosc:bardzo; smutek:bardzo; schronienie:bardzo; od-swiata:bardzo; nadzieja:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000748','2026-09-03','dom:bardzo; samotnosc:bardzo; schronienie:bardzo; bezsennosc-restless:bardzo; brak-napedu:bardzo; wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; smierc:bardzo; utrata:bardzo; smutek:bardzo; sen:bardzo; komunikacja-problem:bardzo; prawda:troche; woda:bardzo; przetrwanie:bardzo; czulosc:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000749','2026-09-03','strach:bardzo; lek-antycypacyjny:bardzo; samotnosc:bardzo; droga-podroz:bardzo; ucieczka:bardzo; wolnosc:bardzo; od-kogos:bardzo; milosc:bardzo; tesknota:bardzo; noc:bardzo; woda:troche; sprawczosc:bardzo; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000750','2026-09-03','wspomnienia:bardzo; ku-przeszlosci:bardzo; czas:bardzo; milosc:bardzo; utrata:bardzo; zal:bardzo; wina:troche; smierc-wlasna:bardzo; samotnosc:bardzo; performowanie-roli:bardzo; dopasowanie-roli:bardzo; cialo:bardzo; pozadanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000751','2026-09-03','noc:bardzo; substancje:troche; sensoryka-przytloczenie:bardzo; sensoryka-szukanie:bardzo; cialo:bardzo; utrata:bardzo; bezsilnosc:bardzo; droga-podroz:bardzo; emocja-przez-cialo:bardzo; wysokie-pobudzenie:bardzo; do-swiata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000752','2026-09-03','ucieczka:bardzo; droga-podroz:bardzo; milosc:bardzo; ku-komus:bardzo; czulosc:troche; noc:bardzo; ciemnosc:bardzo; czas:bardzo; taniec:bardzo; przetrwanie:troche; sensoryka-metafora:bardzo; sprzeczne-potrzeby:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000753','2026-09-03','ucieczka:bardzo; droga-podroz:bardzo; wolnosc:bardzo; bunt:bardzo; innosc:bardzo; niedopasowanie-spoleczne:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; sprawczosc:bardzo; ku-przyszlosci:bardzo; radosc:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000754','2026-09-03','milosc:bardzo; ku-komus:bardzo; droga-podroz:bardzo; ogien:bardzo; euforia-naped:troche; sensoryka-szukanie:bardzo; innosc:troche; czas:bardzo; sprawczosc:bardzo; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000755','2026-09-03','cialo:bardzo; oddech-powietrze:bardzo; sen:bardzo; woda:bardzo; ucieczka:bardzo; lek-antycypacyjny:bardzo; strach:bardzo; sensoryka-metafora:bardzo; bezsilnosc:troche; milosc:bardzo; sprzeczne-potrzeby:bardzo; ku-komus:bardzo; wysokie-pobudzenie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000756','2026-09-03','tesknota:bardzo; milosc:troche; samotnosc:bardzo; cyklicznosc-wzorzec:bardzo; strach:bardzo; ku-przeszlosci:bardzo; wspomnienia:bardzo; czas:bardzo; droga-podroz:bardzo; sensoryka-metafora:bardzo; prawda:bardzo; zablokowanie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000757','2026-09-03','wolnosc:bardzo; milosc:bardzo; od-kogos:bardzo; prawda:bardzo; sprzeczne-potrzeby:bardzo; samotnosc:bardzo; sprawczosc:bardzo; przemiana:bardzo; odrodzenie:troche; zablokowanie:bardzo; ku-przyszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000758','2026-09-03','prawda:bardzo; ucieczka:bardzo; smierc:bardzo; wina:bardzo; zal:bardzo; cialo:bardzo; strach:bardzo; samotnosc:bardzo; bezsilnosc:bardzo; rozpacz:bardzo; znikniecie:bardzo; sprzeczne-emocje:bardzo; wysokie-pobudzenie:bardzo; sprawczosc:bardzo; od-kogos:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000759','2026-09-03','niedopasowanie-spoleczne:bardzo; innosc:bardzo; bunt:bardzo; do-swiata:bardzo; gniew:troche; smierc-wlasna:bardzo; czas:bardzo; duma:bardzo; komunikacja-problem:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000760','2026-09-03','kontrola:bardzo; sprawdzanie:bardzo; hiperczujnosc:bardzo; niemoznosc-odpuszczenia:bardzo; milosc:bardzo; zazdrosc:troche; utrata:bardzo; tesknota:bardzo; noc:bardzo; sen:bardzo; ku-komus:bardzo; lek-antycypacyjny:troche; potrzeba-zapewnienia:bardzo; cyklicznosc-wzorzec:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000761','2026-09-03','droga-podroz:bardzo; cel-nieosiagniety:bardzo; marzenie:bardzo; niepewnosc-nie-do-zniesienia:troche; prawda:bardzo; przemiana:bardzo; odrodzenie:bardzo; ku-przyszlosci:bardzo; nadzieja:bardzo; sensoryka-metafora:bardzo; do-swiata:bardzo; czas:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000762','2026-09-03','zazdrosc:bardzo; gniew:bardzo; smierc:bardzo; ucieczka:bardzo; droga-podroz:bardzo; wolnosc:bardzo; sprawczosc:bardzo; od-kogos:bardzo; wysokie-pobudzenie:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000763','2026-09-03','sensoryka-przytloczenie:bardzo; wysokie-pobudzenie:bardzo; lek:bardzo; strach:bardzo; bezsilnosc:bardzo; zablokowanie:bardzo; milosc:bardzo; do-swiata:bardzo; przemiana:bardzo; nadzieja:bardzo; ulga-odroczona:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000765','2026-09-03','innosc:bardzo; niedopasowanie-spoleczne:bardzo; samotnosc:bardzo; wycofanie:bardzo; deszcz:bardzo; smutek:troche; znikniecie:bardzo; sensoryka-metafora:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000766','2026-09-03','gniew:bardzo; strach:bardzo; cialo:bardzo; sensoryka-przytloczenie:bardzo; substancje:troche; maska:bardzo; powrot-do:bardzo; milosc:bardzo; znikniecie:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000767','2026-09-03','komunikacja-problem:bardzo; gniew:bardzo; zal:bardzo; do-swiata:bardzo; smierc:bardzo; brak-nadziei:bardzo; katastrofizacja:bardzo; woda:bardzo; czas:bardzo; zablokowanie:bardzo; rozpad:bardzo; bezsilnosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000768','2026-09-03','bezsilnosc:bardzo; zamartwianie:bardzo; przeciazenie-przyszloscia:bardzo; potrzeba-zapewnienia:bardzo; ulga-z-zewnatrz:bardzo; substancje:bardzo; substancja-regulacja:bardzo; wyczerpanie:bardzo; cialo:bardzo; droga-podroz:bardzo; przetrwanie:bardzo; smutek:bardzo; brak-nadziei:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000769','2026-09-03','smierc:bardzo; lek-antycypacyjny:bardzo; hiperczujnosc:bardzo; ucieczka:bardzo; droga-podroz:bardzo; wysokie-pobudzenie:bardzo; ukrywanie-reakcji:bardzo; substancje:troche; sprawczosc:bardzo; do-innych:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000770','2026-09-03','prawda:bardzo; milosc:bardzo; czulosc:bardzo; dotyk:bardzo; wolnosc:bardzo; cialo:bardzo; smierc:bardzo; odrodzenie:bardzo; przemiana:bardzo; do-siebie:bardzo; sprawczosc:bardzo; sprzeczne-emocje:troche; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000771','2026-09-03','noc:bardzo; substancje:bardzo; taniec:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; gniew:bardzo; impulsywnosc:bardzo; do-innych:bardzo; strach:troche; ogien:bardzo; cialo:troche; euforia-naped:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000772','2026-09-03','milosc:bardzo; pozadanie:bardzo; cialo:bardzo; ogien:bardzo; intensywna-percepcja:bardzo; sensoryka-szukanie:bardzo; ku-komus:bardzo; rutyna-repetycja:bardzo; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000773','2026-09-03','cialo:bardzo; ziemia:bardzo; ulga-z-zewnatrz:bardzo; sensoryka-metafora:bardzo; rutyna-repetycja:bardzo; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000778','2026-09-03','substancje:bardzo; utrata:bardzo; zazdrosc:bardzo; smutek:bardzo; tesknota:bardzo; milosc:bardzo; wspomnienia:bardzo; pamiec:bardzo; droga-podroz:bardzo; samotnosc:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000782','2026-09-03','niepewnosc-nie-do-zniesienia:bardzo; kontrola:bardzo; niedopasowanie-spoleczne:bardzo; sprzeczne-potrzeby:bardzo; hiperczujnosc:bardzo; przeciazenie-przyszloscia:bardzo; zablokowanie:bardzo; komunikacja-problem:troche; zamartwianie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000785','2026-09-03','latanie-spadanie:bardzo; impulsywnosc:bardzo; sensoryka-szukanie:bardzo; wysokie-pobudzenie:bardzo; euforia-naped:bardzo; cyklicznosc-wzorzec:bardzo; sprzeczne-potrzeby:bardzo; czas:bardzo; marzenie:bardzo; sprawczosc:bardzo; bunt:troche; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000788','2026-09-03','wspomnienia:bardzo; pamiec:bardzo; ku-przeszlosci:bardzo; melancholia:bardzo; smutek:bardzo; tesknota:bardzo; utrata:bardzo; samotnosc:bardzo; droga-podroz:bardzo; powrot-do:bardzo; czas:bardzo; woda:bardzo; sensoryka-szukanie:bardzo; nadzieja:troche; znikniecie:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000797','2026-09-06','substancje:bardzo; substancja-regulacja:bardzo; prawda:bardzo; bunt:bardzo; do-swiata:bardzo; frustracja:bardzo; gniew:troche; zobojetnienie:troche; sprawdzanie:troche; bezsilnosc:troche; dosc-przesyt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000798','2026-09-06','taniec:bardzo; samotnosc:bardzo; smutek:bardzo; zal:bardzo; tesknota:bardzo; sprzeczne-emocje:bardzo; ku-swiatu:troche; radosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000799','2026-09-06','hiperfokus:bardzo; nuda-nietolerancja:bardzo; nigdy-dosc:bardzo; cyklicznosc-wzorzec:bardzo; intensywnosc-potem-crash:troche; substancje:troche; substancja-regulacja:troche; prawda:bardzo; kontrola-wizerunku:troche; do-swiata:bardzo; bunt:bardzo; sprawczosc:bardzo; pogon:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000800','2026-09-06','woda:bardzo; droga-podroz:bardzo; schronienie:bardzo; przetrwanie:bardzo; dotarcie:bardzo; ucieczka:troche; ciemnosc:bardzo; nadzieja:troche; ulga-z-zewnatrz:bardzo; bezsilnosc:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000801','2026-09-06','ukrywanie-reakcji:bardzo; komunikacja-problem:bardzo; milosc:troche; kontrola:bardzo; kontrola-wizerunku:troche; ku-przeszlosci:troche; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000802','2026-09-06','droga-podroz:bardzo; smierc:bardzo; smierc-wlasna:bardzo; latanie-spadanie:bardzo; ziemia:bardzo; rozpad:bardzo; zobojetnienie:bardzo; do-swiata:bardzo; sprawczosc:bardzo; wysokie-pobudzenie:troche; nic-pustka:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000803','2026-09-06','przetrwanie:bardzo; przemiana:bardzo; odrodzenie:bardzo; sprawczosc:bardzo; duma:bardzo; radosc:bardzo; nadzieja:bardzo; wolnosc:bardzo; od-kogos:bardzo; ku-swiatu:bardzo; ulga:bardzo; utrata:troche; smutek:troche; bunt:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000804','2026-09-06','milosc:bardzo; czulosc:bardzo; dotyk:bardzo; cialo:troche; odrodzenie:bardzo; ku-komus:bardzo; radosc:troche; nadzieja:troche; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000805','2026-09-06','niedopasowanie-spoleczne:bardzo; wina:bardzo; smutek:bardzo; lek:bardzo; zamartwianie:bardzo; hiperczujnosc:bardzo; bezsilnosc:bardzo; zablokowanie:bardzo; wyczerpanie:bardzo; do-siebie:bardzo; do-innych:troche; wstyd:troche; rozpacz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000806','2026-09-06','ucieczka:bardzo; samotnosc-preferowana:bardzo; droga-podroz:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; noc:bardzo; ciemnosc:bardzo; sen:troche; od-swiata:bardzo; wycofanie:bardzo; utrata:troche; melancholia:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000807','2026-09-06','intensywna-percepcja:bardzo; cialo:bardzo; taniec:bardzo; sensoryka-metafora:bardzo; ku-komus:bardzo; ku-swiatu:bardzo; wysokie-pobudzenie:troche; radosc:troche; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000808','2026-09-06','woda:bardzo; droga-podroz:bardzo; gniew:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; smutek:bardzo; zal:bardzo; utrata:bardzo; marzenie:bardzo; sensoryka-metafora:bardzo; ucieczka:troche; intensywna-percepcja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000809','2026-09-06','wspomnienia:bardzo; ku-przeszlosci:bardzo; milosc:bardzo; czulosc:bardzo; droga-podroz:bardzo; woda:bardzo; ogien:troche; smierc-wlasna:troche; samotnosc:bardzo; tesknota:bardzo; noc:bardzo; ciemnosc:bardzo; bezsennosc:troche; ku-komus:bardzo; dotyk:troche; schronienie:troche; czas:bardzo; komunikacja-problem:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000810','2026-09-06','samotnosc:bardzo; substancje:bardzo; substancja-regulacja:troche; noc:bardzo; woda:bardzo; sensoryka-metafora:bardzo; latanie-spadanie:troche; cel-nieosiagniety:bardzo; zablokowanie:bardzo; bezsilnosc:bardzo; melancholia:bardzo; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000811','2026-09-06','maska:bardzo; performowanie-roli:bardzo; ja-publiczne-ja-prywatne:bardzo; kontrola-wizerunku:bardzo; nierozpoznanie-siebie:troche; lek:bardzo; wycofanie:bardzo; od-swiata:troche; ukrywanie-reakcji:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000812','2026-09-06','smutek:bardzo; wina:bardzo; bezsilnosc:troche; sprzeczne-emocje:bardzo; ukrywanie-reakcji:bardzo; dosc-przesyt:bardzo; do-innych:bardzo; cialo:bardzo; smierc:troche; przetrwanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000813','2026-09-06','strach:bardzo; lek-antycypacyjny:bardzo; katastrofizacja:bardzo; ciemnosc:bardzo; noc:bardzo; bezsilnosc:bardzo; wysokie-pobudzenie:bardzo; woda:troche; cyklicznosc-wzorzec:bardzo; brak-nadziei:bardzo; do-swiata:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000814','2026-09-06','wolnosc:bardzo; czas:troche; smierc:troche; czulosc:troche; innosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000815','2026-09-06','dom:bardzo; radosc:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; odrodzenie:bardzo; ziemia:bardzo; cyklicznosc-wzorzec:bardzo; ku-swiatu:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000816','2026-09-06','czulosc:bardzo; milosc:troche; spokoj:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000817','2026-09-06','wina:bardzo; przemiana:bardzo; odrodzenie:bardzo; nadzieja:bardzo; ku-komus:bardzo; ulga-z-zewnatrz:bardzo; sprawczosc:bardzo; czulosc:troche; spokoj:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000818','2026-09-06','droga-podroz:bardzo; utrata:bardzo; tesknota:bardzo; smutek:bardzo; melancholia:bardzo; bezsilnosc:bardzo; brak-nadziei:bardzo; ziemia:bardzo; dom:bardzo; milosc:bardzo; cialo:troche; noc:troche; od-kogos:bardzo; sprawczosc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000819','2026-09-06','milosc:bardzo; czulosc:bardzo; pozadanie:bardzo; cialo:bardzo; seks:troche; substancje:bardzo; radosc:bardzo; ku-komus:bardzo; sprawczosc:bardzo; noc:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000820','2026-09-06','wspomnienia:bardzo; ku-przeszlosci:bardzo; utrata:bardzo; tesknota:bardzo; milosc:bardzo; smutek:bardzo; melancholia:bardzo; rozpacz:troche; brak-nadziei:bardzo; dotyk:bardzo; czas:bardzo; ku-komus:bardzo; od-kogos:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000821','2026-09-06','smutek:bardzo; czulosc:bardzo; milosc:bardzo; nadzieja:bardzo; ku-komus:bardzo; do-innych:troche; schronienie:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000822','2026-09-06','pozadanie:bardzo; seks:bardzo; ku-komus:bardzo; sprawczosc:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000823','2026-09-06','sprawczosc:bardzo; kontrola:bardzo; wina:bardzo; do-innych:bardzo; do-swiata:bardzo; smierc:bardzo; gniew:troche; ciemnosc:troche; nadzieja:troche; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000824','2026-09-06','taniec:bardzo; radosc:bardzo; euforia-naped:bardzo; wysokie-pobudzenie:bardzo; sensoryka-szukanie:bardzo; duma:bardzo; ku-swiatu:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000877','2026-09-06','spokoj:bardzo; sprawczosc:bardzo; czas:bardzo; sen:troche; sensoryka-metafora:bardzo; prawda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000878','2026-09-06','schronienie:bardzo; przetrwanie:bardzo; droga-podroz:bardzo; woda:bardzo; ogien:bardzo; nadzieja:bardzo; ulga-z-zewnatrz:bardzo; dotarcie:bardzo; ku-przyszlosci:bardzo; spokoj:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000879','2026-09-06','nic-pustka:bardzo; prawda:bardzo; wolnosc:bardzo; przemiana:bardzo; droga-podroz:bardzo; dotarcie:bardzo; ulga:bardzo; spokoj:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000880','2026-09-06','pamiec:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; milosc:troche; tesknota:troche; droga-podroz:troche; wstyd:bardzo; czas:bardzo; cyklicznosc-wzorzec:bardzo; przemiana:bardzo; od-kogos:bardzo; ku-komus:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000881','2026-09-06','woda:bardzo; utrata:bardzo; milosc:bardzo; wina:bardzo; smierc:bardzo; smierc-wlasna:bardzo; droga-podroz:bardzo; latanie-spadanie:bardzo; bezsilnosc:bardzo; pamiec:bardzo; marzenie:troche; noc:troche; sensoryka-metafora:bardzo; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000882','2026-09-06','nic-pustka:bardzo; pozadanie:bardzo; milosc:troche; utrata:troche; substancje:troche; taniec:troche; sprzeczne-emocje:bardzo; sprzeczne-potrzeby:troche; wina:troche; wspomnienia:troche; ucieczka:ociupinke; noc:ociupinke');

INSERT INTO tag_snapshots VALUES('lyrics-000827','2026-09-06','utrata:bardzo; milosc:bardzo; smutek:bardzo; melancholia:bardzo; zal:bardzo; wspomnienia:bardzo; pamiec:troche; prawda:bardzo; od-kogos:bardzo; ku-przeszlosci:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000828','2026-09-06','pozadanie:bardzo; milosc:troche; czulosc:troche; ku-komus:bardzo; sprawczosc:bardzo; wolnosc:bardzo; cialo:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000829','2026-09-06','smutek:bardzo; samotnosc:bardzo; substancje:bardzo; substancja-regulacja:bardzo; ucieczka:bardzo; nic-pustka:bardzo; ulga-z-zewnatrz:bardzo; ku-komus:bardzo; sen:troche; nadzieja:troche; brak-nadziei:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000830','2026-09-06','smierc:bardzo; smierc-wlasna:bardzo; strach:bardzo; lek-antycypacyjny:bardzo; wina:bardzo; potrzeba-zapewnienia:bardzo; schronienie:bardzo; ulga-z-zewnatrz:bardzo; ku-przyszlosci:bardzo; ku-komus:bardzo; nadzieja:troche; zamartwianie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000831','2026-09-06','lek:bardzo; spokoj:bardzo; ulga:bardzo; przemiana:bardzo; wygaszanie:bardzo; schronienie:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000832','2026-09-06','milosc:bardzo; bezsilnosc:bardzo; czas:bardzo; emocjonalna-dysregulacja:bardzo; wysokie-pobudzenie:troche; zablokowanie:troche; rozpad:troche; sprzeczne-potrzeby:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000833','2026-09-06','milosc:bardzo; cialo:bardzo; dotyk:bardzo; czulosc:bardzo; pozadanie:troche; zaraz-minie:bardzo; lek-antycypacyjny:bardzo; katastrofizacja:bardzo; schronienie:bardzo; ku-komus:bardzo; sprzeczne-emocje:bardzo; czas:troche; sensoryka-metafora:troche; woda:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000834','2026-09-06','samotnosc:bardzo; spokoj:bardzo; woda:bardzo; ziemia:bardzo; oddech-powietrze:bardzo; czas:bardzo; od-swiata:bardzo; sensoryka-metafora:bardzo; droga-podroz:troche; nadzieja:troche; nic-pustka:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000835','2026-09-06','bezsilnosc:bardzo; zablokowanie:bardzo; woda:bardzo; lek-antycypacyjny:troche; ku-przyszlosci:troche; niepewnosc-nie-do-zniesienia:troche; przetrwanie:troche; frustracja:troche; sensoryka-metafora:bardzo; droga-podroz:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000836','2026-09-06','utrata:bardzo; smutek:bardzo; melancholia:bardzo; nic-pustka:bardzo; sen:troche; wyczerpanie:bardzo; odrodzenie:bardzo; przemiana:bardzo; nadzieja:bardzo; ulga-odroczona:bardzo; do-siebie:bardzo; czas:bardzo; ku-przyszlosci:bardzo; tesknota:troche; od-kogos:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000837','2026-09-06','droga-podroz:bardzo; wolnosc:bardzo; ku-swiatu:bardzo; sprawczosc:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000838','2026-09-06','gniew:bardzo; frustracja:bardzo; bunt:bardzo; do-innych:bardzo; do-swiata:troche; lek:troche; sprawczosc:bardzo; ku-swiatu:bardzo; wysokie-pobudzenie:bardzo; przemiana:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000839','2026-09-06','droga-podroz:bardzo; woda:bardzo; wina:bardzo; utrata:bardzo; strach:bardzo; marzenie:bardzo; kontrola:bardzo; sprawczosc:bardzo; pamiec:bardzo; smierc:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000840','2026-09-06','milosc:bardzo; tesknota:bardzo; czulosc:bardzo; smutek:troche; melancholia:troche; ku-komus:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000841','2026-09-06','melancholia:bardzo; spokoj:bardzo; niskie-pobudzenie:bardzo; czas:bardzo; wspomnienia:troche; ku-przeszlosci:troche; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000842','2026-09-06','gniew:bardzo; wysokie-pobudzenie:bardzo; do-swiata:troche; sensoryka-metafora:bardzo; strach:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000843','2026-09-06','ogien:bardzo; gniew:bardzo; wysokie-pobudzenie:bardzo; sensoryka-metafora:bardzo; bunt:troche; ku-swiatu:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000844','2026-09-06','strach:bardzo; smierc:bardzo; czas:bardzo; ogien:bardzo; woda:troche; sensoryka-metafora:bardzo; intensywna-percepcja:bardzo; sensoryka-przytloczenie:bardzo; bezsilnosc:troche; sprawczosc:troche; wina:troche; ku-komus:bardzo; przemiana:bardzo; ulga:bardzo; ulga-z-zewnatrz:bardzo; spokoj:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000845','2026-09-06','schronienie:bardzo; spokoj:bardzo; czulosc:bardzo; ku-komus:bardzo; sensoryka-metafora:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000846','2026-09-06','ziemia:bardzo; radosc:bardzo; spokoj:bardzo; ku-swiatu:bardzo; przemiana:bardzo; sensoryka-metafora:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000847','2026-09-06','noc:bardzo; pamiec:bardzo; wspomnienia:troche; czulosc:bardzo; pozadanie:bardzo; ogien:bardzo; znikniecie:bardzo; zaraz-minie:bardzo; ku-komus:bardzo; czas:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000848','2026-09-06','zazdrosc:bardzo; wina:troche; wolnosc:bardzo; przemiana:bardzo; sprawczosc:bardzo; ku-swiatu:bardzo; sensoryka-metafora:bardzo; odrodzenie:troche; nadzieja:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000849','2026-09-06','zamartwianie:bardzo; niepewnosc-nie-do-zniesienia:bardzo; zablokowanie:bardzo; komunikacja-problem:bardzo; ku-komus:bardzo; prawda:bardzo; lek:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000850','2026-09-06','wspomnienia:bardzo; ku-przeszlosci:bardzo; czas:bardzo; utrata:bardzo; znikniecie:bardzo; wolnosc:troche; melancholia:bardzo; tesknota:bardzo; powrot-do:troche; przemiana:bardzo; bezsilnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000851','2026-09-06','milosc:bardzo; tesknota:bardzo; utrata:bardzo; powrot-do:bardzo; ku-komus:bardzo; droga-podroz:bardzo; przemiana:bardzo; sprzeczne-emocje:bardzo; bezsilnosc:troche; czas:troche; melancholia:troche; cel-nieosiagniety:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000852','2026-09-06','wspomnienia:bardzo; tesknota:bardzo; utrata:bardzo; ogien:bardzo; woda:troche; sensoryka-metafora:bardzo; rozpad:bardzo; powrot-do:bardzo; ku-komus:bardzo; droga-podroz:bardzo; milosc:troche; bezsilnosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000853','2026-09-06','utrata:bardzo; zal:bardzo; od-kogos:bardzo; ku-komus:troche; sprzeczne-emocje:bardzo; sprawczosc:bardzo; czulosc:troche; milosc:troche; ucieczka:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000854','2026-09-06','latanie-spadanie:bardzo; rozpad:bardzo; bezsilnosc:bardzo; wysokie-pobudzenie:bardzo; eskalacja:bardzo; emocjonalna-dysregulacja:bardzo; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000855','2026-09-06','wolnosc:bardzo; droga-podroz:bardzo; innosc:bardzo; samotnosc:bardzo; sprzeczne-potrzeby:bardzo; ku-swiatu:bardzo; sprawczosc:bardzo; bunt:troche; niedopasowanie-spoleczne:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000856','2026-09-06','przetrwanie:bardzo; sprawczosc:bardzo; droga-podroz:bardzo; przemiana:bardzo; nadzieja:bardzo; latanie-spadanie:bardzo; sensoryka-metafora:bardzo; ku-swiatu:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000857','2026-09-06','utrata:bardzo; milosc:bardzo; tesknota:bardzo; smutek:bardzo; rozpacz:troche; nic-pustka:bardzo; nierozpoznanie-siebie:bardzo; samotnosc:troche; oddech-powietrze:bardzo; bezsilnosc:troche; ku-przeszlosci:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000858','2026-09-06','wspomnienia:bardzo; ku-przeszlosci:bardzo; milosc:troche; pozadanie:troche; substancje:troche; ucieczka:troche; sprzeczne-emocje:bardzo; emocja-z-opoznieniem:bardzo; zazdrosc:troche; smutek:troche; prawda:troche; cyklicznosc-wzorzec:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000859','2026-09-06','nierozpoznanie-siebie:bardzo; do-siebie:bardzo; ku-komus:bardzo; prawda:troche; niepewnosc-nie-do-zniesienia:troche; czuje-bez-nazwy:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000860','2026-09-06','innosc:bardzo; wolnosc:bardzo; bunt:bardzo; sprawczosc:bardzo; performowanie-roli:troche; dopasowanie-roli:troche; marzenie:troche; duma:troche; ku-swiatu:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000861','2026-09-06','marzenie:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; prawda:troche; niepewnosc-nie-do-zniesienia:troche; spokoj:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000862','2026-09-06','spokoj:bardzo; ku-przyszlosci:bardzo; czas:bardzo; wspomnienia:troche; nadzieja:troche; marzenie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000863','2026-09-06','czulosc:bardzo; pamiec:bardzo; wspomnienia:troche; ku-przeszlosci:bardzo; czas:troche; milosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000864','2026-09-06','przetrwanie:bardzo; duma:bardzo; sprawczosc:bardzo; droga-podroz:troche; nadzieja:troche; wyczerpanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000865','2026-09-06','komunikacja-problem:bardzo; sprzeczne-potrzeby:bardzo; zablokowanie:bardzo; czuje-bez-nazwy:bardzo; wycofanie:troche; ku-komus:troche; od-kogos:troche; czulosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000866','2026-09-06','pustka-emocjonalna:bardzo; nierozpoznanie-siebie:bardzo; przemiana:bardzo; odrodzenie:troche; ogien:bardzo; sensoryka-metafora:bardzo; niskie-pobudzenie:bardzo; do-siebie:bardzo; czas:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000867','2026-09-07','ucieczka:bardzo; wina:bardzo; strach:bardzo; ku-przeszlosci:troche; do-siebie:bardzo; sensoryka-metafora:bardzo; sprawczosc:troche; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000868','2026-09-07','woda:bardzo; ziemia:bardzo; intensywna-percepcja:bardzo; radosc:bardzo; ku-swiatu:bardzo; duma:troche; sensoryka-metafora:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000869','2026-09-07','ciemnosc:bardzo; smutek:bardzo; zamartwianie:bardzo; zablokowanie:bardzo; sensoryka-metafora:bardzo; ku-swiatu:troche; sprawczosc:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000870','2026-09-07','odrodzenie:bardzo; przemiana:bardzo; radosc:bardzo; cialo:bardzo; intensywna-percepcja:bardzo; ku-swiatu:bardzo; euforia-naped:troche; sensoryka-szukanie:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000871','2026-09-07','droga-podroz:bardzo; ku-przyszlosci:bardzo; lek-antycypacyjny:bardzo; lek:bardzo; sprzeczne-emocje:bardzo; przemiana:bardzo; ku-swiatu:bardzo; sprawczosc:bardzo; nadzieja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000872','2026-09-07','ukrywanie-reakcji:bardzo; sprawczosc:bardzo; ku-swiatu:bardzo; wysokie-pobudzenie:bardzo; eskalacja:bardzo; bunt:troche; sensoryka-metafora:bardzo; komunikacja-problem:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000873','2026-09-07','marzenie:bardzo; wspomnienia:bardzo; ku-przeszlosci:bardzo; wolnosc:bardzo; bezsilnosc:troche; powrot-do:troche; czas:bardzo; sprzeczne-potrzeby:bardzo; przemiana:troche; utrata:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000874','2026-09-07','radosc:bardzo; wolnosc:bardzo; ku-swiatu:bardzo; czas:bardzo; euforia-naped:bardzo; czulosc:troche; intensywna-percepcja:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000875','2026-09-07','komunikacja-problem:bardzo; ja-publiczne-ja-prywatne:bardzo; prawda:bardzo; niedopasowanie-spoleczne:troche; ku-komus:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000876','2026-09-07','ogien:bardzo; dom:bardzo; strach:bardzo; prawda:bardzo; kontrola:bardzo; do-swiata:bardzo; cyklicznosc-wzorzec:bardzo; chaos-balagan:bardzo; sensoryka-metafora:bardzo; przetrwanie:troche; ku-komus:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000826','2026-09-07','dom:bardzo; ziemia:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; czas:bardzo; przemiana:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000429','2026-09-07','ziemia:bardzo; smierc:bardzo; przetrwanie:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; odrodzenie:bardzo; dom:bardzo; powrot-do:bardzo; ulga-odroczona:bardzo; czas:bardzo; wspomnienia:bardzo; smutek:bardzo; radosc:bardzo; sprzeczne-emocje:bardzo; ku-swiatu:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000586','2026-09-07','taniec:bardzo; radosc:bardzo; bunt:bardzo; wolnosc:bardzo; milosc:bardzo; ku-komus:bardzo; cialo:bardzo; seks:troche; sprawczosc:bardzo; gniew:troche; do-innych:bardzo');

INSERT INTO tag_snapshots VALUES('lyrics-000764','2026-09-07','marzenie:bardzo; tesknota:bardzo; droga-podroz:bardzo; schronienie:bardzo; cel-nieosiagniety:bardzo; melancholia:bardzo; smutek:troche; ucieczka:troche; ku-przyszlosci:troche');

INSERT INTO tag_snapshots VALUES('lyrics-000825','2026-09-07','dom:bardzo; radosc:bardzo; nadzieja:bardzo; ku-przyszlosci:bardzo; odrodzenie:bardzo; ziemia:bardzo; cyklicznosc-wzorzec:bardzo; ku-swiatu:bardzo');

