import io

import yaml

d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
for s in ['ship:rodney', 'ship:prince-of-wales', 'ship:prinz-eugen']:
    print(s)
    for x in d['images']:
        if x.get('subject') == s:
            print(f"  {x['id']:<42} primary={str(x.get('primary')):<6} tier={x.get('license_tier')} date={x.get('date')}")
            print(f"     {x.get('title', {}).get('zh', '')}")
