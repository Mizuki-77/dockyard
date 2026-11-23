# -*- coding: utf-8 -*-
import ssl, urllib.request, urllib.error

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "https://www.ibiblio.org/hyperwar/USN/"
URLS = [
 "USN-CN-Midway/",
 "USN-CN-Midway/index.html",
 "USN-CN-Midway/USN-CN-Midway-1.html",
 "USN-CN-Midway/USN-CN-Midway-3.html",
 "ships/ships-ca.html",
 "ships/",
 "orders-of-battle/",
 "OOB/",
 "rep/Midway/",
 "rep/Midway/index.html",
]
for p in URLS:
    u = BASE + p
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            print("%s  %-45s %d bytes" % (r.status, p, len(r.read())))
    except urllib.error.HTTPError as e:
        print("HTTP %s  %s" % (e.code, p))
    except Exception as e:
        print("FAIL    %-45s (%s)" % (p, e))

# also navweaps orders of battle
for p in ["https://www.navweaps.com/index_oob/index_oob.htm",
          "https://www.navweaps.com/index_oob/OOB_WWII_Pacific/OOB_WWII_Midway.htm"]:
    req = urllib.request.Request(p, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            print("%s  %-45s %d bytes" % (r.status, p, len(r.read())))
    except urllib.error.HTTPError as e:
        print("HTTP %s  %s" % (e.code, p))
    except Exception as e:
        print("FAIL    %-45s (%s)" % (p, e))
