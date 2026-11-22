# 统计 commander 数据，决定「战舰指挥官」页面能做什么。
import glob
import io
import re

import yaml

rows = []
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    sid = d.get('id')
    zh = (d.get('name') or {}).get('zh')
    cid = d.get('class')
    for f in d.get('facts') or []:
        if f.get('field') != 'service.commander':
            continue
        v = f.get('valid') or {}
        rows.append({
            'ship': sid, 'ship_zh': zh, 'class': cid,
            'name': str(f.get('value') or ''),
            'from': str(v.get('from') or ''),
            'to': str(v.get('to') or ''),
            'src': f.get('src') or [],
            'conf': f.get('confidence'),
            'note': str(f.get('note') or ''),
        })

print(f'commander fact 总数：{len(rows)}')
print()

# 去重后的人名数（粗略：取名字主干）
def rough_name(s):
    # 去掉括号注释、军衔前缀
    s = re.sub(r'（[^）]*）', '', s)
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'^(Capt\.|Captain|Cdr\.|Commander|Lt\.|Lieutenant|'
               r'Kpt\.z\.S\.|Kapitän zur See|kmdr por\.|kmdr|Adm\.|Admiral)\s*', '', s)
    s = re.sub(r',\s*(RN|DSO|DSC|VC|OBE|KCB)[^,]*$', '', s)
    return s.strip(' ,')

names = {}
for r in rows:
    n = rough_name(r['name'])
    if n:
        names.setdefault(n, []).append(r)
print(f'不同人名（粗略去重）：{len(names)}')
print()

# 涉及舰数
ships = {}
for r in rows:
    ships.setdefault(r['ship'], 0)
    ships[r['ship']] += 1
print(f'有 commander 数据的舰：{len(ships)} / 25')
for s, n in sorted(ships.items(), key=lambda x: -x[1]):
    print(f'  {s:<16} {n}')
print()

print('样例（前 8 条）：')
for r in rows[:8]:
    print(f"  {r['ship_zh']:<10} {r['name'][:60]:<60} {r['from']}..{r['to']}")
