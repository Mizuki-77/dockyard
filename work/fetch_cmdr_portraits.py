# 抓 6 位指挥官的肖像照。
#
# 照片来源已验证可用（上一轮 probe 出来的 pageimages）。
# 下载走 thumb.wikimedia.org 的缩略图，并逐个校验文件头 ——
# 这条规矩是上一轮用四个版本换来的（见 docs/49 §5.2）：
#   upload.wikimedia.org 对本站持续 429，
#   凡是 upload 直链都要改写成 /thumb/ 形式的缩略图。
import io
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'commanders'
OUT.mkdir(parents=True, exist_ok=True)

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

data = json.load(io.open(ROOT / 'work' / 'cmdr13_data.json', encoding='utf-8'))


def to_thumb(url, width=720):
    u = (url or '').split('?')[0]
    if not u:
        return None
    if '//thumb.wikimedia.org/' in u:
        return u
    m = re.match(
        r'^https://upload\.wikimedia\.org/wikipedia/commons/'
        r'([0-9a-f])/([0-9a-f]{2})/([^/]+)$', u)
    if not m:
        return u
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
                time.sleep(10 + a * 10)
                continue
            print(f'        HTTP {e.code}')
            if a == retries - 1:
                return None
            time.sleep(8)
        except Exception as e:
            if a == retries - 1:
                print(f'        ERR {type(e).__name__}')
                return None
            time.sleep(8)
    return None


def ext_of(d):
    if d.startswith(b'\xff\xd8'):
        return 'jpg'
    if d.startswith(b'\x89PNG'):
        return 'png'
    if d[:4] == b'RIFF' and d[8:12] == b'WEBP':
        return 'webp'
    return None


report = {}
for pid, v in sorted(data.items()):
    if not v.get('image'):
        print(f'  -  {pid}: 无照片，跳过')
        continue
    url = to_thumb(v['image'])
    blob = fetch(url)
    if not blob:
        print(f'  !  {pid}: 下载失败')
        continue
    ext = ext_of(blob)
    if not ext:
        print(f'  !  {pid}: 非图片（{len(blob)}B）')
        continue
    fname = f'{pid}.{ext}'
    (OUT / fname).write_bytes(blob)
    report[pid] = {
        'file': f'/img/commanders/{fname}',
        'bytes': len(blob),
        'wiki': v['wiki_url'],
        'person': v['person'],
    }
    print(f'  OK {len(blob)//1024:>4}KB  {fname}')
    time.sleep(2)

io.open(ROOT / 'work' / 'cmdr_portraits.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print(f'成功 {len(report)} 张')
