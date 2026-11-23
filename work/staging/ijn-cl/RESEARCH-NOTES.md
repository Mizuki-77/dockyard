# 调研底稿 —— 旧日本海军轻巡：长良（长良型）/ 川内（川内型）

> 2026-11-23 · ijn-cl 组 · 供 Dockyard 二战战舰资料站入库
> 工作目录 `work/staging/ijn-cl/` · 原始页面在 `_raw/`

---

## 0. 一句话结论

两舰**不同级**（长良型 6 艘 / 川内型 3 艘），已各建一个 class 文件。
中途岛编队：**长良 = 第十水雷战队旗舰，随南云机动部队（第一航空舰队警戒队）**；
**川内 = 第三水雷战队旗舰，随山本主力部队，在主战场后方 600 海里，全程未交战**。
结局：**长良 1944-08-07 在天草诸岛以西被 USS Croaker 击沉**（不是 1943、不在瑙鲁附近）；
**川内 1943-11-02 在布干维尔奥古斯塔皇后湾海战中被美军巡洋舰击沉**（地点对、方式需订正）。
**鱼雷再装填装置（次発装填装置）装几组：两舰均未获取**，见 §6。

---

## 1. 抓取方式与可达性（实测）

按任务书要求**全程未用 `web_fetch` / `research`**（本机 SSRF 拦截）。
统一用 Python `urllib` + 浏览器 UA 直连，抓取脚本 `_tools/fetch.py`，
HTML→文本 `_tools/totext.py`，PDF→文本 `_tools/pdftotext.py`。

| 站点 | 结果 | 备注 |
|---|---|---|
| combinedfleet.com | 200 | 主力，TROM + 级页参数卡 |
| navypedia.org | 200 | 主力，主尺度/排水/装甲/改装台账 |
| navweaps.com | 200 | 主力，14 cm/50 三年式主炮页 |
| kasado.net | 200 | 逐部位装甲表（做 qual 化的关键） |
| japanese-warship.com | 200 | 三时点装备表 |
| naval-encyclopedia.com | 200 | 旁证（页内自相矛盾较多） |
| dougakan675.blog49.fc2.com | 200 | 鱼雷发射管沿革（日文技术随笔） |
| ja.wikipedia.org | 200 | **tier E，只作线索** |
| archive.navalsubleague.org | 200 | 日本鱼雷综述（英文） |
| legacy.maritime.org（ONI 222-J） | **403** | 放弃，未重试 |
| hnsa.org `/oni222j.pdf` | **404** | 放弃 |
| fischer-tropsch.org（USNTMJ O-01-3 PDF） | 200 但**扫描件无文本层** | 20 页只提取出 411 字符，不可用作原句来源 |

抓取脚本还遇到两个坑，已解决并写进 `_tools/`：
- **日文站编码**：kasado.net 声明 utf-8 但实际混用，第一版直出乱码；
  `fetch.py` 改为「HTTP 头 charset → meta charset → 尝试 cp932/euc_jp」的逐级回退后才正常。
- **YAML 行内标量含 `': '`**：`note: navypedia 原话「deck: 29 (...)」` 会让 PyYAML 报
  `mapping values are not allowed here`。已用 `_tools/fixnote.py` 全部改成双引号包裹。

---

## 2. 任务书核对结果（**主会话请读这一节**）

任务书里的史实陈述按规矩一律当「待核实」，逐条核完如下：

| # | 任务书原话 | 核查结果 | 依据 |
|---|---|---|---|
| 1 | 「两舰都参加了 1942-06 中途岛」 | **正确** | combinedfleet 两页 TROM 均有 1942-05-27/29 出击记录 |
| 2 | 「这两舰不同级：长良属长良型（6 艘），川内属川内型（3 艘）」 | **正确** | navypedia 两级页面标题与建造表 |
| 3 | 「长良是第 10 水雷战队旗舰（机动部队本队）」 | **基本正确，需精确** | 她是 DesRon 10 旗舰，隶属**第一航空舰队**（南云机动部队）的**警戒队**，不是「本队」。见 §3.1 |
| 4 | 「川内是第 3 水雷战队旗舰（主力部队）」 | **正确** | combinedfleet「30 May ... with the CINC ... Main Body」+「The Main Body remains 600 miles behind」 |
| 5 | 「两舰结局都沉于 1943 年」 | **错一半** | **长良是 1944-08-07**；川内 1943-11-02 正确 |
| 6 | 「长良在瑙鲁附近被潜艇击沉？」 | **错两处** | 日期错（1944 非 1943）、地点错（**天草诸岛以西 32-09N 129-53E**，不是瑙鲁）。她 1943-06 确实跑过瑙鲁运输，疑与地点混淆 |
| 7 | 「川内在布干维尔？」 | **地点对，方式需订正** | 布干维尔岛奥古斯塔皇后湾海战，**被美军四艘轻巡雷达射击命中后沉没**，不是被潜艇或飞机击沉 |
| 8 | 「鱼雷再装填装置是日本轻巡/驱逐舰的特色，查清长良与川内各装几组」 | **两舰均未获取** | 见 §6，这是本组最大的空白，如实报告 |

