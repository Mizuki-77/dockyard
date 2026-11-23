# 从干净备份恢复 images.yaml，并在恢复后的文件上重做两处修正
#
# 事故原因：2026-11-24 我用 yaml.safe_dump 整篇重写 data/images.yaml，
# safe_dump 会丢掉所有 YAML 注释 —— 包括文件头部那段授权三档规则说明
# （A/B/C 档、IWM 判例），以及 6 张 PRELOAD 预存素材的标记。
# 这是不该犯的：改 YAML 应该用 edit 做定点替换，不能整篇 dump。
#
# 本脚本：
#   1. 从 data/images.yaml.bak-2026-11-24（425017 字节，含 PRELOAD，未被污染）恢复
#   2. 在恢复后的文本上做两次定点文本替换（不用 safe_dump）：
#      a) 20cm-3ns-primary 的 subject 改为 weapon:20cm-3ns-no2
#      b) 追加本轮 6 条已验过的武器配图
#   3. 保留全部注释
import io
import os
import re
import shutil
from datetime import datetime

STAMP = datetime.now().strftime('%Y-%m-%d')
IMGS = 'data/images.yaml'
CLEAN = 'data/images.yaml.bak-2026-11-24'

src = io.open(CLEAN, encoding='utf-8').read()
assert 'PRELOAD' in src, '备份里没有 PRELOAD，选错了备份'
assert src.count('- id:') >= 520, f'备份条目数异常: {src.count("- id:")}'
print(f'从 {CLEAN} 恢复：{len(src)} 字节，{src.count("- id:")} 条，'
      f'{sum(1 for l in src.split(chr(10)) if l.strip().startswith("#"))} 行注释')

# ---- a) 修 20cm-3ns-primary 的 subject
# 在文本里找到那个条目的 subject 行并替换（限定在该 id 之后的 20 行内）
m = re.search(r"- id: '20cm-3ns-primary'", src)
if m:
    start = m.start()
    window = src[start:start + 1500]
    if 'subject: weapon:20cm-3ns\n' in window:
        new_window = window.replace('subject: weapon:20cm-3ns\n',
                                    'subject: weapon:20cm-3ns-no2\n', 1)
        src = src[:start] + new_window + src[start + 1500:]
        print('  [subject] 20cm-3ns-primary → weapon:20cm-3ns-no2')
    else:
        print('  ! 没找到 subject 行，跳过')

