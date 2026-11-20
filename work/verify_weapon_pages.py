# 验证 12 型武器的页面现在都有图有正文。
import io
import re
import os

IDS = ['a6m2', 'd3a1', 'b5n2', '25mm-96', '20cm-3ns', '12cm-10ns',
       '127cm-89', '5in38-mk12', '11in75-mk1', 'f4f-wildcat', 'sbd-dauntless',
       'tbd-devastator']

print(f'{"武器":<16} {"页":<6} {"主图":<6} {"简介段":<7} {"历史节":<7} {"来源块"}')
print('-' * 60)

for wid in IDS:
    p = f'dist/weapons/{wid}/index.html'
    if not os.path.exists(p):
        print(f'{wid:<16} 页面缺失')
        continue
    h = io.open(p, encoding='utf-8').read()

    # 主图：hero 区是否有 <img>
    has_hero = 'weapon-hero' in h or 'hero' in h.lower()
    # 更准确：看是否有指向该武器图的 img
    has_img = bool(re.search(r'<img[^>]+src="/img/weapons/' + re.escape(wid), h))

    # 正文：简介段落数（prose__p 或 article 段落）
    paras = len(re.findall(r'class="prose__p"', h))
    # 历史事件数
    events = len(re.findall(r'class="weapon-history__item|class="timeline__item|class="ev__', h))

    # 来源块数
    srcblocks = len(re.findall(r'class="srcblock"', h))

    print(f'{wid:<16} {"OK" if True else "":<6} {"YES" if has_img else "NO":<6} {paras:<7} {"?":<7} {srcblocks}')

print()
# 反查：有没有图片文件没被任何页面引用
print('=== 12 张主图是否都被页面引用 ===')
for wid in IDS:
    p = f'dist/weapons/{wid}/index.html'
    if not os.path.exists(p):
        continue
    h = io.open(p, encoding='utf-8').read()
    fn = f'/img/weapons/{wid}-primary.jpg'
    print(f'  {wid:<16} {"引用" if fn in h else "未引用"}')
