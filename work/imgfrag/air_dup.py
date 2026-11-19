import sys, os, glob, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:\deepseek harness\website-warships"

def urls(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    return re.findall(r"source_url:\s*\"?([^\s\"']+)", txt)

main = urls(os.path.join(ROOT, "data", "images.yaml"))
frag = []
for p in glob.glob(os.path.join(ROOT, "work", "imgfrag", "*.yaml")):
    frag.extend(urls(p))
print("main count", len(main), "frag count", len(frag))
allurls = set(main) | set(frag)

CAND = [
 "Swordfish_on_HMS_Victorious_before_strike_on_Bismarck",
 "The_Royal_Navy_during_the_Second_World_War_A18270",
 "The_Royal_Navy_during_the_Second_World_War_A7977",
 "The_Royal_Navy_during_the_Second_World_War_A7279",
 "The_Royal_Navy_during_the_Second_World_War_A6974",
 "ZZZ_003915_E_Gladiator",
 "A_Chance-Vought_Corsair_landing_aboard_HMS_ILLUSTRIOUS",
 "The_Royal_Navy_during_the_Second_World_War_A23036",
 "Avenger_being_armed_on_HMS_Illustrious",
 "The_Royal_Navy_during_the_Second_World_War_A25377",
 "The_Royal_Navy_during_the_Second_World_War_A100",
 "The_Royal_Navy_during_the_Second_World_War_A9272",
 "The_Royal_Navy_during_the_Second_World_War_A6654",
 "The_Royal_Navy_during_the_Second_World_War_A22229",
 "Arado_Ar_196_aboard_the_German_battleship_Gneisenau",
 "German_Arado_Ar_196A-3_on_the_catapult",
 "Fairey_Flycatcher_1923",
 "Fairey_Flycatcher.jpg",
 "HMS_Furious-19",
 "Corsairs_in_hanger_on_Illustrious",
]
for c in CAND:
    hit = [u for u in allurls if c in u]
    print(("CLASH " if hit else "free   ") + c, hit if hit else "")
