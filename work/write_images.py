# 把 189 张舰图写入 data/images.yaml
#
# 用文本追加而非 safe_dump 整篇重写 —— 上次用 safe_dump 把 18 行注释抹掉了
# （docs/52 §3.1 记录的事故），这次必须保留注释。
import io
import os
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
IMGS = 'data/images.yaml'

d = yaml.safe_load(io.open('work/_ship_images_apply.yaml', encoding='utf-8'))['ships']
text = io.open(IMGS, encoding='utf-8').read()

# 已登记的 id 集合
existing = yaml.safe_load(text)
have_ids = {im.get('id') for im in existing['images']}

SHIP_ZH = {
    'tone': '利根号', 'chikuma': '筑摩号', 'haruna': '榛名号', 'kirishima': '雾岛号',
    'hosho': '凤翔号', 'nagara': '长良号', 'sendai': '川内号', 'astoria': '阿斯托里亚号',
    'portland': '波特兰号', 'minneapolis': '明尼阿波利斯号', 'new-orleans': '新奥尔良号',
    'vincennes': '文森斯号', 'northampton': '北安普敦号', 'pensacola': '彭萨科拉号',
    'atlanta': '亚特兰大号', 'hammann': '哈曼号', 'monaghan': '莫纳汉号',
    'benham': '本汉号',
}

lines = ['', '  # ===== 2026-11-25 新增：中途岛扩编 18 艘舰的配图 =====',
         '  # 全部 A 档（PD/CC0），Commons 分类按 Category 浏览抓取。',
         '  # 每舰第一张标 primary。主体判定：Commons 原名或描述首选主体为本舰，',
         '  # 已剔除舰队合影、友舰视角、同级的其他舰（详见 work/decide_images.py）。', '']

added = 0
for sid, items in d.items():
    zh = SHIP_ZH.get(sid, sid)
    for i, it in enumerate(items):
        iid = f'{sid}-{i+1:02d}'
        if iid in have_ids:
            continue
        title_zh = f'{zh}（第 {i+1} 张）'
        title_en = str(it.get('commons_title', '')).replace('File:', '').rsplit('.', 1)[0]
        descr = str(it.get('descr') or '').replace("'", "''").replace('\n', ' ')[:200]
        lines.append(f"  - id: '{iid}'")
        lines.append(f"    file: '{it['file']}'")
        lines.append(f"    subject: ship:{sid}")
        lines.append(f"    title:")
        lines.append(f"      zh: '{title_zh}'")
        lines.append(f"      en: '{title_en[:90]}'")
        lines.append(f"    license: pd")
        lines.append(f"    license_tier: A")
        lines.append(f"    license_raw: '{str(it.get('license_raw') or 'Public domain').replace(chr(39), chr(39)*2)}'")
        au = str(it.get('author') or '').replace("'", "''")[:100]
        lines.append(f"    author: '{au}'")
        lines.append(f"    source_url: '{str(it.get('source_url') or '')}'")
        if it.get('width'):
            lines.append(f"    width: {it['width']}")
        if it.get('height'):
            lines.append(f"    height: {it['height']}")
        if i == 0:
            lines.append(f"    primary: true")
        if descr:
            lines.append(f"    note: '{descr}'")
        lines.append('')
        added += 1

new_text = text.rstrip('\n') + '\n' + '\n'.join(lines)

# 校验能解析
chk = yaml.safe_load(new_text)
print(f'追加 {added} 条，图片总数 {len(chk["images"])}')

shutil.copy2(IMGS, f'{IMGS}.bak-{STAMP}')
with io.open(IMGS, 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_text)
print('已写入 data/images.yaml')
print('PRELOAD 保留:', 'PRELOAD' in new_text)
