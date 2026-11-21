# 重下被删掉的图，拉长重试间隔（上次是限流不是 URL 问题）。
import io
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))
picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))

# 建立 title -> entry 映射
tmap = {}
for sid, es in cand.items():
    for e in es:
        tmap[e['title']] = (sid, e)

# 找出 picked 里记录但磁盘上没有的文件（也就是被删掉的）
missing = []
for sid, es in picked.items():
    for e in es:
        p = OUT / e['name']
        if not p.exists():
            missing.append((sid, e))

print(f'需要重下 {len(missing)} 张')

fixed = 0
for i, (sid, e) in enumerate(missing):
    info = tmap.get(e['title'])
    if not info:
        print(f'  [{i+1}] 候选里没有: {e["title"][:50]}')
        continue
    src = info[1]
    url = src.get('thumb')
    if not url:
        continue

    dest = OUT / e['name']
    ok = False
    for a in range(8):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) > 5000 and data[:2] == b'\xff\xd8':
                io.open(dest, 'wb').write(data)
                ok = True
                break
            else:
                print(f'  [{i+1}] 返回非图片 ({len(data)} bytes)')
                break
        except urllib.error.HTTPError as ex:
            if ex.code == 429:
                wait = 30 + a * 20
                time.sleep(wait)
                continue
            print(f'  [{i+1}] HTTP {ex.code}')
            break
        except Exception:
            time.sleep(10)
    if ok:
        fixed += 1
        print(f'  [{i+1}] OK {e["name"][:56]}')
    time.sleep(4)

print()
print(f'重下成功 {fixed}/{len(missing)}')

# 从 picked 里移除仍然失败的
kept = {}
for sid, es in picked.items():
    kept[sid] = [e for e in es if (OUT / e['name']).exists()]

io.open(WORK / 'picked.json', 'w', encoding='utf-8').write(
    json.dumps(kept, ensure_ascii=False, indent=2))

print()
print('=== 每舰最终 ===')
for sid, es in kept.items():
    print(f'  {sid:<18} {len(es)}')
print(f'总计 {sum(len(v) for v in kept.values())}')
