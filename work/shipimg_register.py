# 把新增舰图登记进 images.yaml。
#
# 要点：
# 1. 不覆盖已有主图（primary: true 的那张保留）
# 2. 新图一律 primary: false，作为图集补充
# 3. part/view 从标题与描述里推断，推断不出的标 other
# 4. Commons 的 Artist 字段可能含 HTML，已在上游剥过
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
    if any(k in b for k in ['aerial', 'overhead', 'from above', 'vertical']):
        return 'hull_side'
    return 'hull_side'


def infer_view(blob):
    b = blob.lower()
    if any(k in b for k in ['aerial', 'overhead', 'from above', 'vertical aerial']):
        return 'overhead'
    if any(k in b for k in ['detail', 'close', 'closeup', 'gun crew', 'mounting']):
        return 'detail'
    if any(k in b for k in ['bow']):
        return 'bow'
    if any(k in b for k in ['stern']):
        return 'stern'
    if any(k in b for k in ['deck']):
        return 'deck'
    return 'broadside'


def infer_date(entry):
    """从日期字段或标题里抽年份。"""
    for src in (entry.get('date', ''), entry.get('title', ''), entry.get('desc', '')):
        m = re.search(r'(19[23]\d)', str(src))
        if m:
            return m.group(1)
    return None


def zh_title(entry):
    """给一个不夸张的中文标题：优先用描述里的一句话，否则用文件名。"""
    desc = entry.get('desc', '').strip()
    if desc:
        # 取第一个句子，限长
        s = re.split(r'[.;]', desc)[0].strip()
        if 8 <= len(s) <= 110:
            return s
    base = entry['title'].rsplit('.', 1)[0]
    base = re.sub(r'\s*-\s*NARA.*$', '', base)
    base = re.sub(r'\(.*?\)', '', base).strip()
    return base[:100] or entry['name']


def q(s):
    return "'" + str(s or '').replace("'", "''") + "'"


ORDER = ['akagi', 'bismarck', 'enterprise', 'hiryu', 'hornet', 'illustrious',
         'kaga', 'king-george-v', 'prince-of-wales', 'prinz-eugen', 'rodney',
         'soryu', 'tirpitz', 'yorktown']

blocks = []
count = 0
for sid in ORDER:
    for e in picked.get(sid, []):
        blob = e['title'] + ' ' + e.get('desc', '')
        part = infer_part(blob)
        view = infer_view(blob)
        date = infer_date(e)
        lic = e.get('license', '')
        tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B'
        iid = e['name'].rsplit('.', 1)[0].replace('_', '-')
        if len(iid) > 60:
            iid = iid[:60]

        parts = [
            f'  - id: {iid}',
            f'    file: /img/ships/{e["name"]}',
            f'    subject: ship:{sid}',
            '    title:',
            f'      zh: {zh_title(e)}',
            f'      en: {q(e["title"])}',
            f'    part: {part}',
            f'    view: {view}',
        ]
        if date:
            parts.append(f'    date: {date}')
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
        count += 1

text = io.open(IMG, encoding='utf-8').read()

# 安全检查：已有的新图 id 不重复插入
added = 0
for b in blocks:
    m = re.search(r'^  - id: (\S+)$', b, re.M)
    iid = m.group(1)
    if f'id: {iid}' in text:
        continue
    anchor = '  - id: a6m2-primary'
    i = text.find(anchor)
    if i < 0:
        print('找不到锚点')
        break
    text = text[:i] + b + '\n' + text[i:]
    added += 1

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
print(f'生成 {count} 条，实际插入 {added} 条')

import yaml
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print('图片总数:', len(d['images']))
ships = {}
for im in d['images']:
    s = str(im.get('subject') or '')
    if s.startswith('ship:'):
        ships[s[5:]] = ships.get(s[5:], 0) + 1
print()
print('=== 每舰图数（登记后）===')
for sid in ORDER:
    print(f'  {sid:<18} {ships.get(sid, 0)}')
print(f'舰图总计 {sum(ships.values())}')