---

## 3. 中途岛编队（任务重点，逐条原句）

### 3.1 长良：第十水雷战队旗舰 / 第一航空舰队警戒队

> 「10 April 1942: NAGARA is assigned as flagship of Rear Admiral (later Vice Admiral)
> Kimura Susumu's (40)(former CO of HARUNA) new DesRon 10 with DesDiv 7's NOWAKI, ARASHI,
> HAGIKAZE and MAIKAZE, DesDiv 10's MAKIGUMO, KAZAGUMO and YUGUMO and DesDiv 17's URAKAZE,
> ISOKAZE, HAMAKAZE and TANIKAZE. DesRon 10 is assigned to Vice Admiral (Admiral,
> posthumously) Nagumo Chuichi's (former CO of YAMASHIRO) First Air Fleet.」
> — combinedfleet.com/nagara_t.htm

> 「27 May 1942: NAGARA departs Hashirajima with DesDiv 7, DesDiv 10 and DesDiv 17 and
> Vice Admiral Nagumo's Carrier Striking Force's CarDiv 1's AKAGI and KAGA, CarDiv 2's
> HIRYU and SORYU and Rear Admiral ... Abe Hiroaki's ... Support Group's CruDiv 8's TONE
> and CHIKUMA, BatDiv 3/2's HARUNA and KIRISHIMA」
> — 同上

> 「At 1047, after flagship AKAGI is hit and set afire by dive-bombers from ENTERPRISE,
> Vice Admiral Nagumo transfers his flag to destroyer NOWAKI. At 1130, Nagumo transfers
> to NAGARA.」
> — 同上

**订正说明**：任务书写「机动部队本队」。严格讲长良属南云机动部队的**警戒队（護衛隊）**，
「本隊（Main Body）」在南军语汇里是山本亲率的那支（川内所在）。
两者若都写「本队」会混淆，故本站 fact 写「第一航空艦隊 第十水雷戦隊 旗艦」，
正文写「警戒队旗舰」。

### 3.2 川内：第三水雷战队旗舰 / 主力部队

> 「29 May 1942: "MI" Sakusen - The Battle of Midway: Departs Sukumo Bay with the CINC,
> Combined Fleet, Admiral (Fleet Admiral, posthumously) Yamamoto Isoroku's (former CO of
> AKAGI) Main Body and DesDiv 11's FUBUKI, SHIRAYUKI, MURAKUMO and HATSUYUKI, DesDiv 19's
> URANAMI, SHIKANAMI, AYANAMI, ISONAMI and YUKAZE. Screens BatDiv 1's YAMATO, NAGATO and
> MUTSU, escort carrier HOSHO, seaplane tenders CHIYODA and NISSHIN and Captain Nishioka
> Shigeyasu's Supply Group No. 1's oilers NARUTO and TOEI MARU.」
> — combinedfleet.com/sendai_t.htm

> 「The Main Body remains 600 miles behind Vice Admiral (Admiral, posthumously) Nagumo
> Chuichi's (former CO of KIRISHIMA) First Carrier Striking Force and does not engage
> American forces.」
> — 同上（这句是本组最关键的一句：川内全程未与美军交战）

中文侧的互证（tier E，仅作旁证）：
「第三水雷戦隊（軽巡川内《旗艦》…）は連合艦隊司令長官山本五十六大将直率の主力部隊に所属した」。

---

## 4. 结局（任务重点，逐条原句）

### 4.1 长良 1944-08-07（**不是 1943**）

> 「7 August 1944: Departs Kagoshima for Sasebo with a subchaser and two floatplanes as
> aerial cover. NAGARA is spotted by veteran submariner LtCdr (later Rear Admiral-Ret)
> John E. Lee's (USNA '30) new USS CROAKER (SS-246) on her first war patrol. Lee lets
> NAGARA close to 1,300 yards and fires a salvo of four stern torpedoes. At 1222, NAGARA
> is hit starboard aft by one of the torpedoes. At 1240, she sinks by the stern off
> Amakusa Shoto at 32-09N, 129-53E. Captain Nakahara and 348 crewmen are killed, but 237
> other men are rescued.」
> — combinedfleet.com/nagara_t.htm

> 「Nagara 15.7.1943 was damaged by a mine (laid by US submarine Silversides). 4.12.1943
> she was damaged by US carrier aircraft. 7.8.1944 she was sunk in 35nm S off Nagasaki by
> US submarine Croaker.」
> — navypedia.org/ships/japan/jap_cr_nagara.htm

两源在「1944-08-07 / Croaker / 长崎以南（= 天草诸岛以西）」上一致。
**任务书的「1943 年」「瑙鲁附近」两处均与来源不符**，本站以来源为准。

