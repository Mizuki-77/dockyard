# 给预存图（舰未入库）加显式标记，避免以后被误判为孤儿数据删除。
import io
import re

IMG = 'data/images.yaml'
text = io.open(IMG, encoding='utf-8').read()

PRELOAD = {
    'yamato-explosion-1945': '大和号（未入库）',
    'yamato-trials-1941': '大和号（未入库）',
    'yamato-under-attack-1945': '大和号（未入库）',
    'yamato-samar-1944': '大和号（未入库）',
    'iowa-broadside-1944': '衣阿华号（未入库）',
    'missouri-pacific-1945': '密苏里号（未入库）',
}

for iid, label in PRELOAD.items():
    pat = re.compile(r'(^  - id: ' + re.escape(iid) + r'\n)(.*?)(?=^  - id: |\Z)', re.S | re.M)
    m = pat.search(text)
    if not m:
        print(f'找不到 {iid}')
        continue
    head, body = m.group(1), m.group(2)
    if 'PRELOAD' in body:
        print(f'{iid} 已标记')
        continue
    # 在 file 行后面插入一行注释
    fm = re.search(r'^    file: .*$', body, re.M)
    if not fm:
        continue
    note = (
        f'    # PRELOAD：{label}的素材，该舰尚未入库。\n'
        f'    # 现在没有任何页面会渲染它；等该舰入库后 ship:{iid.split("-")[0]} 即可自动生效。\n'
        f'    # 不要因为「没有页面引用」就把它当成孤儿数据删掉。\n'
    )
    body = body[:fm.end() + 1] + note + body[fm.end() + 1:]
    text = text[:m.start()] + head + body + text[m.end():]
    print(f'标记 {iid}')

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)

import yaml
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print(f'\n图片总数: {len(d["images"])}')
