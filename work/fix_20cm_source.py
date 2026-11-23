# 修复 navweaps-20cm-3ns 来源错配
#
# 问题：2026-11-19 登记时把两门炮搞混了。
#   id      = navweaps-20cm-3ns
#   title   = "20 cm/50 (7.9") 3rd Year Type"        ← No.1 的口径与标题
#   url     = WNJAP_8-50_3ns.htm                     ← No.2 的页面
#   引用者  = data/ships/akagi.yaml(11) + kaga.yaml(5)，数据 bore=200 / mv=870 → 全是 No.1
#
# 2026-11-24 实测两个页面都存在且独立：
#   WNJAP_79-50_3ns.htm → "Japan 20 cm/50 (7.9") 3rd Year Type No. 1"
#   WNJAP_8-50_3ns.htm  → "Japan 20 cm/50 (8") 3rd Year Type No. 2"
#
# 修法（不动任何 fact 的 src 引用）：
#   1. 原 id `navweaps-20cm-3ns` 的 url 改成 No.1 的正确页面 —— 保持 16 条 fact 的引用继续有效
#   2. 新增 `navweaps-20cm-3ns-no2` 指向 No.2 页面 —— 供利根级等使用
import io
import shutil
from datetime import datetime

import yaml

SRC = 'data/sources.yaml'
STAMP = datetime.now().strftime('%Y-%m-%d')
URL_NO1 = 'https://www.navweaps.com/Weapons/WNJAP_79-50_3ns.htm'
URL_NO2 = 'https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.htm'


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


d = load(SRC)
sources = d['sources']
by_id = {s.get('id'): s for s in sources}

old = by_id.get('navweaps-20cm-3ns')
assert old, 'navweaps-20cm-3ns 不存在'

print('修正前：')
print('  title:', old.get('title'))
print('  url  :', old.get('url'))

# 1) 原记录改成货真价实的 No.1
old['title'] = 'Japanese 20 cm/50 (7.9") 3rd Year Type No. 1 — NavWeaps'
old['url'] = URL_NO1
old['note'] = (
    'No.1（1 GÔ）炮。实弹径 20.0 cm、初速 870 mps，赤城与加贺的炮廓炮即此型，'
    '妙高级亦曾使用。2026-11-24 修正：本记录原 url 误指 No.2 页面'
    '（WNJAP_8-50_3ns.htm），标题却写 No.1 口径；两门炮是独立页面，已更正。'
    'No.2 另见 navweaps-20cm-3ns-no2。'
)

# 2) 补一条真正的 No.2
if 'navweaps-20cm-3ns-no2' not in by_id:
    no2 = {
        'id': 'navweaps-20cm-3ns-no2',
        'title': 'Japanese 20 cm/50 (8") 3rd Year Type No. 2 — NavWeaps',
        'url': URL_NO2,
        'type': 'website',
        'tier': 'C',
        'role': ['data'],
        'operator': 'navweaps.com',
        'lang': 'en',
        'access': 'direct',
        'fetched': '2026-11-24',
        'license': 'all_rights_reserved',
        'note': (
            'No.2（2 GÔ）炮。实弹径 20.32 cm、初速 840 mps，'
            '装备妙高/高雄/利根级重巡。1931-04-06 采用，No.1 的序号即因它而补。'
            '「三年式」指大正三年（1914），但本型设计在 1930-31 年。'
        ),
    }
    sources.append(no2)
    print('\n已新增 navweaps-20cm-3ns-no2')

bak = f'{SRC}.bak-{STAMP}'
shutil.copy2(SRC, bak)
d['updated'] = STAMP
dump(SRC, d)

print('\n修正后：')
d2 = load(SRC)
for s in d2['sources']:
    if str(s.get('id', '')).startswith('navweaps-20cm-3ns'):
        print(f'  {s["id"]}')
        print(f'      title: {s.get("title")}')
        print(f'      url  : {s.get("url")}')
print(f'\n备份：{bak}')
print(f'来源总数：{len(d2["sources"])}')
