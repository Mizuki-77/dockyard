# -*- coding: utf-8 -*-
"""Probe a list of URLs, report status only."""
import ssl, urllib.request, urllib.error, sys

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URLS = [
 "https://www.ibiblio.org/hyperwar/USN/rep/",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/index.html",
 "https://www.ibiblio.org/hyperwar/USN/rep/Savo/",
 "https://www.ibiblio.org/hyperwar/USN/ref/Midway/",
 "https://www.ibiblio.org/hyperwar/USN/ref/",
 "https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-2.html",
 "https://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/",
 "https://www.ibiblio.org/hyperwar/USN/BB/",
 "https://www.ibiblio.org/hyperwar/USN/rep/Guadalcanal/",
 "https://www.ibiblio.org/hyperwar/USN/rep/Solomons/index.html",
]

for u in URLS:
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            print("%s  %s  %d bytes" % (r.status, u, len(r.read())))
    except urllib.error.HTTPError as e:
        print("HTTP %s  %s" % (e.code, u))
    except Exception as e:
        print("FAIL    %s  (%s)" % (u, e))
