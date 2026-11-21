import io

import yaml

d = yaml.safe_load(io.open('data/sources.yaml', encoding='utf-8'))
for s in d['sources']:
    if 'kbismarck' in s['id']:
        print(f"  {s['id']:<34} {s['url']}")
