from pathlib import Path
import subprocess

FILES = [
    'audhd/63-cechy-rdzen-czy-maskowanie-01_01-2026-08-26.html',
    'audhd/CLAUDE_co-dziala-po-poznej-diagnozie-02_01-2026-08-26.html',
    'audhd/CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html',
    'audhd/CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html',
    'audhd/ESEJ_architektury-pamieci-1_02-2026-04-28.html',
    'audhd/POWIESC_architektury-pamieci-2_00-2026-04-29.html',
    'audhd/adhd-pomaganie-kosztem-siebie-v01.00-2026-05-14.html',
    'audhd/apendyks1-po-ludzku-02_01-2026-08-26.html',
    'audhd/audhd-fundatorzy-it-1_00-2026-04-27.html',
    'audhd/audhd-po-ludzku-v02_02-2026-07-09.html',
    'audhd/audhd_opracowanie_v6_0_2026-07-01-2.html',
    'audhd/autyzm-regulacja-mowienia-v01.00-2026-05-14.html',
    'audhd/co-to-znaczy-audhd-v03_01-2026-07-09-2.html',
    'audhd/dluga-lista-publikacji-4.01-2026-08-26.html',
    'audhd/ilu-nas-jest-audhd-polska-wstep-v03_00-2026-08-10.html',
    'audhd/kognitywistyka-ai-bledy-poznawcze-2_00-2026-04-28.html',
    'audhd/obiektywnosc-autyzm-v01.00-2026-05-14.html',
    'audhd/piec-jezykow-milosci-nd-v01.00-2026-05-18.html',
]

for name in FILES:
    if not Path(name).is_file():
        raise SystemExit(f'STOP: brak pliku {name}')

p = Path('piosenki/content_structure.py')
text = p.read_text(encoding='utf-8')
old_select = """            COALESCE(s.description,'')
        FROM content_sections s"""
new_select = """            COALESCE(s.description,''),
            COALESCE(s.content_html,'')
        FROM content_sections s"""
old_cols = '        "anchor_status", "deep_link", "opis",\n    ]'
new_cols = '        "anchor_status", "deep_link", "opis", "content_html",\n    ]'
if text.count(old_select) != 1:
    raise SystemExit(f'STOP: content_structure SELECT match={text.count(old_select)}')
if text.count(old_cols) != 1:
    raise SystemExit(f'STOP: content_structure columns match={text.count(old_cols)}')
text = text.replace(old_select, new_select).replace(old_cols, new_cols)
p.write_text(text, encoding='utf-8')

