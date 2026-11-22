# 调研底稿 —— 郡级（County class）· HMS Norfolk（78）/ HMS Dorsetshire（40）

> g3-county 组 · 2026-11-22
> 产出目录：`work/staging/g3-county/`
> 本文件按 SCHEMA §9 的规矩写：每一条结论带**英文原句 + URL**。

---

## 0. 本轮取证环境的特殊说明（合并时必读）

**`web_fetch` 工具对本轮所有主要站点全部返回 SSRF 拦截**，原因是域名解析到了私有地址段（198.18.x.x）：

| 站点 | web_fetch 结果 |
|---|---|
| `www.navypedia.org` | SSRF blocked: resolves to private address 198.18.0.98 |
| `www.naval-history.net` | SSRF blocked: 198.18.0.99 |
| `uboat.net` | SSRF blocked: 198.18.0.101 |
| `en.wikipedia.org` | SSRF blocked: 198.18.0.18 |
| `www.navweaps.com` | SSRF blocked: 198.18.0.50 |
| `ww2db.com` | SSRF blocked: 198.18.0.102 |
| `kbismarck.com` | SSRF blocked: 198.18.0.106 |
| `www.battleships-cruisers.co.uk` | SSRF blocked: 198.18.0.105 |
| `navyhistory.au` / `sahistory.org.za` | SSRF blocked: 198.18.0.104 / .107 |

**改用 PowerShell `Invoke-WebRequest` 直连后才取到正文。** 所以 `sources-fragment.yaml` 里
`access` 记的是 `direct`（确实抓到了正文），但这一轮的"直连"是本机 shell 直连，
**不是工具代理**。取证路径与其它组不同，主会话合并时请注意。

另有一处必须报告的 **URL 错误**：SCHEMA §9 与主会话任务书给的
`https://www.naval-history.net/xGM-Chrono-10CA-HMS_Norfolk.htm` 是 **404**。
实际可用路径是 `06CA` 系列：

- 正确：`https://www.naval-history.net/xGM-Chrono-06CA-Norfolk.htm`（注意没有 `HMS_` 前缀）
- 正确：`https://www.naval-history.net/xGM-Chrono-06CA-Dorsetshire.htm`
- 对照：Nelson 级用的是 `01BB-HMS_Rodney.htm`（有 `HMS_`），驱逐舰用 `15Fr-Loch-HMSAS_xxx`，
  **编号段与前缀都随舰种变化，不能按同一模板套**。

---

## 1. 舰级定位：County 有三个子级，本站只建 Norfolk 子级

> "The 13 Counties were built in the Kent, London and Norfolk sub-classes. They were the only
> 10,000-ton 8-inch gun, or 'A', cruisers that the Royal Navy built."
> — https://en.wikipedia.org/wiki/County-class_cruiser

> "The final pair of Counties – Norfolk and Dorsetshire – formed the Norfolk class."
> — 同上

> "Cornwall and Dorsetshire were respectively the second and the last of 13 heavy cruisers
> completed between 1927 and 1930 for the RN and RAN. ... the final two were the Norfolks –
> Norfolk itself and Dorsetshire."
> — https://www.combinedfleet.com/CornwallDorsetshireX-RStuart-Adobe.pdf （Robert Stuart, 2019）

**结论**：`classes/county.yaml` 的 `name` 写成「郡级重巡洋舰（Norfolk 子级）」，
`class_of: [norfolk, dorsetshire]`，并在文件头与 `identity.name_original` 的 note 里把三个子级写清。
Kent / London 两个子级不入库。

**没建成的三艘**（navypedia 与维基一致，写进 `identity.building_program` 的 note）：

> "Another two ships that had been deferred from the 1927–1928 and 1928–1929 programmes – to have
> been named Northumberland and Surrey – were ordered on 15 May 1929, but suspended on 23 August
> and finally cancelled on 14 January 1930. A proposed fifth vessel of the sub-class was also
> cancelled."
> — https://en.wikipedia.org/wiki/County-class_cruiser

---

## 2. 主尺度 / 排水量 / 动力

> "Displacement standard, t 9925 - 9975 (Norfolk finally about 10900)
> Displacement full, t 13425 (Norfolk finally 14600)
> Length, m 181.4 pp 192.9 - 193.7 oa
> Breadth, m 20.1
> Draught, m 6.37 deep load (Norfolk finally 6.91)
> No of shafts 4
> Machinery 4 sets Parsons geared steam turbines, 8 Admiralty 3-drum boilers
> Power, h. p. 80000
> Max speed, kts 32.3
> Fuel, t oil 3210 (later 3005)
> Endurance, nm(kts) 12500(12)
> Complement 710"
> — https://www.navypedia.org/ships/uk/brit_cr_norfolk.htm

