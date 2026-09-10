-- SOL — schema Turso / SQLite
-- Źródła: sol-o-co-kaman-HTML-v01-00.html, aktywne CSV oraz sol-ontologia-tagow-TXT-v01-03.txt
-- Walencja i biegunowość są osobnymi warstwami semantycznymi.

PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

CREATE TABLE lyrics (
  lyrics_id TEXT PRIMARY KEY,
  lyrics_text TEXT NOT NULL
);

CREATE TABLE tag_catalog (
  tag TEXT PRIMARY KEY,
  definition TEXT
);

CREATE TABLE families (
  family_name TEXT PRIMARY KEY,
  label TEXT NOT NULL,
  color_hex TEXT NOT NULL,
  description TEXT NOT NULL,
  sort_order INTEGER NOT NULL UNIQUE
);

CREATE TABLE tag_groups (
  group_name TEXT PRIMARY KEY,
  label TEXT NOT NULL
);

CREATE TABLE axes (
  axis_name TEXT PRIMARY KEY,
  label TEXT NOT NULL,
  description TEXT NOT NULL,
  family_name TEXT NOT NULL REFERENCES families(family_name),
  sort_order INTEGER NOT NULL UNIQUE
);

CREATE TABLE tag_group (
  tag TEXT NOT NULL REFERENCES tag_catalog(tag),
  group_name TEXT NOT NULL REFERENCES tag_groups(group_name),
  PRIMARY KEY (tag, group_name)
);

CREATE TABLE tag_axis (
  tag TEXT NOT NULL REFERENCES tag_catalog(tag),
  axis_name TEXT NOT NULL REFERENCES axes(axis_name),
  PRIMARY KEY (tag, axis_name)
);

CREATE TABLE tag_valence (
  tag TEXT PRIMARY KEY REFERENCES tag_catalog(tag),
  valence INTEGER,
  status TEXT NOT NULL,
  CHECK (valence IN (-1, 0, 1) OR valence IS NULL),
  CHECK (status IN ('resolved', 'contextual', 'unresolved')),
  CHECK (
    (status = 'resolved' AND valence IS NOT NULL)
    OR
    (status IN ('contextual', 'unresolved') AND valence IS NULL)
  )
);

CREATE TABLE tag_axis_polarity (
  tag TEXT NOT NULL REFERENCES tag_catalog(tag),
  axis_name TEXT NOT NULL REFERENCES axes(axis_name),
  polarity INTEGER,
  status TEXT NOT NULL,
  PRIMARY KEY (tag, axis_name),
  CHECK (polarity IN (-1, 0, 1) OR polarity IS NULL),
  CHECK (status IN ('resolved', 'contextual', 'unresolved')),
  CHECK (
    (status = 'resolved' AND polarity IS NOT NULL)
    OR
    (status IN ('contextual', 'unresolved') AND polarity IS NULL)
  )
);

CREATE TABLE middle_end (
  utwu_id TEXT PRIMARY KEY,
  lyrics_id TEXT REFERENCES lyrics(lyrics_id),
  spotify_id TEXT,
  spotify_order INTEGER,
  title_original TEXT,
  title_normalized TEXT,
  title_parsed TEXT,
  artist_original TEXT,
  artist_normalized TEXT,
  artist_parsed TEXT,
  album_original TEXT,
  match_status TEXT,
  match_candidates TEXT,
  match_note TEXT,
  lyrics_status TEXT,
  audio_id TEXT REFERENCES audio(audio_id),
  youtube_video_id TEXT,
  audio_match_quality TEXT
);

CREATE TABLE tag_snapshots (
  lyrics_id TEXT REFERENCES lyrics(lyrics_id),
  tagged_at TEXT,
  tags TEXT
);

-- Warstwa audio V1
CREATE TABLE IF NOT EXISTS audio (
    audio_id TEXT PRIMARY KEY,
    source_filename TEXT NOT NULL UNIQUE,
    source_relative_path TEXT,
    youtube_video_id TEXT NOT NULL UNIQUE,
    file_size_mb REAL NOT NULL,
    duration_seconds REAL NOT NULL,
    sample_rate_hz INTEGER NOT NULL,
    channels INTEGER NOT NULL,
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CHECK (length(trim(audio_id)) > 0),
    CHECK (length(trim(source_filename)) > 0),
    CHECK (length(trim(youtube_video_id)) > 0),
    CHECK (file_size_mb > 0),
    CHECK (duration_seconds > 0),
    CHECK (sample_rate_hz > 0),
    CHECK (channels > 0)
);

