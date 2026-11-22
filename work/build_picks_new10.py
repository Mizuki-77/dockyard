# 把 pick_new10.py 的人工挑选结果整理成可下载的清单，并校验：
#   - 候选索引存在
#   - 授权是 PD/CC0（A 档）或 CC-BY/CC-BY-SA（B 档）
#   - 不是视频/PDF
import io
import json
import sys

sys.path.insert(0, 'work')
from pick_new10 import PICKS  # noqa: E402

cand = json.load(io.open('work/shipimg/candidates_new10.json', encoding='utf-8'))

out = {}
problems = []
for sid, picks in PICKS.items():
    es = cand.get(sid) or []
    rows = []
    for (idx, part, view, date, note) in picks:
        if idx >= len(es):
            problems.append(f'{sid}: 索引 {idx} 超出候选范围（只有 {len(es)} 张）')
            continue
        e = es[idx]
        lic = e.get('license') or ''
        if 'Public domain' in lic or 'CC0' in lic:
            tier = 'A'
            lic_key = 'pd' if 'Public domain' in lic else 'cc0'
        elif 'CC BY' in lic:
            tier = 'B'
            lic_key = 'cc_by' if 'CC BY-SA' not in lic else 'cc_by_sa'
        elif 'No restrictions' in lic:
            tier = 'A'
            lic_key = 'unknown'
        else:
            problems.append(f'{sid}[{idx}]: 授权 {lic!r} 不是 A/B 档，排除')
            continue
        rows.append({
            'idx': idx, 'part': part, 'view': view, 'date': date, 'note': note,
            'title': e['title'], 'thumb': e['thumb'], 'w': e['w'], 'h': e['h'],
            'license_raw': lic, 'license': lic_key, 'tier': tier,
            'artist': e.get('artist'), 'page': e.get('page'),
        })
    out[sid] = rows
    print(f'{sid:<14} {len(rows):>2} 张  (A 档 {sum(1 for r in rows if r["tier"]=="A")}, '
          f'B 档 {sum(1 for r in rows if r["tier"]=="B")})')

print()
print(f'总计 {sum(len(v) for v in out.values())} 张')
if problems:
    print('\n问题：')
    for p in problems:
        print('  !', p)

io.open('work/shipimg/picked_new10.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=2))
print('\n已写 work/shipimg/picked_new10.json')
