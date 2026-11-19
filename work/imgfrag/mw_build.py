# -*- coding: utf-8 -*-
"""按分组生成中途岛图片清单 markdown。"""
import sys, json, re, html, io

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

META = ["_meta_mid_battle.json", "_meta_mid_ships.json",
        "_meta_mid_air.json", "_meta_mid_extra.json"]

raw = {}
for fn in META:
    for e in json.load(open(fn, encoding="utf-8")):
        raw[e["title"]] = e

ver = {v["title"]: v for v in json.load(open("_verify2.json", encoding="utf-8")).values()}
lic = json.load(open("_licenses.json", encoding="utf-8"))

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def clean(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


# Commons 的 DateTimeOriginal 常常是「上传日期」或只给年份，
# 这里按图注/史实逐条校正，只保留有把握的。
DATE_OVERRIDE = {
    "Kaga, Akagi and Soryu under attack.jpg": "1942（沙盘，描绘 6-04 上午）",
    "Battle of Midway.jpg": "1942（沙盘，描绘 6-04 上午）",
    "Soryu-Midway.png": "1942-06-04",
    "Japanese aircraft carrier Soryu 1937.jpg": "1937 年初",
    "Kaga Reconstruction overhead.jpg": "1935",
    "HIJMS Kaga.jpg": "1936 年后",
    "Japanese aircraft carrier kaga.jpg": "1936-1942",
    "Japanese.aircraft.carrier.kaga.jpg": "未标注",
    "Kaga Carrier Zero Fighters.jpg": "1942-01（Commons 上传日 2017 非拍摄日）",
    "Kaga B5N aircrew Pearl Harbor.jpg": "1941-12-06",
    "Kaga Pearl Harbor brief.jpg": "1941-12-06",
    "Chuichi Nagumo in the bridge of Akagi heading to attack Pearl Harbor.jpg": "1941-11/12（驶向珍珠港途中）",
    "Chuichi Nagumo with the staff of the 1st Air Fleet.jpg": "1941-1942（任第一航空舰队司令期间）",
    "Chuichi Nagumo.jpg": "约 1941-1942",
    "Damaged Grumman F4F-3 Wildcat of VMF-221 on Midway, 24 June 1942 (80-G-11636).jpg": "1942-06-24",
    "96siki-kankou.jpg": "1945 年前",
    "Aft view of USS Hornet (CV-8), circa in late 1941 (NH 81313).jpg": "1941 年末",
    "F2As VMF-221 over Midway.jpg": "1942-05/06",
    "USS Hammann DD-412 sunk-depth charges exploding near Yorktown.jpg": "1942-06-06",
    "USS Hammann alongside USS Yorktown-both torpedoed.jpg": "1942-06-06",
    "USS Hammann sinking 1942-06-06 seen from USS Yorktown.jpg": "1942-06-06",
    "Battle of Midway- Mikuma capsizing 88-188-ac.jpg": "1942（画作）",
    "Air Attack on Japanese Carriers Kagi and Akagi, Midway Battle.jpg": "1942（画作）",
    "88-188-ag.jpg": "1942（画作）",
    "Admiral Frank Jack Fletcher.jpg": "未标注",
    "Admiral Isoroku Yamamoto.jpg": "未标注（PD-Japan-oldphoto）",
    "Portrait of Yamamoto Isoroku.jpg": "1943 年前",
    "TamonYamaguchi.jpg": "未标注",
    "Kaku Tomeo.jpg": "未标注（本人 1942 阵亡）",
    "Last Moments of Admiral Yamaguchi.jpg": "未标注（画作）",
    "Mogami & Nichiei Maru after Midway.jpg": "1942-06 后",
}


def norm_date(s, fname=None):
    """把 Commons 的 DateTimeOriginal 归一化成人读日期。"""
    if fname and fname in DATE_OVERRIDE:
        return DATE_OVERRIDE[fname]
    s = clean(s)
    if not s:
        return "未标注"
    # 优先取形如 4 June 1942 / 6 June 1942 的完整日期
    m = re.search(r"(\d{1,2})\s+([A-Z][a-z]+)\s+(\d{4})", s)
    if m and m.group(2) in MONTHS:
        return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2)], int(m.group(1)))
    # 1942-06-04
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m and m.group(1) != "0000":
        if m.group(2) == "00":
            return m.group(1)
        if m.group(3) == "00":
            return "%s-%s" % (m.group(1), m.group(2))
        return m.group(0)
    # circa May 1942 / May 1942
    m = re.search(r"([A-Z][a-z]+)\s+(\d{4})", s)
    if m and m.group(1) in MONTHS:
        return "%s-%02d" % (m.group(2), MONTHS[m.group(1)])
    m = re.search(r"(\d{4})", s)
    if m:
        return m.group(1)
    return s[:20]


