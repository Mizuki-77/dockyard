import io
import json

d = json.load(io.open('work/shipimg/picked.json', encoding='utf-8'))
for sid, es in d.items():
    for e in es:
        if 'fix' in e['name']:
            print(f'  {sid:<18} {e["name"][:54]}')
            print(f'     {e["title"][:82]}')
