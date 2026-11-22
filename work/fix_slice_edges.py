# 修两个切片的边界问题。
#   1. enterprise：补 1943-11 至 1960 的战后切片
#   2. illustrious：I00 起点应取最早 fact（1936-07-08 参谋要求定稿）
import io
import os
import re

import yaml


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8')) or {}


# ---------------------------------------------------------------- enterprise
p = 'data/slices/enterprise.yaml'
text = io.open(p, encoding='utf-8').read()
if 'E7' not in text:
    # 在文件末尾的 slices 之下追加
    add = """  - code: E7
    title: 战后
    from: 1943-11-01
    to: 1947-02-17
    note: >-
      1943-11 大改装后编入快速航母部队，参加马里亚纳、莱特湾、硫磺岛。
      1945-05-14 被神风撞中前升降机、退出战斗，战后担任运兵船。
      1947-02-17 退役。涂装 Measure 21/22 海军蓝体系。
      这一段此前没有切片，时间轴上 1943-11 之后一直是空白。

  - code: E8
    title: 封存与拆解
    from: 1947-02-18
    to: 1960-07-01
    note: >-
      1947-02-17 退役封存于纽约。多次试图保存为博物馆舰未果，
      1958-07 售出、1958-10 拆解开工，1960 年拆解完毕。
      Navy 曾在一份 1947 年的评估里把她列为「不应保存」的那一类。
"""
    text = text.rstrip() + '\n\n' + add
    io.open(p, 'w', encoding='utf-8', newline='\n').write(text)
    print('enterprise: 已补 E7 / E8')
else:
    print('enterprise: E7 已存在')

# ---------------------------------------------------------------- illustrious
p2 = 'data/slices/illustrious.yaml'
t2 = io.open(p2, encoding='utf-8').read()
m = re.search(r'(  - code: I00\n    title: 订购与建造\n    from: )([\d-]+)', t2)
if m:
    old = m.group(2)
    if old != '1936-07-08':
        t2 = t2[:m.start(2)] + '1936-07-08' + t2[m.end(2):]
        io.open(p2, 'w', encoding='utf-8', newline='\n').write(t2)
        print(f'illustrious: I00 起点 {old} -> 1936-07-08')
    else:
        print('illustrious: I00 起点已是 1936-07-08')
else:
    print('illustrious: 找不到 I00')

print()
for sid in ['enterprise', 'illustrious']:
    d = load(f'data/slices/{sid}.yaml')
    sl = d.get('slices') or []
    print(f'{sid}: {len(sl)} 片，{sl[0].get("from")} ~ {sl[-1].get("to")}')
