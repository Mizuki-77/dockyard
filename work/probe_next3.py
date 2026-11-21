import re
import urllib.request

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0 Safari/537.36')

# 三艘舰实际能用上的来源，逐个实测
TARGETS = [
    # 罗德尼 —— 该舰战报已登记，实测确认
    ('kbismarck-rodney-report (已登记)',
     'https://www.kbismarck.com/rodney-gunnery-report.html', ['Rodney']),
    ('navweaps-16in-45-mk1 (已登记)',
     'https://www.navweaps.com/Weapons/WNBR_16-45_mk1.php', ['16"/45']),

    # 欧根亲王 —— 该舰的 20.3 cm 主炮
    ('navweaps-20-3-sk-c34 (待登记)',
     'https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php', ['SK C/34']),
    ('kbismarck 首页 Prinz Eugen 链接',
     'https://www.kbismarck.com/prinz-eugen.html', ['Prinz']),

    # 威尔士亲王 —— KGV 级已有，查该级主炮页
    ('navweaps-14in-45-mk7 (已登记)',
     'https://www.navweaps.com/Weapons/WNBR_14-45_mk7.php', ['14"/45']),

    # 丹麦海峡已有
    ('kbismarck-denmark-strait (已登记)',
     'https://www.kbismarck.com/denmark-strait-battle.html', ['Hood', 'Prince of Wales']),

    # 纳尔逊级舰级数据
    ('kbismarck-nelson?',
     'https://www.kbismarck.com/nelson.html', ['Nelson']),
]

for sid, url, needles in TARGETS:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            code = r.getcode()
            html = r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        print(f'{sid:<36} HTTP {e.code}')
        continue
    except Exception as e:
        print(f'{sid:<36} {type(e).__name__}')
        continue
    text = ' '.join(re.sub(r'<[^>]+>', ' ', html).split())
    hits = {n: text.lower().count(n.lower()) for n in needles}
    print(f'{sid:<36} {code}  len {len(text):<7} {hits}')