1943 年长良确有两次受损，可能是混淆源：
- 1943-07-15 卡维恩触雷（舰尾轻损）
- 1943-12-04/05 夸贾林空袭（近失弹致搭载鱼雷诱爆）

### 4.2 川内 1943-11-02

> 「2 November 1943: The Battle of Empress Augusta Bay ... At 0050, all four of Merrill's
> cruisers take SENDAI under radar directed 6-inch fire. They hit her with their first
> salvo and more thereafter setting her afire. ... At 0200, SENDAI is abandoned.
> ComDesRon 3 Rear Admiral Ijuin enters the water. 236 other SENDAI crewmen are rescued by
> destroyers. ... SENDAI remains afloat until 0430 when she sinks at 06-10S, 154-20E.
> Captain Shoji and 184 crewmen go down with her.」
> — combinedfleet.com/sendai_t.htm

> 「Sendai 2.11.1943 was destroyed in battle in Empress Augusta Bay by gunfire of US
> cruisers Montpelier, Cleveland, Columbia and Denver, later she was torpedoed by
> destroyers Charles Ausburn, Converse and Dyson.」
> — navypedia.org/ships/japan/jap_cr_sendai.htm

**分歧**：navypedia 多了「later she was torpedoed by destroyers」，combinedfleet 无此说。
两条并列，不裁决。

---

## 5. 数值对照与分歧（逐项，两边原话并列）

### 5.1 排水量口径 —— 最容易出错的一项

| 口径 | 长良型 | 川内型 | 原话 | 来源 |
|---|---|---|---|---|
| 基准/标准 | 5,170 t | 5,195 t | 「基準排水量 5,170t」/「Displacement standard, t 5195」 | kasado-nagara / navypedia-sendai |
| 常備 | 5,502 t | 5,595 t | 「常備排水量 5,502.81トン」/「常備排水量5,595t」 | kasado-nagara / kasado-sendai |
| 公表 | 5,570 英吨 | — | 「公表値 5,570英トン」 | tier E，仅线索 |
| normal | 5,570 t | — | 「Displacement normal, t 5570」 | navypedia-nagara |
| full | 7,050 t | 7,100 t | 「Displacement full, t 7050 / 7100」 | navypedia |

**结论**：`displacement.standard` 只有 5,170（长良是从 kasado 的「基準」栏取、
川内是从 navypedia 的「standard」栏取）。**combinedfleet 级页的 5,570 / 7,100 分别是
normal 与 full，不是标准排水量**，不能直接当 standard 引用。
注册表无常備字段，故常備值只写进 note，不立 fact。

### 5.2 舷侧装甲：63/64 vs 38 mm —— 两说并列，不裁决

> navypedia（长良级）：「Armour, mm | belt: 63, shields: 20, deck: 29 (45 over magazines),
> CT: 51 - 25」

> navypedia（川内级）：「Armour, mm | belt: 64, deck: 29」

> kasado（两级的同名栏目均写）：「水線部舷側装甲 38mm 装甲材質:高張力鋼」

可能解释（**仅见于 tier E，未采纳为裁决依据**）：日文维基作「舷側：63.5mm
(25.4+38.1mmHT鋼)」，即「2 层合计 63.5 mm」；kasado 可能只记承力的那一层 38.1 mm。
按红线 §2「不跨来源拼凑、不自己裁决」，本站在 classes 里两条都写、各带各的 src。

### 5.3 续航：5,000/14 vs 6,000/15 vs 9,000/10

> kasado（两级）：14.0kt / 5,000nm
> japanese-warship（长良）：「航続距離① 14ノット：5,000海里」
> navypedia（长良级）：「Endurance, nm(kts) | 6000(15)」
> navypedia（川内级）：「Endurance, nm(kts) | 6000(15)」
> naval-encyclopedia（长良级）正文：「a range of 6,000 nmi (11,000 km) at 14 knots」，
> 同页另一处又写「Their range, thanks to oil, was still of 9,000 nautical miles
> (17,000 km) at 10 knots cruising speed.」

三说并存，两级各写两条 fact（5,000 @ 14 + 6,000 @ 15），**不换算、不取平均**。
naval-encyclopedia 同页自相矛盾（6,000 @14 与 9,000 @10），未采用其数值。

### 5.4 川内型全长：162.15 / 162.46 / 163.0

> japanese-warship（川内本舰）：「全　長 162.15m」
> kasado（川内/那珂栏）：「全長 162.46m」
> navypedia（川内级）：「Length, m | 152.4 pp 158.5 wl 163.0 oa」
> naval-encyclopedia：「162.46m 全長」（隐含，未直引）

三说并列。navypedia 的 163.0 疑与那珂改舰首有关，但该页未说明适用范围，本站不归因。

### 5.5 川内型吃水 4.80 vs 4.91

