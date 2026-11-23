# -*- coding: utf-8 -*-
import ssl, urllib.request, urllib.error

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URLS = [
 "http://www.ussastoria.org/",
 "https://www.ussastoria.org/",
 "http://www.ww2db.com/ship_spec.php?ship_id=A418",
 "https://ww2db.com/ship_spec.php?ship_id=A406",
 "http://www.microworks.net/pacific/",
 "https://www.ibiblio.org/hyperwar/USN/rep/index.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/Savo-I/index.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/Savo-1.html",
 "https://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca34.html",
 "https://www.ibiblio.org/hyperwar/USN/ref/ONI/index.html",
 "https://www.history.navy.mil/",
 "http://www.navsource.org/",
 "https://www.navypedia.org/ships/usa/us_cr_new_orleans.htm",
 "https://www.navypedia.org/ships/usa/us_cr_northampton.htm",
 "https://www.navweaps.com/index_oob/OOB_WWII_Pacific/OOB_WWII_Guadalcanal.htm",
 "https://www.navweaps.com/index_oob/index_oob.htm",
]
for u in URLS:
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            print("%s  %-70s %d bytes" % (r.status, u, len(r.read())))
    except urllib.error.HTTPError as e:
        print("HTTP %s  %s" % (e.code, u))
    except Exception as e:
        print("FAIL    %-70s (%s)" % (u, type(e).__name__))
