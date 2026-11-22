# 验证切片配图现在都是整舰构图，并检查有多少片变成「无影像」。
import io
import json
import os
import re
import subprocess

# 从构建产物里抽 payload 的 slices 部分不好做（是序列化 JSON），
# 改用 node 直接调 sliceImages。这里用更笨但可靠的办法：
# 读 dist 页面里的内联 JSON。
import yaml

SHIPS = ['akagi', 'bismarck', 'enterprise', 'hiryu', 'hornet', 'illustrious',
         'kaga', 'king-george-v', 'prince-of-wales', 'prinz-eugen', 'rodney',
         'soryu', 'tirpitz', 'yorktown']

d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
by_id = {x['id']: x for x in d['images']}

LOCAL_PARTS = {'turret', 'superstructure', 'bridge', 'propeller', 'catapult',
               'aircraft_handling', 'weapon', 'radar'}

print(f'{"舰":<18} {"片数":<5} {"有图":<5} {"无图":<5} {"仍挂局部图"}')
print('-' * 56)

for sid in SHIPS:
    p = f'dist/ships/{sid}/index.html'
    if not os.path.exists(p):
        continue
    h = io.open(p, encoding='utf-8').read()
    # 找 slices 的 pic.file
    pics = re.findall(r'"pic":\{"file":"([^"]+)"', h)
    # 统计该页 slices 总数
    m = re.search(r'"slices":\[(.*?)\],"groups"', h, re.S)
    n_slices = 0
    if m:
        n_slices = len(re.findall(r'"code":"', m.group(1)))

    bad = []
    for f in pics:
        # 反查是哪张图
        rec = None
        for x in d['images']:
            if str(x.get('file')) == f:
                rec = x
                break
        if rec and (str(rec.get('part')) in LOCAL_PARTS or str(rec.get('view')) == 'detail'):
            bad.append(f'{rec["id"][:30]}({rec.get("part")}/{rec.get("view")})')

    n_pic = len(pics)
    print(f'{sid:<18} {n_slices:<5} {n_pic:<5} {n_slices-n_pic:<5} {"; ".join(bad) if bad else "-"}')
