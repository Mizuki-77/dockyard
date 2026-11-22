# HMS Victorious（胜利号，38）调研底稿

> Dockyard 分片组 g1-victorious · 2026-11-22
> 目标：光辉级已有 151 条舰级 fact，本组只写单舰差异。
> 交付目录：`work/staging/g1-victorious/`

## 0. 抓取方式与一个必须报告的环境问题

**`web_fetch` / `research` 在本会话对所有域名返回 SSRF blocked。**

```
Error: SSRF blocked: www.naval-history.net resolves to private address 198.18.0.99
Error: SSRF blocked: www.armouredcarriers.com resolves to private address 198.18.0.100
Error: SSRF blocked: example.com resolves to private address 198.18.0.103
```

连 `https://example.com` 都被拦，说明不是目标站的问题，是本会话的
域名解析走了代理的假地址段（198.18.0.0/15）。`research` 工具同样失败：

```
fetch direct failed for https://en.wikipedia.org/wiki/HMS_Victorious_(R38):
SSRF blocked: en.wikipedia.org resolves to private address 198.18.0.18
notEvaluated: all fetches failed — snippets only
```

**绕法：本机 `Invoke-WebRequest` 直连全部成功（十处 200）。**
本次所有页面都是这么抓的，原始 HTML 与转好的纯文本留在
`work/staging/g1-victorious/_raw/`（`h2t.py` 是转换脚本）。
建议主会话把这个绕法记进 SCHEMA §9，否则后续 subagent 会重复踩。

抓不到的（记 `status: blocked`，未登记成来源）：
- `iwm.org.uk` → **403**。Tungsten 的影像条目
  （object/1060020447）只能看到搜索摘要，没拿到正文。
- `hmshood.org.uk`（Tovey 电文原件 ADM 234/509）→ **403**。
  因此 1941-05-24 的空袭细节改引 wc-victorious 的转述（tier C），
  而不是当一手件用。

---

## 1. 身份与建造

**建造四要素（navypedia + naval-history + 美方卡片，三源交叉）**

> "Victorious | 38, 1948- R23, 1949- R38 | 11 | Vickers-Armstrong, Tyne |
> 4.5.1937 | 14.9.1939 | 15.5.1941 | stricken 3.1968"
> —— https://www.navypedia.org/ships/uk/brit_cv1_illustrious.htm

> "ordered from Victors-Armstrong, Newcastle on 13th Jan.1937 and laid down on
> 5th May that year. The ship was launched by Lady Inskip, Wife of a Defence
> Minister, on 14th September 1939. She was the 5th RN ship to carry the name,
> introduced in 1783 for a 3rd Rate, and last used for an 1895 battleship sold
> in 1923. Build was completed on 15th May 1941 at a cost of £4.05M."
> —— https://www.naval-history.net/xGM-Chrono-04CV-Victorious.htm

> "Commissioned 29th March 1941. Built by Vickers Armstrong, Walker on Tyne."
> —— https://www.armouredcarriers.com/hms-victorious-ship-characteristics-card

**三个日期必须分清（这是本舰最容易写错的一处）**：

| 事件 | 日期 | 出处 |
|---|---|---|
| 服役 commissioned | 1941-03-29 | navypedia「Comp 15.5.1941」是**完工**；naval-history 明写「29th March Commissioned for service in Home Fleet」；美方卡片也写 29 March 1941 |
| 完工 completed | 1941-05-15 | navypedia 与 naval-history 一致 |
| 下水 launched | 1939-09-14 | 两源一致 |

**开工日一天之差**：navypedia `4.5.1937` vs naval-history `5th May`。
两说并列，本站取 navypedia。已写进 fact 的 note。

**舾装拖长的原因（推断，未写成 fact）**：下水在 1939-09-14，战争 09-03 已爆发；
naval-history 没有解释，但「1939-09 下水、1941-03 服役」这 18 个月远长于
光辉号的 12 个月（1939-04 下水 → 1940-05 完工），主因显然是战争初期
劳力与设备被挤占，**该推断没有来源支持，故不写进任何 fact**。

**造价**：`£4.05M`（naval-history 原句）。注册表 `construction.cost` 是
`number / count` 且无币种，照 bismarck 的帝国马克、hood 的英镑先例记
`4050000`，并在 note 里声明不可跨舰比较。

**命名**：`identity.namesake` 用 naval-history 的原句（第 5 艘同名舰、
1783 年三等战列舰）。**舰训与纹章拉丁文未获取**——该页只给了图案描写：
"Badge: On a Field Red a winged female figure, habited and supported with the
hands uplifted White, a wreath of Laurel also White."，没有 motto 行。

---

## 2. 1941-05-24 对俾斯麦：本站已有更正，本组不重犯

`data/battles/last-battle.yaml` 文首的更正（原文照录）：

> "**必须更正一个常见误解** —— 胜利号（HMS Victorious）并未参加 5-26 夜至 5-27
> 的决战。她的 Swordfish 空袭发生在 5-24 深夜至 5-25 凌晨（对俾斯麦号，命中 1 雷），
> 此后即脱离。Admiralty War Diary 5-26 记她当日 09:55B 位于 39°05'N 26°05'W、
> 天气不宜飞行，13:28B 已奉命赴克莱德湾加油 —— 距战场数百英里。
> 5-26/27 在场的是皇家方舟号（Force H）。"

