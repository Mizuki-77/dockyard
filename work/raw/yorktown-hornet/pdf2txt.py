import sys, os, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pypdf

d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf")
for p in sorted(glob.glob(os.path.join(d, "*.pdf"))):
    out = os.path.splitext(p)[0] + ".txt"
    if os.path.exists(out):
        print("skip", os.path.basename(out)); continue
    try:
        r = pypdf.PdfReader(p)
        txt = []
        for i, pg in enumerate(r.pages):
            try:
                txt.append("\n=== page %d ===\n" % (i + 1) + (pg.extract_text() or ""))
            except Exception as e:
                txt.append("\n=== page %d EXTRACT_FAIL %s ===\n" % (i + 1, e))
        s = "".join(txt)
        open(out, "w", encoding="utf-8").write(s)
        print("OK", os.path.basename(out), len(r.pages), "pages", len(s), "chars")
    except Exception as e:
        print("FAIL", os.path.basename(p), type(e).__name__, e)