> kasado：「吃水 常備時:4.80m」
> japanese-warship：「水線下幅14.17m」（未给吃水）、常備値 4.80 见 kasado
> navypedia：「Draught, m | 4.91」

两说并列（疑为常備/公試两种状态，来源未注明）。

### 5.6 乘员 450 vs 438 vs 452 vs 446

> navypedia（两级）：「Complement | 450」
> combinedfleet 级页（长良级）：「Crew | 438」
> combinedfleet 级页（川内级）：「Crew | 450」
> kasado（川内型）：「定員 452名」
> tier E（长良）：「竣工時定員450名」；（川内）：「川内竣工時定員446名」

长良型取 450（三源一致），川内型取 450（两源一致），438/452 写进 note 并列。

### 5.7 长良 1943-12-05 夸贾林空袭的伤亡：三说

> combinedfleet 正文：「The planes also damage light cruisers NAGARA and ISUZU ...」
> 「5 December 1943: ... NAGARA is damaged slightly by near misses.」

> combinedfleet 引 FRUMEL 截获电文（1943-12-13）：「2 men killed and ? injured in NAGARA
> when bombed in Marshal1s at 0510 on 5th December.」

> japanese-warship：「至近弾により搭載魚雷が誘爆、48名が死亡、艦長を含む112名が負傷した」

三说并列：「轻微损伤」/「2 死若干伤」/「48 死 112 伤」。
**注意第三种口径里舰长也受伤**，这是唯一提到舰长受伤的来源。

### 5.8 长良沉没伤亡 348 是否含舰长

> combinedfleet：「Captain Nakahara and 348 crewmen are killed, but 237 other men are
> rescued.」→ 舰长 + 348，即 348 不含舰长

> japanese-warship：「中原艦長以下348名が戦死し、237名が救助された」→「以下」含舰长

两说并列，数值同为 348，仅口径差一人。

### 5.9 长良触雷（1943-07-15）的布雷者：三说

> combinedfleet 正文：「While mooring, NAGARA detonates a mine laid at night by Australian
> PBY "Catalina" flying boats.」

> combinedfleet 脚注 [2]：「Some sources credit the mine as being laid 4 June 1943 by USS
> SILVERSIDES (SS-236).」

> navypedia：「Nagara 15.7.1943 was damaged by a mine (laid by US submarine Silversides)」

**同一页面内两说**（正文 vs 自己的脚注）。三条并列，不裁决。

### 5.10 雷达型号与时间（长良）

> combinedfleet：「20 August 1943: ... Drydocked and refitted. A Type 21 air-search radar
> set is fitted.」→ Type 21，1943-08

> navypedia：「5/1943, Abukuma; 10.1943, Nagara: + 1-shiki 2-go radar」
> → 一号二型，1943-10

型号名与月份都不同。**站内 fact 取 combinedfleet 的 1943-08 + Type 21**，
navypedia 的一号二型/10 月写进 note。

### 5.11 雷达型号与时间（川内）

> combinedfleet：「5 May 1943: ... A Type 21 radar is installed.」

> navypedia：「6/1943, Sendai: ... 1-shiki 2-go radar」

同 5.10 的结构：型号（Type 21 vs 一号二型）与月份（5 月 vs 6 月）都不同。

### 5.12 长良 1944 年鱼雷发射管：换没换四连装

这是本组**最实质的一处史料争议**，四个来源四种说法：

> ① combinedfleet（1944-01/04 舞鹤改装）：「The fore and aft twin torpedo tubes are
> removed and replaced by two quadruple tube mounts aft.」→ **换了**，后部四连装 2 基

> ② japanese-warship（1944-08 时点表）：「61cm4連装魚雷発射管 2基8門」→ **换了**

> ③ navypedia（1944-04 改装条）：「4/1944, Nagara: - 1 x 1 - 140/50 (No 7), 4 x 2 - 610 TT,
> catapult and seaplane; + ... 2 x 4 - 610 TT ...」→ **换了**，撤 4 基连装、加 2 基四连装

> ④ tier E（日文维基，引田村俊夫）：「1944年7月1日に作られた『艦船要目概要一覧表』には、
> 魚雷兵装に関して「連装発射管四基、九三式魚雷」と書かれている事」「あ号作戦後に作られた
> 『各艦機銃電探哨信儀等現状調査表』の図ではウェルデッキのままであり」「沈没時に米潜水艦
> クローカーから撮られた写真では、ウェルデッキが確認されている事」
> → **没换**（田村俊夫的质疑：改装无根据，发射管仍是连装 4 基，只是改造得以发射九三式）

**本站处理**：fact 层按 ①②③ 取「1944-04 起为四连装 2 基 8 门」，
但把 ④ 的质疑**完整写进 fact 的 note 与正文**，不裁决、不隐藏。

### 5.13 日方主炮高角炮数：2 门 vs 4 门