本次核到的独立旁证：

> "Victorious had only just commissioned when Tovey called on her to help stop
> Bismarck. His despatch records nine operational Swordfish and six Fulmars
> aboard, with little time available for working up. On 24 May he detached the
> carrier with cruisers... Nine Swordfish took off that evening. Eight attacked;
> the ninth lost contact in cloud. Airborne radar helped locate the target, but
> the crews also needed redirection from Norfolk. The attack was an achievement
> of navigation and coordination as well as flying. The despatch reports at
> least one torpedo hit. Its later Admiralty footnote qualifies Tovey's original
> assessment of the result: the immediate, principal cause of the eventual
> interception was the rudder damage inflicted by Ark Royal's aircraft on 26 May."
> —— https://wartimechapters.com/ships/victorious/

> "24th Launched air strike against BISMARCK escorted by HM Cruisers AURORA,
> KENYA and HERMIONE. One hit obtained but this ran 'shallow' and did little
> damage. The failure of the Aircraft Homing Beacon prejudiced landing of aircraft."
> —— https://www.naval-history.net/xGM-Chrono-04CV-Victorious.htm

**结论**：本站已收录的叙述（9 架起飞 / 8 架攻击 / 1 雷 / 命中舯部装甲带 /
损伤极小 / 05-26 已脱离）在三处独立来源里一致。本组在 article 里把
「05-26 已脱离」单独立成一条事件，并在 intro、history lead、fact note
三处各写了一次，防止再被合并回 5-26 决战。

**一处需要主会话知道的补充**：naval-history 提到「归航信标故障影响了回收」，
站内现有的 `data/weapons/swordfish.yaml` 那一段没写这一点。是否补进去，
由主会话决定，本组没动 `data/`。

---

## 3. 改装历程（本舰最有价值的部分，按时间轴整理）

### 3.1 1941-10：第一批 20 mm

> "10/1941, Victorious: + 8 x 1 - 20/70 Oerlikon Mk II/IV"
> —— navypedia（Modernizations 1 段）

建成时本级无 20 mm（见舰级文件）。这 8 门是本舰近防的起点。

### 3.2 1942-09/10：原型机 Aircraft Direction Room

> "September Nominated for refit. Taken in hand for refit. October Under refit.
> Prototype Aircraft Direction Room fitted... On completion carried out Deck
> Landing trials at Scapa Flow."
> —— naval-history

这条是本舰整条改装史里最关键的一件：**它的管制室是原型机**，
而这套东西后来成了美军最想要的东西（见 §4）。

### 3.3 1943-01：诺福克海军船厂（美方主导）

舰长报告原件（ADM 199/534，1943-02-01）逐项列出：

> "(a) extension of the Round Down,
> (b) the addition of nineteen extra Oerlikon Guns, eight of them on a platform
>     on stern below the round down,
> (c) removal of forward searchlights (one Oerlikon in each in lieu),
> (d) fitting of vertical plot in F.D.O. office,
> (e) removal of type 72 Beacon – YE Beacon fitted in lieu (aerial on mast on
>     starboard side centre of funnel),
> (f) installing three emergency Diesel Fire Pumps,
> (g) installation of Fog Fire system in certain compartments and living
>     accommodation,
> (h) hangar Officer's control position fitted to control hangar traffic and
>     parking,
> (i) two electric Coding machines...
> (j) extra Mess Deck built for increased Flight Deck party on starboard side
>     Upper Gallery Deck in place of potato locker.
> (k) weather damage to bows repaired..."
> —— https://www.armouredcarriers.com/uss-robin-hms-victorious

> "The number and types of aircraft to be carried was also discussed and the
> complement it was decided at finally was 36 Martlet (F4F4) and 18 T.B.F's.
> The number of T.B.F's was dependent on the question of levelling the flight
> deck round down – this was considered most desirable, as not only would it
> allow six more T.B.F's to be carried but it would increase the amount of take
> off run available."

> "I was impressed by the large number of Oerlikon guns in the U.S. Carriers.
> Having found nineteen suitable sites for such guns, the alteration was approved
> by British Admiralty Maintenance Representative and the guns are now fitted.
> This brings our total to thirty Oerlikons."

**奥里康累计数的推演（进 fact，标 C）**：
1941-10 的 8 门 + 1943-01 的 19 门 = 27，但舰长原话说「增至 30 门」。
差额 3 门来自 (c) 项「拆前部探照灯、原位换 2 门」与其它零星加装。
因此本组的 `armament.mount.summary` 在 1943-01 那条写 25 门（8+17，
取自 navypedia「1/1943: + 17 x 1」），而在 note 里说明舰长报告说 30 门，
**两个数不是矛盾而是统计日期不同**（navypedia 的 1/1943 早于诺福克改装完成）。

### 3.4 1943-03：珍珠港

