import sys, os, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import api

TITLES = [
 "File:Fairey Flycatcher.jpg",
 "File:HMS Furious-19.jpg",
 "File:Fairey Flycatcher 1923.jpg",
]
for t in TITLES:
    d = api({"action": "parse", "page": t, "prop": "wikitext", "format": "json"})
    wt = d.get("parse", {}).get("wikitext", "") or ""
    lic = re.findall(r"\{\{\s*(PD[^}|\n]*|Cc-[^}|\n]*|No restrictions[^}|\n]*)", wt, re.I)
    print("### " + t)
    print("  templates:", lic)
    for line in wt.split("\n"):
        if re.search(r"source|author|permission|licen", line, re.I):
            print("   |", line.strip()[:180])
    print()