RENDERER = r'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AuDHD</title>
<style>
:root{--bg:#062e28;--paper:#f1e7cb;--gold:#dfbd63;--muted:#c8ae6b;--line:rgba(223,189,99,.28);color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--paper);font-family:Georgia,"Times New Roman",serif;font-size:18px;line-height:1.65}
main{width:min(920px,calc(100% - 32px));margin:0 auto;padding:44px 0 72px}
h1,h2,h3,h4,h5,h6{color:var(--gold);line-height:1.18;scroll-margin-top:18px}h1{font-size:clamp(2rem,6vw,3.5rem);margin:.2em 0 .65em}h2{font-size:1.75rem;margin:1.7em 0 .55em}h3{font-size:1.35rem;margin:1.5em 0 .5em}h4,h5,h6{margin:1.35em 0 .45em}
p{margin:.7em 0}a{color:var(--gold)}strong,b{color:#f5dc98}blockquote{margin:1.2em 0;padding:.2em 1em;border-left:3px solid var(--gold);color:#e8dbbd}
ul,ol{padding-left:1.4em}li{margin:.28em 0}hr{border:0;border-top:1px solid var(--line);margin:2em 0}
table{border-collapse:collapse;width:100%;display:block;overflow:auto;margin:1.2em 0}th,td{border:1px solid var(--line);padding:.45em .6em;vertical-align:top}th{color:var(--gold)}
pre{overflow:auto;padding:1em;border:1px solid var(--line);background:rgba(0,0,0,.16)}code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.9em}img{max-width:100%;height:auto}
#status{color:var(--muted);padding:18vh 0;text-align:center}.error{color:#ffd0d0}
@media(max-width:700px){body{font-size:17px}main{width:min(100% - 24px,920px);padding-top:28px}}
</style>
</head>
<body>
<main id="doc"><p id="status">Ładowanie tekstu z SQL…</p></main>
<script>
const API='https://piosenki-api.onrender.com/api/content/audhd/structure';
const doc=document.getElementById('doc');
const filename=decodeURIComponent(location.pathname.split('/').pop());
const isEnglish=/EN|equations-metaphysics/i.test(filename);
document.documentElement.lang=isEnglish?'en':'pl';
if(isEnglish) document.getElementById('status').textContent='Loading text from SQL…';
function fail(msg){doc.innerHTML='<p class="error"></p>';doc.firstChild.textContent=msg;}
function addMathJax(){
  window.MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']]},startup:{typeset:false}};
  const s=document.createElement('script');
  s.async=true;
  s.src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
  s.onload=()=>window.MathJax?.typesetPromise?.([doc]);
  document.head.appendChild(s);
}
fetch(API,{cache:'no-store'})
.then(r=>{if(!r.ok)throw new Error(`HTTP ${r.status}`);return r.json();})
.then(data=>{
  const rows=(Array.isArray(data.rows)?data.rows:[])
    .filter(r=>r.dokument_plik===filename && r.section_kind==='heading')
    .sort((a,b)=>Number(a.source_order??a.kolejnosc)-Number(b.source_order??b.kolejnosc));
  if(!rows.length)throw new Error(`SQL: brak dokumentu ${filename}`);
  if(rows.some(r=>typeof r.content_html!=='string'))throw new Error('SQL/API: brak pola content_html');
  document.title=rows[0].dokument_tytul||rows[0].sekcja_tytul||'AuDHD';
  doc.innerHTML='';
  for(const r of rows){
    const level=Math.min(6,Math.max(1,parseInt(String(r.poziom).replace(/\D/g,''),10)||2));
    const h=document.createElement('h'+level);
    h.id=r.anchor||'';
    h.textContent=r.sekcja_tytul||'';
    doc.appendChild(h);
    if(r.content_html){
      const body=document.createElement('div');
      body.className='section-content';
      body.innerHTML=r.content_html;
      doc.appendChild(body);
    }
  }
  addMathJax();
  if(location.hash){
    requestAnimationFrame(()=>{
      const id=decodeURIComponent(location.hash.slice(1));
      document.getElementById(id)?.scrollIntoView();
    });
  }
})
.catch(err=>fail((isEnglish?'Could not load text from SQL: ':'Nie udało się wczytać tekstu z SQL: ')+err.message));
</script>
</body>
</html>
'''

for name in FILES:
    Path(name).write_text(RENDERER, encoding='utf-8')

def redirect(target: str, lang: str = 'pl') -> str:
    return f'''<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<meta http-equiv="refresh" content="0; url=../{target}">\n<title>Przekierowanie</title>\n<script>location.replace('../{target}' + location.hash);</script>\n</head>\n<body><p><a href="../{target}">Przejdź do tekstu</a></p></body>\n</html>\n'''

Path('audhd/rownania/index.html').write_text(
    redirect('CLAUDE_rownania-metafizyka-i-komisja-v01_02-2026-09-03.html'),
    encoding='utf-8',
)
Path('audhd/rownania/index-en.html').write_text(
    redirect('CLAUDE_equations-metaphysics-and-rigged-jury-EN-v01_03-2026-09-07.html', 'en'),
    encoding='utf-8',
)

expected = sorted([
    'piosenki/content_structure.py',
    *FILES,
    'audhd/rownania/index.html',
    'audhd/rownania/index-en.html',
])
changed = sorted(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
if changed != expected:
    missing = sorted(set(expected) - set(changed))
    extra = sorted(set(changed) - set(expected))
    raise SystemExit(f'STOP: zly zestaw zmian missing={missing} extra={extra}')

subprocess.run(['python3', '-m', 'py_compile', 'piosenki/content_structure.py'], check=True)
subprocess.run(['git', 'diff', '--check'], check=True)
print(f'OK PATCH: pliki={len(changed)}; renderery=18; API=content_html; rownania_redirect=2')
