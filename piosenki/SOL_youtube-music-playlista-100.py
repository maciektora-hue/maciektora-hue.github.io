#!/usr/bin/env python3
from pathlib import Path
import sys

# ============================================================
# USTAW TYLKO TO JEDNO:
PLAYLIST_URL = "WKLEJ_TUTAJ_LINK_DO_PLAYLISTY"
# ============================================================

ILE_NA_RAZ = 100

# Android / Termux:
# przed pierwszym użyciem wykonaj raz: termux-setup-storage
KATALOG = Path.home() / "storage" / "music" / "YTMusic_playlist"
ARCHIWUM = KATALOG / "pobrane.txt"


def main():
    if PLAYLIST_URL == "WKLEJ_TUTAJ_LINK_DO_PLAYLISTY" or not PLAYLIST_URL.strip():
        print("\nBŁĄD: wklej link do playlisty w zmiennej PLAYLIST_URL na górze pliku.\n")
        sys.exit(1)

    try:
        import yt_dlp
    except ImportError:
        print("\nBrak yt-dlp.")
        print('Zainstaluj raz w Termuxie:')
        print('python -m pip install -U "yt-dlp[default]"')
        sys.exit(1)

    # Sprawdzenie dostępu do pamięci telefonu.
    music_dir = Path.home() / "storage" / "music"
    if not music_dir.exists():
        print("\nBrak dostępu do pamięci telefonu.")
        print("W Termuxie wykonaj raz:")
        print("termux-setup-storage")
        sys.exit(1)

    KATALOG.mkdir(parents=True, exist_ok=True)

    opcje = {
        # Najlepszy dostępny strumień audio, bez konwersji do WAV/MP3.
        "format": "bestaudio/best",

        # Każdy poprawnie pobrany utwór trafia do archiwum.
        # Przy następnym uruchomieniu zostanie automatycznie pominięty.
        "download_archive": str(ARCHIWUM),

        # Maksymalnie 100 NOWYCH pobrań na jedno uruchomienie.
        "max_downloads": ILE_NA_RAZ,

        # Błąd pojedynczego utworu nie wywala całej playlisty.
        "ignoreerrors": True,

        # Nie pobieraj filmu, tylko audio.
        "noplaylist": False,

        # Czytelne nazwy; numer zachowuje pozycję na playliście.
        "outtmpl": str(
            KATALOG
            / "%(playlist_index)04d - %(artist,uploader)s - %(title)s [%(id)s].%(ext)s"
        ),

        # Bez nadpisywania istniejących plików.
        "overwrites": False,

        # Mniej śmieci w terminalu, ale pokazuj postęp.
        "quiet": False,
        "no_warnings": False,
    }

    print(f"\nKatalog: {KATALOG}")
    print(f"Limit tego uruchomienia: {ILE_NA_RAZ} nowych utworów")
    print("Już pobrane utwory zostaną automatycznie pominięte.\n")

    try:
        with yt_dlp.YoutubeDL(opcje) as ydl:
            ydl.download([PLAYLIST_URL])
    except yt_dlp.utils.MaxDownloadsReached:
        print(f"\nOK: pobrano limit {ILE_NA_RAZ} nowych utworów.")
        print("Uruchom ten sam plik ponownie, żeby pobrać następną setkę.")
        return
    except KeyboardInterrupt:
        print("\nPrzerwano ręcznie.")
        print("To, co pobrało się poprawnie, jest zapamiętane.")
        return

    print("\nKoniec.")
    print("Jeżeli playlista ma jeszcze niepobrane utwory, następne uruchomienie je znajdzie.")



# Lista z public.middle_end: audio_id NULL/puste, odczyt 2026-09-14.
# Uruchom bez argumentów: uzupełnianie 211 braków (wybór nagrania).
# Dawny tryb playlisty: python SOL_youtube-music-playlista-100.py --playlist URL
# Przygotowanie w Termuxie:
# termux-setup-storage
# python -m pip install -U "yt-dlp[default]"
# pkg install deno
# Wyniki są lokalne. Przypisanie w SQL wymaga osobnego importu/weryfikacji.
import argparse
import json
import re

