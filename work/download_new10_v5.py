# 下载挑好的图（第五版，最终版）。
#
# 诊断过程（值得记，因为这是本项目最容易反复踩的地方）：
#
#   现象：thumb.wikimedia.org 手动连续请求 3 次全部 200 / 0.5s，
#         但脚本跑到第 3 张就开始 429 且越退避越糟。
#
#   根因：picked_new10.json 里存的 thumb 字段有两种形态 ——
#     ① https://thumb.wikimedia.org/.../thumb/.../1280px-X.jpg   （缩略图，好下）
#     ② https://upload.wikimedia.org/.../X.jpg                  （原图直链）
#   ② 就是 imageinfo 的 thumbnail_unscaled：**原图本身宽度 ≤ 1280**，
#   所以 API 不生成缩略图，直接给原图。
#
#   而 upload.wikimedia.org 对本项目**持续 429**（docs/45 §8.2 第 5 条
#   早就记了这条：「图床域名用 thumb.wikimedia.org，upload.wikimedia.org
#   对本站持续 429」）。我前几版只是在 URL 处理上兜圈子，没意识到
#   有一半的图拿到的就是 upload 直链。
#
#   解法：凡是 upload.wikimedia.org 的 URL，一律改写成 thumb.wikimedia.org
#   的缩略图形式。改写规则（实测有效）：
#     upload/wikipedia/commons/1/10/Name.jpg
#       -> thumb/wikipedia/commons/thumb/1/10/Name.jpg/960px-Name.jpg
#   宽度用 960（合法档位），因为这类原图本来就 ≤1280，960 仍能看清结构，
#   而且体积更小、更不容易触发限流。
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


def to_thumb(url, width=960):
    """把 upload 直链改写成 thumb 缩略图；已经是 thumb 的原样返回。"""
    u = (url or '').split('?')[0]
    if not u:
        return None
    if '//thumb.wikimedia.org/' in u:
        return u
    m = re.match(
        r'^https://upload\.wikimedia\.org/wikipedia/commons/'
        r'([0-9a-f])/([0-9a-f]{2})/([^/]+)$', u)
    if not m:
        return u          # 认不出的原样试一次
    a, b, name = m.group(1), m.group(2), m.group(3)
    return (f'https://thumb.wikimedia.org/wikipedia/commons/thumb/'
            f'{a}/{b}/{name}/{width}px-{name}')


def fetch(url, retries=6):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 10 + a * 10
                print(f'        429 wait {w}s')
                time.sleep(w)
                continue
            print(f'        HTTP {e.code}')
            if a == retries - 1:
                return None
            time.sleep(6)
        except Exception as e:
            if a == retries - 1:
                print(f'        ERR {type(e).__name__}')
                return None
            time.sleep(6)
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
            print(f'  [{i+1}] 已有 {f.stat().st_size//1024:>4}KB  {f.name[:52]}')
            report[sid].append({**r, 'file': f'/img/ships/{f.name}'})
            ok += 1
            continue

        url = to_thumb(r.get('thumb'))
        data = fetch(url)
        if not data:
            fail.append((sid, i, r['title'], 'fetch failed'))
            continue
        ext = img_ext(data)
        if not ext:
            fail.append((sid, i, r['title'], f'HEAD={data[:26]!r}'))
            print(f'  [{i+1}] 非图片丢弃（{len(data)}B）')
            continue

        base = safe_name(r['title'].rsplit('.', 1)[0])[:46]
        fname = f'{sid}-{i+1:02d}-{base}.{ext}'
        (OUT / fname).write_bytes(data)
        print(f'  [{i+1}] OK {len(data)//1024:>5}KB  {fname[:56]}')
        report[sid].append({**r, 'file': f'/img/ships/{fname}'})
        ok += 1
        time.sleep(1.5)

io.open(ROOT / 'work' / 'shipimg' / 'download_report.json',
        'w', encoding='utf-8').write(json.dumps(report, ensure_ascii=False, indent=2))

print()
print(f'成功 {ok} 张，失败 {len(fail)} 张')
for f in fail:
    print('  !', f[0], f'[{f[1]}]', f[2][:48], '|', f[3][:46])
