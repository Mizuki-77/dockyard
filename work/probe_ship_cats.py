# 探 18 艘新舰在 Commons 的分类与可用图片量
# 规矩（docs/45 §3.1 + 交接报告 §7.2）：必须按 Category 浏览，不用关键词搜索
import json
import ssl
import time
import urllib.parse
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDR = {'User-Agent': 'DockyardArchive/1.0 (research; low-rate)'}
API = 'https://commons.wikimedia.org/w/api.php'

# 按 docs/45 §3.1 的命名规律给候选分类
SHIPS = {
    # 日本：<名> (ship, <下水年>)
    'tone': ['Tone (ship, 1937)'],
    'chikuma': ['Chikuma (ship, 1938)'],
    'haruna': ['Haruna (ship, 1913)'],
    'kirishima': ['Kirishima (ship, 1913)'],
    'hosho': ['Hōshō (ship, 1921)', 'Hosho (ship, 1921)'],
    'nagara': ['Nagara (ship, 1921)'],
    'sendai': ['Sendai (ship, 1923)'],
    # 美国：USS <名> (<舷号>)
    'astoria': ['USS Astoria (CA-34)'],
    'portland': ['USS Portland (CA-33)'],
    'minneapolis': ['USS Minneapolis (CA-36)'],
    'new-orleans': ['USS New Orleans (CA-32)'],
    'vincennes': ['USS Vincennes (CA-44)'],
    'northampton': ['USS Northampton (CA-26)'],
    'pensacola': ['USS Pensacola (CA-24)'],
    'atlanta': ['USS Atlanta (CL-51)'],
    'hammann': ['USS Hammann (DD-412)'],
    'monaghan': ['USS Monaghan (DD-354)'],
    'benham': ['USS Benham (DD-397)'],
}


def api(params, tries=6):
    url = API + '?' + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HDR)
            with urllib.request.urlopen(req, timeout=40, context=ctx) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(5 * (i + 1))
                continue
            raise
    return {}


def cat_files(cat, limit=500):
    j = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:' + cat,
             'cmtype': 'file', 'cmlimit': str(limit), 'format': 'json'})
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


print(f'{"舰":14} {"分类":28} {"图片数":>6}  说明')
print('=' * 78)
total = 0
for sid, cats in SHIPS.items():
    line = None
    for c in cats:
        try:
            files = cat_files(c)
        except Exception as e:
            files = []
        time.sleep(1.8)
        if files:
            # 排除视频
            imgs = [f for f in files if not f.lower().endswith(('.ogv', '.webm', '.ogg'))]
            line = (c, len(imgs))
            total += len(imgs)
            break
    if line:
        print(f'{sid:14} {line[0]:28} {line[1]:>6}')
    else:
        print(f'{sid:14} {"— 分类未找到":28} {0:>6}  ← 需换名重试')

print('=' * 78)
print(f'合计可用 {total} 张（目标每舰 10-15 张，18 舰约需 180-270 张）')