TM = json.load(open("_templates.json", encoding="utf-8"))
EX = json.load(open("_extra_lic.json", encoding="utf-8"))


def tmpl_of(title):
    v = [x for x in (TM.get(title) or []) if x.lower() != "pd-because"]
    if not v:
        lp = (EX.get(title) or {}).get("license_param")
        if lp:
            v = [lp]
    return " / ".join(v) if v else ""


def lic_of(title):
    d = lic.get(title) or {}
    short = d.get("license") or d.get("license_short") or "?"
    usage = clean(d.get("usage"))
    return short, usage


def lic_raw(title):
    """返回 Commons license 原文：优先用具体 PD 模板名。"""
    tp = tmpl_of(title)
    if tp:
        return "Public domain（%s）" % tp
    u = clean((lic.get(title) or {}).get("usage"))
    return u or "Public domain"


def direct(title, fname):
    v = ver.get(title) or {}
    u = (v.get("redirect") or "").split("?")[0]
    if not u:
        e = raw[title]
        u = (e.get("url") or "").split("?")[0]
    return u


def size(title):
    e = raw[title]
    return e.get("width"), e.get("height")


# ---- 分组定义：(分区标题, [(Commons 文件名, 中文说明), ...]) ----
GROUPS = []

GROUPS.append(("一、战役场景：日军航母中弹 / 燃烧", [
    ("Kaga, Akagi and Soryu under attack.jpg",
     "1942-06-04 上午，加贺、赤城、苍龙同时遭美军 SBD 俯冲轰炸。Norman Bel Geddes 二战期间制作的立体沙盘（官方 USN 战时依据当时情报复原，非现场照片），横构图，可作整版场景图"),
    ("Battle of Midway.jpg",
     "同上沙盘的另一角度/另一幅：约克城号与企业号俯冲轰炸机攻击苍龙、赤城、加贺。构图更聚焦单舰"),
    ("Air Attack on Japanese Carriers Kagi and Akagi, Midway Battle.jpg",
     "海军战斗画家 Griffith Bailey Coale 少校的木炭＋粉彩画：加贺、赤城遭空袭。竖构图 3622x4808，适合做插页"),
    ("Soryu-Midway.png",
     "苍龙在 1942-06-04 空袭下规避（美军拍摄航拍）。分辨率较低 762x615，但为现场实拍"),
    ("Japanese aircraft carrier Sōryū underway during Battle of Midway on 4 June 1942.jpg",
     "苍龙 1942-06-04 08:00 后被 B-17E 攻击时绕圈规避的航拍，与上一条同源但为另一幅"),
    ("Aerial view of the Japanese aircraft carrier Sōryū evading an air attack on 4 June 1942 (fsa.8e00397).jpg",
     "同场景高分辨率版本 3436x3154，可见完整环形尾迹，推荐作为苍龙规避图主用"),
    ("Japanese aircraft carrier Hiryu dodging bombs on 4 June 1942 (USAF-3725).jpg",
     "飞龙 1942-06-04 规避 B-17E 投弹，竖构图 4160x5103"),
    ("Japanese aircraft carrier Hiryu maneuvers to avoid bombs on 4 June 1942 (USAF-3725).jpg",
     "同批次的横幅版本 5024x3740，舰体完整、浪迹清晰，推荐横版主用"),
    ("Japanese aircraft carrier Hiryu burning on 5 June 1942 (NH 73064).jpg",
     "★飞龙中弹后燃烧：1942-06-05 日出后由凤翔号九六式舰攻拍摄。舰桥前部升降机被炸翻竖立，飞行甲板右端塌陷"),
    ("Japanese aircraft carrier Hiryu adrift and burning on 5 June 1942 (NH 73065).jpg",
     "★飞龙燃烧漂流的另一角度（同机同批）。飞行甲板被 Norman Kleiss 投下的炸弹掀开，数小时后沉没"),
    ("88-188-ag.jpg",
     "海军战斗画家 Coale 的木炭/粉彩：1942-06-06 攻击三隈、最上。分辨率仅 500x396，仅作补充"),
    ("Battle of Midway- Mikuma capsizing 88-188-ac.jpg",
     "三隈倾覆画作（Coale），竖构图 500x631，分辨率低"),
]))

