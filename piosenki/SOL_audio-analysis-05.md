# SOL audio-analysis v05

Standalone'owy skrypt do analizy lokalnych plików `.webm` z playlisty YouTube Music w Termuxie. Nie zmienia plików źródłowych i nie tworzy WAV-ów na dysku: `ffmpeg` dekoduje audio do 2-kanałowego PCM float32 w locie, a Python/NumPy liczy cechy.

## Założenia

- katalog wejściowy: `~/storage/music/YTMusic_playlist`
- pliki wejściowe: `.webm`
- batch: maksymalnie 100 nowych utworów na jedno uruchomienie
- wznowienie: na podstawie osobnego pliku stanu v05
- v05 jest niezależne od v01/v02/v03/v04 i zaczyna własną serię obliczeń od zera
- wynik: jeden rekord CSV na utwór
- liczba kolumn: 191

## Pliki tworzone przez skrypt

- `audio_features_v05.csv` — wynik analizy
- `audio_features_v05_done.txt` — lista już policzonych plików
- `audio_features_v05_errors.txt` — błędy

Wiersz CSV jest zapisywany i synchronizowany na dysk przed dopisaniem pliku do `done`, więc przerwanie procesu nie powinno oznaczać utraty całej wykonanej paczki.

## Główny tor STFT

Parametry:

- sample rate: 48 kHz
- stereo: 2 kanały
- FFT: 4096
- hop: 2048
- okno: Hann

Liczone są między innymi:

- RMS i peak osobno L/R
- crest factor
- udział próbek > 0 dBFS
- mid/side
- balans L/R
- korelacja stereo
- szerokość stereo
- RMS ramek i ZCR
- spectral centroid
- rolloff 85%
- bandwidth
- spectral flatness
- spectral flux
- spectral slope
- spectral variability
- spectral edge 99% i 99.9%
- praktyczny cutoff przy -60 dB
- energia w 10 pasmach od 20 Hz do 20 kHz
- spectral contrast w 8 pasmach
- MFCC 1–13, średnia i odchylenie standardowe

## BPM v03, zachowane w v05

BPM ma osobny gęsty tor rytmiczny, żeby uniknąć schodków wynikających z grubego hopu STFT.

Parametry:

- rhythm window: 2048
- rhythm hop: 256, czyli około 5.33 ms
- zakres: 40–220 BPM

Estymator wykorzystuje:

- gęsty envelope zmian energii i energii sygnału różnicowego
- autokorelację
- interpolację paraboliczną maksimum, więc lag nie musi być całkowity
- kilka kandydatów BPM
- szeroki prior pomagający rozstrzygać half/double tempo
- niezależny pomocniczy pomiar z odstępów między onsetami

Do CSV trafiają m.in. `bpm_estimate`, `bpm_confidence`, kandydat 2 i 3, niezależne `bpm_interval_estimate` oraz jego confidence.

## Chroma v05

To główna zmiana względem v04. v04 nadal zbyt mocno rozsmarowywało energię po 12 klasach wysokości. v05 ma osobny tor chromy o większej rozdzielczości częstotliwościowej.

Parametry:

- chroma FFT: 16384
- chroma hop: 4096
- rozdzielczość przy 48 kHz: około 2.93 Hz/bin
- analiza nut: 80–2000 Hz
- wsparcie harmoniczne widma: do 5000 Hz
- reprezentacja pośrednia: 36 binów, po 3 na półton
- próg lokalnych pików: -40 dB względem maksimum ramki
- maksymalnie 60 najmocniejszych pików na ramkę
- bramka oktaw: -18 dB

### Co robi tor chromy

1. Wykrywa lokalne piki widmowe zamiast traktować całe widmo jako równoprawne źródło informacji tonalnej.
2. Interpoluje położenie piku poniżej rozdzielczości pojedynczego binu FFT.
3. Stosuje harmonic voting: kandydat na ton podstawowy dostaje większą wagę, jeśli widmo wspiera również jego 2f, 3f itd.
4. Odrzuca słabe oktawy zamiast agresywnie wyrównywać wszystkie oktawy.
5. Zachowuje 36-binową reprezentację do estymacji odstrojenia.
6. Szacuje globalne strojenie w centach i jego confidence.
7. Po korekcji strojenia składa 36 binów do 12 klas przez wąskie gaussowskie przypisanie, maksymalnie ±0.5 półtonu.
8. Zamiast spłaszczającego `sqrt(chroma)` stosuje wyostrzenie `chroma^1.5`.
9. Ramki są ważone przez amplitudę, spectral flatness i koncentrację tonalną, więc szumowe/perkusyjne fragmenty mają mniejszy wpływ.

Do CSV trafiają średnie i odchylenia dla C, C#, D, D#, E, F, F#, G, G#, A, A#, B oraz:

- tuning w centach + confidence
- entropia chromy
- kontrast między najsilniejszymi klasami
- udział aktywnych tonalnie ramek
- dominująca klasa wysokości
- jej siła

## Estymacja tonacji

v05 rozdziela dwie rzeczy:

- dominującą klasę wysokości
- tonację utworu

Tonacja jest estymowana przez dopasowanie średniego profilu chromy do 24 profili Krumhansl-Schmuckler: 12 tonacji major i 12 minor.

Zapisywane są:

- root
- major/minor
- pełna nazwa tonacji
- wynik najlepszego profilu
- wynik drugiego profilu
- margines między nimi
- pomocnicze `key_confidence`

`key_confidence` jest wskaźnikiem diagnostycznym, nie prawdopodobieństwem statystycznym.

## Uruchomienie w Termuxie

Wymagania:

```bash
pkg install python-numpy ffmpeg
termux-setup-storage
```

Uruchomienie:

```bash
python SOL_audio-analysis-05.py
```

Po policzeniu 100 nowych utworów skrypt kończy działanie. Następne uruchomienie pomija wpisy z `audio_features_v05_done.txt` i liczy kolejną setkę.

## Status wersji

v05 powstało po teście pierwszych 100 utworów v04. BPM v04 przestał mieć wcześniejszy problem kwantyzacji do niewielkiej liczby wartości, natomiast chroma nadal była zbyt płaska i miała podejrzany rozkład dominant. v05 przebudowuje właśnie tor chromy. Przed puszczeniem całej playlisty warto ponownie sprawdzić pierwsze 100 utworów i rozkład chromy/tonacji.
