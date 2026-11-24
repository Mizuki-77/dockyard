import os
import re

OUT = 'public/img/ships'
for sid in ['tone', 'haruna', 'nagara', 'monaghan', 'new-orleans', 'hosho', 'atlanta']:
    fs = sorted(f for f in os.listdir(OUT) if re.match(rf'^{re.escape(sid)}-\d+-', f))
    print(f'\n{sid} ({len(fs)}):')
    for f in fs:
        short = f.split('-', 2)[2] if f.count('-') >= 2 else f
        print('   ', short[:62])