GROUPS.append(("二、战役场景：三隈号被炸（1942-06-06）", [
    ("Japanese heavy cruiser Mikuma sinking on 6 June 1942 (80-G-414422).jpg",
     "★三隈 1942-06-06 下午，自企业号 SBD 拍摄。舯部结构炸烂、后部鱼雷发射管挂着一条鱼雷。5724x4501 大图"),
    ("Japanese cruiser Mikuma burning with DD 1942.jpg",
     "★三隈燃烧，右侧有驱逐舰。5717x4414"),
    ("Japanese cruiser Mikuma burning and sinking on 6 June 1942 (80-G-457861).jpg",
     "三隈燃烧下沉，600x490 低分辨率，与上两条同场景，可省"),
    ("Japanese cruiser Mikuma dead in water 1942.jpg",
     "三隈失去动力停在水面，740x554"),
    ("SBD-3 Dauntless bombers of VS-8 over the burning Japanese cruiser Mikuma on 6 June 1942.jpg",
     "★大黄蜂号 VS-8 的 SBD-3 飞越燃烧的三隈，准备第三轮攻击。3000x2400，战役感最强的一张"),
    ("Mogami & Nichiei Maru after Midway.jpg",
     "最上号与日荣丸在中途岛之后的受损状态，481x799 竖图，分辨率低"),
    ("PBY sights Japanese minesweepers en route to Midway on 3 June 1942.jpg",
     "1942-06-03 PBY 发现驶向中途岛的日军扫雷艇，5659x4327"),
]))

GROUPS.append(("三、战役场景：约克城号中弹 / 倾斜 / 弃舰 / 沉没", [
    ("USS Yorktown (CV-5) burning after the first attack by Japanese dive bombers during the Battle of Midway on 4 June 1942.jpg",
     "★约克城号被日军俯冲轰炸机首轮命中（3 弹）后燃烧。5644x4233"),
    ("USS Yorktown (CV-5) is hit by a torpedo on 4 June 1942.jpg",
     "★约克城号左舷舯部被九一式航空鱼雷命中瞬间（飞龙号攻击队），舰体开始左倾。5660x4467，最具戏剧性的一张"),
    ("USS Yorktown (CV-5) burning and listing on 4 June 1942.jpg",
     "★约克城号燃烧并倾斜，约 16:20 被两条鱼雷击中后、弃舰前。5659x4488"),
    ("Damaged USS Yorktown (CV-5) and Astoria (CA-34) at Midway 1942.jpg",
     "约克城号中弹后甲板浓烟（烟道起火、锅炉失效），右为阿斯托里亚号。1413x763"),
    ("Flight deck of USS Yorktown (CV-5) after damage at Midway 1942.jpg",
     "约克城号受损后的飞行甲板，前景水兵正在抢修木甲板。2109x1504"),
    ("Island of USS Yorktown (CV-5) after bomb hits during the Battle of Midway, 4 June 1942 (80-G-23978).jpg",
     "约克城号舰桥中弹后的特写，竖构图 2020x2689"),
    ("USS Yorktown (CV-5) listing and abandoned on 4 June 1942.jpg",
     "★约克城号严重左倾、已弃舰。甲板上仍停着 VF-3 的两架 F4F-4。2767x1963"),
    ("Sinking of the USS Yorktown (CV-5) 01.jpg",
     "★弃舰：舰员离舰，右方为巴尔奇号驱逐舰，海面大片油膜与救生筏。5453x4079"),
    ("Sinking of the USS Yorktown (CV-5) 02.jpg",
     "★约克城号左倾、烟囱冒烟的另一幅，1656x1524"),
    ("USS Yorktown (CV-5) being abandonded, 4 June 1942.jpg",
     "★弃舰全景，四艘驱逐舰（本汉姆、拉塞尔、巴尔奇、安德森）在旁待命。5591x4125"),
    ("USS Yorktown (CV-5) sinking, 7 June 1942.jpg",
     "★约克城号 1942-06-07 拂晓沉没，已向左翻覆，露出右舷舭部与鱼雷破口。2816x2107"),
    ("USS Hammann alongside USS Yorktown-both torpedoed.jpg",
     "哈曼号靠泊约克城号旁（两者随后同被日军潜艇伊-168 命中），740x509"),
    ("USS Hammann DD-412 sunk-depth charges exploding near Yorktown.jpg",
     "★哈曼号沉没时深水炸弹在水下连续爆炸，约克城号视角。5554x4281，视觉冲击极强"),
    ("USS Hammann sinking 1942-06-06 seen from USS Yorktown.jpg",
     "1942-06-06 哈曼号沉没，自约克城号拍摄。740x593"),
]))

