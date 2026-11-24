# 带代理的 Commons 客户端
#
# 2026-11-24 晚实测：直连 commons.wikimedia.org 已超时（TLS 握手失败），
# 必须走本机代理 http://127.0.0.1:12450。
# 上一轮（11-23）直连还能通，环境变了。
import json
import ssl
import time
import urllib.parse
import urllib.request

PROXY = 'http://127.0.0.1:12450'
HDR = {'User-Agent': 'DockyardArchive/1.0 (research; low-rate)'}
API = 'https://commons.wikimedia.org/w/api.php'

# 用 ProxyHandler 走代理；证书校验保持宽松（代理 MITM）
_ctx = ssl.create_default_context()
_ctx.check_hostname = False
_ctx.verify_mode = ssl.CERT_NONE

_opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}),
    urllib.request.HTTPSHandler(context=_ctx),
)


def api(params, tries=6, wait_base=4):
    url = API + '?' + urllib.parse.urlencode(params)
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HDR)
            with _opener.open(req, timeout=60) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503):
                time.sleep(wait_base * (i + 1))
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(wait_base * (i + 1))
    if last:
        raise last
    return {}


def cat_files(cat, limit=500):
    j = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:' + cat if not cat.startswith('Category:') else cat,
             'cmtype': 'file', 'cmlimit': str(limit), 'format': 'json'})
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


def cat_exists(cat):
    full = cat if cat.startswith('Category:') else 'Category:' + cat
    j = api({'action': 'query', 'titles': full, 'format': 'json'})
    pages = j.get('query', {}).get('pages') or {}
    return not any('missing' in p for p in pages.values())


def search_cats(term, limit=8):
    j = api({'action': 'query', 'list': 'search', 'srsearch': term,
             'srnamespace': '14', 'srlimit': str(limit), 'format': 'json'})
    return [x['title'] for x in (j.get('query', {}).get('search') or [])]


if __name__ == '__main__':
    print('=== 通路测试 ===')
    j = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:Yokosuka B4Y', 'cmtype': 'file',
             'cmlimit': '5', 'format': 'json'})
    print('  Yokosuka B4Y:', len(j.get('query', {}).get('categorymembers') or []), '个文件')

    print('\n=== 搜日本舰分类 ===')
    for term in ['Tone class cruiser', 'Haruna battleship', 'Hosho aircraft carrier']:
        print(f'  [{term}]')
        for c in search_cats(term)[:5]:
            print('      ', c)
        time.sleep(2)
