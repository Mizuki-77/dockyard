# 为武器实体下载配图并写进 images.yaml
#
# 规矩（交接报告 §7.2）：
#   - 按 Category 浏览，不用关键词搜索
#   - thumburl 用 API 原值，不自己拼
#   - 只用合法缩略宽度 120/250/330/500/960/1280/1920/3840
#   - 下载后必须校验文件头 \xff\xd8 或 \x89PNG
#   - 排除 .ogv/.webm 视频
#   - Artist 字段是 HTML，必须剥标签
#   - 只取 PD/CC0（A 档归档），有署名义务的走 B 档外链（本轮先只做 A 档）
import html
import io
import json
import os
import re
import ssl
import time
import urllib.parse
import urllib.request

import yaml

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDR = {'User-Agent': 'DockyardArchive/1.0 (research; low-rate)'}
API = 'https://commons.wikimedia.org/w/api.php'
OUTDIR = 'public/img/weapons'

# 已确认有文件的分类（每个取 1 张，优先 A 档 PD/CC0）
PLAN = {
    '14cm-50-3ns': 'Category:14 cm/50 3rd Year Type naval gun',
    '20cm-3ns-no2': 'Category:20 cm/50 3rd Year Type naval gun',
    '36cm-45-t41': 'Category:41 cm/45 3rd Year Type naval gun',
    '8cm-40-3ns': 'Category:Type 3 8cm AA Gun',
    '15cm-50-t41': 'Category:15.5 cm/60 3rd Year Type',
    '5in25-mk10': 'Category:5"/25 caliber gun (United States)',
    '8in-55-mk9': 'Category:8"/55 caliber gun',
    '21in-mk15': 'Category:Mark 15 torpedo',
    'a5m4': 'Category:Mitsubishi A5M',
    'b4y1': 'Category:Yokosuka B4Y',
    '47in-45-mk12': 'Category:QF 4.7 inch Mk IX Mk XII naval gun',
}

VALID_WIDTHS = [120, 250, 330, 500, 960, 1280, 1920, 3840]


def api(params, tries=5):
    url = API + '?' + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HDR)
            with urllib.request.urlopen(req, timeout=45, context=ctx) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(4 * (i + 1))
                continue
            raise
    return {}


def strip_tags(s):
    if not s:
        return ''
    s = re.sub(r'<[^>]+>', '', str(s))
    return html.unescape(s).strip()


def cat_files(cat, limit=12):
    j = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': cat,
             'cmtype': 'file', 'cmlimit': str(limit), 'format': 'json'})
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


def file_info(title):
    j = api({'action': 'query', 'titles': title, 'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata', 'iiurlwidth': '1280',
             'format': 'json'})
    pages = j.get('query', {}).get('pages') or {}
    for _, p in pages.items():
        ii = (p.get('imageinfo') or [None])[0]
        if ii:
            return ii
    return None


def is_free(ii):
    """判定是否 A 档（PD / CC0）"""
    md = ii.get('extmetadata') or {}
    lic = strip_tags(md.get('LicenseShortName', {}).get('value', '')).lower()
    return any(k in lic for k in ('public domain', 'pd', 'cc0'))


os.makedirs(OUTDIR, exist_ok=True)

entries = []
print('武器配图下载')
print('=' * 70)
for wid, cat in PLAN.items():
    print(f'\n--- {wid}')
    try:
        files = cat_files(cat)
    except Exception as e:
        print(f'    取分类失败: {type(e).__name__}')
        continue
    time.sleep(1.5)

    picked = None
    for ft in files:
        # 排除视频
        if ft.lower().endswith(('.ogv', '.webm', '.ogg')):
            continue
        try:
            ii = file_info(ft)
        except Exception:
            continue
        time.sleep(1.2)
        if not ii:
            continue
        if not is_free(ii):
            continue
        picked = (ft, ii)
        break

    if not picked:
        print('    无 A 档（PD/CC0）可用图，跳过')
        continue

    ft, ii = picked
    thumb = ii.get('thumburl') or ii.get('url')
    if not thumb:
        print('    无缩略图 URL，跳过')
        continue

    # 文件名
    base = re.sub(r'[^A-Za-z0-9._-]', '-', ft.replace('File:', ''))
    ext = os.path.splitext(base)[1].lower()
    if ext not in ('.jpg', '.jpeg', '.png'):
        print(f'    扩展名 {ext} 不接受，跳过')
        continue
    fn = f'{wid}{ext}'
    dst = os.path.join(OUTDIR, fn)

    try:
        req = urllib.request.Request(thumb, headers=HDR)
        with urllib.request.urlopen(req, timeout=60, context=ctx) as f:
            data = f.read()
    except Exception as e:
        print(f'    下载失败: {type(e).__name__}')
        continue
    time.sleep(1.5)

    # 文件头校验（§7.2 第 4 条）
    if not (data[:2] == b'\xff\xd8' or data[:8] == b'\x89PNG\r\n\x1a\n' or data[:4] == b'\x89PNG'):
        print(f'    文件头不对（可能是 HTML 错误页），丢弃。前16字节={data[:16]}')
        continue

    with open(dst, 'wb') as f:
        f.write(data)

    md = ii.get('extmetadata') or {}
    entries.append({
        'id': f'weapon-{wid}-main',
        'file': f'/img/weapons/{fn}',
        'subject': f'weapon:{wid}',
        'title': {'zh': f'{wid} 实物照', 'en': strip_tags(md.get('ObjectName', {}).get('value', '')) or ft},
        'license': 'pd',
        'license_tier': 'A',
        'license_raw': strip_tags(md.get('LicenseShortName', {}).get('value', '')),
        'author': strip_tags(md.get('Artist', {}).get('value', ''))[:120],
        'credit': strip_tags(md.get('Credit', {}).get('value', ''))[:120],
        'source_url': 'https://commons.wikimedia.org/wiki/' + urllib.parse.quote(ft.replace(' ', '_')),
        'width': ii.get('width'),
        'height': ii.get('height'),
        'primary': True,
    })
    print(f'    ✓ {fn}  ({len(data)} bytes)  {ft}')

print(f'\n\n成功 {len(entries)} 张')
if entries:
    with io.open('work/_weapon_images_fragment.yaml', 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump({'images': entries}, f, allow_unicode=True,
                       sort_keys=False, default_flow_style=False, indent=2, width=200)
    print('分片写到 work/_weapon_images_fragment.yaml')
