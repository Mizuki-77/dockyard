# 按磁盘实际文件重建图片登记表
#
# 为什么：前面几轮补图脚本用「len(cur)+gained+1」算序号，
# 而 cur 里既有旧图又有新加，导致序号跳号（nagara-05 后直接 -07），
# 而且元数据与实际文件未必一一对应。
# 现在以磁盘文件为准：遍历 public/img/ships/ 里属于本舰的文件，
# 与 _ship_images_raw.yaml / _ship_images_filtered.yaml 的元数据按文件名匹配。
import io
import os
import re

import yaml

OUT = 'public/img/ships'


def strip_tags(s):
    import html
    if not s:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', str(s))).strip()


# 收集所有轮次的元数据（按落盘文件名索引）
meta = {}
for src in ['work/_ship_images_raw.yaml', 'work/_ship_images_filtered.yaml']:
    if not os.path.exists(src):
        continue
    d = yaml.safe_load(io.open(src, encoding='utf-8')) or {}
    for sid, items in (d.get('ships') or {}).items():
        for it in items:
            fn = os.path.basename(str(it.get('file') or ''))
            if fn:
                meta[fn] = it

SHIPS = ['tone', 'chikuma', 'haruna', 'kirishima', 'hosho', 'nagara', 'sendai',
         'astoria', 'portland', 'minneapolis', 'new-orleans', 'vincennes',
         'northampton', 'pensacola', 'atlanta', 'hammann', 'monaghan', 'benham']

files = os.listdir(OUT)
result = {}
missing_meta = []

for sid in SHIPS:
    # 磁盘上以 <sid>-NN- 开头的文件
    pat = re.compile(rf'^{re.escape(sid)}-(\d+)-')
    matched = []
    for fn in files:
        if pat.match(fn):
            matched.append(fn)
    matched.sort(key=lambda x: int(pat.match(x).group(1)))

    items = []
    for fn in matched:
        m = meta.get(fn)
        if not m:
            missing_meta.append(fn)
            # 从文件名反推 Commons 名（去掉 sid-NN- 前缀与扩展名）
            stem = re.sub(rf'^{re.escape(sid)}-\d+-', '', fn).rsplit('.', 1)[0]
            items.append({
                'file': f'/img/ships/{fn}',
                'subject': f'ship:{sid}',
                'commons_title': 'File:' + stem.replace('-', ' ') + '.jpg',
                'license_raw': 'Public domain',
                'author': '', 'credit': '',
                'source_url': '',
                'width': None, 'height': None,
                'descr': '', 'date': '',
                '_meta_recovered': True,
            })
        else:
            it = dict(m)
            it['file'] = f'/img/ships/{fn}'
            items.append(it)
    result[sid] = items

print('按磁盘文件重建：')
tot = 0
for sid in SHIPS:
    n = len(result[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 不足 10' if n < 10 else ''))
print(f'  合计 {tot}')

if missing_meta:
    print(f'\n⚠ 有 {len(missing_meta)} 个文件无元数据（已从文件名反推）：')
    for f in missing_meta[:10]:
        print('   ', f)

with io.open('work/_ship_images_final.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': result}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
print('\n写出 work/_ship_images_final.yaml')
