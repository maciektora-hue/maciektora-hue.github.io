-- tabela: tag_axis
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS tag_axis (
  tag TEXT NOT NULL REFERENCES tag_catalog(tag),
  axis_name TEXT NOT NULL REFERENCES axes(axis_name),
  PRIMARY KEY (tag, axis_name)
);

INSERT INTO tag_axis VALUES('sensoryka-przytloczenie','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('sensoryka-przytloczenie','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('sensoryka-szukanie','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('sensoryka-szukanie','nasycenie/naped');

INSERT INTO tag_axis VALUES('niedopasowanie-spoleczne','relacja/spoleczne');

INSERT INTO tag_axis VALUES('maskowanie','maskowanie');

INSERT INTO tag_axis VALUES('maskowanie','relacja/spoleczne');

INSERT INTO tag_axis VALUES('komunikacja-problem','relacja/spoleczne');

INSERT INTO tag_axis VALUES('samotnosc-preferowana','relacja/spoleczne');

INSERT INTO tag_axis VALUES('samotnosc-preferowana','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('alexithymia','dostep-do-emocji');

INSERT INTO tag_axis VALUES('shutdown-meltdown','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('shutdown-meltdown','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('sensoryka-metafora','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('intensywna-percepcja','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('performowanie-roli','maskowanie');

INSERT INTO tag_axis VALUES('performowanie-roli','relacja/spoleczne');

INSERT INTO tag_axis VALUES('rutyna-repetycja','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('rutyna-repetycja','czas/ciaglosc');

INSERT INTO tag_axis VALUES('specjalne-zainteresowanie-osoba','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('specjalne-zainteresowanie-osoba','relacja/spoleczne');

INSERT INTO tag_axis VALUES('racing-thoughts','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('racing-thoughts','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('impulsywnosc','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('impulsywnosc','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('time-blindness','czas/ciaglosc');

INSERT INTO tag_axis VALUES('time-blindness','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('dysfunkcja-wykonawcza','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('dysfunkcja-wykonawcza','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('hiperfokus','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('hiperfokus','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('bezsennosc-restless','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('bezsennosc-restless','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('emocjonalna-dysregulacja','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('emocjonalna-dysregulacja','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('substancja-regulacja','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('substancja-regulacja','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('nuda-nietolerancja','nasycenie/naped');

INSERT INTO tag_axis VALUES('nuda-nietolerancja','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('intensywnosc-potem-crash','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('intensywnosc-potem-crash','czas/ciaglosc');

INSERT INTO tag_axis VALUES('zapominanie-gubienie','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('chaos-balagan','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('chaos-balagan','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('sprzeczne-potrzeby','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('sprzeczne-potrzeby','kierunek');

INSERT INTO tag_axis VALUES('wyczerpanie-maska','maskowanie');

INSERT INTO tag_axis VALUES('wyczerpanie-maska','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('za-duzo-i-za-malo','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('za-duzo-i-za-malo','nasycenie/naped');

INSERT INTO tag_axis VALUES('za-duzo-i-za-malo','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('podwojna-samotnosc','relacja/spoleczne');

INSERT INTO tag_axis VALUES('podwojna-samotnosc','kierunek');

INSERT INTO tag_axis VALUES('cyklicznosc-wzorzec','czas/ciaglosc');

INSERT INTO tag_axis VALUES('cyklicznosc-wzorzec','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('demand-avoidance','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('demand-avoidance','kierunek');

INSERT INTO tag_axis VALUES('milosc','tresc/motyw');

INSERT INTO tag_axis VALUES('milosc','relacja/spoleczne');

INSERT INTO tag_axis VALUES('milosc','emocja/afekt');

INSERT INTO tag_axis VALUES('cialo','tresc/motyw');

INSERT INTO tag_axis VALUES('cialo','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('cialo','cialo');

INSERT INTO tag_axis VALUES('seks','tresc/motyw');

INSERT INTO tag_axis VALUES('seks','cialo');

INSERT INTO tag_axis VALUES('samotnosc','tresc/motyw');

INSERT INTO tag_axis VALUES('samotnosc','relacja/spoleczne');

INSERT INTO tag_axis VALUES('ciemnosc','tresc/motyw');

INSERT INTO tag_axis VALUES('ciemnosc','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('noc','tresc/motyw');

INSERT INTO tag_axis VALUES('noc','czas/ciaglosc');

INSERT INTO tag_axis VALUES('maska','tresc/motyw');

INSERT INTO tag_axis VALUES('maska','maskowanie');

INSERT INTO tag_axis VALUES('substancje','tresc/motyw');

INSERT INTO tag_axis VALUES('substancje','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('ucieczka','tresc/motyw');

INSERT INTO tag_axis VALUES('ucieczka','ruch/cel');

INSERT INTO tag_axis VALUES('ucieczka','kierunek');

INSERT INTO tag_axis VALUES('ogien','tresc/motyw');

INSERT INTO tag_axis VALUES('ogien','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('wolnosc','tresc/motyw');

INSERT INTO tag_axis VALUES('wolnosc','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('innosc','tresc/motyw');

INSERT INTO tag_axis VALUES('innosc','relacja/spoleczne');

INSERT INTO tag_axis VALUES('nic-pustka','tresc/motyw');

INSERT INTO tag_axis VALUES('mocne-kobiety','tresc/motyw');

INSERT INTO tag_axis VALUES('gniew','tresc/motyw');

INSERT INTO tag_axis VALUES('gniew','kierunek');

INSERT INTO tag_axis VALUES('gniew','emocja/afekt');

INSERT INTO tag_axis VALUES('czas','tresc/motyw');

INSERT INTO tag_axis VALUES('czas','czas/ciaglosc');

INSERT INTO tag_axis VALUES('woda','tresc/motyw');

INSERT INTO tag_axis VALUES('woda','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('dotyk','tresc/motyw');

INSERT INTO tag_axis VALUES('dotyk','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('dotyk','relacja/spoleczne');

INSERT INTO tag_axis VALUES('dotyk','cialo');

INSERT INTO tag_axis VALUES('dom','tresc/motyw');

INSERT INTO tag_axis VALUES('dom','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('tesknota','tresc/motyw');

INSERT INTO tag_axis VALUES('tesknota','czas/ciaglosc');

INSERT INTO tag_axis VALUES('tesknota','relacja/spoleczne');

INSERT INTO tag_axis VALUES('tesknota','emocja/afekt');

INSERT INTO tag_axis VALUES('bunt','tresc/motyw');

INSERT INTO tag_axis VALUES('bunt','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('smierc','tresc/motyw');

INSERT INTO tag_axis VALUES('taniec','tresc/motyw');

INSERT INTO tag_axis VALUES('taniec','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('latanie-spadanie','tresc/motyw');

INSERT INTO tag_axis VALUES('latanie-spadanie','ruch/cel');

INSERT INTO tag_axis VALUES('prawda','tresc/motyw');

INSERT INTO tag_axis VALUES('prawda','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('oddech-powietrze','tresc/motyw');

INSERT INTO tag_axis VALUES('oddech-powietrze','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('oddech-powietrze','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('ziemia','tresc/motyw');

INSERT INTO tag_axis VALUES('ziemia','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('deszcz','tresc/motyw');

INSERT INTO tag_axis VALUES('deszcz','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('sen','tresc/motyw');

INSERT INTO tag_axis VALUES('marzenie','tresc/motyw');

INSERT INTO tag_axis VALUES('marzenie','czas/ciaglosc');

INSERT INTO tag_axis VALUES('droga-podroz','tresc/motyw');

INSERT INTO tag_axis VALUES('droga-podroz','ruch/cel');

INSERT INTO tag_axis VALUES('przemiana','tresc/motyw');

INSERT INTO tag_axis VALUES('przemiana','czas/ciaglosc');

INSERT INTO tag_axis VALUES('odrodzenie','tresc/motyw');

INSERT INTO tag_axis VALUES('odrodzenie','czas/ciaglosc');

INSERT INTO tag_axis VALUES('wspomnienia','tresc/motyw');

INSERT INTO tag_axis VALUES('wspomnienia','czas/ciaglosc');

INSERT INTO tag_axis VALUES('pamiec','tresc/motyw');

INSERT INTO tag_axis VALUES('pamiec','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('ulga','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('ulga','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('ulga','emocja/afekt');

INSERT INTO tag_axis VALUES('spokoj','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('spokoj','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('spokoj','emocja/afekt');

INSERT INTO tag_axis VALUES('ulga-odroczona','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('ulga-odroczona','czas/ciaglosc');

INSERT INTO tag_axis VALUES('ulga-utracona','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('ulga-utracona','czas/ciaglosc');

INSERT INTO tag_axis VALUES('ulga-z-zewnatrz','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('ulga-z-zewnatrz','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('schronienie','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('schronienie','ruch/cel');

INSERT INTO tag_axis VALUES('dotarcie','ruch/cel');

INSERT INTO tag_axis VALUES('cel-nieosiagniety','ruch/cel');

INSERT INTO tag_axis VALUES('cel-nieosiagniety','czas/ciaglosc');

INSERT INTO tag_axis VALUES('pogon','ruch/cel');

INSERT INTO tag_axis VALUES('pogon','kierunek');

INSERT INTO tag_axis VALUES('powrot-do','ruch/cel');

INSERT INTO tag_axis VALUES('powrot-do','czas/ciaglosc');

INSERT INTO tag_axis VALUES('powrot-do','kierunek');

INSERT INTO tag_axis VALUES('wystarczy','nasycenie/naped');

INSERT INTO tag_axis VALUES('nigdy-dosc','nasycenie/naped');

INSERT INTO tag_axis VALUES('dosc-przesyt','nasycenie/naped');

INSERT INTO tag_axis VALUES('dosc-przesyt','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('euforia-naped','nasycenie/naped');

INSERT INTO tag_axis VALUES('euforia-naped','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('euforia-naped','emocja/afekt');

INSERT INTO tag_axis VALUES('zaraz-minie','czas/ciaglosc');

INSERT INTO tag_axis VALUES('przetrwanie','czas/ciaglosc');

INSERT INTO tag_axis VALUES('przetrwanie','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('utrata','czas/ciaglosc');

INSERT INTO tag_axis VALUES('przez-szczescie','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('bezsilnosc','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('bezsilnosc','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('bezsilnosc','emocja/afekt');

INSERT INTO tag_axis VALUES('anhedonia','depresyjnosc');

INSERT INTO tag_axis VALUES('brak-nadziei','depresyjnosc');

INSERT INTO tag_axis VALUES('brak-nadziei','czas/ciaglosc');

INSERT INTO tag_axis VALUES('bezwartosciowosc','depresyjnosc');

INSERT INTO tag_axis VALUES('bezwartosciowosc','kierunek');

INSERT INTO tag_axis VALUES('wina','depresyjnosc');

INSERT INTO tag_axis VALUES('wina','kierunek');

INSERT INTO tag_axis VALUES('wina','emocja/afekt');

INSERT INTO tag_axis VALUES('wycofanie','depresyjnosc');

INSERT INTO tag_axis VALUES('wycofanie','kierunek');

INSERT INTO tag_axis VALUES('wycofanie','relacja/spoleczne');

INSERT INTO tag_axis VALUES('brak-napedu','depresyjnosc');

INSERT INTO tag_axis VALUES('brak-napedu','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('wyczerpanie','depresyjnosc');

INSERT INTO tag_axis VALUES('wyczerpanie','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('zobojetnienie','depresyjnosc');

INSERT INTO tag_axis VALUES('zobojetnienie','dostep-do-emocji');

INSERT INTO tag_axis VALUES('pustka-emocjonalna','depresyjnosc');

INSERT INTO tag_axis VALUES('pustka-emocjonalna','dostep-do-emocji');

INSERT INTO tag_axis VALUES('spowolnienie','depresyjnosc');

INSERT INTO tag_axis VALUES('spowolnienie','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('bezsennosc','depresyjnosc');

INSERT INTO tag_axis VALUES('bezsennosc','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('nadmierny-sen','depresyjnosc');

INSERT INTO tag_axis VALUES('nadmierny-sen','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('smierc-wlasna','depresyjnosc');

INSERT INTO tag_axis VALUES('smierc-wlasna','tresc/motyw');

INSERT INTO tag_axis VALUES('znikniecie','depresyjnosc');

INSERT INTO tag_axis VALUES('znikniecie','kierunek');

INSERT INTO tag_axis VALUES('zamartwianie','lek/gad');

INSERT INTO tag_axis VALUES('zamartwianie','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('lek-antycypacyjny','lek/gad');

INSERT INTO tag_axis VALUES('lek-antycypacyjny','czas/ciaglosc');

INSERT INTO tag_axis VALUES('katastrofizacja','lek/gad');

INSERT INTO tag_axis VALUES('katastrofizacja','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('hiperczujnosc','lek/gad');

INSERT INTO tag_axis VALUES('hiperczujnosc','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('hiperczujnosc','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('niepewnosc-nie-do-zniesienia','lek/gad');

INSERT INTO tag_axis VALUES('niepewnosc-nie-do-zniesienia','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('kontrola','lek/gad');

INSERT INTO tag_axis VALUES('kontrola','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('sprawdzanie','lek/gad');

INSERT INTO tag_axis VALUES('sprawdzanie','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('potrzeba-zapewnienia','lek/gad');

INSERT INTO tag_axis VALUES('potrzeba-zapewnienia','relacja/spoleczne');

INSERT INTO tag_axis VALUES('potrzeba-zapewnienia','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('napiecie-ciala','lek/gad');

INSERT INTO tag_axis VALUES('napiecie-ciala','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('napiecie-ciala','cialo');

INSERT INTO tag_axis VALUES('niemoznosc-odpuszczenia','lek/gad');

INSERT INTO tag_axis VALUES('niemoznosc-odpuszczenia','czas/ciaglosc');

INSERT INTO tag_axis VALUES('unikanie-z-leku','lek/gad');

INSERT INTO tag_axis VALUES('unikanie-z-leku','ruch/cel');

INSERT INTO tag_axis VALUES('unikanie-z-leku','kierunek');

INSERT INTO tag_axis VALUES('zamrozenie','lek/gad');

INSERT INTO tag_axis VALUES('zamrozenie','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('zamrozenie','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('przeciazenie-przyszloscia','lek/gad');

INSERT INTO tag_axis VALUES('przeciazenie-przyszloscia','czas/ciaglosc');

INSERT INTO tag_axis VALUES('przeciazenie-przyszloscia','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('samokontrola-spoleczna','maskowanie');

INSERT INTO tag_axis VALUES('samokontrola-spoleczna','relacja/spoleczne');

INSERT INTO tag_axis VALUES('ukrywanie-reakcji','maskowanie');

INSERT INTO tag_axis VALUES('ukrywanie-reakcji','dostep-do-emocji');

INSERT INTO tag_axis VALUES('ukrywanie-potrzeb','maskowanie');

INSERT INTO tag_axis VALUES('ukrywanie-potrzeb','regulacja/bezpieczenstwo');

INSERT INTO tag_axis VALUES('dopasowanie-roli','maskowanie');

INSERT INTO tag_axis VALUES('dopasowanie-roli','relacja/spoleczne');

INSERT INTO tag_axis VALUES('nasladowanie','maskowanie');

INSERT INTO tag_axis VALUES('nasladowanie','relacja/spoleczne');

INSERT INTO tag_axis VALUES('skryptowanie','maskowanie');

INSERT INTO tag_axis VALUES('skryptowanie','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('analiza-po-kontakcie','maskowanie');

INSERT INTO tag_axis VALUES('analiza-po-kontakcie','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('analiza-po-kontakcie','czas/ciaglosc');

INSERT INTO tag_axis VALUES('analiza-przed-kontaktem','maskowanie');

INSERT INTO tag_axis VALUES('analiza-przed-kontaktem','poznanie/uwaga/pamiec');

INSERT INTO tag_axis VALUES('analiza-przed-kontaktem','czas/ciaglosc');

INSERT INTO tag_axis VALUES('kontrola-wizerunku','maskowanie');

INSERT INTO tag_axis VALUES('kontrola-wizerunku','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('maskowanie-koszt','maskowanie');

INSERT INTO tag_axis VALUES('maskowanie-koszt','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('rozpad-po-masce','maskowanie');

INSERT INTO tag_axis VALUES('rozpad-po-masce','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('rozpad-po-masce','czas/ciaglosc');

INSERT INTO tag_axis VALUES('ja-publiczne-ja-prywatne','maskowanie');

INSERT INTO tag_axis VALUES('ja-publiczne-ja-prywatne','kierunek');

INSERT INTO tag_axis VALUES('nierozpoznanie-siebie','maskowanie');

INSERT INTO tag_axis VALUES('nierozpoznanie-siebie','dostep-do-emocji');

INSERT INTO tag_axis VALUES('do-siebie','kierunek');

INSERT INTO tag_axis VALUES('do-innych','kierunek');

INSERT INTO tag_axis VALUES('do-swiata','kierunek');

INSERT INTO tag_axis VALUES('ku-przeszlosci','kierunek');

INSERT INTO tag_axis VALUES('ku-przeszlosci','czas/ciaglosc');

INSERT INTO tag_axis VALUES('ku-przyszlosci','kierunek');

INSERT INTO tag_axis VALUES('ku-przyszlosci','czas/ciaglosc');

INSERT INTO tag_axis VALUES('ku-komus','kierunek');

INSERT INTO tag_axis VALUES('ku-komus','relacja/spoleczne');

INSERT INTO tag_axis VALUES('od-kogos','kierunek');

INSERT INTO tag_axis VALUES('od-kogos','relacja/spoleczne');

INSERT INTO tag_axis VALUES('ku-swiatu','kierunek');

INSERT INTO tag_axis VALUES('od-swiata','kierunek');

INSERT INTO tag_axis VALUES('wysokie-pobudzenie','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('niskie-pobudzenie','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('eskalacja','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('eskalacja','czas/ciaglosc');

INSERT INTO tag_axis VALUES('wygaszanie','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('wygaszanie','czas/ciaglosc');

INSERT INTO tag_axis VALUES('zablokowanie','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('zablokowanie','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('rozpad','pobudzenie/dynamika');

INSERT INTO tag_axis VALUES('rozpad','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('sprawczosc','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('wiem-co-czuje','dostep-do-emocji');

INSERT INTO tag_axis VALUES('nie-wiem-co-czuje','dostep-do-emocji');

INSERT INTO tag_axis VALUES('czuje-bez-nazwy','dostep-do-emocji');

INSERT INTO tag_axis VALUES('emocja-przez-cialo','dostep-do-emocji');

INSERT INTO tag_axis VALUES('emocja-przez-cialo','sensoryka/bodzce');

INSERT INTO tag_axis VALUES('emocja-przez-cialo','cialo');

INSERT INTO tag_axis VALUES('emocja-z-opoznieniem','dostep-do-emocji');

INSERT INTO tag_axis VALUES('emocja-z-opoznieniem','czas/ciaglosc');

INSERT INTO tag_axis VALUES('emocja-przez-skutek','dostep-do-emocji');

INSERT INTO tag_axis VALUES('emocja-przez-skutek','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('emocja-przez-innego','dostep-do-emocji');

INSERT INTO tag_axis VALUES('emocja-przez-innego','relacja/spoleczne');

INSERT INTO tag_axis VALUES('sprzeczne-emocje','dostep-do-emocji');

INSERT INTO tag_axis VALUES('sprzeczne-emocje','kierunek');

INSERT INTO tag_axis VALUES('smutek','emocja/afekt');

INSERT INTO tag_axis VALUES('melancholia','emocja/afekt');

INSERT INTO tag_axis VALUES('melancholia','czas/ciaglosc');

INSERT INTO tag_axis VALUES('radosc','emocja/afekt');

INSERT INTO tag_axis VALUES('lek','emocja/afekt');

INSERT INTO tag_axis VALUES('lek','lek/gad');

INSERT INTO tag_axis VALUES('strach','emocja/afekt');

INSERT INTO tag_axis VALUES('wstyd','emocja/afekt');

INSERT INTO tag_axis VALUES('wstyd','kierunek');

INSERT INTO tag_axis VALUES('wstyd','maskowanie');

INSERT INTO tag_axis VALUES('wstret','emocja/afekt');

INSERT INTO tag_axis VALUES('wstret','kierunek');

INSERT INTO tag_axis VALUES('zazdrosc','emocja/afekt');

INSERT INTO tag_axis VALUES('zazdrosc','relacja/spoleczne');

INSERT INTO tag_axis VALUES('nadzieja','emocja/afekt');

INSERT INTO tag_axis VALUES('nadzieja','czas/ciaglosc');

INSERT INTO tag_axis VALUES('nadzieja','kierunek');

INSERT INTO tag_axis VALUES('rozpacz','emocja/afekt');

INSERT INTO tag_axis VALUES('rozpacz','depresyjnosc');

INSERT INTO tag_axis VALUES('czulosc','emocja/afekt');

INSERT INTO tag_axis VALUES('czulosc','relacja/spoleczne');

INSERT INTO tag_axis VALUES('pozadanie','emocja/afekt');

INSERT INTO tag_axis VALUES('pozadanie','relacja/spoleczne');

INSERT INTO tag_axis VALUES('pozadanie','cialo');

INSERT INTO tag_axis VALUES('frustracja','emocja/afekt');

INSERT INTO tag_axis VALUES('frustracja','sprawczosc/przyczynowosc');

INSERT INTO tag_axis VALUES('nuda','emocja/afekt');

INSERT INTO tag_axis VALUES('nuda','nasycenie/naped');

INSERT INTO tag_axis VALUES('zal','emocja/afekt');

INSERT INTO tag_axis VALUES('zal','czas/ciaglosc');

INSERT INTO tag_axis VALUES('duma','emocja/afekt');

INSERT INTO tag_axis VALUES('duma','kierunek');

