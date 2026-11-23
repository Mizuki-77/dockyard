# 为缺图的 13 个武器实体在 Commons 找候选图
# 规矩来自交接报告 §7.2：必须按 Category 浏览，不要用关键词搜索
import json
import urllib.parse
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDR = {'User-Agent': 'DockyardArchive/1.0 (research; contact via site)'}
API = 'https://commons.wikimedia.org/w/api.php'

# 武器 id → 候选 Commons 分类名
TARGETS = {
    '14cm-50-3ns': ['Category:14 cm/50 3rd Year Type naval gun',
                    'Category:Type 3 140 mm naval gun'],
    '15cm-50-t41': ['Category:15.5 cm/50 3rd Year Type naval gun',
                    'Category:Type 3 155 mm naval gun'],
    '36cm-45-t41': ['Category:36 cm/45 41st Year Type naval gun',
                    'Category:41 cm/45 3rd Year Type naval gun'],
    '8cm-40-3ns': ['Category:8 cm/40 3rd Year Type naval gun',
                   'Category:Type 88 75 mm AA gun'],
    '5in25-mk10': ['Category:5"/25 caliber gun',
                   'Category:5 inch/25 caliber gun'],
    '8in-55-mk9': ['Category:8"/55 caliber gun',
                   'Category:8 inch/55 caliber gun'],
    '8in-55-mk15': ['Category:8"/55 caliber gun'],
    '21in-mk15': ['Category:Mark 15 torpedo',
                  'Category:21 inch torpedo'],
    'a5m4': ['Category:Mitsubishi A5M'],
    'b4y1': ['Category:Yokosuka B4Y'],
    '20cm-3ns-no2': ['Category:20 cm/50 3rd Year Type naval gun'],
    '45in-45-mk1': ['Category:QF 4.5 inch naval gun'],
    '47in-45-mk12': ['Category:QF 4.7 inch Mark IX naval gun',
                     'Category:4.7 inch QF gun'],
}


def cat_members(cat):
    """按分类取文件成员（Commons 规矩：浏览 Category 而非关键词搜索）"""
    q = urllib.parse.urlencode({
        'action': 'query', 'list': 'categorymembers',
        'cmtitle': cat, 'cmtype': 'file', 'cmlimit': '10', 'format': 'json',
    })
    req = urllib.request.Request(API + '?' + q, headers=HDR)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as f:
        j = json.load(f)
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


def cat_exists(cat):
    q = urllib.parse.urlencode({
        'action': 'query', 'titles': cat, 'format': 'json',
    })
    req = urllib.request.Request(API + '?' + q, headers=HDR)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as f:
        j = json.load(f)
    pages = j.get('query', {}).get('pages') or {}
    return not any('missing' in p for p in pages.values())


print('武器配图候选盘点（按 Commons Category 浏览）')
print('=' * 70)
found = {}
for wid, cats in TARGETS.items():
    hit = None
    for c in cats:
        try:
            if not cat_exists(c):
                continue
            files = cat_members(c)
            if files:
                hit = (c, files)
                break
        except Exception as e:
            print(f'  ! {wid} / {c}: {type(e).__name__}')
    if hit:
        found[wid] = hit
        print(f'\n[有] {wid}')
        print(f'     分类: {hit[0]}  ({len(hit[1])} 个文件)')
        for f in hit[1][:4]:
            print(f'       - {f}')
    else:
        print(f'\n[无] {wid}')
        for c in cats:
            print(f'      试过: {c}')

print()
print(f'共 {len(found)}/{len(TARGETS)} 有候选分类')
