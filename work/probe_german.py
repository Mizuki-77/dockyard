# 有限预算内探德文来源 —— 只测通不通，不抓全文。
# 欧根亲王是唯一资料缺口，值得多花这一点 token。
import re
import urllib.request

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0 Safari/537.36')

TARGETS = [
    # 德国联邦档案馆 —— sources.yaml 记着需要代理
    ('Bundesarchiv 搜索', 'https://www.bundesarchiv.de/'),
    ('Lexikon der Wehrmacht', 'https://www.lexikon-der-wehrmacht.de/'),
    ('Württembergische Landesbibliothek', 'https://www.wlb-stuttgart.de/'),
    # 德文海军专题站
    ('deutsche-kriegsmarine', 'https://www.deutsche-kriegsmarine.de/'),
    ('Schiffe der Kriegsmarine', 'https://www.kriegsmarine.de/'),
    # 已知英文站再试一次别的路径
    ('kbismarck 站点地图', 'https://www.kbismarck.com/sitemap.html'),
    ('kbismarck 舰船列表', 'https://www.kbismarck.com/schiffe.html'),
]

for sid, url in TARGETS:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=18) as r:
            code = r.getcode()
            html = r.read().decode('utf-8', 'replace')
        text = ' '.join(re.sub(r'<[^>]+>', ' ', html).split())
        # 有没有提到 Prinz Eugen / Hipper
        pe = text.lower().count('prinz eugen')
        hi = text.lower().count('hipper')
        print(f'{sid:<32} {code}  len {len(text):<7} prinz={pe} hipper={hi}')
    except urllib.error.HTTPError as e:
        print(f'{sid:<32} HTTP {e.code}')
    except Exception as e:
        print(f'{sid:<32} {type(e).__name__}')
