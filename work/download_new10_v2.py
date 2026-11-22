# 下载挑好的图（第二版）。
#
# 第一版失败 34 张，原因有两个，都是 URL 处理问题：
#   ① imageinfo 返回的 thumburl 带 ?utm_source=... 查询串，拼进路径就 404
#      或返回 HTML 错误页（被文件头校验拦下，没污染数据 —— 校验生效了）；
#   ② 原图宽度不足 1280 时，iiurlwidth=1280 返回的是**未缩放原图**，
#      也就是 upload.wikimedia.org 的直链，不是 /thumb/ 路径。
#
# 修法：
#   - 先剥掉查询串；
#   - 判断是「原图直链」还是「缩略图直链」：
#       有 /thumb/  → 缩略图，改宽度段；域名换 thumb.
#       没有 /thumb/ → 原图（说明它本来就小于目标宽度），原样下载，
#                     域名保持 upload.（试过换 thumb. 会 404）
#   - 仍然逐个校验 \xff\xd8，PNG 单独认 \x89PNG（zulu 那张是 png）。
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

LEGAL_WIDTHS = [120, 250, 330, 500, 960, 1280, 1920, 3840]


def normalize(url, width=1280):
    """剥查询串；按 /thumb/ 判断是缩略图还是原图。"""
    if not url:
        return None, None
    u = url.split('?')[0]
    is_thumb = '/thumb/' in u
    if is_thumb:
        # 改宽度段（合法档位）
        m = re.search(r'/(\d+)px-', u)
        if m:
            u = u[:m.start(1)] + str(width) + u[m.end(1):]
        u = u.replace('//upload.wikimedia.org/', '//thumb.wikimedia.org/')
        return u, 'thumb'
    # 原图：保持 upload 域名
    return u, 'original'


def fetch(url, retries=6):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read(), r.headers.get('Content-Type', '')
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 25 + a * 25
                print(f'        429 wait {w}s')
                time.sleep(w)
                continue
            print(f'        HTTP {e.code}')
            if a == retries - 1:
                return None, ''
            time.sleep(10)
        except Exception as e:
            if a == retries - 1:
                print(f'        ERR {e}')
                return None, ''
            time.sleep(10)
    return None, ''


def is_image(data, ctype):
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
ok, fail, skipped = 0, [], 0
report = {}

for sid, rows in picked.items():
    print(f'=== {sid} ===')
    report[sid] = []
    for i, r in enumerate(rows):
        # 已经下成功的先认出来（第一版下的 25 张就靠这个跳过）
        existing = list(OUT.glob(f'{sid}-{i+1:02d}-*.jpg')) + \
                   list(OUT.glob(f'{sid}-{i+1:02d}-*.png'))
        if existing and existing[0].stat().st_size > 3000:
            f = existing[0]
            print(f'  [{i+1}] 已存在 {f.stat().st_size//1024} KB  {f.name[:60]}')
            report[sid].append({**r, 'file': f'/img/ships/{f.name}'})
            ok += 1
            continue

        url, kind = normalize(r.get('thumb') or r.get('page'))
        data, ctype = fetch(url)
        if not data:
            fail.append((sid, i, r['title'], 'fetch failed'))
            continue

        ext = is_image(data, ctype)
        if not ext:
            fail.append((sid, i, r['title'], f'HEAD={data[:40]!r}'))
            print(f'  [{i+1}] 不是图片，丢弃（{len(data)} 字节）')
            continue

        base = safe_name(r['title'].rsplit('.', 1)[0])[:50]
        fname = f'{sid}-{i+1:02d}-{base}.{ext}'
        dst = OUT / fname
        dst.write_bytes(data)
        print(f'  [{i+1}] OK {len(data)//1024:>5} KB [{kind}] {fname[:60]}')
        report[sid].append({**r, 'file': f'/img/ships/{fname}'})
        ok += 1
        time.sleep(2.5)

io.open(ROOT / 'work' / 'shipimg' / 'download_report.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print(f'成功 {ok} 张，失败 {len(fail)} 张')
for f in fail:
    print('  !', f[0], f[1], f[2][:55], '|', f[3][:60])