> navypedia（长良级）：「2 x 1 - 76/40 3-shiki」
> naval-encyclopedia：「two 2 × 8 cm/40 3rd Year Type naval gun」（= 2 门）
> kasado（长良级）：「三年式 40口径7.6cm単装高角砲:4基」→ **4 门**

长良型取 2 门（两源），kasado 的 4 门写进 note。
川内型三源一致为 2 门（navypedia / kasado / japanese-warship），无分歧。

### 5.14 机雷数：48 vs 56

> navypedia（两级）：「48 mines」
> naval-encyclopedia（长良级）：「48 naval mines」
> kasado（川内型）与 tier E：56 个（九三式機雷56個）

fact 层取 48（英文两源一致），56 写进 note 并列。tier E 不作来源。

### 5.15 速力（长良）：36.0 / 34.5 / 32

> kasado：「速力 36.0kt」（竣工时）
> japanese-warship：「速力① 計画36.0ノット / ② 34.5ノット」（1934 改装后）
> navypedia：「Max speed, kts | 36」，正文「maximal speed has decreased to 32kts」且注
> 「1934 - 1935, all: solid and liquid ballasts were added, full displacement increased to
> 8000t and speed fell to 32kts」

改装后两说（34.5 / 32）并列，两条 fact。

### 5.16 川内型锅炉数：12 基，但混烧比例两说

> navypedia：「12 Kampon boilers」
> kasado：「ロ号艦本式重油専焼水管罐:12基」→ 12 基全重油专烧
> japanese-warship：「混焼4基、重油8基」→ 4+8=12，但含 4 基混烧

**总数三源一致 12 基**，分歧只在混烧炉是否计入/占比。两条并列。
（本组第一稿曾把 4+8 误算成 14 并写成两条冲突的 fact，已修正为统一 12 基 + 比例并列。）

---

## 6. 卡住的地方（**本组最重要的空白，请主会话知晓**）

### 6.1 鱼雷再装填装置（次発装填装置）装几组 —— 未获取

任务书明确要求「查清长良与川内各装几组」。**本组未能完成这一项**，理由如下：

查过的全部来源里，只有一处出现「次発装填装置」这个词，且**不是长良也不是川内**：

> kasado 的「五十鈴 1945年頃」栏：「九二式 61.0cm四連装発射管 (次発装填装置付き):2基」
> — kasado.net/Cruisers/Japan/Nagara_1922.html

即：**只有五十鈴在 1945 年状态栏被明确标注「付き（带）」**。
长良栏、川内/那珂栏、神通栏**都没有这个字样**。

但「没写」≠「没有」。本组尝试过但失败的取证路径：
1. **combinedfleet 的长良/川内 TROM**：全文无 reload 相关字样（已 grep 确认）。
2. **combinedfleet 的 `torps.htm`**：只有一句「Typical Japanese destroyer mount. Note bank
   of reload tubes to rear, portside.」——讲的是**驱逐舰**的备用雷架，不是轻巡的装置。
3. **navweaps 的日方鱼雷页**（WTJAP_WWII / PreWWII）：给的是鱼雷本体参数，
   没有发射管/装填装置的舰级装配表。
4. **dougakan-cl4（日文技术随笔）**：讲了长良型「魚雷搭載数は両舷各二斉射分の一六本」、
   单座全备 13 t 余、5 hp 电机、360° 约 1 分钟——**但全文没有「次発装填装置」这个词**。
   它只说明「16 条 = 两舷各两个齐射份」，即**推论上存在 8 条备份雷**，
   而**没有一句说这些备份雷靠机械装置上膛**。
5. **naval-ency-sendai**：唯一出现英文「reload」的地方是
   「Eight tubes, but the same number or reloads (so 16 torpedoes in all).」
   —— 这里的「reloads」指**备份鱼雷**，不等于「机械再装填装置」，
   而且这句说的是那珂与神通，**不是川内**。
6. **USNTMJ O-01-3「Japanese Torpedoes and Tubes - Article 3, Above-Water Tubes」**：
   这份正是最该有答案的一手报告（美国海军技术调查团 1945 年实地拆解日本发射管），
   PDF 已下载（`_raw/usntmj-o-01-3.pdf`，20 页，2.3 MB），
   **但它是扫描件、无文本层**，PyMuPDF 20 页只提取出 411 字符。**本组无法读取**。
   本机无 OCR 工具链（未安装 tesseract）。

**结论**：本站两舰的 `classes` / `ships` 文件里**没有任何关于再装填装置组数的 fact**。
`armament.torpedo.tubes` 只记 8 门，`armament.mount.summary` 不提再装填。
正文里明写「本站在这一项上只查到 16 条鱼雷，没查到机械再装填装置的可靠记载」。

**建议主会话**：若这一项是 P2 必填，需要 (a) 上 OCR 处理 USNTMJ O-01-3，
或 (b) 引入 Lacroix & Wells《Japanese Cruisers of the Pacific War》（本组无法获取全书）。

