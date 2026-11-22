# 下载挑好的图并校验文件头。
#
# 硬规矩（docs/45 §8.2，这一条踩得最惨）：
#   ① 必须校验文件头 \xff\xd8（JPEG）。Commons 限流时返回 HTTP 200 + HTML
#      错误页，urlopen 不抛异常，不校验就会把 HTML 存成 .jpg；
#   ② 图床用 thumb.wikimedia.org，upload.wikimedia.org 对本项目持续 429；
#   ③ 缩略图宽度只用合法档位 120/250/330/500/960/1280/1920/3840；
#   ④ 视频/PDF 按扩展名排除（已在上一步排过）。
import io
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'ships'
OUT.mkdir(parents=True, exist_ok=True)
PICKS = ROOT / 'work' / 'shipimg' / 'picked_new10.json'

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'


def thumb_url(url, width=1280):
    """把 upload.wikimedia.org 换成 thumb.wikimedia.org，并设合法宽度。"""
    if not url:
        return None
    u = url.replace('//upload.wikimedia.org/', '//thumb.wikimedia.org/')
    # 已经是缩略图 URL 的，直接改宽度段
    import re
    m = re.search(r'/(\d+)px-', u)
    if m:
        u = u[:m.start(1)] + str(width) + u[m.end(1):]
        return u
    # 原图 URL：/wikipedia/commons/x/xy/Name.jpg -> /thumb/.../Name.jpg/1280px-Name.jpg
    mm = re.match(r'^(https://thumb\.wikimedia\.org/wikipedia/commons/[0-9a-f]/[0-9a-f]{2}/)([^/]+)$', u)
    if mm:
        return f'{mm.group(1)}{mm.group(2)}/{width}px-{mm.group(2)}'
    return u


def fetch(url, retries=6):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 20 + a * 20
                print(f'      429 wait {w}s')
                time.sleep(w)
                continue
            print(f'      HTTP {e.code} {url[:80]}')
            if a == retries - 1:
                return None
            time.sleep(8)
        except Exception as e:
            if a == retries - 1:
                print(f'      ERR {e}')
                return None
            time.sleep(8)
    return None


def safe_name(s):
    import re
    s = re.sub(r'[^a-zA-Z0-9._-]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-').lower()


picked = json.load(io.open(PICKS, encoding='utf-8'))
ok = 0
fail = []
report = {}

for sid, rows in picked.items():
    print(f'=== {sid} ===')
    report[sid] = []
    for i, r in enumerate(rows):
        # 目标文件名：<ship>-<序号>-<短名>.jpg
        base = safe_name(r['title'].rsplit('.', 1)[0])[:50]
        fname = f'{sid}-{i+1:02d}-{base}.jpg'
        dst = OUT / fname
        if dst.exists() and dst.stat().st_size > 5000:
            print(f'  [{i+1}] 已存在，跳过 {fname}')
            report[sid].append({**r, 'file': f'/img/ships/{fname}', 'skipped': True})
            ok += 1
            continue

        url = thumb_url(r.get('thumb') or r.get('page'))
        data = fetch(url)
        if not data:
            fail.append((sid, i, r['title']))
            print(f'  [{i+1}] 失败 {r["title"][:50]}')
            continue
        # ⚠️ 文件头校验：Commons 限流时会给 HTML
        if not data.startswith(b'\xff\xd8'):
            head = data[:80]
            fail.append((sid, i, f'{r["title"]} HEAD={head[:40]!r}'))
            print(f'  [{i+1}] 不是 JPEG，丢弃 {r["title"][:40]}')
            continue

        dst.write_bytes(data)
        size_kb = len(data) // 1024
        print(f'  [{i+1}] OK {size_kb:>5} KB  {fname[:70]}')
        report[sid].append({**r, 'file': f'/img/ships/{fname}'})
        ok += 1
        time.sleep(3)

io.open(ROOT / 'work' / 'shipimg' / 'download_report.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print(f'成功 {ok} 张，失败 {len(fail)} 张')
for f in fail:
    print('  !', f)
