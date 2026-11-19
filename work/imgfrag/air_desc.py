import sys, os, re, html
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import info

TITLES = [
 "File:The Royal Navy during the Second World War A22229.jpg",
 "File:The Royal Navy during the Second World War A15442.jpg",
 "File:Fairey Flycatcher 1923.jpg",
 "File:The Royal Navy during the Second World War A6974.jpg",
 "File:ZZZ 003915 E Gladiator.jpg",
 "File:HMS Furious-19.jpg",
 "File:Fairey Flycatcher.jpg",
 "File:The Royal Navy during the Second World War A18270.jpg",
]
for t in TITLES:
    for rec in info([t]):
        ii = rec["info"]; em = (ii or {}).get("extmetadata") or {}
        d = (em.get("ImageDescription") or {}).get("value") or ""
        d = html.unescape(re.sub(r"<[^>]+>", " ", d))
        print("### " + t)
        print(re.sub(r"\s+", " ", d).strip())
        print()
