const fs = require('fs');
const { createClient } = require('@libsql/client');

function stop(msg) {
  throw new Error('STOP AUDHD CONTENT: ' + msg);
}

function parseTsv(path) {
  const lines = fs.readFileSync(path, 'utf8').replace(/^\uFEFF/, '').trimEnd().split(/\r?\n/);
  const headers = lines[0].split('\t');
  return lines.slice(1).map(line => {
    const vals = line.split('\t');
    return Object.fromEntries(headers.map((h, i) => [h, vals[i] ?? '']));
  });
}

function extractHeadingBodies(html, file) {
  const bodyMatch = html.match(/<body\b[^>]*>([\s\S]*?)<\/body\s*>/i);
  if (!bodyMatch) stop(`${file}: brak <body>`);
  const body = bodyMatch[1];

  const re = /<(h[1-6])\b([^>]*\bid=(['"])([^'"]+)\3[^>]*)>[\s\S]*?<\/\1\s*>/gi;
  const heads = [];
  let m;
  while ((m = re.exec(body)) !== null) {
    heads.push({
      tag: m[1].toUpperCase(),
      anchor: m[4],
      start: m.index,
      end: re.lastIndex,
    });
  }

  const out = new Map();
  for (let i = 0; i < heads.length; i++) {
    const h = heads[i];
    if (out.has(h.anchor)) stop(`${file}: zduplikowany anchor ${h.anchor}`);
    const nextStart = i + 1 < heads.length ? heads[i + 1].start : body.length;
    out.set(h.anchor, {
      tag: h.tag,
      html: body.slice(h.end, nextStart).trim(),
    });
  }
  return { heads, out };
}

async function main() {
  const creds = fs.readFileSync('daneDoSql.txt', 'utf8');
  const urlMatch = creds.match(/libsql:\/\/[^\s]+/);
  const tokenMatch = creds.match(/eyJ[a-zA-Z0-9._-]+/);
  if (!urlMatch || !tokenMatch) stop('brak URL lub tokena w daneDoSql.txt');

  const mapRows = parseTsv('audhd/SOL_mapa-sekcji-i-anchorow-audhd.tsv');
  if (mapRows.length !== 338) stop(`mapa: oczekiwano 338 rekordow, jest ${mapRows.length}`);

  const byFile = new Map();
  for (const r of mapRows) {
    if (!byFile.has(r.dokument_plik)) byFile.set(r.dokument_plik, []);
    byFile.get(r.dokument_plik).push(r);
  }
  if (byFile.size !== 18) stop(`mapa: oczekiwano 18 dokumentow, jest ${byFile.size}`);

  const fragments = new Map();
  let totalFragmentChars = 0;

  for (const [file, rows] of byFile) {
    const path = `audhd/${file}`;
    if (!fs.existsSync(path)) stop(`brak pliku ${path}`);
    const html = fs.readFileSync(path, 'utf8');
    const parsed = extractHeadingBodies(html, file);

    if (parsed.heads.length !== rows.length) {
      stop(`${file}: HTML ma ${parsed.heads.length} naglowkow, mapa ma ${rows.length}`);
    }

    const htmlAnchors = parsed.heads.map(h => h.anchor);
    const mapAnchors = rows.map(r => r.anchor);
    for (let i = 0; i < mapAnchors.length; i++) {
      if (htmlAnchors[i] !== mapAnchors[i]) {
        stop(`${file}: kolejnosc anchorow rozna przy ${mapAnchors[i]} / ${htmlAnchors[i]}`);
      }
    }

    for (const r of rows) {
      const f = parsed.out.get(r.anchor);
      if (!f) stop(`${file}: brak anchor ${r.anchor}`);
      if (f.tag !== r.poziom) stop(`${file}#${r.anchor}: HTML=${f.tag}, mapa=${r.poziom}`);
      const key = `${r.dokument_kod}\t${r.anchor}`;
      if (fragments.has(key)) stop(`duplikat klucza ${key}`);
      fragments.set(key, f.html);
      totalFragmentChars += f.html.length;
    }
  }

  if (fragments.size !== 338) stop(`fragmenty: oczekiwano 338, jest ${fragments.size}`);

  const client = createClient({ url: urlMatch[0], authToken: tokenMatch[0] });

  const pragma = await client.execute('PRAGMA table_info(content_sections)');
  const columns = new Set(pragma.rows.map(r => String(r.name)));
  if (!columns.has('content_html')) {
    await client.execute('ALTER TABLE content_sections ADD COLUMN content_html TEXT');
  }

  const sqlRows = await client.execute({
    sql: `SELECT s.section_id, d.document_code, s.anchor
          FROM content_sections s
          JOIN content_documents d ON d.document_id=s.document_id
          WHERE d.collection_id='audhd' AND s.section_kind='heading'
          ORDER BY d.document_order, s.section_order`,
    args: []
  });

  if (sqlRows.rows.length !== 338) stop(`SQL: oczekiwano 338 heading, jest ${sqlRows.rows.length}`);

  const statements = [];
  for (const r of sqlRows.rows) {
    const key = `${String(r.document_code)}\t${String(r.anchor)}`;
    if (!fragments.has(key)) stop(`SQL bez fragmentu: ${key}`);
    statements.push({
      sql: 'UPDATE content_sections SET content_html=? WHERE section_id=?',
      args: [fragments.get(key), Number(r.section_id)]
    });
  }

  for (let i = 0; i < statements.length; i += 50) {
    await client.batch(statements.slice(i, i + 50), 'write');
  }

  const check = await client.execute({
    sql: `SELECT
            count(*) AS headings,
            sum(CASE WHEN s.content_html IS NOT NULL THEN 1 ELSE 0 END) AS with_content,
            sum(length(COALESCE(s.content_html,''))) AS chars
          FROM content_sections s
          JOIN content_documents d ON d.document_id=s.document_id
          WHERE d.collection_id='audhd' AND s.section_kind='heading'`,
    args: []
  });

  const c = check.rows[0];
  if (Number(c.headings) !== 338 || Number(c.with_content) !== 338) {
    stop(`walidacja SQL: headings=${c.headings}, with_content=${c.with_content}`);
  }

  console.log(`OK AUDHD CONTENT: dokumenty=18; sekcje=338; content_html=338; chars=${c.chars}; source_fragment_chars=${totalFragmentChars}`);
}

main().catch(err => {
  console.error(err.message);
  process.exit(1);
});
