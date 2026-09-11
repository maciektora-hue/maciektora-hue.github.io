from pathlib import Path

FILES = {
    'piosenki/audio.html': ('<h2>Co zrobiliśmy</h2>', 'pl'),
    'piosenki/audio-en.html': ('<h2>What we did</h2>', 'en'),
    'piosenki/SOL-klastrowanie-audio-wyniki-dwa-glosy-v01-2026-09-08.html': ('<h2 id="playlisty-sql">Playlisty — SQL</h2>', 'pl'),
    'piosenki/SOL-audio-clustering-three-island-signatures-two-voices-v01-2026-09-08-en.html': ('<h2 id="mini-glossary">Mini-glossary</h2>', 'en'),
}

CSS = '''
.playlist-top{margin:1.25rem 0 1.8rem;padding:16px 18px;border:2px solid var(--line);border-radius:10px;background:var(--panel)}
.playlist-top h2{margin:.1rem 0 .35rem}
.playlist-top-intro{margin:.15rem 0 1rem;color:var(--muted)}
.playlist-top-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(245px,1fr));gap:10px}
.playlist-top-card{padding:11px 12px;border:1px solid var(--line);border-radius:9px;background:var(--panel2)}
.playlist-top-card p{margin:.25rem 0 .55rem;color:var(--muted);font-size:.9rem}
.playlist-top-links{display:flex;gap:7px;flex-wrap:wrap}
.playlist-top-links a{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:5px 9px;text-decoration:none;font-size:.82rem;font-weight:700;color:var(--strong)}
'''

URLS = {
    'depth': ('https://open.spotify.com/playlist/2XlvqJZUNVjR4KGIpF39nG', 'https://music.youtube.com/playlist?list=PLUK_LdKYWxTk'),
    'light': ('https://open.spotify.com/playlist/272wzPwVUjxBmqJ8eNQsTW', 'https://music.youtube.com/playlist?list=PLdqONEJClykk'),
    'motion': ('https://open.spotify.com/playlist/3KEDfDtvGvwWyZINTWm37i', 'https://music.youtube.com/playlist?list=PLeop-pmwxm1w'),
    'bridge': ('https://open.spotify.com/playlist/42r40qtwg2mOoHDk5Akr9G', 'https://music.youtube.com/playlist?list=PLacFJ1WpA7YQ'),
    'periphery': ('https://open.spotify.com/playlist/4hPcWJRfNQjEef2Re2NRli', 'https://music.youtube.com/playlist?list=PLAFO32rZCzu4'),
}

def links(key):
    spotify, youtube = URLS[key]
    return f'<div class="playlist-top-links"><a href="{spotify}" target="_blank" rel="noopener">Spotify ↗</a><a href="{youtube}" target="_blank" rel="noopener">YouTube Music ↗</a></div>'

BLOCK_PL = f'''<!-- STATIC-PLAYLIST-LINKS -->
<section class="playlist-top" aria-label="Playlisty do słuchania">
  <h2>Playlisty do słuchania</h2>
  <p class="playlist-top-intro">Linki są widoczne od razu, pod opisem. Bez rozwijania sekcji i bez zależności od SQL.</p>
  <div class="playlist-top-grid">
    <div class="playlist-top-card"><strong>Głębia</strong><p>Ciemniejsza, basowa, skupiona.</p>{links('depth')}</div>
    <div class="playlist-top-card"><strong>Światło</strong><p>Jasna, szerokopasmowa, ziarnista.</p>{links('light')}</div>
    <div class="playlist-top-card"><strong>Ruch</strong><p>Środek pasma, przepływ i ruch harmoniczny.</p>{links('motion')}</div>
    <div class="playlist-top-card"><strong>Most Głębia ↔ Ruch</strong><p>Największy z mostów między rdzeniami.</p>{links('bridge')}</div>
    <div class="playlist-top-card"><strong>Peryferia</strong><p>Najrzadsze akustycznie części mapy.</p>{links('periphery')}</div>
  </div>
</section>
'''

BLOCK_EN = f'''<!-- STATIC-PLAYLIST-LINKS -->
<section class="playlist-top" aria-label="Playlists to listen to">
  <h2>Playlists to listen to</h2>
  <p class="playlist-top-intro">The links are visible immediately, below the description. No collapsed section and no SQL dependency.</p>
  <div class="playlist-top-grid">
    <div class="playlist-top-card"><strong>Depth</strong><p>Darker, bass-rich and focused.</p>{links('depth')}</div>
    <div class="playlist-top-card"><strong>Light</strong><p>Bright, broadband and grainy.</p>{links('light')}</div>
    <div class="playlist-top-card"><strong>Motion</strong><p>Midrange, flow and harmonic movement.</p>{links('motion')}</div>
    <div class="playlist-top-card"><strong>Depth ↔ Motion bridge</strong><p>The largest bridge between the cores.</p>{links('bridge')}</div>
    <div class="playlist-top-card"><strong>Periphery</strong><p>The acoustically sparsest parts of the map.</p>{links('periphery')}</div>
  </div>
</section>
'''

for filename, (anchor, lang) in FILES.items():
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    if '<!-- STATIC-PLAYLIST-LINKS -->' in text:
        print(filename, 'already patched')
        continue
    if '</style>' not in text:
        raise SystemExit(f'{filename}: no closing style tag')
    if anchor not in text:
        raise SystemExit(f'{filename}: anchor not found')
    text = text.replace('</style>', CSS + '\n</style>', 1)
    text = text.replace(anchor, (BLOCK_PL if lang == 'pl' else BLOCK_EN) + '\n' + anchor, 1)
    path.write_text(text, encoding='utf-8')
    print(filename, 'patched')
