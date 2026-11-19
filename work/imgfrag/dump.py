import sys, os, io, json, re, html
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

titles = [l.strip() for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cand.txt"), encoding="utf-8") if l.strip()]
extra = [
    "File:Dramatic End of the Tirpitz C4775.jpg",
    "File:Battlehip Tirpitz capsized at Tromso c1944.jpg",
    "File:NH 71402 (22502381875).jpg",
    "File:Royal Air Force Bomber Command, 1942-1945. CH17864.jpg",
    "File:Royal Air Force 1939-1945- Bomber Command CH17863.jpg",
    "File:Royal Air Force Bomber Command, 1942-1945. CH14145.jpg",
    "File:Tirpitz-1.jpg",
    "File:Battleship Tirpitz off Kiel Sept 1941.jpg",
    "File:Tirpitz trials 1941 h59668.jpg",
    "File:Tirpitz Norway h71318.jpg",
    "File:German Battleship Tirpitz.jpg",
    "File:Tirpitz (AWM SUK14095).jpg",
    "File:Tirpitz at Tromso fjord in November 1944.JPG",
    "File:Tirpitz leaving a Norwegian fjord, circa 1942. (51055380606).jpg",
    "File:Battleship Tirptiz in Kaafjord during May 1943.JPG",
    "File:Tirpitz Anchored in the Alta Fjord, in northern Norway, protected by anti-torpedo nets (1943-1944). (51055432497).jpg",
    "File:Tirpitz (1941-1944) Camouflaged at her moorings at Alta fjord , Norway, during World War II (50050816347).jpg",
    "File:German battleship Tirpitz partly covered by a smokescreen at Kaafjord A22634.jpg",
    "File:German battleship Tirpitz evading torpedoes during Operation Sportpalast.jpg",
    "File:Fleet Air Arm attack the battleship Tirpitz.jpg",
    "File:Cañones del acorazado Tirpitz.jpg",
    "File:Tirpitz Crewmen on board the battleship, while she was moored in a Norwegian fjord, circa 1942-44. One of the ship's 380mm (15) gun turrets is trained abeam, and several camouflage floats are in the distance. (51055366666).jpg",
]
allt = titles + [e for e in extra if e not in titles]
res = meta.show(allt)
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cand-meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def clean(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"QS:P571,.*", "", s)
    return re.sub(r"\s+", " ", s).strip()


for i, r in enumerate(res):
    t = r["title"].replace("File:", "")
    print("[%d] %s" % (i, t))
    print("    %sx%s | %s | %s" % (r.get("w"), r.get("h"), clean(r.get("LicenseShortName")), clean(r.get("Artist"))[:60]))
    print("    date=%s | %s" % (clean(r.get("DateTimeOriginal"))[:45], clean(r.get("Credit"))[:60]))
    print("    desc=%s" % clean(r.get("ImageDescription"))[:200])
