# 检查下载下来的图有没有明显不对的。
import json
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
picked = json.load(io.open(ROOT / 'work' / 'shipimg' / 'picked.json', encoding='utf-8'))

# 明显的错误模式
SUSPECT = [
    ('lexington', ' Lexington'),
    ('texas', ' Texas'),
    ('jacob', 'Jacob'),
    ('pawaalpav', 'pawaalpav'),
    ('churchill', 'Churchill'),
    ('restoration', 'restoration'),
    ('partial', 'partial'),
    ('original scan', 'scan'),
    ('tiff', 'tiff'),
    ('png', 'png'),
    ('h60452', 'H60452'),
    ('hu108', 'HU108'),
    ('hu7602', 'HU7602'),
]

print('=== 可疑条目 ===')
for sid, entries in picked.items():
    for e in entries:
        blob = (e['title'] + ' ' + e.get('desc', '')).lower()
        for key, label in SUSPECT:
            if key in blob:
                print(f'  {sid:<18} {e["name"][:50]:<52} ← {label}')
                break

print()
print('=== 每舰张数与文件名 ===')
for sid, entries in picked.items():
    print(f'{sid} ({len(entries)})')
    for e in entries:
        print(f'   {e["name"]}')