BRAKI = [
  {
    "utwu_id": "utwu-000003",
    "title_original": "Bankiet",
    "artist_original": "KONIEC ŚWIATA"
  },
  {
    "utwu_id": "utwu-000008",
    "title_original": "I'm Going Slightly Mad - Remastered 2011",
    "artist_original": "Queen"
  },
  {
    "utwu_id": "utwu-000018",
    "title_original": "Blask",
    "artist_original": "Kacperczyk, Ralph Kaminski"
  },
  {
    "utwu_id": "utwu-000026",
    "title_original": "Bez końca",
    "artist_original": "Artur Rojek"
  },
  {
    "utwu_id": "utwu-000038",
    "title_original": "New Day",
    "artist_original": "Kormac, Jack O'Rourke"
  },
  {
    "utwu_id": "utwu-000047",
    "title_original": "Reason or Rhyme",
    "artist_original": "The Bryan Ferry Orchestra"
  },
  {
    "utwu_id": "utwu-000048",
    "title_original": "Bad Sign",
    "artist_original": "Greni"
  },
  {
    "utwu_id": "utwu-000051",
    "title_original": "Lay All Your Love on Me",
    "artist_original": "Pale Honey"
  },
  {
    "utwu_id": "utwu-000056",
    "title_original": "SEEING RED",
    "artist_original": "MY BABY"
  },
  {
    "utwu_id": "utwu-000073",
    "title_original": "Loud",
    "artist_original": "JJ Kamei"
  },
  {
    "utwu_id": "utwu-000087",
    "title_original": "Obsession",
    "artist_original": "Ran Nir"
  },
  {
    "utwu_id": "utwu-000095",
    "title_original": "Historie",
    "artist_original": "Hey"
  },
  {
    "utwu_id": "utwu-000106",
    "title_original": "A Bird, A Bee, Humanity",
    "artist_original": "The Leisure Society"
  },
  {
    "utwu_id": "utwu-000134",
    "title_original": "Baby",
    "artist_original": "DakhaBrakha"
  },
  {
    "utwu_id": "utwu-000149",
    "title_original": "Do polityka",
    "artist_original": "Zbigniew Preisner, Anna Szałapak"
  },
  {
    "utwu_id": "utwu-000150",
    "title_original": "Kiss of Fire",
    "artist_original": "Hugh Laurie"
  },
  {
    "utwu_id": "utwu-000169",
    "title_original": "Money Money",
    "artist_original": "Joel Grey, Liza Minnelli"
  },
  {
    "utwu_id": "utwu-000176",
    "title_original": "Ja pas!",
    "artist_original": "Nosowska"
  },
  {
    "utwu_id": "utwu-000185",
    "title_original": "Ave Maria",
    "artist_original": "Maria Peszek"
  },
  {
    "utwu_id": "utwu-000198",
    "title_original": "Make It Wit Chu",
    "artist_original": "Olivier Libaux, Mélanie Pain"
  },
  {
    "utwu_id": "utwu-000201",
    "title_original": "Ievan Polkka",
    "artist_original": "Traditional, Le Chœur Voyageur, Alexis Duffaure"
  },
  {
    "utwu_id": "utwu-000225",
    "title_original": "Paint It Black",
    "artist_original": "Rémi Panossian"
  },
  {
    "utwu_id": "utwu-000234",
    "title_original": "Nowhere To Be",
    "artist_original": "H-Burns"
  },
  {
    "utwu_id": "utwu-000266",
    "title_original": "Moonlight Avenue",
    "artist_original": "Ti.po.ta, Manu Chao, Klelia Renesi"
  },
  {
    "utwu_id": "utwu-000275",
    "title_original": "Blue Hotel",
    "artist_original": "trentemøller"
  },
  {
    "utwu_id": "utwu-000285",
    "title_original": "All That We Are",
    "artist_original": "Charlie Winston"
  },
  {
    "utwu_id": "utwu-000287",
    "title_original": "Cannes",
    "artist_original": "Barbara Carlotti"
  },
  {
    "utwu_id": "utwu-000297",
    "title_original": "Melodia ulotna",
    "artist_original": "Mela Koteluk"
  },
  {
    "utwu_id": "utwu-000307",
    "title_original": "Dom Sąsiedni",
    "artist_original": "L.U.C., Rebel Babel Ensemble, Renata Przemyk"
  },
  {
    "utwu_id": "utwu-000311",
    "title_original": "Your Woman",
    "artist_original": "GYM"
  },
  {
    "utwu_id": "utwu-000314",
    "title_original": "Piangi con me",
    "artist_original": "Bee Bee Sea"
  },
  {
    "utwu_id": "utwu-000315",
    "title_original": "Fuck the Government, I Love You",
    "artist_original": "The Burning Hell"
  },
  {
    "utwu_id": "utwu-000325",
    "title_original": "Dos",
    "artist_original": "Rémi Panossian"
  },
  {
    "utwu_id": "utwu-000355",
    "title_original": "Appaloosa",
    "artist_original": "Lor"
  },
  {
    "utwu_id": "utwu-000363",
    "title_original": "Bed Of Stone",
    "artist_original": "Tiwayo"
  },
  {
    "utwu_id": "utwu-000365",
    "title_original": "You Spin Me Round (Like a Record)",
    "artist_original": "Dead Or Alive"
  },
  {
    "utwu_id": "utwu-000382",
    "title_original": "My Way",
    "artist_original": "Frank Sinatra"
  },
  {
    "utwu_id": "utwu-000386",
    "title_original": "L'enfant roi",
    "artist_original": "Noir Désir"
  },
  {
    "utwu_id": "utwu-000402",
    "title_original": "Das Model",
    "artist_original": "Seu Jorge, Almaz"
  },
  {
    "utwu_id": "utwu-000410",
    "title_original": "The Passenger",
    "artist_original": "Dinah Eastwood"
  },
  {
    "utwu_id": "utwu-000434",
    "title_original": "Golden Brown",
    "artist_original": "THE TAKE VIBE E.P."
  },
  {
    "utwu_id": "utwu-000445",
    "title_original": "Wonderful Life",
    "artist_original": "Katie Melua"
  },
  {
    "utwu_id": "utwu-000453",
    "title_original": "Ten Lines",
    "artist_original": "MISSINCAT"
  },
  {
    "utwu_id": "utwu-000470",
    "title_original": "You Can Discover",
    "artist_original": "Roseaux, Melissa Laveaux"
  },
  {
    "utwu_id": "utwu-000504",
    "title_original": "Creep",
    "artist_original": "Scala & Kolacny Brothers"
  },
  {
    "utwu_id": "utwu-000519",
    "title_original": "Heard Somebody Whistle",
    "artist_original": "Jay-Jay Johanson"
  },
  {
    "utwu_id": "utwu-000521",
    "title_original": "What Does the Fox Say?",
    "artist_original": "Yvar"
  },
  {
    "utwu_id": "utwu-000522",
    "title_original": "Riptide",
    "artist_original": "Vance Joy"
  },
  {
    "utwu_id": "utwu-000533",
    "title_original": "Too Many Friends",
    "artist_original": "Charles Pasi"
  },
  {
    "utwu_id": "utwu-000542",
    "title_original": "Strange Things",
    "artist_original": "Roseaux, Aloe Blacc"
  },
  {
    "utwu_id": "utwu-000555",
    "title_original": "Akacje",
    "artist_original": "IKARVS, AKASHA MX"
  },
  {
    "utwu_id": "utwu-000567",
    "title_original": "Jammin",
    "artist_original": "Męskie Granie Orkiestra, Igo, Mrozu, Vito Bambino"
  },
  {
    "utwu_id": "utwu-000585",
    "title_original": "Underground",
    "artist_original": "Mariama"
  },
  {
    "utwu_id": "utwu-000593",
    "title_original": "Vajrasattva",
    "artist_original": "Gaiea Sanskrit"
  },
  {
    "utwu_id": "utwu-000594",
    "title_original": "To Remove Fear",
    "artist_original": "Gaiea Sanskrit"
  },
  {
    "utwu_id": "utwu-000596",
    "title_original": "Melos",
    "artist_original": "Vassilis Tsabropoulos, Anja Lechner, U.T. Gandhi"
  },
  {
    "utwu_id": "utwu-000609",
    "title_original": "Madryt",
    "artist_original": "Kult"
  },
  {
    "utwu_id": "utwu-000612",
    "title_original": "Somebody to Love",
    "artist_original": "Jefferson Airplane"
  },
  {
    "utwu_id": "utwu-000652",
    "title_original": "Symphony No. 2 in C minor - \"Resurrection\" / 5th Movement: Wieder zurückhaltend",
    "artist_original": "Gustav Mahler, Wiener Philharmoniker, Gilbert Kaplan"
  },
  {
    "utwu_id": "utwu-000663",
    "title_original": "Złote łezki",
    "artist_original": "Meek, Oh Why?, BIESY"
  },
  {
    "utwu_id": "utwu-000674",
    "title_original": "Nobody Knows",
    "artist_original": "Elsiane"
  },
  {
    "utwu_id": "utwu-000680",
    "title_original": "Amara Terra Mia",
    "artist_original": "Elina Duni"
  },
  {
    "utwu_id": "utwu-000684",
    "title_original": "Looking for You",
    "artist_original": "Flo Morrissey, Matthew E. White"
  },
  {
    "utwu_id": "utwu-000689",
    "title_original": "Redshift",
    "artist_original": "Nitin Sawhney, J’Danna"
  },
  {
    "utwu_id": "utwu-000754",
    "title_original": "Eden",
    "artist_original": "Hooverphonic"
  },
  {
    "utwu_id": "utwu-000756",
    "title_original": "Mad About You",
    "artist_original": "Hooverphonic"
  },
  {
    "utwu_id": "utwu-000808",
    "title_original": "Symphony No. 9 in D Minor, Op. 125 \"Choral\": III. Adagio molto e cantabile - Andante moderato",
    "artist_original": "Ludwig van Beethoven, Helena Juntunen, Katarina Karnéus, Daniel Norman, Neal Davies, Minnesota Chorale, Minnesota Orchestra, Osmo Vänskä"
  },
  {
    "utwu_id": "utwu-000811",
    "title_original": "D'Angelo",
    "artist_original": "Diablo Swing Orchestra"
  },
  {
    "utwu_id": "utwu-000815",
    "title_original": "Blue Rondo à la Turk",
    "artist_original": "The Dave Brubeck Quartet"
  },
  {
    "utwu_id": "utwu-000819",
    "title_original": "Za Milena J.",
    "artist_original": "Moriarty"
  },
  {
    "utwu_id": "utwu-000841",
    "title_original": "Do Rycerzy, do Szlachty, do Mieszczan",
    "artist_original": "Hey"
  },
  {
    "utwu_id": "utwu-000853",
    "title_original": "Golden Brown",
    "artist_original": "The Secret Sea"
  },
  {
    "utwu_id": "utwu-000854",
    "title_original": "Pismo",
    "artist_original": "Dr Misio"
  },
  {
    "utwu_id": "utwu-000877",
    "title_original": "Remedy",
    "artist_original": "MY BABY"
  },
  {
    "utwu_id": "utwu-000888",
    "title_original": "Bóg - 2008 Remaster",
    "artist_original": "T.Love"
  },
  {
    "utwu_id": "utwu-000890",
    "title_original": "Щедрик (Szczedryk)",
    "artist_original": "Katedralny Chór Parafii Prawosławnej Św. Mikołaja w Gdańsku"
  },
  {
    "utwu_id": "utwu-000897",
    "title_original": "Montage from Twin Peaks",
    "artist_original": "Angelo Badalamenti"
  },
  {
    "utwu_id": "utwu-000900",
    "title_original": "Never Let You Go",
    "artist_original": "Waldeck, Patrizia Ferrara"
  },
  {
    "utwu_id": "utwu-000901",
    "title_original": "Mother Mary: Blessings of Our Miraculous Mother of Solar Light",
    "artist_original": "Alana Fairchild"
  },
  {
    "utwu_id": "utwu-000915",
    "title_original": "You & Me",
    "artist_original": "MEUTE"
  },
  {
    "utwu_id": "utwu-000919",
    "title_original": "O Fortuna",
    "artist_original": "Charles B, MOR3L, MOTi, Amero"
  },
  {
    "utwu_id": "utwu-000920",
    "title_original": "O Fortuna",
    "artist_original": "Carl Orff, André Rieu, The Platin Tenors, Johann Strauss Orchestra, Carmen Monarcha, Mirusia, Suzan Erens"
  },
  {
    "utwu_id": "utwu-000921",
    "title_original": "Space Oddity - 2015 Remaster",
    "artist_original": "David Bowie"
  },
  {
    "utwu_id": "utwu-000922",
    "title_original": "Evolution of Music",
    "artist_original": "dj-Nate"
  },
  {
    "utwu_id": "utwu-000923",
    "title_original": "One Like You",
    "artist_original": "LP"
  },
  {
    "utwu_id": "utwu-000924",
    "title_original": "Ajai Alai",
    "artist_original": "Meditative Mind"
  },
  {
    "utwu_id": "utwu-000926",
    "title_original": "Bhagavad Gītā, Chapter 11",
    "artist_original": "Gaiea Sanskrit"
  },
  {
    "utwu_id": "utwu-000927",
    "title_original": "Lusterka",
    "artist_original": "Sw@da, Niczos"
  },
  {
    "utwu_id": "utwu-000928",
    "title_original": "Somebody That I Used To Know",
    "artist_original": "Gotye, Kimbra"
  },
  {
    "utwu_id": "utwu-000929",
    "title_original": "Somebody That I Used To Know - Tiësto Remix",
    "artist_original": "Gotye, Kimbra, Tiësto"
  },
  {
    "utwu_id": "utwu-000930",
    "title_original": "PESNA ŠTO GORI",
    "artist_original": "Da Dzaka Nakot"
  },
  {
    "utwu_id": "utwu-000931",
    "title_original": "BOG NA VOJNA",
    "artist_original": "Da Dzaka Nakot"
  },
  {
    "utwu_id": "utwu-000932",
    "title_original": "Feed Your Head",
    "artist_original": "Paul Kalkbrenner"
  },
  {
    "utwu_id": "utwu-000933",
    "title_original": "Aleksandra odchodzi",
    "artist_original": "Michał Łanuszka"
  },
  {
    "utwu_id": "utwu-000934",
    "title_original": "The Carol of the Old Ones - Soprano Version",
    "artist_original": "Мико́ла Дми́трович Леонто́вич, Mao Endo, Gico Forte"
  },
  {
    "utwu_id": "utwu-000935",
    "title_original": "Long Vajrasattva Purifying Mantra chanted in Sanskrit",
    "artist_original": "Buddha Weekly"
  },
  {
    "utwu_id": "utwu-000936",
    "title_original": "Wrecking Ball Parody",
    "artist_original": "Bart Baker"
  },
  {
    "utwu_id": "utwu-000937",
    "title_original": "Carol of the Bells - Remastered",
    "artist_original": "The Tabernacle Choir at Temple Square"
  },
  {
    "utwu_id": "utwu-000938",
    "title_original": "Toccata and Fugue in Dm Bwv 565 for Electric Guitar",
    "artist_original": "Dr.Viossy"
  },
  {
    "utwu_id": "utwu-000943",
    "title_original": "Lost On You - Live At Harvard And Stone",
    "artist_original": "LP"
  },
  {
    "utwu_id": "utwu-000944",
    "title_original": "One Day",
    "artist_original": "Typh Barrow"
  },
  {
    "utwu_id": "utwu-000949",
    "title_original": "Little Talks",
    "artist_original": "Of Monsters and Men"
  },
  {
    "utwu_id": "utwu-000950",
    "title_original": "Ukulele Song",
    "artist_original": "Jackal & the Wind"
  },
  {
    "utwu_id": "utwu-000951",
    "title_original": "Cleopatra",
    "artist_original": "The Lumineers"
  },
  {
    "utwu_id": "utwu-000952",
    "title_original": "Wicked Streets",
    "artist_original": "J. Bernardt"
  },
  {
    "utwu_id": "utwu-000953",
    "title_original": "Run",
    "artist_original": "SMOLIK / KEV FOX"
  },
  {
    "utwu_id": "utwu-000954",
    "title_original": "Renegades",
    "artist_original": "X Ambassadors"
  },
  {
    "utwu_id": "utwu-000955",
    "title_original": "Look at me Joe",
    "artist_original": "Waldeck, Patrizia Ferrara"
  },
  {
    "utwu_id": "utwu-000956",
    "title_original": "Wolves Without Teeth",
    "artist_original": "Of Monsters and Men"
  },
  {
    "utwu_id": "utwu-000957",
    "title_original": "Wish You Were Here - 2011 Remaster",
    "artist_original": "Pink Floyd"
  },
  {
    "utwu_id": "utwu-000958",
    "title_original": "I Want To Break Free",
    "artist_original": "Queen"
  },
  {
    "utwu_id": "utwu-000959",
    "title_original": "Bohemian Rhapsody",
    "artist_original": "Queen"
  },
  {
    "utwu_id": "utwu-000960",
    "title_original": "My Generation - Stereo Version",
    "artist_original": "The Who"
  },
  {
    "utwu_id": "utwu-000961",
    "title_original": "Every Breath You Take",
    "artist_original": "The Police"
  },
  {
    "utwu_id": "utwu-000962",
    "title_original": "Stairway to Heaven - Remaster",
    "artist_original": "Led Zeppelin"
  },
  {
    "utwu_id": "utwu-000963",
    "title_original": "Hey Joe",
    "artist_original": "Jimi Hendrix"
  },
  {
    "utwu_id": "utwu-000964",
    "title_original": "Under Pressure - Remastered 2011",
    "artist_original": "Queen, David Bowie"
  },
  {
    "utwu_id": "utwu-000965",
    "title_original": "People Are Strange",
    "artist_original": "The Doors"
  },
  {
    "utwu_id": "utwu-000966",
    "title_original": "Sewer Blues",
    "artist_original": "Timber Timbre"
  },
  {
    "utwu_id": "utwu-000967",
    "title_original": "Prayer in C - Robin Schulz Radio Edit",
    "artist_original": "Lilly Wood and The Prick, Robin Schulz"
  },
  {
    "utwu_id": "utwu-000968",
    "title_original": "I Need A Dollar",
    "artist_original": "Aloe Blacc"
  },
  {
    "utwu_id": "utwu-000969",
    "title_original": "Pumped Up Kicks",
    "artist_original": "Foster The People"
  },
  {
    "utwu_id": "utwu-000970",
    "title_original": "Awake My Soul",
    "artist_original": "Mumford & Sons"
  },
  {
    "utwu_id": "utwu-000971",
    "title_original": "Friday Night",
    "artist_original": "Lily Allen"
  },
  {
    "utwu_id": "utwu-000972",
    "title_original": "Witchcraft - Kristóf Kelemen Remix",
    "artist_original": "Дeva, Kristóf Kelemen"
  },
  {
    "utwu_id": "utwu-000973",
    "title_original": "Ikiri",
    "artist_original": "Дeva, Labek & Chrobak"
  },
  {
    "utwu_id": "utwu-000974",
    "title_original": "Czarne serce",
    "artist_original": "Limboski"
  },
  {
    "utwu_id": "utwu-000975",
    "title_original": "Niejasności",
    "artist_original": "Gaba Kulka"
  },
  {
    "utwu_id": "utwu-000976",
    "title_original": "Ptak głuptak",
    "artist_original": "Spięty"
  },
  {
    "utwu_id": "utwu-000977",
    "title_original": "Już nie ma dzikich plaż",
    "artist_original": "Irena Santor"
  },
  {
    "utwu_id": "utwu-000978",
    "title_original": "Party in My Pussy",
    "artist_original": "Catastrophe"
  },
  {
    "utwu_id": "utwu-000979",
    "title_original": "Qui erat et qui est",
    "artist_original": "Zbigniew Preisner"
  },
  {
    "utwu_id": "utwu-000980",
    "title_original": "Symphony No. 7, \"Siedem Bram Jerozolimy\": III. De Profundis",
    "artist_original": "Krzysztof Penderecki, Warsaw Philharmonic Orchestra"
  },
  {
    "utwu_id": "utwu-000981",
    "title_original": "Boléro, M. 81",
    "artist_original": "Maurice Ravel, Semyon Bychkov, Wiener Philharmoniker"
  },
  {
    "utwu_id": "utwu-000982",
    "title_original": "What Do You Want From Me - 2011 Remaster",
    "artist_original": "Pink Floyd"
  },
  {
    "utwu_id": "utwu-000983",
    "title_original": "Hypnotise",
    "artist_original": "The White Stripes"
  },
  {
    "utwu_id": "utwu-000984",
    "title_original": "Bizet: Carmen, Act 1: \"Quels regardes! Quelle effronterie!\" (Carmen, José)",
    "artist_original": "Georges Bizet, Maria Callas, Nicolai Gedda, Orchestre de l'Opéra National de Paris, Georges Prêtre, Orchestre du Théâtre National de l'Opéra Paris, Paris Opera Orchestra"
  },
  {
    "utwu_id": "utwu-000985",
    "title_original": "Les noces de Jeannette, Scene 4: \"Mais qu'entends-je ?\" - Chanson. \"Margot, Margot, lève ton sabot !\" (Jeannette, Jean, Chœur)",
    "artist_original": "Victor Massé, Orchestre Pasdeloup, Jean Allain, Renee Doria, Lucien Huberty, Chœurs de l'Association des Concerts Pasdeloup"
  },
  {
    "utwu_id": "utwu-000986",
    "title_original": "Rhapsody in Blue",
    "artist_original": "George Gershwin"
  },
  {
    "utwu_id": "utwu-000987",
    "title_original": "Prayer",
    "artist_original": "Zbigniew Preisner"
  },
  {
    "utwu_id": "utwu-000988",
    "title_original": "St James Infirmary",
    "artist_original": "Hugh Laurie"
  },
  {
    "utwu_id": "utwu-000989",
    "title_original": "Hujawiak",
    "artist_original": "Maria Peszek"
  },
  {
    "utwu_id": "utwu-000990",
    "title_original": "Symphony No. 9 in D Minor, Op. 125 \"Choral\": IV. Finale. Presto - Allegro assai",
    "artist_original": "Ludwig van Beethoven, Helena Juntunen, Katarina Karnéus, Daniel Norman, Neal Davies, Minnesota Chorale, Minnesota Orchestra, Osmo Vänskä"
  },
  {
    "utwu_id": "utwu-000991",
    "title_original": "Chomiczówka",
    "artist_original": "Sidney Polak"
  },
  {
    "utwu_id": "utwu-000992",
    "title_original": "Poetic Pitbull Revolution",
    "artist_original": "Diablo Swing Orchestra"
  },
  {
    "utwu_id": "utwu-000993",
    "title_original": "JPS",
    "artist_original": "Nosowska"
  },
  {
    "utwu_id": "utwu-000994",
    "title_original": "La vie en rose - DJ Antoine vs. Mad Mark 2k17 Mix",
    "artist_original": "DJ Antoine"
  },
  {
    "utwu_id": "utwu-000995",
    "title_original": "Atlas Air",
    "artist_original": "Massive Attack"
  },
  {
    "utwu_id": "utwu-000996",
    "title_original": "Pust wsiegda",
    "artist_original": "KONIEC ŚWIATA"
  },
  {
    "utwu_id": "utwu-000997",
    "title_original": "Symphony No. 9 in D Minor, Op. 125 \"Choral\": II. Molto vivace",
    "artist_original": "Ludwig van Beethoven, Helena Juntunen, Katarina Karnéus, Daniel Norman, Neal Davies, Minnesota Chorale, Minnesota Orchestra, Osmo Vänskä"
  },
  {
    "utwu_id": "utwu-000998",
    "title_original": "Superglue",
    "artist_original": "Maria Peszek"
  },
  {
    "utwu_id": "utwu-000999",
    "title_original": "Wild Honey",
    "artist_original": "Hugh Laurie"
  },
  {
    "utwu_id": "utwu-001000",
    "title_original": "Bizet: Carmen, Act 4: \"Les voici! voici la quadrille!\" (Chorus, Escamillo, Carmen, Frasquita)",
    "artist_original": "Georges Bizet, Maria Callas/Robert Massard/Nadine Sautereau/Choeurs René Duclos/Choeurs d'Enfants Jean Pesneaud/Orchestre de l'Opéra National de Paris/Georges Prêtre, Georges Prêtre, Orchestre du Théâtre National de l'Opéra Paris, Orchestre de l'Opéra National de Paris, Paris Opera Orchestra"
  },
  {
    "utwu_id": "utwu-001001",
    "title_original": "La Double vie de Véronique, marionettes: I. Tu viendras",
    "artist_original": "Zbigniew Preisner, Jeroen van Veen"
  },
  {
    "utwu_id": "utwu-001002",
    "title_original": "A Tapdancer's Dilema",
    "artist_original": "Diablo Swing Orchestra"
  },
  {
    "utwu_id": "utwu-001003",
    "title_original": "Kokon",
    "artist_original": "Artur Rojek"
  },
  {
    "utwu_id": "utwu-001004",
    "title_original": "Somebody",
    "artist_original": "The Chainsmokers, Drew Love"
  },
  {
    "utwu_id": "utwu-001005",
    "title_original": "Ailleurs et autrement",
    "artist_original": "Catastrophe"
  },
  {
    "utwu_id": "utwu-001006",
    "title_original": "Symphony No. 5: I. Funeral March - With measured step. Strict. Like a cortege - Live",
    "artist_original": "Gustav Mahler, New York Philharmonic, Lorin Maazel"
  },
  {
    "utwu_id": "utwu-001007",
    "title_original": "Cha-Ching (Till We Grow Older)",
    "artist_original": "Imagine Dragons"
  },
  {
    "utwu_id": "utwu-001008",
    "title_original": "Boléro (Ravel)",
    "artist_original": "London Symphony Orchestra"
  },
  {
    "utwu_id": "utwu-001009",
    "title_original": "Unchain My Heart",
    "artist_original": "Hugh Laurie"
  },
  {
    "utwu_id": "utwu-001010",
    "title_original": "The Greatest Show",
    "artist_original": "Hugh Jackman, Keala Settle, Zac Efron, Zendaya, The Greatest Showman Ensemble"
  },
  {
    "utwu_id": "utwu-001011",
    "title_original": "Skin",
    "artist_original": "Rag'n'Bone Man"
  },
  {
    "utwu_id": "utwu-001012",
    "title_original": "I Of The Storm",
    "artist_original": "Of Monsters and Men"
  },
  {
    "utwu_id": "utwu-001013",
    "title_original": "La Double vie de Véronique: I. Marionettes",
    "artist_original": "Zbigniew Preisner, Jeroen van Veen"
  },
  {
    "utwu_id": "utwu-001014",
    "title_original": "St. James' Infirmary Blues",
    "artist_original": "Jools Holland, Tom Jones"
  },
  {
    "utwu_id": "utwu-001015",
    "title_original": "16 Tons",
    "artist_original": "Tom Morello: the Nightwatchman"
  },
  {
    "utwu_id": "utwu-001016",
    "title_original": "Symphony No. 5: IV. Adagietto",
    "artist_original": "Gustav Mahler, Junge Deutsche Philharmonie, Rudolf Barshai"
  },
  {
    "utwu_id": "utwu-001017",
    "title_original": "Puttin' On the Ritz",
    "artist_original": "Gypsy Swing Revue"
  },
  {
    "utwu_id": "utwu-001018",
    "title_original": "Odchodząc",
    "artist_original": "Republika"
  },
  {
    "utwu_id": "utwu-001019",
    "title_original": "Put a Lid on It - Caspar Remix",
    "artist_original": "Squirrel Nut Zippers, Caspar"
  },
  {
    "utwu_id": "utwu-001020",
    "title_original": "La Vie En Rose",
    "artist_original": "Iggy Pop"
  },
  {
    "utwu_id": "utwu-001021",
    "title_original": "Bright Lights Late Nights",
    "artist_original": "The Speakeasies' Swing Band!"
  },
  {
    "utwu_id": "utwu-001022",
    "title_original": "Between the Bars",
    "artist_original": "Seth Avett & Jessica Lea Mayfield"
  },
  {
    "utwu_id": "utwu-001023",
    "title_original": "Dżentelmeni metalu",
    "artist_original": "Nocny Kochanek"
  },
  {
    "utwu_id": "utwu-001024",
    "title_original": "Les marionnettes",
    "artist_original": "Zbigniew Preisner"
  },
  {
    "utwu_id": "utwu-001025",
    "title_original": "Pink Noise Waltz",
    "artist_original": "Diablo Swing Orchestra"
  },
  {
    "utwu_id": "utwu-001026",
    "title_original": "Girl I Love You - She Is Danger Remix",
    "artist_original": "Massive Attack, Horace Andy, She is Danger"
  },
  {
    "utwu_id": "utwu-001027",
    "title_original": "1979 - Remastered 2012",
    "artist_original": "The Smashing Pumpkins"
  },
  {
    "utwu_id": "utwu-001028",
    "title_original": "Build the Fire",
    "artist_original": "Kal Cahoone"
  },
  {
    "utwu_id": "utwu-001029",
    "title_original": "SIÓDME",
    "artist_original": "Luxtorpeda"
  },
  {
    "utwu_id": "utwu-001030",
    "title_original": "Ta droga była daleka",
    "artist_original": "Kazik & Kwartet ProForma"
  },
  {
    "utwu_id": "utwu-001031",
    "title_original": "Coming Back As A Man",
    "artist_original": "Caro Emerald"
  },
  {
    "utwu_id": "utwu-001032",
    "title_original": "Bizet: Carmen, Act 2: \"Enfin c'est toi!...Tout doux, Monsieur\" (Carmen, José)",
    "artist_original": "Georges Bizet, Maria Callas, Nicolai Gedda, Orchestre de l'Opéra National de Paris, Georges Prêtre, Orchestre du Théâtre National de l'Opéra Paris, Paris Opera Orchestra"
  },
  {
    "utwu_id": "utwu-001033",
    "title_original": "Six Cold Feet",
    "artist_original": "Hugh Laurie"
  },
  {
    "utwu_id": "utwu-001034",
    "title_original": "Song for the Unification of Europe - Patrice's Version",
    "artist_original": "Zbigniew Preisner"
  },
  {
    "utwu_id": "utwu-001035",
    "title_original": "Bez znieczulenia",
    "artist_original": "Happysad"
  },
  {
    "utwu_id": "utwu-001036",
    "title_original": "Who We Are",
    "artist_original": "Imagine Dragons"
  },
  {
    "utwu_id": "utwu-001037",
    "title_original": "Hero",
    "artist_original": "Lissie"
  },
  {
    "utwu_id": "utwu-001038",
    "title_original": "Lift Me Up - 2006 Remastered Version",
    "artist_original": "Moby"
  },
  {
    "utwu_id": "utwu-001039",
    "title_original": "Co się z nami stało",
    "artist_original": "Strachy Na Lachy"
  },
  {
    "utwu_id": "utwu-001040",
    "title_original": "Wizja dźwięku",
    "artist_original": "Piotr Rogucki"
  },
  {
    "utwu_id": "utwu-001041",
    "title_original": "Happy",
    "artist_original": "Kat Frankie"
  },
  {
    "utwu_id": "utwu-001042",
    "title_original": "When I Get Low, I Get High",
    "artist_original": "The Speakeasy Three"
  },
  {
    "utwu_id": "utwu-001043",
    "title_original": "Polska",
    "artist_original": "Nosowska"
  },
  {
    "utwu_id": "utwu-001044",
    "title_original": "Nie raj - Radio Edit",
    "artist_original": "Lao Che"
  },
  {
    "utwu_id": "utwu-001045",
    "title_original": "Second Chances",
    "artist_original": "Imagine Dragons"
  },
  {
    "utwu_id": "utwu-001046",
    "title_original": "Kokon - Live",
    "artist_original": "Artur Rojek"
  },
  {
    "utwu_id": "utwu-001047",
    "title_original": "Czuły barbarzyńca",
    "artist_original": "Matylda/Łukasiewicz, Matylda, Radek Łukasiewicz"
  },
  {
    "utwu_id": "utwu-001048",
    "title_original": "Spektakl",
    "artist_original": "Spięty"
  },
  {
    "utwu_id": "utwu-001049",
    "title_original": "Cichosza",
    "artist_original": "IKARVS"
  },
  {
    "utwu_id": "utwu-001050",
    "title_original": "Pan Piotruś Pan",
    "artist_original": "Spięty"
  },
  {
    "utwu_id": "utwu-001051",
    "title_original": "Sing Sing",
    "artist_original": "Maja Kleszcz"
  },
  {
    "utwu_id": "utwu-001052",
    "title_original": "Residue",
    "artist_original": "Benjamin Clementine"
  },
  {
    "utwu_id": "utwu-001053",
    "title_original": "Čálkko Niillas",
    "artist_original": "Hildá Länsman, Tuomas Norvio"
  },
  {
    "utwu_id": "utwu-001054",
    "title_original": "Bored",
    "artist_original": "Billie Eilish"
  },
  {
    "utwu_id": "utwu-001055",
    "title_original": "Space Oddity - 2019 Mix, Single Edit",
    "artist_original": "David Bowie"
  },
  {
    "utwu_id": "utwu-001056",
    "title_original": "Za Ostatni Grosz",
    "artist_original": "Budka Suflera"
  },
  {
    "utwu_id": "utwu-001057",
    "title_original": "Poles Apart - 2011 Remaster",
    "artist_original": "Pink Floyd"
  },
  {
    "utwu_id": "utwu-001058",
    "title_original": "So Long, Marianne - MTV Unplugged Live in Melbourne",
    "artist_original": "Courtney Barnett"
  }
]

