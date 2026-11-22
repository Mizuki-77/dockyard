# 为缺少建造期切片的舰补一个前置切片。
#
# 为什么要补：时间轴的范围由 fact 决定（如提尔皮茨最早 fact 在 1936-06-14 开工），
# 但切片是「给人看的标签」，之前都从服役前后开始，导致时间轴左端有一大段
# 没有任何切片的高亮区 —— 拖动滑块时下方一片空白，读者以为数据缺失。
#
# 切片代码用「现有首片代码 + 0」，例如 A0 → A00，保持排序且不冲突。
import datetime
import glob
import io
import os
import re
import subprocess

import yaml


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8')) or {}


def prev_day(datestr):
    """YYYY-MM-DD 的前一天；不合法就原样返回。"""
    try:
        d = datetime.date.fromisoformat(datestr[:10])
        return (d - datetime.timedelta(days=1)).isoformat()
    except Exception:
        return datestr


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


def build_note(sid, ship):
    facts = (ship.get('facts') or []) + \
            (classes.get(ship.get('class'), {}).get('facts') or [])
    g = {}
    for f in facts:
        fld = str(f.get('field') or '')
        if not fld.startswith('construction.'):
            continue
        v = str(f.get('value') or '')
        if fld == 'construction.builder':
            g['builder'] = v
        elif fld == 'construction.builder_location':
            g['where'] = v
        elif fld == 'construction.order_date':
            g['order'] = v
        elif fld == 'construction.laid_down':
            g['laid'] = v
        elif fld == 'construction.launched':
            g['launch'] = v

    parts = []
    if g.get('order'):
        parts.append(f"{g['order']} 订购")
    if g.get('laid'):
        parts.append(f"{g['laid']} 开工")
    if g.get('builder'):
        w = f"（{g['where']}）" if g.get('where') else ''
        parts.append(f"承造 {g['builder']}{w}")
    if g.get('launch'):
        parts.append(f"{g['launch']} 下水")
    body = '；'.join(parts) if parts else '建造期'
    return body + '。'


def main():
    todo = []
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
        if not re.match(r'^\d{4}', first_from):
            continue
        if earliest[:4] >= first_from[:4]:
            continue
        if int(first_from[:4]) - int(earliest[:4]) < 1:
            continue
        if str(sl[0].get('code', '')).endswith('00'):
            continue  # 已补过

        todo.append({
            'sid': sid,
            'path': sp,
            'from': earliest[:10],
            'to': prev_day(first_from),
            'code': str(sl[0].get('code')) + '0',
            'note': build_note(sid, ship),
        })

    print(f'需要补 {len(todo)} 艘\n')
    for t in todo:
        print(f"  {t['sid']:<14} {t['code']:<5} {t['from']} ~ {t['to']}")

    if not todo:
        return

    print('\n开始写入...')
    for t in todo:
        sp = t['path']
        text = io.open(sp, encoding='utf-8').read()
        # 插到第一个 "  - code:" 之前
        m = re.search(r'^  - code: ', text, re.M)
        if not m:
            print(f"  ✗ {t['sid']}: 找不到插入点")
            continue
        block = (
            f"  - code: {t['code']}\n"
            f"    title: 订购与建造\n"
            f"    from: {t['from']}\n"
            f"    to: {t['to']}\n"
            f"    note: >-\n"
            f"      {t['note']}\n"
            f"      这一段此前在时间轴上没有切片，拖动滑块时下方是空白的；\n"
            f"      补上后切片范围与 fact 的实际时间范围对齐。\n\n"
        )
        text = text[:m.start()] + block + text[m.start():]
        io.open(sp, 'w', encoding='utf-8', newline='\n').write(text)
        print(f"  ✓ {t['sid']}")

    print('\n验证 YAML：')
    for t in todo:
        try:
            d = load(t['path'])
            print(f"  {t['sid']:<14} {len(d.get('slices') or [])} 片  OK")
        except Exception as e:
            print(f"  {t['sid']:<14} YAML 错误: {e}")


if __name__ == '__main__':
    main()
