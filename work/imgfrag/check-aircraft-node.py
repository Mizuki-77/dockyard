"""用站点自身的解析器（node + yaml，见 src/lib/data.ts:55）再验一次分片。"""
import sys, os, json, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:\deepseek harness\website-warships"
FRAG = os.path.join(ROOT, "work", "imgfrag", "img-aircraft.yaml")

JS = r"""
const fs = require('fs');
const YAML = require('yaml');
const p = process.argv[1];
const d = YAML.parse(fs.readFileSync(p, 'utf8'), { uniqueKeys: false });
const need = ['id','file','subject','title','part','view','date','license',
              'license_tier','license_raw','author','credit','source_url',
              'width','height','primary','note'];
const probs = [];
for (const it of d.images) {
  for (const k of need) if (!(k in it)) probs.push(it.id + ' missing ' + k);
  const extra = Object.keys(it).filter(k => !need.includes(k));
  if (extra.length) probs.push(it.id + ' extra ' + extra.join(','));
  if (!it.title || !it.title.zh || !it.title.en) probs.push(it.id + ' title incomplete');
  if (typeof it.primary !== 'boolean') probs.push(it.id + ' primary not bool');
}
console.log(JSON.stringify({
  keys: Object.keys(d),
  n: d.images.length,
  probs,
  subjects: [...new Set(d.images.map(i => i.subject))].sort(),
}, null, 1));
"""

data = json.dumps(JS)
cmd = ["node", "-e", JS, FRAG]
r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("exit:", r.returncode)
print(r.stdout)
if r.stderr:
    print("stderr:", r.stderr[:2000])
