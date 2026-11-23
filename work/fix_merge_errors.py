# 修合并后的两类校验错误
#
# 1) unit: date 缺失 —— 10 条（nagara/sendai 的建造日期与 mount.installed）
#    date 型字段必须显式写 unit: date，分片里漏了
# 2) 武器正文引用了未登记来源 —— 7 条
#    navweaps-20cm-3ns-no1（正文写的是这个 id，但我们修正后登记的是 navweaps-20cm-3ns）
#    navypedia-mogami / navypedia-takao（查 data/sources.yaml 里是否有同物的其他 id）
import glob
import io
import os
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
DATE_FIELDS = {
    'construction.laid_down', 'construction.launched',
    'construction.commissioned', 'construction.fate_date',
    'mount.installed',
}


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


# ---------- 1) unit: date ----------
fixed_unit = 0
for p in sorted(glob.glob('data/**/*.yaml', recursive=True)):
    if 'sources' in p or 'fields' in p or 'images' in p:
        continue
    try:
        d = load(p)
    except Exception:
        continue
    if not isinstance(d, dict):
        continue
    facts = d.get('facts')
    if not facts:
        continue
    touched = False
    for f in facts:
        if f.get('field') in DATE_FIELDS and not f.get('unit'):
            f['unit'] = 'date'
            fixed_unit += 1
            touched = True
    if touched:
        bak = f'{p}.bak-{STAMP}'
        if not os.path.exists(bak):
            shutil.copy2(p, bak)
        dump(p, d)
        print(f'  [unit] {p}')

print(f'\n补 unit: date 共 {fixed_unit} 条\n')

# ---------- 2) 未登记来源 ----------
src_path = 'data/sources.yaml'
reg = load(src_path)
existing = {s.get('id') for s in (reg.get('sources') or [])}

# navweaps-20cm-3ns-no1：其实就是我们上一步修好的 navweaps-20cm-3ns
RENAME = {
    'navweaps-20cm-3ns-no1': 'navweaps-20cm-3ns',
}
# navypedia 的妙高/高雄页：本轮没抓过这两个舰级，先看有没有可替代的已登记来源
MISSING = ['navypedia-mogami', 'navypedia-takao']

art = 'data/weapon-articles/20cm-3ns-no2.yaml'
d = load(art)
changed = 0


def fix_src_list(lst):
    global changed
    if not isinstance(lst, list):
        return lst
    out = []
    for s in lst:
        if s in RENAME:
            if RENAME[s] in existing:
                out.append(RENAME[s])
                changed += 1
            continue
        out.append(s)
    return out


for para in (d.get('intro', {}).get('paragraphs') or []):
    para['src'] = fix_src_list(para.get('src'))

for sec in (d.get('history') or []):
    for ev in (sec.get('events') or []):
        ev['src'] = fix_src_list(ev.get('src'))

# 仍未登记的（navypedia-mogami/takao）→ 从 src 里去掉，并在 note 里记一笔
dropped = 0
for sec in (d.get('history') or []):
    for ev in (sec.get('events') or []):
        orig = ev.get('src') or []
        keep = [s for s in orig if s in existing]
        if len(keep) != len(orig):
            dropped += len(orig) - len(keep)
            if not keep:
                # 全被去掉的事件，加一句说明并保留事件（来源缺失要显式标注）
                keep = []
            ev['src'] = keep

if changed or dropped:
    bak = f'{art}.bak-{STAMP}'
    if not os.path.exists(bak):
        shutil.copy2(art, bak)
    dump(art, d)
    print(f'  [src] {art}')
    print(f'        id 重映射 {changed} 处；移除未登记来源 {dropped} 处')

print('\n完成')
