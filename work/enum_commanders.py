# 枚举全部指挥官记录，去重成人，产出清单供后续调研。
import glob
import io
import json
import re
import unicodedata

import yaml

# 军衔前缀（英/德/波三套）
RANKS = [
    'Kapitän zur See', 'Kpt.z.S.', 'Korvettenkapitän', 'K.Kpt.',
    'kmdr por.', 'kmdr ppor.', 'kmdr',
    'Captain', 'Capt.', 'Commander', 'Cdr.', 'Lieutenant', 'Lt.',
]


def parse(raw):
    s = str(raw or '').strip()

    # 值里可能有 "→ Capt. XXX" 连写两个任期，先只保留第一段
    # （第二段是接任者，不是这一个人）
    if '→' in s:
        s = s.split('→')[0].strip()

    # 剥括号。括号内是任期冗余信息（与 valid 窗口重复），丢弃
    paren = ''
    m = re.search(r'[（(]([^）)]*)[）)]', s)
    if m:
        paren = m.group(1).strip()
        s = (s[:m.start()] + ' ' + s[m.end():]).strip()

    # 军衔前缀
    rank = ''
    for r in RANKS:
        if s.startswith(r + ' ') or s.startswith(r + '.'):
            rank = r.rstrip('.').strip()
            s = s[len(r):].strip().lstrip('.').strip()
            break

    # 勋衔串：DSO / DSC / RN / VC / OBE / KCB / DSO* 这类全大写缩写，
    # 以及夹杂的逗号。反复剥到没有为止（有的名字后面跟三四个）
    while True:
        new = re.sub(r',\s*[A-Z]{2,4}\*?\s*$', '', s).strip()
        new = re.sub(r',\s*[A-Z][a-z]{1,3}\*?\s*$', '', new).strip()
        if new == s:
            break
        s = new

    s = s.strip(' ,')
    # 去掉可能残留的空括号
    s = re.sub(r'\(\s*\)|（\s*）', '', s).strip()
    return rank, s, paren


rows = []
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    sid = d.get('id')
    szh = (d.get('name') or {}).get('zh')
    for f in d.get('facts') or []:
        if f.get('field') != 'service.commander':
            continue
        v = f.get('valid') or {}
        rank, name, paren = parse(f.get('value'))
        rows.append({
            'ship': sid,
            'ship_zh': szh,
            'rank': rank,
            'name': name,
            'raw': str(f.get('value') or ''),
            'from': str(v.get('from') or ''),
            'to': str(v.get('to') or ''),
            'note': str(f.get('note') or ''),
            'src': f.get('src') or [],
            'paren': paren,
        })

# 按人名归并（同一人可能指挥多艘舰 / 多任期）
people = {}
for r in rows:
    key = r['name']
    if not key:
        continue
    p = people.setdefault(key, {'name': key, 'ranks': set(), 'tenures': []})
    if r['rank']:
        p['ranks'].add(r['rank'])
    p['tenures'].append(r)

print(f'事实记录 {len(rows)} 条 → 去重后 {len(people)} 人')
print()
for i, (name, p) in enumerate(sorted(people.items()), 1):
    ships = []
    for t in p['tenures']:
        span = f"{t['from'] or '?'}..{t['to'] or '?'}"
        ships.append(f"{t['ship_zh']}({span})")
    print(f'{i:>2}. {name}')
    print(f'    军衔: {"/".join(sorted(p["ranks"])) or "?"}')
    print(f'    任期: {"; ".join(ships)}')

io.open('work/cmdr_rows.json', 'w', encoding='utf-8').write(
    json.dumps({'rows': rows, 'people': {k: {'name': v['name'],
                                             'ranks': sorted(v['ranks']),
                                             'tenures': v['tenures']}
                                         for k, v in people.items()}},
               ensure_ascii=False, indent=2, default=str))
print()
print('已写 work/cmdr_rows.json')
