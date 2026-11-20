# 用 Commons API（未限流）重新确认 25mm-96 的正确主图直链。
# 上一轮自动选中了「加贺着陆作业」——那是分类污染，不是 25mm 炮。

import io
import json
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

TARGETS = [
    'File:127-GW-304-143496 (24979023882).jpg',   # 硫磺岛双联 25mm，PD
    'File:Type 96 Japanese 25 mm gun - Beijing Museum.jpg',  # 北京军博，PD，3400x2409
]

d = json.load(io.open('work/weaponimg/candidates.json', encoding='utf-8'))
entries = {e['title']: e for e in d['25mm-96']['entries']}

for t in TARGETS:
    e = entries.get(t)
    if not e:
        print(f'{t}: 不在候选里')
        continue
    print(f'\n=== {t} ===')
    print(f"  {e['w']}x{e['h']}  {e['license']}")
    print(f"  thumb: {e['thumb']}")
    print(f"  full : {e['full']}")
    print(f"  page : {e['page']}")
    print(f"  author: {e.get('artist')}")
