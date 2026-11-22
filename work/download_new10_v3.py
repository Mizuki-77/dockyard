# 下载挑好的图（第三版，最终）。
#
# 前两版的失败原因，逐条记下来（这是本项目最容易重复踩的坑）：
#
#   ① imageinfo 的 thumburl 带 ?utm_source=... 查询串 —— 不剥掉就 404。
#   ② 判据错了：`thumbnail_unscaled` 说明**原图宽度小于请求宽度**，
#      此时 API 给的是 upload.wikimedia.org 的**原图直链**，把它换成
#      thumb.wikimedia.org 一定 404（我第二版就是这么挂的）。
#      正确做法：**thumburl 是什么域名就用什么域名，只剥查询串，不要改域名。**
#   ③ upload.wikimedia.org 对本项目持续 429 —— 这局限流比 thumb. 严格，
#      所以每张之间要停 3 秒以上，遇到 429 要长退避。
#   ④ 必须校验文件头。实测：对不存在的 thumb URL，Commons 返回的是
#      **HTTP 200 + HTML 错误页**，urlopen 不抛异常。不校验就会把
#      HTML 存成 .jpg（第一轮就是这么拦下 34 个的）。
import io
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'ships'
OUT.mkdir(parents=True, exist_ok=True)
PICKS = ROOT / 'work' / 'shipimg' / 'picked_new10.json'

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'


def normalize(url):
    """只剥查询串，不改域名 —— 域名由 API 决定。"""
    if not url:
        return None
    return url.split('?')[0]


def fetch(url, retries=8):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 30 + a * 30
                print(f'        429 wait {w}s')
                time.sleep(w)
                continue
            print(f'        HTTP {e.code}')
            if a == retries - 1:
                return None
            time.sleep(15)
        except Exception as e:
            if a == retries - 1:
                print(f'        ERR {type(e).__name__}')
                return None
            time.sleep(15)
    return None


def img_ext(data):
    if data.startswith(b'\xff\xd8'):
        return 'jpg'
    if data.startswith(b'\x89PNG'):
        return 'png'
    if data.startswith(b'GIF8'):
        return 'gif'
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp'
    return None


def safe_name(s):
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
        existing = (list(OUT.glob(f'{sid}-{i+1:02d}-*.jpg')) +
                    list(OUT.glob(f'{sid}-{i+1:02d}-*.png')) +
                    list(OUT.glob(f'{sid}-{i+1:02d}-*.webp')))
        if existing and existing[0].stat().st_size > 3000:
            f = existing[0]
            print(f'  [{i+1}] 已有 {f.stat().st_size//1024}KB  {f.name[:55]}')
            report[sid].append({**r, 'file': f'/img/ships/{f.name}'})
            ok += 1
            continue

        url = normalize(r.get('thumb') or r.get('page'))
        data = fetch(url)
        if not data:
            fail.append((sid, i, r['title'], 'fetch failed'))
            continue

        ext = img_ext(data)
        if not ext:
            fail.append((sid, i, r['title'], f'HEAD={data[:30]!r}'))
            print(f'  [{i+1}] 非图片丢弃（{len(data)}B）')
            continue

        base = safe_name(r['title'].rsplit('.', 1)[0])[:48]
        fname = f'{sid}-{i+1:02d}-{base}.{ext}'
        (OUT / fname).write_bytes(data)
        print(f'  [{i+1}] OK {len(data)//1024:>5}KB  {fname[:58]}')
        report[sid].append({**r, 'file': f'/img/ships/{fname}'})
        ok += 1
        time.sleep(3.5)

io.open(ROOT / 'work' / 'shipimg' / 'download_report.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print(f'成功 {ok} 张，失败 {len(fail)} 张')
for f in fail:
    print('  !', f[0], f'[{f[1]}]', f[2][:50], '|', f[3][:50])
