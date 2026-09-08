const fs = require('fs');
const crypto = require('crypto');
const { createClient } = require('@libsql/client');

const EXPECTED_HASH = 'aa036cf1acce4d57386c1c03e0b7e2f491d1c3b5dbd7275928f7a511b4bd346e';

function stop(msg) {
  throw new Error('STOP AUDHD OPISY PREFLIGHT: ' + msg);
}

function parseSimpleTsv(path) {
  const lines = fs.readFileSync(path, 'utf8').replace(/^\uFEFF/, '').trimEnd().split(/\r?\n/);
  const headers = lines[0].split('\t');
  return lines.slice(1).map(line => {
    const vals = line.split('\t');
    return Object.fromEntries(headers.map((h, i) => [h, vals[i] ?? '']));
  });
}

function keyHash(keys) {
  const text = [...keys].sort().join('\n') + '\n';
  return crypto.createHash('sha256').update(text, 'utf8').digest('hex');
}

async function main() {
  const mapRows = parseSimpleTsv('audhd/SOL_mapa-sekcji-i-anchorow-audhd.tsv');
  if (mapRows.length !== 338) stop(`mapa ma ${mapRows.length} wierszy zamiast 338`);

  const mapKeys = mapRows.map(r => `${String(r.dokument_kod).trim()}\t${String(r.anchor).trim()}`);
  if (new Set(mapKeys).size !== 338) stop('mapa ma duplikaty dokument_kod+anchor');
  if (new Set(mapRows.map(r => String(r.dokument_kod).trim())).size !== 18) stop('mapa nie ma 18 dokumentow');
  if (mapKeys.some(k => k.startsWith('\t') || k.endsWith('\t'))) stop('mapa ma pusty dokument_kod lub anchor');

  const mapHash = keyHash(mapKeys);
  if (mapHash !== EXPECTED_HASH) stop(`hash kluczy mapy ${mapHash} != hash pliku opisow ${EXPECTED_HASH}`);

  const creds = fs.readFileSync('daneDoSql.txt', 'utf8');
  const urlMatch = creds.match(/libsql:\/\/[^\s]+/);
  const tokenMatch = creds.match(/eyJ[a-zA-Z0-9._-]+/);
  if (!urlMatch || !tokenMatch) stop('brak URL lub tokena');

  const client = createClient({ url: urlMatch[0], authToken: tokenMatch[0] });

  const pragma = await client.execute('PRAGMA table_info(content_sections)');
  const columns = new Set(pragma.rows.map(r => String(r.name)));
  for (const c of ['description','section_title_en','description_en','keywords_pl','keywords_en']) {
    if (!columns.has(c)) stop(`brak kolumny ${c}`);
  }

  const q = await client.execute({
    sql: `SELECT d.document_code, s.anchor, s.description
          FROM content_sections s
          JOIN content_documents d ON d.document_id=s.document_id
          WHERE d.collection_id='audhd' AND s.section_kind='heading'`,
    args: []
  });

  if (q.rows.length !== 338) stop(`SQL AuDHD ma ${q.rows.length} heading zamiast 338`);
  const sqlKeys = q.rows.map(r => `${String(r.document_code).trim()}\t${String(r.anchor).trim()}`);
  if (new Set(sqlKeys).size !== 338) stop('SQL AuDHD ma duplikaty document_code+anchor');
  if (new Set(q.rows.map(r => String(r.document_code).trim())).size !== 18) stop('SQL AuDHD nie ma 18 dokumentow');
  if (sqlKeys.some(k => k.startsWith('\t') || k.endsWith('\t'))) stop('SQL AuDHD ma pusty document_code lub anchor');

  const sqlHash = keyHash(sqlKeys);
  if (sqlHash !== EXPECTED_HASH) stop(`hash kluczy SQL ${sqlHash} != hash pliku opisow ${EXPECTED_HASH}`);

  const existingDescriptions = q.rows.filter(r => r.description !== null && String(r.description).trim() !== '').length;
  if (existingDescriptions !== 0) stop(`AuDHD ma juz ${existingDescriptions} niepustych description`);

  const metadata = await client.execute(`
    SELECT
      sum(CASE WHEN section_title_en IS NOT NULL THEN 1 ELSE 0 END) AS title_en,
      sum(CASE WHEN description_en IS NOT NULL THEN 1 ELSE 0 END) AS description_en,
      sum(CASE WHEN keywords_pl IS NOT NULL THEN 1 ELSE 0 END) AS keywords_pl,
      sum(CASE WHEN keywords_en IS NOT NULL THEN 1 ELSE 0 END) AS keywords_en
    FROM content_sections s
    JOIN content_documents d ON d.document_id=s.document_id
    WHERE d.collection_id='audhd' AND s.section_kind='heading'
  `);
  const m = metadata.rows[0];
  if (Number(m.title_en) || Number(m.description_en) || Number(m.keywords_pl) || Number(m.keywords_en)) {
    stop(`nowe pola AuDHD nie sa puste: title_en=${m.title_en}, description_en=${m.description_en}, keywords_pl=${m.keywords_pl}, keywords_en=${m.keywords_en}`);
  }

  const rosja = await client.execute(`
    SELECT
      sum(CASE WHEN s.section_kind='heading' THEN 1 ELSE 0 END) AS headings,
      sum(CASE WHEN s.section_kind='volume' THEN 1 ELSE 0 END) AS volumes,
      sum(CASE WHEN s.section_kind='heading' AND s.description IS NOT NULL AND trim(s.description)<>'' THEN 1 ELSE 0 END) AS descriptions
    FROM content_sections s
    JOIN content_documents d ON d.document_id=s.document_id
    WHERE d.collection_id='rosja'
  `);
  const r = rosja.rows[0];
  if (Number(r.headings) !== 620 || Number(r.volumes) !== 9 || Number(r.descriptions) !== 620) {
    stop(`ROSJA niezgodna: H=${r.headings}, TOM=${r.volumes}, opisy=${r.descriptions}`);
  }

  console.log(`OK AUDHD OPISY PREFLIGHT: plik=338/18/338 unikalnych; mapa_hash=${mapHash}; SQL=338/18/338 unikalnych; SQL_hash=${sqlHash}; description AuDHD=0/338; nowe metadata AuDHD=NULL; ROSJA H=620, TOM=9, opisy=620; ZERO SQL WRITE.`);
}

main().catch(err => {
  console.error(err.message);
  process.exit(1);
});
