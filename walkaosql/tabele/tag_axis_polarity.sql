-- tabela: tag_axis_polarity
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS tag_axis_polarity (
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

