import sys, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

T = ["File:The Royal Navy during the Second World War A25430.jpg",
     "File:Dramatic End of the Tirpitz C4775.jpg",
     "File:Tromsö, Royal Air Force Bomber Command, 1942-1945 CL2830.jpg"]

def clean(s):
    if not s: return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", s).strip()

for r in meta.show(T):
    print("====", r["title"])
    print("  lic:", clean(r.get("LicenseShortName")), "| size:", r.get("w"), "x", r.get("h"))
    print("  artist:", clean(r.get("Artist"))[:120])
    print("  credit:", clean(r.get("Credit"))[:250])
    print("  date:", clean(r.get("DateTimeOriginal"))[:60])
    print("  desc:", clean(r.get("ImageDescription"))[:400])
