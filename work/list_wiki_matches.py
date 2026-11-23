import io
import json

d = json.load(io.open('work/cmdr_wiki.json', encoding='utf-8'))
for k, v in sorted(d.items()):
    art = v.get('article') or '-'
    img = 'IMG' if v.get('image') else '   '
    print(f'{img} {k:<42} -> {art}')
