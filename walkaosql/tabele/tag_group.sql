-- tabela: tag_group
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS tag_group (
  tag TEXT NOT NULL REFERENCES tag_catalog(tag),
  group_name TEXT NOT NULL REFERENCES tag_groups(group_name),
  PRIMARY KEY (tag, group_name)
);

INSERT INTO tag_group VALUES('sensoryka-przytloczenie','asd');

INSERT INTO tag_group VALUES('sensoryka-szukanie','asd');

INSERT INTO tag_group VALUES('niedopasowanie-spoleczne','asd');

INSERT INTO tag_group VALUES('maskowanie','asd');

INSERT INTO tag_group VALUES('komunikacja-problem','asd');

INSERT INTO tag_group VALUES('samotnosc-preferowana','asd');

INSERT INTO tag_group VALUES('alexithymia','asd');

INSERT INTO tag_group VALUES('shutdown-meltdown','asd');

INSERT INTO tag_group VALUES('sensoryka-metafora','asd');

INSERT INTO tag_group VALUES('intensywna-percepcja','asd');

INSERT INTO tag_group VALUES('performowanie-roli','asd');

INSERT INTO tag_group VALUES('rutyna-repetycja','asd');

INSERT INTO tag_group VALUES('specjalne-zainteresowanie-osoba','asd');

INSERT INTO tag_group VALUES('racing-thoughts','adhd');

INSERT INTO tag_group VALUES('impulsywnosc','adhd');

INSERT INTO tag_group VALUES('time-blindness','adhd');

INSERT INTO tag_group VALUES('dysfunkcja-wykonawcza','adhd');

INSERT INTO tag_group VALUES('hiperfokus','adhd');

INSERT INTO tag_group VALUES('bezsennosc-restless','adhd');

INSERT INTO tag_group VALUES('emocjonalna-dysregulacja','adhd');

INSERT INTO tag_group VALUES('substancja-regulacja','adhd');

INSERT INTO tag_group VALUES('nuda-nietolerancja','adhd');

INSERT INTO tag_group VALUES('intensywnosc-potem-crash','adhd');

INSERT INTO tag_group VALUES('zapominanie-gubienie','adhd');

INSERT INTO tag_group VALUES('chaos-balagan','adhd');

INSERT INTO tag_group VALUES('sprzeczne-potrzeby','audhd');

INSERT INTO tag_group VALUES('wyczerpanie-maska','audhd');

INSERT INTO tag_group VALUES('za-duzo-i-za-malo','audhd');

INSERT INTO tag_group VALUES('podwojna-samotnosc','audhd');

INSERT INTO tag_group VALUES('cyklicznosc-wzorzec','audhd');

INSERT INTO tag_group VALUES('demand-avoidance','audhd');

INSERT INTO tag_group VALUES('milosc','motywy-tresciowe');

INSERT INTO tag_group VALUES('cialo','motywy-tresciowe');

INSERT INTO tag_group VALUES('seks','motywy-tresciowe');

INSERT INTO tag_group VALUES('samotnosc','motywy-tresciowe');

INSERT INTO tag_group VALUES('ciemnosc','motywy-tresciowe');

INSERT INTO tag_group VALUES('noc','motywy-tresciowe');

INSERT INTO tag_group VALUES('maska','motywy-tresciowe');

INSERT INTO tag_group VALUES('substancje','motywy-tresciowe');

INSERT INTO tag_group VALUES('ucieczka','motywy-tresciowe');

INSERT INTO tag_group VALUES('ogien','motywy-tresciowe');

INSERT INTO tag_group VALUES('wolnosc','motywy-tresciowe');

INSERT INTO tag_group VALUES('innosc','motywy-tresciowe');

INSERT INTO tag_group VALUES('nic-pustka','motywy-tresciowe');

INSERT INTO tag_group VALUES('mocne-kobiety','motywy-tresciowe');

INSERT INTO tag_group VALUES('gniew','motywy-tresciowe');

INSERT INTO tag_group VALUES('czas','motywy-tresciowe');

INSERT INTO tag_group VALUES('woda','motywy-tresciowe');

INSERT INTO tag_group VALUES('dotyk','motywy-tresciowe');

