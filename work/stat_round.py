import io

import yaml

ships = ['victorious', 'sheffield', 'norfolk', 'dorsetshire', 'ark-royal',
         'cossack', 'maori', 'zulu', 'sikh', 'piorun']
print('ship              slices  intro  hist(sections/events)')
print('-' * 60)
ts = ti = th = te = 0
for s in ships:
    d = yaml.safe_load(io.open(f'data/slices/{s}.yaml', encoding='utf-8'))
    a = yaml.safe_load(io.open(f'data/articles/{s}.yaml', encoding='utf-8'))
    ns = len(d['slices'])
    ni = len(a['intro']['paragraphs'])
    nh = len(a['history'])
    ev = sum(len(h.get('events') or []) for h in a['history'])
    ts += ns
    ti += ni
    th += nh
    te += ev
    print(f'{s:<16} {ns:>4}  {ni:>5}  {nh:>2} / {ev}')
print('-' * 60)
print(f'{"合计":<16} {ts:>4}  {ti:>5}  {th:>2} / {te}')
