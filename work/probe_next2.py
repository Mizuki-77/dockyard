import re
import urllib.request

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0 Safari/537.36')

CANDIDATES = [
    # kbismarck 的命名惯例可能是下划线
    ('kbismarck-prinz-eugen-alt', 'https://www.kbismarck.com/prinz_eugen.html', ['Prinz']),
    ('kbismarck-rodney-alt', 'https://www.kbismarck.com/rodney.htm', ['Rodney']),
    ('kbismarck-bismarck-index', 'https://www.kbismarck.com/', ['Rodney', 'Prinz']),
    # 罗德尼：NavWeaps 有 16in 页，另外 KBismarck 的 last-battle 页已有
    ('navweaps-16in', 'https://www.navweaps.com/Weapons/WNBR_16-45_mk1.php', ['16"/45']),
    # NHHC 行动报告索引
    ('nhhc-action-reports', 'https://www.history.navy.mil/research/archives/digital-exhibits-highlights/action-reports.html', ['action']),
    # 威尔士亲王：Commons 有分类，也可以用 Wikipedia 找线索（不作数据源）
    ('nhhc-pow-search', 'https://www.history.navy.mil/search.html?q=Prince+of+Wales', ['Prince']),
]

for sid, url, needles in CANDIDATES:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            code = r.getcode()
            html = r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        print(f'{sid:<30} HTTP {e.code}')
        continue
    except Exception as e:
        print(f'{sid:<30} {type(e).__name__}')
        continue
    text = ' '.join(re.sub(r'<[^>]+>', ' ', html).split())
    hits = {n: text.lower().count(n.lower()) for n in needles}
    print(f'{sid:<30} {code}  len {len(text):<7} {hits}')
    if sid == 'kbismarck-bismarck-index':
        # 打印所有含 rodney / prinz 的链接
        links = set(re.findall(r'href="([^"]+)"', html))
        rel = [x for x in links if re.search(r'rodney|prinz|eugen', x, re.I)]
        print('   相关链接:', rel[:10])
