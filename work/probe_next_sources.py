# 第二步开工前的来源可行性实测。
# 只测「能不能抓到」，不抓全文 —— 抓不到就要在任务书里标成未获取。
import re
import urllib.request

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0 Safari/537.36')

TARGETS = [
    ('kbismarck-prinz-eugen',
     'https://www.kbismarck.com/prinzeugen.html',
     ['Prinz Eugen']),

    ('kbismarck-rodney',
     'https://www.kbismarck.com/rodney.html',
     ['Rodney']),

    ('navweaps-20-3-sk-c34',
     'https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php',
     ['SK C/34', '20.3']),

    ('nhhc-pow-midway-generic',
     'https://www.history.navy.mil/research/archives/digital-exhibits-highlights/action-reports/wwii-battle-of-midway.html',
     ['action report']),

    ('hmshood-pow',
     'https://www.hmshood.org.uk/reference/official/adm234/adm234-509guns.htm',
     ['Prince of Wales']),
]

for sid, url, needles in TARGETS:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            code = r.getcode()
            html = r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        print(f'{sid:<28} HTTP {e.code}  {url}')
        continue
    except Exception as e:
        print(f'{sid:<28} 失败 {type(e).__name__}  {url}')
        continue

    text = ' '.join(re.sub(r'<[^>]+>', ' ', html).split())
    hits = {n: text.lower().count(n.lower()) for n in needles}
    print(f'{sid:<28} {code}  长度 {len(text):<7} 命中 {hits}')
