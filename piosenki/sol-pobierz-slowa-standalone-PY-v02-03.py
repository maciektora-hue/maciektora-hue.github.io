#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOL — standalone lyrics fetcher v02-03, drugi przebieg dla pozostałych braków.

NIE CZYTA ŻADNYCH PLIKÓW WEJŚCIOWYCH.
Lista 84 nierozwiązanych utworów jest osadzona bezpośrednio w tym pliku.

Co zmieniono względem v01:
1. Oryginał i transliteracja ASCII są osobnymi zapytaniami.
2. Tytuły z separatorami są szukane także fragmentami.
3. Dopiski live/remaster/edit/version/feat. są agresywniej usuwane.
4. Przy wielu wykonawcach skrypt pyta pełny zapis i każdego wykonawcę
   rozdzielonego przecinkiem; NIE rozcina nazw po "and" ani "&".
5. Dla mantr, sutr, Shchedryka, Prząśniczki i kilku dzieł klasycznych
   działa osobna gałąź canonical work lookup.

Zasada architektury canonical:
- kluczem wyszukiwania jest rozpoznane DZIEŁO / alias dzieła / tytuł kanoniczny,
- wykonawca konkretnego nagrania NIE jest warunkiem wyszukania tekstu,
- wykonawca pozostaje wyłącznie metadaną pomocniczą konkretnego utwu_id,
- artist_* nie bierze udziału w scoringu gałęzi canonical,
- tekst znaleziony po samym dziele dostaje status canonicaltext, nie found,
- identyfikacja nagrania i identyfikacja dzieła są dwiema osobnymi funkcjami,
- WORK_ALIASES nie trafiają do zwykłej ścieżki identyfikacji nagrania.

Status canonicaltext oznacza:
- znaleziono kanoniczny / bazowy tekst dzieła,
- wykonawca konkretnego nagrania NIE jest traktowany jako autor tekstu,
- nie potwierdzono jeszcze zgodności tekstu 1:1 z konkretnym nagraniem,
- wynik zawiera tekst i może później dostać lyrics_id w Middle Endzie.

Uruchom:
    python sol-pobierz-slowa-standalone-PY-v02-03.py

Wynik:
    nowy CSV przy każdym uruchomieniu, np.
    szukamy-slow-pobrane-2pass-20260906-120000.csv