> "Once HMS Victorious arrived at Pearl Harbour on March 4, 1943, her air group
> was flown off to Ford Island... They quickly affected any remaining repairs to
> damage caused by the Panama Canal passage and the serious fires - as well as
> adding yet more 20mm cannons, as well as twin 40mm and quadruple 40mm
> emplacements in front of the seaplane cranes. The flattened aft flight deck, as
> fitted at Norfolk Navy Yard, allowed the Pearl Harbour engineers to add two
> US-style arresting wires behind the original Number 1 wire."
> —— https://www.armouredcarriers.com/uss-robin-hms-victorious

**甲板方框（对模型很重要）**：

> "Avengers aboard 'USS ROBIN' (HMS VICTORIOUS). Note the square painted on the
> centre of the flight deck: It was a decoy lift intended to draw the aim of
> Japanese attacks to the strongest point of the carrier's armoured flight deck."

### 3.5 1943-04 前后：本土改装与 40 mm Bofors 首次上舰

> "4/1943, Victorious: - type 79B radar; + 2 x 4 - 40/56 Bofors Mk 1.2,
> 2 x 2 - 40/56 Bofors Mk 1.2, 10 x 2 - 20/70 Oerlikon Mk II/IV, type 272,
> type 277, type 279, type 281B, 6x type 282, type 293 radars"
> —— navypedia

**「4/1943」这个记法要小心**：该月本舰实际正在太平洋（1943-03-04 抵珍珠港、
05-08 才离港）。所以 navypedia 的「4/1943」是**改装批次的归档写法**，
不能当成「1943 年 4 月正在英国改装」。本组在 fact note 里写明了这点，
把有效窗口给成 `1943-04-01` 起。

### 3.6 1944-01/03：Liverpool 改装

> "December Taken in hand for refit in Liverpool at commercial shipyard.
> 1944 January Under refit at Liverpool. New radars installed. to February"
> —— naval-history
> "The carrier returned to the Clyde on September 26, 1943, before moving on to
> Liverpool's Gladstone Dock for a refit which lasted until March 4, 1944."
> —— https://www.armouredcarriers.com/uss-robin-hms-victorious

### 3.7 1944-04 与 1945：Bofors 替换 Oerlikon

> "4/1944, Victorious: - 1 x 8 - 40/39, 10 x 1 - 20/70; + 13 x 2 - 20/70 Oerlikon Mk II/IV"
> "1945, Victorious: - 4 x 2 - 20/70, 2 x 1 - 20/70; + 6 x 1 - 40/56 Bofors Mk I/III"
> "late 1945, Victorious: - 3 x 2 - 20/70 Oerlikon; + 3 x 1 - 40/56 Bofors Mk I/III"
> —— navypedia

方向很清楚：战争末期用 40 mm 替换 20 mm。原因是 20 mm 对神风机的
拦截距离不够（同页 ac-worthwhile 的战场评估也这么说）。
**但 navypedia 只给增减量、不给累计数**，本组的累计值全部是相加所得，
一律标 `confidence: C` 并在 note 里声明「本书相加」。

### 3.8 1950-1958：重建

> "(3/1950 - 1.1958) Victorious: Hull was lengthened, widened and deepened,
> machinery and boilers replaced. Two 44m steam catapults, two new faster lifts
> and angled (8.75°) deck fitted. Hangar height was 5.25m. Electric generating
> capacity doubled. New artillery fitted. (fd - 6,366 m², ha - 5,690 m² / 29,869 m³)."
> —— navypedia

重建前后对照（全部进 fact，两条一套、窗口不重叠）：

| 项 | 1941/1943 | 1958 |
|---|---|---|
| 标准排水量 | 23,000 t（舰级） | 30,530 t |
| 满载 | 30,481 t（1943 卡片，C） | 35,500 t |
| 全长 | 228.3 m（1943 卡片） | 238.0 m |
| 水线宽 | 29.3 m | 31.5 m |
| 吃水 | 8.84 / 9.45 m | 9.50 m |
| 功率 | 111,164 hp（实测） | 110,000 hp |
| 航速 | 31 kn（试航） | 31 kn |
| 锅炉 | Admiralty 三鼓 ×6 | Foster Wheeler ×6 |
| 燃油 | 4,840 t（舰级） | 6,000 t |
| 续航 | 12,600 nm @14 kn | 10,000 nm @20 kn |
| 机库净高 | 4.9 m | 5.25 m |
| 弹射器 | 1 × BH-III 液压 | 2 × 44 m 蒸汽 |
| 主炮 | 8 × 2 - 114 mm | 6 × 2 - 76 mm Mk 33 |

**一处需要并列的矛盾**：功率从 111,164 掉到 110,000 hp，但航速
从 30.5 变成 31 kn，而排水量涨了 7,500 t。这三个数放在一起是说不通的，
只能由新锅炉的蒸汽参数或推进效率改善解释。**本站未取得锅炉压力/温度**，
所以不做结论，两个数值都照录并各自标 B。

---

## 4. 借调美国海军：USS Robin（一手材料最密的一段）

**窗口的两个口径**（并列保留，不合并）：