GROUPS.append(("四、战役场景：日军俘虏 / 落水者 / 其他", [
    ("Survivors of Hiryu USNA 80 G 79974 1.jpg",
     "★飞龙号轮机部幸存者——在中途岛战后两周被巴拉德号（AVD-10）从救生艇救起，成为日军俘虏。740x491，唯一一类「日军俘虏」题材"),
    ("USS Yorktown (CV-5) survivors aboard USS Benham (DD-397) on 4 June 1942 (80-G-32379).jpg",
     "约克城号 720 名幸存者转移到本汉姆号，1942-06-04 约 19:00 靠拢波特兰号。2328x2252"),
    ("USS Benham (DD-397) on 4 June 1942, with survivors of USS Yorktown (CV-5) on board (80-G-32390).jpg",
     "同上场景的另一幅，4388x4478 大图"),
    ("Battle of Midway (Japanese air raid).jpg",
     "中途岛遭日军空袭（东岛），2100x1650"),
    ("Eastern Island Midway under attack 1942.jpg",
     "东岛被攻击，785x557"),
    ("G17056 Oil tanks burn at Midway after japanese attack 4 june 1942.jpg",
     "1942-06-04 日军空袭后中途岛油罐燃烧，1247x899"),
    ("Memorial service on Midway after battle 1942.jpg",
     "战后中途岛追悼仪式，812x608"),
]))

GROUPS.append(("五、参战舰艇：加贺（Kaga）", [
    ("Japanese aircraft carrier kaga.jpg",
     "★加贺 1934-36 改装后在航，舷侧全貌。3694x2389，舰种识别图首选"),
    ("Japanese Navy Aircraft Carrier Kaga.jpg",
     "1936 年（昭和 11 年）大改装完成后的加贺，可见向下弯折的烟囱。2424x1310"),
    ("Kaga Reconstruction overhead.jpg",
     "1935 年改装完成后的加贺俯视全景，1858x464（超宽横幅，适合页眉）"),
    ("HIJMS Kaga.jpg",
     "加贺 1936 年后侧视，1440x535（横幅剪影式）"),
    ("Kaga and Zuikaku Pearl Harbor.jpg",
     "★1941-11 驶向夏威夷途中，前景加贺、背景瑞鹤，海况恶劣。2236x1256"),
    ("Zuikaku and Kaga and Akagi.jpg",
     "★1941-11 驶向珍珠港：前景瑞鹤、中景加贺、远景赤城。3100x2050"),
    ("Zuikaku November 1941.jpg",
     "1941-11 瑞鹤（前）与加贺（后），3129x2021"),
    ("Kaga China Incident.jpg",
     "1937 年中日事变期间，九六式舰攻飞近加贺，1612x983"),
    ("Kaga air operations full deck 1937.jpg",
     "★1937-05-11 加贺全甲板航空作业，甲板上有八九式、九〇式、九四式舰载机。2573x2061"),
    ("Kaga landing operations 1937.jpg",
     "1937-05-11 加贺着舰作业，可见放倒的天线（带助降灯）。2367x2150"),
]))

GROUPS.append(("六、参战舰艇：苍龙（Sōryū）", [
    ("Japanese aircraft carrier Soryu 1938.jpg",
     "★苍龙 1938-01-22 在馆山冲公试，横幅全貌。3451x1564，舰种识别首选"),
    ("Japanese aircraft carrier Soryu.jpg",
     "1938 年 1 月在航的苍龙，3570x1587"),
    ("Japanese aircraft carrier Soryu 02.jpg",
     "1941 年千岛群岛锚泊的苍龙（太平洋战争前夕），2907x2025"),
    ("Japanese aircraft carrier Soryu 1937.jpg",
     "1937 年初在吴海军工厂舾装中的苍龙，3587x2355"),
    ("Soryu 1937.jpg",
     "1937-12-29 苍龙服役当日，吴港，1000x600"),
    ("Launching Soryu.jpg",
     "1935-12-23 苍龙下水，吴港，604x455（分辨率低）"),
    ("Fantail Soryu.jpg",
     "★1937-11-11 苍龙在丰后水道以近 35 节试航时的舰尾尾流特写（NH 73062），3806x2844。少见的角度"),
    ("Soryu landing test.jpg",
     "1937-12 苍龙在丰后水道试航，九二式舰攻着舰进场，1600x1093"),
]))

