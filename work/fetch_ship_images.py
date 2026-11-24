# 为 18 艘新舰下载配图（目标每舰 10-15 张，A 档 PD/CC0 落盘）
#
# 分类名已用 search 逐个核实（2026-11-24 夜），不是我猜的下水年：
#   利根 Tone (ship, 1938) / 筑摩 Chikuma (ship, 1939) / 榛名 Haruna (ship, 1915)
#   雾岛 Kirishima (ship, 1915) / 凤翔 Hōshō (ship, 1922) / 长良 Nagara (ship, 1922)
#   川内 Sendai (ship, 1924)
#
# 硬规矩（docs/45 §3.1 + 交接报告 §7.2）：
#   1. 按 Category 浏览，不用关键词搜索
#   2. thumburl 用 API 原值；upload 直链被 429 时改 thumb.wikimedia.org 且保留 /thumb/
#   3. 下载后校验文件头 \xff\xd8 或 \x89PNG
#   4. 排除 .ogv/.webm 视频
#   5. 缩略宽度只用合法档位
#   6. Artist 字段是 HTML，剥标签
#   7. 只取 PD/CC0（A 档落盘）；CC-BY 类记 B 档外链
import html
import io
import json
import os
import re
import time

import yaml

from commons_client import api

OUTROOT = 'public/img/ships'
VALID_WIDTHS = [120, 250, 330, 500, 960, 1280, 1920, 3840]
WIDTH = 1280

# 舰 id → (Commons 分类, 中文名)
PLAN = {
    'tone': ('Tone (ship, 1938)', '利根号'),
    'chikuma': ('Chikuma (ship, 1939)', '筑摩号'),
    'haruna': ('Haruna (ship, 1915)', '榛名号'),
    'kirishima': ('Kirishima (ship, 1915)', '雾岛号'),
    'hosho': ('Hōshō (ship, 1922)', '凤翔号'),
    'nagara': ('Nagara (ship, 1922)', '长良号'),
    'sendai': ('Sendai (ship, 1924)', '川内号'),
    'astoria': ('USS Astoria (CA-34)', '阿斯托里亚号'),
    'portland': ('USS Portland (CA-33)', '波特兰号'),
    'minneapolis': ('USS Minneapolis (CA-36)', '明尼阿波利斯号'),
    'new-orleans': ('USS New Orleans (CA-32)', '新奥尔良号'),
    'vincennes': ('USS Vincennes (CA-44)', '文森斯号'),
    'northampton': ('USS Northampton (CA-26)', '北安普敦号'),
    'pensacola': ('USS Pensacola (CA-24)', '彭萨科拉号'),
    'atlanta': ('USS Atlanta (CL-51)', '亚特兰大号'),
    'hammann': ('USS Hammann (DD-412)', '哈曼号'),
    'monaghan': ('USS Monaghan (DD-354)', '莫纳汉号'),
    'benham': ('USS Benham (DD-397)', '本汉号'),
}

MAX_PER_SHIP = 15
TARGET_MIN = 10


def strip_tags(s):
    if not s:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', str(s))).strip()


def cat_files(cat, limit=500):
    j = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:' + cat, 'cmtype': 'file',
             'cmlimit': str(limit), 'format': 'json'})
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


def file_infos(titles, batch=20):
    """批量取 imageinfo（一次 20 个，省调用）"""
    out = {}
    for i in range(0, len(titles), batch):
        chunk = titles[i:i + batch]
        j = api({'action': 'query', 'titles': '|'.join(chunk),
                 'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata',
                 'iiurlwidth': str(WIDTH), 'format': 'json'})
        pages = j.get('query', {}).get('pages') or {}
        for _, p in pages.items():
            ii = (p.get('imageinfo') or [None])[0]
            if ii:
                out[p.get('title')] = ii
        time.sleep(1.2)
    return out


def lic_of(ii):
    md = ii.get('extmetadata') or {}
    return strip_tags(md.get('LicenseShortName', {}).get('value', ''))


def is_a_tier(lic):
    l = lic.lower()
    return ('public domain' in l or l == 'pd' or l.startswith('pd-')
            or 'cc0' in l or 'pd' in l.split(';')[0])


