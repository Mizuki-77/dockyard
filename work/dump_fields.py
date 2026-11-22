import yaml

reg = yaml.safe_load(open('data/fields.yaml', encoding='utf-8'))
fields = reg['fields']
print('total fields', len(fields))

by_ns = {}
for f in fields:
    ns = f['id'].split('.')[0]
    by_ns.setdefault(ns, []).append(f)

order = ['identity', 'displacement', 'dimensions', 'propulsion', 'protection',
         'armament', 'sensors', 'aviation', 'construction', 'service',
         'appearance', 'media', 'modelling']
for ns in order:
    items = by_ns.get(ns, [])
    print(f"\n## {ns} ({len(items)})")
    for f in items:
        u = f.get('unit') or '-'
        extra = ''
        if f.get('qual_keys'):
            extra += f" qual={f['qual_keys']}"
        if f.get('type') == 'enum':
            extra += f" enum"
        if f.get('multi'):
            extra += " multi"
        print(f"  {f['id']:<52} {f['type']:<8} {u:<6}{extra}")
