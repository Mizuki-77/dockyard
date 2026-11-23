import io
import json

d = json.load(io.open('work/cmdr13_data.json', encoding='utf-8'))
for k, v in sorted(d.items()):
    n = len(v.get('full') or '')
    img = 'IMG' if v.get('image') else '   '
    print(f'{img} {k:<24} full={n:>5}  intro={len(v.get("intro") or "")}')