**口径陷阱 1：长度区间 192.9–193.7 的上沿对不上本级两舰。**
维基两舰条目给 Norfolk 192.81 m（632 ft 7 in）、Dorsetshire 192.86 m（632 ft 9 in），
都在下沿附近。193.7 m 是 **Kent 子级**（Cornwall/Cumberland 等）的 oa 值，
疑为 navypedia 在同级页里混入了别子级的数。舰级文件取区间下沿 192.9 m。

**口径陷阱 2：装甲表与正文自相矛盾。**
navypedia 装甲行的 `belt: 25` 是防破片板，不是主装甲带；
同页"Protection"段自己写得更细：

> "Magazines were protected by 111 (102mm armour on 9mm plating) - 25mm sides and 76 - 25mm
> platform deck. Machinery was protected by 25mm bulkheads and 32mm deck. Steering gear had
> 38 - 25mm horizontal protection."

**口径陷阱 3：Dorsetshire 的排水量三源不一。**

| 来源 | 标准排水量 | 备注 |
|---|---|---|
| combinedfleet 表 1（建成时） | 9,830? | 原文带问号，作者存疑 |
| combinedfleet 正文 + 表 2（1937 改装后） | 10,400 | 「an estimated 10,400 tons」 |
| 英文维基 Dorsetshire 条目 | 10,035 lt = 10,196 t | tier E |
| navypedia | 9,925–9,975 区间 | 两舰共用，不分改装前后 |

处理方式：舰级文件记 9,925 t + note 里列出三说；单舰文件记 **10,400 t**（1937 年改装后，
tier C 明确支撑、载况清楚），并在 note 里把另外三说明白。锚点句：

> "After this refit Dorsetshire's standard displacement was an estimated 10,400 tons and its full
> load displacement 13,775 tons."
> — https://www.combinedfleet.com/CornwallDorsetshireX-RStuart-Adobe.pdf

**航速为何三说**：navypedia 32.3、combinedfleet 32.25、维基 Norfolk 32.25 但 Dorsetshire 条目
正文写 32.3、信息框写 31.5。31.5 是 Kent 子级的设计值（combinedfleet 表 1 明确：
Kent「Designed max speed 31.5」），疑为跨子级串值。取 32.3，三说并列写进 note。

**为什么设计航速只有 31.5–32.3 而不是想要的 33 节**（写进 `propulsion.power.design` 的 note）：

> "Forced to compromise to stay within the 10,000 ton limit but unwilling to sacrifice armament or
> range, for the Kent class the Admiralty accepted a designed maximum speed of 31.5 knots at
> standard displacement, rather than the desired 33 knots, so that 400 tons could be saved by
> fitting 80,000 shaft horsepower (shp) machinery instead of a 100,000shp plant."
> — https://www.combinedfleet.com/CornwallDorsetshireX-RStuart-Adobe.pdf

**没有拿到的**：试航实测功率、试航实测航速、螺旋桨直径、舵面积、舱段划分、型深、
方形系数、水线面积、干舷、蒸汽温度、发电机台数/功率、造价。全部**不写 fact**。
`propulsion.propeller.count` 是由"4 轴"推得，已标 confidence B 并在 note 里说明是推导。

---

## 3. 装甲：本级的关键数字与一处必须纠正的说法

**装甲构造（tier C，写进 `protection.scheme` 与各 `armor.thickness` 的 note）**：

> "It highlights in particular that the British designs had 400 to 500 tons less armour than the
> ships of their two future enemies. In the context of their sinking by 250 kg bombs, it is
> significant that horizontal armour, some of it rather thin, was provided only over the magazines
> and shell rooms (from 1 to 3 inches), the machinery spaces (1⅜ inches), and the steering gear
> (1½ inches). The thickest armour was on the sides of the main and secondary magazines (4⅜ and
> 3⅜ inches, respectively)."
> — https://www.combinedfleet.com/CornwallDorsetshireX-RStuart-Adobe.pdf

表 1 给的装甲重量：**Dorsetshire 1,060 吨**（Cornwall 992 吨）。
（**没写进 fact**：`protection.armor.weight` 只有这一处给 Dorsetshire 的值，
Norfolk 完全没有；为避免"只给一舰装甲总重"造成对比器误导，两舰都没写这条，
只在本文档留档。）

**必须纠正的维基说法**：英文维基 Norfolk 条目称本级"before the war"加装过 3.5 英寸（89 mm）装甲带：

> "As built there was no belt armour, but a 3.5 in (89 mm) belt was added before the war."
> — https://en.wikipedia.org/wiki/HMS_Norfolk_(78)

**这条站不住**，有三条反证：

1. combinedfleet 逐条列了 Dorsetshire 1937 年那轮改装，最后一条明写 **"No additional armour was fitted."**
2. 维基自己的 County 级条目说加带只针对 Kent 子级五舰（Berwick / Cumberland / Suffolk / Kent /
   Cornwall），London 只有 London 自己在 1938 年加 —— **Norfolk 子级不在名单内**。
