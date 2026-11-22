import io

import yaml

for sid in ['enterprise', 'illustrious']:
    d = yaml.safe_load(io.open(f'data/slices/{sid}.yaml', encoding='utf-8')) or {}
    print(f'=== {sid} ===')
    for s in d.get('slices') or []:
        print(f"  {s.get('code'):<5} {s.get('from')} ~ {s.get('to') or '?':<12} {s.get('title')}")
    print()
