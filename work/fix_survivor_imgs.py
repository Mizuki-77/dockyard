# 修正：幸存者照片的 part 不该是 hull_side/None，它们是人物照。
# 把这两条改成 other + detail，这样 isWholeShipShot 会排除它们，
# 时间轴不会挂「人被救起」的照片当整舰图 —— 那对看舰型毫无帮助。
import io
import re

ROOT = '.'
IMG = 'data/images.yaml'

text = io.open(IMG, encoding='utf-8').read()

# 要改的 id -> 新 part/view
FIX = {
    'bismarck-survivors-dorsetshire-1941': ('other', 'detail'),
    'bismarck-extra-3-hms-dorsetshire-bismarck-survivors-jpg': ('other', 'detail'),
}

for iid, (part, view) in FIX.items():
    # 定位该 block
    pat = re.compile(r'(^  - id: ' + re.escape(iid) + r'\n)(.*?)(?=^  - id: |\Z)', re.S | re.M)
    m = pat.search(text)
    if not m:
        print(f'找不到 {iid}')
        continue
    head, body = m.group(1), m.group(2)

    def setk(b, k, v):
        kp = re.compile(r'^    ' + k + r':.*$', re.M)
        if kp.search(b):
            return kp.sub(f'    {k}: {v}', b, count=1)
        return b + f'    {k}: {v}\n'

    body = setk(body, 'part', part)
    body = setk(body, 'view', view)
    # 加一句说明
    if 'note:' in body:
        body = re.sub(r'^    note:.*$',
                      '    note: >-\n      人物照（幸存者被救起），不是舰体照片。part 标 other、view 标 detail，'
                      '切片配图会排除它 —— 时间轴要的是能看出舰型的整舰照。',
                      body, count=1, flags=re.M)
    print(f'修正 {iid} -> {part}/{view}')
    text = text[:m.start()] + head + body + text[m.end():]

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)

import yaml
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print('图片总数:', len(d['images']))
for iid in FIX:
    for x in d['images']:
        if x['id'] == iid:
            print(f"  验证 {iid}: part={x.get('part')} view={x.get('view')}")