3. navypedia 的装甲行从建成到 1944 年都没出现过 89 mm 这一档。

**处理**：`protection.armor.thickness` 的 belt 记 25 mm，note 里把 89 mm 一说完整写出并说明为何不采。
**没有把它写成 89 mm**，也没有删掉这条争议。

---

## 4. 主炮：8"/50 (20.3 cm) Mark VIII + Mk II 炮塔

全部来自 `navweaps-8in-50-mk8`（已登记，直接引用）
— https://www.navweaps.com/Weapons/WNBR_8-50_mk8.php

关键原句：

> "Designation 8"/50 (20.3 cm) Mark VIII / Date Of Design 1923 / Date In Service 1927
> Gun Weight Mark VIII and VIII*: 38,528 lbs. (17,476 kg) / Mark VIII**: 38,640 lbs. (17,527 kg)
> Gun Length oa 413.1 in (10.493 m) / Bore Length 400.0 in (10.160 m) /
> Rifling Length 346.3 in (8.796 m)
> Chamber Volume 3,646 in 3 (59.75 dm 3 )
> Projectile Types and Weights SAPC Mark Ib - 256 lbs. (116.1 kg) / HE Mark IIIb - 255 lbs. (115.7 kg)
> Propellant Charge 66.0 lbs. (29.94 kg) SC 205
> Muzzle Velocity 2,805 fps (855 mps)
> Approximate Barrel Life 550 rounds
> Magazine capacity per gun Kent class - 130 / London class - 150 / Dorsetshire class - 150 /
> York class - 172.5"

**三个必须注意的坑（都写进 fact 的 note 了）**：

1. **初速降过级**：
   > "The original muzzle velocity was 2,900 fps (884 mps) with a 72.25 lbs. (32.77 kg) SC charge,
   > but this was derated to the figure given above in order to reduce dispersion and increase
   > liner life."
   任何用 884 m/s 推算射程或穿深的做法都是错的。

2. **射程表的初速又是另一个数**：射程表头写 `MV = 2,725 fps (831 mps)`，
   最大射程 30,650 码（28,030 m）@45°。与 855 差 24 m/s，不能混用。

3. **射速**：理论 3–6、实战 3–4。
   > "'British Cruisers of World War Two' states that this rate was never reached during wartime
   > service and that the maximum sustained ROF in action was actually 3 to 4 rounds per minute."
   参谋部最初要 12 发/分（"an impossibly high figure for the time"），后降到 6 发；
   试航中 HMS Kent 短时达到 5 发/分。fact 存 4（实战上限），confidence B。

**炮塔为什么是 Mk II —— 这是 Norfolk 子级与另外两个子级的分界**：

> "Kent (4) and Australia (4) : Mark I / London (4): Mark I* / Norfolk (4) and York (3): Mark II /
> Exeter (3): Mark II*
> Weight ... Original Estimate Mark I: 155 tons / Mark I*: 159.5 tons / Mark II: 168.8 tons
> As Completed Mark I: 205 tons / Mark I*: 210 tons / Mark II: 220.3 tons"

配上 navweaps 自己的评语：

> "It was originally hoped that the Mark II mounting would be much lighter than the Mark I, but the
> reverse turned out to be the case."
> 以及脚注："These were Treaty-limited warships, these overruns for the main armament had to be
> compensated for by taking weight out of other areas, such as reducing the number of hull
> scantlings."

→ **本想减重，结果比 Mk I 更重的 15 吨，只能在舰体结构上继续抠。** 这是本级设计困局的硬证据。

**70° 仰角的无用性**（`weapon.category` 的 note）：

> "the mountings for these weapons were given a high maximum elevation in order to provide an
> anti-aircraft capability. However, the training and elevation gear was inefficient and both the
> elevation and training rates were too slow to allow these mountings to be useful in that role."

→ 所以 `weapon.category` 记 `naval_gun`，不记 `anti_aircraft_gun`。

**炮位命名 A/B/X/Y 的依据**：navweaps 与维基都以 "X" 指第三座（后部第一座）：

> "although the right gun in 'X' turret only fired eight rounds (compared to 103 rounds from the
> right gun in 'B' turret)" — navweaps
> "the third ('X') twin 8 inch turret was landed in 1944" — https://en.wikipedia.org/wiki/HMS_Norfolk_(78)

A/B/Y 无直接来源，是 RN 惯例推论，故那三条 `mount.label_name` 给 confidence C（X 给 B）。

---

## 5. Norfolk：建造、战历、结局

**建造（三源一致）**

> "HMS Norfolk ... Builder Fairfield Shipbuilding & Engineering Co. Ltd, Govan / Laid down 8 July
> 1927 / Launched 12 December 1928 / Commissioned 30 April 1930 / Pennant number: 78"
> — https://en.wikipedia.org/wiki/HMS_Norfolk_(78)