def rewrite_thumb(url):
    """upload.wikimedia.org/.../d/df/N.jpg → thumb.wikimedia.org/.../thumb/d/df/N.jpg/960px-N.jpg"""
    if '/thumb/' in url:
        return url
    m = re.match(r'https?://upload\.wikimedia\.org(/wikipedia/commons)/(.)/(..)/([^/]+)$', url)
    if not m:
        return url
    base, h1, h2, fname = m.groups()
    stem = fname.rsplit('.', 1)[0]
    return (f'https://thumb.wikimedia.org{base}/thumb/{h1}/{h2}/{fname}/'
            f'{WIDTH}px-{stem}.jpg')


def fetch_bytes(urls):
    import ssl
    import urllib.request
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({'http': 'http://127.0.0.1:12450',
                                     'https': 'http://127.0.0.1:12450'}),
        urllib.request.HTTPSHandler(context=ctx))
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'DockyardArchive/1.0'})
            with opener.open(req, timeout=90) as f:
                data = f.read()
            if data[:2] == b'\xff\xd8' or data[:4] == b'\x89PNG':
                return data
        except Exception:
            time.sleep(2)
            continue
    return None


def main():
    catalog = {}
    report = []

    for sid, (cat, zh) in PLAN.items():
        print(f'\n========== {sid} ({zh})  [{cat}]')
        try:
            files = cat_files(cat)
        except Exception as e:
            print('   取分类失败', type(e).__name__)
            report.append((sid, 0, '分类失败'))
            continue

        cand = [f for f in files if not f.lower().endswith(('.ogv', '.webm', '.ogg'))
                and os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png')]
        print(f'   候选文件 {len(cand)} / 分类内 {len(files)}')
        if not cand:
            report.append((sid, 0, '无可用格式'))
            continue

        infos = file_infos(cand)
        time.sleep(1.5)

        outdir = os.path.join(OUTROOT)
        os.makedirs(outdir, exist_ok=True)

        got = 0
        entries = []
        skipped_b = 0
        for ft in cand:
            if got >= MAX_PER_SHIP:
                break
            ii = infos.get(ft)
            if not ii:
                continue
            lic = lic_of(ii)
            if not is_a_tier(lic):
                skipped_b += 1
                continue

            urls = []
            if ii.get('thumburl'):
                urls.append(ii['thumburl'])
            if ii.get('url'):
                urls.append(rewrite_thumb(ii['url']))
                urls.append(ii['url'])

            data = fetch_bytes(urls)
            if not data:
                print(f'      拿不到 {ft[:52]}')
                continue

            # 文件名：shipid-序号-短名
            base = re.sub(r'[^A-Za-z0-9]+', '-', ft.replace('File:', '').rsplit('.', 1)[0])
            base = base.strip('-')[:48]
            fn = f'{sid}-{got + 1:02d}-{base}.jpg'
            with open(os.path.join(outdir, fn), 'wb') as f:
                f.write(data)

            md = ii.get('extmetadata') or {}
            entries.append({
                'file': f'/img/ships/{fn}',
                'subject': f'ship:{sid}',
                'commons_title': ft,
                'license_raw': lic,
                'author': strip_tags(md.get('Artist', {}).get('value', ''))[:120],
                'credit': strip_tags(md.get('Credit', {}).get('value', ''))[:120],
                'source_url': 'https://commons.wikimedia.org/wiki/' + ft.replace(' ', '_'),
                'width': ii.get('width'),
                'height': ii.get('height'),
                'descr': strip_tags(md.get('ImageDescription', {}).get('value', ''))[:300],
                'date': strip_tags(md.get('DateTimeOriginal', {}).get('value', ''))[:40],
            })
            got += 1
            print(f'      [{got:>2}] {fn}  ({len(data)//1024}KB, {lic})')
            time.sleep(1.8)

        catalog[sid] = entries
        note = f'{got} 张' + (f'（跳过非 A 档 {skipped_b}）' if skipped_b else '')
        if got < TARGET_MIN:
            note += f'  ← 低于 {TARGET_MIN}，素材上限'
        report.append((sid, got, note))
        print(f'   → {note}')

    # 落盘元数据（供下一步分类与登记用）
    with io.open('work/_ship_images_raw.yaml', 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump({'ships': catalog}, f, allow_unicode=True,
                       sort_keys=False, default_flow_style=False, indent=2, width=200)

    print('\n\n========== 汇总 ==========')
    tot = 0
    for sid, n, note in report:
        print(f'  {sid:14} {n:>3}  {note}')
        tot += n
    print(f'  合计 {tot} 张')
    print('  元数据: work/_ship_images_raw.yaml')


if __name__ == '__main__':
    main()
