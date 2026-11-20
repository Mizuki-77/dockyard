# 补加 11in75-mk1 的图片条目（上一轮下载失败，fragment 里没有它）。
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'

BLOCK = """  - id: 11in75-mk1-primary
    file: /img/weapons/11in75-mk1-primary.jpg
    subject: weapon:11in75-mk1
    title:
      zh: 大黄蜂号上的四联 1.1"/75 高炮正在射击
      en: 'Quad 1.1"/75 mount firing aboard USS Hornet (CV-8)'
    part: mount
    view: three_quarter
    date: 1942-05
    license: pd
    license_tier: A
    license_raw: 'Public domain'
    author: 'U.S. Navy'
    credit: 'U.S. Navy / NHHC'
    source_url: "https://commons.wikimedia.org/wiki/File:28_mm_Flak_USS_Hornet_(CV-8)_May_1942.jpg"
    width: 500
    height: 383
    primary: true
    note: >-
      1942 年 5 月，大黄蜂号（CV-8）上的四联 28 mm（1.1"/75）Mk 1 高炮正在射击，
      与本项目收录的大黄蜂号直接对应。这是全站分辨率最低的一张主图（原图仅 795x609），
      找不到更高分辨率的该型在舰上使用的照片。
"""

text = io.open(IMG, encoding='utf-8').read()

if 'id: 11in75-mk1-primary' in text:
    print('已存在，跳过')
else:
    # 插到 a6m2-primary 之前（保持武器图成组）
    anchor = '  - id: a6m2-primary'
    i = text.find(anchor)
    if i < 0:
        print('找不到插入锚点')
        raise SystemExit(1)
    text = text[:i] + BLOCK + text[i:]
    io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
    print('已插入 11in75-mk1-primary')

# 验证
import yaml
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print('图片数:', len(d['images']))
newids = [x['id'] for x in d['images'] if str(x['id']).endswith('-primary')]
print('新增图:', len(newids))
for i in sorted(newids):
    print('  ', i)
