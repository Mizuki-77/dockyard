import glob
import io
import os

import yaml


def zh(v):
    if isinstance(v, dict):
        return v.get('zh') or v.get('en') or ''
    return str(v)


known = set()
for p in glob.glob('data/ships/*.yaml'):
    if '.bak' not in p:
        known.add(os.path.basename(p)[:-5])

for p in sorted(glob.glob('data/battles/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    bid = os.path.basename(p)[:-5]

    total = 0
    linked = 0
    unlinked_names = []
    for side in d.get('belligerents') or []:
        for s in side.get('ships') or []:
            total += 1
            sid = s.get('ship_id')
            if sid and sid in known:
                linked += 1
            else:
                unlinked_names.append((s.get('name'), sid))

    tl = len(d.get('timeline') or [])
    hits = len(d.get('hits_received') or [])
    imgs = 0
    ip = 'data/images.yaml'
    if os.path.exists(ip):
        im = yaml.safe_load(io.open(ip, encoding='utf-8')) or {}
        imgs = len([x for x in im.get('images') or []
                    if x.get('subject') == f'battle:{bid}'])

    print(f'--- {bid}  ({zh(d.get("name"))}) ---')
    print(f'  参战舰: {total}  已挂 ship_id 且入库: {linked}  未挂: {total - linked}')
    print(f'  时间轴 {tl} 条 / 命中 {hits} 条 / 图 {imgs} 张')
    for nm, sid in unlinked_names:
        mark = '（本站已有此舰）' if sid in known else ''
        print(f'    未挂: {nm}  ship_id={sid} {mark}')
    print()
