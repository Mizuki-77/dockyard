# 抽查每个切片实际挂了哪张图，确认是整舰构图。
import io
import os
import re

import yaml

d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
by_file = {str(x.get('file')): x for x in d['images']}

SHIPS = ['akagi', 'bismarck', 'tirpitz', 'illustrious', 'prinz-eugen', 'kaga',
         'king-george-v', 'enterprise', 'hood', 'rodney']

for sid in SHIPS:
    p = f'dist/ships/{sid}/index.html'
    if not os.path.exists(p):
        continue
    h = io.open(p, encoding='utf-8').read()
    # 抽 slice 的 code + pic file 对
    pairs = re.findall(r'"code":"(\w+)","title":"([^"]*)".*?"pic":\{"file":"([^"]+)"', h)
    if not pairs:
        pairs = re.findall(r'"code":"(\w+)".*?"pic":\{"file":"([^"]+)"', h)
    print(f'=== {sid} ===')
    for item in pairs[:8]:
        if len(item) == 3:
            code, title, f = item
        else:
            code, f = item
            title = ''
        rec = by_file.get(f, {})
        part = rec.get('part', '?')
        view = rec.get('view', '?')
        print(f'  {code:<3} {part:<12} {view:<10} {f.split("/")[-1][:44]}')
    print()