def zapisz_stan(path, state):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def wybierz(ydl, row):
    query = row["artist_original"] + " " + row["title_original"]
    while True:
        result = ydl.extract_info("ytsearch5:" + query, download=False)
        entries = [e for e in (result or {}).get("entries", []) if e and
                   re.fullmatch(r"[A-Za-z0-9_-]{11}", e.get("id", ""))]
        print("\n" + row["utwu_id"] + ": " + row["artist_original"] + " — " + row["title_original"])
        for n, entry in enumerate(entries, 1):
            print(f'{n}. {entry.get("title")} | {entry.get("uploader") or entry.get("channel")} | {entry.get("duration")} s')
            print("   https://www.youtube.com/watch?v=" + entry["id"])
        answer = input("Numer nagrania; Enter=pomiń; q=koniec; /=nowe wyszukiwanie: ").strip()
        if answer.lower() == "q":
            raise KeyboardInterrupt
        if not answer:
            return None
        if answer.startswith("/"):
            query = answer[1:].strip() or query
            continue
        if answer.isdigit() and 1 <= int(answer) <= len(entries):
            entry = entries[int(answer) - 1]
            return {"youtube_video_id": entry["id"], "selected_title": entry.get("title"),
                    "selected_channel": entry.get("uploader") or entry.get("channel"),
                    "status": "selected"}


