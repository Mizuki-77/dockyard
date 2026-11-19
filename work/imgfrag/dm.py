import sys, os, json
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wapi

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "d.txt")
mode = sys.argv[1]
lines = []
try:
    if mode == "meta":
        titles = json.load(open(sys.argv[2], encoding="utf-8"))
        res = wapi.q(titles, width=1280)
        for t in titles:
            ii = res.get(t) or {}
            if not ii:
                lines.append("### %s\n  NOTFOUND" % t)
                continue
            m = wapi.meta(ii)
            lines.append("### %s" % t)
            lines.append("  size %sx%s  thumb %sx%s" % (m["w"], m["h"], m["thumb_w"], m["thumb_h"]))
            lines.append("  lic=%r usage=%r licurl=%r" % (m["licshort"], m["usage"], m["licurl"]))
            lines.append("  artist=%r" % m["artist"])
            lines.append("  credit=%r" % m["credit"])
            lines.append("  date=%r" % m["datetime"])
            lines.append("  restr=%r attr=%r copyrighted=%r attreq=%r" % (
                m["restrictions"], m["attribution"], m["copyrighted"], m["attributionrequired"]))
            lines.append("  desc=%r" % m["desc"])
            lines.append("  cats=%r" % m["cats"])
            lines.append("  descurl=%s" % m["descurl"])
            lines.append("  thumb=%s" % m["thumburl"])
except Exception as e:
    lines.append("ERROR " + repr(e))
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("ok", len(lines))
