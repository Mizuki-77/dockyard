# 德语维基只用来「找线索」—— 定下它的参考文献列表，看有没有可及的原始资料。
# 按项目规矩，维基是 tier E，只能作 lead，不能作 fact 的 src。
import json
import re
import urllib.parse
import urllib.request

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0 Safari/537.36')

TITLES = ['Prinz_Eugen_(Schiff,_1938)', 'Schwerer_Kreuzer_Prinz_Eugen']

for t in TITLES:
    url = f'https://de.wikipedia.org/wiki/{urllib.parse.quote(t)}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode('utf-8', 'replace')
    except Exception as e:
        print(f'{t}: {type(e).__name__}')
        continue

    text = ' '.join(re.sub(r'<[^>]+>', ' ', html).split())
    print(f'=== {t} ===')
    print(f'  长度 {len(text)}')
    # 打印参考文献节里出现的书名/作者
    m = re.search(r'(Literatur|Quellen).{0,2500}', html, re.S)
    if m:
        seg = ' '.join(re.sub(r'<[^>]+>', ' ', m.group(0)).split())
        print('  参考文献片段:')
        print('   ', seg[:1200])
    print()
