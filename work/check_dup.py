import collections
import re

ts = open('src/lib/catalog.ts', encoding='utf-8').read()
block = ts.split('const ROLE_BY_WEAPON')[1].split('};')[0]
keys = re.findall(r"'([^']+)':", block)
dup = [k for k, c in collections.Counter(keys).items() if c > 1]
print('duplicate keys:', dup if dup else 'none')
print('total registered:', len(keys))
