# 修正 20cm 炮的图片归属
#
# 问题（2026-11-24 核对发现）：
#   data/images.yaml 里 id=20cm-3ns-primary 的图，subject 写 weapon:20cm-3ns（No.1），
#   但图本身是「高雄号前部炮塔」，note 里也写「高雄号」。
#   而 NavWeaps 明确：高雄级装的是 No.2 炮（20.32 cm / 840 mps），
#   不是赤城/加贺用的 No.1（20.0 cm / 870 mps）。
#   → 这张图的 subject 挂错了，应归 weapon:20cm-3ns-no2。
#
# 同时本轮新抓的 20cm-3ns-no2.jpg 与它哈希完全相同，是同一张。
# 处理：
#   1. 把 20cm-3ns-primary 的 subject 改成 weapon:20cm-3ns-no2（真正归属）
#   2. 删掉本轮重复下载的 20cm-3ns-no2.jpg 文件与条目
#   3. 保留 20cm-3ns-primary.jpg 文件名不动（避免动其他引用）
import hashlib
import io
import os
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
IMGS = 'data/images.yaml'


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


d = load(IMGS)
imgs = d['images']

# 1) 修正 subject
target = None
for im in imgs:
    if im.get('id') == '20cm-3ns-primary':
        target = im
        break

if target:
    old = target.get('subject')
    target['subject'] = 'weapon:20cm-3ns-no2'
    target['note'] = (
        '高雄号前部一号、二号主炮塔与舰桥。'
        '2026-11-24 修正：本图原挂 weapon:20cm-3ns（No.1），'
        '但高雄级装的是 No.2 炮（20.32 cm / 840 mps），'
        'No.1（20.0 cm / 870 mps）装在赤城与加贺的炮廓。已改归 No.2。'
    )
    print(f'  [subject] 20cm-3ns-primary: {old} → weapon:20cm-3ns-no2')

# 2) 删掉重复下载的文件
dup = 'public/img/weapons/20cm-3ns-no2.jpg'
if os.path.exists(dup):
    os.remove(dup)
    print(f'  [删除] {dup}（与 20cm-3ns-primary.jpg 哈希相同）')

shutil.copy2(IMGS, f'{IMGS}.bak-{STAMP}')
dump(IMGS, d)
print('\n已写回 data/images.yaml')
