from pathlib import Path

# playlist_api.py: use only playlist_tags and perform one-time guarded DROP at startup.
p = Path('piosenki/playlist_api.py')
s = p.read_text(encoding='utf-8')
s = s.replace(
    'from app import app, get_connection, fetch_rows\n\n\n@app.get("/api/playlisty")',
    '''from app import app, get_connection, fetch_rows\n\n\ndef _drop_legacy_playlist_tags_once():\n    conn = get_connection()\n    try:\n        columns = [row[1] for row in conn.execute("PRAGMA table_info(playlist)").fetchall()]\n        if "tags" not in columns:\n            print("PLAYLIST_LEGACY_TAGS_DROP_ALREADY_DONE", flush=True)\n            return\n        if "playlist_tags" not in columns:\n            raise RuntimeError("playlist_tags missing; refusing to drop legacy tags")\n        before = int(conn.execute("SELECT COUNT(*) FROM playlist").fetchone()[0] or 0)\n        empty = int(conn.execute("SELECT COUNT(*) FROM playlist WHERE TRIM(COALESCE(playlist_tags, ''))='' ").fetchone()[0] or 0)\n        if empty:\n            raise RuntimeError(f"refusing to drop legacy tags: {empty} playlists have empty playlist_tags")\n        conn.execute("ALTER TABLE playlist DROP COLUMN tags")\n        conn.commit()\n        after_columns = [row[1] for row in conn.execute("PRAGMA table_info(playlist)").fetchall()]\n        after = int(conn.execute("SELECT COUNT(*) FROM playlist").fetchone()[0] or 0)\n        if "tags" in after_columns or "playlist_tags" not in after_columns or before != after:\n            raise RuntimeError("legacy tags DROP verification failed")\n        print(f"PLAYLIST_LEGACY_TAGS_DROP_OK playlists={after}", flush=True)\n    finally:\n        conn.close()\n\n\n_drop_legacy_playlist_tags_once()\n\n\n@app.get("/api/playlisty")''',
    1,
)
s = s.replace("COALESCE(NULLIF(p.playlist_tags, ''), p.tags) AS tags,", "p.playlist_tags AS tags,", 1)
s = s.replace('p.exported_at, p.imported_at, p.playlist_tags, p.tags', 'p.exported_at, p.imported_at, p.playlist_tags', 1)
if 'p.tags' in s or 'COALESCE(NULLIF(p.playlist_tags' in s:
    raise SystemExit('playlist_api.py still references legacy p.tags')
if 'PLAYLIST_LEGACY_TAGS_DROP_OK' not in s:
    raise SystemExit('playlist_api.py migration block not installed')
p.write_text(s, encoding='utf-8')

# playlist_importer.py: stop writing legacy JSON tags.
p = Path('piosenki/playlist_importer.py')
s = p.read_text(encoding='utf-8')
s = s.replace('import json\n', '', 1)
old_func = '''def _tags_json(tags: list[str]) -> str:\n    out = []\n    for tag in tags:\n        tag = tag.strip()\n        if tag and tag not in out:\n            out.append(tag)\n    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))\n\n\n'''
s = s.replace(old_func, '', 1)
s = s.replace(
    '''                       external_playlist_id, external_url, source_file, exported_at, tags, playlist_tags\n                   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    '''                       external_playlist_id, external_url, source_file, exported_at, playlist_tags\n                   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    1,
)
s = s.replace(
    '''                 external_url, Path(source_path).name, exported_at, _tags_json(tags), _tags_plain(tags)),''',
    '''                 external_url, Path(source_path).name, exported_at, _tags_plain(tags)),''',
    1,
)
if '_tags_json' in s or 'exported_at, tags, playlist_tags' in s:
    raise SystemExit('playlist_importer.py still writes legacy tags')
p.write_text(s, encoding='utf-8')

# island_playlist_import.py: stop writing legacy JSON tags.
p = Path('piosenki/island_playlist_import.py')
s = p.read_text(encoding='utf-8')
s = s.replace(
    '''                        exported_at, tags\n                    ) VALUES (?, ?, 'spotify', ?, ?, ?, ?, NULL, ?)''',
    '''                        exported_at, playlist_tags\n                    ) VALUES (?, ?, 'spotify', ?, ?, ?, ?, NULL, ?)''',
    1,
)
s = s.replace(
    '''                        json.dumps(["owner:maciek-tora"], ensure_ascii=False, separators=(",", ":")),''',
    '''                        "owner:maciek-tora",''',
    1,
)
if 'exported_at, tags' in s or 'json.dumps(["owner:maciek-tora"]' in s:
    raise SystemExit('island_playlist_import.py still writes legacy tags')
p.write_text(s, encoding='utf-8')

print('PLAYLIST_LEGACY_TAGS_CODE_PATCH_OK')
