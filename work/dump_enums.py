import yaml

reg = yaml.safe_load(open('data/fields.yaml', encoding='utf-8'))
fields = reg['fields']
want = ['identity.ship_type', 'identity.nation', 'identity.era',
        'construction.fate_type', 'protection.scheme', 'propulsion.plant_type',
        'sensors.fire_control.rpc', 'appearance.island_position',
        'media.image.view', 'media.image.part', 'media.image.license',
        'media.image.license_tier', 'modelling.kit.status', 'modelling.kit.material',
        'weapon.category', 'weapon.nation', 'weapon.role', 'weapon.era']
for f in fields:
    if f['id'] in want:
        print(f"{f['id']}: {f.get('values')}")

print('\n=== qual_values for armor ===')
for f in fields:
    if f.get('qual_values'):
        print(f['id'], '->', f['qual_values'])

print('\n=== all weapon.* fields ===')
for f in fields:
    if f['id'].startswith('weapon.') or f['id'].startswith('mount.'):
        print(f"  {f['id']:<40} {f['type']:<8} {f.get('unit') or '-'}")
