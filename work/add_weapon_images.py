# 把肉眼确认过的武器配图写入 data/images.yaml
#
# 2026-11-24 人眼过图后的判定（交接报告 §7.2 第 8 条：自动筛选一定混进错图，必须人眼过）：
#
#   ✅ 采用：
#     weapon:5in25-mk10   北安普敦号 5"/25 在韦贾环礁开火（1942-02-01），舰上实拍
#     weapon:a5m4         A5M 九六式舰战实机（9-122 涂装）
#     weapon:b4y1         九六式舰攻实机
#     weapon:8cm-40-3ns   8 cm/40 三年式高炮博物馆实物
#     weapon:15cm-50-t41  大和号舰尾 155 mm 炮塔（同一型号）
#     weapon:47in-45-mk12 QF 4.7 英寸 Mk IX 炮座图纸（是图纸非照片，note 注明）
#
#   ❌ 不采用：
#     weapon:8in-55-mk9   抓到的是「新奥尔良号破损舰首」，炮只是陪衬，题材错
#     weapon:14cm-50-3ns  抓到的是「塔拉瓦岸炮」，是陆上架设不是舰炮
#     weapon:21in-mk15    抓到的是 1953 年 O'Brien 号，年代与二战用法不符
#     weapon:20cm-3ns-no2 已由 20cm-3ns-primary 承担，重复
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


def strip_tags(s):
    import re
    return re.sub(r'<[^>]+>', '', str(s or '')).strip()