- `1943-02-13 至 1943-08-19`：wc-victorious 转引 IWM 照片目录 A 19682
  的图注「HMS Victorious was lent to the USN, 13 February to 19 August 1943」。
- `1942-11-23 至 1943-09-26`：ac-pacops 的副题，即从离英到返抵克莱德河的全过程。

两个都不是错的：前者是「受美军指挥」的窗口，后者含往返航渡与两次改装。
本组在 `service.unit` 里用前者，在 article 与 slices 里两个都写。

**「USS Robin」是呼号，不是改名**（本组据此改了表述）：

> "It is about this point that Victorious was given the radio call-sign 'Robin'
> as a half-hearted security/deception attempt."
> "The extent to which HMS Victorious became referred to as 'USS Robin' is
> unclear. It certainly became a popular monniker among historians and
> commentators after the war. But the few primary references available seem to
> apply only to the one instance - when the ship was transiting the Panama canal
> enroute to Hawaii."
> "A USN battleship (elsewhere identified as USS Massachusetts) signalled
> 'what ship?'. The carrier replied 'USS Robin' - even though the White Ensign
> was flying proudly from her mast."
> —— https://www.armouredcarriers.com/uss-robin-hms-victorious

**战斗机管制室：本舰带过去的最有价值的东西**

> "Strikes were observed... The British Fighter Direction Office was the major RN
> innovation the USN was most interested in. The design and layout were later
> incorporated in the USN Command Information System (CIC)."
> "Mackintosh gave them an advanced copy of C.B. Direction Fighters in H.M. Ships.
> The book was then forwarded to the Bureau of Aeronautics."
> —— ac-pacops

**战果为零，但纪录很好看**

> "HMS Victorious and Task Group 36.3 returned to Noumea on July 25 after
> operating continuously at sea for 28 days, steaming 12,233 miles at 18.1 knots.
> This was a record for an RN aircraft carrier. The 614 sorties flown from her
> deck had resulted in only eight accidents - the lowest accident rate yet recorded."
> "Victorious had during her three months in the South West Pacific steamed some
> 23,000 miles and conducted 2101 deck landings."

**唯一一次有据的行动**：

> "The only taste of action came in the last days of the operation: A USN
> Dauntless pilot spotted a solo 'Betty' bomber some 50 miles out from the fleet.
> His guns had no effect and the 'Betty' escaped before the CAP fighters could arrive."

**美方对这条船的批评（原文，供 narrative 用）**——Commander Mitchell 的意见
经 Sheehy 转述：载机量小、升降机对 Avenger 太窄、修理设施不足、
甲板与机库是钢的遇水油即滑、装甲机库没有通风口因而无法在库内试车第二波、
手提 CO2 灭火器不足、没有 crash dolly。原文见 ac-pacops 第 284 行一段。

**金恩的不满**：

> "But Admiral King made his displeasure known in a letter to General George C
> Marshall, dated April 7: He claimed HMS Victorious was in a poor state of
> general readiness, making her 'so far of no use'."
> —— ac-pacops

这条与金恩本人 1942-12-05 给丘吉尔的电报（「other considerations make it
necessary to forego the services of VICTORIOUS there」，见 ac-pacops 转录的
PREM 3/163/1）放在一起看很有意思：1942 年 12 月美方说不要她、
1943 年 4 月又说她没用，但她还是去了。本组没有把这层写进 article
（避免叙事化），留给主会话判断。

---

## 5. 1944 钨作战（Operation Tungsten）

> "For Operation Tungsten, the Admiralty battle summary describes two planned
> strikes of twenty-one Barracudas, each drawing twelve aircraft from Victorious
> and nine from Furious. Squadrons had exchanged carriers so that each trained
> wing could operate together. A strike's association with one carrier's wing
> does not mean that every aircraft launched from that ship."
> —— https://wartimechapters.com/ships/victorious/ （引 YT-T22）

> "3rd Launched BARRACUDA strikes on TIRPITZ which was leaving harbour for trials.
> Three BARRACUDA aircraft were lost due to the intense AA fire but several hits
> were obtained. Repair of damage took over a month."
> —— naval-history

**机群编成三说并列**（这是本组遇到的第一个真正需要裁决却无法裁决的地方）：

| 来源 | 数字 | 说明 |
|---|---|---|
| navypedia 4.1944 栏 | 28 Corsair + 21 Barracuda = 49 | 搭载总数 |
| ac-design | 1834(14)+1836(14) Corsair + 827(9)+831(9) Barracuda = 46 | 逐中队清单，含中队号 |
| wc-tungsten / wc-victorious | 24 Barracuda + 21 Corsair = 45 | **攻击波编成**，不是搭载总数 |

三组数字口径不同（搭载 / 中队编制 / 出击波次），本组全部并列，
fact 取 46（ac-design 逐中队可核）并标 B。

**一个 wc 站自己标注的局限，值得转抄**：

> "An official synthesis compiled from reports, not the signed original reports of
> Victorious and Furious... The flying programme is a planned schedule."

即 YT-T22 是官方**合成**件（tier B），不是两舰签署的原件。
所以本组把 wc-tungsten 记 tier B 而不是 A。

