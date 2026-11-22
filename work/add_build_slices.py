# 为 13 艘舰补「建造与舾装」前置切片。
#
# 为什么要补：时间轴的范围由 fact 决定（如提尔皮茨最早 fact 在 1936-06-14 开工），
# 但切片是「给人看的标签」，之前都从服役前后开始，导致时间轴左端有一大段
# 没有任何切片的高亮区 —— 拖动滑块时下方一片空白，读者以为数据缺失。
#
# 切片代码统一用 <现有首片代码前加 0>，例如 akagi 的 A0 → A00，
# 这样既保持排序，也不与现有代码冲突。
import glob
import io
import os
import re

import yaml


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8')) or {}


ships = {}
for p in glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    ships[os.path.basename(p)[:-5]] = load(p)

classes = {}
for p in glob.glob('data/classes/*.yaml'):
    if '.bak' in p:
        continue
    classes[os.path.basename(p)[:-5]] = load(p)


def build_info(sid, ship):
    """抽取建造相关的节点文字。"""
    facts = (ship.get('facts') or []) + \
            (classes.get(ship.get('class'), {}).get('facts') or [])
    out = {}
    for f in facts:
        fld = str(f.get('field') or '')
        if not fld.startswith('construction.'):
            continue
        v = f.get('value')
        a = str((f.get('valid') or {}).get('from') or '')
        if fld == 'construction.order_date':
            out['order'] = (str(v), a)
        elif fld == 'construction.laid_down':
            out['laid'] = (str(v), a)
        elif fld == 'construction.launched':
            out['launch'] = (str(v), a)
        elif fld == 'construction.builder':
            out['builder'] = (str(v), a)
        elif fld == 'construction.builder_location':
            out['where'] = (str(v), a)
    return out


CHANGES = []

for sid, ship in ships.items():
    sp = f'data/slices/{sid}.yaml'
    if not os.path.exists(sp):
        continue
    sd = load(sp)
    sl = sd.get('slices') or []
    if not sl:
        continue

    facts = (ship.get('facts') or []) + \
            (classes.get(ship.get('class'), {}).get('facts') or [])
    cands = [
        str((f.get('valid') or {}).get('from') or '')
        for f in facts
        if str(f.get('field') or '').startswith('construction.')
        and not f.get('about')
        and re.match(r'^\d{4}', str((f.get('valid') or {}).get('from') or ''))
    ]
    if not cands:
        continue
    earliest = min(cands)
    first_from = str(sl[0].get('from') or '')
    if earliest[:4] >= first_from[:4]:
        continue
    if int(first_from[:4]) - int(earliest[:4]) < 1:
        continue

    # 已经补过就跳过
    if str(sl[0].get('code', '')).endswith('00'):
        continue

    info = build_info(sid, ship)
    name = (ship.get('name') or {}).get('zh') or sid
    parts = []
    if 'order' in info:
        parts.append(f"{info['order'][1][:10]} 订购")
    if 'laid' in info:
        parts.append(f"{info['laid'][0]} 开工")
    if 'builder' in info:
        w = info.get('where', ('', ''))[0]
        parts.append(f"承造 {info['builder'][0]}{('（' + w + '）') if w else ''}")
    if 'launch' in info:
        parts.append(f"{info['launch'][0]} 下水")

    note = '；'.join(parts) if parts else '建造期'
    note = (note + '。\n      这一段此前在时间轴上没有切片，拖动滑块时下方空白，'
                   '补上后与 fact 的时间范围对齐。').replace('\n       ', '\n      ')

    new_slice = {
        'code': str(sl[0].get('code', 'X0')) + '0',
        'title': '订购与建造',
        'from': earliest[:10],
        'to': _prev_day(first_from) if False else None,
        'note': note,
    }
    CHANGES.append((sid, sp, new_slice, first_from))

print(f'待补 {len(CHANGES)} 艘：')
for sid, sp, ns, ff in CHANGES:
    print(f"  {sid:<14} {ns['code']:<5} {ns['from']} ~ ?  （现有首片从 {ff} 开始）")