Skrypt nie czyta ani nie modyfikuje żadnego istniejącego CSV.
Używa wyłącznie standardowej biblioteki Pythona.
"""

import csv
import html
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

USER_AGENT = "SOL-LyricsFetcher/2.2"
TIMEOUT = 18
RETRIES = 3
PAUSE = 0.12

TRACKS = [{"utwu_id":"utwu-000937","spotify_id":"1rJgJ31pdLTjdO3IAk2SFh","spotify_order":"2","title_original":"Carol of the Bells - Remastered","title_normalized":"carol of the bells - remastered","title_parsed":"carol of the bells remastered","artist_original":"The Tabernacle Choir at Temple Square","artist_normalized":"the tabernacle choir at temple square","artist_parsed":"the tabernacle choir at temple square","album_original":"This Is Christmas (The Mormon Tabernacle Choir Performing Timeless Christmas Songs)"},{"utwu_id":"utwu-000935","spotify_id":"2AgEFv5V9NwBSMU3iF6FNh","spotify_order":"4","title_original":"Long Vajrasattva Purifying Mantra chanted in Sanskrit","title_normalized":"long vajrasattva purifying mantra chanted in sanskrit","title_parsed":"long vajrasattva purifying mantra chanted in sanskrit","artist_original":"Buddha Weekly","artist_normalized":"buddha weekly","artist_parsed":"buddha weekly","album_original":"Mantra Collection 1"},{"utwu_id":"utwu-000934","spotify_id":"0cLdMgwO2tqKilhWbUARWG","spotify_order":"5","title_original":"The Carol of the Old Ones - Soprano Version","title_normalized":"the carol of the old ones - soprano version","title_parsed":"the carol of the old ones soprano version","artist_original":"Мико́ла Дми́трович Леонто́вич, Mao Endo, Gico Forte","artist_normalized":"мико́ла дми́трович леонто́вич, mao endo, gico forte","artist_parsed":"микола дмитрович леонтович | mao endo | gico forte","album_original":"The Carol of the Old Ones (Soprano Version)"},{"utwu_id":"utwu-000933","spotify_id":"6raClVJaHReAILC7ITassT","spotify_order":"6","title_original":"Aleksandra odchodzi","title_normalized":"aleksandra odchodzi","title_parsed":"aleksandra odchodzi","artist_original":"Michał Łanuszka","artist_normalized":"michał łanuszka","artist_parsed":"michał łanuszka","album_original":"Łanuszka / Cohen"},{"utwu_id":"utwu-000931","spotify_id":"2r8lQVkWiPcv5dryFZh9Or","spotify_order":"8","title_original":"BOG NA VOJNA","title_normalized":"bog na vojna","title_parsed":"bog na vojna","artist_original":"Da Dzaka Nakot","artist_normalized":"da dzaka nakot","artist_parsed":"da dzaka nakot","album_original":"OGAN"},{"utwu_id":"utwu-000930","spotify_id":"2XSSr3IS1F9bkltmchybcM","spotify_order":"9","title_original":"PESNA ŠTO GORI","title_normalized":"pesna što gori","title_parsed":"pesna sto gori","artist_original":"Da Dzaka Nakot","artist_normalized":"da dzaka nakot","artist_parsed":"da dzaka nakot","album_original":"OGAN"},{"utwu_id":"utwu-000926","spotify_id":"6rKCkCMgQC0n94XineFKzL","spotify_order":"13","title_original":"Bhagavad Gītā, Chapter 11","title_normalized":"bhagavad gītā, chapter 11","title_parsed":"bhagavad gita chapter 11","artist_original":"Gaiea Sanskrit","artist_normalized":"gaiea sanskrit","artist_parsed":"gaiea sanskrit","album_original":"Bhagavad Gita"},{"utwu_id":"utwu-000925","spotify_id":"5kmr2Ip9xbfgDVf45AHI6E","spotify_order":"14","title_original":"Shchedryk - Carol of the Bells;Sharovaari Orchestral Version","title_normalized":"shchedryk - carol of the bells;sharovaari orchestral version","title_parsed":"shchedryk carol of the bells sharovaari orchestral version","artist_original":"Eileen","artist_normalized":"eileen","artist_parsed":"eileen","album_original":"Shchedryk (Carol of the Bells;Sharovaari Orchestral Version)"},{"utwu_id":"utwu-000924","spotify_id":"3EiHf4NihLd3WiE83gTNVH","spotify_order":"15","title_original":"Ajai Alai","title_normalized":"ajai alai","title_parsed":"ajai alai","artist_original":"Meditative Mind","artist_normalized":"meditative mind","artist_parsed":"meditative mind","album_original":"Ajai Alai"},{"utwu_id":"utwu-000922","spotify_id":"5PzS4t23BDEmsESvFd14Z5","spotify_order":"17","title_original":"Evolution of Music","title_normalized":"evolution of music","title_parsed":"evolution of music","artist_original":"dj-Nate","artist_normalized":"dj-nate","artist_parsed":"dj nate","album_original":"Classic Classics (2005-2010)"},{"utwu_id":"utwu-000917","spotify_id":"1vrnALuaFUZUEdD53j1M47","spotify_order":"22","title_original":"Versatile - Live in Paris","title_normalized":"versatile - live in paris","title_parsed":"versatile live in paris","artist_original":"MEUTE","artist_normalized":"meute","artist_parsed":"meute","album_original":"Live In Paris"},{"utwu_id":"utwu-000916","spotify_id":"4G3oFJE6aei1ygJVinVt1O","spotify_order":"23","title_original":"Raw","title_normalized":"raw","title_parsed":"raw","artist_original":"MEUTE","artist_normalized":"meute","artist_parsed":"meute","album_original":"Puls"},{"utwu_id":"utwu-000901","spotify_id":"7k2RgMZo4ZsQy0QcTWYFJx","spotify_order":"38","title_original":"Mother Mary: Blessings of Our Miraculous Mother of Solar Light","title_normalized":"mother mary: blessings of our miraculous mother of solar light","title_parsed":"mother mary blessings of our miraculous mother of solar light","artist_original":"Alana Fairchild","artist_normalized":"alana fairchild","artist_parsed":"alana fairchild","album_original":"The Kuan Yin Transmission"},{"utwu_id":"utwu-000897","spotify_id":"7Hh8uQRwnlSV7fYZTB2G2D","spotify_order":"42","title_original":"Montage from Twin Peaks","title_normalized":"montage from twin peaks","title_parsed":"montage from twin peaks","artist_original":"Angelo Badalamenti","artist_normalized":"angelo badalamenti","artist_parsed":"angelo badalamenti","album_original":"Twin Peaks: Fire Walk With Me - Soundtrack"},{"utwu_id":"utwu-000894","spotify_id":"5g24dfca4XvSL4VhGCmXNs","spotify_order":"45","title_original":"Pieśń Wdzięczności | Song of Gratitude | gdy niebo i ziemia staje się jednym","title_normalized":"pieśń wdzięczności | song of gratitude | gdy niebo i ziemia staje się jednym","title_parsed":"piesn wdziecznosci song of gratitude gdy niebo i ziemia staje sie jednym","artist_original":"Beata Ślusarek","artist_normalized":"beata ślusarek","artist_parsed":"beata slusarek","album_original":"Pieśń Wdzięczności | Song of Gratitude | gdy niebo i ziemia staje się jednym"},{"utwu_id":"utwu-000893","spotify_id":"0fsljuB0X7bY7tRGBTRTUJ","spotify_order":"46","title_original":"Złap mnie – zanim zapomnę ● Zaklęcie Nocy ● slavic fire","title_normalized":"złap mnie - zanim zapomnę ● zaklęcie nocy ● slavic fire","title_parsed":"złap mnie zanim zapomne zaklecie nocy slavic fire","artist_original":"Beata Ślusarek","artist_normalized":"beata ślusarek","artist_parsed":"beata slusarek","album_original":"Złap mnie – zanim zapomnę ● Zaklęcie Nocy ● slavic fire"},{"utwu_id":"utwu-000892","spotify_id":"4zp87k6eCpaUgWJP24dRih","spotify_order":"47","title_original":"Potężna magia obfitości – Uwolnienie od zazdrości, klątw, złorzeczeń, obciążeń rodowych i własnych przewinień. Głos przodków, ziołowy dym, moc duszy. Szeptanka słowiańska (Slavic Magia)","title_normalized":"potężna magia obfitości - uwolnienie od zazdrości, klątw, złorzeczeń, obciążeń rodowych i własnych przewinień. głos przodków, ziołowy dym, moc duszy. szeptanka słowiańska (slavic magia)","title_parsed":"potezna magia obfitosci uwolnienie od zazdrosci klatw złorzeczen obciazen rodowych i własnych przewinien głos przodkow ziołowy dym moc duszy szeptanka słowianska slavic magia","artist_original":"Beata Ślusarek","artist_normalized":"beata ślusarek","artist_parsed":"beata slusarek","album_original":"Potężna magia obfitości – Uwolnienie od zazdrości, klątw, złorzeczeń, obciążeń rodowych i własnych przewinień. Głos przodków, ziołowy dym, moc duszy. Szeptanka słowiańska (Slavic Magia)"},{"utwu_id":"utwu-000890","spotify_id":"3IYsP4sl8TlMRGGQqS0KpP","spotify_order":"49","title_original":"Щедрик (Szczedryk)","title_normalized":"щедрик (szczedryk)","title_parsed":"щедрик szczedryk","artist_original":"Katedralny Chór Parafii Prawosławnej Św. Mikołaja w Gdańsku","artist_normalized":"katedralny chór parafii prawosławnej św. mikołaja w gdańsku","artist_parsed":"katedralny chor parafii prawosławnej sw mikołaja w gdansku","album_original":"Kolędy"},{"utwu_id":"utwu-000876","spotify_id":"6snvt5biwMulcNrVWPIOH6","spotify_order":"63","title_original":"Aviary","title_normalized":"aviary","title_parsed":"aviary","artist_original":"Labek & Chrobak","artist_normalized":"labek & chrobak","artist_parsed":"labek | chrobak","album_original":"Wanderer"},{"utwu_id":"utwu-000860","spotify_id":"4Ft2ecdZmWtf9FW9s8IZAx","spotify_order":"79","title_original":"Too Late","title_normalized":"too late","title_parsed":"too late","artist_original":"Joe Bel","artist_normalized":"joe bel","artist_parsed":"joe bel","album_original":"Dreams"},{"utwu_id":"utwu-000859","spotify_id":"0eEwn4pPQdIRHMeql0CisG","spotify_order":"80","title_original":"In Your Head","title_normalized":"in your head","title_parsed":"in your head","artist_original":"Isaya","artist_normalized":"isaya","artist_parsed":"isaya","album_original":"Dead Or Alive, I'll Get You Back (Radical Version)"},{"utwu_id":"utwu-000856","spotify_id":"6OHt64WlY423qZWFZg3Rjt","spotify_order":"83","title_original":"Song X","title_normalized":"song x","title_parsed":"song x","artist_original":"Kyrie Kristmanson","artist_normalized":"kyrie kristmanson","artist_parsed":"kyrie kristmanson","album_original":"Pagan Love"},{"utwu_id":"utwu-000848","spotify_id":"0Iw5GdyGy6xxryx8BFY7bU","spotify_order":"91","title_original":"Jođi","title_normalized":"jođi","title_parsed":"jođi","artist_original":"Hildá Länsman, Lávre","artist_normalized":"hildá länsman, lávre","artist_parsed":"hilda lansman | lavre","album_original":"Jođi"},{"utwu_id":"utwu-000844","spotify_id":"7sR93qMXyYoj1ShD44QGqf","spotify_order":"95","title_original":"My Russomisia Is Stored In My Tits","title_normalized":"my russomisia is stored in my tits","title_parsed":"my russomisia is stored in my tits","artist_original":"Dee Lav","artist_normalized":"dee lav","artist_parsed":"dee lav","album_original":"My Russomisia Is Stored In My Tits"},{"utwu_id":"utwu-000828","spotify_id":"5nFQsRIjWRnro5cNMBhZc0","spotify_order":"111","title_original":"Czy widziałeś już tę smugę?","title_normalized":"czy widziałeś już tę smugę?","title_parsed":"czy widziałes juz te smuge","artist_original":"Limboski","artist_normalized":"limboski","artist_parsed":"limboski","album_original":"Ucieczka saula"},{"utwu_id":"utwu-000824","spotify_id":"4i3VEozXMJnnPmTXJWoJW4","spotify_order":"115","title_original":"Octobre","title_normalized":"octobre","title_parsed":"octobre","artist_original":"Ezéchiel Pailhès","artist_normalized":"ezéchiel pailhès","artist_parsed":"ezechiel pailhes","album_original":"Tout va bien"},{"utwu_id":"utwu-000817","spotify_id":"7kricxujMus766dyNv1y9h","spotify_order":"122","title_original":"Symphony No. 5 in C-Sharp Minor: I. Trauermarsch (Funeral March)","title_normalized":"symphony no. 5 in c-sharp minor: i. trauermarsch (funeral march)","title_parsed":"symphony no 5 in c sharp minor i trauermarsch funeral march","artist_original":"Gustav Mahler, Berliner Philharmoniker, Bernard Haitink","artist_normalized":"gustav mahler, berliner philharmoniker, bernard haitink","artist_parsed":"gustav mahler | berliner philharmoniker | bernard haitink","album_original":"Mahler's 5th Symphony"},{"utwu_id":"utwu-000808","spotify_id":"5XSfUql8myjvMsBF48LPhZ","spotify_order":"131","title_original":"Symphony No. 9 in D Minor, Op. 125 \"Choral\": III. Adagio molto e cantabile - Andante moderato","title_normalized":"symphony no. 9 in d minor, op. 125 \"choral\": iii. adagio molto e cantabile - andante moderato","title_parsed":"symphony no 9 in d minor op 125 choral iii adagio molto e cantabile andante moderato","artist_original":"Ludwig van Beethoven, Helena Juntunen, Katarina Karnéus, Daniel Norman, Neal Davies, Minnesota Chorale, Minnesota Orchestra, Osmo Vänskä","artist_normalized":"ludwig van beethoven, helena juntunen, katarina karnéus, daniel norman, neal davies, minnesota chorale, minnesota orchestra, osmo vänskä","artist_parsed":"ludwig van beethoven | helena juntunen | katarina karneus | daniel norman | neal davies | minnesota chorale | minnesota orchestra | osmo vanska","album_original":"Beethoven, Van L.: Symphony No. 9, \"Choral\""},{"utwu_id":"utwu-000795","spotify_id":"08fAyOrHiPc8FqPBzuP9h5","spotify_order":"144","title_original":"How We Disappear (feat. Gaba Kulka)","title_normalized":"how we disappear (feat. gaba kulka)","title_parsed":"how we disappear feat gaba kulka","artist_original":"Daniel Bloom, Gaba Kulka","artist_normalized":"daniel bloom, gaba kulka","artist_parsed":"daniel bloom | gaba kulka","album_original":"Lovely Fear"},{"utwu_id":"utwu-000728","spotify_id":"1j5S9kOSvPCTiSbbkE5zLU","spotify_order":"211","title_original":"Ameland","title_normalized":"ameland","title_parsed":"ameland","artist_original":"Aafke Romeijn, Spinvis","artist_normalized":"aafke romeijn, spinvis","artist_parsed":"aafke romeijn | spinvis","album_original":"M"},{"utwu_id":"utwu-000725","spotify_id":"06SZOEJ33jWR2XazmUko3L","spotify_order":"214","title_original":"Deep End","title_normalized":"deep end","title_parsed":"deep end","artist_original":"Indian Askin","artist_normalized":"indian askin","artist_parsed":"indian askin","album_original":"Deep End"},{"utwu_id":"utwu-000723","spotify_id":"33OoPrY7Sf8lmD9Bfj87KM","spotify_order":"216","title_original":"Wherever","title_normalized":"wherever","title_parsed":"wherever","artist_original":"The Fruitcakes","artist_normalized":"the fruitcakes","artist_parsed":"the fruitcakes","album_original":"Into The Sun"},{"utwu_id":"utwu-000722","spotify_id":"4OHHYQxvnyPtbrnE3Ci9dT","spotify_order":"217","title_original":"Atlas wysp","title_normalized":"atlas wysp","title_parsed":"atlas wysp","artist_original":"Adam Repucha","artist_normalized":"adam repucha","artist_parsed":"adam repucha","album_original":"Atlas wysp"},{"utwu_id":"utwu-000714","spotify_id":"2iGu50v4RTHdoZM58gPnKG","spotify_order":"225","title_original":"So Long","title_normalized":"so long","title_parsed":"so long","artist_original":"Jaguar Jaguar","artist_normalized":"jaguar jaguar","artist_parsed":"jaguar jaguar","album_original":"So Long"},{"utwu_id":"utwu-000692","spotify_id":"2NY4A8D2xqwnS21ki6ENGh","spotify_order":"247","title_original":"Nosedive","title_normalized":"nosedive","title_parsed":"nosedive","artist_original":"The Flabbies","artist_normalized":"the flabbies","artist_parsed":"the flabbies","album_original":"Back in Town"},{"utwu_id":"utwu-000691","spotify_id":"7w0eDwpwVu4cW6KaGqkQR3","spotify_order":"248","title_original":"BEATNIK OR NOT TO BE","title_normalized":"beatnik or not to be","title_parsed":"beatnik or not to be","artist_original":"Elias Dris","artist_normalized":"elias dris","artist_parsed":"elias dris","album_original":"Beatnik or Not to Be"},{"utwu_id":"utwu-000688","spotify_id":"3qrSK3XkSIE2S7ny2wZVpg","spotify_order":"251","title_original":"Wings of Life","title_normalized":"wings of life","title_parsed":"wings of life","artist_original":"Gods Of Venus","artist_normalized":"gods of venus","artist_parsed":"gods of venus","album_original":"Wings Of Life"},{"utwu_id":"utwu-000681","spotify_id":"12qK04fJriVXCCEf2roMyr","spotify_order":"258","title_original":"Ice for Aureliano Buendia","title_normalized":"ice for aureliano buendia","title_parsed":"ice for aureliano buendia","artist_original":"Evgeny Grinko","artist_normalized":"evgeny grinko","artist_parsed":"evgeny grinko","album_original":"Ice for Aureliano Buendia (Deluxe Edition)"},{"utwu_id":"utwu-000680","spotify_id":"5OhzrS0N9hUOLDqRNhe28K","spotify_order":"259","title_original":"Amara Terra Mia","title_normalized":"amara terra mia","title_parsed":"amara terra mia","artist_original":"Elina Duni","artist_normalized":"elina duni","artist_parsed":"elina duni","album_original":"Partir"},{"utwu_id":"utwu-000673","spotify_id":"2IcZ2OrLIxNCrxvwabWLns","spotify_order":"266","title_original":"The Air I Breathe","title_normalized":"the air i breathe","title_parsed":"the air i breathe","artist_original":"Badmarsh & Shri","artist_normalized":"badmarsh & shri","artist_parsed":"badmarsh | shri","album_original":"Dancing Drums"},{"utwu_id":"utwu-000671","spotify_id":"6DJ7FQf1hPp0s0mPkbIF7X","spotify_order":"268","title_original":"Shiva Saṅkalpa Sūktam Peaceful Mind","title_normalized":"shiva saṅkalpa sūktam peaceful mind","title_parsed":"shiva sankalpa suktam peaceful mind","artist_original":"Gaiea Sanskrit","artist_normalized":"gaiea sanskrit","artist_parsed":"gaiea sanskrit","album_original":"Powerful Sanskrit Mantras"},{"utwu_id":"utwu-000670","spotify_id":"15jOrmaFGWThhlWccOAzDH","spotify_order":"269","title_original":"Durgā Sūktam Courage & Strength","title_normalized":"durgā sūktam courage & strength","title_parsed":"durga suktam courage strength","artist_original":"Gaiea Sanskrit","artist_normalized":"gaiea sanskrit","artist_parsed":"gaiea sanskrit","album_original":"Powerful Sanskrit Mantras"},{"utwu_id":"utwu-000668","spotify_id":"7wMGKziHMkic15akQHvRBF","spotify_order":"271","title_original":"Oh Angel","title_normalized":"oh angel","title_parsed":"oh angel","artist_original":"Polskie Znaki, Mark Lanegan","artist_normalized":"polskie znaki, mark lanegan","artist_parsed":"polskie znaki | mark lanegan","album_original":"Rzeczy ostatnie"},{"utwu_id":"utwu-000665","spotify_id":"7HUQsxWDNH9j4HD0pYEVdN","spotify_order":"274","title_original":"Čuojahat Mu","title_normalized":"čuojahat mu","title_parsed":"cuojahat mu","artist_original":"Hildá Länsman, Tuomas Norvio","artist_normalized":"hildá länsman, tuomas norvio","artist_parsed":"hilda lansman | tuomas norvio","album_original":"Čuojahat Mu"},{"utwu_id":"utwu-000663","spotify_id":"1LbebplBg3Av4K5V8ALx1a","spotify_order":"276","title_original":"Złote łezki","title_normalized":"złote łezki","title_parsed":"złote łezki","artist_original":"Meek, Oh Why?, BIESY","artist_normalized":"meek, oh why?, biesy","artist_parsed":"meek | oh why | biesy","album_original":"Wszystko w swoim czasie"},{"utwu_id":"utwu-000660","spotify_id":"6BdFZd5lLdoV1VjuBajSpQ","spotify_order":"279","title_original":"Nie stało się nic (Mierzeja 2 | Empik Go)","title_normalized":"nie stało się nic (mierzeja 2 | empik go)","title_parsed":"nie stało sie nic mierzeja 2 empik go","artist_original":"Matylda/Łukasiewicz, Matylda, Radek Łukasiewicz","artist_normalized":"matylda/łukasiewicz, matylda, radek łukasiewicz","artist_parsed":"matylda/łukasiewicz | matylda | radek łukasiewicz","album_original":"Nie stało się nic (Mierzeja 2 | Empik Go)"},{"utwu_id":"utwu-000604","spotify_id":"0KeTYvIucwFVN2mNqcaHN3","spotify_order":"335","title_original":"Who are you ?","title_normalized":"who are you ?","title_parsed":"who are you","artist_original":"Louis Aguilar","artist_normalized":"louis aguilar","artist_parsed":"louis aguilar","album_original":"Who are you ?"},{"utwu_id":"utwu-000595","spotify_id":"3NVzrwDFsl9YG4Vaj924NN","spotify_order":"344","title_original":"Om Maṇi Padme Hūm","title_normalized":"om maṇi padme hūm","title_parsed":"om mani padme hum","artist_original":"Gaiea Sanskrit","artist_normalized":"gaiea sanskrit","artist_parsed":"gaiea sanskrit","album_original":"Powerful Sanskrit Mantras"},{"utwu_id":"utwu-000594","spotify_id":"2owq11I1uoyyOPNbzL0pW1","spotify_order":"345","title_original":"To Remove Fear","title_normalized":"to remove fear","title_parsed":"to remove fear","artist_original":"Gaiea Sanskrit","artist_normalized":"gaiea sanskrit","artist_parsed":"gaiea sanskrit","album_original":"Powerful Sanskrit Mantras"},{"utwu_id":"utwu-000593","spotify_id":"2xWnlp8263yjHJv81vrDoM","spotify_order":"346","title_original":"Vajrasattva","title_normalized":"vajrasattva","title_parsed":"vajrasattva","artist_original":"Gaiea Sanskrit","artist_normalized":"gaiea sanskrit","artist_parsed":"gaiea sanskrit","album_original":"Breath Of God"},{"utwu_id":"utwu-000592","spotify_id":"5oM7rBOmOJgP95iN2ulzGT","spotify_order":"347","title_original":"Heart Sutra","title_normalized":"heart sutra","title_parsed":"heart sutra","artist_original":"Gaiea Sanskrit","artist_normalized":"gaiea sanskrit","artist_parsed":"gaiea sanskrit","album_original":"Sanskrit Medicine Mantras"},{"utwu_id":"utwu-000569","spotify_id":"6yEfNY4hAzCtckKBdLFH6f","spotify_order":"370","title_original":"Złote łezki","title_normalized":"złote łezki","title_parsed":"złote łezki","artist_original":"Meek, Oh Why?, BIESY","artist_normalized":"meek, oh why?, biesy","artist_parsed":"meek | oh why | biesy","album_original":"Złote łezki"},{"utwu_id":"utwu-000551","spotify_id":"7KWpUSHVTL6X6vpuFRQBAi","spotify_order":"388","title_original":"Man","title_normalized":"man","title_parsed":"man","artist_original":"Elvett","artist_normalized":"elvett","artist_parsed":"elvett","album_original":"Man"},{"utwu_id":"utwu-000544","spotify_id":"2CIsc2LDQrcE40s95aoocT","spotify_order":"395","title_original":"Prząśniczka","title_normalized":"prząśniczka","title_parsed":"przasniczka","artist_original":"Olga Pasiecznik, Ewa Pobłocka","artist_normalized":"olga pasiecznik, ewa pobłocka","artist_parsed":"olga pasiecznik | ewa pobłocka","album_original":"Stanisław Moniuszko: Pieśni"},{"utwu_id":"utwu-000543","spotify_id":"5etkQpmZeBbQc60sSCc9dt","spotify_order":"396","title_original":"Moniuszko: Prząśniczka","title_normalized":"moniuszko: prząśniczka","title_parsed":"moniuszko przasniczka","artist_original":"Stanisław Moniuszko, Jakub Józef Orliński, Aleksander Dębicz","artist_normalized":"stanisław moniuszko, jakub józef orliński, aleksander dębicz","artist_parsed":"stanisław moniuszko | jakub jozef orlinski | aleksander debicz","album_original":"Moniuszko: Prząśniczka"},{"utwu_id":"utwu-000467","spotify_id":"3USAWsibaJCljQzlR4QWIv","spotify_order":"472","title_original":"Fairytales","title_normalized":"fairytales","title_parsed":"fairytales","artist_original":"Ami Warning","artist_normalized":"ami warning","artist_parsed":"ami warning","album_original":"Seasons"},{"utwu_id":"utwu-000461","spotify_id":"03QDUD4o205b5aclvPXSkT","spotify_order":"478","title_original":"Freedom","title_normalized":"freedom","title_parsed":"freedom","artist_original":"London Score Orchestra","artist_normalized":"london score orchestra","artist_parsed":"london score orchestra","album_original":"Tarantino the Collection"},{"utwu_id":"utwu-000448","spotify_id":"7oF5VnIPiVyZxWQurUXh5Z","spotify_order":"491","title_original":"Qui sait","title_normalized":"qui sait","title_parsed":"qui sait","artist_original":"Ezéchiel Pailhès","artist_normalized":"ezéchiel pailhès","artist_parsed":"ezechiel pailhes","album_original":"Divine"},{"utwu_id":"utwu-000399","spotify_id":"3Sjzioq6pR8z7wnKgLE5yl","spotify_order":"540","title_original":"Video Games - Radio edit","title_normalized":"video games - radio edit","title_parsed":"video games radio edit","artist_original":"Trio SR9, Sandra Nkaké","artist_normalized":"trio sr9, sandra nkaké","artist_parsed":"trio sr9 | sandra nkake","album_original":"Video Games (Radio edit)"},{"utwu_id":"utwu-000398","spotify_id":"0jrp6HSRyI0ewltX3XH5JA","spotify_order":"541","title_original":"Call Me","title_normalized":"call me","title_parsed":"call me","artist_original":"Skye","artist_normalized":"skye","artist_parsed":"skye","album_original":"Hollywood, mon amour (80's Movie Songs Reinvented)"},{"utwu_id":"utwu-000389","spotify_id":"4S4dsfH5ZeDSVs56NRbuVD","spotify_order":"550","title_original":"Juz nigdy","title_normalized":"juz nigdy","title_parsed":"juz nigdy","artist_original":"Mieczysław Fogg","artist_normalized":"mieczysław fogg","artist_parsed":"mieczysław fogg","album_original":"Co nam zostalo z tych lat - cykl 1"},{"utwu_id":"utwu-000372","spotify_id":"4s4egs79fvp5UQYsRSDrUY","spotify_order":"567","title_original":"Onna no Yujyo - 1934 Edit","title_normalized":"onna no yujyo - 1934 edit","title_parsed":"onna no yujyo 1934 edit","artist_original":"R Vincenzo","artist_normalized":"r vincenzo","artist_parsed":"r vincenzo","album_original":"EP"},{"utwu_id":"utwu-000369","spotify_id":"3Mnhi3krYvlWJMh4dfhPpy","spotify_order":"570","title_original":"Get the Party Started (Originally Performed By Shirley Bassey) [Full Vocal Version]","title_normalized":"get the party started (originally performed by shirley bassey) [full vocal version]","title_parsed":"get the party started originally performed by shirley bassey full vocal version","artist_original":"Chart Collective","artist_normalized":"chart collective","artist_parsed":"chart collective","album_original":"Karaoke Shirley Bassey, Vol. 2"},{"utwu_id":"utwu-000363","spotify_id":"5KEk9cyq1dnQa6g4JFS72W","spotify_order":"576","title_original":"Bed Of Stone","title_normalized":"bed of stone","title_parsed":"bed of stone","artist_original":"Tiwayo","artist_normalized":"tiwayo","artist_parsed":"tiwayo","album_original":"The Gypsy Soul Of Tiwayo"},{"utwu_id":"utwu-000361","spotify_id":"5ocg5H6tZKhjBU0sjsXZvc","spotify_order":"578","title_original":"In the Land of Your Soul","title_normalized":"in the land of your soul","title_parsed":"in the land of your soul","artist_original":"Nicolas Repac","artist_normalized":"nicolas repac","artist_parsed":"nicolas repac","album_original":"Rhapsodic"},{"utwu_id":"utwu-000346","spotify_id":"5I77RxtGq8bEvizYJkZM0N","spotify_order":"593","title_original":"Silent Talk","title_normalized":"silent talk","title_parsed":"silent talk","artist_original":"Catastrophe Waitress","artist_normalized":"catastrophe waitress","artist_parsed":"catastrophe waitress","album_original":"Silent Talk"},{"utwu_id":"utwu-000339","spotify_id":"5rJhl1nP2MQ4rlhOAMrb7a","spotify_order":"600","title_original":"De Glace","title_normalized":"de glace","title_parsed":"de glace","artist_original":"Sammy Decoster","artist_normalized":"sammy decoster","artist_parsed":"sammy decoster","album_original":"Sortie 21"},{"utwu_id":"utwu-000329","spotify_id":"2TbrVvMrXgVjA1rv6rXMom","spotify_order":"610","title_original":"Sugarman","title_normalized":"sugarman","title_parsed":"sugarman","artist_original":"Ndidi O","artist_normalized":"ndidi o","artist_parsed":"ndidi o","album_original":"Dark Swing"},{"utwu_id":"utwu-000324","spotify_id":"6f0OSlCKwA1OsqX0v6XrT2","spotify_order":"615","title_original":"You Can't Run from the Devil","title_normalized":"you can't run from the devil","title_parsed":"you can t run from the devil","artist_original":"Digger Barnes","artist_normalized":"digger barnes","artist_parsed":"digger barnes","album_original":"Near Exit 27"},{"utwu_id":"utwu-000320","spotify_id":"3TX2AAnuap3U0a1DR5KRtQ","spotify_order":"619","title_original":"La Vida De Los Uruguayos","title_normalized":"la vida de los uruguayos","title_parsed":"la vida de los uruguayos","artist_original":"The Bas Lexter Ensample","artist_normalized":"the bas lexter ensample","artist_parsed":"the bas lexter ensample","album_original":"Truncate It Right"},{"utwu_id":"utwu-000314","spotify_id":"3UZuRa4jawcfmiUbe1CaFV","spotify_order":"625","title_original":"Piangi con me","title_normalized":"piangi con me","title_parsed":"piangi con me","artist_original":"Bee Bee Sea","artist_normalized":"bee bee sea","artist_parsed":"bee bee sea","album_original":"Piangi con me"},{"utwu_id":"utwu-000238","spotify_id":"5d8J6r6ZkNVbLw2S6VCDNH","spotify_order":"701","title_original":"Je broie du noir","title_normalized":"je broie du noir","title_parsed":"je broie du noir","artist_original":"Lisa Mélissa & The Mess","artist_normalized":"lisa mélissa & the mess","artist_parsed":"lisa melissa | the mess","album_original":"Je broie du noir"},{"utwu_id":"utwu-000235","spotify_id":"2jL3y2d8azHZ6WJmB08Dxn","spotify_order":"704","title_original":"Getting Old","title_normalized":"getting old","title_parsed":"getting old","artist_original":"Felix Laband","artist_normalized":"felix laband","artist_parsed":"felix laband","album_original":"Deaf Safari"},{"utwu_id":"utwu-000198","spotify_id":"37gnxr7LvByMQwzSudAQPK","spotify_order":"741","title_original":"Make It Wit Chu","title_normalized":"make it wit chu","title_parsed":"make it wit chu","artist_original":"Olivier Libaux, Mélanie Pain","artist_normalized":"olivier libaux, mélanie pain","artist_parsed":"olivier libaux | melanie pain","album_original":"Make It Wit Chu"},{"utwu_id":"utwu-000149","spotify_id":"0MHR1fEriY1sBZHQuE8iAI","spotify_order":"790","title_original":"Do polityka","title_normalized":"do polityka","title_parsed":"do polityka","artist_original":"Zbigniew Preisner, Anna Szałapak","artist_normalized":"zbigniew preisner, anna szałapak","artist_parsed":"zbigniew preisner | anna szałapak","album_original":"Głosy"},{"utwu_id":"utwu-000133","spotify_id":"1xJvn7nufiBc8A5isZxwGs","spotify_order":"806","title_original":"Tcheren Deya","title_normalized":"tcheren deya","title_parsed":"tcheren deya","artist_original":"Mathias Duplessy","artist_normalized":"mathias duplessy","artist_parsed":"mathias duplessy","album_original":"My Mongolia"},{"utwu_id":"utwu-000125","spotify_id":"6kK1twz2ZFcmJ6Bgz3dXTD","spotify_order":"814","title_original":"Nektar","title_normalized":"nektar","title_parsed":"nektar","artist_original":"Skarby, Błękit","artist_normalized":"skarby, błękit","artist_parsed":"skarby | błekit","album_original":"Nektar"},{"utwu_id":"utwu-000098","spotify_id":"2Y9O5gdWTSdBzYBnojnr8N","spotify_order":"841","title_original":"The Station","title_normalized":"the station","title_parsed":"the station","artist_original":"Izzy and the Black Trees, Kev Fox","artist_normalized":"izzy and the black trees, kev fox","artist_parsed":"izzy | the black trees | kev fox","album_original":"The Station"},{"utwu_id":"utwu-000073","spotify_id":"4B9hMTO37anEZicqEVZ9Rz","spotify_order":"866","title_original":"Loud","title_normalized":"loud","title_parsed":"loud","artist_original":"JJ Kamei","artist_normalized":"jj kamei","artist_parsed":"jj kamei","album_original":"My Angels"},{"utwu_id":"utwu-000067","spotify_id":"0GD99QvkSnDq1dNKbsujcq","spotify_order":"872","title_original":"Love Theme from \"Phaedra\"","title_normalized":"love theme from \"phaedra\"","title_parsed":"love theme from phaedra","artist_original":"Dreamers Inc., Mikis Theodorakis, Meditelectro, Melina Mercouri","artist_normalized":"dreamers inc., mikis theodorakis, meditelectro, melina mercouri","artist_parsed":"dreamers inc | mikis theodorakis | meditelectro | melina mercouri","album_original":"Digitalik"},{"utwu_id":"utwu-000063","spotify_id":"09wpjeyOBaXCJkIUHW4bOY","spotify_order":"876","title_original":"Video Games","title_normalized":"video games","title_parsed":"video games","artist_original":"Moss","artist_normalized":"moss","artist_parsed":"moss","album_original":"Video Games"},{"utwu_id":"utwu-000042","spotify_id":"3qbA1asuGsDV5A3D2qeXEa","spotify_order":"897","title_original":"Jeg Drømmer Om En Sang","title_normalized":"jeg drømmer om en sang","title_parsed":"jeg drømmer om en sang","artist_original":"Claus Hempler","artist_normalized":"claus hempler","artist_parsed":"claus hempler","album_original":"Kuffert Fuld Af Mursten"},{"utwu_id":"utwu-000037","spotify_id":"3tBTXJ4n3xIqMQIgxc0Dxj","spotify_order":"902","title_original":"Zomer Van Ons Leven","title_normalized":"zomer van ons leven","title_parsed":"zomer van ons leven","artist_original":"Lenny En De Wespen, Jack Parow","artist_normalized":"lenny en de wespen, jack parow","artist_parsed":"lenny en de wespen | jack parow","album_original":"Zomer Van Ons Leven"},{"utwu_id":"utwu-000036","spotify_id":"5Cya2NpLNEH4o4m9lYXu9K","spotify_order":"903","title_original":"You Misread Me","title_normalized":"you misread me","title_parsed":"you misread me","artist_original":"Portland","artist_normalized":"portland","artist_parsed":"portland","album_original":"Your Colours Will Stain"}]

OUTPUT_COLUMNS = [
    "utwu_id", "spotify_id", "spotify_order",
    "title_original", "artist_original", "album_original",
    "lyrics_status", "lyrics", "lyrics_source", "lyrics_source_ref",
    "lyrics_match_score", "lyrics_match_method", "lyrics_query_title",
    "lyrics_query_artist", "lyrics_note",
]

VERSION_WORDS = {
    "remaster", "remastered", "remastering", "live", "radio edit", "edit",
    "version", "mix", "remix", "alt mix", "alternative mix", "single version",
    "album version", "acoustic", "instrumental", "orchestral version",
    "soprano version", "full vocal version", "originally performed by",
    "from soundtrack", "soundtrack", "bonus track", "demo", "mono", "stereo",
}

SPECIAL_LATIN = str.maketrans({
    "ł":"l", "Ł":"L", "ø":"o", "Ø":"O", "đ":"d", "Đ":"D",
    "ð":"d", "Ð":"D", "þ":"th", "Þ":"Th", "æ":"ae", "Æ":"AE",
    "œ":"oe", "Œ":"OE", "ß":"ss", "ħ":"h", "ı":"i",
})

CYRILLIC_GENERIC = {
    "А":"A","а":"a","Б":"B","б":"b","В":"V","в":"v","Г":"G","г":"g",
    "Ґ":"G","ґ":"g","Д":"D","д":"d","Е":"E","е":"e","Ё":"Yo","ё":"yo",
    "Є":"Ye","є":"ye","Ж":"Zh","ж":"zh","З":"Z","з":"z","И":"I","и":"i",
    "І":"I","і":"i","Ї":"Yi","ї":"yi","Й":"Y","й":"y","К":"K","к":"k",
    "Л":"L","л":"l","М":"M","м":"m","Н":"N","н":"n","О":"O","о":"o",
    "П":"P","п":"p","Р":"R","р":"r","С":"S","с":"s","Т":"T","т":"t",
    "У":"U","у":"u","Ф":"F","ф":"f","Х":"Kh","х":"kh","Ц":"Ts","ц":"ts",
    "Ч":"Ch","ч":"ch","Ш":"Sh","ш":"sh","Щ":"Shch","щ":"shch","Ъ":"","ъ":"",
    "Ы":"Y","ы":"y","Ь":"","ь":"","Э":"E","э":"e","Ю":"Yu","ю":"yu",
    "Я":"Ya","я":"ya","Ј":"J","ј":"j","Љ":"Lj","љ":"lj","Њ":"Nj","њ":"nj",
    "Ѓ":"Gj","ѓ":"gj","Ќ":"Kj","ќ":"kj","Ѕ":"Dz","ѕ":"dz","Џ":"Dzh","џ":"dzh",
    "Ђ":"Dj","ђ":"dj","Ћ":"C","ћ":"c",
}

CYRILLIC_UKRAINIAN = dict(CYRILLIC_GENERIC)
CYRILLIC_UKRAINIAN.update({
    "Г":"H","г":"h","И":"Y","и":"y","І":"I","і":"i","Ї":"Yi","ї":"yi",
    "Є":"Ye","є":"ye","Й":"Y","й":"y",
})

# Aliasy dzieł używane TYLKO w specjalnej gałęzi. Jeśli znajdziemy tekst
# po samym dziele, ale nie potwierdzimy wykonawcy, wynik będzie canonicaltext.
WORK_ALIASES = {
    "utwu-000937": ["Carol of the Bells", "Carol of Bells"],
    "utwu-000935": ["Vajrasattva Mantra", "100 Syllable Vajrasattva Mantra", "Hundred Syllable Vajrasattva Mantra"],
    "utwu-000934": ["The Carol of the Old Ones", "Carol of the Old Ones"],
    "utwu-000926": ["Bhagavad Gita Chapter 11", "Bhagavad Gita 11", "Vishvarupa Darshana Yoga"],
    "utwu-000925": ["Shchedryk", "Carol of the Bells", "Shchedryk Carol of the Bells"],
    "utwu-000924": ["Ajai Alai", "Ajai Alai Mantra"],
    "utwu-000890": ["Щедрик", "Shchedryk", "Szczedryk"],
    "utwu-000817": ["Mahler Symphony No. 5 Trauermarsch", "Symphony No. 5 Trauermarsch"],
    "utwu-000808": ["Beethoven Symphony No. 9 Adagio molto e cantabile", "Symphony No. 9 III Adagio molto e cantabile"],
    "utwu-000671": ["Shiva Sankalpa Suktam", "Shiva Sankalpa Sukta"],
    "utwu-000670": ["Durga Suktam", "Durga Sukta"],
    "utwu-000595": ["Om Mani Padme Hum", "Om Mani Padme Hum Mantra"],
    "utwu-000593": ["Vajrasattva", "Vajrasattva Mantra", "100 Syllable Vajrasattva Mantra"],
    "utwu-000592": ["Heart Sutra", "Prajnaparamita Hridaya Sutra", "Heart Sutra Sanskrit"],
    "utwu-000544": ["Prząśniczka", "Przasniczka", "Moniuszko Prząśniczka"],
    "utwu-000543": ["Prząśniczka", "Przasniczka", "Moniuszko Prząśniczka"],
}


def _map_chars(text, mapping):
    return "".join(mapping.get(ch, ch) for ch in text)


def strip_marks(text):
    text = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in text if not unicodedata.combining(ch))


def latin_ascii(text):
    text = "" if text is None else str(text)
    text = text.translate(SPECIAL_LATIN)
    text = strip_marks(text)
    return text.encode("ascii", "ignore").decode("ascii")


def transliterate_generic(text):
    text = "" if text is None else str(text)
    text = _map_chars(text, CYRILLIC_GENERIC)
    text = text.translate(SPECIAL_LATIN)
    text = strip_marks(text)
    return text.encode("ascii", "ignore").decode("ascii")


def transliterate_ukrainian(text):
    text = "" if text is None else str(text)
    text = _map_chars(text, CYRILLIC_UKRAINIAN)
    text = text.translate(SPECIAL_LATIN)
    text = strip_marks(text)
    return text.encode("ascii", "ignore").decode("ascii")


def raw_key(text):
    text = "" if text is None else str(text)
    text = unicodedata.normalize("NFC", text).casefold()
    text = re.sub(r"\s+", " ", text).strip()
    return text


def unique_query(values, limit=None):
    """Deduplikacja zapytań bez zjadania wariantu ASCII."""
    out, seen = [], set()
    for value in values:
        value = "" if value is None else str(value).strip()
        key = raw_key(value)
        if value and key not in seen:
            seen.add(key)
            out.append(value)
            if limit and len(out) >= limit:
                break
    return out


def match_norm(text):
    """Normalizacja tylko do porównywania kandydatów, NIE do deduplikacji zapytań."""
    text = transliterate_generic(text).casefold()
    text = text.replace("&", " and ")
    text = re.sub(r"[\u2010-\u2015]", "-", text)
    text = re.sub(r"[^a-z0-9\s]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def similarity(a, b):
    a, b = match_norm(a), match_norm(b)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    return SequenceMatcher(None, a, b).ratio()


def simplify_title(title):
    if not title:
        return ""
    s = str(title).strip()

    # feat./ft./featuring w nawiasie albo na końcu
    s = re.sub(r"\s*[\(\[]\s*(?:feat\.?|ft\.?|featuring)\b.*?[\)\]]\s*", " ", s, flags=re.I)
    s = re.sub(r"\s+(?:feat\.?|ft\.?|featuring)\b.*$", "", s, flags=re.I)

    # originally performed by ... także jeśli siedzi w nawiasie
    s = re.sub(r"\s*[\(\[]?\s*originally performed by\b.*?[\)\]]?\s*$", "", s, flags=re.I)

    # końcowe nawiasy opisujące wersję
    def bracket_repl(m):
        inside = m.group(1)
        low = inside.casefold()
        if any(word in low for word in VERSION_WORDS):
            return " "
        return m.group(0)
    s = re.sub(r"\s*[\(\[]([^\)\]]+)[\)\]]\s*$", bracket_repl, s)

    # suffix po myślniku
    parts = re.split(r"\s+[-–—]\s+", s)
    if len(parts) > 1:
        tail = parts[-1].casefold()
        if any(word in tail for word in VERSION_WORDS) or re.search(r"\b(?:19|20)\d{2}\s+edit\b", tail):
            s = " - ".join(parts[:-1])

    # samodzielne końcowe określenia
    s = re.sub(
        r"\s+(?:radio\s+edit|live(?:\s+in\s+.+)?|remaster(?:ed)?(?:\s+\d{4})?|"
        r"(?:19|20)\d{2}\s+edit|full\s+vocal\s+version|soprano\s+version|"
        r"orchestral\s+version|instrumental|alt[- ]mix(?:\s+by\s+.+)?)\s*$",
        "", s, flags=re.I,
    )
    return re.sub(r"\s+", " ", s).strip(" -–—[]()")


def title_fragments(title):
    """Rozbija ozdobne wieloczłonowe tytuły, ale zachowuje także pełny tytuł."""
    if not title:
        return []
    s = str(title).strip()
    out = []
    # Najmocniejsze separatory metadanych/ozdobników.
    for part in re.split(r"\s*(?:\||●|;|•)\s*", s):
        part = part.strip(" -–—:;|●•")
        if len(part) >= 3:
            out.append(part)
    # Dwukropek często rozdziela tytuł od objaśnienia.
    if ":" in s:
        for part in s.split(":"):
            part = part.strip(" -–—:;|●•")
            if len(part) >= 4:
                out.append(part)
    return out


def ascii_variants(value):
    vals = [value, latin_ascii(value), transliterate_generic(value), transliterate_ukrainian(value)]
    return unique_query(vals)


def title_variants(row):
    bases = unique_query([
        row.get("title_original", ""),
        row.get("title_normalized", ""),
        row.get("title_parsed", ""),
    ])
    vals = []
    for base in bases:
        vals.extend(ascii_variants(base))
        simp = simplify_title(base)
        vals.extend(ascii_variants(simp))
        for frag in title_fragments(base):
            vals.extend(ascii_variants(frag))
            vals.extend(ascii_variants(simplify_title(frag)))
    # UWAGA: aliasy DZIEŁA nie należą do identyfikacji konkretnego nagrania.
    # WORK_ALIASES są używane wyłącznie w canonical_work_branch().
    return unique_query(vals, limit=28)


def split_artists_original(text):
    """Celowo NIE rozcina po 'and' ani '&'."""
    if not text:
        return []
    s = str(text).strip()
    # przecinek i średnik są w naszych danych realnymi separatorami wykonawców
    parts = re.split(r"\s*[,;]\s*", s)
    out = []
    for p in parts:
        p = re.sub(r"^(?:feat\.?|ft\.?|featuring)\s+", "", p, flags=re.I).strip()
        if p:
            out.append(p)
    return out


def artist_variants(row):
    original = row.get("artist_original", "")
    vals = [original, row.get("artist_normalized", ""), row.get("artist_parsed", "")]
    vals.extend(split_artists_original(original))
    # Wariant bez części po feat./ft., jeśli wystąpiła w pełnym zapisie.
    vals.append(re.split(r"\s+(?:feat\.?|ft\.?|featuring)\s+", original, maxsplit=1, flags=re.I)[0])
    expanded = []
    for v in vals:
        expanded.extend(ascii_variants(v))
    return unique_query(expanded, limit=18)


def album_variants(row):
    vals = []
    for v in [row.get("album_original", "")]:
        vals.extend(ascii_variants(v))
    return unique_query(vals, limit=5)


def request(url, params=None):
    if params:
        query = urllib.parse.urlencode(params, doseq=True)
        url += ("&" if "?" in url else "?") + query
    for attempt in range(RETRIES):
        req = urllib.request.Request(url, headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json,text/plain,application/xml,text/xml,*/*",
        })
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return response.read(), charset
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, None
            if e.code == 429 or 500 <= e.code < 600:
                time.sleep(1.0 + attempt * 1.5)
                continue
            return None, None
        except (urllib.error.URLError, TimeoutError):
            time.sleep(0.8 + attempt * 1.2)
    return None, None


def get_json(url, params=None):
    raw, charset = request(url, params)
    if not raw:
        return None
    try:
        return json.loads(raw.decode(charset or "utf-8", errors="replace"))
    except Exception:
        return None


def get_text(url, params=None):
    raw, charset = request(url, params)
    if not raw:
        return None
    return raw.decode(charset or "utf-8", errors="replace")


def clean_lyrics(text):
    if not text:
        return ""
    text = html.unescape(str(text))
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"(?m)^(?:\[[0-9]{1,2}:[0-9]{2}(?:\.[0-9]{1,3})?\])+", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def score_candidate(row, cand_title, cand_artist, cand_album="", aliases=None):
    titles = title_variants(row)
    if aliases:
        titles = unique_query(list(titles) + list(aliases))
    artists = artist_variants(row)
    albums = album_variants(row)
    st = max((similarity(x, cand_title) for x in titles), default=0.0)
    sa = max((similarity(x, cand_artist) for x in artists), default=0.0) if cand_artist else 0.0
    salb = max((similarity(x, cand_album) for x in albums), default=0.0) if cand_album and albums else 0.0
    score = 0.67 * st + 0.30 * sa + 0.03 * salb
    return score, st, sa


def acceptable(score, st, sa):
    # Świadomie ostrzej niż v01: mniej fałszywych trafień.
    if st >= 0.985 and sa >= 0.62:
        return True
    if st >= 0.94 and sa >= 0.74 and score >= 0.84:
        return True
    return score >= 0.88 and st >= 0.88 and sa >= 0.82


def work_title_score(row, cand_title):
    aliases = WORK_ALIASES.get(row.get("utwu_id", ""), [])
    if not aliases:
        return 0.0
    variants = []
    for a in aliases:
        variants.extend(ascii_variants(a))
    return max((similarity(a, cand_title) for a in variants), default=0.0)


def make_result(status, lyrics, source, ref, score, method, qtitle, qartist, note):
    return {
        "status": status,
        "lyrics": clean_lyrics(lyrics),
        "source": source,
        "ref": str(ref or ""),
        "score": float(score or 0.0),
        "method": method,
        "qtitle": qtitle or "",
        "qartist": qartist or "",
        "note": note or "",
    }


def query_pairs(row, max_pairs=34):
    titles = title_variants(row)
    artists = artist_variants(row)
    pairs = []
    if not titles:
        return []
    if not artists:
        return [(t, "") for t in titles[:max_pairs]]

    # Każdy ważny wariant tytułu z głównym wykonawcą.
    for t in titles[:18]:
        pairs.append((t, artists[0]))
    # Oryginalny/simplified tytuł z każdym wariantem wykonawcy.
    for a in artists[:12]:
        pairs.append((titles[0], a))
        if len(titles) > 1:
            pairs.append((titles[1], a))

    out, seen = [], set()
    for t, a in pairs:
        key = (raw_key(t), raw_key(a))
        if t and key not in seen:
            seen.add(key)
            out.append((t, a))
            if len(out) >= max_pairs:
                break
    return out


def lrclib(row):
    candidates = []
    seen = set()
    for qtitle, qartist in query_pairs(row):
        params = {"track_name": qtitle}
        if qartist:
            params["artist_name"] = qartist
        data = get_json("https://lrclib.net/api/search", params)
        time.sleep(PAUSE)
        if not isinstance(data, list):
            continue
        for c in data:
            key = c.get("id") or (raw_key(c.get("trackName") or c.get("name")), raw_key(c.get("artistName")))
            if key in seen:
                continue
            seen.add(key)
            ctitle = c.get("trackName") or c.get("name") or ""
            cartist = c.get("artistName") or ""
            calbum = c.get("albumName") or ""
            score, st, sa = score_candidate(row, ctitle, cartist, calbum)
            candidates.append((score, st, sa, qtitle, qartist, c))

    candidates.sort(key=lambda x: x[0], reverse=True)
    for score, st, sa, qtitle, qartist, c in candidates:
        if not acceptable(score, st, sa):
            continue
        note = f"{c.get('artistName','')} — {c.get('trackName') or c.get('name','')}"
        if c.get("instrumental") is True:
            return make_result("instrumental", "", "lrclib", c.get("id"), score, "metadata-match", qtitle, qartist, note)
        lyrics = clean_lyrics(c.get("plainLyrics") or c.get("syncedLyrics") or "")
        if lyrics:
            # Osłona na znany fałszywy rekord z pierwszej tury.
            if row.get("utwu_id") == "utwu-000937" and "bell" not in match_norm(lyrics):
                continue
            return make_result("found", lyrics, "lrclib", c.get("id"), score, "metadata-match", qtitle, qartist, note)
    return None


def lyrics_ovh(row):
    for qtitle, qartist in query_pairs(row, max_pairs=24):
        if not qartist:
            continue
        url = "https://api.lyrics.ovh/v1/" + urllib.parse.quote(qartist, safe="") + "/" + urllib.parse.quote(qtitle, safe="")
        data = get_json(url)
        time.sleep(PAUSE)
        if not isinstance(data, dict):
            continue
        lyrics = clean_lyrics(data.get("lyrics"))
        if lyrics:
            # lyrics.ovh nie zwraca metadanych kandydata, więc jako scoring bierzemy
            # siłę samego wariantu zapytania względem rekordu źródłowego.
            st = max(similarity(qtitle, t) for t in title_variants(row))
            sa = max(similarity(qartist, a) for a in artist_variants(row))
            score = 0.69 * st + 0.31 * sa
            if score >= 0.82:
                return make_result("found", lyrics, "lyrics.ovh", "", score, "direct-query", qtitle, qartist, "bezpośrednie artist/title")
    return None


def chartlyrics(row):
    for qtitle, qartist in query_pairs(row, max_pairs=22):
        if not qartist:
            continue
        text = get_text("https://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect", {"artist": qartist, "song": qtitle})
        time.sleep(PAUSE)
        if not text:
            continue
        try:
            root = ET.fromstring(text)
        except ET.ParseError:
            continue
        def first_text(name):
            for elem in root.iter():
                if elem.tag.split("}")[-1] == name:
                    return elem.text or ""
            return ""
        lyrics = clean_lyrics(first_text("Lyric"))
        if not lyrics:
            continue
        ctitle = first_text("LyricSong") or qtitle
        cartist = first_text("LyricArtist") or qartist
        score, st, sa = score_candidate(row, ctitle, cartist)
        if acceptable(score, st, sa):
            return make_result("found", lyrics, "chartlyrics", first_text("LyricId"), score, "metadata-match", qtitle, qartist, f"{cartist} — {ctitle}")
    return None


def canonical_work_branch(row):
    """
    Canonical work lookup.

    WAŻNE:
    - NIE używa artist_original / artist_normalized / artist_parsed jako klucza,
    - NIE wymaga zgodności wykonawcy,
    - NIE dodaje zgodności wykonawcy do score,
    - identyfikuje wyłącznie dzieło po kontrolowanej liście WORK_ALIASES.

    Wykonawca konkretnego nagrania pozostaje metadaną rekordu utwu_id.
    Wykonawca zwrócony przez źródło jest zapisywany wyłącznie w notatce
    o pochodzeniu kandydata, nigdy jako dowód autorstwa tekstu.
    """
    aliases = WORK_ALIASES.get(row.get("utwu_id", ""), [])
    if not aliases:
        return None

    canonical_aliases = unique_query(
        sum((ascii_variants(a) for a in aliases), []),
        limit=18,
    )

    # Dwa niezależne tryby LRCLIB bez artist_name:
    # 1) track_name: bardziej precyzyjny,
    # 2) q: szerszy fallback.
    # W obu przypadkach scoring jest WYŁĄCZNIE po tożsamości dzieła.
    seen = set()
    best_text = None
    best_instrumental = None

    for alias in canonical_aliases:
        searches = [
            ("canonical-track-name", {"track_name": alias}),
            ("canonical-q", {"q": alias}),
        ]

        for method, params in searches:
            data = get_json("https://lrclib.net/api/search", params)
            time.sleep(PAUSE)
            if not isinstance(data, list):
                continue

            for c in data:
                key = c.get("id") or (
                    raw_key(c.get("trackName") or c.get("name")),
                    raw_key(c.get("artistName")),
                )
                if key in seen:
                    continue
                seen.add(key)

                ctitle = c.get("trackName") or c.get("name") or ""
                source_artist = c.get("artistName") or ""

                # TU CELOWO NIE MA artist score.
                stw = work_title_score(row, ctitle)
                if stw < 0.93:
                    continue

                provenance = (
                    f"canonical work match: {ctitle}; "
                    f"wykonawca w źródle={source_artist or '[brak]'}; "
                    f"wykonawca nie uczestniczył w wyszukiwaniu ani scoringu"
                )

                if c.get("instrumental") is True:
                    candidate = make_result(
                        "candidate_instrumental",
                        "",
                        "lrclib",
                        c.get("id"),
                        stw,
                        method,
                        alias,
                        "",
                        provenance + "; źródło oznacza ten wariant jako instrumentalny",
                    )
                    if (
                        best_instrumental is None
                        or candidate["score"] > best_instrumental["score"]
                    ):
                        best_instrumental = candidate
                    continue

                lyrics = clean_lyrics(
                    c.get("plainLyrics") or c.get("syncedLyrics") or ""
                )
                if not lyrics:
                    continue

                # Znany false positive z poprzedniej tury.
                if row.get("utwu_id") == "utwu-000937" and "bell" not in match_norm(lyrics):
                    continue

                candidate = make_result(
                    "canonicaltext",
                    lyrics,
                    "lrclib",
                    c.get("id"),
                    stw,
                    method,
                    alias,
                    "",
                    provenance,
                )
                if best_text is None or candidate["score"] > best_text["score"]:
                    best_text = candidate

    # Tekst dzieła ma pierwszeństwo przed informacją, że jakieś inne wykonanie
    # tego dzieła było instrumentalne.
    if best_text is not None:
        return best_text
    return best_instrumental


def identify_recording(row):
    """
    Identyfikacja KONKRETNEGO NAGRANIA.

    Ta ścieżka może używać artist_* i albumu, bo jej pytanie brzmi:
    "czy znaleziony tekst należy do tego konkretnego wykonania / wersji?".

    Celowo NIE używa WORK_ALIASES. Alias dzieła nie jest aliasem nagrania.
    """
    for provider in (lrclib, lyrics_ovh, chartlyrics):
        try:
            result = provider(row)
            if result:
                return result
        except Exception as exc:
            print(f"    {provider.__name__}: błąd {exc}")
    return None


def identify_canonical_text(row):
    """
    Identyfikacja KANONICZNEGO TEKSTU DZIEŁA.

    Ta ścieżka jest niezależna od wykonawcy konkretnego nagrania:
    - szuka po WORK_ALIASES / nazwie dzieła,
    - nie wysyła artist_* jako warunku,
    - nie używa artist_* w scoringu,
    - wynik tekstowy ma status canonicaltext, nie found.
    """
    try:
        return canonical_work_branch(row)
    except Exception as exc:
        print(f"    canonical_work_branch: błąd {exc}")
        return None


def fetch_one(row):
    # ETAP 1: konkretne nagranie.
    result = identify_recording(row)
    if result:
        return result

    # ETAP 2: osobna tożsamość dzieła / tekstu kanonicznego.
    result = identify_canonical_text(row)
    if result:
        return result

    return make_result("missing", "", "", "", 0.0, "", "", "", "Brak tekstu w użytych źródłach i wariantach.")


def save_new_file(rows):
    folder = Path(__file__).resolve().parent
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = f"szukamy-slow-pobrane-2pass-{stamp}"
    output_path = folder / f"{base}.csv"
    counter = 1
    while output_path.exists():
        output_path = folder / f"{base}-{counter:02d}.csv"
        counter += 1
    with output_path.open("x", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return output_path


def main():
    results = []
    counts = {"found":0, "canonicaltext":0, "instrumental":0, "candidate_instrumental":0, "missing":0}
    total = len(TRACKS)
    for i, row in enumerate(TRACKS, start=1):
        artist = row.get("artist_original", "")
        title = row.get("title_original", "")
        print(f"[{i}/{total}] {artist} — {title}")
        result = fetch_one(row)
        out = {
            "utwu_id": row.get("utwu_id", ""),
            "spotify_id": row.get("spotify_id", ""),
            "spotify_order": row.get("spotify_order", ""),
            "title_original": title,
            "artist_original": artist,
            "album_original": row.get("album_original", ""),
            "lyrics_status": result["status"],
            "lyrics": result["lyrics"],
            "lyrics_source": result["source"],
            "lyrics_source_ref": result["ref"],
            "lyrics_match_score": f"{result['score']:.4f}",
            "lyrics_match_method": result["method"],
            "lyrics_query_title": result["qtitle"],
            "lyrics_query_artist": result["qartist"],
            "lyrics_note": result["note"],
        }
        results.append(out)
        counts[result["status"]] = counts.get(result["status"], 0) + 1
        if result["status"] == "found":
            print(f"    ✓ {result['source']} ({len(result['lyrics'])} znaków) [{result['method']}]")
        elif result["status"] == "instrumental":
            print(f"    ∅ instrumental [{result['method']}]")
        elif result["status"] == "canonicaltext":
            print(f"    ≈ canonicaltext — tekst dzieła znaleziony bez wymogu zgodności wykonawcy")
        elif result["status"] == "candidate_instrumental":
            print("    ? candidate_instrumental — samo dzieło występuje jako instrumentalne; konkretne nagranie wymaga sprawdzenia")
        else:
            print("    × brak")

    output_path = save_new_file(results)
    print()
    print("GOTOWE")
    print(f"Nowy plik: {output_path}")
    print(", ".join(f"{k}={v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
