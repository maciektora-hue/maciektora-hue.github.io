const fs = require('fs');
const crypto = require('crypto');
const { createClient } = require('@libsql/client');

function stop(msg) {
  throw new Error('STOP AUDHD OPISY IMPORT: ' + msg);
}

function hashRows(rows) {
  const normalized = rows.map(r => {
    const o = {};
    for (const k of Object.keys(r).sort()) o[k] = r[k] === null ? null : String(r[k]);
    return o;
  });
  normalized.sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
  return crypto.createHash('sha256').update(JSON.stringify(normalized), 'utf8').digest('hex');
}

async function main() {
  const inputPath = process.argv[2];
  if (!inputPath) stop('brak sciezki do JSON z opisami');
  const input = JSON.parse(fs.readFileSync(inputPath, 'utf8'));

  if (!Array.isArray(input) || input.length !== 338) stop(`plik opisow ma ${Array.isArray(input) ? input.length : 'nie-tablice'} zamiast 338`);
  const inputKeys = input.map(r => `${String(r.dokument_kod || '').trim()}\t${String(r.anchor || '').trim()}`);
  if (new Set(inputKeys).size !== 338) stop('plik opisow ma duplikaty dokument_kod+anchor');
  if (new Set(input.map(r => String(r.dokument_kod || '').trim())).size !== 18) stop('plik opisow nie ma 18 dokumentow');
  if (input.some(r => !String(r.dokument_kod || '').trim() || !String(r.anchor || '').trim() || !String(r.description || '').trim())) stop('plik opisow ma puste pole');

  const byKey = new Map(input.map(r => [`${String(r.dokument_kod).trim()}\t${String(r.anchor).trim()}`, String(r.description).trim()]));

  const creds = fs.readFileSync('daneDoSql.txt', 'utf8');
  const urlMatch = creds.match(/libsql:\/\/[^\s]+/);
  const tokenMatch = creds.match(/eyJ[a-zA-Z0-9._-]+/);
  if (!urlMatch || !tokenMatch) stop('brak URL lub tokena');
  const client = createClient({ url: urlMatch[0], authToken: tokenMatch[0] });

  const pragma = await client.execute('PRAGMA table_info(content_sections)');
  const columns = new Set(pragma.rows.map(r => String(r.name)));
  for (const c of ['section_id','document_id','section_kind','section_title','anchor','description','content_html','section_title_en','description_en','keywords_pl','keywords_en']) {
    if (!columns.has(c)) stop(`brak kolumny ${c}`);
  }

  const audhdBeforeQ = await client.execute(`
    SELECT s.section_id, d.document_code, s.anchor, s.section_title, s.description,
           s.content_html, s.section_title_en, s.description_en, s.keywords_pl, s.keywords_en
    FROM content_sections s
    JOIN content_documents d ON d.document_id=s.document_id
    WHERE d.collection_id='audhd' AND s.section_kind='heading'
    ORDER BY d.document_code, s.section_order
  `);
  const audhdBefore = audhdBeforeQ.rows;
  if (audhdBefore.length !== 338) stop(`SQL AuDHD ma ${audhdBefore.length} heading zamiast 338`);
  const sqlKeys = audhdBefore.map(r => `${String(r.document_code).trim()}\t${String(r.anchor).trim()}`);
  if (new Set(sqlKeys).size !== 338) stop('SQL AuDHD ma duplikaty document_code+anchor');
  if (sqlKeys.some(k => !byKey.has(k))) stop('SQL AuDHD zawiera klucz bez opisu');
  if (inputKeys.some(k => !new Set(sqlKeys).has(k))) stop('plik opisow zawiera klucz bez sekcji SQL');
  if (audhdBefore.some(r => r.description !== null && String(r.description).trim() !== '')) stop('AuDHD ma juz niepusty description');
  if (audhdBefore.some(r => r.section_title_en !== null || r.description_en !== null || r.keywords_pl !== null || r.keywords_en !== null)) stop('nowe pola EN/keywords AuDHD nie sa puste przed importem');

  const immutableBefore = hashRows(audhdBefore.map(r => ({
    section_id:r.section_id, document_code:r.document_code, anchor:r.anchor,
    section_title:r.section_title, content_html:r.content_html,
    section_title_en:r.section_title_en, description_en:r.description_en,
    keywords_pl:r.keywords_pl, keywords_en:r.keywords_en
  })));

  const rosjaBeforeQ = await client.execute(`
    SELECT s.section_id, s.document_id, s.parent_section_id, s.section_kind,
           s.heading_level, s.depth, s.section_order, s.structure_order,
           s.section_title, s.anchor, s.description, s.content_html,
           s.section_title_en, s.description_en, s.keywords_pl, s.keywords_en
    FROM content_sections s
    JOIN content_documents d ON d.document_id=s.document_id
    WHERE d.collection_id='rosja'
    ORDER BY s.section_id
  `);
  if (rosjaBeforeQ.rows.length !== 629) stop(`ROSJA ma ${rosjaBeforeQ.rows.length} rekordow zamiast 629`);
  const rosjaBeforeHash = hashRows(rosjaBeforeQ.rows);

  const tx = await client.transaction('write');
  let committed = false;
  try {
    for (const r of audhdBefore) {
      const key = `${String(r.document_code).trim()}\t${String(r.anchor).trim()}`;
      const result = await tx.execute({
        sql: `UPDATE content_sections
              SET description=?
              WHERE section_id=? AND (description IS NULL OR trim(description)='')`,
        args: [byKey.get(key), Number(r.section_id)]
      });
      if (Number(result.rowsAffected) !== 1) stop(`UPDATE section_id=${r.section_id} rowsAffected=${result.rowsAffected}`);
    }

    const verifyQ = await tx.execute(`
      SELECT s.section_id, d.document_code, s.anchor, s.section_title, s.description,
             s.content_html, s.section_title_en, s.description_en, s.keywords_pl, s.keywords_en
      FROM content_sections s
      JOIN content_documents d ON d.document_id=s.document_id
      WHERE d.collection_id='audhd' AND s.section_kind='heading'
      ORDER BY d.document_code, s.section_order
    `);
    if (verifyQ.rows.length !== 338) stop(`po UPDATE AuDHD ma ${verifyQ.rows.length} heading`);
    for (const r of verifyQ.rows) {
      const key = `${String(r.document_code).trim()}\t${String(r.anchor).trim()}`;
      if (String(r.description || '') !== byKey.get(key)) stop(`opis po UPDATE niezgodny: ${key}`);
    }
    if (verifyQ.rows.some(r => r.section_title_en !== null || r.description_en !== null || r.keywords_pl !== null || r.keywords_en !== null)) stop('nowe pola EN/keywords zostaly naruszone');

    const immutableAfter = hashRows(verifyQ.rows.map(r => ({
      section_id:r.section_id, document_code:r.document_code, anchor:r.anchor,
      section_title:r.section_title, content_html:r.content_html,
      section_title_en:r.section_title_en, description_en:r.description_en,
      keywords_pl:r.keywords_pl, keywords_en:r.keywords_en
    })));
    if (immutableAfter !== immutableBefore) stop('zmienily sie istniejace dane AuDHD poza description');

    const rosjaAfterQ = await tx.execute(`
      SELECT s.section_id, s.document_id, s.parent_section_id, s.section_kind,
             s.heading_level, s.depth, s.section_order, s.structure_order,
             s.section_title, s.anchor, s.description, s.content_html,
             s.section_title_en, s.description_en, s.keywords_pl, s.keywords_en
      FROM content_sections s
      JOIN content_documents d ON d.document_id=s.document_id
      WHERE d.collection_id='rosja'
      ORDER BY s.section_id
    `);
    if (hashRows(rosjaAfterQ.rows) !== rosjaBeforeHash) stop('zmienily sie dane ROSJA');

    await tx.commit();
    committed = true;
  } finally {
    if (!committed) {
      try { await tx.rollback(); } catch (_) {}
    }
  }

  const finalQ = await client.execute(`
    SELECT count(*) AS headings,
           sum(CASE WHEN s.description IS NOT NULL AND trim(s.description)<>'' THEN 1 ELSE 0 END) AS descriptions,
           sum(CASE WHEN s.section_title_en IS NOT NULL THEN 1 ELSE 0 END) AS title_en,
           sum(CASE WHEN s.description_en IS NOT NULL THEN 1 ELSE 0 END) AS description_en,
           sum(CASE WHEN s.keywords_pl IS NOT NULL THEN 1 ELSE 0 END) AS keywords_pl,
           sum(CASE WHEN s.keywords_en IS NOT NULL THEN 1 ELSE 0 END) AS keywords_en
    FROM content_sections s
    JOIN content_documents d ON d.document_id=s.document_id
    WHERE d.collection_id='audhd' AND s.section_kind='heading'
  `);
  const f = finalQ.rows[0];
  if (Number(f.headings) !== 338 || Number(f.descriptions) !== 338) stop(`final: headings=${f.headings}, descriptions=${f.descriptions}`);
  if (Number(f.title_en) || Number(f.description_en) || Number(f.keywords_pl) || Number(f.keywords_en)) stop('final: nowe pola EN/keywords nie sa NULL');

  console.log(`OK AUDHD OPISY IMPORT: description=338/338; dokumenty=18; tylko description zmienione; EN/keywords nadal NULL; ROSJA 629 rekordow bez zmian; transakcja COMMIT.`);
}

main().catch(err => {
  console.error(err.message);
  process.exit(1);
});