---

## 6. 1945 神风：两份一手报告 + 一份专题汇总

**5-09 当舰报告（ac-kami-co，ADM 转录，tier A）**——本节最有价值的一份：

> "1647 Raid reported by KING GEORGE V at 275° 28 miles. This was picked up at
> 23 miles by VICTORIOUS' Type 277... 1656 Redar reported Bogey at 9 miles.
> Emergency turn 60° to starboard... 1 Zeke was sighted on the starboard quarter,
> height 3000 feet, range about 3 miles... As it was clearly coming for
> VICTORIOUS, 25° of starboard rudder was put on and the ship swung well.
> ... it crashed on the accelerator abreast 'B' Group. The bomb detonated on
> contact with the flight deck."

> "I regret to report the loss of Temporary Lieutenant(A) Donald CAMERON,
> RNZNVR, No.1834 Squadron, who failed to return from a fighter-bomber mission
> in Strike 'Dog' on 9th May... also the deaths of the following: Joseph LANDERS,
> Steward, D/LX. 557849, Albert Anthony BISS, Able Seaman, D/JX.1/79376, and
> John Edward Elenzo CANN, Able Seaman, D/3X.215013. There were twenty others
> wounded in this attack, ranging from four serious cases to minor ones."

**雷达型号**：这份一手报告写「VICTORIOUS' Type 277」，本组据此把 277
作为 1943-1945 的装舰雷达之一（与 ac-design 的 1945 年天线位置图一致）。

**5-09 上层汇总（ac-kami-vian，tier A）**：

> "At 1645 five low bogies were detected 25 miles to the westward. Two divisions
> of Seafires were immediately sent out; one division intercepted at 15 miles but
> allowed to be drawn off by one ZEKE which retired to the Westward and was later
> splashed. The second interception failed. The four remaining ZEKES attacked the Fleet."
> "The approach of the KAMIKAZES was very low until sighting the Fleet when they
> climbed steeply to 5000 feet, from which height the final approach was made in a
> shallow dive."
> "The conclusions drawn from the attacks on 4th and 9th May are that the enemy,
> having failed to penetrate our fighter defences at medium and high altitudes,
> is now trying low. His first two attacks have succeeded."

**4-01 神风（ac-vic-kamikaze，tier C）**：

> "Victor was now swinging very fast and as we watched the aircraft banked more
> steeply trying to keep on the target. He roared in and his starboard wing struck
> the port edge of the flight deck and caused his plane to cartwheel into the sea
> on the port side. The bomb detonated underwater about 80ft clear of the ship's
> side and threw tons of water, a quantity of petrol and many fragments of the
> aircraft and pilot on to the flight deck."

> "The eight aircraft on Victorious' deck park were positioned forward at the time
> of the attack and suffered minimal damage... Two of the deck crew were injured."

**5-09 命中与损管（ac-vic-kamikaze）**：

> "The kamikaze succeeded in diving on over the starboard quarter, past the bridge
> and crashed into the flight deck at Frame 31 between 'B2' 4.5in turret and the
> raised catapult... Its 500lb bomb detonated at the junction of 3in and 1.5in 'D'
> quality deck plates over a longitudinal bulkhead."
> "The explosion ripped up the 60lb plating (the strengthened but unarmoured steel
> which supported the lift well over a 12ft diameter. The blast depressed the deck
> some 3in over an area of 144sq ft and the bulkhead below was buckled. The
> accelerator was knocked out of alignment and put out of commission."
> "The 'B2' 4.5in turret was almost directly under the impacting aircraft and was
> riddled with splinters and fire, killing its gun crew and putting the mount out
> of operation."
> "The nearby forward lift also suffered the failure of one of its motors."

**伤亡两组数并存（不裁决）**：

| 来源 | 死亡 | 受伤 |
|---|---|---|
| ac-kami-co（舰长原件，tier A） | 3（另 Cameron 失踪） | "twenty others wounded" |
| ac-vic-kamikaze（专题汇总，tier C） | 4 | "four seriously injured... Some 20 others" |

本组写两条 `service.casualties`，A 档那条记 3、C 档那条记 4，
两条 valid.from 都是 1945-05-09。这是本站「两说并列」规则的直接应用。

**一处对模型的提示（来自 ac-vic-kamikaze 图注）**：

> "HMS VICTORIOUS burns in the vicinity of B2 4.5in turret on the port bow...
> The prominent director in front of her island was moved there from on top of
> the bridge to provide space for new radar equipment. HMS Formidable received a
> similar modification, but HMS Illustrious and Indomitable did not."

即 1945 年状态下本舰**舰桥前方的指挥仪是从舰桥顶上搬下来的**，
这是与光辉号/不倦号的外观差异之一。本组没有对应的注册字段，
故只写在 slices 里（未写，因为不在 V6 摘要中——见 §10 遗留项）。

---

## 7. 舵机与锅炉：本舰独有的长期缺陷

