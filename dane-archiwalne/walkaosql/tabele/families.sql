-- tabela: families
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS families (
  family_name TEXT PRIMARY KEY,
  label TEXT NOT NULL,
  color_hex TEXT NOT NULL,
  description TEXT NOT NULL,
  sort_order INTEGER NOT NULL UNIQUE
);

INSERT INTO families VALUES('lapis','LAPIS','#26619C','świat / doświadczenie',1);

INSERT INTO families VALUES('butelkowa-zielen','BUTELKOWA ZIELEŃ','#1F5A46','regulacja / energia',2);

INSERT INTO families VALUES('sliwka','ŚLIWKA','#704264','relacja / pozycja wobec świata',3);

INSERT INTO families VALUES('ochra','OCHRA / STARE ZŁOTO','#B18736','poznanie / działanie',4);

INSERT INTO families VALUES('terakota','TERAKOTA','#A85D4D','emocje / cierpienie',5);