### 6.2 其他未获取项（逐条列明，均未填 0）

| 字段 | 试过哪里 | 结论 |
|---|---|---|
| `armament.total_weight`（武备总重） | navypedia / kasado / japanese-warship / naval-encyclopedia | 四站均无 → 未获取 |
| `protection.underwater.depth`（水下防护纵深） | 同上 | 无防雷突出部，各站均未给数值 → 未获取 |
| `protection.armor.weight`（装甲总重） | 同上 | 均无 → 未获取 |
| `dimensions.depth.molded`（型深） | 英文四站均无；只有 tier E 有 29 ft | 未获取（tier E 不作来源） |
| `construction.cost`（造价） | 五站均无 | 未获取 |
| `service.fate_authority`（结局判定机构） | 所有来源均未说明由哪个机构判定 | 未获取 |
| `propulsion.boiler.pressure` / `.temperature` | navypedia / kasado / japanese-warship | 均无 → 未获取 |
| `weapon.range.max`（主炮最大射程） | navweaps | 只给分仰角射程表（20° 15,800 / 25° 17,500 / 30° 19,100 / 35° 20,574 m），无单一「最大射程 + 仰角」值 → 取任何单值都是插值，未获取 |
| `aviation.catapult.type`（弹射器型号） | 各站 | navypedia 只写「1 catapult」，无型号 → 未获取 |
| 川内型炮座防盾厚度 | navypedia（数据行只写 belt/deck）| 未单列 → 只有 kasado 的 25 mm 单源 |

**关于「0」的使用**：本组只用「0」表达「确实没有」，共 3 处，且都在 note 里写明理由：
- 两级 `aviation.catapult.count = 0`（竣工时确实无弹射器，来源写「-」）
- 川内型 `armament.aa_20mm.count = 0`（竣工时防空只有 8 cm 高角炮，25 mm 是 1937-38 才换的）

第一稿里曾把「未获取」写成 `value: 0`（armament.total_weight / construction.cost /
protection.underwater.depth），**已全部删除并改为注释说明「未获取」**。

---

## 7. 逐条原句索引（fact ↔ 原文）

以下按文件名列出每条 fact 对应的英文/日文原句，供校对。
（正文里已逐条嵌入，这里只列**关键项**，避免重复全文。）

### classes/nagara.yaml

| fact | 原句 | URL |
|---|---|---|
| displacement.standard 5170 | 「基準排水量 5,170t」 | kasado-nagara |
| displacement.full 7050 | 「Displacement full, t 7050」 | navypedia-nagara |
| length.oa 162.15 | 「全長 162.15m」 | kasado-nagara |
| length.wl 158.53 | 「水線長 158.53m」 | kasado-nagara |
| length.pp 152.40 | 「垂線間長 152.40m」 | kasado-nagara |
| beam.wl 14.17 | 「最大幅 14.17m」 | kasado-nagara |
| draught.mean 4.80 | 「Draught, m 4.80」 | navypedia-nagara |
| boiler.count 12 | 「12 Kampon boilers」 | navypedia-nagara |
| power.design 90000 | 「Power, h. p. 90000」 | navypedia-nagara |
| speed.design 36.0 | 「Max speed, kts 36」 | navypedia-nagara |
| fuel.capacity 1260 | 「Fuel, t coal 350 + oil 1260」 | navypedia-nagara |
| complement.standard 450 | 「Complement 450」 | navypedia-nagara |
| armor belt 63 | 「belt: 63, shields: 20, deck: 29 (45 over magazines), CT: 51 - 25」 | navypedia-nagara |
| armor belt 38 | 「水線部舷側装甲 38mm 装甲材質:高張力鋼」 | kasado-nagara |
| mine.capacity 48 | 「48 mines」 | navypedia-nagara |
| torpedo.tubes 8 / diameter 610 | 「4 x 2 - 610 TT」 | navypedia-nagara |
| weapon 14cm 全组 | 「Official Designation: 50 caliber 3rd Year Type 14 cm Gun」等 | navweaps-14cm-50-3ns |

### classes/sendai.yaml

| fact | 原句 | URL |
|---|---|---|
| displacement.standard 5195 | 「Displacement standard, t 5195」 | navypedia-sendai |
| displacement.full 7100 | 「Displacement full, t 7100」 | navypedia-sendai |
| length.oa 162.15 / 163.0 | 「全長 162.15m」/「163.0 oa」 | japanese-warship-sendai / navypedia-sendai |
| draught.mean 4.80 / 4.91 | 「吃水 常備時:4.80m」/「Draught, m 4.91」 | kasado-sendai / navypedia-sendai |
| boiler.count 12 | 「12 Kampon boilers」/「混焼4基、重油8基」 | navypedia-sendai / japanese-warship-sendai |
| 四烟囱由来 | 「instead of two boilers with mixed firing Sendai class cruisers had four boilers in No1 and No2 boiler rooms, that has caused increase in number of funnels from three to four」 | navypedia-sendai |
| speed.design 35.25 | 「速力 35.25kt」 | kasado-sendai |
| armor belt 64 / 38 | 「belt: 64, deck: 29」/「水線部舷側装甲 38mm」 | navypedia-sendai / kasado-sendai |
| 炮座仰角 30° | 「Sendai and Yubari: -7 / +30 degrees」 | navweaps-14cm-50-3ns |
| 川内不换四连装 | 「1941, Naka, Jintsu: - 4 x 2 - 610 TT; + 2 x 4 - 610 TT」（无 Sendai） | navypedia-sendai |