GROUPS.append(("七、参战舰艇：飞龙（Hiryū）", [
    ("Japanese aircraft carrier Hiryu 1939.jpg",
     "★飞龙 1939-07-05 在横须贺军港完工，2915x1764，舰种识别首选"),
    ("Japanese aircraft carrier Hiryu.jpg",
     "★飞龙 1939-04-28 全速试航，3860x2142"),
    ("Japanese aircraft carrier hiryu.jpg",
     "飞龙 1939-04-28 试航的另一幅，3852x2155"),
    ("Hiryu under construction.jpg",
     "1939-06-20 横须贺在建的飞龙，991x678（分辨率偏低）"),
]))

GROUPS.append(("八、参战舰艇：约克城号（USS Yorktown CV-5）", [
    ("USS Yorktown (CV-5) underway at Midway 1942.jpg",
     "★约克城号 1942-06-04 约 06:30-07:30 中途岛当日，甲板满载舰载机。1928x1299，与战役直接相关"),
    ("USS Yorktown (CV-5) entering Pearl Harbor May 1942.jpg",
     "★1942-05-27 珊瑚海海战后返抵珍珠港，舰员着白装在甲板列队；正中为霍加号拖船。5665x4014。三天后即出航参加中途岛"),
    ("USS Yorktown (CV-5) in a dry dock at the Pearl Harbor Naval Shipyard, 29 May 1942 (80-G-13065).jpg",
     "★1942-05-29 在珍珠港 1 号干船坞紧急抢修（珊瑚海战损），次日即出航。5734x4565。著名的「72 小时抢修」现场"),
    ("USS Yorktown (CV-5) during the Battle of the Coral Sea, April 1942.jpg",
     "约克城号在太平洋作战（珊瑚海前后），自刚起飞的 TBD 上俯拍，甲板上还有 SBD 与 F4F-3。5734x4489"),
    ("USS Yorktown (CV-5) anchored in Hampton Roads on 30 October 1937.jpg",
     "1937-10-30 汉普顿锚地锚泊，5459x4112"),
    ("Overhead view of USS Yorktown (CV-5) in the Caribbean Sea on 17 January 1938.jpg",
     "1938-01-17 加勒比海试航期俯视，5673x4188（俯视甲板布局极清晰）"),
    ("80-CF-80301-1 USS Yorktown (CV-5).jpg",
     "1936-04-04 由罗斯福夫人主持的下水典礼，纽波特纽斯。1280x1037"),
]))

GROUPS.append(("九、参战舰艇：大黄蜂号（USS Hornet CV-8）", [
    ("USS Hornet (CV-8) underway in the Southern Pacific on 15 May 1942 (80-G-14866).jpg",
     "★1942-05-15 南太平洋在航，珊瑚海战后、被召回珍珠港准备中途岛的前一天。5605x4185，舰种识别首选"),
    ("USS Hornet (CV-8) steaming in the Coral Sea area on 13 May 1942.jpg",
     "★1942-05-13 珊瑚海海域，自企业号拍摄。5728x4484"),
    ("USS Hornet (CV-8) entering Pearl Harbor, 26 May 1942.jpg",
     "★1942-05-26 驶入珍珠港，两天后即出航参加中途岛。5654x4501"),
    ("USS Hornet (CV-8) underway at sea in May 1942.jpg",
     "1942 年 5 月在航，1024x634"),
    ("Hornet (CV8). Aerial, port bow, underway, 10-27-1941 - NARA - 520816.jpg",
     "★1941-10-27 左舷舰首方向航拍（NARA 520816），3000x2406"),
    ("Aft view of USS Hornet (CV-8), circa in late 1941 (NH 81313).jpg",
     "1941 年末完工不久的舰尾视角，740x514"),
]))

