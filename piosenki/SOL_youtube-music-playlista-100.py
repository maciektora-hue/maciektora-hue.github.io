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


if __name__ == "__main__":
    main()