NEW = [
    {
        'id': 'weapon-5in25-mk10-northampton',
        'file': '/img/weapons/5in25-mk10.jpg',
        'subject': 'weapon:5in25-mk10',
        'title': {'zh': '北安普敦号的 5 英寸/25 倍径炮向韦贾环礁射击（1942-02-01）',
                  'en': '127 mm guns aboard USS Northampton (CA-26) firing on Wotje, 1 February 1942'},
        'part': 'mount',
        'view': 'side',
        'date': '1942-02-01',
        'license': 'pd',
        'license_tier': 'A',
        'license_raw': 'Public domain',
        'author': 'US Navy',
        'credit': '美国国家档案馆',
        'source_url': 'https://commons.wikimedia.org/wiki/File:127_mm_guns_aboard_USS_Northampton_(CA-26)_firing_on_Wotje_on_1_February_1942.jpg',
        'width': 1280,
        'height': 947,
        'primary': True,
        'note': '舰上实拍，可清楚看到 5"/25 的单装开放式炮座与装填手位置。中途岛时七艘美军重巡装的都是这一型。',
    },
    {
        'id': 'weapon-a5m4-claude',
        'file': '/img/weapons/a5m4.jpg',
        'subject': 'weapon:a5m4',
        'title': {'zh': '九六式舰战 A5M（9-122 涂装）',
                  'en': 'Mitsubishi A5M "Claude" fighter, coded 9-122'},
        'part': 'aircraft',
        'view': 'three_quarter',
        'date': '1930s',
        'license': 'pd',
        'license_tier': 'A',
        'license_raw': 'Public domain',
        'author': '日本海軍',
        'credit': ' Commons',
        'source_url': 'https://commons.wikimedia.org/wiki/File:A5M_Claude.jpg',
        'width': 421,
        'height': 195,
        'primary': True,
        'note': '九六式舰战实机。凤翔号与凤翔级在中途岛前后搭载过这一型。',
    },
    {
        'id': 'weapon-b4y1-jean',
        'file': '/img/weapons/b4y1.jpg',
        'subject': 'weapon:b4y1',
        'title': {'zh': '九六式舰攻 B4Y1',
                  'en': 'Yokosuka B4Y1 "Jean" carrier attack aircraft'},
        'part': 'aircraft',
        'view': 'three_quarter',
        'date': '1930s',
        'license': 'pd',
        'license_tier': 'A',
        'license_raw': 'Public domain',
        'author': '日本海軍',
        'credit': 'Commons',
        'source_url': 'https://commons.wikimedia.org/wiki/File:96siki-kankou.jpg',
        'width': 570,
        'height': 300,
        'primary': True,
        'note': '九六式舰攻。凤翔号 1942-06 中途岛时载 8 架，全部用于搜索。',
    },
    {
        'id': 'weapon-8cm-40-3ns-museum',
        'file': '/img/weapons/8cm-40-3ns.jpg',
        'subject': 'weapon:8cm-40-3ns',
        'title': {'zh': '8 cm/40 三年式高炮（博物馆实物）',
                  'en': 'Japanese Type 3 Navy 80 mm AA gun, museum example'},
        'part': 'mount',
        'view': 'three_quarter',
        'date': '1940s',
        'license': 'pd',
        'license_tier': 'A',
        'license_raw': 'Public domain',
        'author': '',
        'credit': 'Commons',
        'source_url': 'https://commons.wikimedia.org/wiki/File:Japanese_Type_3_Navy_80mm_AA_Gun.jpg',
        'width': 690,
        'height': 898,
        'primary': True,
        'note': '博物馆保存的实物，可见炮身、驻退复进机与基座结构。旁边的炮弹是同型弹药。',
    },
    {
        'id': 'weapon-15cm-50-t41-yamato-aft',
        'file': '/img/weapons/15cm-50-t41.jpg',
        'subject': 'weapon:15cm-50-t41',
        'title': {'zh': '大和号舰尾 15.5 cm 三联装炮塔',
                  'en': 'Aft 155 mm gun turret of the battleship Yamato'},
        'part': 'turret',
        'view': 'rear',
        'date': '1940s',
        'license': 'pd',
        'license_tier': 'A',
        'license_raw': 'Public domain',
        'author': '',
        'credit': 'Commons',
        'source_url': 'https://commons.wikimedia.org/wiki/File:Aft_155_mm_gun_turret_Yamato_300px.jpg',
        'width': 300,
        'height': 222,
        'primary': True,
        'note': '大和号舰尾的 15.5 cm 三联装炮塔。同一型号也装在金刚级与最上级上，'
                '本图仅示炮塔外形，不代表某一具体装舰。',
    },
    {
        'id': 'weapon-47in-45-mk12-diagram',
        'file': '/img/weapons/47in-45-mk12.jpg',
        'subject': 'weapon:47in-45-mk12',
        'title': {'zh': 'QF 4.7 英寸 Mk IX 炮与 CP Mk XVIII 炮座图',
                  'en': 'QF 4.7 inch Mk IX gun in CP Mk XVIII mounting, diagram'},
        'part': 'mount',
        'view': 'side',
        'date': '1940s',
        'license': 'pd',
        'license_tier': 'A',
        'license_raw': 'Public domain',
        'author': '',
        'credit': 'Commons',
        'source_url': 'https://commons.wikimedia.org/wiki/File:QF_4.7_inch_Mk_IX_gun_CP_Mk_XVIII_mounting_diagrams.jpg',
        'width': 960,
        'height': 720,
        'primary': True,
        'note': '这是技术图纸，不是照片。可清楚看到炮座与装填机构的结构，'
                '对模型制作者比照片更有用。',
    },
]

d = load(IMGS)
imgs = d['images']
have_ids = {im.get('id') for im in imgs}

added = 0
for e in NEW:
    if e['id'] in have_ids:
        print(f'  跳过已存在 {e["id"]}')
        continue
    if not os.path.exists('public' + e['file']):
        print(f'  ! 文件不存在，跳过 {e["file"]}')
        continue
    imgs.append(e)
    added += 1
    print(f'  + {e["id"]}  → {e["subject"]}')

shutil.copy2(IMGS, f'{IMGS}.bak2-{STAMP}')
dump(IMGS, d)
print(f'\n写入 {added} 条，图片总数 {len(imgs)}')