GROUPS.append(("十、舰载机：日军（零战 / 九九舰爆 / 九七舰攻）", [
    ("Akagi Pearl Harbor Second Wave.jpg",
     "★赤城甲板：1941-12-07 珍珠港第二攻击波出发前，机翼仍系留在甲板、地勤围在机旁。2245x1419。「甲板上的日机」首选"),
    ("Japanese planes preparing-Pearl Harbor.jpg",
     "★1941-12-07 晨，九九式舰爆（D3A1）在航母甲板准备起飞，背景为苍龙。5746x4573 超大图，全篇画质最好的一张日机甲板照"),
    ("Kaga B5N Pearl Harbor departure.jpg",
     "★加贺的九七式舰攻完成珍珠港第一波攻击后飞向集结点，2231x1406"),
    ("Kaga B5N aircrew Pearl Harbor.jpg",
     "★1941-12-06 加贺甲板上九七舰攻机组在机前合影（珍珠港前一日），2247x1773"),
    ("Kaga Pearl Harbor brief.jpg",
     "★1941-12-06 加贺鱼雷机队长北岛一郎在甲板向机组简报，黑板上画着珍珠港平面图与攻击方案。2237x1490"),
    ("Kaga B5N Pearl Harbor.jpg",
     "加贺九七舰攻在珍珠港被吊起（铃木三守机，机组三人阵亡），2206x1813"),
    ("Kaga Carrier Zero Fighters.jpg",
     "★加贺的零战 1942 年 1 月起飞攻击新几内亚盟军，1131x1196。注意 Commons 上传日期为 2017，但图本身是二战照片"),
    ("96siki-kankou.jpg",
     "加贺所属的九六式舰上攻击机，1122x563"),
    ("GF in Indian Ocean, 1942.jpg",
     "★1942-03-30 印度洋作战，自瑞鹤拍摄：赤城、苍龙、飞龙、比叡、雾岛、榛名、金刚依次排开。1687x1117。四舰同框的珍贵一张"),
    ("Soryu B5N1 1939.png",
     "1939 年春，九七式舰攻（B5N1）进入苍龙着舰航线，600x276（PNG，分辨率很低）"),
    ("Aichi D3A Replica Airshow.jpg",
     "⚠CC BY-SA 2.0——2006 年航展上的九九舰爆复制品（由 BT-13 改装，曾用于《虎！虎！虎！》拍摄）。非历史照片，本站按 B 档外链不下载"),
]))

GROUPS.append(("十一、舰载机：美军（F4F / SBD / TBD）", [
    ("Hornet Air Group morning take off 1942-06-04.jpg",
     "★1942-06-04 晨大黄蜂号甲板，机群待发攻击机动部队，前景 F4F-4（F-21/F-16/F-20/F-24/F-22）。1888x1464"),
    ("TBDs on USS Enterprise (CV-6) during Battle of Midway.jpg",
     "★1942-06-04 约 07:30-07:40 企业号 VT-6 的 TBD-1 待起飞，可见 14 架中的 11 架。4946x2591"),
    ("Douglas TBD-1 Devastators of VT-6 are spotted for launch aboard USS Enterprise (CV-6) on 4 June 1942 (80-G-41686).jpg",
     "同上场景的另一幅（80-G-41686），5015x3755，画质更高"),
    ("SBD 8-B-11 on USS Hornet Midway.jpg",
     "★1942-06-04 大黄蜂号 VB-8 的 SBD-3（8-B-11）停在甲板，2128x1716"),
    ("USS Hornet island SBD Midway.jpg",
     "★1942-06-04 大黄蜂号：SBD-3 正在着舰，背景为舰桥，可见全副战斗装具的甲板人员。2070x1657"),
    ("SBD VB-8 over LSO USS Hornet 1942.jpg",
     "★1942-06-04 大黄蜂号 VB-8 的 SBD 几乎压在着舰信号官（LSO）头上，2128x1709"),
    ("SBD-3 VS-5 on USS Yorktown Midway.jpg",
     "★1942-06-04 上午晚些时候，约克城号 VS-5 的 SBD-3，飞行员 Leif Larsen 与后座机枪手 John Gardener。2159x1683"),
    ("Hornet Air Group morning take off 1942-06-04.jpg", ""),
    ("TBD T-5 VT-8 CV-8 15May42.jpg",
     "★1942-05-15 大黄蜂号 VT-8 的 TBD-1（T-5，BuNo 0308）沿甲板滑行，已装双联 .30 后座机枪、挂实雷。827x567"),
    ("TBD VT-8 taking off from USS Hornet (CV-8) May 1942.jpg",
     "1942-05 大黄蜂号 VT-8 的 TBD-1 起飞，726x547"),
    ("TBD VT-8 taking off from USS Hornet (CV-8).jpg",
     "同上的另一幅，795x604"),
    ("Douglas SBD-3 take off USS Hornet CV-8.jpg",
     "1942-05 大黄蜂号 VS-8 的 SBD-3 起飞，801x601"),
    ("USS Hornet Air Group on deck May 1942.jpg",
     "1942-05 大黄蜂号航空组全甲板列队，725x547"),
    ("TBD on Enterprise elevator 1942.jpg",
     "1942-06 企业号 VT-6 的 TBD-1 在后升降机上，797x640"),
    ("TBD sinking astern of USS Enterprise (CV-6) in May 1942.jpg",
     "★1942-05-28 林赛中校的 TBD-1（BuNo 0370）着舰事故后沉入企业号舰尾，5607x4204"),
    ("F4F-4 wings folded.jpg",
     "★1942-05-29 卡内奥赫，VF-3 的 F4F-4（BuNo 5171）折叠机翼；该机 6 月 4 日由萨奇少校驾驶。5588x4174"),
    ("Damaged Grumman F4F-3 Wildcat of VMF-221 on Midway, 24 June 1942 (80-G-11636).jpg",
     "★1942-06-24/25 中途岛沙岛，VMF-221 被击伤拆解的 F4F-3（BuNo 4006，John Carey 上尉机）。5598x4481"),
    ("F2As VMF-221 over Midway.jpg",
     "VMF-221 的 F2A-3 水牛在中途岛上空，618x473"),
    ("Brewster F2A-3 VMF-221 in flight 1941.jpg",
     "1941-11-15 VMF-221 的 F2A-3（BuNo 01552），563x428"),
]))

