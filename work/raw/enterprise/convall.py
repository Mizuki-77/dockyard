import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
d = r"D:\deepseek harness\website-warships\work\raw\enterprise"
conv = r"D:\deepseek harness\website-warships\work\raw\_tmp\html2txt.py"
import subprocess
for f in glob.glob(os.path.join(d, "*.html")):
    out = f[:-5] + ".txt"
    subprocess.run([sys.executable, conv, f, out])
