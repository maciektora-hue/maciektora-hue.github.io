from pathlib import Path

path = Path('piosenki/playlist_importer.py')
text = path.read_text(encoding='utf-8')

old_func = '''def _tags_json(tags: list[str]) -> str:\n    out = []\n    for tag in tags:\n        tag = tag.strip()\n        if tag and tag not in out:\n            out.append(tag)\n    return json.dumps(out, ensure_ascii=False, separators=(\",\", \":\"))\n'''
new_func = old_func + '''\n\ndef _tags_plain(tags: list[str]) -> str:\n    out = []\n    for tag in tags:\n        tag = tag.strip()\n        if tag and tag not in out:\n            out.append(tag)\n    return \"; \".join(out)\n'''

old_insert = '''                \"\"\"INSERT INTO playlist(\n                       playlist_id, playlist_series_id, service, name,\n                       external_playlist_id, external_url, source_file, exported_at, tags\n                   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\",\n                (playlist_id, playlist_series_id, service, name, external_playlist_id,\n                 external_url, Path(source_path).name, exported_at, _tags_json(tags)),\n'''
new_insert = '''                \"\"\"INSERT INTO playlist(\n                       playlist_id, playlist_series_id, service, name,\n                       external_playlist_id, external_url, source_file, exported_at, tags, playlist_tags\n                   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\",\n                (playlist_id, playlist_series_id, service, name, external_playlist_id,\n                 external_url, Path(source_path).name, exported_at, _tags_json(tags), _tags_plain(tags)),\n'''

if 'def _tags_plain(' not in text:
    if old_func not in text:
        raise SystemExit('Nie znaleziono funkcji _tags_json do patchowania')
    text = text.replace(old_func, new_func, 1)

if 'exported_at, tags, playlist_tags' not in text:
    if old_insert not in text:
        raise SystemExit('Nie znaleziono INSERT playlist do patchowania')
    text = text.replace(old_insert, new_insert, 1)

if 'def _tags_plain(' not in text or 'exported_at, tags, playlist_tags' not in text:
    raise SystemExit('Weryfikacja patcha importera nie powiodla sie')

path.write_text(text, encoding='utf-8')
print('PLAYLIST_IMPORTER_TAGS_PATCH_OK')
