import yaml

for sid in ['ark-royal', 'victorious', 'dorsetshire']:
    d = yaml.safe_load(open(f'data/slices/{sid}.yaml', encoding='utf-8'))
    s = d['slices']
    print(f"== {sid}: {len(s)} slices, {s[0]['from']} -> {s[-1].get('to')}")
    for x in s:
        print(f"    {x['code']:<3} {x['from']} -> {x.get('to')}")
        print(f"        {x['title'][:60]}")
