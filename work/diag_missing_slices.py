# 查图池充足但切片仍无图的舰：是 date 缺失还是筛选过严。
import io
import yaml

SHIPS = ['prinz-eugen', 'kaga', 'akagi', 'illustrious']

d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))

LOCAL_PARTS = {'turret', 'superstructure', 'bridge', 'propeller', 'catapult',
               'aircraft_handling', 'weapon', 'radar'}

for sid in SHIPS:
    imgs = [x for x in d['images'] if str(x.get('subject')) == f'ship:{sid}']
    whole = [x for x in imgs
             if str(x.get('part')) not in LOCAL_PARTS and str(x.get('view')) != 'detail']
    with_date = [x for x in whole if x.get('date')]

    print(f'=== {sid} ===')
    print(f'  总数 {len(imgs)}，整舰构图 {len(whole)}，其中有日期 {len(with_date)}')
    for x in whole:
        dt = x.get('date')
        mark = '' if dt else '  ← 无日期，切片不会用它'
        print(f'    {str(dt) or "(无)":<12} {x["id"][:46]}{mark}')

    # 切片
    sp = f'data/slices/{sid}.yaml'
    try:
        sd = yaml.safe_load(io.open(sp, encoding='utf-8')) or {}
        print('  切片:')
        for sl in sd.get('slices') or []:
            print(f'    {sl.get("code")}  {sl.get("from")} ~ {sl.get("to")}')
    except Exception as e:
        print('  切片读取失败', e)
    print()