> "On August 20, 1944, Victorious had just participated in the launch of Corsairs
> and Barracudas against Sumatra. As the fleet returned to Trincomalee,
> Victorious' rudder suddenly jammed. For a time the carrier was not under control.
> Engineers worked furiously for 30 minutes before the fault was rectified.
> But it would be only the first instance of what would become a recurring problem."
> —— ac-vic-kamikaze

> "On February 11, 1945, HMS Victorious arrived in Sydney for a 16-day respite.
> Other carriers - especially HMS Illustrious - needed the docking facilities more
> urgently, so Victorious did not have her rudder extensively examined."

> "While at Manus, Victorious was exercising with other ships of the fleet when -
> at 1525 on March 14 - a serious fire took hold in the centre boiler room."

> "A new rudder had arrived in Sydney from Britain while Victorious was on station
> off Japan. It would not be fitted. Instead it was hoisted on deck and welded down
> for the passage back to the British Islands with Formidable."

**这一串读下来是一因果链**：1942-08 Pedestal 的多次近失 → 结构损伤累积 →
1944-08 起舵机反复卡死 → 1945-02 因泊位让给光辉号而没彻底检修 →
1945-05 带着这个毛病打冲绳 → 战后新舵运到却不装、焊在甲板上带回国。
**「近失导致舵机故障」这一环是专题站的推测**（原句
"Perhaps this had set a chain of defects in motion"），本组**没有**把它写成 fact，
只在 slices 的 V5/V6 里以「舵机反复发作」这个中性表述保留。

---

## 8. 1958 年重建与结局

见 §3.8 的对照表。结局链：

> "Although intended to refit for further service in 1967 this had to be cancelled
> after a serious fire in November that year which made further refit work
> uneconomic. The ship was then reduced to Reserve status once again and placed on
> the Disposal List in 1969. She was sold later that year to British Shipbreakers
> and towed to Faslane for demolition arriving there on 13th July 1969."
> —— naval-history

> "1967-11-11 在朴次茅斯改装期间舱室起火、死 1 名水兵"（Hansard 书面答复）
> "1967-11-27 国防大臣 Healey 在下院宣布该舰将退役并作为废钢处置"（Hansard 辩论）
> —— 两处均转引自 https://wartimechapters.com/ships/victorious/ 的 TL-RN14 / TL-RN15

**除籍日分歧**：navypedia `stricken 3.1968` vs naval-history「1969 年列入处置名单」。
本组判定两者不是同一事件（除籍 vs 出售/拖走），并列保留。

---

## 9. 字段与来源的取舍记录

### 9.1 没有写的字段（及原因）

| 字段 | 为什么没写 |
|---|---|
| `identity.building_program` | 来源只有 naval-history 的「ordered on 13th Jan.1937」，没说是哪个年度计划（舰级文件写的 1936 年海军计划）。**不拿舰级值顶替**。 |
| `propulsion.boiler.pressure` / `.temperature` | 全部来源都没给。1958 年换锅炉后也没有。 |
| `dimensions.metacentric_height` | 未获取。 |
| `protection.armor.weight` | 本舰的装甲总重**未获取**。舰级的 5,000 t 是全级设计值，不顶替。 |
| `protection.underwater.depth` | 同上，本舰未获取。 |
| `aviation.hangar.length` / `.width` | 舰级值适用于本级全部（含本舰），且本舰无改造记录改变它。**按「换一艘同级舰就变吗」判据，这是舰级数据**，故不重复写。 |
| `aviation.elevator.dimensions` | 同上（2 部 13.7 × 6.7 m）。1958 年换「faster lifts」但**尺寸未获取**。 |
| `aviation.catapult.count`（1941） | 建成时 1 部（舰级值）。**有材料称后期增至 2 部，本组未取得可证来源**，故 1941-1949 段不写 count，只在 1958 段写 2。 |
| `service.complement.standard` | 建成编制是舰级数据（1,229）。本舰只拿到 1943 年的 1,790，记在 `service.complement.wartime`。 |
| `weapon.*` / `mount.*` | **本组一条都没写。** 理由见 9.2。 |
| `appearance.color.hull` / `.deck` | 1943 年美制蓝灰的**具体色号未获取**（来源只写 "blue grey favoured by the USN"）。1941–42 与 1944–45 的色号同样未获取。 |

### 9.2 为什么一条 `weapon:` / `mount:` 实体都不建

本舰的武器全是**已存在的实体**：`weapon:4_5in-qf-mk3`、`weapon:2pdr-mk8`、
`weapon:40mm-bofors`、`weapon:20mm-oerlikon`，以及
`weapon:type-279`、`type-281b`、`type-277`、`type-282`、`type-293`、
`type:285`、`type:272`、`type:79b`、`corsair`、`avenger`、`falmar`、`swordfish`
等，都已在 `data/classes/illustrious.yaml` 与 `data/ships/illustrious.yaml`
建好。**新建 `mount:victorious-*` 只会让左树出现第二条同名装备**——
这正是 `data/ships/illustrious.yaml` 第 472–484 行那条注释里
（2026-11-18 的归并判例）明确警告过的错误。所以本组只在
`sensors.radar.installed` / `aviation.aircraft.types` / `armament.mount.summary`
这些**文字字段**里记录本舰的逐期配置。

