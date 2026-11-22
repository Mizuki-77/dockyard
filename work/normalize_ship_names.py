# 统一舰名中文写法：全部加「号」。
#
# 依据（2026-11-22 实测，不是凭感觉）：
#   - 中文维基百科条目名一律带「号」：
#       赤城号航空母舰 / 加贺号航空母舰 / 蒼龍號航空母艦 / 飛龍號航空母艦
#       企業號航空母艦 (CV-6) / 約克鎮號航空母艦 (CV-5) / 大黃蜂號航空母艦 (CV-8)
#       胡德号战列巡洋舰 / 羅德尼號戰艦 / 威尔士亲王号战列舰
#       俾斯麥號戰艦 / 欧根亲王号重巡洋舰 / 勝利號航空母艦
#       皇家方舟号航空母舰 (1937年) / 多塞特郡号重巡洋舰 / 谢菲尔德号轻巡洋舰 (C24)
#   - 中国航海博物馆（shmmc.com.cn）展牌：「俾斯麦」号（带引号、带号）
#   - 人民网军事「名舰传奇：威震全球的十大舰艇」：俾斯麦级战列舰「俾斯麦」号
#
# 结论：中文军事出版与官方科普媒体一律写「××号」。
# 本站原来 15 艘里日本 4 艘（赤城/加贺/苍龙/飞龙）、英德若干没带「号」，
# 是不同批次写作造成的，不是刻意区分。
#
# 顺带：日本舰名在中文里确实常省略「号」（如「赤城中弹」），但那是行文里的
# 简称，作条目标题时仍写全「赤城号」。本站 name_zh 是条目名，取全称。
#
# 用法：python work/normalize_ship_names.py --dry-run
import glob
import io
import os
import re
import sys
from datetime import datetime

import yaml

DRY = '--dry-run' in sys.argv

# 逐舰指定，避免「自动加号」把已经有号的名字加成「××号号」，
# 也避免把本来就不该带号的短语改坏。
FIXES = {
    # 日 —— 原来不带号
    'akagi': '赤城号',
    'kaga': '加贺号',
    'soryu': '苍龙号',
    'hiryu': '飞龙号',
    # 德 —— 原来不带号
    'bismarck': '俾斯麦号',
    'tirpitz': '提尔皮茨号',
    # 英 —— 原来不带号
    'hood': '胡德号',
    'king-george-v': '英王乔治五世号',
    'illustrious': '光辉号',
    'victorious': '胜利号',
    'ark-royal': '皇家方舟号',
    # 已经是「号」的核对一遍（防止有漏或有多余空格）
    'enterprise': '企业号',
    'yorktown': '约克城号',
    'hornet': '大黄蜂号',
    'prince-of-wales': '威尔士亲王号',
    'prinz-eugen': '欧根亲王号',
    'rodney': '罗德尼号',
    'sheffield': '谢菲尔德号',
    'norfolk': '诺福克号',
    'dorsetshire': '多塞特郡号',
    'cossack': '哥萨克号',
    'maori': '毛利人号',
    'zulu': '祖鲁人号',
    'sikh': '锡克人号',
    'piorun': '闪电号',
}

changed = []
for sid, new_name in sorted(FIXES.items()):
    p = f'data/ships/{sid}.yaml'
    if not os.path.exists(p):
        print(f'  ! 缺文件 {p}，跳过')
        continue
    text = io.open(p, encoding='utf-8').read()
    d = yaml.safe_load(text)
    old = d['name']['zh']
    if old == new_name:
        continue

    # 文本层面替换，保住注释与排版
    # 只改 name: 下面 zh: 那一行（ship 文件的 name 是块状映射）
    m = re.search(r'^(name:\n(?:\s+\S+:.*\n)*?)(\s+zh:\s*)(.+)$', text, re.M)
    if not m:
        print(f'  ! {sid}: 找不到 name.zh 行，跳过（原名 {old!r}）')
        continue

    new_text = text[:m.start(3)] + new_name + text[m.end(3):]

    if not DRY:
        bak = f'{p}.bak-{datetime.now().strftime("%Y-%m-%d")}'
        if not os.path.exists(bak):
            io.open(bak, 'w', encoding='utf-8', newline='\n').write(text)
        io.open(p, 'w', encoding='utf-8', newline='\n').write(new_text)

    changed.append((sid, old, new_name))

print(f'\n改名 {len(changed)} 艘：')
for sid, old, new in changed:
    print(f'  {sid:<18} {old:<12} -> {new}')

if DRY:
    print('\n=== dry-run，没有写文件 ===')
else:
    # 复验
    print('\n复验全部 25 艘：')
    bad = []
    for p in sorted(glob.glob('data/ships/*.yaml')):
        if '.bak' in p:
            continue
        d = yaml.safe_load(io.open(p, encoding='utf-8'))
        zh = d['name']['zh']
        ok = zh.endswith('号')
        if not ok:
            bad.append((d['id'], zh))
        print(f"  {d['id']:<18} {zh:<14} {'OK' if ok else '<- 仍不带号'}")
    print()
    print('全部带号' if not bad else f'仍有 {len(bad)} 个不带号：{bad}')
