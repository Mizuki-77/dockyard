import io
import json
import re

d = json.load(io.open('work/weaponimg/candidates.json', encoding='utf-8'))


def clean(h):
    s = re.sub(r'<[^>]+>', '', str(h or ''))
    s = s.replace('&amp;', '&').replace('&quot;', '"')
    return ' '.join(s.split())


for wid in ['a6m2', '25mm-96', '11in75-mk1', '12cm-10ns']:
    print('=' * 72)
    print(wid)
    for i, e in enumerate(d[wid]['entries'][:16]):
        lic = clean(e.get('license'))
        tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B'
        t = clean(e.get('title')).replace('File:', '')
        print(f'[{i:>2}] {tier}  {e.get("w")}x{e.get("h")}  {lic[:20]}')
        print('     ' + t[:95])
        dd = clean(e.get('desc'))
        if dd:
            print('     ' + dd[:105])
    print()