### ships/nagara.yaml

| fact | 原句 | URL |
|---|---|---|
| laid_down 1920-09-09 | 「9 September 1920: Sasebo Navy Yard. Laid down.」 | combinedfleet-nagara |
| launched 1921-04-25 | 「25 April 1921: Launched and named NAGARA.」 | combinedfleet-nagara |
| commissioned 1922-04-21 | 「21 April 1922: Completed and registered in the IJN.」 | combinedfleet-nagara |
| DesRon 10 旗艦 | 「10 April 1942: NAGARA is assigned as flagship of ... new DesRon 10 ...」 | combinedfleet-nagara |
| 南云移乘 | 「At 1130, Nagumo transfers to NAGARA.」 | combinedfleet-nagara |
| 一等瓜岛 6 死 | 「Six men are killed, but the ship sustains only minor hull damage.」 | combinedfleet-nagara |
| 夸贾林 48 死 | 「48名が死亡、艦長を含む112名が負傷した」 | japanese-warship-nagara |
| 沉没 348 死 / 237 生还 | 「Captain Nakahara and 348 crewmen are killed, but 237 other men are rescued.」 | combinedfleet-nagara |
| fate_date 1944-08-07 | 「7 August 1944 ... At 1240, she sinks by the stern off Amakusa Shoto at 32-09N, 129-53E.」 | combinedfleet-nagara |
| 1944 鱼雷管改四连装 | 「The fore and aft twin torpedo tubes are removed and replaced by two quadruple tube mounts aft.」 | combinedfleet-nagara |

### ships/sendai.yaml

| fact | 原句 | URL |
|---|---|---|
| laid_down 1922-02-16 | 「16 February 1922: Nagasaki. Laid down as a light cruiser at Mitsubishi Shipbuilding's Yard.」 | combinedfleet-sendai |
| commissioned 1924-04-29 | 「29 April 1924: Completed and registered in the IJN. Lead ship of the SENDAI-class.」 | combinedfleet-sendai |
| 主力部队 | 「29 May 1942: ... with the CINC ... Main Body ...」 | combinedfleet-sendai |
| 未交战 | 「The Main Body remains 600 miles behind ... and does not engage American forces.」 | combinedfleet-sendai |
| 公试 97,657 hp / 36.189 kn | 「公試97,657馬力」「公試36.189ノット」 | japanese-warship-sendai |
| 1943-05-05 改装 | 「A Type 21 radar is installed. The No. five 5.5-inch gun mount is removed. Two triple 25-mm AA gun mounts are installed.」 | combinedfleet-sendai |
| 旗舰移交新月 | 「That same day, destroyer NIIZUKI becomes flagship of DesRon 3.」 | combinedfleet-sendai |
| 沉没 | 「SENDAI remains afloat until 0430 when she sinks at 06-10S, 154-20E.」 | combinedfleet-sendai |
| 184 死 / 236 生还 | 「Captain Shoji and 184 crewmen go down with her.」「236 other SENDAI crewmen are rescued by destroyers.」 | combinedfleet-sendai |
| RO-104 救 75 人 | 「On 3 Nov 43, Rear Admiral Ijuin and 75 survivors from SENDAI are rescued by ... RO-104.」 | combinedfleet-sendai |

---

## 8. 本组内部的技术性修正记录（供主会话复核时跳过）

为透明起见，记录本组自查中发现并已修掉的问题：

1. **川内型锅炉数误算**：第一稿把「混焼4基、重油8基」读成 4+8=14 基，
   与 navypedia 的 12 基对立成「两说」。**实际 4+8=12**，三源一致。
   已改为单条 12 基 fact + 混烧比例并列的 note。
2. **「未获取」被写成 `value: 0`**：三处（armament.total_weight / construction.cost /
   protection.underwater.depth）。按红线「区分未获取与 0」，已全部删除并改注释。
3. **`armament.gun_failures` / `construction.fate_type` / `service.fate_authority` 被借用**：
   第一稿拿这三个字段承载「炮座形态」「触雷事件」「除籍日期」，属字段语义挪用。
   已改为：炮座形态进 `mount:*` 实体；触雷改用 `construction.fate_type: sunk_cause_disputed`
   并在 note 明写「本条不是结局」；除籍日期移进正文。
   **若主会话认为 fate_type 的这次借用也不可接受，请删除该条**（note 里已标）。
