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
  lyrics_status TEXT
);

CREATE TABLE tag_snapshots (
  lyrics_id TEXT REFERENCES lyrics(lyrics_id),
  tagged_at TEXT,
  tags TEXT
);

COMMIT;
