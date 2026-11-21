# 全面校验所有 -extra- 图，然后重新生成 images.yaml 的登记。
import io
import json
import os
import re
import urllib.request
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'
IMG = ROOT / 'data' / 'images.yaml'

# 1. 校验所有文件
bad = []
good = []
for f in sorted(os.listdir(OUT)):
    if '-extra-' not in f:
        continue
    p = OUT / f
    try:
        with io.open(p, 'rb') as fh:
            head = fh.read(2)
        if head == b'\xff\xd8' and p.stat().st_size > 5000:
            good.append(f)
        else:
            bad.append(f)
    except Exception:
        bad.append(f)

print(f'有效 {len(good)}，无效 {len(bad)}')
for b in bad:
    print(f'  删除无效 {b}')
    try:
        (OUT / b).unlink()
    except Exception:
        pass

# 2. 建立文件名 -> 候选元数据 的映射（按 slug 匹配）
cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))


def slug(s):
    return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()


# 为每个文件名找对应候选
tmap = {}
for sid, entries in cand.items():
    for e in entries:
        tmap[slug(e['title'])[:40]] = e
        tmap[slug(e['title'])[:44]] = e

matched = 0
unmatched = []

# 3. 读现有 images.yaml，移除我们之前加的（避免重复），再统一重加
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
existing_files = {str(x.get('file', '')) for x in d['images']}

# 4. 生成新块
ORDER = ['akagi', 'bismarck', 'enterprise', 'hiryu', 'hornet', 'illustrious',
         'kaga', 'king-george-v', 'prince-of-wales', 'prinz-eugen', 'rodney',
         'soryu', 'tirpitz', 'yorktown']


def q(s):
    s = str(s or '').replace('\n', ' ').strip()
    return "'" + s.replace("'", "''") + "'"


def infer_part(b):
    b = b.lower()
    if any(k in b for k in ['turret', 'gun', 'barbette']):
        return 'turret'
    if any(k in b for k in ['bridge', 'island', 'superstructure', 'funnel',
                            'mast', 'radar', 'director']):
        return 'superstructure'
    if any(k in b for k in ['flight deck', 'catapult', 'aircraft', 'plane']):
        return 'aircraft_handling'
    if any(k in b for k in ['stern', 'quarterdeck']):
        return 'stern'
    if any(k in b for k in ['bow', 'forecastle']):
        return 'bow'
    return 'hull_side'


def infer_view(b):
    b = b.lower()
    if any(k in b for k in ['aerial', 'overhead', 'from above', 'vertical']):
        return 'overhead'
    if any(k in b for k in ['detail', 'closeup', 'gun crew']):
        return 'detail'
    if 'bow' in b:
        return 'bow'
    if 'stern' in b:
        return 'stern'
    if 'deck' in b:
        return 'deck'
    return 'broadside'


def infer_date(e):
    for src in (e.get('date', ''), e.get('title', ''), e.get('desc', '')):
        m = re.search(r'(19[234]\d)', str(src))
        if m:
            return m.group(1)
    return None


def zh_title(e):
    desc = (e.get('desc') or '').strip()
    if desc:
        s = re.split(r'[.;]', desc)[0].strip()
        s = re.sub(r'^[A-Za-z]{4,16}:\s*', '', s)
        if 8 <= len(s) <= 100:
            return s
    base = e['title'].rsplit('.', 1)[0]
    base = re.sub(r'\s*-\s*NARA.*$', '', base)
    return base[:100]


blocks = []
for sid in ORDER:
    files = sorted([f for f in good if f.startswith(sid + '-extra-')])
    for f in files:
        # 找元数据：文件名里含 slug 的候选
        base = f.rsplit('.', 1)[0]
        m = re.search(r'-extra-[a-z]?\d*-(.+)$', base)
        key = m.group(1) if m else ''
        e = tmap.get(key) or tmap.get(key[:40])
        if not e:
            # 退而求其次：把 key 当标题
            e = {'title': key, 'desc': '', 'license': 'Public domain',
                 'artist': '', 'page': '', 'w': 1280, 'h': 800, 'date': ''}
            unmatched.append(f)
        else:
            matched += 1

        b = e['title'] + ' ' + (e.get('desc') or '')
        lic = e.get('license', '')
        tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B'
        iid = re.sub(r'[^a-zA-Z0-9-]+', '-', base).strip('-').lower()[:58]

        parts = [
            f'  - id: {iid}',
            f'    file: /img/ships/{f}',
            f'    subject: ship:{sid}',
            '    title:',
            f'      zh: {q(zh_title(e))}',
            f'      en: {q(e["title"])}',
            f'    part: {infer_part(b)}',
            f'    view: {infer_view(b)}',
        ]
        dt = infer_date(e)
        if dt:
            parts.append(f'    date: {dt}')
        parts += [
            f'    license: {"pd" if tier == "A" else "cc"}',
            f'    license_tier: {tier}',
            f'    license_raw: {q(lic)}',
            f'    author: {q(e.get("artist") or "Unknown author")}',
            f'    source_url: {q(e.get("page"))}',
            f'    width: {e.get("w") or 1280}',
            f'    height: {e.get("h") or 800}',
            '    primary: false',
        ]
        blocks.append('\n'.join(parts) + '\n')

print(f'\n匹配元数据 {matched} 条，未匹配 {len(unmatched)}')

text = io.open(IMG, encoding='utf-8').read()
added = 0
for b in blocks:
    iid = re.search(r'^  - id: (\S+)$', b, re.M).group(1)
    if f'id: {iid}\n' in text:
        continue
    anchor = '  - id: a6m2-primary'
    i = text.find(anchor)
    if i < 0:
        break
    text = text[:i] + b + '\n' + text[i:]
    added += 1

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
print(f'插入 {added} 条')

d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print('图片总数:', len(d['images']))
ships = {}
for im in d['images']:
    s = str(im.get('subject') or '')
    if s.startswith('ship:'):
        ships[s[5:]] = ships.get(s[5:], 0) + 1
print()
for sid in ORDER:
    print(f'  {sid:<18} {ships.get(sid, 0)}')
print(f'舰图总计 {sum(ships.values())}')
