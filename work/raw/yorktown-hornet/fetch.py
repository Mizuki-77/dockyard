import sys, urllib.request, re, html, os, ssl

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def fetch(tag, url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*",
        "Accept-Language": "en-US,en;q=0.9",
    })
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
            raw = r.read()
            st = r.status
    except Exception as e:
        print("FAIL", tag, url, type(e).__name__, e)
        return False
    hp = os.path.join(OUT, tag + ".html")
    open(hp, "wb").write(raw)
    m = re.search(rb'charset=["\']?([\w\-]+)', raw[:4000], re.I)
    enc = m.group(1).decode() if m else "utf-8"
    try:
        h = raw.decode(enc, errors="replace")
    except LookupError:
        h = raw.decode("utf-8", errors="replace")
    t = re.sub(r"(?is)<(script|style|head|noscript)[^>]*>.*?</\1>", " ", h)
    t = re.sub(r"(?is)<br\s*/?>", "\n", t)
    t = re.sub(r"(?is)</(p|div|tr|h\d|li|table|blockquote|dt|dd)>", "\n", t)
    t = re.sub(r"(?is)</t[dh]>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
    open(os.path.join(OUT, tag + ".txt"), "w", encoding="utf-8").write(t.strip())
    print("OK", tag, st, len(raw), "->", len(t))
    return True

if __name__ == "__main__":
    for line in open(sys.argv[1], encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        tag, url = line.split(None, 1)
        fetch(tag, url.strip())
