# 登记 navypedia 的妙高/高雄页，补回武器正文缺 src 的两条事件
#
# 背景：合并时 20cm-3ns-no2.yaml 里 events[3] 与 events[7] 引用了
# navypedia-takao / navypedia-mogami，但这两个来源从未登记，被我剥掉了，
# 结果两条事件缺 src 校验失败。
# 2026-11-24 实测两页真实存在（TAKAO heavy cruisers 1932 / MOGAMI 1935-1937），
# 正确做法是补登记来源，而不是删事件。
import io
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
SRC_PATH = 'data/sources.yaml'
ART = 'data/weapon-articles/20cm-3ns-no2.yaml'

NEW = [
    {
        'id': 'navypedia-takao',
        'title': 'TAKAO heavy cruisers (1932) — Navypedia',
        'url': 'https://www.navypedia.org/ships/japan/jap_cr_takao.htm',
        'type': 'website',
        'tier': 'D',
        'role': ['data', 'narrative'],
        'operator': 'navypedia.org',
        'lang': 'en',
        'access': 'direct',
        'fetched': '2026-11-24',
        'license': 'all_rights_reserved',
        'note': '高雄级重巡（高雄/爱宕/鸟海/摩耶）逐舰技术数据与结局。20 cm No.2 炮的主要装舰级。',
    },
    {
        'id': 'navypedia-mogami',
        'title': 'MOGAMI light / heavy cruisers (1935 - 1937) — Navypedia',
        'url': 'https://www.navypedia.org/ships/japan/jap_cr_mogami.htm',
        'type': 'website',
        'tier': 'D',
        'role': ['data', 'narrative'],
        'operator': 'navypedia.org',
        'lang': 'en',
        'access': 'direct',
        'fetched': '2026-11-24',
        'license': 'all_rights_reserved',
        'note': '最上级（最上/三隈/铃谷/熊野）轻巡→重巡改装记录。15.5 cm 换 20 cm No.2 的关键案例。',
    },
]


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


reg = load(SRC_PATH)
existing = {s.get('id') for s in reg['sources']}
added = 0
for s in NEW:
    if s['id'] not in existing:
        reg['sources'].append(s)
        existing.add(s['id'])
        added += 1
        print(f'  + 登记 {s["id"]}')
reg['updated'] = STAMP
shutil.copy2(SRC_PATH, f'{SRC_PATH}.bak2-{STAMP}')
dump(SRC_PATH, reg)
print(f'\n新登记来源 {added} 条，总数 {len(reg["sources"])}')

# 补回事件 src
d = load(ART)
TARGET = {
    3: ['navypedia-takao', 'navypedia-mogami'],
    7: ['navypedia-takao'],
}
for sec in d['history']:
    if sec.get('id') != 'war-and-fate':
        continue
    for i, ev in enumerate(sec['events']):
        if i in TARGET and not ev.get('src'):
            ev['src'] = TARGET[i]
            print(f'  [src] events[{i}] ← {TARGET[i]}')

shutil.copy2(ART, f'{ART}.bak2-{STAMP}')
dump(ART, d)
print('\n完成')