CREATE TABLE IF NOT EXISTS audio_middle_end (
    audio_id TEXT PRIMARY KEY
        REFERENCES audio(audio_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    utwu_id TEXT
        REFERENCES middle_end(utwu_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    match_status TEXT NOT NULL,
    match_note TEXT,

    CHECK (match_status IN ('matched', 'out', 'uncertain')),
    CHECK (
        (match_status = 'matched' AND utwu_id IS NOT NULL)
        OR
        (match_status IN ('out', 'uncertain'))
    )
);

CREATE TABLE IF NOT EXISTS audio_match_details (
    utwu_id TEXT PRIMARY KEY REFERENCES middle_end(utwu_id),
    audio_id TEXT NOT NULL REFERENCES audio(audio_id),
    variant_type TEXT NOT NULL,
    note TEXT
);

CREATE TABLE IF NOT EXISTS audio_feature_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    audio_id TEXT NOT NULL
        REFERENCES audio(audio_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    analyzer_version TEXT NOT NULL,
    dataset_version TEXT NOT NULL,
    analyzed_at TEXT,

    n_fft INTEGER NOT NULL,
    hop INTEGER NOT NULL,
    liczba_ramek INTEGER NOT NULL,
    rms_left REAL NOT NULL,
    rms_left_dbfs REAL NOT NULL,
    rms_right REAL NOT NULL,
    rms_right_dbfs REAL NOT NULL,
    peak_left REAL NOT NULL,
    peak_left_dbfs REAL NOT NULL,
    peak_right REAL NOT NULL,
    peak_right_dbfs REAL NOT NULL,
    crest_left REAL NOT NULL,
    crest_left_db REAL NOT NULL,
    crest_right REAL NOT NULL,
    crest_right_db REAL NOT NULL,
    over_0dbfs_fraction_left REAL NOT NULL,
    over_0dbfs_fraction_right REAL NOT NULL,
    rms_mid REAL NOT NULL,
    rms_mid_dbfs REAL NOT NULL,
    peak_mid REAL NOT NULL,
    peak_mid_dbfs REAL NOT NULL,
    rms_side REAL NOT NULL,
    rms_side_dbfs REAL NOT NULL,
    stereo_balance_db_L_over_R REAL NOT NULL,
    stereo_correlation_LR REAL NOT NULL,
    stereo_width_side_over_mid REAL NOT NULL,
    stereo_width_db REAL NOT NULL,
    over_0dbfs_fraction_mid REAL NOT NULL,
    frame_rms_mean REAL NOT NULL,
    frame_rms_std REAL NOT NULL,
    frame_rms_p10 REAL NOT NULL,
    frame_rms_p50 REAL NOT NULL,
    frame_rms_p90 REAL NOT NULL,
    frame_zcr_mean REAL NOT NULL,
    frame_zcr_std REAL NOT NULL,
    frame_zcr_p10 REAL NOT NULL,
    frame_zcr_p50 REAL NOT NULL,
    frame_zcr_p90 REAL NOT NULL,
    spectral_centroid_hz_mean REAL NOT NULL,
    spectral_centroid_hz_std REAL NOT NULL,
    spectral_centroid_hz_p10 REAL NOT NULL,
    spectral_centroid_hz_p50 REAL NOT NULL,
    spectral_centroid_hz_p90 REAL NOT NULL,
    spectral_rolloff85_hz_mean REAL NOT NULL,
    spectral_rolloff85_hz_std REAL NOT NULL,
    spectral_rolloff85_hz_p10 REAL NOT NULL,
    spectral_rolloff85_hz_p50 REAL NOT NULL,
    spectral_rolloff85_hz_p90 REAL NOT NULL,
    spectral_bandwidth_hz_mean REAL NOT NULL,
    spectral_bandwidth_hz_std REAL NOT NULL,
    spectral_bandwidth_hz_p10 REAL NOT NULL,
    spectral_bandwidth_hz_p50 REAL NOT NULL,
    spectral_bandwidth_hz_p90 REAL NOT NULL,
    spectral_flatness_mean REAL NOT NULL,
    spectral_flatness_std REAL NOT NULL,
    spectral_flatness_p10 REAL NOT NULL,
    spectral_flatness_p50 REAL NOT NULL,
    spectral_flatness_p90 REAL NOT NULL,
    spectral_flux_mean REAL NOT NULL,
    spectral_flux_std REAL NOT NULL,
    spectral_flux_p10 REAL NOT NULL,
    spectral_flux_p50 REAL NOT NULL,
    spectral_flux_p90 REAL NOT NULL,
    spectral_slope_db_per_khz_mean REAL NOT NULL,
    spectral_slope_db_per_khz_std REAL NOT NULL,
    spectral_slope_db_per_khz_p10 REAL NOT NULL,
    spectral_slope_db_per_khz_p50 REAL NOT NULL,
    spectral_slope_db_per_khz_p90 REAL NOT NULL,
    spectral_variability_mean REAL NOT NULL,
    spectral_edge_99_hz REAL NOT NULL,
    spectral_edge_999_hz REAL NOT NULL,
    spectral_cutoff_m60db_hz REAL NOT NULL,
    band_20_60_fraction REAL NOT NULL,
    band_60_120_fraction REAL NOT NULL,
    band_120_250_fraction REAL NOT NULL,
    band_250_500_fraction REAL NOT NULL,
    band_500_1000_fraction REAL NOT NULL,
    band_1000_2000_fraction REAL NOT NULL,
    band_2000_4000_fraction REAL NOT NULL,
    band_4000_8000_fraction REAL NOT NULL,
    band_8000_12000_fraction REAL NOT NULL,
    band_12000_20000_fraction REAL NOT NULL,
    spectral_contrast_50_100_mean_db REAL NOT NULL,
    spectral_contrast_50_100_std_db REAL NOT NULL,
    spectral_contrast_100_200_mean_db REAL NOT NULL,
    spectral_contrast_100_200_std_db REAL NOT NULL,
    spectral_contrast_200_400_mean_db REAL NOT NULL,
    spectral_contrast_200_400_std_db REAL NOT NULL,
    spectral_contrast_400_800_mean_db REAL NOT NULL,
    spectral_contrast_400_800_std_db REAL NOT NULL,
    spectral_contrast_800_1600_mean_db REAL NOT NULL,
    spectral_contrast_800_1600_std_db REAL NOT NULL,
    spectral_contrast_1600_3200_mean_db REAL NOT NULL,
    spectral_contrast_1600_3200_std_db REAL NOT NULL,
    spectral_contrast_3200_6400_mean_db REAL NOT NULL,
    spectral_contrast_3200_6400_std_db REAL NOT NULL,
    spectral_contrast_6400_12800_mean_db REAL NOT NULL,
    spectral_contrast_6400_12800_std_db REAL NOT NULL,
    mfcc_01_mean REAL NOT NULL,
    mfcc_01_std REAL NOT NULL,
    mfcc_02_mean REAL NOT NULL,
    mfcc_02_std REAL NOT NULL,
    mfcc_03_mean REAL NOT NULL,
    mfcc_03_std REAL NOT NULL,
    mfcc_04_mean REAL NOT NULL,
    mfcc_04_std REAL NOT NULL,
    mfcc_05_mean REAL NOT NULL,
    mfcc_05_std REAL NOT NULL,
    mfcc_06_mean REAL NOT NULL,
    mfcc_06_std REAL NOT NULL,
    mfcc_07_mean REAL NOT NULL,
    mfcc_07_std REAL NOT NULL,
    mfcc_08_mean REAL NOT NULL,
    mfcc_08_std REAL NOT NULL,
    mfcc_09_mean REAL NOT NULL,
    mfcc_09_std REAL NOT NULL,
    mfcc_10_mean REAL NOT NULL,
    mfcc_10_std REAL NOT NULL,
    mfcc_11_mean REAL NOT NULL,
    mfcc_11_std REAL NOT NULL,
    mfcc_12_mean REAL NOT NULL,
    mfcc_12_std REAL NOT NULL,
    mfcc_13_mean REAL NOT NULL,
    mfcc_13_std REAL NOT NULL,
    chroma_C_mean REAL NOT NULL,
    chroma_C_std REAL NOT NULL,
    chroma_Cs_mean REAL NOT NULL,
    chroma_Cs_std REAL NOT NULL,
    chroma_D_mean REAL NOT NULL,
    chroma_D_std REAL NOT NULL,
    chroma_Ds_mean REAL NOT NULL,
    chroma_Ds_std REAL NOT NULL,
    chroma_E_mean REAL NOT NULL,
    chroma_E_std REAL NOT NULL,
    chroma_F_mean REAL NOT NULL,
    chroma_F_std REAL NOT NULL,
    chroma_Fs_mean REAL NOT NULL,
    chroma_Fs_std REAL NOT NULL,
    chroma_G_mean REAL NOT NULL,
    chroma_G_std REAL NOT NULL,
    chroma_Gs_mean REAL NOT NULL,
    chroma_Gs_std REAL NOT NULL,
    chroma_A_mean REAL NOT NULL,
    chroma_A_std REAL NOT NULL,
    chroma_As_mean REAL NOT NULL,
    chroma_As_std REAL NOT NULL,
    chroma_B_mean REAL NOT NULL,
    chroma_B_std REAL NOT NULL,
    chroma_tuning_cents REAL NOT NULL,
    chroma_tuning_confidence REAL NOT NULL,
    chroma_entropy_mean REAL NOT NULL,
    chroma_entropy_std REAL NOT NULL,
    chroma_peak_contrast_mean REAL NOT NULL,
    chroma_peak_contrast_std REAL NOT NULL,
    chroma_active_frames_fraction REAL NOT NULL,
    chroma_dominant_pc_index INTEGER NOT NULL,
    chroma_dominant_pc_name TEXT NOT NULL,
    chroma_dominant_strength REAL NOT NULL,
    chroma_key_root_index INTEGER NOT NULL,
    chroma_key_mode TEXT NOT NULL,
    chroma_key_name TEXT NOT NULL,
    chroma_key_score REAL NOT NULL,
    chroma_key_second_score REAL NOT NULL,
    chroma_key_margin REAL NOT NULL,
    chroma_key_confidence REAL NOT NULL,
    chroma_frame_count INTEGER NOT NULL,
    chroma_n_fft INTEGER NOT NULL,
    chroma_hop INTEGER NOT NULL,
    onset_strength_mean REAL NOT NULL,
    onset_strength_std REAL NOT NULL,
    onset_strength_p90 REAL NOT NULL,
    onset_count INTEGER NOT NULL,
    onset_rate_per_s REAL NOT NULL,
    onset_interval_mean_s REAL NOT NULL,
    onset_interval_std_s REAL NOT NULL,
    onset_interval_cv REAL NOT NULL,
    bpm_estimate REAL NOT NULL,
    bpm_confidence REAL NOT NULL,
    bpm_candidate_2 REAL NOT NULL,
    bpm_candidate_3 REAL NOT NULL,
    bpm_interval_estimate REAL NOT NULL,
    bpm_interval_confidence REAL NOT NULL,
    bpm_period_s REAL NOT NULL,
    bpm_rhythm_window INTEGER NOT NULL,
    bpm_rhythm_hop INTEGER NOT NULL,

    UNIQUE (audio_id, analyzer_version, dataset_version)
);

CREATE INDEX IF NOT EXISTS idx_audio_middle_end_utwu_id
    ON audio_middle_end(utwu_id);

CREATE INDEX IF NOT EXISTS idx_audio_feature_snapshots_audio_id
    ON audio_feature_snapshots(audio_id);


-- Playlist layer
CREATE TABLE IF NOT EXISTS playlist (
    playlist_id TEXT PRIMARY KEY,
    service TEXT NOT NULL,
    name TEXT NOT NULL,
    external_playlist_id TEXT,
    external_url TEXT,
    source_file TEXT,
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (service IN ('spotify', 'youtube_music', 'youtube')),
    UNIQUE (service, external_playlist_id)
);

CREATE TABLE IF NOT EXISTS playlist_item (
    playlist_id TEXT NOT NULL
        REFERENCES playlist(playlist_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    position INTEGER NOT NULL,
    utwu_id TEXT
        REFERENCES middle_end(utwu_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    external_track_id TEXT,
    source_name TEXT,
    source_artist TEXT,
    source_album TEXT,
    PRIMARY KEY (playlist_id, position),
    CHECK (position > 0)
);

CREATE INDEX IF NOT EXISTS idx_playlist_item_utwu_id
    ON playlist_item(utwu_id);

CREATE INDEX IF NOT EXISTS idx_playlist_item_external_track_id
    ON playlist_item(external_track_id);

COMMIT;
