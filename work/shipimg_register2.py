# 修正版登记：zh 标题一律加单引号，避免冒号/撇号破坏 YAML。
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'
WORK = ROOT / 'work' / 'shipimg'

picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))


def infer_part(blob):
    b = blob.lower()
    if any(k in b for k in ['turret', 'gun', 'barbette']):
        return 'turret'
    if any(k in b for k in ['bridge', 'island', 'superstructure', 'funnel',
                            'mast', 'radar', 'director']):
        return 'superstructure'
    if any(k in b for k in ['flight deck', 'deck', 'catapult', 'aircraft',
                            'plane', 'air group']):
        return 'aircraft_handling'
    if any(k in b for k in ['stern', 'quarterdeck']):
        return 'stern'
    if any(k in b for k in ['bow', 'forecastle']):
        return 'bow'
    return 'hull_side'


def infer_view(blob):
    b = blob.lower()
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


def infer_date(entry):
    for src in (entry.get('date', ''), entry.get('title', ''), entry.get('desc', '')):
        m = re.search(r'(19[234]\d)', str(src))
        if m:
            return m.group(1)
    return None


def zh_title(entry):
    desc = (entry.get('desc') or '').strip()
    if desc:
        s = re.split(r'[.;]', desc)[0].strip()
        # 去掉开头的 "Description:" / "Omschrijving:" 之类前缀
        s = re.sub(r'^[A-Za-z]{4,16}:\s*', '', s)
        if 8 <= len(s) <= 100:
            return s
    base = entry['title'].rsplit('.', 1)[0]
    base = re.sub(r'\s*-\s*NARA.*$', '', base)
    return base[:100] or entry['name']


def q(s):
    """YAML 单引号字符串：内部单引号翻倍，冒号与特殊字符自动安全。"""
    s = str(s or '').replace('\n', ' ').strip()
    return "'" + s.replace("'", "''") + "'"


ORDER = ['akagi', 'bismarck', 'enterprise', 'hiryu', 'hornet', 'illustrious',
         'kaga', 'king-george-v', 'prince-of-wales', 'prinz-eugen', 'rodney',
         'soryu', 'tirpitz', 'yorktown']

blocks = []
for sid in ORDER:
    for e in picked.get(sid, []):
        blob = e['title'] + ' ' + (e.get('desc') or '')
        lic = e.get('license', '')
        tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B'
        iid = re.sub(r'[^a-zA-Z0-9-]+', '-', e['name'].rsplit('.', 1)[0]).strip('-').lower()
        if len(iid) > 58:
            iid = iid[:58]

        parts = [
            f'  - id: {iid}',
            f'    file: /img/ships/{e["name"]}',
            f'    subject: ship:{sid}',
            '    title:',
            f'      zh: {q(zh_title(e))}',
            f'      en: {q(e["title"])}',
            f'    part: {infer_part(blob)}',
            f'    view: {infer_view(blob)}',
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

text = io.open(IMG, encoding='utf-8').read()
added = 0
skipped = 0
for b in blocks:
    iid = re.search(r'^  - id: (\S+)$', b, re.M).group(1)
    if f'id: {iid}\n' in text or f'id: {iid} ' in text:
        skipped += 1
        continue
    anchor = '  - id: a6m2-primary'
    i = text.find(anchor)
    if i < 0:
        print('锚点丢失')
        break
    text = text[:i] + b + '\n' + text[i:]
    added += 1

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
print(f'插入 {added} 条（跳过重复 {skipped}）')

import yaml
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
