# -*- coding: utf-8 -*-
import sys, ssl, urllib.request, json, time, re, urllib.parse

UA = "DockyardArchive/1.0 (research)"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def cdx(pattern, limit=400):
    u = ("https://web.archive.org/cdx/search/cdx?url=%s&output=json&collapse=urlkey"
         "&fl=original,timestamp,statuscode&limit=%d" % (urllib.parse.quote(pattern, safe=""), limit))
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


for pat in sys.argv[1:]:
    try:
        rows = cdx(pat)
    except Exception as e:
        print("FAIL", pat, e)
        continue
    print("==== %s (%d)" % (pat, len(rows)))
    for row in rows[1:]:
        if re.search(r"\.(html|htm|php)$", row[0], re.I):
            print("  %-95s %s %s" % (row[0], row[1], row[2]))
    time.sleep(2)