> "DORSETSHIRE-Class cruiser built by Fairfield shipyard at Govan, Glasgow and launched on 12th
> December 1928. The completion date was 1st May 1930."
> — https://www.naval-history.net/xGM-Chrono-06CA-Norfolk.htm

navypedia 的 Comp 栏写 30.4.1930，另给船台号 628（Yard No 628）、1948 年改舷号 C78。
**完工日 4/30 vs 5/1 一天之差，两说并列，fact 取 4-30。**

**1940-03-16 斯卡帕湾空袭**

> "After return to Scapa Flow came under air attack and hit on port side of quarterdeck abreast Y
> turret. Sustained damaged by bomb which exploded in Shell Room."
> — naval-history（如上）

> "Norfolk was struck by a 250 kg bomb from a Junkers Ju 88 at 19:59, which hit the quarterdeck
> near the Y turret, passed through the upper, main and lower decks, and exploded near the Y shell
> room, blowing a hole in the starboard side below the waterline and flooding the X and Y
> magazines. Four crewmen were killed and six wounded."
> — https://en.wikipedia.org/wiki/HMS_Norfolk_(78)

**左右舷打架（port vs starboard）**，两说并列写进 note。
**伤亡 4 死 6 伤只见于维基（tier E），按红线不入库** —— 已在 ships 文件里留了说明块。

**1941-05-27：527 发（两个独立来源吻合，confidence A）**

> "The Mark II was also successful in the battle with Bismarck in May 1941. During this battle, HMS
> Norfolk in about 90 minutes fired 527 rounds with minor problems, although the right gun in 'X'
> turret only fired eight rounds (compared to 103 rounds from the right gun of 'B' turret), probably
> because of double ramming of the cordite charges. Her Commander, Capt. A.J.L. Phillips reported:
> 'For 8in Mark II mountings, the final state of affairs and the percentage output are considered
> most satisfactory.'"
> — navweaps

> "380 of 40.6 cm from Rodney / 339 of 35.6 cm from King George V / 527 of 20.3 cm from Norfolk /
> 254 of 20.3 cm from Dorsetshire / 716 of 15.2 cm from Rodney / 660 of 13.3 cm from King George V"
> — https://kbismarck.com（本机已存 `work/raw/lb-lb.txt`）

**X 塔故障只给 B**：navweaps 原文带 "probably"，且是转述舰长战报而非战报原件
（原件 ADM 234/509 部分已由 hmshood.org.uk 转录，但该站本轮 403 拒抓，见 §9）。

**flank marking 的一手依据（Tovey 战报）**：

> "At 0735, when the enemy bore 120°, 21 miles, course was altered to 080° to close ... 'Norfolk' was
> shadowing from the north-westward, prepared to carry out flank marking for the battleships; and
> at 0820 she came in sight and provided a visual link."
> "At 0948 'Norfolk' had stopped flank marking and had joined in the action."
> — hmshood-tovey-dispatch（已登记）

**注意时间口径**：navweaps／维基记 0854 加入射击，Tovey 记 0948 停止 flank marking 转入射击。
**两者不是同一事件**（前者第一轮开火、后者角色转换），不能合并成一个时间点。已写进 note。

**1943-12-26 北角海战**

> "26th Engaged German battleship SCHARNHORST after radar contact by HM Cruiser SHEFFIELD ...
> Twice hit by enemy fire which damaged X turret and radar equipment. Seven of ships company were
> killed and five wounded."
> — naval-history（如上）

维基记 6 人阵亡。**fact 取 7（有 tier D 支撑），6 写进 note**。

**1944-11 大改装**

> "11/1944, Norfolk : - 1 x 2 - 203/50 ('X'), 2 x 8 - 40/39, 2 x 1 - 20/70, type 273, type 281,
> type 284, type 286M radars; + 6 x 4 - 40/39 2pdr QF Mk VIII, 11 x 2 - 20/70 Oerlikon Mk II/IV,
> type 274, type 277, type 282, type 283, type 293 radars; displacement was 10900/14600t"
> — navypedia

> "An extra superstructure was added aft to carry barrage directors, fitted with radar Type 283,
> which finally allowed the main armament to serve in its intended anti-aircraft role."
> — https://en.wikipedia.org/wiki/County-class_cruiser（Norfolk 子级节）

**结局**

> "She was Paid-off into Reserve before laying-up at Falmouth. Placed on the Disposal List and this
> cruiser was sold to BISCO on 3rd January 1950 for demolition by Cashmore at Newport, South Wales.
> The ship arrived at the breaker's yard in tow on 19 February that year."
> — naval-history

---

## 6. Dorsetshire：建造、战历、沉没

**建造**

> "30.9.1930" 完工、"21.9.1927" 开工、"29.1.1929" 下水、Yard: Portsmouth DYd、舷号 40
> — navypedia

