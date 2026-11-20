# 验证 B5N 相关来源页面
import re
import urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

TARGETS = [
    ('combinedfleet-b5n', 'http://www.combinedfleet.com/ijna/b5n.htm', ['B5N', 'Span', 'Weight']),
    ('avh-b5n', 'https://www.aviation-history.com/nakajima/b5n.html', ['B5N', 'Kate']),
    ('navweaps-5in25-mk10', 'https://www.navweaps.com/Weapons/WNUS_5-25_mk10.php', ['5"/25', 'Mark 10']),
]

for sid, url, needles in TARGETS:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode('utf-8', 'replace')
    except Exception as e:
        print(f'{sid}: 失败 {e}')
        continue
    text = ' '.join(re.sub(r'<[^>]+>', ' ', html).split())
    print(f'\n=== {sid} ===')
    print(f'  长度 {len(text)}')
    for n in needles:
        print(f'  「{n}」{text.lower().count(n.lower())} 次')
    m = re.search(r'.{40}(Span|Width).{120}', text, re.I)
    if m:
        print('  样例: ...' + m.group(0)[:170].strip() + '...')
