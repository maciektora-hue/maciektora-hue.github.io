#!/usr/bin/env python3
from pathlib import Path
import subprocess
import csv
import math
import os
import shutil
import sys

try:
    import numpy as np
except ImportError:
    print("\nBRAK numpy.")
    print("W Termuxie zainstaluj:")
    print("pkg install python-numpy ffmpeg")
    sys.exit(1)

# ============================================================
# AUDIO ANALYSIS v05
# NOWA seria obliczeń od zera.
# Nie korzysta z plików stanu ani CSV wersji v01/v02/v03/v04.
#
# KATALOG Z PLIKAMI .webm:
KATALOG = Path.home() / "storage" / "music" / "YTMusic_playlist"
# ============================================================

BATCH_SIZE = 100

SAMPLE_RATE = 48000
N_FFT = 4096
HOP = 2048
CHUNK_FRAMES = 256
EPS = 1e-12

# Osobny, gęstszy tor rytmiczny tylko do estymacji BPM.
# Nie zmienia parametrów STFT używanych dla pozostałych cech.
RHYTHM_WINDOW = 2048
RHYTHM_HOP = 256
BPM_MIN = 40.0
BPM_MAX = 220.0
BPM_PRIOR_CENTER = 120.0
BPM_PRIOR_SIGMA_OCT = 0.9

WYNIK_CSV = KATALOG / "audio_features_v05.csv"
STAN_TXT = KATALOG / "audio_features_v05_done.txt"
BLEDY_TXT = KATALOG / "audio_features_v05_errors.txt"

PASMA = [
    ("20_60", 20, 60),
    ("60_120", 60, 120),
    ("120_250", 120, 250),
    ("250_500", 250, 500),
    ("500_1000", 500, 1000),
    ("1000_2000", 1000, 2000),
    ("2000_4000", 2000, 4000),
    ("4000_8000", 4000, 8000),
    ("8000_12000", 8000, 12000),
    ("12000_20000", 12000, 20000),
]

CONTRAST_BANDS = [
    ("50_100", 50, 100),
    ("100_200", 100, 200),
    ("200_400", 200, 400),
    ("400_800", 400, 800),
    ("800_1600", 800, 1600),
    ("1600_3200", 1600, 3200),
    ("3200_6400", 3200, 6400),
    ("6400_12800", 6400, 12800),
]

CHROMA_NAMES = ["C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B"]

# Chroma v05: osobny tor wysokiej rozdzielczości.
# Cel: mniej rozsmarowania po 12 klasach, lepsza tonalność i osobna estymacja key.
# Bez librosy/scipy, żeby działało sensownie w Termuxie.
CHROMA_N_FFT = 16384
CHROMA_HOP = 4096
CHROMA_CHUNK_FRAMES = 64
CHROMA_FMIN = 80.0
CHROMA_NOTE_FMAX = 2000.0
CHROMA_SPECTRUM_FMAX = 5000.0
CHROMA_BINS_PER_SEMITONE = 3
CHROMA_BINS = 12 * CHROMA_BINS_PER_SEMITONE
CHROMA_PEAK_FLOOR_DB = -40.0
CHROMA_OCTAVE_GATE_DB = -18.0
CHROMA_MAX_PEAKS_PER_FRAME = 60
CHROMA_SHARPEN_POWER = 1.5
CHROMA_FOLD_SIGMA_SEMITONES = 0.22
CHROMA_FOLD_MAX_DISTANCE = 0.50
CHROMA_HARMONIC_WEIGHTS = np.array([1.0, 0.55, 0.35, 0.25, 0.18], dtype=np.float64)



def percentile_fields(prefix):
    return [
        f"{prefix}_mean",
        f"{prefix}_std",
        f"{prefix}_p10",
        f"{prefix}_p50",
        f"{prefix}_p90",
    ]


POLA = [
    "plik",
    "sciezka_wzgledna",
    "rozmiar_mb",
    "czas_s",
    "sample_rate_hz",
    "channels",
    "n_fft",
    "hop",
    "liczba_ramek",

    # amplituda stereo
    "rms_left",
    "rms_left_dbfs",
    "rms_right",
    "rms_right_dbfs",
    "peak_left",
    "peak_left_dbfs",
    "peak_right",
    "peak_right_dbfs",
    "crest_left",
    "crest_left_db",
    "crest_right",
    "crest_right_db",
    "over_0dbfs_fraction_left",
    "over_0dbfs_fraction_right",

    # mid/side i stereo
    "rms_mid",
    "rms_mid_dbfs",
    "peak_mid",
    "peak_mid_dbfs",
    "rms_side",
    "rms_side_dbfs",
    "stereo_balance_db_L_over_R",
    "stereo_correlation_LR",
    "stereo_width_side_over_mid",
    "stereo_width_db",
    "over_0dbfs_fraction_mid",
]

POLA += percentile_fields("frame_rms")
POLA += percentile_fields("frame_zcr")
POLA += percentile_fields("spectral_centroid_hz")
POLA += percentile_fields("spectral_rolloff85_hz")
POLA += percentile_fields("spectral_bandwidth_hz")
POLA += percentile_fields("spectral_flatness")
POLA += percentile_fields("spectral_flux")
POLA += percentile_fields("spectral_slope_db_per_khz")

POLA += [
    "spectral_variability_mean",
    "spectral_edge_99_hz",
    "spectral_edge_999_hz",
    "spectral_cutoff_m60db_hz",
]

POLA += [f"band_{name}_fraction" for name, _, _ in PASMA]

for name, _, _ in CONTRAST_BANDS:
    POLA += [
        f"spectral_contrast_{name}_mean_db",
        f"spectral_contrast_{name}_std_db",
    ]

for i in range(1, 14):
    POLA += [f"mfcc_{i:02d}_mean", f"mfcc_{i:02d}_std"]

for name in CHROMA_NAMES:
    POLA += [f"chroma_{name}_mean", f"chroma_{name}_std"]

POLA += [
    "chroma_tuning_cents",
    "chroma_tuning_confidence",
    "chroma_entropy_mean",
    "chroma_entropy_std",
    "chroma_peak_contrast_mean",
    "chroma_peak_contrast_std",
    "chroma_active_frames_fraction",
    "chroma_dominant_pc_index",
    "chroma_dominant_pc_name",
    "chroma_dominant_strength",
    "chroma_key_root_index",
    "chroma_key_mode",
    "chroma_key_name",
    "chroma_key_score",
    "chroma_key_second_score",
    "chroma_key_margin",
    "chroma_key_confidence",
    "chroma_frame_count",
    "chroma_n_fft",
    "chroma_hop",
]

POLA += [
    "onset_strength_mean",
    "onset_strength_std",
    "onset_strength_p90",
    "onset_count",
    "onset_rate_per_s",
    "onset_interval_mean_s",
    "onset_interval_std_s",
    "onset_interval_cv",
    "bpm_estimate",
    "bpm_confidence",
    "bpm_candidate_2",
    "bpm_candidate_3",
    "bpm_interval_estimate",
    "bpm_interval_confidence",
    "bpm_period_s",
    "bpm_rhythm_window",
    "bpm_rhythm_hop",
]


def dbfs(x):
    x = float(x)
    if x <= 0:
        return -200.0
    return 20.0 * math.log10(x)


