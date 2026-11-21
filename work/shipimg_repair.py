# 修复：44 张是 HTML 错误页。重新下载它们，用正确的 thumb.wikimedia.org。
import io
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))
cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))


def get_title_map():
    m = {}
    for sid, entries in cand.items():
        for e in entries:
            m[e['title']] = e
    return m


tmap = get_title_map()


def download_ok(url, dest):
    """下载并校验文件头是 JPEG。返回 True/False。"""
    if not url:
        return False
    url = url.replace('upload.wikimedia.org', 'thumb.wikimedia.org')
    for a in range(6):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 5000 or data[:2] != b'\xff\xd8':
                return False
            io.open(dest, 'wb').write(data)
            return True
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 25 + a * 20
                print(f'      429 wait {w}s')
                time.sleep(w)
                continue
            print(f'      HTTP {e.code}')
            return False
        except Exception as ex:
            time.sleep(6)
    return False


fixed = 0
failed = []

for sid in list(picked.keys()):
    keep = []
    for e in picked[sid]:
        p = OUT / e['name']
        if not p.exists():
            continue
        with io.open(p, 'rb') as fh:
            head = fh.read(2)
        if head == b'\xff\xd8':
            keep.append(e)
            continue

        # 是坏的：找候选里的原始 URL 重下
        src = tmap.get(e['title'])
        if not src:
            print(f'  {sid}: 候选里找不到 {e["title"][:50]}, 删除')
            p.unlink()
            continue

        ok = download_ok(src.get('thumb'), p)
        if ok:
            print(f'  修复 {sid} {e["name"][:52]}')
            fixed += 1
            keep.append(e)
        else:
            print(f'  失败 {sid} {e["name"][:52]} -> 删除')
            p.unlink()
            failed.append((sid, e['name']))
        time.sleep(3)

    picked[sid] = keep

io.open(WORK / 'picked.json', 'w', encoding='utf-8').write(
    json.dumps(picked, ensure_ascii=False, indent=2))

print()
print(f'修复 {fixed} 张，失败 {len(failed)} 张')

# 再校验一遍
import os
bad = 0
for f in os.listdir(OUT):
    if '-extra-' not in f:
        continue
    with io.open(OUT / f, 'rb') as fh:
        if fh.read(2) != b'\xff\xd8':
            bad += 1
print(f'复查：剩余坏文件 {bad}')