INSERT INTO tag_group VALUES('dom','motywy-tresciowe');

INSERT INTO tag_group VALUES('tesknota','motywy-tresciowe');

INSERT INTO tag_group VALUES('bunt','motywy-tresciowe');

INSERT INTO tag_group VALUES('smierc','motywy-tresciowe');

INSERT INTO tag_group VALUES('taniec','motywy-tresciowe');

INSERT INTO tag_group VALUES('latanie-spadanie','motywy-tresciowe');

INSERT INTO tag_group VALUES('prawda','motywy-tresciowe');

INSERT INTO tag_group VALUES('oddech-powietrze','motywy-tresciowe');

INSERT INTO tag_group VALUES('ziemia','motywy-tresciowe');

INSERT INTO tag_group VALUES('deszcz','motywy-tresciowe');

INSERT INTO tag_group VALUES('sen','motywy-tresciowe');

INSERT INTO tag_group VALUES('marzenie','motywy-tresciowe');

INSERT INTO tag_group VALUES('droga-podroz','motywy-tresciowe');

INSERT INTO tag_group VALUES('przemiana','motywy-tresciowe');

INSERT INTO tag_group VALUES('odrodzenie','motywy-tresciowe');

INSERT INTO tag_group VALUES('wspomnienia','motywy-tresciowe');

INSERT INTO tag_group VALUES('pamiec','motywy-tresciowe');