4. **navweaps 区间值取了中值**：炮重 5,600-5,700 取 5,650、初速 850-855 取 852、
   身管寿命 500-600 取 550。中值是本站折算，按「不推算」改取**区间下限**。
5. **`weapon.range.max` 插值**：第一稿在 25°(17,500 m) 与 35°(20,574 m) 之间插出
   19,560 m。已删除，改注释说明「来源无单一值」。
6. **YAML 语法**：`note:` 行内含 `': '` 会导致解析失败（6 处），`event` 里的 `src:`
   误缩进到 `text:` 之下（38 处）。均由 `_tools/fixnote.py` / `_tools/fixsrc.py` 修好，
   现 `_tools/selfcheck.py` 报告 0 error / 0 warning。

---

## 9. 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | **2**（classes/nagara.yaml 65 条 fact, classes/sendai.yaml 57 条 fact） |
| 单舰文件 | **2**（ships/nagara.yaml 48 条 fact, ships/sendai.yaml 31 条 fact） |
| 切片文件 | **2**（slices/nagara.yaml 7 片, slices/sendai.yaml 5 片） |
| 正文文件 | **2**（articles/nagara.yaml 5 节 34 事件, articles/sendai.yaml 5 节 30 事件） |
| 新登记来源 | **20**（其中 tier E 4 个，仅作线索；无一条 fact 引 tier E） |
| 骨架 34 字段覆盖 | 两舰均 **32 / 34**；缺 `protection.armor.weight`、`protection.underwater.depth`（均未获取，见 §6.2） |
| 自检结果 | `_tools/selfcheck.py`：**0 error / 0 warning** |


### 卡住的地方
- **鱼雷再装填装置组数：两舰均未获取**。全部可达来源里只有 kasado 的「五十鈴 1945 年」
  栏出现「次発装填装置付き」字样，长良与川内栏都没有。最该有一手答案的
  USNTMJ O-01-3 报告已下载但为无文本层扫描件（20 页仅提取 411 字符），
  本机无 OCR 工具链。详见 §6.1。
- 武备总重、装甲总重、水下防护纵深、型深、造价、锅炉压力/温度、主炮单一最大射程、
  弹射器型号、川内型炮座防盾厚度：均未获取，已逐项列在 §6.2，**一律未填 0**。

### 有争议的记载（全部并列，未裁决）
1. **舷侧装甲**：63/64 mm（navypedia）vs 38 mm（kasado）—— §5.2
2. **续航**：5,000@14（kasado/japanese-warship）vs 6,000@15（navypedia）vs 9,000@10（naval-ency）—— §5.3
3. **川内型全长**：162.15 / 162.46 / 163.0 —— §5.4
4. **川内型吃水**：4.80 vs 4.91 —— §5.5
5. **乘员**：450 / 438 / 452 / 446 —— §5.6
6. **长良夸贾林空袭伤亡**：轻微 / 2 死 / 48 死 112 伤 —— §5.7
7. **长良沉没 348 是否含舰长** —— §5.8
8. **长良触雷布雷者**：澳军 PBY / 美军潜艇 Silversides（同一页内两说）—— §5.9
9. **长良雷达**：Type 21 @1943-08 vs 一号二型 @1943-10 —— §5.10
10. **川内雷达**：Type 21 @5 月 vs 一号二型 @6 月 —— §5.11
11. **长良 1944 鱼雷管是否换四连装**：三源说换了、田村俊夫（经 tier E 转述）说没换 —— §5.12
12. **长良型高角炮数**：2 门 vs 4 门 —— §5.13
13. **机雷数**：48 vs 56 —— §5.14
14. **长良改装后速力**：34.5 vs 32 —— §5.15
15. **川内型混烧锅炉占比**：全重油专烧 vs 混烧 4 基 —— §5.16
16. **川内是否被驱逐舰补射鱼雷**：navypedia 说是、combinedfleet 无此说 —— §4.2

### 给主会话的三条提醒
1. `classes/nagara.yaml` 里建了 `weapon:14cm-50-3ns` 这个**全局武器实体**，
   `classes/sendai.yaml` 只写 `mount:sendai-14cm-single` 并引用它。
   合并时**不要**在两处各建一份武器实体。
2. `mount.type` 取了枚举 `single_turret`，但来源原话是「Single Pedestal Mounts（単装砲）」
   —— 这是枚举映射不是史实，若站内规范认为应归 `open_mount` / `shielded_mount`，
   请统一改（两级共 2 处）。
3. `ships/nagara.yaml` 里有一条 `construction.fate_type: sunk_cause_disputed`
   （valid 1943-07-15 当日），承载的是**触雷事件的归因分歧**，不是她沉没。
   若校验器会把它当结局参与时间轴，请删除该条、把内容并入正文（note 已标注）。