> "ordered from HM Dockyard Portsmouth in the 1927-8 Estimates and laid down in September 1927.
> She was launched on 29th January 1929 as the 3rd RN ship to bear this name ... Build completion
> date was 30th September 1929."
> — https://www.naval-history.net/xGM-Chrono-06CA-Dorsetshire.htm

**三处日期问题，都已在 fact 的 note 里写明**：

1. naval-history 的完工年写 1929，与它自己的下水年（1929）和另两源（1930）都对不上 → **判笔误**。
2. 英文维基 County 级舰表写下**水日 24 Jan 1929**，而它自己的 Dorsetshire 条目与 naval-history
   都写 29 Jan 1929 → 同一站内自相矛盾，取 29 日。
3. uboat.net 建造厂栏把 Portsmouth Dockyard 与 Cammell Laird (Birkenhead) 并列 →
   取 Portsmouth（另三源一致）。

**1940：不是挪威，是南大西洋与达喀尔**

> "From Freetown ... to watch French battleship RICHELIEU ... On 25 June, she set out from Freetown to
> watch the French battleship Richelieu, which left Dakar for Casablanca two days later."
> — https://en.wikipedia.org/wiki/HMS_Dorsetshire_(40)（tier E，仅作线索）

tier C/D 的确证：

> "Vom 18.-23.6. wird das noch unfertige Schlachtschiff Richelieu (Cpt. Marzin) in Begleitung der
> Zerstörer Fougueux und Frondeur von Brest nach Dakar verlegt. ... Richelieu erreicht Dakar am 23.6.,
> am gleichen Tag lief Kreuzer Dorsetshire von Freetown aus und trifft vor Dakar mit dem
> Flugzeugträger Hermes zusammen."
> — https://www.historisches-marinearchiv.de/projekte/rohwer_chronik/40-06.htm

> "In Dakar erhalten die U-Boote Le Héros und Le Glorieux den Befehl zum Auslaufen und Angriff auf den
> brit. Kreuzer Dorsetshire, dieser kann den Booten mit Manövern bei hoher Geschwindigkeit ausweichen,
> darauf hin werden die U-Boote zurückgerufen."
> — https://www.historisches-marinearchiv.de/projekte/rohwer_chronik/40-07.htm

**1941-05-27：最后雷击**

> "10:22 多塞特郡号自 3,000 m 向右舷发射 2 枚 21 英寸 Mark VII 鱼雷，均命中，但「几乎没有使她震动」。
> 英方一手审讯记该舰 'having hit with three torpedoes'（合计 3 雷）"
> — data/battles/last-battle.yaml（已入库，本组保持一致）

combinedfleet 的时间是 **10:25**（差 3 分钟，并列不裁）：

> "Just over an hour later Dorsetshire delivered the coup de grâce, firing two torpedoes into
> Bismarck's starboard side at 1025 and a third into her port side at 1036. Bismarck sank four
> minutes later. After Dorsetshire and the destroyer Maori picked up 110 survivors they left the
> scene as a U-boat was suspected to be in the area."
> — https://www.combinedfleet.com/CornwallDorsetshireX-RStuart-Adobe.pdf

**1941-12-01 Python —— 必须与 Atlantis 分开**

> "Her patrolling bore fruit on 1 December, when she intercepted the German supply ship Python, which
> was in the process of transferring supplies and fuel to two U-boats, U-68 and U-A. Python, carrying
> some 300 survivors from the raider Atlantis (sunk by county class cruiser Devonshire on 22 November),
> was scuttled by her own crew. U-A fired a total of five torpedoes at Dorsetshire. None hit, but the
> presence of the submarines forced Dorsetshire to depart without rescuing anyone from Python."
> — 同上（这一句信息量最大，把两件事的关系讲得最清）

**1942-04-05 沉没：逐条命中位置有一手战报口径**

