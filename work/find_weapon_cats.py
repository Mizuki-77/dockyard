# 查 10 型新武器的 Commons 分类。
#
# 武器图的分类规律与舰不同：多数是「型号名」或「口径 + 型号」。
# 先批量试点，能拿到就抓，拿不到就记「无图」——
# 用户本轮说了「尽力而为，不强求多图」，武器图尤其如此。
import json
import time
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

CANDIDATES = {
    '8in-50-mk8': ['BL 8 inch Mk VIII naval gun', '8 inch 50 calibre Mk VIII',
                   'BL 8-inch naval gun'],
    '6in-50-mk23': ['BL 6 inch Mk XXIII naval gun', 'QF 6 inch Mk XXIII',
                    'BL 6-inch gun Mk XXIII'],
    '45in-45-mk1': ['QF 4.5 inch Mk I naval gun', 'QF 4.5-inch Mk I',
                    '4.5 inch naval gun'],
    '47in-45-mk12': ['QF 4.7 inch Mk XII', 'QF 4.7-inch gun',
                     '4.7 inch QF Mark XII'],
    '4in-45-mk16': ['QF 4 inch Mk XVI naval gun', 'QF 4-inch Mk XVI',
                    '4 inch 45 calibre gun'],
    'vickers-50': ['Vickers .50 machine gun', 'Vickers 0.5 inch',
                   'Vickers .50 calibre'],
    '3pdr-hotchkiss': ['QF 3 pounder Hotchkiss', '3 pounder Hotchkiss',
                       'Hotchkiss 3-pdr'],
    'skua': ['Blackburn Skua', 'Blackburn B-24 Skua'],
    'roc': ['Blackburn Roc', 'Blackburn B-25 Roc'],
    'albacore': ['Fairey Albacore', 'Fairey TBR Albacore'],
}


def api(params, retries=5):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 + a * 15)
                continue
            return {'_err': str(e)}
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(8)
    return {}


def count(cat):
    d = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:' + cat, 'cmtype': 'file', 'cmlimit': '500'})
    if '_err' in d:
        return None
    return len(d.get('query', {}).get('categorymembers', []))


out = {}
for wid, cands in CANDIDATES.items():
    print(f'=== {wid} ===')
    best = None
    for c in cands:
        n = count(c)
        print(f'   {n if n is not None else "?":>4}  {c}')
        if n and (best is None or n > best[1]):
            best = (c, n)
        time.sleep(1.2)
    out[wid] = best[0] if best else None
    print()

print('=== 结论 ===')
for wid, cat in out.items():
    print(f'  {wid:<16} {cat or "（无可用分类）"}')

json.dump(out, open('work/weapcat_results.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('\n已写 work/weapcat_results.json')