def mean_std_p(values):
    if len(values) == 0:
        return 0.0, 0.0, 0.0, 0.0, 0.0
    a = np.asarray(values, dtype=np.float64)
    return (
        float(np.mean(a)),
        float(np.std(a)),
        float(np.percentile(a, 10)),
        float(np.percentile(a, 50)),
        float(np.percentile(a, 90)),
    )


def put_stats(row, prefix, values):
    m, s, p10, p50, p90 = mean_std_p(values)
    row[f"{prefix}_mean"] = m
    row[f"{prefix}_std"] = s
    row[f"{prefix}_p10"] = p10
    row[f"{prefix}_p50"] = p50
    row[f"{prefix}_p90"] = p90


def wczytaj_stan():
    if not STAN_TXT.exists():
        return set()
    return {
        line.strip()
        for line in STAN_TXT.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def zapisz_done(rel_path):
    with STAN_TXT.open("a", encoding="utf-8") as f:
        f.write(rel_path + "\n")
        f.flush()
        os.fsync(f.fileno())


def zapisz_blad(rel_path, msg):
    with BLEDY_TXT.open("a", encoding="utf-8") as f:
        f.write(f"{rel_path}\t{msg}\n")


def dekoduj_stereo_f32(path):
    cmd = [
        "ffmpeg",
        "-v", "error",
        "-i", str(path),
        "-vn",
        "-ac", "2",
        "-ar", str(SAMPLE_RATE),
        "-f", "f32le",
        "-acodec", "pcm_f32le",
        "pipe:1",
    ]

    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if p.returncode != 0:
        err = p.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(err or f"ffmpeg exit code {p.returncode}")

    raw = np.frombuffer(p.stdout, dtype="<f4")
    if raw.size < 2:
        raise RuntimeError("Brak próbek audio po dekodowaniu")

    if raw.size % 2:
        raw = raw[:-1]

    stereo = raw.reshape(-1, 2)
    return stereo


def frame_view(x):
    if len(x) < N_FFT:
        x = np.pad(x, (0, N_FFT - len(x)))

    n_frames = 1 + (len(x) - N_FFT) // HOP
    n_frames = max(n_frames, 1)

    shape = (n_frames, N_FFT)
    strides = (x.strides[0] * HOP, x.strides[0])

    return np.lib.stride_tricks.as_strided(
        x,
        shape=shape,
        strides=strides,
        writeable=False,
    )


def hz_to_mel(hz):
    return 2595.0 * np.log10(1.0 + hz / 700.0)


def mel_to_hz(mel):
    return 700.0 * (10.0 ** (mel / 2595.0) - 1.0)


def build_sparse_mel_filters(freq, n_filters=26, fmin=20.0, fmax=20000.0):
    mel_points = np.linspace(hz_to_mel(fmin), hz_to_mel(fmax), n_filters + 2)
    hz_points = mel_to_hz(mel_points)

    filters = []
    for i in range(n_filters):
        left, center, right = hz_points[i:i + 3]
        idx = np.where((freq >= left) & (freq <= right))[0]
        if idx.size == 0:
            filters.append((idx, np.array([], dtype=np.float64)))
            continue

        f = freq[idx]
        w = np.zeros_like(f, dtype=np.float64)

        rising = f <= center
        if center > left:
            w[rising] = (f[rising] - left) / (center - left)

        falling = f > center
        if right > center:
            w[falling] = (right - f[falling]) / (right - center)

        w = np.maximum(w, 0.0)
        filters.append((idx, w))

    return filters


def build_dct_matrix(n_filters=26, n_mfcc=13):
    n = np.arange(n_filters, dtype=np.float64)
    # MFCC 1..13, bez C0
    rows = []
    for k in range(1, n_mfcc + 1):
        rows.append(np.cos(np.pi / n_filters * (n + 0.5) * k))
    dct = np.vstack(rows)
    dct *= math.sqrt(2.0 / n_filters)
    return dct


def weighted_mean_std_matrix(values, weights):
    values = np.asarray(values, dtype=np.float64)
    weights = np.asarray(weights, dtype=np.float64)

    if len(values) == 0 or np.sum(weights) <= EPS:
        return np.zeros(values.shape[1], dtype=np.float64), np.zeros(values.shape[1], dtype=np.float64)

    w = weights / (np.sum(weights) + EPS)
    mean = np.sum(values * w[:, None], axis=0)
    var = np.sum(((values - mean[None, :]) ** 2) * w[:, None], axis=0)
    return mean, np.sqrt(np.maximum(var, 0.0))



def frame_view_custom(x, n_fft, hop):
    """Widok ramek dla osobnego toru analizy."""
    x = np.asarray(x, dtype=np.float32)

    if len(x) < n_fft:
        x = np.pad(x, (0, n_fft - len(x)))

    n_frames = 1 + (len(x) - n_fft) // hop
    n_frames = max(n_frames, 1)

    shape = (n_frames, n_fft)
    strides = (x.strides[0] * hop, x.strides[0])

    return np.lib.stride_tricks.as_strided(
        x,
        shape=shape,
        strides=strides,
        writeable=False,
    )


def build_chroma_fold_matrix_v05(tuning_semitones):
    """
    36 binów -> 12 klas.
    W v05 przypisanie jest wąskie: maks. +/- 0.5 półtonu.
    Nie rozlewamy już pojedynczego binu aż na pełny półton w każdą stronę.
    """
    positions = np.arange(CHROMA_BINS, dtype=np.float64) / CHROMA_BINS_PER_SEMITONE
    positions = positions - tuning_semitones

    fold = np.zeros((CHROMA_BINS, 12), dtype=np.float64)

    for b, pos in enumerate(positions):
        for c in range(12):
            d = ((pos - c + 6.0) % 12.0) - 6.0
            ad = abs(d)
            if ad <= CHROMA_FOLD_MAX_DISTANCE:
                fold[b, c] = math.exp(
                    -0.5 * (ad / CHROMA_FOLD_SIGMA_SEMITONES) ** 2
                )

    sums = np.sum(fold, axis=1, keepdims=True)

    # Przy bardzo pechowym położeniu numerycznym wybierz najbliższą klasę.
    missing = np.where(sums[:, 0] <= EPS)[0]
    for b in missing:
        pos = positions[b]
        distances = np.array([
            abs(((pos - c + 6.0) % 12.0) - 6.0)
            for c in range(12)
        ])
        fold[b, int(np.argmin(distances))] = 1.0

    fold /= np.sum(fold, axis=1, keepdims=True) + EPS
    return fold


def _interp_mag_at_freq(mag, target_freq, bin_hz):
    """Liniowa interpolacja amplitudy widma w zadanej częstotliwości."""
    x = target_freq / bin_hz
    lo = int(math.floor(x))
    frac = x - lo

    if lo < 0 or lo >= len(mag):
        return 0.0
    if lo + 1 >= len(mag):
        return float(mag[lo])

    return float((1.0 - frac) * mag[lo] + frac * mag[lo + 1])


def _pitch_class_key_estimate(chroma_mean):
    """
    Krumhansl-Schmuckler: 24 profile (12 major + 12 minor).
    Zwraca najlepszą tonację i margines nad drugą.
    """
    major = np.array(
        [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88],
        dtype=np.float64,
    )
    minor = np.array(
        [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17],
        dtype=np.float64,
    )

    obs = np.asarray(chroma_mean, dtype=np.float64)
    if obs.size != 12 or np.sum(obs) <= EPS:
        return {
            "chroma_key_root_index": -1,
            "chroma_key_mode": "",
            "chroma_key_name": "",
            "chroma_key_score": 0.0,
            "chroma_key_second_score": 0.0,
            "chroma_key_margin": 0.0,
            "chroma_key_confidence": 0.0,
        }

    obs = obs - np.mean(obs)
    obs_norm = np.linalg.norm(obs)
    if obs_norm <= EPS:
        return {
            "chroma_key_root_index": -1,
            "chroma_key_mode": "",
            "chroma_key_name": "",
            "chroma_key_score": 0.0,
            "chroma_key_second_score": 0.0,
            "chroma_key_margin": 0.0,
            "chroma_key_confidence": 0.0,
        }
    obs /= obs_norm

    scores = []
    meta = []

    for mode, template in (("major", major), ("minor", minor)):
        t = template - np.mean(template)
        t /= np.linalg.norm(t) + EPS

        for root in range(12):
            score = float(np.dot(obs, np.roll(t, root)))
            scores.append(score)
            meta.append((root, mode))

    order = np.argsort(scores)[::-1]
    best_i = int(order[0])
    second_i = int(order[1]) if len(order) > 1 else best_i

    best = float(scores[best_i])
    second = float(scores[second_i])
    margin = best - second
    root, mode = meta[best_i]

    # Confidence jest pomocnicze, 0..1. Nie udaje prawdopodobieństwa.
    confidence = float(np.clip(margin / (abs(best) + EPS), 0.0, 1.0))
    name = f"{CHROMA_NAMES[root]} {mode}"

    return {
        "chroma_key_root_index": int(root),
        "chroma_key_mode": mode,
        "chroma_key_name": name,
        "chroma_key_score": best,
        "chroma_key_second_score": second,
        "chroma_key_margin": margin,
        "chroma_key_confidence": confidence,
    }


def analyze_chroma_v05(mid):
    """
    Osobny tor chromy v05.

    Najważniejsze różnice względem v04:
    - FFT 16384 / hop 4096, czyli ~2.93 Hz/bin zamiast ~11.72 Hz/bin,
    - tylko lokalne piki >= -40 dB,
    - kandydat nuty dostaje premię za zgodny szereg harmoniczny,
    - słabe oktawy są bramkowane przy -18 dB, bez agresywnego wyrównywania,
    - 36-binowa reprezentacja zachowuje informację o odstrojeniach,
    - po korekcji strojenia fold 36->12 ma tylko +/-0.5 półtonu,
    - zamiast sqrt() używamy potęgi 1.5, czyli chromę WYOSTRZAMY,
    - ramki do średniej wybieramy przez RMS + tonalność, nie przez banalne >p10,
    - osobno liczymy dominant pitch class i tonację major/minor.
    """
    x = np.asarray(mid, dtype=np.float32)
    frames = frame_view_custom(x, CHROMA_N_FFT, CHROMA_HOP)
    n_frames = len(frames)

    window = np.hanning(CHROMA_N_FFT).astype(np.float32)
    freq = np.fft.rfftfreq(CHROMA_N_FFT, d=1.0 / SAMPLE_RATE)
    bin_hz = SAMPLE_RATE / CHROMA_N_FFT

    lo_bin = max(1, int(math.floor(CHROMA_FMIN / bin_hz)))
    hi_bin = min(len(freq) - 2, int(math.ceil(CHROMA_SPECTRUM_FMAX / bin_hz)))
    note_hi_bin = min(hi_bin, int(math.ceil(CHROMA_NOTE_FMAX / bin_hz)))

    chroma36_frames = np.zeros((n_frames, CHROMA_BINS), dtype=np.float32)
    rms_values = np.zeros(n_frames, dtype=np.float64)
    flatness_values = np.ones(n_frames, dtype=np.float64)

    tuning_z = 0.0 + 0.0j
    tuning_wsum = 0.0

    floor_ratio = 10.0 ** (CHROMA_PEAK_FLOOR_DB / 20.0)
    octave_gate_ratio = 10.0 ** (CHROMA_OCTAVE_GATE_DB / 20.0)

    for start in range(0, n_frames, CHROMA_CHUNK_FRAMES):
        stop = min(start + CHROMA_CHUNK_FRAMES, n_frames)
        fr = np.asarray(frames[start:stop], dtype=np.float32)
        fr64 = fr.astype(np.float64, copy=False)
        rms_values[start:stop] = np.sqrt(np.mean(fr64 * fr64, axis=1))

        spec = np.fft.rfft(fr * window[None, :], axis=1)
        mags = np.abs(spec).astype(np.float64)

        band = mags[:, lo_bin:hi_bin + 1] + EPS
        flatness_values[start:stop] = (
            np.exp(np.mean(np.log(band), axis=1)) /
            (np.mean(band, axis=1) + EPS)
        )

        for local_i in range(len(fr)):
            frame_i = start + local_i
            mag = mags[local_i]

            search = mag[lo_bin:note_hi_bin + 1]
            if search.size < 3:
                continue

            frame_max = float(np.max(search))
            if frame_max <= EPS:
                continue

            local = np.zeros(len(search), dtype=bool)
            local[1:-1] = (
                (search[1:-1] > search[:-2]) &
                (search[1:-1] >= search[2:])
            )
            local &= search >= frame_max * floor_ratio

            pidx_local = np.where(local)[0]
            if pidx_local.size == 0:
                continue

            # Zostaw tylko najmocniejsze piki. Reszta to zwykle harmoniczny pył.
            if pidx_local.size > CHROMA_MAX_PEAKS_PER_FRAME:
                strongest = np.argsort(search[pidx_local])[-CHROMA_MAX_PEAKS_PER_FRAME:]
                pidx_local = pidx_local[strongest]

            pidx = pidx_local + lo_bin

            # Sub-binowa interpolacja paraboli w log-amplitudzie.
            logmag = np.log(mag + EPS)
            y1 = logmag[pidx - 1]
            y2 = logmag[pidx]
            y3 = logmag[pidx + 1]
            denom = y1 - 2.0 * y2 + y3
            delta = np.zeros_like(y2)
            good = np.abs(denom) > 1e-12
            delta[good] = 0.5 * (y1[good] - y3[good]) / denom[good]
            delta = np.clip(delta, -0.5, 0.5)

            peak_freq = (pidx.astype(np.float64) + delta) * bin_hz
            peak_amp = mag[pidx] / (frame_max + EPS)

            scores = np.zeros(len(pidx), dtype=np.float64)

            # Harmoniczne głosowanie:
            # kandydat fundamentalny ma większy score, jeśli widmo wspiera też 2f,3f...
            for j, f0 in enumerate(peak_freq):
                if f0 < CHROMA_FMIN or f0 > CHROMA_NOTE_FMAX:
                    continue

                harmonic_score = 0.0
                support = 0

                for h, hw in enumerate(CHROMA_HARMONIC_WEIGHTS, start=1):
                    fh = f0 * h
                    if fh > CHROMA_SPECTRUM_FMAX:
                        break

                    a = _interp_mag_at_freq(mag, fh, bin_hz) / (frame_max + EPS)
                    harmonic_score += float(hw) * a

                    if a >= floor_ratio:
                        support += 1

                # Fundamentalny pik jest obowiązkowy, a zgodne harmoniczne premiują.
                scores[j] = (
                    (peak_amp[j] ** 0.70) *
                    harmonic_score *
                    (1.0 + 0.12 * max(support - 1, 0))
                )

            keep = scores > EPS
            if not np.any(keep):
                continue

            peak_freq = peak_freq[keep]
            scores = scores[keep]

            midi = 69.0 + 12.0 * np.log2(peak_freq / 440.0)
            octaves = np.floor(midi / 12.0).astype(int)

            # Bramka oktaw -18 dB. Bez normalizacji każdej oktawy do tej samej wagi.
            octave_totals = {}
            for o in np.unique(octaves):
                octave_totals[int(o)] = float(np.sum(scores[octaves == o]))

            max_oct = max(octave_totals.values()) if octave_totals else 0.0
            if max_oct <= EPS:
                continue

            keep_oct = np.array([
                octave_totals[int(o)] >= max_oct * octave_gate_ratio
                for o in octaves
            ], dtype=bool)

            peak_freq = peak_freq[keep_oct]
            scores = scores[keep_oct]
            midi = midi[keep_oct]
            octaves = octaves[keep_oct]

            if scores.size == 0:
                continue

            # Łagodna premia dla mocniejszych oktaw, bez starego "wszyscy po równo".
            for o in np.unique(octaves):
                mask = octaves == o
                rel = octave_totals[int(o)] / (max_oct + EPS)
                scores[mask] *= rel ** 0.35

            # Strojenie: najlepiej wspierane kandydaty mają największy głos.
            residual = midi - np.rint(midi)
            tuning_z += np.sum(scores * np.exp(2j * np.pi * residual))
            tuning_wsum += float(np.sum(scores))

            # 36 binów / oktawę klas wysokości, interpolacja liniowa.
            pos = np.mod(midi * CHROMA_BINS_PER_SEMITONE, CHROMA_BINS)
            b0 = np.floor(pos).astype(int)
            frac = pos - b0
            b1 = (b0 + 1) % CHROMA_BINS

            c36 = np.zeros(CHROMA_BINS, dtype=np.float64)
            np.add.at(c36, b0, scores * (1.0 - frac))
            np.add.at(c36, b1, scores * frac)

            chroma36_frames[frame_i] = c36.astype(np.float32, copy=False)

    if tuning_wsum > EPS and abs(tuning_z) > EPS:
        tuning_semitones = float(np.angle(tuning_z) / (2.0 * np.pi))
        tuning_semitones = float(np.clip(tuning_semitones, -0.5, 0.5))
        tuning_conf = float(abs(tuning_z) / tuning_wsum)
    else:
        tuning_semitones = 0.0
        tuning_conf = 0.0

    fold = build_chroma_fold_matrix_v05(tuning_semitones)
    chroma12 = chroma36_frames.astype(np.float64) @ fold

    sums = np.sum(chroma12, axis=1, keepdims=True)
    valid_rows = sums[:, 0] > EPS
    chroma12[valid_rows] /= sums[valid_rows]

    # v04 robiło sqrt(), czyli spłaszczało. v05 robi odwrotnie: lekkie wyostrzenie.
    chroma12 = np.maximum(chroma12, 0.0) ** CHROMA_SHARPEN_POWER
    sums = np.sum(chroma12, axis=1, keepdims=True)
    valid_rows = sums[:, 0] > EPS
    chroma12[valid_rows] /= sums[valid_rows]

    entropy = -np.sum(chroma12 * np.log(chroma12 + EPS), axis=1) / math.log(12.0)
    sorted_chroma = np.sort(chroma12, axis=1)
    peak_contrast = sorted_chroma[:, -1] - sorted_chroma[:, -2]
    concentration = np.clip(1.0 - entropy, 0.0, 1.0)

    if n_frames:
        rms_med = float(np.median(rms_values)) + EPS
        rms_p25 = float(np.percentile(rms_values, 25))
        amp_weight = np.clip(rms_values / rms_med, 0.0, 2.0)

        # Tonalność: skoncentrowana chroma + przewaga głównej klasy,
        # dodatkowo tłumienie ramek szumowych.
        contrast_scaled = np.clip(peak_contrast / 0.20, 0.0, 1.0)
        tonal_score = (
            0.65 * concentration +
            0.35 * contrast_scaled
        )
        noise_weight = np.exp(-5.0 * np.clip(flatness_values, 0.0, 1.0))

        tonal_threshold = float(np.percentile(tonal_score, 40))
        active_frames = (
            (rms_values >= max(rms_p25, EPS)) &
            (tonal_score >= tonal_threshold) &
            valid_rows &
            (peak_contrast >= 0.005)
        )

        chroma_weights = (
            amp_weight *
            noise_weight *
            (0.10 + 0.90 * tonal_score) *
            active_frames.astype(np.float64)
        )

        # Awaryjnie: jeśli materiał jest bardzo mało tonalny, nie zeruj wyniku całkiem.
        if np.sum(chroma_weights) <= EPS:
            chroma_weights = (
                amp_weight *
                noise_weight *
                (0.10 + 0.90 * tonal_score) *
                valid_rows.astype(np.float64)
            )
            active_frames = valid_rows
    else:
        chroma_weights = np.zeros(0, dtype=np.float64)
        active_frames = np.zeros(0, dtype=bool)

    if np.sum(chroma_weights) > EPS:
        chroma_mean, chroma_std = weighted_mean_std_matrix(chroma12, chroma_weights)
        w = chroma_weights / (np.sum(chroma_weights) + EPS)

        ent_mean = float(np.sum(entropy * w))
        ent_std = float(np.sqrt(np.sum(((entropy - ent_mean) ** 2) * w)))
        pc_mean = float(np.sum(peak_contrast * w))
        pc_std = float(np.sqrt(np.sum(((peak_contrast - pc_mean) ** 2) * w)))
    else:
        chroma_mean = np.zeros(12, dtype=np.float64)
        chroma_std = np.zeros(12, dtype=np.float64)
        ent_mean = 1.0
        ent_std = 0.0
        pc_mean = 0.0
        pc_std = 0.0

    out = {}

    for i, name in enumerate(CHROMA_NAMES):
        out[f"chroma_{name}_mean"] = float(chroma_mean[i])
        out[f"chroma_{name}_std"] = float(chroma_std[i])

    dominant = int(np.argmax(chroma_mean)) if np.sum(chroma_mean) > EPS else -1

    out.update({
        "chroma_tuning_cents": float(tuning_semitones * 100.0),
        "chroma_tuning_confidence": float(tuning_conf),
        "chroma_entropy_mean": ent_mean,
        "chroma_entropy_std": ent_std,
        "chroma_peak_contrast_mean": pc_mean,
        "chroma_peak_contrast_std": pc_std,
        "chroma_active_frames_fraction": float(np.mean(active_frames)) if n_frames else 0.0,
        "chroma_dominant_pc_index": dominant,
        "chroma_dominant_pc_name": CHROMA_NAMES[dominant] if dominant >= 0 else "",
        "chroma_dominant_strength": float(np.max(chroma_mean)) if dominant >= 0 else 0.0,
        "chroma_frame_count": int(n_frames),
        "chroma_n_fft": int(CHROMA_N_FFT),
        "chroma_hop": int(CHROMA_HOP),
    })

    out.update(_pitch_class_key_estimate(chroma_mean))
    return out


def fft_autocorr(x):
    x = np.asarray(x, dtype=np.float64)
    if x.size == 0:
        return np.array([], dtype=np.float64)

    x = x - np.mean(x)
    n = x.size
    nfft = 1 << (2 * n - 1).bit_length()
    spec = np.fft.rfft(x, n=nfft)
    ac = np.fft.irfft(spec * np.conj(spec), n=nfft)[:n]
    return ac


def _frame_energy_fast(x, window, hop):
    """Szybka energia ramek bez dodatkowego FFT."""
    x = np.asarray(x, dtype=np.float64)

    if x.size < window:
        x = np.pad(x, (0, window - x.size))

    sq = x * x
    csum = np.concatenate(([0.0], np.cumsum(sq)))
    starts = np.arange(0, len(x) - window + 1, hop, dtype=np.int64)

    if starts.size == 0:
        return np.array([], dtype=np.float64)

    energy = (csum[starts + window] - csum[starts]) / window
    return energy


def _robust_positive(v):
    v = np.asarray(v, dtype=np.float64)
    if v.size == 0:
        return v

    med = float(np.median(v))
    mad = float(np.median(np.abs(v - med))) + EPS
    z = (v - med) / (1.4826 * mad)
    return np.maximum(z, 0.0)


def rhythm_onset_envelope(x):
    """
    Gęsty envelope rytmiczny co 256 próbek (~5.33 ms).
    Łączy zmianę energii sygnału i zmianę energii sygnału różnicowego.
    Liczy się porcjami, żeby nie produkować wielkich tablic pośrednich.
    """
    x = np.asarray(x, dtype=np.float32)

    if x.size < 2:
        return np.array([], dtype=np.float64)

    if len(x) < RHYTHM_WINDOW:
        x = np.pad(x, (0, RHYTHM_WINDOW - len(x)))

    n_frames = 1 + (len(x) - RHYTHM_WINDOW) // RHYTHM_HOP
    if n_frames <= 0:
        return np.array([], dtype=np.float64)

    frames = np.lib.stride_tricks.as_strided(
        x,
        shape=(n_frames, RHYTHM_WINDOW),
        strides=(x.strides[0] * RHYTHM_HOP, x.strides[0]),
        writeable=False,
    )

    energy = np.empty(n_frames, dtype=np.float64)
    diff_energy = np.empty(n_frames, dtype=np.float64)

    rhythm_chunk = 512

    for start in range(0, n_frames, rhythm_chunk):
        stop = min(start + rhythm_chunk, n_frames)
        fr = frames[start:stop]

        sq = fr * fr
        energy[start:stop] = np.mean(sq, axis=1, dtype=np.float64)

        d = np.diff(fr, axis=1)
        diff_energy[start:stop] = np.mean(d * d, axis=1, dtype=np.float64)

    log_e = np.log(energy + EPS)
    log_d = np.log(diff_energy + EPS)

    de = np.maximum(np.diff(log_e, prepend=log_e[0]), 0.0)
    dd = np.maximum(np.diff(log_d, prepend=log_d[0]), 0.0)

    env = 0.5 * _robust_positive(de) + 0.5 * _robust_positive(dd)

    # Krótkie wygładzenie ~16 ms.
    if env.size >= 3:
        env = np.convolve(env, np.ones(3, dtype=np.float64) / 3.0, mode="same")

    # Odcinamy stałe tło, zostawiając transjenty.
    floor = float(np.percentile(env, 60))
    env = np.maximum(env - floor, 0.0)

    return env


def _parabolic_lag(ac, lag, n):
    """
    Interpolacja paraboliczna maksimum autokorelacji.
    Zwraca lag ułamkowy, a nie wyłącznie całkowitą liczbę ramek.
    """
    if lag <= 0 or lag >= len(ac) - 1:
        return float(lag)

    def unbiased(i):
        return float(ac[i]) / max(n - i, 1)

    y1 = unbiased(lag - 1)
    y2 = unbiased(lag)
    y3 = unbiased(lag + 1)

    denom = y1 - 2.0 * y2 + y3
    if abs(denom) <= EPS:
        return float(lag)

    delta = 0.5 * (y1 - y3) / denom
    delta = float(np.clip(delta, -0.5, 0.5))
    return float(lag + delta)


def _tempo_candidates(env):
    env = np.asarray(env, dtype=np.float64)

    if env.size < 16 or np.max(env) <= EPS:
        return []

    ac = fft_autocorr(env)
    if ac.size < 4 or ac[0] <= EPS:
        return []

    frame_rate = SAMPLE_RATE / RHYTHM_HOP
    n = len(env)

    lag_min = max(
        2,
        int(math.floor(frame_rate * 60.0 / BPM_MAX)),
    )
    lag_max = min(
        len(ac) - 2,
        int(math.ceil(frame_rate * 60.0 / BPM_MIN)),
    )

    if lag_max <= lag_min:
        return []

    lags = np.arange(lag_min, lag_max + 1, dtype=np.int64)
    values = ac[lags] / np.maximum(n - lags, 1)

    if values.size < 3:
        return []

    local = (
        (values[1:-1] >= values[:-2]) &
        (values[1:-1] > values[2:])
    )
    idx = np.where(local)[0] + 1

    if idx.size == 0:
        idx = np.array([int(np.argmax(values))], dtype=np.int64)

    base = float(ac[0]) / n + EPS
    candidates = []

    for j in idx:
        lag = int(lags[j])
        lag_f = _parabolic_lag(ac, lag, n)

        if lag_f <= 0:
            continue

        bpm = 60.0 * frame_rate / lag_f

        strength = float(ac[lag]) / max(n - lag, 1) / base
        strength = float(np.clip(strength, 0.0, 1.0))

        # Bardzo szeroki prior tylko do rozstrzygania typowego
        # half/double-tempo. Alternatywy i tak zapisujemy do CSV.
        prior = math.exp(
            -0.5 *
            (math.log2(max(bpm, EPS) / BPM_PRIOR_CENTER) / BPM_PRIOR_SIGMA_OCT) ** 2
        )

        score = strength * prior

        candidates.append({
            "bpm": float(bpm),
            "strength": strength,
            "score": float(score),
            "lag": float(lag_f),
        })

    candidates.sort(key=lambda c: c["score"], reverse=True)
    return candidates


def _interval_bpm_estimate(env):
    """
    Niezależny wskaźnik diagnostyczny z odstępów między pikami onsetu.
    Zwraca BPM i pewność opartą o zgodność odstępów.
    """
    env = np.asarray(env, dtype=np.float64)

    if env.size < 3 or np.max(env) <= EPS:
        return 0.0, 0.0

    threshold = float(np.median(env) + 0.75 * np.std(env))

    candidates = np.where(
        (env[1:-1] > env[:-2]) &
        (env[1:-1] >= env[2:]) &
        (env[1:-1] > threshold)
    )[0] + 1

    if candidates.size < 2:
        return 0.0, 0.0

    min_distance = max(
        1,
        int(round(0.10 * SAMPLE_RATE / RHYTHM_HOP)),
    )

    kept = []
    last = -10**9

    for idx in candidates:
        idx = int(idx)

        if idx - last >= min_distance:
            kept.append(idx)
            last = idx
        elif kept and env[idx] > env[kept[-1]]:
            kept[-1] = idx
            last = idx

    if len(kept) < 2:
        return 0.0, 0.0

    intervals = np.diff(np.asarray(kept, dtype=np.float64))
    intervals_s = intervals * RHYTHM_HOP / SAMPLE_RATE

    valid = intervals_s > 0
    if not np.any(valid):
        return 0.0, 0.0

    bpm_values = 60.0 / intervals_s[valid]

    for i in range(len(bpm_values)):
        while bpm_values[i] < BPM_MIN:
            bpm_values[i] *= 2.0
        while bpm_values[i] > BPM_MAX:
            bpm_values[i] *= 0.5

    bpm = float(np.median(bpm_values))

    log_dev = np.abs(np.log2(np.maximum(bpm_values, EPS) / max(bpm, EPS)))
    dispersion_oct = float(np.median(log_dev))

    # 0.08 oktawy ~ 5.7%. Im ciaśniejszy rozkład interwałów,
    # tym bardziej można ufać tej pomocniczej estymacji.
    confidence = math.exp(-dispersion_oct / 0.08)
    confidence *= min(1.0, len(bpm_values) / 20.0)
    confidence = float(np.clip(confidence, 0.0, 1.0))

    return bpm, confidence


def estimate_bpm_v03(x):
    env = rhythm_onset_envelope(x)
    candidates = _tempo_candidates(env)
    interval_bpm, interval_conf = _interval_bpm_estimate(env)

    if candidates and interval_bpm > 0.0 and interval_conf > 0.0:
        # Drugi, niezależny pomiar pomaga rozstrzygnąć half/double tempo,
        # ale tylko gdy odstępy onsetów są dostatecznie regularne.
        for c in candidates:
            octave_distance = abs(
                math.log2(max(c["bpm"], EPS) / max(interval_bpm, EPS))
            )
            agreement = math.exp(
                -0.5 * (octave_distance / 0.08) ** 2
            )
            c["score"] *= 1.0 + 0.75 * interval_conf * agreement

        candidates.sort(key=lambda c: c["score"], reverse=True)

    if not candidates:
        return {
            "bpm_estimate": 0.0,
            "bpm_confidence": 0.0,
            "bpm_candidate_2": 0.0,
            "bpm_candidate_3": 0.0,
            "bpm_interval_estimate": interval_bpm,
            "bpm_interval_confidence": interval_conf,
            "bpm_period_s": 0.0,
            "bpm_rhythm_window": RHYTHM_WINDOW,
            "bpm_rhythm_hop": RHYTHM_HOP,
        }

    best = candidates[0]
    second_score = candidates[1]["score"] if len(candidates) > 1 else 0.0

    separation = 1.0 - min(
        second_score / (best["score"] + EPS),
        1.0,
    )

    confidence = float(
        np.clip(best["strength"] * separation, 0.0, 1.0)
    )

    bpm = float(best["bpm"])

    return {
        "bpm_estimate": bpm,
        "bpm_confidence": confidence,
        "bpm_candidate_2": float(candidates[1]["bpm"]) if len(candidates) > 1 else 0.0,
        "bpm_candidate_3": float(candidates[2]["bpm"]) if len(candidates) > 2 else 0.0,
        "bpm_interval_estimate": interval_bpm,
        "bpm_interval_confidence": interval_conf,
        "bpm_period_s": 60.0 / bpm if bpm > EPS else 0.0,
        "bpm_rhythm_window": RHYTHM_WINDOW,
        "bpm_rhythm_hop": RHYTHM_HOP,
    }


def onset_peaks(onset_env):
    env = np.asarray(onset_env, dtype=np.float64)

    if env.size < 3:
        return np.array([], dtype=np.int64)

    threshold = float(np.median(env) + np.std(env))
    candidates = np.where(
        (env[1:-1] > env[:-2]) &
        (env[1:-1] >= env[2:]) &
        (env[1:-1] > threshold)
    )[0] + 1

    if candidates.size == 0:
        return candidates

    min_distance = max(1, int(round(0.15 * SAMPLE_RATE / HOP)))

    kept = []
    last = -10**9
    for idx in candidates:
        if idx - last >= min_distance:
            kept.append(int(idx))
            last = int(idx)
        elif kept and env[idx] > env[kept[-1]]:
            kept[-1] = int(idx)
            last = int(idx)

    return np.asarray(kept, dtype=np.int64)


def analizuj(stereo):
    left = stereo[:, 0].astype(np.float64, copy=False)
    right = stereo[:, 1].astype(np.float64, copy=False)

    mid = (left + right) * 0.5
    side = (left - right) * 0.5

    duration_s = len(mid) / SAMPLE_RATE

    rms_l = float(np.sqrt(np.mean(left * left)))
    rms_r = float(np.sqrt(np.mean(right * right)))
    rms_mid = float(np.sqrt(np.mean(mid * mid)))
    rms_side = float(np.sqrt(np.mean(side * side)))

    peak_l = float(np.max(np.abs(left)))
    peak_r = float(np.max(np.abs(right)))
    peak_mid = float(np.max(np.abs(mid)))

    crest_l = peak_l / rms_l if rms_l > EPS else 0.0
    crest_r = peak_r / rms_r if rms_r > EPS else 0.0

    balance_db = 20.0 * math.log10((rms_l + EPS) / (rms_r + EPS))

    l0 = left - np.mean(left)
    r0 = right - np.mean(right)
    denom = math.sqrt(float(np.sum(l0 * l0) * np.sum(r0 * r0)))
    corr = float(np.sum(l0 * r0) / denom) if denom > EPS else 0.0

    width_ratio = rms_side / (rms_mid + EPS)
    width_db = 20.0 * math.log10(width_ratio + EPS)

    row = {
        "czas_s": duration_s,
        "sample_rate_hz": SAMPLE_RATE,
        "channels": 2,
        "n_fft": N_FFT,
        "hop": HOP,

        "rms_left": rms_l,
        "rms_left_dbfs": dbfs(rms_l),
        "rms_right": rms_r,
        "rms_right_dbfs": dbfs(rms_r),
        "peak_left": peak_l,
        "peak_left_dbfs": dbfs(peak_l),
        "peak_right": peak_r,
        "peak_right_dbfs": dbfs(peak_r),
        "crest_left": crest_l,
        "crest_left_db": dbfs(crest_l),
        "crest_right": crest_r,
        "crest_right_db": dbfs(crest_r),
        "over_0dbfs_fraction_left": float(np.mean(np.abs(left) > 1.0)),
        "over_0dbfs_fraction_right": float(np.mean(np.abs(right) > 1.0)),

        "rms_mid": rms_mid,
        "rms_mid_dbfs": dbfs(rms_mid),
        "peak_mid": peak_mid,
        "peak_mid_dbfs": dbfs(peak_mid),
        "rms_side": rms_side,
        "rms_side_dbfs": dbfs(rms_side),
        "stereo_balance_db_L_over_R": balance_db,
        "stereo_correlation_LR": corr,
        "stereo_width_side_over_mid": width_ratio,
        "stereo_width_db": width_db,
        "over_0dbfs_fraction_mid": float(np.mean(np.abs(mid) > 1.0)),
    }

    mid32 = mid.astype(np.float32, copy=False)
    frames = frame_view(mid32)
    n_frames = len(frames)
    row["liczba_ramek"] = n_frames

    window = np.hanning(N_FFT).astype(np.float32)
    freq = np.fft.rfftfreq(N_FFT, d=1.0 / SAMPLE_RATE)
    n_bins = len(freq)

    band_masks = {
        name: np.where((freq >= lo) & (freq < hi))[0]
        for name, lo, hi in PASMA
    }

    contrast_masks = {
        name: np.where((freq >= lo) & (freq < hi))[0]
        for name, lo, hi in CONTRAST_BANDS
    }

    mel_filters = build_sparse_mel_filters(freq)
    dct = build_dct_matrix()

    slope_mask = np.where((freq >= 50.0) & (freq <= 16000.0))[0]
    slope_x = freq[slope_mask] / 1000.0
    slope_xc = slope_x - np.mean(slope_x)
    slope_denom = float(np.sum(slope_xc * slope_xc)) + EPS

    frame_rms_values = []
    frame_zcr_values = []
    centroid_values = []
    rolloff_values = []
    bandwidth_values = []
    flatness_values = []
    flux_values = []
    slope_values = []

    contrast_sum = {name: 0.0 for name, _, _ in CONTRAST_BANDS}
    contrast_sq_sum = {name: 0.0 for name, _, _ in CONTRAST_BANDS}

    band_energy = {name: 0.0 for name, _, _ in PASMA}
    total_energy = 0.0

    spectrum_power_sum = np.zeros(n_bins, dtype=np.float64)
    spectrum_mag_sum = np.zeros(n_bins, dtype=np.float64)
    spectrum_mag_sq_sum = np.zeros(n_bins, dtype=np.float64)

    mfcc_sum = np.zeros(13, dtype=np.float64)
    mfcc_sq_sum = np.zeros(13, dtype=np.float64)

    prev_norm_mag = None
    contrast_frames = 0

    for start in range(0, n_frames, CHUNK_FRAMES):
        stop = min(start + CHUNK_FRAMES, n_frames)
        fr = np.asarray(frames[start:stop], dtype=np.float32)

        # cechy czasowe per ramka
        fr64 = fr.astype(np.float64, copy=False)
        fr_rms = np.sqrt(np.mean(fr64 * fr64, axis=1))
        frame_rms_values.extend(fr_rms.tolist())

        signs = np.signbit(fr)
        changes = np.count_nonzero(signs[:, 1:] != signs[:, :-1], axis=1)
        fr_zcr = changes / (N_FFT - 1)
        frame_zcr_values.extend(fr_zcr.tolist())

        # STFT
        spec = np.fft.rfft(fr * window[None, :], axis=1)
        mag = np.abs(spec).astype(np.float64)
        power = mag * mag

        spectrum_power_sum += np.sum(power, axis=0)
        spectrum_mag_sum += np.sum(mag, axis=0)
        spectrum_mag_sq_sum += np.sum(mag * mag, axis=0)

        power_sum = np.sum(power, axis=1)
        mag_sum = np.sum(mag, axis=1)

        total_energy += float(np.sum(power_sum))

        # pasma
        for name, _, _ in PASMA:
            idx = band_masks[name]
            if idx.size:
                band_energy[name] += float(np.sum(power[:, idx]))

        # centroid
        centroid = np.sum(mag * freq[None, :], axis=1) / (mag_sum + EPS)
        centroid_values.extend(centroid.tolist())

        # rolloff 85%
        cumsum = np.cumsum(power, axis=1)
        threshold = 0.85 * cumsum[:, -1]
        ridx = np.argmax(cumsum >= threshold[:, None], axis=1)
        rolloff = freq[ridx]
        rolloff_values.extend(rolloff.tolist())

        # bandwidth
        diff = freq[None, :] - centroid[:, None]
        bandwidth = np.sqrt(np.sum((diff * diff) * mag, axis=1) / (mag_sum + EPS))
        bandwidth_values.extend(bandwidth.tolist())

        # flatness
        positive = mag + EPS
        flatness = np.exp(np.mean(np.log(positive), axis=1)) / np.mean(positive, axis=1)
        flatness_values.extend(flatness.tolist())

        # flux
        norms = np.linalg.norm(mag, axis=1, keepdims=True) + EPS
        norm_mag = mag / norms

        if prev_norm_mag is not None:
            flux_values.append(float(np.sqrt(np.mean((norm_mag[0] - prev_norm_mag) ** 2))))

        if len(norm_mag) > 1:
            df = norm_mag[1:] - norm_mag[:-1]
            flux_values.extend(np.sqrt(np.mean(df * df, axis=1)).tolist())

        prev_norm_mag = norm_mag[-1].copy()

        # spectral slope w dB/kHz
        dbmag = 20.0 * np.log10(mag[:, slope_mask] + EPS)
        slopes = (dbmag @ slope_xc) / slope_denom
        slope_values.extend(slopes.tolist())

        # spectral contrast
        for name, _, _ in CONTRAST_BANDS:
            idx = contrast_masks[name]
            if idx.size >= 2:
                vals = 20.0 * np.log10(mag[:, idx] + EPS)
                hi = np.percentile(vals, 90, axis=1)
                lo = np.percentile(vals, 10, axis=1)
                contrast = hi - lo
                contrast_sum[name] += float(np.sum(contrast))
                contrast_sq_sum[name] += float(np.sum(contrast * contrast))

        contrast_frames += len(fr)

        # MFCC 1..13
        mel_energy = np.empty((len(fr), len(mel_filters)), dtype=np.float64)
        for j, (idx, weights) in enumerate(mel_filters):
            if idx.size:
                mel_energy[:, j] = np.sum(power[:, idx] * weights[None, :], axis=1)
            else:
                mel_energy[:, j] = 0.0

        log_mel = np.log(mel_energy + EPS)
        mfcc = log_mel @ dct.T
        mfcc_sum += np.sum(mfcc, axis=0)
        mfcc_sq_sum += np.sum(mfcc * mfcc, axis=0)


    put_stats(row, "frame_rms", frame_rms_values)
    put_stats(row, "frame_zcr", frame_zcr_values)
    put_stats(row, "spectral_centroid_hz", centroid_values)
    put_stats(row, "spectral_rolloff85_hz", rolloff_values)
    put_stats(row, "spectral_bandwidth_hz", bandwidth_values)
    put_stats(row, "spectral_flatness", flatness_values)
    put_stats(row, "spectral_flux", flux_values)
    put_stats(row, "spectral_slope_db_per_khz", slope_values)

    # zmienność widma
    mean_mag = spectrum_mag_sum / max(n_frames, 1)
    mean_mag_sq = spectrum_mag_sq_sum / max(n_frames, 1)
    std_mag = np.sqrt(np.maximum(mean_mag_sq - mean_mag * mean_mag, 0.0))
    valid = mean_mag > EPS
    if np.any(valid):
        row["spectral_variability_mean"] = float(
            np.mean(std_mag[valid] / (mean_mag[valid] + EPS))
        )
    else:
        row["spectral_variability_mean"] = 0.0

    # spectral edges / praktyczny cutoff
    mean_power = spectrum_power_sum / max(n_frames, 1)
    cumulative = np.cumsum(mean_power)
    if cumulative[-1] > EPS:
        idx99 = int(np.searchsorted(cumulative, 0.99 * cumulative[-1]))
        idx999 = int(np.searchsorted(cumulative, 0.999 * cumulative[-1]))
        idx99 = min(idx99, len(freq) - 1)
        idx999 = min(idx999, len(freq) - 1)
        row["spectral_edge_99_hz"] = float(freq[idx99])
        row["spectral_edge_999_hz"] = float(freq[idx999])
    else:
        row["spectral_edge_99_hz"] = 0.0
        row["spectral_edge_999_hz"] = 0.0

    kernel = np.ones(9, dtype=np.float64) / 9.0
    smooth_power = np.convolve(mean_power, kernel, mode="same")
    threshold = float(np.max(smooth_power)) * 1e-6  # -60 dB w mocy
    above = np.where(smooth_power >= threshold)[0]
    row["spectral_cutoff_m60db_hz"] = float(freq[above[-1]]) if above.size else 0.0

    # pasma
    for name, _, _ in PASMA:
        row[f"band_{name}_fraction"] = (
            band_energy[name] / total_energy if total_energy > EPS else 0.0
        )

    # contrast
    for name, _, _ in CONTRAST_BANDS:
        if contrast_frames > 0:
            m = contrast_sum[name] / contrast_frames
            v = max(contrast_sq_sum[name] / contrast_frames - m * m, 0.0)
            row[f"spectral_contrast_{name}_mean_db"] = m
            row[f"spectral_contrast_{name}_std_db"] = math.sqrt(v)
        else:
            row[f"spectral_contrast_{name}_mean_db"] = 0.0
            row[f"spectral_contrast_{name}_std_db"] = 0.0

    # MFCC
    mfcc_mean = mfcc_sum / max(n_frames, 1)
    mfcc_var = np.maximum(mfcc_sq_sum / max(n_frames, 1) - mfcc_mean * mfcc_mean, 0.0)
    mfcc_std = np.sqrt(mfcc_var)

    for i in range(13):
        row[f"mfcc_{i + 1:02d}_mean"] = float(mfcc_mean[i])
        row[f"mfcc_{i + 1:02d}_std"] = float(mfcc_std[i])

    # chroma v05: osobny tor wysokiej rozdzielczości.
    row.update(analyze_chroma_v05(mid))

    # onset / rytm / BPM
    onset = np.asarray(flux_values, dtype=np.float64)
    if onset.size:
        onset = np.maximum(onset - np.median(onset), 0.0)
        peaks = onset_peaks(onset)

        row["onset_strength_mean"] = float(np.mean(onset))
        row["onset_strength_std"] = float(np.std(onset))
        row["onset_strength_p90"] = float(np.percentile(onset, 90))
        row["onset_count"] = int(len(peaks))
        row["onset_rate_per_s"] = float(len(peaks) / duration_s) if duration_s > 0 else 0.0

        if len(peaks) >= 2:
            intervals = np.diff(peaks) * HOP / SAMPLE_RATE
            mean_i = float(np.mean(intervals))
            std_i = float(np.std(intervals))
            row["onset_interval_mean_s"] = mean_i
            row["onset_interval_std_s"] = std_i
            row["onset_interval_cv"] = std_i / mean_i if mean_i > EPS else 0.0
        else:
            row["onset_interval_mean_s"] = 0.0
            row["onset_interval_std_s"] = 0.0
            row["onset_interval_cv"] = 0.0

        bpm_info = estimate_bpm_v03(mid)
        row.update(bpm_info)
    else:
        row["onset_strength_mean"] = 0.0
        row["onset_strength_std"] = 0.0
        row["onset_strength_p90"] = 0.0
        row["onset_count"] = 0
        row["onset_rate_per_s"] = 0.0
        row["onset_interval_mean_s"] = 0.0
        row["onset_interval_std_s"] = 0.0
        row["onset_interval_cv"] = 0.0
        row.update(estimate_bpm_v03(mid32))

    return row


def przygotuj_csv():
    nowy = not WYNIK_CSV.exists() or WYNIK_CSV.stat().st_size == 0
    f = WYNIK_CSV.open("a", newline="", encoding="utf-8-sig")
    writer = csv.DictWriter(f, fieldnames=POLA)

    if nowy:
        writer.writeheader()
        f.flush()
        os.fsync(f.fileno())

    return f, writer


def main():
    if shutil.which("ffmpeg") is None:
        print("\nBRAK ffmpeg.")
        print("W Termuxie zainstaluj:")
        print("pkg install ffmpeg")
        sys.exit(1)

    if not KATALOG.exists():
        print(f"\nNie ma katalogu:\n{KATALOG}")
        print("\nJeżeli Termux nie ma dostępu do pamięci:")
        print("termux-setup-storage")
        sys.exit(1)

    files = sorted(
        p for p in KATALOG.rglob("*")
        if p.is_file() and p.suffix.lower() == ".webm"
    )

    if not files:
        print(f"\nBrak plików .webm w:\n{KATALOG}")
        sys.exit(0)

    done = wczytaj_stan()

    pozostale = [
        p for p in files
        if str(p.relative_to(KATALOG)) not in done
    ]

    print("\n================ AUDIO ANALYSIS v05 ================")
    print("NOWA seria od zera — niezależna od v01/v02/v03/v04")
    print(f"Wszystkich .webm:        {len(files)}")
    print(f"v05 już policzonych:     {len(done)}")
    print(f"v05 pozostało:           {len(pozostale)}")
    print(f"Limit uruchomienia:      {BATCH_SIZE}")
    print(f"Liczba kolumn CSV:       {len(POLA)}")
    print(f"BPM tor rytmiczny:       window={RHYTHM_WINDOW}, hop={RHYTHM_HOP}")
    print(f"CSV v05:                 {WYNIK_CSV}")
    print(f"Stan v05:                {STAN_TXT}\n")

    if not pozostale:
        print("Wszystkie utwory są już policzone w v05.")
        return

    csv_file, writer = przygotuj_csv()

    sukces = 0
    bledy = 0

    try:
        for path in pozostale:
            if sukces >= BATCH_SIZE:
                break

            rel = str(path.relative_to(KATALOG))
            print(f"[{sukces + 1}/{BATCH_SIZE}] {path.name}")

            try:
                stereo = dekoduj_stereo_f32(path)
                cechy = analizuj(stereo)

                row = {
                    "plik": path.name,
                    "sciezka_wzgledna": rel,
                    "rozmiar_mb": path.stat().st_size / 1024 / 1024,
                }
                row.update(cechy)

                writer.writerow(row)
                csv_file.flush()
                os.fsync(csv_file.fileno())

                zapisz_done(rel)
                done.add(rel)
                sukces += 1

                print(
                    f"   OK | {cechy['czas_s']:.1f}s | "
                    f"BPM {cechy['bpm_estimate']:.1f} | "
                    f"centroid {cechy['spectral_centroid_hz_mean']:.0f} Hz | "
                    f"corr LR {cechy['stereo_correlation_LR']:.3f}"
                )

                del stereo

            except KeyboardInterrupt:
                print("\nPrzerwano ręcznie.")
                break
            except Exception as e:
                bledy += 1
                msg = str(e).replace("\n", " | ")
                print(f"   BŁĄD: {msg}")
                zapisz_blad(rel, msg)

    finally:
        csv_file.close()

    print("\n================ KONIEC BATCHA v05 ================")
    print(f"Policzono nowych: {sukces}")
    print(f"Błędów:           {bledy}")
    print(f"Łącznie v05:      {len(done)}")
    print(f"CSV:               {WYNIK_CSV}")

    if sukces >= BATCH_SIZE:
        print("\nUruchom ten sam skrypt ponownie dla następnej setki.")
    elif len(done) >= len(files):
        print("\nWszystkie utwory są policzone w v05.")
    else:
        print("\nZostały niepoliczone pliki; uruchom v05 ponownie.")


if __name__ == "__main__":
    main()
