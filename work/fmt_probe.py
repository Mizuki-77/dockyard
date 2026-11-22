import json
import yaml


def default(o):
    return str(o)


imgs = yaml.safe_load(open('data/images.yaml', encoding='utf-8'))['images']
srcs = yaml.safe_load(open('data/sources.yaml', encoding='utf-8'))['sources']

print('=== image entry (rodney first) ===')
for i in imgs:
    if i.get('subject') == 'ship:rodney':
        print(json.dumps(i, ensure_ascii=False, indent=1, default=default))
        break

print('=== image entry (weapon) ===')
for i in imgs:
    if str(i.get('subject', '')).startswith('weapon:'):
        print(json.dumps(i, ensure_ascii=False, indent=1, default=default))
        break

print('=== source entry 0 ===')
print(json.dumps(srcs[0], ensure_ascii=False, indent=1, default=default))

print('=== a royal-navy source ===')
for x in srcs:
    if 'naval-history' in str(x.get('id', '')):
        print(json.dumps(x, ensure_ascii=False, indent=1, default=default))
        break
