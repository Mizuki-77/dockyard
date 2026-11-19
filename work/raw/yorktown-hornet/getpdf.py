import sys, urllib.request, os, ssl
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf")
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
base = "http://www.ibiblio.org/hyperwar/NHC/CoralSeaAARs/"
names = ["CoralSeaAARs-index.pdf"] + ["CoralSeaAAR-Yorktown-%02d.pdf" % i for i in range(1, 16)] + ["CoralSeaAAR-CinCPac-1stEndorse.pdf"]
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
for n in names:
    p = os.path.join(OUT, n)
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        print("skip", n); continue
    try:
        req = urllib.request.Request(base + n, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
            b = r.read()
        open(p, "wb").write(b)
        print("OK", n, len(b))
    except Exception as e:
        print("FAIL", n, type(e).__name__, e)
