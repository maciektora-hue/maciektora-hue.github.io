#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOL — standalone lyrics fetcher v02-03, drugi przebieg dla pozostałych braków.

NIE CZYTA ŻADNYCH PLIKÓW WEJŚCIOWYCH.
Lista 68 utworów z middle_end, dla których lyrics_status = 'missing',
jest osadzona bezpośrednio w tym pliku (Supabase, stan 2026-09-14).

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

TRACKS = [
    {
        "utwu_id": "utwu-000978",
        "spotify_id": "46Bs8oQCNvP1kzIpQpbKU0",
        "spotify_order": "949",
        "title_original": "Party in My Pussy",
        "title_normalized": "party in my pussy",
        "title_parsed": "party in my pussy",
        "artist_original": "Catastrophe",
        "artist_normalized": "catastrophe",
        "artist_parsed": "catastrophe",
        "album_original": "Dernier soleil vision XL"
    },
    {
        "utwu_id": "utwu-000982",
        "spotify_id": "3Tsh9pjiJ5cvmuiZALdgVz",
        "spotify_order": "956",
        "title_original": "What Do You Want From Me - 2011 Remaster",
        "title_normalized": "what do you want from me - 2011 remaster",
        "title_parsed": "what do you want from me 2011 remaster",
        "artist_original": "Pink Floyd",
        "artist_normalized": "pink floyd",
        "artist_parsed": "pink floyd",
        "album_original": "The Division Bell (2011 Remastered Version)"
    },
    {
        "utwu_id": "utwu-000983",
        "spotify_id": "0m8tnq77KFbRDWCKGR404P",
        "spotify_order": "958",
        "title_original": "Hypnotise",
        "title_normalized": "hypnotise",
        "title_parsed": "hypnotise",
        "artist_original": "The White Stripes",
        "artist_normalized": "the white stripes",
        "artist_parsed": "the white stripes",
        "album_original": "Elephant"
    },
    {
        "utwu_id": "utwu-000984",
        "spotify_id": "0q0r8JVp4dPZBbmBUsqsgO",
        "spotify_order": "959",
        "title_original": "Bizet: Carmen, Act 1: \"Quels regardes! Quelle effronterie!\" (Carmen, José)",
        "title_normalized": "bizet: carmen, act 1: \"quels regardes! quelle effronterie!\" (carmen, josé)",
        "title_parsed": "bizet carmen act 1 quels regardes quelle effronterie carmen jose",
        "artist_original": "Georges Bizet, Maria Callas, Nicolai Gedda, Orchestre de l'Opéra National de Paris, Georges Prêtre, Orchestre du Théâtre National de l'Opéra Paris, Paris Opera Orchestra",
        "artist_normalized": "georges bizet, maria callas, nicolai gedda, orchestre de l'opéra national de paris, georges prêtre, orchestre du théâtre national de l'opéra paris, paris opera orchestra",
        "artist_parsed": "georges bizet | maria callas | nicolai gedda | orchestre de l opera national de paris | georges pretre | orchestre du theatre national de l opera paris | paris opera orchestra",
        "album_original": "Bizet: Carmen"
    },
    {
        "utwu_id": "utwu-000985",
        "spotify_id": "34vnbZpXcaC6sjNZw5MQdW",
        "spotify_order": "960",
        "title_original": "Les noces de Jeannette, Scene 4: \"Mais qu'entends-je ?\" - Chanson. \"Margot, Margot, lève ton sabot !\" (Jeannette, Jean, Chœur)",
        "title_normalized": "les noces de jeannette, scene 4: \"mais qu'entends-je ?\" - chanson. \"margot, margot, lève ton sabot !\" (jeannette, jean, chœur)",
        "title_parsed": "les noces de jeannette scene 4 mais qu entends je chanson margot margot leve ton sabot jeannette jean choeur",
        "artist_original": "Victor Massé, Orchestre Pasdeloup, Jean Allain, Renee Doria, Lucien Huberty, Chœurs de l'Association des Concerts Pasdeloup",
        "artist_normalized": "victor massé, orchestre pasdeloup, jean allain, renee doria, lucien huberty, chœurs de l'association des concerts pasdeloup",
        "artist_parsed": "victor masse | orchestre pasdeloup | jean allain | renee doria | lucien huberty | choeurs de l association des concerts pasdeloup",
        "album_original": "Massé: Les noces de Jeannette, extraits (Mono Version)"
    },
    {
        "utwu_id": "utwu-000987",
        "spotify_id": "2QRzKc9NhjGtkg4e08DB2v",
        "spotify_order": "963",
        "title_original": "Prayer",
        "title_normalized": "prayer",
        "title_parsed": "prayer",
        "artist_original": "Zbigniew Preisner",
        "artist_normalized": "zbigniew preisner",
        "artist_parsed": "zbigniew preisner",
        "album_original": "Requiem for My Friend"
    },
    {
        "utwu_id": "utwu-000988",
        "spotify_id": "4eAlHTYUZvllH2dE2juVQZ",
        "spotify_order": "965",
        "title_original": "St James Infirmary",
        "title_normalized": "st james infirmary",
        "title_parsed": "st james infirmary",
        "artist_original": "Hugh Laurie",
        "artist_normalized": "hugh laurie",
        "artist_parsed": "hugh laurie",
        "album_original": "Let Them Talk"
    },
    {
        "utwu_id": "utwu-000989",
        "spotify_id": "4vhmEEYa8ZuCSPhbLkJ7Hx",
        "spotify_order": "966",
        "title_original": "Hujawiak",
        "title_normalized": "hujawiak",
        "title_parsed": "hujawiak",
        "artist_original": "Maria Peszek",
        "artist_normalized": "maria peszek",
        "artist_parsed": "maria peszek",
        "album_original": "Maria Awaria"
    },
    {
        "utwu_id": "utwu-000991",
        "spotify_id": "6WYnBDrYZhzufvPCtIuIA4",
        "spotify_order": "968",
        "title_original": "Chomiczówka",
        "title_normalized": "chomiczówka",
        "title_parsed": "chomiczowka",
        "artist_original": "Sidney Polak",
        "artist_normalized": "sidney polak",
        "artist_parsed": "sidney polak",
        "album_original": "Sidney Polak"
    },
    {
        "utwu_id": "utwu-000992",
        "spotify_id": "6nOOUCdQlkrTQQG7feHUkC",
        "spotify_order": "969",
        "title_original": "Poetic Pitbull Revolution",
        "title_normalized": "poetic pitbull revolution",
        "title_parsed": "poetic pitbull revolution",
        "artist_original": "Diablo Swing Orchestra",
        "artist_normalized": "diablo swing orchestra",
        "artist_parsed": "diablo swing orchestra",
        "album_original": "The Butcher's Ballroom"
    },
    {
        "utwu_id": "utwu-000993",
        "spotify_id": "6LOGEZjhHkClwu6LNWp5sk",
        "spotify_order": "970",
        "title_original": "JPS",
        "title_normalized": "jps",
        "title_parsed": "jps",
        "artist_original": "Nosowska",
        "artist_normalized": "nosowska",
        "artist_parsed": "nosowska",
        "album_original": "8"
    },
    {
        "utwu_id": "utwu-000994",
        "spotify_id": "7MYmZL1lY2HTyYBCzj1Ac1",
        "spotify_order": "971",
        "title_original": "La vie en rose - DJ Antoine vs. Mad Mark 2k17 Mix",
        "title_normalized": "la vie en rose - dj antoine vs. mad mark 2k17 mix",
        "title_parsed": "la vie en rose dj antoine vs mad mark 2k17 mix",
        "artist_original": "DJ Antoine",
        "artist_normalized": "dj antoine",
        "artist_parsed": "dj antoine",
        "album_original": "La vie en rose (DJ Antoine vs. Mad Mark 2k17 Mix)"
    },
    {
        "utwu_id": "utwu-000995",
        "spotify_id": "4y6aEDPYJ2ObOWoDL84W9u",
        "spotify_order": "972",
        "title_original": "Atlas Air",
        "title_normalized": "atlas air",
        "title_parsed": "atlas air",
        "artist_original": "Massive Attack",
        "artist_normalized": "massive attack",
        "artist_parsed": "massive attack",
        "album_original": "Heligoland"
    },
    {
        "utwu_id": "utwu-000996",
        "spotify_id": "7A1UKvywzjhYHSKJZtZyUl",
        "spotify_order": "975",
        "title_original": "Pust wsiegda",
        "title_normalized": "pust wsiegda",
        "title_parsed": "pust wsiegda",
        "artist_original": "KONIEC ŚWIATA",
        "artist_normalized": "koniec świata",
        "artist_parsed": "koniec swiata",
        "album_original": "Oranżada"
    },
    {
        "utwu_id": "utwu-000998",
        "spotify_id": "3NI0uhYaHOxXFmXfwOYZxi",
        "spotify_order": "979",
        "title_original": "Superglue",
        "title_normalized": "superglue",
        "title_parsed": "superglue",
        "artist_original": "Maria Peszek",
        "artist_normalized": "maria peszek",
        "artist_parsed": "maria peszek",
        "album_original": "Maria Awaria"
    },
    {
        "utwu_id": "utwu-000999",
        "spotify_id": "1G09nJ8bspjgSHkSVRMWGC",
        "spotify_order": "980",
        "title_original": "Wild Honey",
        "title_normalized": "wild honey",
        "title_parsed": "wild honey",
        "artist_original": "Hugh Laurie",
        "artist_normalized": "hugh laurie",
        "artist_parsed": "hugh laurie",
        "album_original": "Didn't It Rain"
    },
    {
        "utwu_id": "utwu-001000",
        "spotify_id": "5jQlZoYXoGJAVrYROq3E9j",
        "spotify_order": "981",
        "title_original": "Bizet: Carmen, Act 4: \"Les voici! voici la quadrille!\" (Chorus, Escamillo, Carmen, Frasquita)",
        "title_normalized": "bizet: carmen, act 4: \"les voici! voici la quadrille!\" (chorus, escamillo, carmen, frasquita)",
        "title_parsed": "bizet carmen act 4 les voici voici la quadrille chorus escamillo carmen frasquita",
        "artist_original": "Georges Bizet, Maria Callas/Robert Massard/Nadine Sautereau/Choeurs René Duclos/Choeurs d'Enfants Jean Pesneaud/Orchestre de l'Opéra National de Paris/Georges Prêtre, Georges Prêtre, Orchestre du Théâtre National de l'Opéra Paris, Orchestre de l'Opéra National de Paris, Paris Opera Orchestra",
        "artist_normalized": "georges bizet, maria callas/robert massard/nadine sautereau/choeurs rené duclos/choeurs d'enfants jean pesneaud/orchestre de l'opéra national de paris/georges prêtre, georges prêtre, orchestre du théâtre national de l'opéra paris, orchestre de l'opéra national de paris, paris opera orchestra",
        "artist_parsed": "georges bizet | maria callas | robert massard | nadine sautereau | choeurs rene duclos | choeurs d enfants jean pesneaud | orchestre de l opera national de paris | georges pretre | georges pretre | orchestre du theatre national de l opera paris | orchestre de l opera national de paris | paris opera orchestra",
        "album_original": "Bizet: Carmen"
    },
    {
        "utwu_id": "utwu-001002",
        "spotify_id": "3RJtaxRtxOvvIj6DESm4gh",
        "spotify_order": "984",
        "title_original": "A Tapdancer's Dilema",
        "title_normalized": "a tapdancer's dilema",
        "title_parsed": "a tapdancer s dilema",
        "artist_original": "Diablo Swing Orchestra",
        "artist_normalized": "diablo swing orchestra",
        "artist_parsed": "diablo swing orchestra",
        "album_original": "Sing-Along Songs for the Damned and Delirious"
    },
    {
        "utwu_id": "utwu-001003",
        "spotify_id": "0klcaNjrRAPOU6n7Bcsl7J",
        "spotify_order": "985",
        "title_original": "Kokon",
        "title_normalized": "kokon",
        "title_parsed": "kokon",
        "artist_original": "Artur Rojek",
        "artist_normalized": "artur rojek",
        "artist_parsed": "artur rojek",
        "album_original": "Składam się z ciągłych powtórzeń"
    },
    {
        "utwu_id": "utwu-001004",
        "spotify_id": "0fTiDOXRNEN0lUeYGoSHml",
        "spotify_order": "986",
        "title_original": "Somebody",
        "title_normalized": "somebody",
        "title_parsed": "somebody",
        "artist_original": "The Chainsmokers, Drew Love",
        "artist_normalized": "the chainsmokers, drew love",
        "artist_parsed": "the chainsmokers | drew love",
        "album_original": "Sick Boy"
    },
    {
        "utwu_id": "utwu-001005",
        "spotify_id": "3HPUtPVDClplUMSXR57Pjb",
        "spotify_order": "987",
        "title_original": "Ailleurs et autrement",
        "title_normalized": "ailleurs et autrement",
        "title_parsed": "ailleurs et autrement",
        "artist_original": "Catastrophe",
        "artist_normalized": "catastrophe",
        "artist_parsed": "catastrophe",
        "album_original": "Dernier soleil vision XL"
    },
    {
        "utwu_id": "utwu-001007",
        "spotify_id": "6AynCuiHTQuVMYN2re6jcS",
        "spotify_order": "989",
        "title_original": "Cha-Ching (Till We Grow Older)",
        "title_normalized": "cha-ching (till we grow older)",
        "title_parsed": "cha ching till we grow older",
        "artist_original": "Imagine Dragons",
        "artist_normalized": "imagine dragons",
        "artist_parsed": "imagine dragons",
        "album_original": "Night Visions"
    },
    {
        "utwu_id": "utwu-001009",
        "spotify_id": "1GMoS97EgNwJmuSp3IKhEi",
        "spotify_order": "991",
        "title_original": "Unchain My Heart",
        "title_normalized": "unchain my heart",
        "title_parsed": "unchain my heart",
        "artist_original": "Hugh Laurie",
        "artist_normalized": "hugh laurie",
        "artist_parsed": "hugh laurie",
        "album_original": "Didn't It Rain"
    },
    {
        "utwu_id": "utwu-001010",
        "spotify_id": "4ylWMuGbMXNDgDd8lErEle",
        "spotify_order": "992",
        "title_original": "The Greatest Show",
        "title_normalized": "the greatest show",
        "title_parsed": "the greatest show",
        "artist_original": "Hugh Jackman, Keala Settle, Zac Efron, Zendaya, The Greatest Showman Ensemble",
        "artist_normalized": "hugh jackman, keala settle, zac efron, zendaya, the greatest showman ensemble",
        "artist_parsed": "hugh jackman | keala settle | zac efron | zendaya | the greatest showman ensemble",
        "album_original": "The Greatest Showman (Original Motion Picture Soundtrack)"
    },
    {
        "utwu_id": "utwu-001011",
        "spotify_id": "6y2Kaz9QI01XBKJ8mTb7Pf",
        "spotify_order": "994",
        "title_original": "Skin",
        "title_normalized": "skin",
        "title_parsed": "skin",
        "artist_original": "Rag'n'Bone Man",
        "artist_normalized": "rag'n'bone man",
        "artist_parsed": "rag n bone man",
        "album_original": "Human (Deluxe)"
    },
    {
        "utwu_id": "utwu-001012",
        "spotify_id": "3z8ypl55NHugzc6EDVVFdF",
        "spotify_order": "995",
        "title_original": "I Of The Storm",
        "title_normalized": "i of the storm",
        "title_parsed": "i of the storm",
        "artist_original": "Of Monsters and Men",
        "artist_normalized": "of monsters and men",
        "artist_parsed": "of monsters and men",
        "album_original": "Beneath The Skin (Deluxe)"
    },
    {
        "utwu_id": "utwu-001014",
        "spotify_id": "6TSgebnc69Ndnw52rffHJV",
        "spotify_order": "997",
        "title_original": "St. James' Infirmary Blues",
        "title_normalized": "st. james' infirmary blues",
        "title_parsed": "st james infirmary blues",
        "artist_original": "Jools Holland, Tom Jones",
        "artist_normalized": "jools holland, tom jones",
        "artist_parsed": "jools holland | tom jones",
        "album_original": "Tom Jones & Jools Holland"
    },
    {
        "utwu_id": "utwu-001015",
        "spotify_id": "1okiMm7ZfQij1JWaZAlMni",
        "spotify_order": "998",
        "title_original": "16 Tons",
        "title_normalized": "16 tons",
        "title_parsed": "16 tons",
        "artist_original": "Tom Morello: the Nightwatchman",
        "artist_normalized": "tom morello: the nightwatchman",
        "artist_parsed": "tom morello the nightwatchman",
        "album_original": "Union Town"
    },
    {
        "utwu_id": "utwu-001017",
        "spotify_id": "0UOKYamx2rZB4HYjedYFxn",
        "spotify_order": "1001",
        "title_original": "Puttin' On the Ritz",
        "title_normalized": "puttin' on the ritz",
        "title_parsed": "puttin on the ritz",
        "artist_original": "Gypsy Swing Revue",
        "artist_normalized": "gypsy swing revue",
        "artist_parsed": "gypsy swing revue",
        "album_original": "Puttin' On The Ritz"
    },
    {
        "utwu_id": "utwu-001018",
        "spotify_id": "1FLEVJaXv8vZwunzQZSHLK",
        "spotify_order": "1002",
        "title_original": "Odchodząc",
        "title_normalized": "odchodząc",
        "title_parsed": "odchodzac",
        "artist_original": "Republika",
        "artist_normalized": "republika",
        "artist_parsed": "republika",
        "album_original": "Masakra"
    },
    {
        "utwu_id": "utwu-001019",
        "spotify_id": "3ZPlIHGLp21LDDeq20Q42W",
        "spotify_order": "1003",
        "title_original": "Put a Lid on It - Caspar Remix",
        "title_normalized": "put a lid on it - caspar remix",
        "title_parsed": "put a lid on it caspar remix",
        "artist_original": "Squirrel Nut Zippers, Caspar",
        "artist_normalized": "squirrel nut zippers, caspar",
        "artist_parsed": "squirrel nut zippers | caspar",
        "album_original": "White Mink: Black Cotton, Vol. 3 (Electro Swing vs Speakeasy Jazz)"
    },
    {
        "utwu_id": "utwu-001020",
        "spotify_id": "3PMFNGb08SzI0lLHL6ti08",
        "spotify_order": "1004",
        "title_original": "La Vie En Rose",
        "title_normalized": "la vie en rose",
        "title_parsed": "la vie en rose",
        "artist_original": "Iggy Pop",
        "artist_normalized": "iggy pop",
        "artist_parsed": "iggy pop",
        "album_original": "Après"
    },
    {
        "utwu_id": "utwu-001021",
        "spotify_id": "39Gj4kVhhXoaqUccOA3sfm",
        "spotify_order": "1006",
        "title_original": "Bright Lights Late Nights",
        "title_normalized": "bright lights late nights",
        "title_parsed": "bright lights late nights",
        "artist_original": "The Speakeasies' Swing Band!",
        "artist_normalized": "the speakeasies' swing band!",
        "artist_parsed": "the speakeasies swing band",
        "album_original": "Bathtub Gin"
    },
    {
        "utwu_id": "utwu-001022",
        "spotify_id": "0LvR7Y4iQLGKwNluNfxfOV",
        "spotify_order": "1007",
        "title_original": "Between the Bars",
        "title_normalized": "between the bars",
        "title_parsed": "between the bars",
        "artist_original": "Seth Avett & Jessica Lea Mayfield",
        "artist_normalized": "seth avett & jessica lea mayfield",
        "artist_parsed": "seth avett jessica lea mayfield",
        "album_original": "Seth Avett & Jessica Lea Mayfield Sing Elliott Smith"
    },
    {
        "utwu_id": "utwu-001023",
        "spotify_id": "3fAZ1tIOwFIeWKrPpf7meU",
        "spotify_order": "1009",
        "title_original": "Dżentelmeni metalu",
        "title_normalized": "dżentelmeni metalu",
        "title_parsed": "dzentelmeni metalu",
        "artist_original": "Nocny Kochanek",
        "artist_normalized": "nocny kochanek",
        "artist_parsed": "nocny kochanek",
        "album_original": "Zdrajcy metalu"
    },
    {
        "utwu_id": "utwu-001024",
        "spotify_id": "5QUc4vKdECNtJGkgEUlhXf",
        "spotify_order": "1011",
        "title_original": "Les marionnettes",
        "title_normalized": "les marionnettes",
        "title_parsed": "les marionnettes",
        "artist_original": "Zbigniew Preisner",
        "artist_normalized": "zbigniew preisner",
        "artist_parsed": "zbigniew preisner",
        "album_original": "La Double vie de Véronique (Original Film Soundtrack)"
    },
    {
        "utwu_id": "utwu-001025",
        "spotify_id": "35zClIAZTUIwBatunZdbWj",
        "spotify_order": "1012",
        "title_original": "Pink Noise Waltz",
        "title_normalized": "pink noise waltz",
        "title_parsed": "pink noise waltz",
        "artist_original": "Diablo Swing Orchestra",
        "artist_normalized": "diablo swing orchestra",
        "artist_parsed": "diablo swing orchestra",
        "album_original": "The Butcher's Ballroom"
    },
    {
        "utwu_id": "utwu-001026",
        "spotify_id": "0ZV4E9Ko7pQW278jRJ5o4J",
        "spotify_order": "1013",
        "title_original": "Girl I Love You - She Is Danger Remix",
        "title_normalized": "girl i love you - she is danger remix",
        "title_parsed": "girl i love you she is danger remix",
        "artist_original": "Massive Attack, Horace Andy, She is Danger",
        "artist_normalized": "massive attack, horace andy, she is danger",
        "artist_parsed": "massive attack | horace andy | she is danger",
        "album_original": "Heligoland"
    },
    {
        "utwu_id": "utwu-001027",
        "spotify_id": "3Y8Ff1nH44jFywAtpgmleZ",
        "spotify_order": "1014",
        "title_original": "1979 - Remastered 2012",
        "title_normalized": "1979 - remastered 2012",
        "title_parsed": "1979 remastered 2012",
        "artist_original": "The Smashing Pumpkins",
        "artist_normalized": "the smashing pumpkins",
        "artist_parsed": "the smashing pumpkins",
        "album_original": "Mellon Collie And The Infinite Sadness (Remastered)"
    },
    {
        "utwu_id": "utwu-001028",
        "spotify_id": "0b88IsIjJzvHpY9PPF6P8F",
        "spotify_order": "1015",
        "title_original": "Build the Fire",
        "title_normalized": "build the fire",
        "title_parsed": "build the fire",
        "artist_original": "Kal Cahoone",
        "artist_normalized": "kal cahoone",
        "artist_parsed": "kal cahoone",
        "album_original": "Build the Fire"
    },
    {
        "utwu_id": "utwu-001029",
        "spotify_id": "1pmuken8VQO2mX0uUYCJFk",
        "spotify_order": "1016",
        "title_original": "SIÓDME",
        "title_normalized": "siódme",
        "title_parsed": "siodme",
        "artist_original": "Luxtorpeda",
        "artist_normalized": "luxtorpeda",
        "artist_parsed": "luxtorpeda",
        "album_original": "MYWASWYNAS"
    },
    {
        "utwu_id": "utwu-001030",
        "spotify_id": "07QO5ItAwqLAl6jEr7pihI",
        "spotify_order": "1017",
        "title_original": "Ta droga była daleka",
        "title_normalized": "ta droga była daleka",
        "title_parsed": "ta droga byla daleka",
        "artist_original": "Kazik & Kwartet ProForma",
        "artist_normalized": "kazik & kwartet proforma",
        "artist_parsed": "kazik kwartet proforma",
        "album_original": "Tata Kazika kontra Hedora"
    },
    {
        "utwu_id": "utwu-001031",
        "spotify_id": "523QluF88z1TOiPUb0Htxi",
        "spotify_order": "1018",
        "title_original": "Coming Back As A Man",
        "title_normalized": "coming back as a man",
        "title_parsed": "coming back as a man",
        "artist_original": "Caro Emerald",
        "artist_normalized": "caro emerald",
        "artist_parsed": "caro emerald",
        "album_original": "The Shocking Miss Emerald"
    },
    {
        "utwu_id": "utwu-001032",
        "spotify_id": "3j9hQ1wo9i0ypcW3HlDhMY",
        "spotify_order": "1020",
        "title_original": "Bizet: Carmen, Act 2: \"Enfin c'est toi!...Tout doux, Monsieur\" (Carmen, José)",
        "title_normalized": "bizet: carmen, act 2: \"enfin c'est toi!...tout doux, monsieur\" (carmen, josé)",
        "title_parsed": "bizet carmen act 2 enfin c est toi tout doux monsieur carmen jose",
        "artist_original": "Georges Bizet, Maria Callas, Nicolai Gedda, Orchestre de l'Opéra National de Paris, Georges Prêtre, Orchestre du Théâtre National de l'Opéra Paris, Paris Opera Orchestra",
        "artist_normalized": "georges bizet, maria callas, nicolai gedda, orchestre de l'opéra national de paris, georges prêtre, orchestre du théâtre national de l'opéra paris, paris opera orchestra",
        "artist_parsed": "georges bizet | maria callas | nicolai gedda | orchestre de l opera national de paris | georges pretre | orchestre du theatre national de l opera paris | paris opera orchestra",
        "album_original": "Bizet: Carmen"
    },
    {
        "utwu_id": "utwu-001033",
        "spotify_id": "1qxvyvIFtWiV3QNkv17z10",
        "spotify_order": "1022",
        "title_original": "Six Cold Feet",
        "title_normalized": "six cold feet",
        "title_parsed": "six cold feet",
        "artist_original": "Hugh Laurie",
        "artist_normalized": "hugh laurie",
        "artist_parsed": "hugh laurie",
        "album_original": "Let Them Talk"
    },
    {
        "utwu_id": "utwu-001034",
        "spotify_id": "4uEuLNfedAeV6coYsExjyK",
        "spotify_order": "1023",
        "title_original": "Song for the Unification of Europe - Patrice's Version",
        "title_normalized": "song for the unification of europe - patrice's version",
        "title_parsed": "song for the unification of europe patrice s version",
        "artist_original": "Zbigniew Preisner",
        "artist_normalized": "zbigniew preisner",
        "artist_parsed": "zbigniew preisner",
        "album_original": "Trois Couleurs: Bleu, Blanc, Rouge (Original Motion Picture Soundtrack from the Three Colors Trilogy by Kieślowski)"
    },
    {
        "utwu_id": "utwu-001035",
        "spotify_id": "0eGVLeXORd8sTVFFgTdFIz",
        "spotify_order": "1025",
        "title_original": "Bez znieczulenia",
        "title_normalized": "bez znieczulenia",
        "title_parsed": "bez znieczulenia",
        "artist_original": "Happysad",
        "artist_normalized": "happysad",
        "artist_parsed": "happysad",
        "album_original": "Ciepło / zimno"
    },
    {
        "utwu_id": "utwu-001036",
        "spotify_id": "2x2SotEkKozaFh6H1aVnOZ",
        "spotify_order": "1026",
        "title_original": "Who We Are",
        "title_normalized": "who we are",
        "title_parsed": "who we are",
        "artist_original": "Imagine Dragons",
        "artist_normalized": "imagine dragons",
        "artist_parsed": "imagine dragons",
        "album_original": "Smoke + Mirrors (Deluxe)"
    },
    {
        "utwu_id": "utwu-001037",
        "spotify_id": "3Po087iAvFfh44v18qaiuM",
        "spotify_order": "1027",
        "title_original": "Hero",
        "title_normalized": "hero",
        "title_parsed": "hero",
        "artist_original": "Lissie",
        "artist_normalized": "lissie",
        "artist_parsed": "lissie",
        "album_original": "My Wild West"
    },
    {
        "utwu_id": "utwu-001038",
        "spotify_id": "6AQbbWjXuuabQKjfW91nO0",
        "spotify_order": "1028",
        "title_original": "Lift Me Up - 2006 Remastered Version",
        "title_normalized": "lift me up - 2006 remastered version",
        "title_parsed": "lift me up 2006 remastered version",
        "artist_original": "Moby",
        "artist_normalized": "moby",
        "artist_parsed": "moby",
        "album_original": "Go - The Very Best Of Moby (Deluxe)"
    },
    {
        "utwu_id": "utwu-001039",
        "spotify_id": "6ELHQlQiOKRHC6GclcYjZq",
        "spotify_order": "1029",
        "title_original": "Co się z nami stało",
        "title_normalized": "co się z nami stało",
        "title_parsed": "co sie z nami stalo",
        "artist_original": "Strachy Na Lachy",
        "artist_normalized": "strachy na lachy",
        "artist_parsed": "strachy na lachy",
        "album_original": "Przechodzień o wschodzie"
    },
    {
        "utwu_id": "utwu-001040",
        "spotify_id": "7LqdAcDBXaTFqLNgDhGbZw",
        "spotify_order": "1030",
        "title_original": "Wizja dźwięku",
        "title_normalized": "wizja dźwięku",
        "title_parsed": "wizja dzwieku",
        "artist_original": "Piotr Rogucki",
        "artist_normalized": "piotr rogucki",
        "artist_parsed": "piotr rogucki",
        "album_original": "Loki - wizja dźwięku"
    },
    {
        "utwu_id": "utwu-001041",
        "spotify_id": "050yrnIvcYXX84seDeNWoE",
        "spotify_order": "1031",
        "title_original": "Happy",
        "title_normalized": "happy",
        "title_parsed": "happy",
        "artist_original": "Kat Frankie",
        "artist_normalized": "kat frankie",
        "artist_parsed": "kat frankie",
        "album_original": "The Dance of a Stranger Heart"
    },
    {
        "utwu_id": "utwu-001042",
        "spotify_id": "3nFB1eWA6NXktranjj90BM",
        "spotify_order": "1032",
        "title_original": "When I Get Low, I Get High",
        "title_normalized": "when i get low, i get high",
        "title_parsed": "when i get low i get high",
        "artist_original": "The Speakeasy Three",
        "artist_normalized": "the speakeasy three",
        "artist_parsed": "the speakeasy three",
        "album_original": "When I Get Low, I Get High"
    },
    {
        "utwu_id": "utwu-001043",
        "spotify_id": "0D4qpwBW7oVFzbMot4mpab",
        "spotify_order": "1034",
        "title_original": "Polska",
        "title_normalized": "polska",
        "title_parsed": "polska",
        "artist_original": "Nosowska",
        "artist_normalized": "nosowska",
        "artist_parsed": "nosowska",
        "album_original": "8"
    },
    {
        "utwu_id": "utwu-001045",
        "spotify_id": "7z3AlZQ8NaPpB1Yic5cIDJ",
        "spotify_order": "1037",
        "title_original": "Second Chances",
        "title_normalized": "second chances",
        "title_parsed": "second chances",
        "artist_original": "Imagine Dragons",
        "artist_normalized": "imagine dragons",
        "artist_parsed": "imagine dragons",
        "album_original": "Smoke + Mirrors (Deluxe)"
    },
    {
        "utwu_id": "utwu-001046",
        "spotify_id": "2GFzFA3GKA9XBfhCP0BDAh",
        "spotify_order": "1038",
        "title_original": "Kokon - Live",
        "title_normalized": "kokon - live",
        "title_parsed": "kokon live",
        "artist_original": "Artur Rojek",
        "artist_normalized": "artur rojek",
        "artist_parsed": "artur rojek",
        "album_original": "Koncert w NOSPR"
    },
    {
        "utwu_id": "utwu-001047",
        "spotify_id": "0aB3mcVVzRejbpnIsJlqcx",
        "spotify_order": "",
        "title_original": "Czuły barbarzyńca",
        "title_normalized": "czuły barbarzyńca",
        "title_parsed": "czuly barbarzynca",
        "artist_original": "Matylda/Łukasiewicz, Matylda, Radek Łukasiewicz",
        "artist_normalized": "matylda/łukasiewicz, matylda, radek łukasiewicz",
        "artist_parsed": "matylda lukasiewicz | matylda | radek lukasiewicz",
        "album_original": "Matka"
    },
    {
        "utwu_id": "utwu-001048",
        "spotify_id": "77lQZkzHJJ7t7XeU6NzMH2",
        "spotify_order": "",
        "title_original": "Spektakl",
        "title_normalized": "spektakl",
        "title_parsed": "spektakl",
        "artist_original": "Spięty",
        "artist_normalized": "spięty",
        "artist_parsed": "spiety",
        "album_original": "HEARTCORE"
    },
    {
        "utwu_id": "utwu-001049",
        "spotify_id": "48MFnqibCcU9DMDDH0Sp9H",
        "spotify_order": "",
        "title_original": "Cichosza",
        "title_normalized": "cichosza",
        "title_parsed": "cichosza",
        "artist_original": "IKARVS",
        "artist_normalized": "ikarvs",
        "artist_parsed": "ikarvs",
        "album_original": "Cyrki"
    },
    {
        "utwu_id": "utwu-001050",
        "spotify_id": "58FVEblGAJmAwsDfR295cf",
        "spotify_order": "",
        "title_original": "Pan Piotruś Pan",
        "title_normalized": "pan piotruś pan",
        "title_parsed": "pan piotrus pan",
        "artist_original": "Spięty",
        "artist_normalized": "spięty",
        "artist_parsed": "spiety",
        "album_original": "HEARTCORE"
    },
    {
        "utwu_id": "utwu-001051",
        "spotify_id": "0qIpUJWhbriXfgZUQVbKap",
        "spotify_order": "",
        "title_original": "Sing Sing",
        "title_normalized": "sing sing",
        "title_parsed": "sing sing",
        "artist_original": "Maja Kleszcz",
        "artist_normalized": "maja kleszcz",
        "artist_parsed": "maja kleszcz",
        "album_original": "Osiecka De Luxe"
    },
    {
        "utwu_id": "utwu-001052",
        "spotify_id": "0DJ4WbO2XI6mWVOGU59fif",
        "spotify_order": "",
        "title_original": "Residue",
        "title_normalized": "residue",
        "title_parsed": "residue",
        "artist_original": "Benjamin Clementine",
        "artist_normalized": "benjamin clementine",
        "artist_parsed": "benjamin clementine",
        "album_original": "And I Have Been"
    },
    {
        "utwu_id": "utwu-001053",
        "spotify_id": "0DllheZuGUaoqnz6qDMpo9",
        "spotify_order": "",
        "title_original": "Čálkko Niillas",
        "title_normalized": "čálkko niillas",
        "title_parsed": "calkko niillas",
        "artist_original": "Hildá Länsman, Tuomas Norvio",
        "artist_normalized": "hildá länsman, tuomas norvio",
        "artist_parsed": "hilda lansman | tuomas norvio",
        "album_original": "Dajan"
    },
    {
        "utwu_id": "utwu-001054",
        "spotify_id": "04sN26COy28wTXYj3dMoiZ",
        "spotify_order": "",
        "title_original": "Bored",
        "title_normalized": "bored",
        "title_parsed": "bored",
        "artist_original": "Billie Eilish",
        "artist_normalized": "billie eilish",
        "artist_parsed": "billie eilish",
        "album_original": "Bored"
    },
    {
        "utwu_id": "utwu-001056",
        "spotify_id": "55dWbx9siuMTNMsIgCtBjl",
        "spotify_order": "",
        "title_original": "Za Ostatni Grosz",
        "title_normalized": "za ostatni grosz",
        "title_parsed": "za ostatni grosz",
        "artist_original": "Budka Suflera",
        "artist_normalized": "budka suflera",
        "artist_parsed": "budka suflera",
        "album_original": "Za Ostatni Grosz"
    },
    {
        "utwu_id": "utwu-001057",
        "spotify_id": "6uE9hF8fIb6shBXrrzA12U",
        "spotify_order": "",
        "title_original": "Poles Apart - 2011 Remaster",
        "title_normalized": "poles apart - 2011 remaster",
        "title_parsed": "poles apart 2011 remaster",
        "artist_original": "Pink Floyd",
        "artist_normalized": "pink floyd",
        "artist_parsed": "pink floyd",
        "album_original": "The Division Bell (2011 Remastered Version)"
    },
    {
        "utwu_id": "utwu-001058",
        "spotify_id": "7BCR9ZZJVKwsUrqnrrcum6",
        "spotify_order": "",
        "title_original": "So Long, Marianne - MTV Unplugged Live in Melbourne",
        "title_normalized": "so long, marianne - mtv unplugged live in melbourne",
        "title_parsed": "so long marianne mtv unplugged live in melbourne",
        "artist_original": "Courtney Barnett",
        "artist_normalized": "courtney barnett",
        "artist_parsed": "courtney barnett",
        "album_original": "MTV Unplugged (Live in Melbourne)"
    }
]

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
