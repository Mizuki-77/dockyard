# 把四型武器的配图追加进 images.yaml。
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'
WORK = ROOT / 'work' / 'weaponimg2'

picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))

# 每型在 weapons.yaml 里的 part/view 与图注
ORDER = ['16in-45-mk1', '6in-50-mk22', '47in-40-mk8', '20-3cm-sk-c34']


def q(s):
    return "'" + str(s or '').replace("'", "''") + "'"


blocks = []
for wid in ORDER:
    rec = picked.get(wid)
    if not rec:
        print(f'跳过 {wid}')
        continue
    m = rec['meta']
    blocks.append(f"""  - id: {wid}-primary
    file: {rec['file']}
    subject: weapon:{wid}
    title:
      zh: {m['zh']}
      en: {q(m['en'])}
    part: {m['part']}
    view: {m['view']}
    date: {m['date']}
    license: pd
    license_tier: {rec['tier']}
    license_raw: {q(rec['license'])}
    author: {q(rec['author'])}
    credit: {q('Imperial War Museums / Wikimedia Commons')}
    source_url: {q(rec['page'])}
    width: {rec['w']}
    height: {rec['h']}
    primary: true
    note: {m['note']}
""")

text = io.open(IMG, encoding='utf-8').read()
for b in blocks:
    wid = re.search(r'subject: weapon:(\S+)', b).group(1)
    if f'id: {wid}-primary' in text:
        print(f'{wid} 已存在，跳过')
        continue
    # 插到 a6m2-primary 之前，保持武器图成组
    anchor = '  - id: a6m2-primary'
    i = text.find(anchor)
    if i < 0:
        print('找不到锚点')
        break
    text = text[:i] + b + '\n' + text[i:]
    print(f'插入 {wid}-primary')

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)

import yaml
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print('图片总数:', len(d['images']))
for wid in ORDER:
    n = [x for x in d['images'] if x['id'] == f'{wid}-primary']
    print(f'  {wid}: {"OK" if n else "缺"}')
