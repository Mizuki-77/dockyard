# 逐个核对「切片未覆盖」的那些 fact 到底是什么。
# 判断标准：如果是设计案/订购/命名这类 identity.* 事实，就不该有切片
# （框架里明确排除了 identity.* 参与时间轴计算）。
import glob
import io
import os
import re

import yaml


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8')) or {}


CASES = [
    ('akagi', '1920'), ('bismarck', '1934'), ('enterprise', '1933'),
    ('hiryu', '1932'), ('hood', '1916'), ('hornet', '1934'),
    ('illustrious', '1930'), ('kaga', '1920'), ('king-george-v', '1936'),
    ('prince-of-wales', '1936'), ('prinz-eugen', '1935'), ('soryu', '1934'),
    ('tirpitz', '1934'), ('yorktown', '1933'),
]

for sid, yr in CASES:
    ship = load(f'data/ships/{sid}.yaml')
    cls_id = ship.get('class')
    cls = load(f'data/classes/{cls_id}.yaml') if cls_id else {}
    facts = (ship.get('facts') or []) + (cls.get('facts') or [])

    hits = []
    for f in facts:
        v = f.get('valid') or {}
        a = str(v.get('from') or '')
        if a.startswith(yr):
            hits.append((f.get('field'), a, str(v.get('to') or '')))
    print(f'{sid} ({yr}):')
    for field, a, b in hits[:4]:
        mark = 'identity.* 不算时间轴' if field.startswith('identity.') else '⚠ 非 identity'
        print(f'   {field:<32} {a} ~ {b or "open"}   {mark}')
    if not hits:
        print('   (没找到)')
    print()