def uzupelnij(katalog, limit):
    try:
        import yt_dlp
    except ImportError:
        print('Zainstaluj: python -m pip install -U "yt-dlp[default]"')
        return 1
    katalog.mkdir(parents=True, exist_ok=True)
    state_path = katalog / "braki-211-stan.json"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    downloaded = 0
    errors = 0
    search_opts = {"quiet": True, "extract_flat": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(search_opts) as search:
            for row in BRAKI:
                uid = row["utwu_id"]
                record = state.get(uid, {})
                if record.get("status") == "downloaded" and Path(record.get("filename", "")).is_file():
                    continue
                if downloaded >= limit:
                    break
                try:
                    if not record.get("youtube_video_id"):
                        record = wybierz(search, row)
                        if record is None:
                            continue
                        state[uid] = {**row, **record}
                        zapisz_stan(state_path, state)
                    video_id = record["youtube_video_id"]
                    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
                        raise ValueError("Nieprawidłowy identyfikator w pliku stanu: " + uid)
                    # Osobny folder zapobiega kolizjom numerów ze starą playlistą.
                    # Numer pochodzi z utwu_id, pełne mapowanie zostaje w stanie JSON.
                    number = int(uid.split("-")[1])
                    opts = {
                        "format": "bestaudio/best", "noplaylist": True,
                        "overwrites": False, "continuedl": True,
                        "outtmpl": str(katalog / (f"{number:04d} - %(artist,uploader)s - %(title).100s [%(id)s].%(ext)s")),
                    }
                    # Archiwum starej playlisty nie oznacza zakończenia tego utwu_id.
                    # Sukces zapisujemy dopiero po istnieniu pliku; błędy są ponawiane.
                    with yt_dlp.YoutubeDL(opts) as download:
                        info = download.extract_info("https://www.youtube.com/watch?v=" + video_id, download=True)
                        if not info:
                            raise RuntimeError("Brak wyniku pobrania")
                        filename = download.prepare_filename(info)
                    if not Path(filename).is_file():
                        raise RuntimeError("Nie znaleziono końcowego pliku audio")
                    state[uid] = {**row, **record, "status": "downloaded", "filename": filename}
                    state[uid].pop("error", None)
                    zapisz_stan(state_path, state)
                    downloaded += 1
                except (yt_dlp.utils.DownloadError, ValueError, RuntimeError) as exc:
                    errors += 1
                    state[uid] = {**row, **(record or {}), "status": "error", "error": str(exc)}
                    zapisz_stan(state_path, state)
                    print(f"Błąd {uid}: {exc}")
    except (KeyboardInterrupt, EOFError):
        print("\nPrzerwano. Zapisane wybory i ukończone pobrania zostają zachowane.")
    print(f"Ukończone w tym uruchomieniu: {downloaded}; błędy: {errors}.")
    print(f"Stan i mapowanie utwu_id → YouTube → plik: {state_path}")
    return 1 if errors else 0


def cli():
    global PLAYLIST_URL
    parser = argparse.ArgumentParser(description="Audio SOL: 211 braków z bazy (stan 2026-09-14) lub playlista.")
    parser.add_argument("--playlist", help="Dawny tryb: URL playlisty")
    parser.add_argument("--limit", type=int, default=ILE_NA_RAZ, help="Limit udanych pobrań braków (domyślnie 100)")
    parser.add_argument("--katalog", type=Path, help="Folder audio dla braków")
    parser.add_argument("--lista", action="store_true", help="Pokaż listę braków bez połączeń i pobierania")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit musi być dodatni")
    if args.lista:
        for row in BRAKI:
            print(row["utwu_id"], row["artist_original"], "—", row["title_original"])
        print(f"RAZEM: {len(BRAKI)}")
        return 0
    if args.playlist:
        PLAYLIST_URL = args.playlist
        return main()
    if args.katalog is None and not (Path.home() / "storage" / "music").exists():
        print("W Termuxie wykonaj termux-setup-storage lub podaj --katalog.")
        return 1
    return uzupelnij((args.katalog or KATALOG / "braki-2026-09-14").expanduser().resolve(), args.limit)


if __name__ == "__main__":
    sys.exit(cli())