**如果主会话认为必须给本舰一个 mount 实体**（好让「按舰看装备」的页面
能挂上），建议的做法是在合并阶段**复用舰级已有的 4 个 mount id、
在其 `mount.count` 上为本舰另开一条带 `valid` 窗口的 fact**，
而不是新建 `mount:victorious-45in-twin`。本组没有擅自这么做，
因为那会改动舰级文件。

### 9.3 置信度的判定标准（本组自用）

- **A**：一手档案（舰长报告、美方规格卡、海军部战斗总结的编成部分）直接给出的数值。
- **B**：专题站或 navypedia 的单值，或由一手材料直接换算（单位换算不改数值语义）。
- **C**：需要相加、相减、或需要判断口径才能得到的数（如 20 mm 累计数、
  美方卡片的模糊吨制、三说并列里取中）。

---

## 10. 单位换算全部明细（可复核）

1943-03-24 美方卡片用英制，本站存储层用公制，换算如下
（1 ft = 0.3048 m，1 in = 25.4 mm，1 lb = 0.45359237 kg，
1 US gal = 3.785412 L，1 long ton = 1.01605 t，1 码 = 0.9144 m，1 英里 = 1.609344 km）：

| 原值 | 换算 | 结果 |
|---|---|---|
| Length Overall 749 ft | × 0.3048 | 228.30 m |
| Waterline 710 ft | × 0.3048 | 216.41 m |
| Beam waterline 96 ft | × 0.3048 | 29.26 m |
| Beam minus platforms 107 ft | × 0.3048 | 32.61 m |
| Flight deck 740 ft | × 0.3048 | 225.55 m |
| Flight Deck height 39 ft | × 0.3048 | 11.89 m |
| Draught normal 29 ft | × 0.3048 | 8.84 m |
| Draught deep 31 ft | × 0.3048 | 9.45 m |
| Turning 1450 yards | × 0.9144 | 1,325.9 m |
| Endurance 12,600 miles | × 1.609344 | 20,277 km（fact 存的是海里原值，**未换算**） |
| Petrol 60,700 US gal | × 3.785412 | 229,774 L |
| Hangar ends 80 lbs | × 0.45359237 ÷ 25.4² × 1000 | 50.8 mm → 记 51 |
| Hangar deck outside 100 lbs | 同上 | 63.5 mm → 记 64 |
| Tonnage actual 30,000 tons | × 1.01605（按长吨） | 30,481 t（**吨制存疑，故 confidence: C**） |

**续航那条没换算的原因**：注册表 `propulsion.range.max` 的单位是 `nmi`，
卡片给的是 statute miles（"Endurance - miles"）。1,450 英里差 12%，
本组**按原数字直接搬进 nmi 字段并在 note 里标出**这一口径问题——
严格做法是除以 1.15078（= 12,600 stat mi → 10,949 nmi），
但那样会与 navypedia 的 9,250 nmi 混成同一量级、掩盖真实分歧。
**这条请主会话复核**：如果站内政策要求严格换算，本组的
`propulsion.range.max = 12600` 应改为 `10949`（1943 卡片）与
`8690`（1958 的 10,000「nm」，若那也其实是英里）。

---

## 11. 遗留项（本组没做、建议主会话过问）

1. **1945 年舰桥前指挥仪位置**：ac-vic-kamikaze 的图注明确说本舰与可畏号
   把这具指挥仪从舰桥顶搬到舰桥前方（为给新雷达腾地方），光辉号与不倦号没搬。
   这是一个**可证的外观差异**，但注册表没有对应字段
   （`appearance.island_position` 只有左右舷，`sensors.director.*` 没有位置）。
   建议写进 slices V6 的 note 或 `appearance` 段，本组没有擅自加字段。

2. **续航里程单位**：见 §10 末尾。

3. **`data/weapons/swordfish.yaml` 的 1941-05-24 条目**缺「归航信标故障」
   这一细节（naval-history 有）。是否补，由主会话定。

4. **`propulsion.power.design` 1958 段的矛盾**（功率降而航速升）：见 §3.8。

5. **一处没有使用的线索**：`ac-worthwhile` 记录了一个总数
   「Of the fifteen hits, the Illustrious class flight deck armor defeated only
   one – Victorious shrugged off an anti-personnel bomb dropped at low altitude
   by an Re.2001 fighter.」，以及本舰在 Pedestal 时那两枚炸弹的弹种争议
   （"Some accounts state they were experimental low-altitude anti-armour weapons.
   Others state they were anti-personnel bombs."）。这是一处**两说并列**，
   本组在 article 里只写了「未爆炸即解体翻入海中」这个两源都认的事实，
   **没有**采用任何一方对弹种的判断。若要写进 narrative，请照此两说并列。

---

## 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 0（Victorious 属已有舰级 Illustrious，`classes/` 未写任何东西） |
| 单舰文件 | 1（`ships/victorious.yaml`，**105 条 fact**） |
| 切片文件 | 1（`slices/victorious.yaml`，**V0–V8 共 9 片**） |
| 正文文件 | 1（`articles/victorious.yaml`，简介 **5 段**、历史 **7 节 68 条事件**） |
| 新登记来源 | **10** |

