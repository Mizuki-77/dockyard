import io
import json

d = json.load(io.open('work/shipimg/candidates_new10.json', encoding='utf-8'))

for sid, es in d.items():
    print(f'\n{"="*78}')
    print(f'=== {sid}  ({len(es)} 张) ===')
    for i, e in enumerate(es):
        lic = (e.get('license') or '?')[:28]
        dt = (e.get('date') or '')[:10]
        wh = f"{e.get('w')}x{e.get('h')}"
        print(f'  [{i:>2}] {lic:<28} {dt:<11} {wh:<11}')
        print(f'       title: {e["title"][:110]}')
        if e.get('desc'):
            print(f'       desc : {e["desc"][:110]}')