# ---- b) 追加 6 条武器配图（写成 YAML 文本，保持与现有风格一致）
APPEND = """
  # ===== 2026-11-24 新增：本轮武器的配图（人眼逐张确认过题材） =====
  # 判定依据见 work/add_weapon_images.py 顶部注释。
  # 被否决的 4 张（8in-55-mk9 的破损舰首、14cm-50-3ns 的塔拉瓦岸炮、
  # 21in-mk15 的 1953 年照片、重复的 20cm 炮图）没有登记，文件也已删除。

  - id: 'weapon-5in25-mk10-northampton'
    file: '/img/weapons/5in25-mk10.jpg'
    subject: weapon:5in25-mk10
    title:
      zh: '北安普敦号的 5 英寸/25 倍径炮向韦贾环礁射击（1942-02-01）'
      en: '127 mm guns aboard USS Northampton (CA-26) firing on Wotje, 1 February 1942'
    part: mount
    view: side
    date: '1942-02-01'
    license: pd
    license_tier: A
    license_raw: 'Public domain'
    author: 'US Navy'
    credit: '美国国家档案馆'
    source_url: 'https://commons.wikimedia.org/wiki/File:127_mm_guns_aboard_USS_Northampton_(CA-26)_firing_on_Wotje_on_1_February_1942.jpg'
    width: 1280
    height: 947
    primary: true
    note: '舰上实拍，可清楚看到 5"/25 的单装开放式炮座与装填手位置。中途岛时七艘美军重巡装的都是这一型。'

  - id: 'weapon-a5m4-claude'
    file: '/img/weapons/a5m4.jpg'
    subject: weapon:a5m4
    title:
      zh: '九六式舰战 A5M（9-122 涂装）'
      en: 'Mitsubishi A5M Claude fighter, coded 9-122'
    part: aircraft
    view: three_quarter
    date: '1930s'
    license: pd
    license_tier: A
    license_raw: 'Public domain'
    author: '日本海軍'
    source_url: 'https://commons.wikimedia.org/wiki/File:A5M_Claude.jpg'
    width: 421
    height: 195
    primary: true
    note: '九六式舰战实机。凤翔号在中途岛前后搭载过这一型。'

  - id: 'weapon-b4y1-jean'
    file: '/img/weapons/b4y1.jpg'
    subject: weapon:b4y1
    title:
      zh: '九六式舰攻 B4Y1'
      en: 'Yokosuka B4Y1 Jean carrier attack aircraft'
    part: aircraft
    view: three_quarter
    date: '1930s'
    license: pd
    license_tier: A
    license_raw: 'Public domain'
    author: '日本海軍'
    source_url: 'https://commons.wikimedia.org/wiki/File:96siki-kankou.jpg'
    width: 570
    height: 300
    primary: true
    note: '九六式舰攻。凤翔号 1942-06 中途岛时载 8 架，全部用于搜索。'

  - id: 'weapon-8cm-40-3ns-museum'
    file: '/img/weapons/8cm-40-3ns.jpg'
    subject: weapon:8cm-40-3ns
    title:
      zh: '8 cm/40 三年式高炮（博物馆实物）'
      en: 'Japanese Type 3 Navy 80 mm AA gun, museum example'
    part: mount
    view: three_quarter
    date: '1940s'
    license: pd
    license_tier: A
    license_raw: 'Public domain'
    author: 'Unknown author'
    source_url: 'https://commons.wikimedia.org/wiki/File:Japanese_Type_3_Navy_80mm_AA_Gun.jpg'
    width: 690
    height: 898
    primary: true
    note: '博物馆保存的实物，可见炮身、驻退复进机与基座结构。旁边的炮弹是同型弹药。'

  - id: 'weapon-15cm-50-t41-yamato-aft'
    file: '/img/weapons/15cm-50-t41.jpg'
    subject: weapon:15cm-50-t41
    title:
      zh: '大和号舰尾 15.5 cm 三联装炮塔'
      en: 'Aft 155 mm gun turret of the battleship Yamato'
    part: turret
    view: rear
    date: '1940s'
    license: pd
    license_tier: A
    license_raw: 'Public domain'
    author: 'Unknown author'
    source_url: 'https://commons.wikimedia.org/wiki/File:Aft_155_mm_gun_turret_Yamato_300px.jpg'
    width: 300
    height: 222
    primary: true
    note: '大和号舰尾的 15.5 cm 三联装炮塔。同一型号也装在金刚级与最上级上，本图仅示炮塔外形，不代表某一具体装舰。'

  - id: 'weapon-47in-45-mk12-diagram'
    file: '/img/weapons/47in-45-mk12.jpg'
    subject: weapon:47in-45-mk12
    title:
      zh: 'QF 4.7 英寸 Mk IX 炮与 CP Mk XVIII 炮座图'
      en: 'QF 4.7 inch Mk IX gun in CP Mk XVIII mounting, diagram'
    part: mount
    view: side
    date: '1940s'
    license: pd
    license_tier: A
    license_raw: 'Public domain'
    author: 'Unknown author'
    source_url: 'https://commons.wikimedia.org/wiki/File:QF_4.7_inch_Mk_IX_gun_CP_Mk_XVIII_mounting_diagrams.jpg'
    width: 960
    height: 720
    primary: true
    note: '这是技术图纸，不是照片。可清楚看到炮座与装填机构的结构，对模型制作者比照片更有用。'
"""

if 'weapon-5in25-mk10-northampton' not in src:
    src = src.rstrip('\n') + '\n' + APPEND
    print('  [追加] 6 条武器配图')
else:
    print('  已存在，跳过追加')

# 先把当前（被污染的）文件另存，再写回恢复版
shutil.copy2(IMGS, f'{IMGS}.polluted-{STAMP}')
with io.open(IMGS, 'w', encoding='utf-8', newline='\n') as f:
    f.write(src)

# 校验
import yaml
d = yaml.safe_load(io.open(IMGS, encoding='utf-8'))
print(f'\n恢复后：{len(d["images"])} 条图，'
      f'{sum(1 for l in src.split(chr(10)) if l.strip().startswith("#"))} 行注释')
print(f'PRELOAD 保留: {"PRELOAD" in src}')