> "At about 1340 [more likely 1338], 5th April, three aircraft were sighted by the Dorsetshire
> overhead at a high altitude; assuming them to be hostile, she opened fire immediately ... One
> through the quarterdeck, disabling the steering gear, the second through the catapult, disabling
> both wireless offices, and the third port side amidships, putting out of action all the port A/A
> armament, except the pom-pom. ... Hits were received through the base of the foremost funnel,
> putting out of action S1-H/A group [the forward starboard high angle guns] and 'A' boiler room; on
> the quarterdeck, disabling 'X' turret, and at the base of the after funnel, bringing it down and at
> the same time blowing up the H.A. magazine. This bomb also put both pom-poms out of action.
> Four minutes ['five minutes', according to Agar's first report] after the initial attack the ship
> took a definite list to port ... At least four more hits were received (making a total of 10) in
> addition to several near misses"
> — 引自 1943 年海军部《Naval Operations off Ceylon, 29th March to 10th April, 1942》，
> 由 combinedfleet 专题文转录，同上 URL

> "HMS Dorsetshire ... was sunk in position 01º54'N, 77º45'E in about 8 minutes by 10 hits from
> 250 - 550 pound bombs, and several near misses. The HA magazine exploded, which doubtless counted
> in part for her rapid sinking. 1122 men from a total of 1546 on board both heavy cruisers were
> later rescued by the cruiser HMS Enterprise and the British destroyers HMS Paladin and HMS Panther."
> — https://www.uboat.net/allies/warships/ship/1185.html

> "Sighted by aircraft from Japanese cruiser TONE in position 01.54N 77.45E south of Ceylon. Came
> under heavy dive bombing attacks and sank within 8 minutes. 234 of ship's company lost their lives.
> 6th 1,122 survivors from both cruisers rescued by HMS ENTERPRISE, HM Destroyer PANTHER and PALADIN
> some 30 hours after the sinking."
> — https://www.naval-history.net/xGM-Chrono-06CA-Dorsetshire.htm

> "Dorsetshire was sunk by Japanese carrier aircraft (D3A1 diving bombers from Akagi, Hiryu and Soryu)
> 5.4.1942 (she received up to 10 bombing hits in 8 minutes)."
> — navypedia

**雷达与"为什么没及早发现"**：

> "In 1941 Dorsetshire was fitted with two radar sets, a Type 284 and a Type 290. The Type 284 was a
> gunnery set for the 8-inch guns. The Type 290 was a surface search set for detecting ships. It could
> also detect aircraft but only out to 30,000 yards (15 miles). The operator had to turn the antenna by
> hand and the display screen was an A-scan rather than the Plan Position Indicator (PPI) of today.
> The Type 290 'never functioned as planned', according to one source."
> — combinedfleet 专题文

**它的位置是被命令挪出来的**（这一点决定了"为什么是它"）：

> "27 March - Friday / Dorsetshire enters dock at Colombo and commences refit"
> "31 March - Tuesday / 1900? Dorsetshire leaves Colombo to join Somerville"
> "3 April - Friday / 0940 Cornwall and Dorsetshire are detached to Colombo"
> "4 April - Saturday / 1000 Cornwall and Dorsetshire arrive at Colombo"
> — https://www.combinedfleet.com/Appendex_1-4_Notes-RStuart-Adobe.pdf（附录 2 时间线）

---

## 7. Atlantis 与 Python 的混淆 —— 本组纠正的一条常见错误

任务书里写的是"1941 年 11 月击沉德国袭击舰 Atlantis（大西洋）"，**这条需要更正**。
击沉 Atlantis 的是重巡 **HMS Devonshire**（1941-11-22），本舰战果是 Atlantis 的补给船 **Python**
（1941-12-01）。三级来源互证：

1. combinedfleet（§6 引的那段，明写 "sunk by county class cruiser Devonshire on 22 November"）
2. naval-history Dorsetshire 年表：1941-11-11 "Deployed for search for German commerce raiders
   ATLANTIS and U-Boat Supply ship PYTHON"；1941-12-01 "Sighted German U-Boat supply ship PYTHON ...
   PYTHON scuttled"
3. uboat.net：1941-12-01 条同样只记 Python

**正文与 fact 都按"击沉 Atlantis 的不是本舰"写，并在 ships 文件头单独开了一个说明块。**

---

## 8. 一处**查不到、无法证实**的记载（重要）

任务书里还写"Dorsetshire 1940 年击沉法国布雷斯特的布雷舰"，**本轮无法证实，故完全未写入任何 fact**。

已试过的路径（全部无果）：

| 试过的检索/来源 | 结果 |
|---|---|
| naval-history Dorsetshire 年表（1940 全年逐月） | 无任何"击沉法国军舰"记录；1940 年只有 Wakama（德补给船，自沉）、Richelieu 监视、Zante 炮击 |
| naval-history 1940-06/07 逐日战报（4 个大页） | 涉本舰的条目全是护航、监视、达喀尔施压 |
| uboat.net Dorsetshire 逐日事件表 | 同上，无击沉法舰记录 |
| combinedfleet 专题文（45 页） | "The highlight of Cornwall's service during this period was its battle with the German raider Pinguin"——**那是 Cornwall，不是本舰** |
| de.wikipedia / fr.wikipedia Dorsetshire 条目 | 均无此记载 |
| Rohwer 1940-06 / 07 / 08 年表 | 只有监视 Richelieu 与潜艇攻击的记载 |

**一个高度可能的误传来源**：1940-07-03 英国在本土港口扣押法国舰船（Operation Catapult 的
本土部分），**朴茨茅斯与普利茅斯被扣押的法国舰里确实包含布雷舰**：

> "That night, more than 200 French vessels in British ports, most of them anchored at Portsmouth and
> Plymouth, were impounded. The ships included the battleships Courbet and Paris, the supply ship
> Pollux, destroyers, minelayers, ..."
> — https://warfarehistorynetwork.com/article/battle-against-an-ally/
> （同一句也见于 `https://warfarehistorynetwork.com/mers-el-kebir-sinking-the-french-fleet-in-world-war-ii/`
> 的镜像，但该 URL 本轮已 404，故引现存的那一个）

而本舰 1940-07 正在达喀尔外海，**不在本土**。所以即便有"法国布雷舰"这回事，
也**不是本舰**击沉的。**按红线 §1，本条整条不写，只在本文档与 RESEARCH-NOTES 的"卡住的地方"报备。**

---

## 9. 试过但抓不到的来源（三次不通，按要求报备）

| 目标 | 失败原因 | 影响 |
|---|---|---|
| `https://www.hmshood.org.uk/reference/official/adm234/adm234-509norf.htm` （**ADM 234/509 的 Norfolk 炮术与 RDF 报告转录，tier A**） | 两次尝试均 HTTP 403 | Norfolk 最终战的 527 发与 X 塔故障只能引 navweaps 的转述，拿不到原件。已把 X 塔那条降为 B |
| `https://www.naval-history.net/xGM-Chrono-10CA-HMS_Norfolk.htm` / `..._Dorsetshire.htm` | HTTP 404（SCHEMA 与任务书给的路径不存在） | 已换用 06CA 系列路径取到正文 |
| `https://www.world-war.co.uk/warloss_296fra.php`（法国二战损失全表） | HTTP 403 | 无法用它核对 §8 那条可疑记载 |
| `https://ww2db.com/ship_spec.php?ship_id=456` | HTTP 403 | 影响有限，其它源已覆盖 |

---

## 10. 有争议的记载（一条都没删，全部并列）

| # | 争议点 | A 说 | B 说 | 处理 |
|---|---|---|---|---|
| 1 | **本级有没有 89 mm 主装甲带** | 英文维基 Norfolk 条目："a 3.5 in (89 mm) belt was added before the war" | combinedfleet："No additional armour was fitted"（1937 改装）；维基 County 级条目：加带仅限 Kent 五舰 + London；navypedia 全期只有 25 mm | 取 25 mm；89 mm 完整写进 note，不裁决 |
| 2 | **Norfolk 完工日** | navypedia Comp 30.4.1930；维基单舰条目 30 April 1930 | naval-history "1st May 1930"；维基 County 级舰表 1 May 1930 | fact 取 4-30，5-1 写 note |
| 3 | **Dorsetshire 下水日** | navypedia 29.1.1929；naval-history 29 January 1929；维基单舰条目 29 Jan | 维基 County 级舰表 24 Jan 1929 | fact 取 29 日，24 日写 note（同站内自相矛盾） |
| 4 | **Dorsetshire 建造厂** | navypedia / naval-history / 维基：Portsmouth Dockyard | uboat.net 建造厂栏同时列 Cammell Laird (Birkenhead) | 取 Portsmouth；见 sources-fragment 的 uboat 条 note |
| 5 | **Dorsetshire 标准排水量** | combinedfleet 表 1（建成）：9,830?；正文/表 2（1937 后）：10,400 | 维基：10,035 lt = 10,196 t；navypedia：9,925–9,975 | 单舰取 10,400（载况清楚）；三说全列 |
| 6 | **本级设计航速** | navypedia 32.3；combinedfleet 32.25 | 维基 Dorsetshire 信息框 31.5（疑为 Kent 子级串值） | 取 32.3；三说并列 |
| 7 | **本级续航力** | navypedia 12,500 nm @12 kn | combinedfleet 表 1（Dorsetshire）9,300 nm；维基 Norfolk 12,370 nm @12 kn | 取 navypedia 值；三说并列，均未注载油状态 |
| 8 | **1940-03-16 空袭命中舷别** | naval-history："port side of quarterdeck" | 维基："starboard side below the waterline" | 两说并列，不裁 |
| 9 | **北角海战 Norfolk 阵亡数** | naval-history：7 死 5 伤 | 维基：6 死 | fact 取 7（tier D）；6 写 note |
| 10 | **Dorsetshire 此战鱼雷命中数** | kbismarck 整理 + 英方一手审讯：3 雷全中 | Campbell（经维基引注）：发 3 中 2 | 两说并列，不裁 |
| 11 | **多塞特郡发射鱼雷时刻** | kbismarck + 本站 last-battle.yaml：10:22 | combinedfleet：10:25 | fact 取 10:22 与站内一致；10:25 写 note |
| 12 | **1942-04-05 左倾出现在攻击后几分钟** | combinedfleet 正文：4 分钟 | Agar 首份报告：5 分钟 | 两说并列（来源自带括注） |
| 13 | **Dorsetshire 两舰生还数** | naval-history / uboat：两舰合计被救 1,122（编制 1,546） | 英文维基引 Bercuson & Herwig：仅 110 人获救（85 + 25）；引 Konstam：116 获救 | 1,122 为两舰合计（tier D 支撑），照录；110/116 属单舰口径混用，不采 |
| 14 | **谁先发现俾斯麦（1941-05-23 夜）** | naval-history + ADM 234/509 审讯："first sighted by Norfolk at 2032, 23rd May"；naval-history 年表："Made first sighting report on BISMARCK" | 英文维基 Norfolk 条目："Suffolk spotted the two German ships" | 正文表述取"本舰发出首次接触报告"（两个非 E 来源）；维基的 Suffolk 一说写进此处 |
| 15 | **Dorsetshire 1940 年是否参加挪威战役** | 常见叙述把 County 级挪威作战泛化到本舰 | 本舰 1940-04-24 离西蒙斯敦、05-25 抵普利茅斯改装、06 月即赴达喀尔；naval-history / rohwer 均无挪威记录 | 正文明确写"1940 年本舰不在挪威"，作为纠错段 |

---

## 11. 采用的"不写"清单（按红线 §1，拿不到就不写）

- 装甲总重与装甲占比（Dorsetshire 只有 combinedfleet 给 1,060 t，Norfolk 完全没有 → 两舰都不写）
- 试航实测功率、试航实测航速
- 螺旋桨直径、舵面积、舱段划分、型深、方形系数、水线面积、干舷
- 蒸汽温度、锅炉压力（navypedia 未给本级）
- 发电机台数与总功率
- 造价
- 水下防护纵深（本级无防雷突出部，且无任何纵深数值 → 舰级层用注释说明"不存在"，未编造数字）
- Norfolk 1940-03-16 的伤亡 4 死 6 伤（仅 tier E）
- Dorsetshire 1941-05-27 的伤亡 0（仅 tier E）
- 两舰精确全长与吃水（仅 tier E 有分舰值，统一用舰级区间值）
- 炮塔逐座的重量/射界/仰角（navweaps 只给型号级的通用值，逐塔数据未逐舰给出）

---

## 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/county.yaml`，89 条 fact） |
| 单舰文件 | 2（`ships/norfolk.yaml` 44 条、`ships/dorsetshire.yaml` 31 条） |
| 切片文件 | 2（各 8 片，共 16 片） |
| 正文文件 | 2（`articles/norfolk.yaml` 24 条事件、`articles/dorsetshire.yaml` 23 条事件） |
| 新登记来源 | 9 |

**fact 合计 164 条**（舰级 89 + 单舰 75）。舰级 89 条的构成：
舰级本体 39 + 武器实体 `weapon:8in-50-mk8` 22 + 炮位实体 4 座（A/B/X/Y，共 28）。
另有正文 2 篇（47 条事件）、切片 16 片。

### 卡住的地方

1. **`hmshood.org.uk` 的 ADM 234/509 Norfolk 炮术报告转录（tier A）两次 403**。
   Norfolk 最终战只能引 navweaps 的转述，X 塔故障那条因此只能给 B。
   谁有渠道拿到这件一手材料，可以把它升到 A。
2. **SCHEMA 与任务书给的 naval-history URL 模板（`xGM-Chrono-10CA-HMS_Norfolk.htm`）是 404。**
   实际路径是 `xGM-Chrono-06CA-Norfolk.htm`（**06CA，且无 `HMS_` 前缀**）。
   建议主会话把 SCHEMA §9 与来源模板改掉，否则后续组会全部踩这个坑。
3. **任务书里"Dorsetshire 1940 年击沉法国布雷斯特的布雷舰"无法证实，整条未写。**
   已查 naval-history 全年逐月 + 1940-06/07 逐日战报 + uboat.net 逐日表 + Rohwer 1940-06/07/08
   年表 + combinedfleet 45 页专题文 + de/fr 维基，全部无此记录。
   最可能的误传来源是 1940-07-03 英国本土港口扣押法国舰船（其中确有布雷舰），
   但本舰当时在达喀尔外海，不在本土。详见 §8。
4. **Dorsetshire 精确全长（632 ft 9 in / 192.86 m）与吃水只出现在 tier E**，
   按红线不写 fact，两舰统一用舰级区间值。
5. **`world-war.co.uk` 的法国损失全表 403**，无法用它二次核对第 3 点。

### 有争议的记载

见 §10 的 15 条表。**影响最大的是三条**：

- **第 1 条（89 mm 装甲带）**：维基单舰条目与三处其它来源正面冲突，本站不采维基，
  但把这一说完整保留在 note 里。
- **第 13 条（Dorsetshire 生还数）**：1,122 是**两舰合计**，110/116 是单舰口径，
  极易被混成"本舰生还 110 人"。已在 fact 里用大字写清。
- **第 14 条（谁先发现俾斯麦）**：Admiralty 审讯报告与 naval-history 都说 Norfolk，
  维基说 Suffolk。正文取前两者，维基一说留档。
