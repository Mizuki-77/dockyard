# 诊断「拿不到」：为什么分类里明明有的图下载失败
import ssl
import time
import urllib.request

from commons_client import api

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
PROXY = 'http://127.0.0.1:12450'
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}),
    urllib.request.HTTPSHandler(context=ctx))

TEST = 'File:USS Hammann alongside USS Yorktown.jpg'
j = api({'action': 'query', 'titles': TEST, 'prop': 'imageinfo',
         'iiprop': 'url|size', 'iiurlwidth': '1280', 'format': 'json'})
pages = j.get('query', {}).get('pages') or {}
for k, v in pages.items():
    print('title:', v.get('title'))
    print('missing:', 'missing' in v)
    ii = (v.get('imageinfo') or [None])[0]
    if not ii:
        print('  无 imageinfo')
        print('  原始返回:', str(j)[:400])
        continue
    print('  url     :', ii.get('url'))
    print('  thumburl:', ii.get('thumburl'))
    for label, u in [('thumburl', ii.get('thumburl')), ('url', ii.get('url'))]:
        if not u:
            continue
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'DockyardArchive/1.0'})
            t0 = time.time()
            with opener.open(req, timeout=120) as f:
                data = f.read()
            print(f'  {label}: OK {len(data)} bytes, {time.time()-t0:.1f}s, head={data[:4]}')
        except Exception as e:
            print(f'  {label}: FAIL {type(e).__name__} {str(e)[:90]}')
