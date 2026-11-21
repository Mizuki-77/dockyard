import io
import json
import re

d = json.load(io.open('work/weaponimg2/candidates.json', encoding='utf-8'))


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


for wid, entries in d.items():
    print('=' * 72)
    print(wid)
    for i, e in enumerate(entries):
        lic = clean(e.get('license'))
        tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B'
        t = clean(e.get('title')).replace('File:', '')
        print(f'[{i:>2}] {tier} {e.get("w")}x{e.get("h")} {lic[:18]}')
        print(f'     {t[:92]}')
        dd = clean(e.get('desc'))
        if dd:
            print(f'     {dd[:92]}')
    print()
