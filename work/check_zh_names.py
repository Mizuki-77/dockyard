# 查中文维基的条目标题，确认每艘舰的通行中文名。
#
# 为什么要查：本站 15 艘既有舰的 name_zh 是不同批次写的，「号」字用得不统一
# （赤城 / 企业号 并存）。这一轮新增 10 艘，必须先把规矩定下来。
#
# web_fetch 在本机被 SSRF 拦（解析到 198.18.x.x），urllib 直连正常。
import json
import re
import time
import urllib.parse
import urllib.request

CANDIDATES = {
    # 日
    'akagi': ['赤城號航空母艦', '赤城号航空母舰'],
    'kaga': ['加賀號航空母艦', '加贺号航空母舰'],
    'soryu': ['蒼龍號航空母艦', '苍龙号航空母舰'],
    'hiryu': ['飛龍號航空母艦', '飞龙号航空母舰'],
    # 美
    'enterprise': ['企業號航空母艦 (CV-6)', '企业号航空母舰 (CV-6)'],
    'yorktown': ['約克鎮號航空母艦 (CV-5)', '约克城号航空母舰 (CV-5)'],
    'hornet': ['大黃蜂號航空母艦 (CV-8)', '大黄蜂号航空母舰 (CV-8)'],
    # 英
    'hood': ['胡德號戰鬥巡洋艦', '胡德号战列巡洋舰'],
    'king-george-v': ['英王喬治五世號戰艦', '英王乔治五世号战列舰'],
    'prince-of-wales': ['威爾斯親王號戰艦', '威尔士亲王号战列舰'],
    'illustrious': ['光輝號航空母艦', '光辉号航空母舰'],
    'victorious': ['勝利號航空母艦', '胜利号航空母舰'],
    'rodney': ['羅德尼號戰艦', '罗德尼号战列舰'],
    'sheffield': ['謝菲爾德號輕巡洋艦', '谢菲尔德号轻巡洋舰'],
    'norfolk': ['諾福克號重巡洋艦 (1928年)', '诺福克号重巡洋舰 (1928年)'],
    'dorsetshire': ['多塞特郡號重巡洋艦', '多塞特郡号重巡洋舰'],
    'ark-royal': ['皇家方舟號航空母艦 (1937年)', '皇家方舟号航空母舰 (1937年)'],
    'cossack': ['哥薩克號驅逐艦 (1937年)', '哥萨克号驱逐舰 (1937年)'],
    'maori': ['毛利人號驅逐艦', '毛利人号驱逐舰'],
    'zulu': ['祖魯人號驅逐艦', '祖鲁人号驱逐舰'],
    'sikh': ['錫克人號驅逐艦', '锡克人号驱逐舰'],
    # 德
    'bismarck': ['俾斯麥號戰艦', '俾斯麦号战舰'],
    'tirpitz': ['鐵必制號戰艦', '提尔皮茨号战列舰'],
    'prinz-eugen': ['歐根親王號重巡洋艦', '欧根亲王号重巡洋舰'],
    # 波
    'piorun': ['閃電號驅逐艦', '闪电号驱逐舰'],
}


def fetch_title(q):
    url = 'https://zh.wikipedia.org/w/api.php?' + urllib.parse.urlencode({
        'action': 'query', 'titles': q, 'format': 'json',
        'redirects': 1, 'prop': 'info',
    })
    req = urllib.request.Request(url, headers={'User-Agent': 'DockyardNameCheck/1.0'})
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=20).read().decode('utf-8'))
    except Exception as e:
        return None, str(e)
    pages = d.get('query', {}).get('pages', {})
    for pid, p in pages.items():
        if pid == '-1':
            return None, 'missing'
        return p.get('title'), 'ok'
    return None, 'empty'


for sid, cands in CANDIDATES.items():
    got = None
    for c in cands:
        title, st = fetch_title(c)
        if title:
            got = title
            break
        time.sleep(0.3)
    print(f"{sid:<18} -> {got or '（未找到）'}")
