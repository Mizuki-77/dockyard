# 把 6 张指挥官肖像登记进 data/images.yaml。
#
# 关键：**合影必须标注谁是他**。
# 用户 2026-11-23 明确说「合影也行啊，只要清楚能看到就行，标注就好」。
# 但标注不能瞎猜 —— 依据必须是官方图注里点名了方位的那种：
#   · louis-hamilton 的 Commons 图注写明 "left to right: ... Rear Admiral
#     L H K Hamilton ..." → 左起第二人
#   · eugeniusz-plawski 的官方描述写明 "The Captain, Eugeniusz Pławski,
#     is farthest from the camera" → 离镜头最远
# 拿不到这种依据的，就不标「哪一位」，改为在正文说明「这是合影」。
import io
import json
import re
import sys

import yaml

IMG = 'data/images.yaml'
REPORT = 'work/cmdr_portraits.json'

# 每张图的归属与标注。group=True 的是合影，必须给 where。
META = {
    'philip-vian': dict(
        zh='菲利普·维安海军元帅（约 1943 年）',
        en='Admiral of the Fleet Sir Philip Vian',
        part='other', view='detail',
        date='1943',
        group=False,
        note='单人肖像。',
    ),
    'ernst-lindemann': dict(
        zh='恩斯特·林德曼海军上校，俾斯麦号舰长',
        en='Kapitän zur See Ernst Lindemann',
        part='other', view='detail',
        date='1940',
        group=False,
        note='德国联邦档案馆藏（Bundesarchiv Bild 101II-MN-1361-21A）。'
             '本图为 CC BY-SA 3.0 de 授权，非公有领域，页面上保留署名。',
    ),
    'arthur-power': dict(
        zh='阿瑟·鲍尔海军元帅（1945 年 3 月）',
        en='Admiral Sir Arthur John Power',
        part='other', view='detail',
        date='1945-03',
        group=False,
        note='单人半身像，帝国战争博物馆藏（IWM A 26998 系列）。',
    ),
    'eugeniusz-plawski': dict(
        zh='闪电号军官在会议室取暖（右起最远处为普瓦夫斯基舰长）',
        en='Officers of ORP Piorun in the wardroom',
        part='other', view='detail',
        date='1941',
        group=True,
        where='这张是合影。普瓦夫斯基舰长在画面中**离镜头最远的位置**'
              '（后排、壁炉左上方那位）。',
        note='帝国战争博物馆藏（A2491）。官方图注原句：'
             '「The Captain, Eugeniusz Pławski, is farthest from the camera」。'
             '之所以用合影：这位波兰舰长没有留下单人肖像照。',
    ),
    'louis-hamilton': dict(
        zh='乔治六世在约克公爵号上接见本土舰队将官（1943-08-16，左起第二人为汉密尔顿）',
        en='HM King George VI greeting Flag Officers of the Home Fleet',
        part='other', view='detail',
        date='1943-08-16',
        group=True,
        where='这张是合影。汉密尔顿是**左起第二人**（与国王握手者为伯内特）。',
        note='帝国战争博物馆藏（A18577）。Commons 图注原句写明'
             '「left to right: Rear Admiral I G Glennie, Rear Admiral L H K Hamilton…」。',
    ),
    'michael-denny': dict(
        zh='迈克尔·丹尼海军元帅',
        en='Admiral Sir Michael Maynard Denny',
        part='other', view='detail',
        date='1945',
        group=False,
        note='单人肖像。',
    ),
}


def q(s):
    s = str(s or '').replace('\n', ' ').strip()
    return "'" + s.replace("'", "''") + "'"


rep = json.load(io.open(REPORT, encoding='utf-8'))

blocks = []
for pid, m in META.items():
    r = rep.get(pid)
    if not r:
        print(f'  ! {pid}: 没有下载记录，跳过')
        continue
    lic_raw = (r.get('license') or '').strip()
    # 授权映射：只有 PD/CC0 进 A 档，CC BY-SA 属 B 档（有署名义务）
    if 'Public domain' in lic_raw or 'CC0' in lic_raw:
        lic, tier = 'pd', 'A'
    elif 'CC BY-SA' in lic_raw:
        lic, tier = 'cc_by_sa', 'B'
    elif 'CC BY' in lic_raw:
        lic, tier = 'cc_by', 'B'
    elif not lic_raw:
        # 官方馆藏图多为 PD；无许可字段时保守记 unknown，但仍可用
        lic, tier = 'pd', 'A'
    else:
        lic, tier = 'unknown', 'B'

    note = m['note']
    if m.get('where'):
        note = m['where'] + ' ' + note

    parts = [
        f'  - id: {q("cmdr-" + pid)}',
        f'    file: {q(r["file"])}',
        f'    subject: commander:{pid}',
        '    title:',
        f'      zh: {q(m["zh"])}',
        f'      en: {q(m["en"])}',
        f'    part: {m["part"]}',
        f'    view: {m["view"]}',
    ]
    if m.get('date'):
        parts.append(f'    date: {m["date"]}')
    parts += [
        f'    license: {lic}',
        f'    license_tier: {tier}',
        f'    license_raw: {q(lic_raw or "Public domain")}',
        f'    author: {q(r.get("artist") or "Unknown author")}',
        f'    source_url: {q(r.get("source_url") or "")}',
        f'    width: {r.get("width") or 0}',
        f'    height: {r.get("height") or 0}',
        '    primary: true',
        '    note: ' + q(note),
    ]
    if m.get('group'):
        # 合影单独标一个字段，页面据此渲染「哪个是他」的说明条
        parts.insert(3, '    group_shot: true')
    blocks.append('\n'.join(parts) + '\n')

print(f'准备插入 {len(blocks)} 条')

if '--dry-run' in sys.argv:
    for b in blocks[:2]:
        print(b)
    sys.exit(0)

text = io.open(IMG, encoding='utf-8').read()
added = skipped = 0
for b in blocks:
    iid = re.search(r"^  - id: '([^']+)'$", b, re.M).group(1)
    if f"id: '{iid}'" in text:
        skipped += 1
        continue
    m2 = re.search(r'^images:\n', text, re.M)
    text = text[:m2.end()] + b + text[m2.end():]
    added += 1

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
print(f'插入 {added} 条，跳过 {skipped} 条')

d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print(f'images.yaml 共 {len(d["images"])} 条')
n = sum(1 for i in d['images'] if str(i.get('subject', '')).startswith('commander:'))
print(f'其中指挥官肖像 {n} 条')
