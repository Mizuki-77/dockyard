import sys, os, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import api

TITLES = [
 "File:FFlycatcher(b).jpg",
 "File:Fairey IIIF S1303.jpg",
 "File:Fairey IIIFs über Aden.jpg",
 "File:A Royal Navy Fairey Flycatcher biplane (N9928), ca. 1920s (8676959278).jpg",
]
for t in TITLES:
    try:
        d = api({"action": "parse", "page": t, "prop": "wikitext", "format": "json"})
        wt = d.get("parse", {}).get("wikitext", "") or ""
    except Exception as e:
        print("### " + t, "ERR", e); continue
    lic = re.findall(r"\{\{\s*(PD[^}|\n]*|Cc-[^}|\n]*|No restrictions[^}|\n]*|SDASM[^}|\n]*|GFDL[^}|\n]*)", wt, re.I)
    print("### " + t)
    print("  templates:", sorted(set(lic)))
    for line in wt.split("\n"):
        if re.search(r"source|author|permission|licen", line, re.I):
            print("   |", line.strip()[:200])
    print()
