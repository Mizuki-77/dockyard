# -*- coding: utf-8 -*-
import ssl, urllib.request, urllib.error

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URLS = [
 "http://www.history.navy.mil/research/histories/ship-histories/danfs/a/astoria-ca-34-ii.html",
 "https://web.archive.org/web/2020/https://www.ussastoria.org/USS_ASTORIA_CA-34.html",
 "https://web.archive.org/web/2020/http://www.navsource.org/archives/04/034/04034.htm",
 "https://web.archive.org/web/2020/http://www.navsource.org/archives/04/033/04033.htm",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/NWC/NWC-Savo-8.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/NWC/NWC-Savo-20.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/NWC/NWC-Savo-Fwd.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/NWC/NWC-Savo-21.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/NWC/NWC-Savo-22.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/NWC/NWC-Savo-23.html",
]
for u in URLS:
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
            print("%s  %-80s %d bytes" % (r.status, u, len(r.read())))
    except urllib.error.HTTPError as e:
        print("HTTP %s  %s" % (e.code, u))
    except Exception as e:
        print("FAIL    %-80s (%s)" % (u, type(e).__name__))
