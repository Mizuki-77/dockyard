import sys, os, urllib.request, urllib.error, time

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_raw')
os.makedirs(RAW, exist_ok=True)

HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

def fetch(url, name, timeout=60):
    path = os.path.join(RAW, name)
    try:
        req = urllib.request.Request(url, headers=HDRS)
        data = urllib.request.urlopen(req, timeout=timeout).read()
        with open(path, 'wb') as f:
            f.write(data)
        print(f'OK   {len(data):>8}  {url}  -> {name}')
        return True
    except Exception as e:
        print(f'FAIL {url}  :: {type(e).__name__}: {e}')
        return False

if __name__ == '__main__':
    pairs = []
    for a in sys.argv[1:]:
        url, _, name = a.partition('|')
        pairs.append((url, name or (url.rstrip('/').split('/')[-1] or 'index.html')))
    for url, name in pairs:
        fetch(url, name)
        time.sleep(1)
