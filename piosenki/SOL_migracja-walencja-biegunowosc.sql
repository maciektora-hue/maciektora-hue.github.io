-- SOL — migracja walencji i biegunowości tagów
-- Tworzy dwie osobne tabele i zasila bieżącą, rozstrzygniętą walencję.
-- Nie zmienia tag_catalog ani tag_axis.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS tag_valence (
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

INSERT INTO tag_valence (tag, valence, status) VALUES
  ('samotnosc-preferowana', 1, 'resolved'),
  ('ulga', 1, 'resolved'),
  ('spokoj', 1, 'resolved'),
  ('ulga-z-zewnatrz', 1, 'resolved'),
  ('wystarczy', 1, 'resolved'),
  ('euforia-naped', 1, 'resolved'),
  ('radosc', 1, 'resolved'),
  ('nadzieja', 1, 'resolved'),
  ('czulosc', 1, 'resolved'),
  ('duma', 1, 'resolved'),
  ('zobojetnienie', 0, 'resolved'),
  ('pustka-emocjonalna', 0, 'resolved'),
  ('sensoryka-przytloczenie', -1, 'resolved'),
  ('niedopasowanie-spoleczne', -1, 'resolved'),
  ('komunikacja-problem', -1, 'resolved'),
  ('alexithymia', -1, 'resolved'),
  ('shutdown-meltdown', -1, 'resolved'),
  ('racing-thoughts', -1, 'resolved'),
  ('time-blindness', -1, 'resolved'),
  ('dysfunkcja-wykonawcza', -1, 'resolved'),
  ('bezsennosc-restless', -1, 'resolved'),
  ('emocjonalna-dysregulacja', -1, 'resolved'),
  ('nuda-nietolerancja', -1, 'resolved'),
  ('intensywnosc-potem-crash', -1, 'resolved'),
  ('zapominanie-gubienie', -1, 'resolved'),
  ('chaos-balagan', -1, 'resolved'),
  ('sprzeczne-potrzeby', -1, 'resolved'),
  ('wyczerpanie-maska', -1, 'resolved'),
  ('za-duzo-i-za-malo', -1, 'resolved'),
  ('podwojna-samotnosc', -1, 'resolved'),
  ('samotnosc', -1, 'resolved'),
  ('gniew', -1, 'resolved'),
  ('tesknota', -1, 'resolved'),
  ('ulga-odroczona', -1, 'resolved'),
  ('ulga-utracona', -1, 'resolved'),
  ('cel-nieosiagniety', -1, 'resolved'),
  ('nigdy-dosc', -1, 'resolved'),
  ('dosc-przesyt', -1, 'resolved'),
  ('zaraz-minie', -1, 'resolved'),
  ('utrata', -1, 'resolved'),
  ('bezsilnosc', -1, 'resolved'),
  ('anhedonia', -1, 'resolved'),
  ('brak-nadziei', -1, 'resolved'),
  ('bezwartosciowosc', -1, 'resolved'),
  ('wina', -1, 'resolved'),
  ('brak-napedu', -1, 'resolved'),
  ('wyczerpanie', -1, 'resolved'),
  ('spowolnienie', -1, 'resolved'),
  ('bezsennosc', -1, 'resolved'),
  ('nadmierny-sen', -1, 'resolved'),
  ('zamartwianie', -1, 'resolved'),
  ('lek-antycypacyjny', -1, 'resolved'),
  ('katastrofizacja', -1, 'resolved'),
  ('hiperczujnosc', -1, 'resolved'),
  ('niepewnosc-nie-do-zniesienia', -1, 'resolved'),
  ('napiecie-ciala', -1, 'resolved'),
  ('niemoznosc-odpuszczenia', -1, 'resolved'),
  ('unikanie-z-leku', -1, 'resolved'),
  ('zamrozenie', -1, 'resolved'),
  ('przeciazenie-przyszloscia', -1, 'resolved'),
  ('maskowanie-koszt', -1, 'resolved'),
  ('rozpad-po-masce', -1, 'resolved'),
  ('nierozpoznanie-siebie', -1, 'resolved'),
  ('zablokowanie', -1, 'resolved'),
  ('rozpad', -1, 'resolved'),
  ('smutek', -1, 'resolved'),
  ('melancholia', -1, 'resolved'),
  ('lek', -1, 'resolved'),
  ('strach', -1, 'resolved'),
  ('wstyd', -1, 'resolved'),
  ('wstret', -1, 'resolved'),
  ('zazdrosc', -1, 'resolved'),
  ('rozpacz', -1, 'resolved'),
  ('frustracja', -1, 'resolved'),
  ('nuda', -1, 'resolved'),
  ('zal', -1, 'resolved')
ON CONFLICT(tag) DO UPDATE SET
  valence = excluded.valence,
  status = excluded.status;

COMMIT;
