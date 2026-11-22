import io
import re

print('修复后各舰时间轴范围：')
for s in ['hiryu', 'illustrious', 'kaga', 'akagi', 'enterprise', 'bismarck']:
    h = io.open(f'dist/ships/{s}/index.html', encoding='utf-8').read()
    m = re.search(r'"range":\{"from":"([^"]+)","to":"([^"]+)"', h)
    if m:
        print(f'  {s:<14} {m.group(1)} ~ {m.group(2)}')

print()
print('切片起止：')
import yaml
for s in ['hiryu', 'illustrious']:
    d = yaml.safe_load(io.open(f'data/slices/{s}.yaml', encoding='utf-8')) or {}
    sl = d.get('slices') or []
    if sl:
        print(f'  {s:<14} {sl[0].get("from")} ~ {sl[-1].get("to")}')
