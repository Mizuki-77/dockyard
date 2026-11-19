# -*- coding: utf-8 -*-
"""绕开 PowerShell 编码：直接子进程调 validate，抓 infos/errors。"""
import io
import json
import os
import subprocess
import sys

ROOT = r"D:\deepseek harness\website-warships"
p = subprocess.run(
    [sys.executable, os.path.join(ROOT, "scripts", "validate.py"), "--json"],
    capture_output=True, text=True, encoding="utf-8",
    cwd=ROOT, env={**os.environ, "PYTHONIOENCODING": "utf-8"},
)
d = json.loads(p.stdout)
out = io.open(os.path.join(ROOT, "work", "_infos4.txt"), "w", encoding="utf-8")
out.write("errors=%d warnings=%d infos=%d\n" % (len(d["errors"]), len(d["warnings"]), len(d["infos"])))
for i in d["infos"]:
    if "对比器" in i:
        out.write("CMP> %s\n" % i)
for e in d["errors"][:5]:
    out.write("ERR> %s\n" % e)
out.close()
print("rc", p.returncode)