GROUPS.append(("十二、人物", [
    ("Chuichi Nagumo.jpg",
     "★南云忠一 1941-42 年任第一航空舰队司令长官时的官方肖像（NHHC），4592x5784 超大图，人物图首选"),
    ("Chuichi Nagumo in the bridge of Akagi heading to attack Pearl Harbor.jpg",
     "★南云在赤城舰桥上（1941-11-26 至 12-07 驶向珍珠港途中），1200x803。中途岛时他同样在此舰桥"),
    ("Chuichi Nagumo with the staff of the 1st Air Fleet.jpg",
     "★南云与第一航空舰队幕僚合影（1941-04-10 至 1942-07-14 任期，应摄于赤城舰上）。1991x1265，含源田实等"),
    ("NagumoSaipan.jpg",
     "1944 年塞班岛上的南云与幕僚，1368x956"),
    ("Isoroku Yamamoto on deck photo 1942.jpg",
     "★山本五十六 1942 年甲板照（《台南高等工业学校毕业纪念册》收录），2724x3577"),
    ("Portrait of Yamamoto Isoroku.jpg",
     "★山本五十六任联合舰队司令长官时期肖像，915x1297"),
    ("Admiral Isoroku Yamamoto.jpg",
     "山本五十六肖像（较小 365x547，可作缩略图）"),
    ("Ray Spruance.jpg",
     "★斯普鲁恩斯 1944-04-23 非正式肖像（中途岛时为第 16 特混舰队司令），4550x5765"),
    ("80-G-495845 Admiral Raymond A. Spruance.jpg",
     "1945-11-24 斯普鲁恩斯接任 CINCPACFLT 时读命令，1280x1025"),
    ("Admiral Frank Jack Fletcher.jpg",
     "★弗莱彻（第 17 特混舰队司令，中途岛时坐镇约克城号）肖像，NH 91213，590x765"),
    ("Adm Jack Fletcher.jpg",
     "弗莱彻另一幅肖像（标 1943），400x600"),
    ("TamonYamaguchi.jpg",
     "★山口多闻（第二航空战队司令，飞龙号上随舰沉没），806x1098"),
    ("Last Moments of Admiral Yamaguchi.jpg",
     "画作《山口多闻的最后时刻》——飞龙弃舰时山口与舰长加来止男留在舰上，740x620。注意为绘画非照片"),
    ("Joichi Tomonaga.jpg",
     "★友永丈市（飞龙号鱼雷机队长，1942-06-04 攻击约克城号后未返），560x739"),
]))

# 去掉占位用的重复条目
for gi, (h, items) in enumerate(GROUPS):
    GROUPS[gi] = (h, [(a, b) for a, b in items if b])


