# -*- coding: utf-8 -*-
import sys, ssl, urllib.request, json, time

UA = "DockyardArchive/1.0 (research)"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

QUERIES = [
 "http://ussastoria.org/*",
 "http://www.navsource.org/archives/04/034/*",
]

for q in QUERIES:
    u = ("https://web.archive.org/cdx/search/cdx?url=%s&output=json&collapse=urlkey"
         "&fl=original,timestamp,statuscode&limit=200" % urllib.parse.quote(q, safe=""))
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
            data = json.loads(r.read().decode("utf-8", "replace"))
        print("==== %s  (%d rows)" % (q, len(data)))
        for row in data[:80]:
            print("  ", row)
    except Exception as e:
        print("FAIL", q, type(e).__name__, e)
    time.sleep(2)
