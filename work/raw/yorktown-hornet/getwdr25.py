import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pypdf, urllib.request, ssl
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
url = "https://www.ibiblio.org/hyperwar/USN/rep/WDR/U.S.S.%20YORKTOWN%20(CV-5),%20BOMB%20AND%20TORPEDO%20DAMAGE%20-%20Midway,%20June%204%20to%207,%201942%20(LOST%20IN%20ACTION).pdf"
p = os.path.join(OUT, "wdr25-yorktown-midway.pdf")
if not (os.path.exists(p) and os.path.getsize(p) > 1000):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=180, context=ctx) as r:
            b = r.read()
        open(p, "wb").write(b)
        print("OK", len(b))
    except Exception as e:
        print("FAIL", type(e).__name__, e)
        raise SystemExit
try:
    r = pypdf.PdfReader(p)
    txt = []
    for i, pg in enumerate(r.pages):
        try: txt.append("\n=== page %d ===\n" % (i+1) + (pg.extract_text() or ""))
        except Exception: txt.append("")
    s = "".join(txt)
    open(os.path.splitext(p)[0] + ".txt", "w", encoding="utf-8").write(s)
    print("TXT", len(r.pages), "pages", len(s), "chars")
except Exception as e:
    print("PDFFAIL", type(e).__name__, e)
