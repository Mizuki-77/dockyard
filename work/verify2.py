# 用正确的 class 名重查 12 型页面的正文渲染情况。
import io
import os
import re

IDS = ['a6m2', 'd3a1', 'b5n2', '25mm-96', '20cm-3ns', '12cm-10ns',
       '127cm-89', '5in38-mk12', '11in75-mk1', 'f4f-wildcat', 'sbd-dauntless',
       'tbd-devastator']

print(f'{"武器":<16} {"图":<4} {"简介段":<6} {"历史条":<6} {"字符数":<8} {"来源块"}')
print('-' * 62)

bad = []
for wid in IDS:
    p = f'dist/weapons/{wid}/index.html'
    if not os.path.exists(p):
        bad.append((wid, '页面缺失'))
        continue
    h = io.open(p, encoding='utf-8').read()

    img = f'/img/weapons/{wid}-primary.jpg' in h
    paras = len(re.findall(r'class="prose__block"', h))
    events = len(re.findall(r'class="(?:ev|history__item|timeline__item|wy__item)[^"]*"', h))
    srcs = len(re.findall(r'class="srcblock"', h))

    # 正文纯文字量（粗略：去掉标签）
    body = re.search(r'<main.*?</main>', h, re.S)
    text_len = len(re.sub(r'<[^>]+>', '', body.group(0))) if body else 0

    print(f'{wid:<16} {"Y" if img else "N":<4} {paras:<6} {events:<6} {text_len:<8} {srcs}')

    if not img:
        bad.append((wid, '无主图'))
    if paras < 2:
        bad.append((wid, f'简介段只有 {paras}'))

print()
if bad:
    print('问题：')
    for w, why in bad:
        print(f'  {w}: {why}')
else:
    print('全部 12 型：有主图、简介 >=2 段')
