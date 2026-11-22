import yaml

ships = ['victorious', 'sheffield', 'norfolk', 'dorsetshire', 'ark-royal',
         'cossack', 'maori', 'zulu', 'sikh', 'piorun']
print(f"{'id':<15} {'中文名':<14} English")
print('-' * 60)
for sid in ships:
    d = yaml.safe_load(open(f'data/ships/{sid}.yaml', encoding='utf-8'))
    zh = d['name']['zh']
    en = d['name']['en']
    print(f"{sid:<15} {zh:<14} {en}")

print()
print('=== 新建舰级 ===')
for cid in ['town', 'county', 'tribal', 'ark-royal', 'n-class']:
    d = yaml.safe_load(open(f'data/classes/{cid}.yaml', encoding='utf-8'))
    print(f"{cid:<12} {d['name']['zh']:<22} {d['name']['en']}")
