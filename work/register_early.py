# 登记 early 图，并显示信息。
import io
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'
WORK = ROOT / 'work' / 'shipimg'

added = json.load(io.open(WORK / 'early_added.json', encoding='utf-8'))


def q(s):
    s = str(s or '').replace('\n', ' ').strip()
    return "'" + s.replace("'", "''") + "'"


blocks = []
for x in added:
    sid = x['sid']
    name = x['name']
    iid = re.sub(r'[^a-zA-Z0-9-]+', '-', name.rsplit('.', 1)[0]).strip('-').lower()[:58]
    lic = x.get('license') or ''
    tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B'
    y = x['year']

    # 中文标题：用描述首句，否则用文件名
    desc = (x.get('desc') or '').strip()
    zh = ''
    if desc:
        s = re.split(r'[.;]', desc)[0].strip()
        s = re.sub(r'^[A-Za-z]{4,16}:\s*', '', s)
        if 8 <= len(s) <= 100:
            zh = s
    if not zh:
        zh = x['title'].rsplit('.', 1)[0][:100]

    blocks.append(f"""  - id: {iid}
    file: /img/ships/{name}
    subject: ship:{sid}
    title:
      zh: {q(zh)}
      en: {q(x['title'])}
    part: hull_side
    view: broadside
    date: {y}
    license: {'pd' if tier == 'A' else 'cc'}
    license_tier: {tier}
    license_raw: {q(lic)}
    author: {q(x.get('artist') or 'Unknown author')}
    source_url: {q(x.get('page'))}
    width: {x.get('w') or 1280}
    height: {x.get('h') or 800}
    primary: false
""")
    print(f'  {sid:<16} {y}  {name[:56]}')

text = io.open(IMG, encoding='utf-8').read()
n = 0
for b in blocks:
    iid = re.search(r'^  - id: (\S+)$', b, re.M).group(1)
    if f'id: {iid}\n' in text:
        continue
    anchor = '  - id: a6m2-primary'
    i = text.find(anchor)
    if i < 0:
        break
    text = text[:i] + b + '\n' + text[i:]
    n += 1

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
print(f'\n插入 {n} 条')

d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print('图片总数:', len(d['images']))