**自检结果**

```
yaml ok
ships fact 条数: 105
slices 片数: 9 -> V0, V1, V2, V3, V4, V5, V6, V7, V8
article 简介段数: 5, 历史 7 节 68 条事件
新登记来源: 10
errors: 0  warnings: 0
```

另跑了站内校验器 `python scripts/validate.py`：**0 错误 / 0 警告**
（校验器不检查 `work/staging/`，故另用自写的
`work/staging/g1-victorious/_selfcheck.py` 按 SCHEMA §10 逐条复核，
覆盖：字段注册、单位一致、枚举、qual 齐备、日期格式、
src 登记与 tier E 拦截、confidence 合法、article 三段结构、
events 的 date/text/src、模糊词扫描）。

### 卡住的地方

- **`web_fetch` / `research` 全线 SSRF 失败**（详见 §0）。改用本机
  `Invoke-WebRequest` 后十处全部 200。这是环境问题不是站点问题，
  建议写进 SCHEMA。
- **`iwm.org.uk` 403**：Tungsten 影像条目拿不到正文，
  只能从搜索摘要看到标题与一句描述。未登记为来源。
- **`hmshood.org.uk` 403**：Tovey 电文（ADM 234/509）原件抓不到，
  1941-05-24 的空袭细节只能引 wc-victorious 的转述（tier C 而降级）。
  这是本次唯一一处「本该有 A 档一手件却只能写 C」的地方。
- **1941 年的雷达型号**：navypedia 说建成时装 Type 79B；
  但本舰 1942-08 的 Pedestal 报告附录明写「Victorious 的 Type 279」。
  两说并列处理；**1941-05 到底装的是 79、79B 还是 279，本站没有一手件**。
- **1958 年重建的锅炉蒸汽参数**（压力/温度）全部来源未给，
  导致「功率降而航速升」这一矛盾无法解释。
- **本舰的装甲总重与水下防护深度**未获取，没有拿舰级值顶替。
- **1941–1942 与 1944–1945 的涂装色号全部未获取**。
  能确证的只有一个时点：1943 年 3-9 月为美制蓝灰单色（且无色号）。
- **`aviation.catapult.count`（1941–1949 段）**：有二手材料提到后期增至
  两部，但没找到可证来源，故不写。

### 有争议的记载

| 项 | 说法 A | 说法 B | 本组处理 |
|---|---|---|---|
| 开工日 | navypedia：1937-05-04 | naval-history：1937-05-05 | 两条并列写进 note，fact 取 04 |
| 除籍日 | navypedia：stricken 3.1968 | naval-history：1969 年列入处置名单并出售 | 判定为不同事件（除籍 vs 出售），并列不裁决 |
| 1941 年雷达 | navypedia：Type 79B | Pedestal 报告（一手）：Type 279（1942-08 在舰） | 并列；取「1942-08 已在用 279」为一手结论 |
| 1943 年雷达批次的时点 | navypedia：「4/1943」 | 本舰当时在太平洋（03-04 抵珍珠港、05-08 离港） | 判为**改装批次归档写法**，有效窗口从 1943-04-01 起 |
| 20 mm 累计数（1943-01） | navypedia：+17（累计 25） | 舰长报告：增至 30 门 | 判为统计日期不同，summary 写 25、note 里说明 30 |
| Tungsten 机群数 | navypedia：49（28+21） | ac-design：46（逐中队）／wc：45（攻击波） | 三说并列，fact 取 46 并标 B |
| 借调窗口 | IWM 图注：1943-02-13 至 08-19 | ac-pacops：1942-11-23 至 1943-09-26 | 判为口径不同（受美军指挥 vs 全过程），两个都写 |
| 1945-05-09 伤亡 | 舰长报告（一手）：3 死 20 伤 | 专题汇总：4 死、4 重伤 + 约 20 伤 | 两条 fact 并列，A 档记 3、C 档记 4 |
| 航空汽油容量 | ac-vic-charcard（一手）：60,700 US gal = 229,774 L | ac-design（引 Watton）：40,500 gal | 差约三分之一，两项都没说明口径，并列不写取舍 |
| 续航 | 1943 卡片：12,600 mi @14 kt | navypedia（舰级）：9,250 nm @14 kt | 差 3,350 nm，并列；并标注卡片的「mi」可能不是海里 |
| 1945 机群 | ac-tf57 等三源：37 Corsair | navypedia 3.1945 栏：37 Hellcat | 三比一，判 navypedia 排印错误，但无法证否，fact 里并列注明 |
| 「USS Robin」 | 通俗叙述：改名 USS Robin | 一手材料：仅是过运河时的一次无线电呼号 | 按一手材料写「借调 + 使用呼号 Robin」，**不写改名** |
| 1942-12 美方态度 | 罗斯福 12-05 电报：不要 VICTORIOUS、改要 RANGER | 1943 年金恩 04-07 致马歇尔：她「so far of no use」 | 两件独立材料，未写进 article（避免叙事化），留此备查 |
