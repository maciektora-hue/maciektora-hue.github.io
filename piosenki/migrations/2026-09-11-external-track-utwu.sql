-- SOL — external_track_utwu, krok 2 normalizacji playlist
-- Jawne, rozstrzygnięte połączenia zewnętrznego utworu z naszym middle_end.
-- Brak rekordu = brak rozstrzygniętego mapowania. Kilka rekordów jest dozwolone.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS external_track_utwu (
    external_track_pk INTEGER NOT NULL
        REFERENCES external_track(external_track_pk)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    utwu_id TEXT NOT NULL
        REFERENCES middle_end(utwu_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    PRIMARY KEY (external_track_pk, utwu_id)
);

CREATE INDEX IF NOT EXISTS idx_external_track_utwu_utwu_id
    ON external_track_utwu(utwu_id);

COMMIT;
