# 清掉 fact 里的 '未获取' 占位值
#
# 为什么：fact 的 value 应该是真实数据。写 '未获取' 等于把「没有数据」当成
# 「数据是未获取」记录下来 —— 页面上会渲染出一个 value 为「未获取」的字段，
# 比不写更糟（读者会以为这是个已知取值）。
# SCHEMA §1 红线 1 就是这么要求的：查不到就整条不写，在 RESEARCH-NOTES 里记一句。
import glob
import io
import os
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
PLACEHOLDERS = {'未获取', '未知', '不详', 'N/A', 'None', ''}

removed_log = []


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


targets = [p for p in glob.glob('work/staging/*/**/*.yaml', recursive=True)
           if '_raw' not in p and '_merged' not in p and '.bak' not in p]

for p in sorted(targets):
    try:
        d = load(p)
    except Exception:
        continue
    if not isinstance(d, dict):
        continue
    facts = d.get('facts')
    if not facts:
        continue

    keep = []
    for f in facts:
        v = f.get('value')
        if isinstance(v, str) and v.strip() in PLACEHOLDERS:
            removed_log.append((p, f.get('field'), v, f.get('src')))
            continue
        keep.append(f)

    if len(keep) != len(facts):
        bak = f'{p}.bak-{STAMP}'
        if not os.path.exists(bak):
            shutil.copy2(p, bak)
        d['facts'] = keep
        dump(p, d)
        print(f'  {p}: 删除 {len(facts) - len(keep)} 条占位')

print()
print(f'共删除 {len(removed_log)} 条：')
for p, fld, v, src in removed_log:
    print(f'  {p}\n     {fld} = {v!r}  src={src}')

# 写进对应的 RESEARCH-NOTES，保证信息不丢
notes = os.path.join('work/staging', '_removed-placeholders.md')
with io.open(notes, 'w', encoding='utf-8', newline='\n') as f:
    f.write('# 被删除的「未获取」占位 fact\n\n')
    f.write('> 这些 fact 的 value 是占位词而非真实数据，已从 YAML 删除。\n')
    f.write('> 原始证据仍在各组 `RESEARCH-NOTES.md` 里，这里留一份索引。\n\n')
    f.write('| 文件 | 字段 | 原值 | 来源 |\n|---|---|---|---|\n')
    for p, fld, v, src in removed_log:
        f.write(f'| `{p}` | `{fld}` | {v} | {src} |\n')
print(f'\n索引写到 {notes}')
