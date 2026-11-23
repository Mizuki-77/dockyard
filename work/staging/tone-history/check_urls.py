import re, os, urllib.request, ssl, time

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RESEARCH-NOTES.md')
txt = open(p, encoding='utf-8').read()

urls = sorted(set(re.findall(r'<(https?://[^>\s]+)>', txt)))
print(f'found {len(urls)} unique urls in RESEARCH-NOTES.md\n')

HDRS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

bad = []
for u in urls:
    try:
        req = urllib.request.Request(u, headers=HDRS)
        r = urllib.request.urlopen(req, timeout=25, context=ctx)
        r.read(200)
        print(f'  OK   {r.status}  {u}')
    except Exception as e:
        print(f'  FAIL {type(e).__name__}: {str(e)[:70]}  {u}')
        bad.append((u, str(e)[:90]))
    time.sleep(0.4)

print(f'\n{len(bad)} failures')
for u, e in bad:
    print(' ', u, '::', e)
