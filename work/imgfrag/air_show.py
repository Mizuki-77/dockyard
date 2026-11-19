import sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = json.load(open(sys.argv[1], encoding="utf-8-sig"))
print("count", len(d))
for r in d:
    if r.get("err"):
        print("[ERR]", r["title"]); continue
    print("%s | %sx%s | %s | %s" % (r["title"], r["w"], r["h"], r["lic"],
                                    (r.get("desc") or "")[:200].replace("\n", " ")))
    print("    art=%s date=%s" % ((r.get("artist") or "")[:90].replace("\n", " "), (r.get("date") or "")[:40]))