INSERT INTO tag_group VALUES('ulga','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('spokoj','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('ulga-odroczona','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('ulga-utracona','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('ulga-z-zewnatrz','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('schronienie','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('dotarcie','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('cel-nieosiagniety','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('pogon','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('powrot-do','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('wystarczy','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('nigdy-dosc','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('dosc-przesyt','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('euforia-naped','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('zaraz-minie','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('przetrwanie','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('utrata','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('przez-szczescie','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('bezsilnosc','regulacja-ruch-cel-nasycenie-ciaglosc-sprawczosc');

INSERT INTO tag_group VALUES('anhedonia','depresyjnosc');

INSERT INTO tag_group VALUES('brak-nadziei','depresyjnosc');

INSERT INTO tag_group VALUES('bezwartosciowosc','depresyjnosc');

INSERT INTO tag_group VALUES('wina','depresyjnosc');

INSERT INTO tag_group VALUES('wycofanie','depresyjnosc');

INSERT INTO tag_group VALUES('brak-napedu','depresyjnosc');

INSERT INTO tag_group VALUES('wyczerpanie','depresyjnosc');

INSERT INTO tag_group VALUES('zobojetnienie','depresyjnosc');

INSERT INTO tag_group VALUES('pustka-emocjonalna','depresyjnosc');

INSERT INTO tag_group VALUES('spowolnienie','depresyjnosc');

INSERT INTO tag_group VALUES('bezsennosc','depresyjnosc');

INSERT INTO tag_group VALUES('nadmierny-sen','depresyjnosc');

INSERT INTO tag_group VALUES('smierc-wlasna','depresyjnosc');

INSERT INTO tag_group VALUES('znikniecie','depresyjnosc');

INSERT INTO tag_group VALUES('zamartwianie','lek-gad');

INSERT INTO tag_group VALUES('lek-antycypacyjny','lek-gad');

INSERT INTO tag_group VALUES('katastrofizacja','lek-gad');

INSERT INTO tag_group VALUES('hiperczujnosc','lek-gad');

INSERT INTO tag_group VALUES('niepewnosc-nie-do-zniesienia','lek-gad');

INSERT INTO tag_group VALUES('kontrola','lek-gad');

INSERT INTO tag_group VALUES('sprawdzanie','lek-gad');

INSERT INTO tag_group VALUES('potrzeba-zapewnienia','lek-gad');

INSERT INTO tag_group VALUES('napiecie-ciala','lek-gad');

INSERT INTO tag_group VALUES('niemoznosc-odpuszczenia','lek-gad');

INSERT INTO tag_group VALUES('unikanie-z-leku','lek-gad');

INSERT INTO tag_group VALUES('zamrozenie','lek-gad');

INSERT INTO tag_group VALUES('przeciazenie-przyszloscia','lek-gad');

INSERT INTO tag_group VALUES('samokontrola-spoleczna','maskowanie');

INSERT INTO tag_group VALUES('ukrywanie-reakcji','maskowanie');

INSERT INTO tag_group VALUES('ukrywanie-potrzeb','maskowanie');

INSERT INTO tag_group VALUES('dopasowanie-roli','maskowanie');

INSERT INTO tag_group VALUES('nasladowanie','maskowanie');

INSERT INTO tag_group VALUES('skryptowanie','maskowanie');

INSERT INTO tag_group VALUES('analiza-po-kontakcie','maskowanie');

INSERT INTO tag_group VALUES('analiza-przed-kontaktem','maskowanie');

INSERT INTO tag_group VALUES('kontrola-wizerunku','maskowanie');

INSERT INTO tag_group VALUES('maskowanie-koszt','maskowanie');

INSERT INTO tag_group VALUES('rozpad-po-masce','maskowanie');

INSERT INTO tag_group VALUES('ja-publiczne-ja-prywatne','maskowanie');

INSERT INTO tag_group VALUES('nierozpoznanie-siebie','maskowanie');

INSERT INTO tag_group VALUES('do-siebie','kierunek');

INSERT INTO tag_group VALUES('do-innych','kierunek');

INSERT INTO tag_group VALUES('do-swiata','kierunek');

INSERT INTO tag_group VALUES('ku-przeszlosci','kierunek');

INSERT INTO tag_group VALUES('ku-przyszlosci','kierunek');

INSERT INTO tag_group VALUES('ku-komus','kierunek');

INSERT INTO tag_group VALUES('od-kogos','kierunek');

INSERT INTO tag_group VALUES('ku-swiatu','kierunek');

INSERT INTO tag_group VALUES('od-swiata','kierunek');

INSERT INTO tag_group VALUES('wysokie-pobudzenie','pobudzenie-dynamika-sprawczosc');

INSERT INTO tag_group VALUES('niskie-pobudzenie','pobudzenie-dynamika-sprawczosc');

INSERT INTO tag_group VALUES('eskalacja','pobudzenie-dynamika-sprawczosc');

INSERT INTO tag_group VALUES('wygaszanie','pobudzenie-dynamika-sprawczosc');

INSERT INTO tag_group VALUES('zablokowanie','pobudzenie-dynamika-sprawczosc');

INSERT INTO tag_group VALUES('rozpad','pobudzenie-dynamika-sprawczosc');

INSERT INTO tag_group VALUES('sprawczosc','pobudzenie-dynamika-sprawczosc');

INSERT INTO tag_group VALUES('wiem-co-czuje','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('nie-wiem-co-czuje','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('czuje-bez-nazwy','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('emocja-przez-cialo','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('emocja-z-opoznieniem','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('emocja-przez-skutek','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('emocja-przez-innego','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('sprzeczne-emocje','dostep-do-wlasnej-emocji');

INSERT INTO tag_group VALUES('smutek','emocja-afekt');

INSERT INTO tag_group VALUES('melancholia','emocja-afekt');

INSERT INTO tag_group VALUES('radosc','emocja-afekt');

INSERT INTO tag_group VALUES('lek','emocja-afekt');

INSERT INTO tag_group VALUES('strach','emocja-afekt');

INSERT INTO tag_group VALUES('wstyd','emocja-afekt');

INSERT INTO tag_group VALUES('wstret','emocja-afekt');

INSERT INTO tag_group VALUES('zazdrosc','emocja-afekt');

INSERT INTO tag_group VALUES('nadzieja','emocja-afekt');

INSERT INTO tag_group VALUES('rozpacz','emocja-afekt');

INSERT INTO tag_group VALUES('czulosc','emocja-afekt');

INSERT INTO tag_group VALUES('pozadanie','emocja-afekt');

INSERT INTO tag_group VALUES('frustracja','emocja-afekt');

INSERT INTO tag_group VALUES('nuda','emocja-afekt');

INSERT INTO tag_group VALUES('zal','emocja-afekt');

INSERT INTO tag_group VALUES('duma','emocja-afekt');

