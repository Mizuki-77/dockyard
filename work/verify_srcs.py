# 验证待登记的来源页面是否真的含有所需数据。
# 只登记「真的抓到了内容」的来源，这是 sources.yaml 头部自述的规矩。

import io
import re
import urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

TARGETS = [
    ('combinedfleet-a6m', 'http://www.combinedfleet.com/ijna/a6m.htm', ['A6M2', 'Span', 'Weight']),
    ('combinedfleet-d3a', 'http://www.combinedfleet.com/ijna/d3a.htm', ['D3A1', 'Span', 'Weight']),
    ('avh-d3a', 'https://www.aviation-history.com/aichi/d3a.html', ['D3A', 'dive', 'Heinkel']),
]

for sid, url, needles in TARGETS:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode('utf-8', 'replace')
    except Exception as e:
        print(f'{sid}: 抓取失败 {e}')
        continue
    text = re.sub(r'<[^>]+>', ' ', html)
    text = ' '.join(text.split())
    print(f'\n=== {sid} ===')
    print(f'  正文长度 {len(text)}')
    for n in needles:
        cnt = text.lower().count(n.lower())
        print(f'  「{n}」出现 {cnt} 次')
    # 打印一段含关键字的上下文
    m = re.search(r'.{80}(Span|Wing ?span).{160}', text, re.I)
    if m:
        print('  样例: ...' + m.group(0)[:230].strip() + '...')
