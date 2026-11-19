import sys, os, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import info

titles = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip() and not l.startswith("#")]
rows = []
for rec in info(titles):
    ii = rec["info"]
    if not ii:
        rows.append({"title": rec["title"], "err": "none"}); continue
    em = ii.get("extmetadata") or {}
    g = lambda k: (em.get(k) or {}).get("value")
    rows.append({
        "title": rec["title"],
        "w": ii.get("width"), "h": ii.get("height"),
        "lic": g("LicenseShortName"), "terms": g("UsageTerms"),
        "artist": g("Artist"), "credit": g("Credit"),
        "date": g("DateTimeOriginal"), "obj": g("ObjectName"),
        "desc": g("ImageDescription"),
        "page": ii.get("descriptionurl"),
        "thumb": ii.get("thumburl"),
    })
print(json.dumps(rows, ensure_ascii=False, indent=1))
