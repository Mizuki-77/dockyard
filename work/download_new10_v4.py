# 下载挑好的图（第四版，正确版）。
#
# 前三版全部失败的原因，最终定位到一件事：
#   **thumb URL 必须由 API 给，不能自己拼。**
#
#   API 的 iiurlwidth=1280 返回两种 thumburl：
#     - 原图宽 > 1280：https://thumb.wikimedia.org/wikipedia/commons/thumb/d/df/NAME.jpg/1280px-NAME.jpg
#                      ^^^^ 注意路径里多了 /thumb/ 这一段
#     - 原图宽 ≤ 1280：https://upload.wikimedia.org/wikipedia/commons/d/df/NAME.jpg
#                      （thumbnail_unscaled，就是原图本身）
#
#   我前几版自己拼 URL 时漏了 /thumb/ 这一段，于是 thumb 域名 + 缺 /thumb/
#   得到 HTTP 200 + HTML 错误页 —— 被文件头校验拦下，没污染数据，但白跑。
#
# 本版做法：直接从 picked_new10.json 里存的 thumb 字段取（那就是 API 原值），
# 只剥查询串。宽度 > 1280 的图，API 给的就是 1280px 缩略图，体积可控。
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

UA = ('DockyardArchive/1.0 (historical research; '
      'github.com/Mizuki-77/dockyard)')


def fetch(url, retries=8):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 20 + a * 20
                print(f'        429 wait {w}s')
                time.sleep(w)
                continue
            print(f'        HTTP {e.code}')
            if a == retries - 1:
                return None
            time.sleep(12)
        except Exception as e:
            if a == retries - 1:
                print(f'        ERR {type(e).__name__}')
                return None
            time.sleep(12)
    return None


def img_ext(data):
    if data.startswith(b'\xff\xd8'):
        return 'jpg'
    if data.startswith(b'\x89PNG'):
        return 'png'
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp'
    return None


def safe_name(s):
    s = re.sub(r'[^a-zA-Z0-9._-]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-').lower()


picked = json.load(io.open(PICKS, encoding='utf-8'))
ok, fail, report = 0, [], {}

for sid, rows in picked.items():
    print(f'=== {sid} ===')
    report[sid] = []
    for i, r in enumerate(rows):
        existing = [p for p in OUT.glob(f'{sid}-{i+1:02d}-*')
                    if p.suffix.lower() in ('.jpg', '.png', '.webp')
                    and p.stat().st_size > 3000]
        if existing:
            f = existing[0]
            print(f'  [{i+1}] 已有 {f.stat().st_size//1024:>4}KB  {f.name[:55]}')
            report[sid].append({**r, 'file': f'/img/ships/{f.name}'})
            ok += 1
            continue

        # thumb 字段就是 API 原值，只剥查询串
        url = (r.get('thumb') or '').split('?')[0]
        if not url:
            fail.append((sid, i, r['title'], 'no thumb url'))
            continue
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
        time.sleep(2)

io.open(ROOT / 'work' / 'shipimg' / 'download_report.json',
        'w', encoding='utf-8').write(json.dumps(report, ensure_ascii=False, indent=2))

print()
print(f'成功 {ok} 张，失败 {len(fail)} 张')
for f in fail:
    print('  !', f[0], f'[{f[1]}]', f[2][:50], '|', f[3][:50])