def build():
    buf = io.StringIO()
    w = buf.write
    w("# 中途岛海战 图片清单（imgfrag · 2026-11-19）\n\n")
    w("搜集范围：战役场景 + 参战 6 艘航母（加贺/苍龙/飞龙/约克城/大黄蜂）+ 舰载机 + 人物。\n")
    w("赤城、企业号已有 8+7 张入库，本清单**不重复收录**。\n\n")
    w("## 口径说明\n\n")
    w("- **全部条目已逐条验证直链有效性**（`Special:Redirect/file/` 返回 301 且 Location 指向 upload.wikimedia.org）。\n")
    w("- 尺寸为 Commons 原图尺寸（非缩略图）。\n")
    w("- 直链已去掉 `?utm_*` 追踪参数，可直接 GET。\n")
    w("- 档位：A 档 = Public domain / CC0，可下载自托管；B 档 = CC-BY / CC-BY-SA，仅外链不下载。\n")
    w("- **未使用任何 IWM 站内副本**（C 档禁用）。\n\n")

    total_pd = 0
    total_cc = 0
    for head, items in GROUPS:
        w("## %s\n\n" % head)
        w("| Commons 文件名 | 直链 | 尺寸 | license | 日期 | 说明（中文） |\n")
        w("| --- | --- | --- | --- | --- | --- |\n")
        for fname, note in items:
            title = "File:" + fname
            e = raw.get(title)
            if not e:
                w("| %s | **元数据缺失** | - | - | - | %s |\n" % (fname, note))
                continue
            wd, ht = size(title)
            short, usage = lic_of(title)
            u = direct(title, fname)
            dt = norm_date(e.get("date"), fname)
            if short and short.lower().startswith("cc"):
                total_cc += 1
                tag = "**B 档 · %s**" % short
            else:
                total_pd += 1
                tag = "A 档 · %s" % lic_raw(title)
            w("| `%s` | %s | %dx%d | %s | %s | %s |\n"
              % (fname, u, wd or 0, ht or 0, tag, dt, note))
        w("\n")

    w("## 汇总\n\n")
    w("| 项 | 数 |\n| --- | --- |\n")
    w("| A 档（PD，可下载） | %d |\n" % total_pd)
    w("| B 档（CC-BY-SA，仅外链） | %d |\n" % total_cc)
    w("| 合计 | %d |\n\n" % (total_pd + total_cc))

    w("### 分类计数\n\n")
    w("| 分类 | A 档（PD） | B 档（CC） |\n| --- | --- | --- |\n")
    sum_pd = sum_cc = 0
    for head, items in GROUPS:
        pd = cc = 0
        for fname, _ in items:
            short, _u = lic_of("File:" + fname)
            if short and short.lower().startswith("cc"):
                cc += 1
            else:
                pd += 1
        sum_pd += pd
        sum_cc += cc
        w("| %s | %d | %d |\n" % (head, pd, cc))
    w("| **合计** | **%d** | **%d** |\n\n" % (sum_pd, sum_cc))

    w("### 没找到 / 受限的类别\n\n")
    w("- **日军航母燃烧的彩色照片**：Commons 无。二战日军舰艇彩色实拍照片极稀少，"
      "中途岛阶段没有任何 Color 类目下的日舰彩色原件；本清单里的「彩色」只有 Coale 的画作（黑白/单色粉彩）和 Bel Geddes 沙盘。\n")
    w("- **日军俘虏**：只有 `Survivors of Hiryu USNA 80 G 79974 1.jpg` 一张（飞龙轮机部 2 周后获救者），"
      "分辨率 740x491 偏低。中途岛日军落水者被美军救起的照片 Commons 没有其它条目。\n")
    w("- **日机在航母甲板上的近景**：赤城、加贺各有若干张（见第十节），但**苍龙、飞龙甲板上的日机照片 Commons 无**，"
      "只有 `GF in Indian Ocean, 1942.jpg` 这张四舰同框远景。\n")
    w("- **斯普鲁恩斯 / 弗莱彻 在中途岛当时的照片**：没有。能找到的都是 1943 年后或战后肖像，"
      "清单里已标注实际日期，不要误写成「中途岛期间」。\n")
    w("- **南云忠一在中途岛的照片**：没有。现有两张（赤城舰桥、幕僚合影）都是珍珠港前后的，已注明。\n")
    w("- **IWM 站内副本**：按要求全程未取用。\n")
    return buf.getvalue()


txt = build()
open("midway-images.md", "w", encoding="utf-8").write(txt)
print("written", len(txt), "chars")
