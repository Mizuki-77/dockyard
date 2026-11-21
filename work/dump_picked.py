# 逐条列出 180 张选中的图，人工核对哪些要剔除。
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
picked = json.load(io.open(ROOT / 'work' / 'shipimg' / 'picked.json', encoding='utf-8'))

for sid in ['yorktown', 'hood', 'prince-of-wales', 'enterprise', 'bismarck', 'prinz-eugen']:
    entries = picked.get(sid, [])
    print('=' * 74)
    print(f'{sid} ({len(entries)})')
    for e in entries:
        print(f'  {e["name"][:56]}')
        print(f'     title: {e["title"][:88]}')
        d = e.get('desc', '')
        if d:
            print(f'     desc : {d[:88]}')
