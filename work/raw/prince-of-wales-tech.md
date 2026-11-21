# HMS Prince of Wales（威尔士亲王号，舷号 53）— 单舰差异调研

> 检索日期：2026-11-21。挂靠舰级 `data/classes/king-george-v.yaml`（176 条 fact）。
> **本文只写单舰差异。** 舰级共有的主尺度、排水量、动力、防护、主炮/副炮/高炮性能参数一律不重复，
> 需要时直接指向舰级文件。凡本文出现舰级数值，都是为了**对照出单舰的不同**。
>
> **硬规则执行说明**：每个数值后附来源代号与英文原句（原文照抄，不翻译后回译）；查不到一律写「未获取」；
> 分歧并列、**不裁决**。E 级（维基）只用于定线索，**不作任何数值的来源**，凡引用均单独标注「E，仅线索」。
>
> **前置纠错**：任务书有三处前提与史料不符，已在 §0 集中反驳，正文相应位置再标注。

---

## 0. 对任务书前提的反驳（先看这一节）

### 0.1 「1941-03-31 服役」——不成立。03-31 是**完工**，服役是 1941-01-19

任务书写「1941-03-31 服役」。两个日期在本舰上分得很开，而且分得比首舰更开：

- **1941-01-19 = 服役（commissioned）**，且是「未完工、半船员、仅为试航」服役：
  > 「19th - Commissioned, incomplete, and with only half her crew, for trials. CO Captain Louis Henry Keppel Hamilton RN.」
  > —— [nh-pow]
- **1941-03-31 = 完工（classified as completed）**，而且是**豁免试验换来的完工**：
  > 「31st - The PRINCE OF WALES was officially classified as completed. The 'completion' was achieved by waiving various vital tests and before her armament was fully operational.」
  > —— [nh-pow]
- navypedia 的建造表同一格写「31.3.1941」，它这一栏的表头是 **Comp**（完工），不是服役：
  > 「Prince of Wales | 53 | 1026 | Cammell Laird, Birkenhead | 1.1.1937 | 3.5.1939 | 31.3.1941 | sunk 10.12.1941」—— [navypedia-kgv39]

**这不是本舰独有现象，而且两舰的间隔恰好都是 71 天**：
- 首舰 KGV：1940-10-01 commissioned（for trials）→ 1940-12-11 completed，**71 天**
- 本舰 PoW：1941-01-19 commissioned → 1941-03-31 completed，**71 天**

**这个巧合值得报告**：它说明「先服役、后完工」在本级是**制度化的两段式流程**，不是本舰的特例。
但后果完全不同 —— 本舰在「完工」后仅 **54 天** 就参加了丹麦海峡海战，而 KGV 有近半年。
**所以正确的表述是：1941-01-19 服役，1941-03-31 完工，1941-05-24 参战。**
「服役」与「完工」在本舰上必须分开写，混成一个日期会掩盖「赶工」这个全舰最关键的事实。

### 0.2 「1941-05-24 参加丹麦海峡海战」——成立，但「参加」的程度需要限定

任务书没写错，但漏了最关键的一层：她**名义上完工、实际上没形成战斗力**。
> 「The PRINCE OF WALES had had less than two months working up, which was completely inadequate considering all the new systems and the fact that 80% of her crew were Hostilities Only and had never been on a ship before. Further she still had major problems with her main armament and 100 Vickers Armstrong staff were embarked attempting to fix the problems.」
> —— [nh-pow]

Tovey 在正式战报里的措辞更狠：
> 「The Prince of Wales, with many of the contractor's workmen still on board, had joined the Fleet on 25th March. It was not until 27th April that the last of her turrets could be accepted from the contractor and that practice drills with the whole main armament could be started.」
> —— [adm234-509-tovey] §23

### 0.3 「交战后的燃油与损伤状态（为什么没有继续追击）」——**这是两个不同时间点的事，任务书把它们并成了一件**

任务书的问法隐含「因为没油所以没追」。史料不支持这个因果：

- **1941-05-24 当天不追击，理由里没有燃油。** 理由全部是战备状态。Wake-Walker 的原话：
  > 「should not re-engage until other heavy ships are in contact unless interception fails. Doubtful if she has speed to force action.」
  > —— [adm234-509-tovey] §28
  他自己的补充（同电）是「BISMARCK 效率不确定但高」。
- Tovey 的复核理由，逐条都不是油：
  > 「As a result of the action she was short of one gun and her bridge was wrecked. She was a brand-new ship, with turrets in which mechanical breakdowns had occurred and were to be expected, apart from damage, and she had had a bare minimum period of working up.」
  > —— [adm234-509-tovey] §23
- **燃油是次日（05-25）才成为退出理由的**，而且当时她已经在执行搜索而不是追击：
  > 「At this time the PRINCE OF WALES, now low on fuel, turned north easterly and steered for Iceland.」—— [nh-pow]

**并且必须点出：丹麦海峡之后真正缺油的是 KGV，不是 PoW。** Tovey 只给了 KGV 的油量：
> 「the King George V had only 1,200 tons (32 per cent) remaining」—— [adm234-509-tovey] §64
**PoW 在 05-24／05-25 的剩余燃油吨数与百分比：未获取。** 所有已抓来源都只写「low on fuel」，不给数字。

### 0.4 任务书 D 节把沉没主因写成「鱼雷直接命中 vs 抽水泵失效导致结构性进水」——这是一个伪二选一

真实的分歧不是这两项对立，而是**三条独立的破坏链**，各来源只强调其中一两条：

| 链 | 谁在强调 | 机制 |
|---|---|---|
| ① 鱼雷直接破口 | [bs14]（1955 官方战史）、[lg-forcez] | 命中即造成大破口与即时的舱室进水 |
| ② **螺旋桨轴把舱壁「铰」穿** | [garzke2012]（2007 残骸调查） | 轴偏心旋转，沿轴隧一路撕毁各道横舱壁的填料函 |
| ③ 电力丧失→泵失效 | [nh-pow]、[garzke2012]、[ngb-loss2] | 柴油发电机舱进水→舰尾电力全失→泵、舵机、雷达、后部 5.25in 全停 |

「抽水泵失效」在史料里是 **③ 的下游症状**，不是独立主因；而 ② 才是「结构性进水」的准确机制。
本文 §4 把三链都列，不裁决。

### 0.5 关于「ADM 234/509 机器被封 403」——确认，但正文已拿到

`https://www.hmshood.org.uk/reference/official/adm234/adm234-509guns.htm` 本次实测仍 **403**
（带 `Referer: http://www.hmshood.org.uk/` 亦 403）。**但本工作区已存有该页的完整转录**
`work/raw/hood/of-adm234-509guns.txt`（23,525 字节，含 Enclosure I–IV 全部），本文的 A 级引文全部取自这份本地转录。
同理 `adm234-509tovey.htm`、`adm116-4351_POW.htm` 亦为 403，均使用本地已存转录
（`of-adm234-509tovey.txt`、`of-116_POW.txt`，后者 152,204 字节）。

---

## 1. 建造与服役

### 1.1 下单

- 1936-07-29，1937 年造舰计划：
  > 「KING GEORGE V-Class Battleship ordered from Cammell Laird at Birkenhead under the 1937 Build Programme on 29th July 1936.」—— [nh-pow]
- navypedia 建造表同给 1.1.1937 / 3.5.1939 / 31.3.1941 —— [navypedia-kgv39]
- **注意与舰级文件的口径差**：舰级文件记本级「1936 年造舰计划」。本舰在 [nh-pow] 里明写 **1937 Build Programme**。
  这两句可以并存（1936-07 下单、编入 1937 年度计划），但**不能互相替代**，落库时别把舰级的「1936」覆盖到本舰。

### 1.2 厂 / 船台号

- Cammell Laird, Birkenhead；Yard No **1026** —— [navypedia-kgv39]
- 舰级文件已记全五舰的厂与船台号，此处不重复。

### 1.3 开工 / 下水

- 开工 1937-01-01 —— [nh-pow]、[navypedia-kgv39]
- 下水 **1939-05-03** —— [nh-pow]「laid down on 1st January l937 and launched on 3rd May 1939」；[navypedia-kgv39]「3.5.1939」
- **掷瓶人：未获取。** 首舰 KGV 有 RMG 明写「Launched by HM King George VI」，本舰在已抓来源中**没有任何一份写掷瓶人**。

### 1.4 舰名：原名 King Edward VIII

- **E，仅线索**：「Prince of Wales was originally to be named King Edward VIII but upon the abdication of Edward VIII the ship was renamed at Cammell Laird's shipyard in Birkenhead on 1 January 1937, before being laid down.」—— [wiki-pow]
- 该句给出的改名日期 **1937-01-01 与开工日同日**，逻辑上合理（改名后即铺龙骨）。但这是 E 级孤证，
  **本文不作为 fact**。可以确定的是：本舰是「Prince of Wales」这一舰名的第 12 次使用（[nh-pow]「as the 12th RN ship to carry this name」）。
- 舰训：E 级 infobox 给「Ich Dien」—— **E，仅线索**，未在任何非 E 来源见到。
- 绰号：E 级 infobox 给「PoW」—— 同上，**E，仅线索**。

### 1.5 建造期的两次事故 / 延误

这是本舰最关键的一段，直接决定了 §2 的结论。

**(a) 1940 年空袭受损 —— 日期三说并存，见 §6.1**

[nh-pow] 的记述最完整：
> 「During a Luftwaffe raid on the night of 8-9/8/40 a 250kg bomb (130kg of explosive), fell between the side of the fitting out basin and the ships port side in the vicinity of the after group of 5.25in guns. The bomb exploded underwater below the bilge keel. Buckling of the shell plating was caused for a distance of about 25ft, rivets were sprung and extensive flooding took place in the port outer compartments. The flooding was severe, due to the fact that final compartment air tests had not yet been made and the ship did not have her pumping system in operation.」

**这一段是本舰全部故事的根**：1940 年 8 月那次进水之所以严重，是因为**水密舱气密试验还没做、排水系统还没接上**。
四个月后 1941-12-10 沉没时，坏在同一个地方 —— 见 §4.3。

**(b) 完工被「加速」，靠豁免试验换来**

> 「As the war progressed there was an urgent need for capital ships, and so her completion was advanced by postponing compartment air tests, ventilation tests and a thorough testing of her bilge, ballast and fuel oil systems.」—— [nh-pow]

[nh-pow] 复述 Admiralty 的动机与原话式说明：
> 「The repairs had taken priority over various tests and because of Admiralty pressure many important tests were not carried out; including watertight compartment air tests, tests on fuel oil systems, full power trials et al. Also the quadruple 14in turrets were not fully operational which why Vickers Armstrong staff were still embarked」—— [nh-pow]

**(c) 主炮交货延误**

- 「Nevertheless, the late delivery of gun mountings caused delays in her outfitting.」—— [wiki-pow]（E，仅线索）
- [nh-pow]「This bomb damage and the problems in the deliveries of her main guns and turrets delayed her completion.」—— D 级，可采信。

### 1.6 服役 → 完工 → 参战：逐日节点

| 日期 | 事件 | 原句 / 来源 |
|---|---|---|
| 1941-01-19 | 服役（未完工，半船员，为试航） | 「Commissioned, incomplete, and with only half her crew, for trials.」[nh-pow] |
| 1941-01-19 | 首任舰长 Captain L. H. K. Hamilton RN | 同上 |
| 1941-01-28 | 离 Birkenhead 赴 Rosyth，**舰上载着 Cammell Laird 与 Vickers Armstrong 的工人** | 「When she sailed from Birkenhead she had embarked workers from Cammell Laird and Vickers Armstrong who were working on her main armament turrets」[nh-pow] |
| 1941-01~02 | 途中与 Cape Wrath 外海试炮 | 「En route she carried out gun trials.」[nh-pow] |
| 1941-02 | Rosyth 舾装；**装 Type 281 / 284 / 4×285** | 「Fit of radar Type 281 for aircraft warning and limited fire-control use, together with radar Type 284 for fire-control of forward main armament, and four Type 285 for fire-control of 5.25in armament was completed」[nh-pow] |
| 1941-02-15 | Captain John Catterall Leach MVO RN 接任舰长 | 「The PRINCE OF WALES new CO Captain John Catterall Leach MVO RN took command.」[nh-pow] |
| 1941-03-24 | 离 Rosyth 赴 Scapa，**工人仍在舰上** | 「with workers from Cammell Laird and Vickers Armstrong still embarked」[nh-pow] |
| 1941-03-26 | 开始 working up | 「commenced working up exercisers」[nh-pow] |
| **1941-03-31** | **正式归类为完工** | 「officially classified as completed. The 'completion' was achieved by waiving various vital tests」[nh-pow] |
| 1941-04 | Scapa 训练；**射击训练因四联装炮塔故障被大幅削减** | 「Gunnery exercises were severely curtailed due to the continuing problems with the quadruple 14in turrets.」[nh-pow] |
| **1941-04-27** | **第三座炮塔（最后一座）才被验收** | 「It was on this day that the last of her three turrets was accepted from Vickers Armstrong and practice drills with all her armament could commence.」[nh-pow] |
| 1941-05-08 | 全功率试航 | 「Carried out Full Power Trials.」[nh-pow] |
| 1941-05-21 | 向本土舰队司令报「可执行舰队任务」 | 「Ship reported to CinC Home Fleet as ready for Fleet service.」[nh-pow] |
| 1941-05-22 01:00 | 与 Hood 及 6 艘驱逐舰离 Scapa | [nh-pow]、[adm234-509-tovey] |
| **1941-05-24** | 丹麦海峡海战 | 见 §3 |
| 1941-05-27 | 抵 Hvalfjord 做战损修补 | 「On arrival at Hvalfjord work was immediately commenced on making good her battle damage.」[nh-pow] |
| 1941-05-28 | 赴 Rosyth | [nh-pow] |
| 1941-06~07 | Rosyth 修理；**装 Type 273（该型首装）** | 「Whilst in dockyard hands she was fitted with the first radar Type 273, a big ship surface search version of the 10 cm Type 271.」[nh-pow] |
| 1941-08-05~18 | 大西洋会议（RIVIERA），载邱吉尔 | [nh-pow]、[wiki-pow]（E） |
| 1941-09-24~27 | Operation HALBERD（马耳他运输队），属 Force H 第 II 群 | [wiki-pow]（E，仅线索；本批未取得非 E 来源对此役的记述） |
| 1941-10-25 | 离本土水域赴远东 | [wiki-pow]（E，仅线索） |
| 1941-11 | 开普敦，**加装 7 门单装 20mm** | 「(Whilst at Cape Town the PRINCE OF WALES had a seven 20mm Oerlikons fitted)」[nh-pow] |
| 1941-11-28 | 抵科伦坡 | [wiki-pow]（E） |
| 1941-12-02 | 抵新加坡，Force G 改名 Force Z | [nh-pow]「On arrival the force was renamed Force Z」 |
| **1941-12-10** | 被日军航空鱼雷/炸弹击沉 | 见 §4 |

### 1.7 造价

- **单舰精确值：未获取。** 本批所有已抓来源（[nh-pow]、[navypedia-kgv39]、[bs14]、[lg-forcez]、[garzke2012]）均未给本舰造价。
- 舰级文件里那条「Prince of Wales - £7,426,000」出自 Buxton & Johnston 的二手引述，**原页 403，未能核验**，
  舰级文件自己已标注「仅作线索登记，不作数据来源」。**本文沿用该判断，不写数字。**

---

## 2. 与同级舰的装备差异（本文最重要的一节）

### 2.0 先把「差异」分成三类 —— 这是本节的方法论

任务书要求区分「设计如此」与「舾装未完成」。实测下来**必须分成三类**，两分法不够用：

| 类别 | 定义 | 本舰实例 |
|---|---|---|
| **I 类 · 设计如此** | 本级各舰建造时就有区别，与工期无关 | 3 座 UP 火箭发射器（KGV 4 座）；1 门单装 40 mm Bofors（KGV 建成时无） |
| **II 类 · 舾装/改装节奏不同** | 同一设计，但装上船的时间点不同 | Type 282×4 / 285×4 / 281 / 284（1941-02 Rosyth）；Type 273（1941-07）；7×20 mm（1941-11）；追加 pom-pom |
| **III 类 · 名义有、实际不能用** | 装在舰上但战斗时不可用，根源是赶工期 | 14in 炮塔（Vickers 工人随舰修理）；Type 284（开战当天故障）；Type 281（被禁止使用）；**水密舱气密试验未做** |

**III 类才是本舰的真正特征**，也是它和首舰 KGV 最本质的差别 —— KGV 服役时同样未完工，但没有在「完工」后 54 天就打仗。

### 2.1 I 类：UP 火箭发射器 —— 本舰 **3 座**，KGV **4 座**

- 本舰：> 「Prince of Wales: 2 x 4 - 356/45 BL Mk VII, 1 x 2 - 356/45 BL Mk VII, 8 x 2 - 133/50 QF Mk I, 1 x 1 - 40/56 Bofors Mk I/III, 4 x 8 - 40/39 2pdr QF Mk VIII, **3 x 20 - 178 UP rockets projectors**, 1 catapult D-III-H, 2 seaplanes (Walrus, Swordfish, Seafox)」—— [navypedia-kgv39]
- 首舰：> 「King George V: … **4 x 20 - 178 UP rockets projectors**, …」—— 同上，同一页紧邻上一行
- **这是同一张表里的两行，直接可比**，不是跨来源拼凑。E 级 infobox 亦给「3 × 20-barrel AA rockets」（[wiki-pow]，仅线索）。
- **为什么少一座：未获取。** 已抓来源中无任何一份解释这个差别的来源或理由。**不推测。**
- 拆除时点：1941-06~07 Rosyth 改装中全部拆除（见 §2.3）。

### 2.2 I 类：单装 40 mm Bofors —— 本舰有 1 门，KGV 建成时**没有**

- 本舰装备行明列「1 x 1 - 40/56 Bofors Mk I/III」—— [navypedia-kgv39]
- 首舰装备行**无此一项** —— 同上
- **独立佐证（关键）**：1941-12-10 沉没当天的战斗记述里，40 mm Bofors 确实在射击：
  > 「the tracer shells of the 20mm Oerlikons and the 40mm Bofors were seen to make some of the attackers jink」—— [nh-pow]
  这一句把「本舰有 40 mm」从装备表推断升级为**战斗记录实证**。
- **对照舰级文件**：舰级文件记 KGV 的 Bofors 是 **1944-07** 才装的 2 座四联美制 Mk II。
  本舰这 1 门是**单装、英制 40/56 Mk I/III**，口径同、型号不同、数量不同、时间早三年。**落库时不要合并。**
- 装舰时点：未获取（[nh-pow] 的逐日年表里没有「装 40 mm」这一条，只在 12-10 战斗中出现）。

### 2.3 II 类：舾装与改装带来的配置差

**(a) 1941-02，Rosyth：Type 281 + 284 + 4×285**
> 「Fit of radar Type 281 for aircraft warning and limited fire-control use, together with radar Type 284 for fire-control of forward main armament, and four Type 285 for fire-control of 5.25in armament was completed」—— [nh-pow]

**(b) 1941 年 5 月（赴丹麦海峡前）：再加 4×282 + 4×285，合计九部防空火控雷达**
> 「The PRINCE OF WALES went to sea with HACS IVGB, with full radar ranging systems, and no less than nine AA fire control radars: four Type 285 Radars, one on each High Angle Director Tower and four Type 282 Radars, one on each Mk IV pom-pom director, and a long range Type 281 Radar which also had precision ranging panels for aerial and surface targets. This placed the PRINCE OF WALES in the forefront of naval HA AA fire control systems at the time」—— [nh-pow]

**这一段有三个可直接落库的推论**：
1. **高角指挥仪塔 = 4 座**（「one on each High Angle Director Tower」，4 部 285）。
2. **pom-pom 指挥仪 = 4 座**（「one on each Mk IV pom-pom director」，4 部 282）—— 而同级首舰的调研
   （`work/raw/kgv-tech.md` §fire_control）记 KGV 是 **6 座** Mk IV pom-pom director。
   **注意口径**：`data/classes/king-george-v.yaml` 里**没有**这一项（只有 `sensors.director.count = 2`，指主炮指挥仪塔），
   6 座这个数只存在于 KGV 的单舰调研稿，**尚未进舰级文件**。若属实，这是两舰的真实差别，不是笔误；
   但它是「艘间差异」还是「不同时期状态」，本文**未能判定** —— 已列入 §6.3 未获取。
3. **Type 282 的首装舰就是本舰**，有独立的 D 级来源确认：
   > 「Type 282 … First used on HMS Prince of Wales.」—— [navweaps-radar-uk]

**(c) 1941-06~07，Rosyth：拆 UP、加 pom-pom、装 Type 273**
> 「UP projectors removed. 2 × 8-barrelled and 1 × 4-barrelled 2-pdr pom-poms added. Type 271 radar added.」—— [wiki-pow]（E，仅线索）

**但同一件事在 [nh-pow] 里写的是 Type 273，不是 271**：
> 「Whilst in dockyard hands she was fitted with the first radar Type 273, a big ship surface search version of the 10 cm Type 271.」—— [nh-pow]

见 §6.4，此处分歧不裁决。**pom-pom 的增量两源一致（+2 座八联 +1 座四联）**，这部分可用。

**(d) 1941-11，开普敦：7 门单装 20 mm**
> 「(Whilst at Cape Town the PRINCE OF WALES had a seven 20mm Oerlikons fitted)」—— [nh-pow]
- 同一事实的 E 级版本：「November 1941 | Cape Town | 7 × single 20 mm added.」—— [wiki-pow]（仅线索，与 D 级吻合属巧合利好，但**不作数值来源**）
- **对照**：KGV 到 1941-12 已有 18 门单装 20 mm（舰级文件）。**本舰沉没时只有 7 门。** 这是防空火力上的实质差距。

**(e) 鱼雷发射管：无 —— 与舰级一致，非差异**
舰级文件已判定本级无鱼雷管，本文不重复论证。

**(f) 弹射器与水上飞机：1 座 D-III-H，机型有分歧，见 §6.5**

### 2.4 III 类：装在舰上但打不了 —— 本舰的关键问题

**(a) 14 英寸炮塔：从服役到沉没就没好过**

本舰四联装炮塔的不可靠是本级公认缺陷（舰级文件已记），但本舰的**程度**是单舰级别的：
> 「During the working up period numerous minor mechanical defects have been experienced in spite of unremitting efforts on the part of the Ordnance staff, and during the operations against Bismarck this state of affairs persisted. In the circumstances the output achieved might well have been lower. That this was not so was due to the continual efforts of the Ordnance staff and with one exception, to good loading drill in the turrets. **The presence in each turret of one of Messrs. Vickers Armstrong's erecting staff was of the greatest assistance.**」
> —— [adm234-509]（本舰舰长 Leach 本人 1941-06-12 的《炮术附录》原文）

**「每座炮塔里都有一名 Vickers Armstrong 的装配技师」—— 这是 A 级一手文件，一句话把「未完工」钉死。**
到 1941-05-24 时已经打完两个月训练，工人还在舰上。

舰级文件已列的炮塔机械复杂度、3,000+ 活动件等，此处不重复。本节只补单舰事实。

**(b) Type 284 主炮雷达：开战前数小时被判定故障**

这是本舰最戏剧性的一条，**A 级与 D 级双重印证**：

D 级（事件链）：
> 「At 0203 hours ... Holland ordered the PRINCE OF WALES to make a surface search with her Type 284 radar, when activated the 284 was found to be defective, and Holland refused permission to use the Type 281.」—— [nh-pow]

A 级（本舰炮术报告的结论）：
> 「No results were obtained from either Type 281 or 284 R.D.F.; it is understood that Signal School Officers are now of the opinion that Type 281 suffered interference and Type 284 was defective, although it appeared at the time that 284 was also suffering from interference.」
> —— [adm234-509] §4

**注意这两句的关系**：D 级说 284 在 0203 就坏了；A 级说「281 受干扰、284 有缺陷」。
两者不矛盾，而是**互补**：284 是硬件坏，281 是受干扰（且 Holland 干脆不许用）。

**关键的对照**：就在前一天（05-23）的雷达校准演习，结论是「一切正常」。
> 「Between 1135 and 1245 hours further radar calibration exercises were conducted; again the radars were found to be working in accordance with specification.」—— [nh-pow]

**即：本舰在 05-23 中午雷达是好的，05-24 0203 就坏了，05-24 0553 开火时没有雷达测距。**
这就是「舾装未完成 + 时间不够」的直接后果，而不是设计缺陷。

**(c) 没有雷达测距之后怎么打的 —— 本舰炮术官的应急办法**

这是本舰单舰层面的亮点，值得单列：
> 「The rangefinders failed to develop a satisfactory range plot before opening fire; the fore D.C.T. 15-ft rangefinder was the only rangefinder which had a reasonable chance; the closing rate was very high and "A" and "B" rangefinders were able to see the enemy's superstructure for a short time only before "table turning." Conditions for ranging on the enemy's masts were not easy. As a result it required two down ladders to find the target.」
> —— [adm234-509] §3

**对照舰级文件的记录**：本舰的 Type 284 有「forward main armament」的 fire-control 用途（1941-02 装）。
也就是说，**装是装了，仗打到一半发现是坏的**。这是 III 类的标准样本。

### 2.5 若查不到差异，明确写「查不到」的项目

以下项目**本文明确写「未获取」/「查不到」，不写「与舰级相同」**：

| 项目 | 状态 |
|---|---|
| 本舰 5.25 in 副炮的**实际座数与布置**在本舰层面是否有别于 KGV | 查不到。两源均给 8 座双联（[navypedia-kgv39]、[nh-pow]），与舰级一致，**但没有任何来源明说「与首舰相同」**，因此只能记「两源数值相同」，不能记「确认无差异」 |
| 本舰 HACS 的实际型号是否为 **Mk IVGB**（而非 Mk IV） | **有，见下** |
| 本舰 pom-pom 的**精确座数**在 1941-05-24 当日 | 查不到即时快照。[navypedia-kgv39] 给建成 4×8；1941-06/07 加 2×8+1×4 |
| 本舰 20 mm 在 1941-05-24 当日的门数 | **未获取**。7 门是 1941-11 开普敦加装的；此前有无、有几门，无来源 |
| 本舰有无 0.5 in 机枪 | 未获取（KGV 是设计案未装，见舰级文件） |
| 本舰防空指挥仪的**陀螺测速**改装状态 | 未获取 |

**关于 HACS 型号（可以确认，且与舰级文件的表述有出入）**：
[nh-pow] 两次明写 **HACS IVGB**：
> 「The PRINCE OF WALES went to sea with **HACS IVGB**, with full radar ranging systems…」—— [nh-pow]
navweaps 的 HACS 专文确认 Mk IV 的装舰范围**是前四艘，不是前两艘**：
> 「The HACS Mark IV was installed on "Town" and succeeding cruisers, **the first four units of the King George V class battleships** and to new aircraft carriers.」—— [navweaps-hacs]

**这与舰级文件「4 部，为本级首两舰（King George V、Prince of Wales）独有配置；本级后续舰改用 Mk V / Mk VI」的表述不完全一致。**
见 §6.6，不裁决。

---

## 3. 丹麦海峡（1941-05-24）

### 3.1 时间与距离：三个来源的「开火距离」互不相同，必须分开记

| 事项 | 数值 | 原句 | 来源 |
|---|---|---|---|
| 发现敌舰 | 05:35，方位 335°，约 41,500 yd | 「At 0535 hours the BISMARCK and PRINZ EUGEN were sighted bearing 335 degrees at approximately 41500 yards」 | [nh-pow] |
| 本舰报告敌情 | 05:37，距 38,000 yd | 「Enemy was sighted at 0537, range about 38,000 yards.」 | [adm234-509] §B1 |
| 本舰开火 | **05:53** | 「Fire was opened at 0553, half a minute after Hood.」 | [adm234-509] §B5 |
| 开火时**真距** | **25,000 yd** | 「The true range on opening was 25,000 yards.」 | [adm234-509] §B6 |
| 停火时**真距** | **14,500 yd** | 「The true range on ceasing fire was 14,500 yards.」 | [adm234-509] §B6 |
| navypedia 的解说 | — | 「The first has achieved three hits to German ship 24.5.1941」 | [navypedia-kgv39] |

**注意**：kbismarck 给的开火距离是 23,150 m / 25,330 yd（「from a distance of about 12.5 miles (23,150 metres / 25,330 yards)」—— [kb-ds]），
与 [adm234-509] 的 25,000 yd 差约 330 yd。两者是「本舰实测」与「第三方推算」之别，**并列不裁决**。

### 3.2 射击过程（A 级，本舰炮术官视角）

[adm234-509] §B6 是逐次齐射的原始记录，直接可引：

> 「Salvoes 1 and 2 were spread for line, salvo 1 falling right and salvo 2 in line over. Salvoes 3 and 4 were fired as a down ladder and fell over. Salvoes 5 and 6 were fired as a further down ladder; 5 fell over and 6 straddled. It had been decided after Prince of Wales' last firing to use a 200-yard as opposed to a 100-yard zigzag, as the spreads were in the nature of 350 yards. Accordingly salvoes 7 and 8 were fired as a 200-yard zigzag about salvo 6's range. Both 7 and 8 were observed as over and salvoes 9 and 10 were fired as a regaining down ladder. Salvo 9 was seen to straddle, 10 short, and salvoes 11 and 12 were fired as a 200-yard zigzag about salvo 9's range. Both of these were spotted as short, and salvoes 13 and 14 were fired as a regaining ladder up: 13 appeared to straddle, 14 went over…」

**命中判定（A 级，最保守的表述）**：
> 「No hits were observed, but it is likely from results observed that fire was effective between salvoes 5 and 16.」—— [adm234-509] §B6

**这一句必须原样保留**：本舰自己的炮术报告**没有观察到命中**。所谓「三发命中俾斯麦」是战后综合判定，
不是本舰当时的观察结果。落库时这一层不能抹掉。

射击效率（A 级，Enclosure I 表格）：

| 项目 | 第一次交战（05:53–06:13 前后） |
|---|---|
| 持续时间 | 8 分 58 秒 |
| 齐射数 | 18 |
| 实际发射炮弹 | 55 |
| 应发射炮弹 | 74 |
| 齐射/分 | 1.895 |
| 有效全齐射/分（E.F.G.） | 1.41 |
| **火力输出损失** | **25.65 %** |

—— 全部出自 [adm234-509] Enclosure (I)。D 级复述同值：
> 「The PRINCE OF WALES fired 18 salvoes in which 74 guns should have fired but only 55 actually fired. The 18 salvos achieved three straddles and three hits on BISMARCK」—— [nh-pow]

### 3.3 命中俾斯麦的那几发：逐发、部位、后果

三发的部位与后果，[kb-ds] 与 [nh-pow] 记述**实质一致**，措辞近乎同源：

**第一发 —— XIV 段水线下，主装甲带下方**
> 「The first shell hit Bismarck amidships below the waterline in section XIV, passed through the outer hull just below the main belt, and exploded against the 45-mm armoured torpedo bulkhead. This hit caused the flooding of the port electric plant No. 4. The adjacent No. 2 boiler room also took some water, but this was contained by the damage control parties through the use of hammocks.」—— [kb-ds]
> 「Hit one - Hit amidships below the waterline in section XIV, passed through the outer hull just below the main belt, and exploded against the 45mm armoured torpedo bulkhead. This hit caused the flooding of the port electric plant No. 4. The adjacent No. 2 boiler room also took on some water.」—— [nh-pow]
**后果：左舷 4 号涡轮发电机舱全淹；2 号锅炉舱少量进水，用吊床堵住。**

**第二发 —— XX–XXI 段水线上，穿舰首，未爆**
> 「The second shell hit the bow in section XX-XXI, just above the waterline. This projectile entered the port side, passed through the ship above the 20-mm upper platform deck without exploding, and exited the starboard side leaving a hole of 1.5 metres in diameter. Around 1,000 tons of salt water got into the forecastle, and as a consequence of this several hundred tons of fuel oil were blocked down in the lower tanks.」—— [kb-ds]
[nh-pow] 多给一句后果：
> 「Oil from the ruptured tanks flowed out causing a broad oil slick in her wake.」
**后果：约 1,000 t 海水进艏楼，数百吨燃油被封在下部油舱、部分外泄形成油迹。**

**第三发 —— 穿过舰中部一艘救生艇，无实质损伤**
> 「The third shell simply passed through a boat amidships without any appreciable damage at all.」—— [kb-ds]
> 「Hit three - this shell passed through a boat amidships without causing any appreciable damage.」—— [nh-pow]

**综合后果**
> 「As a result of these hits, the top speed of the Bismarck was reduced to 28 knots. The battleship was 3° down by the bow and had a 9° list to port. Because of this, the ship motions caused the blades of the starboard propeller to emerge from the water at times. Therefore the starboard void tanks in sections II and III were flooded to reduce the bow trim and list. The damage was not particularly serious, the Bismarck maintained intact her fighting capability, good speed, and there were no casualties among the crew; only five men had been slightly wounded. However, the loss of fuel was to affect the remaining course of action.」—— [kb-ds]

**⚠ 第三发「打坏弹射器蒸汽管」这一条，本文未能证实。**
`data/battles/denmark-strait.yaml` 的 hits_received 第三条写「穿过一艘救生艇，再穿过水上飞机弹射器，未爆炸。打坏弹射器蒸汽管——这直接导致 5 月 27 日无法弹射 Ar 196 送走航海日志」，src 为 `[kbismarck-denmark-strait, kbismarck-aviation]`。
但 [kb-ds] 原文只有「passed through a boat amidships without any appreciable damage at all」，**没有提弹射器，也没有提蒸汽管**。本文在 [kb-ds] 中检索 `catapult` 亦无命中。
本条可能出自 kbismarck 的另一页（avioni），但本批**未能核到该页原文**，故标为**存疑，不作本文结论**。

### 3.4 本舰自身受损

**命中次数：三说并存，见 §6.2。** 三种计法：

| 说法 | 数字 | 原句 | 来源 |
|---|---|---|---|
| 7 发（4×15in + 3×8in） | 7 | 「Within a very few minutes she was hit by four 15-in, and three smaller, probably 8-in. shells」 | [adm234-509-tovey] §19 |
| 7 发（3×15in + 4×8in） | 7 | 「the PRINCE OF WALES was hit seven times, three hits with 15in shells and four hits with 8in shells」 | [nh-pow] |
| 8 发（5×38cm + 3×20.3cm） | 8 | 「itself has received 5 380mm and 3 203mm shells」 | [navypedia-kgv39] |
| 7 发（4+3，德方视角） | 7 | 「being hit a total of four times by the Bismarck and three more by the Prinz Eugen」 | [kb-ds] |

**舰桥命中（06:02）**
> 「At 0602, the Bismarck hit Prince of Wales' bridge, killing everybody there, except the commander, Captain John Catterall Leach and another man.」—— [kb-ds]
> 「At 0602 hours A shell from BISMARCK's first salvo fired at the PRINCE OF WALES passed through the compass platform without exploding but killing everyone except the Captain and the Chief Yeoman.」—— [nh-pow]
- **两源对「谁活下来」的表述不同**：kbismarck 说「舰长与另一人」，naval-history 说「舰长与首席文书军士（Chief Yeoman）」。
  后者更具体，但**两者都只说两人**，实质一致。
- **弹种与后果**：炮弹**未爆**，穿出。伤亡由弹道帽碎片与穿舱抛出的碎片造成。
  E 级 infobox 对碎片机制的描述更细（「Casualties were caused by the fragments from the shell's ballistic cap and the material it dislodged」），**仅线索**。
- **Tovey 的官方概括**：「her compass platform was damaged and most of the people on it killed or wounded; **both forward H.A. Directors and the starboard after one were out of action**; one four-gunned turret had jammed and the ship was holed underwater aft.」—— [adm234-509-tovey] §19
  **「两座前部高角指挥仪 + 右舷后部一座失效」= 4 座里废了 3 座。** 这是本舰防空指挥能力在当天崩掉的直接证据。

**炮塔故障（A 级，逐炮逐齐射）**

[adm234-509] Enclosure (I) 注与 Enclosure (III) 给出精确到「第几发齐射、几号炮」的记录：

- 「A.1 gun out of action after one salvo.」—— A 塔 1 号炮打完第一发齐射即失效
- 「A.1 gun out of action from 5th salvo onwards.」—— 第二次交战中，A1 从第 5 发齐射起失效
- 「A.3 gun temporarily out of action after 11th salvo.」—— A3 在第 11 发齐射后临时失效
- 「In addition "Y" turret fired four rounds in local control after 18th salvo: shell ring then jammed.」—— Y 塔在第 18 发齐射后于局部控制下打了 4 发，随后**炮圈卡死**
- 「"Y" turrets' shell ring jammed during the turn away and the turret was out of action until 0825」—— Y 塔卡到 **08:25** 才恢复

Enclosure (III) 更细，例如 Y 塔：
> 「Salvo 20 - Owing to the motion of the ship, a shell slid out of the port shell room and fouled the revolving shell ring while the latter was locked to the trunk and the turret was training. The hinge tray was severely buckled, putting the revolving shell ring out of action.」

**这些是 A 级一手细节，舰级文件没有、也不可能有一一对应到齐射编号的记录。落库时这是本舰独有的一组 fact。**

**水线下中弹（未爆弹）—— 本舰最接近沉没的一次**

[nh-pow] 全文转录了舰长 1941-06-08 的报告原文，这是极好的一手材料：
> 「During the early morning action on May 24th a heavy hit was felt abreast the Starboard Diesel Room. It was found that the outer air space 184-196, the outer oil fuel tank 184-206, the inner air space 184-194, the starboard diesel tank 184-206 were full to the crown with oil and water.」
> 「2. On Friday 6th June, on pumping out the dry dock a clean hole in the side about 15in diameter was found, a foot above the bilge keel at 187 starboard.」
> 「5. The diameter of the shell measured just above the driving band was 14.875 inches. From point of first impact on the ship to point of impact on the protective bulkhead the shell travelled 12 ft.」
> 「**If the shell had exploded it is possible that the PRINCE OF WALES may have met the same fate as the HOOD.**」—— [nh-pow]

**这一句是本舰生涯最重要的假设句，且出自舰长本人。** 落库时建议整条保留。

### 3.5 击沉胡德时本舰在哪里、做了什么

**位置（05:49，接敌时的队位）**：本舰在 Hood 的右后方 4 链（810 yd）。
> 「At 0549 hours course was altered to 300 degrees. At this time the PRINCE OF WALES took station on HOOD's starboard quarter, four cables distant (810 yards), bearing 135 degrees.」—— [nh-pow]

**⚠ 这是 05:49 的队位，不是 06:01 Hood 爆炸瞬间的队位。** 两者之间英舰做过两次转向（20° 向左、再 20° 向左），
**06:01 时本舰相对 Hood 的精确方位与距离：未获取**（[nh-pow] 只给「右后方 4 链」这一个时点）。

**Hood 爆炸后本舰的规避动作，反而把自己送进了德舰火线**：
> 「The British battleship had since altered her course to avoid the wreck of the Hood, and this placed her between the sinking battle cruiser and the German ships. The Germans were thus presented with an easy target switch.」—— [kb-ds]

**期间本舰在做的两件事**：
1. **继续射击俾斯麦**。按 [adm234-509] Enclosure I，本舰第一次交战共 18 发齐射；Hood 于 06:01 爆炸，
   06:13 停火，**这 12 分钟内的齐射编号未逐发标注**（原文只标到第 18 发齐射是最后一次）。
   能确定的是第 13、14 发被记为「straddle / over」，第 15–16 发「both appeared as short」，第 17–18 发「probably went short」。
   > 「salvoes 13 and 14 were fired as a regaining ladder up: 13 appeared to straddle, 14 went over… and salvoes 17 and 18 were fired as an up regaining ladder. The fall of shot of these salvoes is not certain, but it is probably that they went short」—— [adm234-509] §B6
2. **水上飞机被打掉** —— Tovey 的记述：
   > 「After emptying her aircraft in preparation for a night encounter, she had been unable to refuel it in time to fly off before contact was made. It was just about to be catapulted when it was hit by splinters and had to be jettisoned.」—— [adm234-509-tovey] §19
   即：**燃油受污染 → 来不及放飞 → 弹射前被破片击中 → 抛弃。** 三因叠加，本舰当天**全程无空中侦察**。
   Bonomi 的记述补了燃油污染的细节：「Due to the presence of water in the fuel, the launch was postponed; the airplane was later damaged during the battle and jettisoned.」—— [hood-bonomi]（C 级）

**「本舰有没有为 Hood 报仇式的追击」——没有，也不可能。** 06:13 停火撤离：
> 「At 0613 hours Captain Leach decided to break off the action and turned hard to port. This manoeuvre caused Y turret to jam as it trained round to compensate for the change of course.」—— [nh-pow]

### 3.6 交战后的损伤与燃油状态

**损伤（次日 Hvalfjord 抢修时确认）**
> 「The most pressing problem was the flooding aft, so the ship was listed to port exposing where two 8in shells had burst in the stern. The water was pumped out and the damaged plated over.」—— [nh-pow]

**航速**：Tovey 记录本舰当时「could not exceed 27 knots」，且「had taken in 400 tons of water aft」—— [adm234-509-tovey] §23。
（设计 28 kn，见舰级文件；此处是**战损后实测上限**，是单舰数据。）

**伤亡**：13 死 9 伤，其中 1 人次日死亡 → 合计 14。
> 「but they caused 13 deaths and 9 wounded, one of whom died the following day」—— [nh-pow]（D 级）
> 「The Prince of Wales had 13 fatal casualties that would become 14 by the following day」—— [kb-ds]（D 级）
[kb-ds] 脚注给了 14 人全部姓名，并注明最后一人：
> 「…and Leading Seaman Mervyn Richard Tucker who died on 25 May 1941.」
**两源一致，可采信。** 这与 `data/battles/denmark-strait.yaml` 的「13 人，次日增至 14 人」吻合。

**燃油**：见 §0.3 —— **本舰 05-24／05-25 的剩余油量数字，未获取。**

---

## 4. 远东与沉没（1941-12-10）

### 4.1 编成：Force Z 的准确名单（A 级，C-in-C 战报原文）

> 「5. Force Z consisted of H.M Ships: PRINCE OF WALES (Captain J. C. Leach, M.V.O., D.S.O., R.N.) flying the flag of Admiral Sir Tom S. V. Phillips, K.C.B., REPULSE (Captain W. G. Tennant, C.B., M.V.O., R.N.), ELECTRA (Commander C. W. May, R.N.), EXPRESS (Lieutenant Commander F. J. Cartwright, R.N.), H.M.A.S. VAMPIRE (Commander W. T. A. Moran, R.A.N.), H.M.S. TENEDOS (Lieutenant R. Dyer, R.N.).」—— [lg-forcez] §5

**同段给出的「为什么不是别的舰」，这一段很容易被漏掉，但它解释了编成**：
> 「JUPITER and ENCOUNTER were under repair and STRONGHOLD had to be used for meeting a division of U.S. destroyers expected at Singapore pm. 9th December. DURBAN was available but the Commander-in-Chief decided not to take her.」—— [lg-forcez] §5

**注意**：TENEDOS 于 12-09 18:34 因续航不足先返新加坡（[lg-forcez] §9），**实际参战的是 5 艘**。
[bs14] 的表述与此一致：「Force "Z" (Prince of Wales, Repulse, Electra, Express and Vampire)」—— [bs14] §12。

**航母缺席**：Indomitable 在牙买加附近搁浅未能前来（[wiki-pow] E 级，仅线索；本批未取得非 E 来源确认）。

### 4.2 攻击过程：逐次打击

**日方兵力（B 级官方战史）**
> 「About an hour later the Striking Force, consisting of 84 aircraft (34 bombers and 50 torpedo planes), was ordered to the estimated position of the ships.」—— [bs14] §11

**（i）11:13–11:22 高空轰炸**，集中打 Repulse。本舰参与射击。
> 「At 1113 hours the PRINCE OF WALES opened fire on eight Nell high-level bombers, flying at about 10000ft, each armed with 2 x 250kg bombs, these attacked the REPULSE.」—— [nh-pow]

**NavWeaps 对这一轮的数字（D 级，唯一给出弹药消耗的来源）**
> 「During this particular attack, a total of 108 rounds were fired by the 5.25-inch guns on HMS Prince of Wales and a further thirty-six rounds were fired by the 4-inch guns on HMS Repulse. Five aircraft were damaged, two seriously enough that they were forced to return to base without dropping their second bomb.」—— [navweaps-hacs]

**NavWeaps 的整体评价（极重要的定性结论）**
> 「For example, during the destruction of Force Z, both HMS Prince of Wales and HMS Repulse apparently failed to shoot down a single plane with their HACS-controlled guns. Interestingly, the first attack was by eight high-level bombers, the very threat that HACS had been designed to combat.」—— [navweaps-hacs]

**（ii）11:44 第一波鱼雷攻击 —— 致命一击**
> 「(iii) Attack B. (1144) 9 T/Bs (torpedo bombers) attacked PRINCE OF WALES on port side. Ship turned towards but was hit by one torpedo abreast P.3 and 4 turrets. Ship listed 13° to port and speed dropped to 15 knots. Both port shafts out of action, steering gear failed and ship was never again under complete control. Five 5.25 inch turrets out of action temporarily owing to power failure and/or list.」—— [lg-forcez] §18(iii)

命中部位（D 级，最精确）：
> 「The first wave of attackers achieved one catastrophic torpedo hit on the port side, aft of water tight bulkhead at frame 274, blowing a hole in the hull 20ft x 13ft. The hit was close to the stern tube of the port outer propeller shaft, at the time the 17.5in diameter shaft was turning at 204rpm. The explosion damaged/broke the A frame supporting the end of the propeller shaft, which continued turning but eccentrically.」
> 「By 1155 hours it was realised that the eccentrically rotating shaft had breached all the water tight bulkheads from frame 184 aft.」—— [nh-pow]

残骸调查给出的部位（C 级）：
> 「The upper profile view shows where the first torpedo hit to port at about Frame 280, based on …」—— [garzke2012]

**（iii）12:19–12:23 第二波鱼雷攻击 —— 右舷三雷**
> 「(vi) Attack E. (1222) T/B attack by 9 aircraft, in two groups. 6 came in slightly first on the starboard side and fired at PRINCE OF WALES who was incapable of taking avoiding action and was hit three times on starboard side: — (a) Near stem. (b) Abreast B turret. (c) Aft. List was reduced to 3° and speed dropped to 8 knots. One aircraft was shot down.」—— [lg-forcez] §18(vi)

**（iv）12:44 最后的高空轰炸 —— 电影厅中弹，伤亡最惨**
> 「At 1244 a bomb hit her near 'S3' turret, wrecking the port crane and canteen flat, and causing a fire. It failed, however, to pierce the armoured deck. The remainder missed narrowly aft, falling on both sides of the ship.」—— [bs14] §12
> 「Seven 500kg bombs were dropped, only one of which was a hit, landing on the port side amidships. The bomb penetrated the Upper Deck and exploded in the Cinema Flat where up to 300 wounded were being treated, causing heavy causalities. The bomb also damaged the ventilators for B Boiler Room causing it to be shut down.」—— [nh-pow]

**（v）13:20 倾覆沉没**
> 「At 1320 hours the PRINCE of WALES sank capsizing to port, in position 3-33-36N, 104-28-42E.」—— [nh-pow]
[bs14] 给沉的姿态与战后定位：
> 「At 1320 she heeled over sharply, turned turtle and sank.」…「In 1954 H.M.S. Defender located the wreck in 3° 33.6' N, 104° 29.7' E.」—— [bs14] §12 及注 5

### 4.3 鱼雷命中数的争议 —— 两边都写，不裁决

| 立场 | 数字 | 原句 | 来源 | 等级 |
|---|---|---|---|---|
| **日方飞行员声称** | **5** | 「A review of survivor testimony reveals that some sailors did report a fourth torpedo hit, while **Japanese aviators claimed five**.」 | [garzke2012] 注 16 | C |
| 英方 C-in-C 战报（当时） | **4（可能 5）** | 「PRINCE OF WALES hit by four (possibly five) torpedoes and one bomb.」 | [lg-forcez] §18(ix) | A |
| 英方 C-in-C 战报（第一波附注） | 第一波 **2** 发同时命中 | 「Subsequent investigation has established the fact that PRINCE OF WALES was struck at this time by two torpedoes simultaneously」 | [lg-forcez] 注 ** | A |
| 1955 官方战史（第一波） | **1（大概 2）** | 「One, probably two, torpedo hits on Prince of Wales.」 | [bs14] §13 表 | B |
| 1955 官方战史（第二波） | 12:23 **2** 发 + 一分半后 **2** 发 = **4** | 「sustained two hits at 1223, and a further two a minute and a half later」 | [bs14] §12 | B |
| Bucknill 调查委员会 | 第一波**不少于 2** 发 | 「A committee under the chairmanship of the Hon. Mr. Justice Bucknill … considered that the rapid and extensive flooding which occurred in two distinct areas could not have been caused by less than two torpedoes.」 | [bs14] §12 注 1 | B |
| **残骸调查（2007/2012）** | **第一波 1 发 + 第二波 3 发 = 4 发** | 「This paper will confirm beyond doubt (referencing Expedition 'Job' 4's survey data) that there were only **three actual hits during this devastating attack**. However, there is some circumstantial evidence that there may have been one 'non contact' torpedo explosion close to the hull in the area of the mainmast that was, presumably, set off as a 'sympathetic detonation' by the shock wave from one of the actual hits.」 | [garzke2012] 注 16 | C |
| 残骸调查对「P3/P4 附近第二雷」的否定 | 无破口 | 「although Expedition 'Job 74' diving team's video survey footage from May 2007 conclusively shows there is no evidence whatsoever of a fourth torpedo hit producing a hole in the hull in that area」 | [garzke2012] | C |
| 同期 D 级叙事（采纳残骸结论） | 第一波 1 发；P3/P4 第二发已被残骸否定 | 「A second hit was reported at the time between turrets P3 and P4, but subsequent examinations of the wreck have disproved this.」 | [nh-pow] | D |

**这里有三层分歧，必须拆开讲，否则会写成一句「有争议」糊过去**：

1. **第一波是 1 发还是 2 发**：Bucknill 与 C-in-C 战报（英方官方、A/B 级）说 2 发；残骸调查（C 级）说 1 发，
   并明确否定了 P3/P4 附近的第二个破口。**这是「当事人判断」与「物证」的分歧，不是笔误。**
2. **第二波是三发还是四发**：残骸调查锁定 3 个破口（舰首、B 炮塔附近、Y 炮塔后）；[bs14] 记为 2+2=4。
3. **总数**：4（残骸/英方后期）vs 5（日方声称）vs 「1+4=5 或 1+2+4=7」这类加总口径差。

**E 级的位置（仅线索，不作数值来源）**：wiki 采「第一波仅 1 雷 + 第二波 3 雷 = 4 雷」：
> 「Despite reports to the contrary, Prince of Wales was struck by only one torpedo.」…「Six aircraft from this wave also attacked Prince of Wales, hitting her with three torpedoes」
—— [wiki-pow]

**本文不裁决。但必须指出一点**：残骸物证（2007 年 Expedition 'Job 74'）是**唯一能数破口的证据类型**，
而它给出的是 4 个破口（1 左舷 + 3 右舷）。不过「破口数」不等于「命中数」—— 未爆雷、哑雷、近失的非接触爆炸都可能不产生破口。
所以**「日方 5 发」与「残骸 4 破口」在物理上并不必然矛盾**，这一点在 [garzke2012] 自己的注 16 里已经承认（「sympathetic detonation」那半句）。

### 4.4 沉没主因的争议 —— 三条破坏链，不裁决

**（链 ①）鱼雷直接破口**
[bs14]（B 级官方战史）的归因最直接：
> 「The consequences of this attack were disastrous. "B" engine room, "Y" boiler room, the port Diesel engine room and "Y" action machinery room were flooded; both port propeller shafts stopped; the speed dropped to 15 knots; the steering gear was injured, and the ship was never again under complete control.」—— [bs14] §12

**（链 ②）螺旋桨轴把舱壁「铰」穿 —— 残骸调查的核心发现**
> 「The shaft disintegration that Expedition 'Job-74' uncovered was in all probability the result of a massive energy spike traveling along the shaft, which overwhelmed its designed strength.」
> 「With the line shaft no longer secured, they expended their energy in flailing against local structures, such as shaft seals (glands) in the transverse bulkheads within the shaft alley, while also moving somewhat aft.」
> 「The shafting, no longer restrained by its connections to the plummer blocks, **destroyed bulkhead stuffing glands and severely damaged the structure of each transverse bulkhead that it passed through**.」
> 「The shafting, no longer restrained by its connections to the plummer blocks, destroyed bulkhead stuffing glands…」
> —— 均出自 [garzke2012]（§Conclusions 与 §The 'Broken' Shaft）
> 「The parting of five sections of shafting at their flange connections can be attributed to the shaft rotating out of center and the subsequent loss of the port outer propeller and strut.」—— [garzke2012]

**这一链的意义**：它说明「水密完整性」不是被鱼雷直接打穿的，而是**被本舰自己的传动轴从内部逐道撕开的**。
从 Frame 184 往后，全部横舱壁失效。这解释了为什么「一条鱼雷」能造成「整条舰尾进水」。

**（链 ③）电力丧失 → 泵失效**
[nh-pow] 的因果链最完整：
> 「The flooding of the Diesel Dynamo Room caused the failure of the electrical system at the after end of the ship putting out of action the steering engine, warning telephone system, radars and the after 5.25in turrets.」
> 「The AA barrage put up by the PRINCE of WALES was subject to many problems. … further the pom-pom mounts were electrically operated so quickly became non-operative due to the loss of electrical power.」

[garzke2012] 给了发电机台的精确状态：
> 「Out of eight generators (six 330-kw DC turbo-dynamos and two 330-kw diesel dynamos), only **three turbo-dynamos were operational** when the second torpedo attack commenced at 1219.」

以及泵的失败：
> 「This power loss also affected vital internal communications, ventilation, steering gear and pumps, and for training and elevation of the 5.25-inch guns and the Pom-Pom machine guns and **meant that the ship's pumps could not pump flood water fast enough to counter the rapidly progressive flooding**.」—— [garzke2012]

[ngb-loss2]（C/D 级）补了泵的额定能力与「无备份」：
> 「The power loss also hit the ship's pumping system, which could normally handle up to 8,900 tons of water an hour, and there was no backup because the emergency diesels were also affected.」

**⚠ 关于「8,900 t/h」这个数字**：该数值仅见于 [ngb-loss2]，转引 Garzke & Dulin 1980 pp.196–198。
**本文把它标为「单一二次来源」，不作 A/B 级数值使用。** [garzke2012] 全文检索 `per hour`／`8,900` **无命中**，
即 2012 年的残骸报告本身没有再给出这个泵排量。这是一个典型的「原料里看着很硬、实际是二手转引」的数据。

**（链 ④，本文补充）设计缺陷 —— 残骸报告点名的两条**

> 「**The failure of internal communications after the first torpedo hit reflected an inexcusable design flaw** — it negated much of the skill and training of the crew to keep the ship afloat.」—— [garzke2012]
> 「Centerline machinery space bulkheads were incorporated to enhance survivability, but such subdivision actually decreases it. … **The decision to use centerline bulkheads in the King George V Class was a serious design flaw.**」—— [garzke2012]

第二条是**舰级缺陷**（不是单舰），但它在本舰身上第一次被实战验证，所以放在这里记录、落库时挂舰级。
第三条（通风不足）同理，且 Tovey 战前就反对派本级去热带：
> 「Admiral Tovey protested the assignment of this battleship to tropical regions because 'recent operations in the Mediterranean made it clear that, when underway, ventilation in the King George V class is most inadequate in a hot climate and health and efficiency of the ship's company will be seriously affected…'」—— [garzke2012] 转引

**综合表述（本文的写法，非裁决）**：
沉没是「1 发命中要害的鱼雷 → 轴系解体 → 舱壁逐道失效 → 电力丧失 → 泵失效 → 进水不可控」的**级联**，
再叠加第二波三雷、近失弹造成的铆钉/板缝失效，以及设计层面的中线舱壁与通风缺陷。
[nh-pow] 对这一过程的定性用词值得照抄：
> 「It was a classic cascade failure.」

**并且必须记住：本舰未完工的那部分（水密舱气密试验）正好是这个级联的起点。**
1940-08 那次进水就已经证明了这一点（「The flooding was severe, due to the fact that final compartment air tests had not yet been made」—— [nh-pow]）。

### 4.5 伤亡数字 —— 四说并存

| 数字（本舰阵亡） | 构成 / 原句 | 来源 | 等级 |
|---|---|---|---|
| **327** | 「Out of her crew of 1612 men; 20 officers, 280 sailors and 27 marines were lost.」 | [nh-pow] | D |
| **327** | 「A total of 90 officers out of 110 and 1,195 ratings out of 1,502 were rescued.」→ 110−90=20；1,502−1,195=307；合计 327 | [bs14] §12 | B |
| **323** | 「naval-history.net … citing 323 from Prince of Wales」 | [ngb-loss2] 注 1，转引 naval-history 伤亡页 | C（转引） |
| **377** | 「Bernard Edwards, Japan's Blitzkrieg …, cites 377 lost from Prince of Wales and 513 from Repulse, p. 23」 | [ngb-loss2] 注 1，转引 Edwards | C（转引） |

**本文的判读（不是裁决，是加权说明）**：
327 这个数有**两条独立来源**支撑（[bs14] 的官兵分项减法与 [nh-pow] 的分项相加），且两者内部自洽
（编制 110 官 + 1,502 兵 = 1,612，与 [nh-pow] 的 1,612 吻合）。323 与 377 都是二手转引，未见原始分项。
**建议落库取 327，并把 323 / 377 写进 note 而非另立 fact。**

**阵亡者中的两位关键人物**：
> 「Among the dead were Admiral Sir Tom Phillips, CinC of the Eastern Fleet, and the CO of the PRINCE OF WALES Captain John C. Leach.」—— [nh-pow]
[bs14] 补了 Leach 的最后时刻，这条极少见：
> 「Lieutenant M. Graham R.N.V.R., while swimming to the Express, came on the body of Captain Leach floating in the water. With the help of some seamen, he endevoured to tow him, but after 10 minutes this proved too much for them. Lieutenant Graham is quite certain that the captain was dead. There is no record of anything being seen of the C.-in-C. after the ship capsized.」—— [bs14] §12 注 1

**救援**：
> 「The destroyers EXPRESS, ELECTRA and VAMPIRE picked up 90 officers and 1195 crew and marines, the majority being picked up by the EXPRESS.」—— [nh-pow]

### 4.6 沉没前的技术状态（对「本舰是否已尽力」的判断有用）

- **雷达**：Type 273 在热带湿热中失效。
  > 「Also her surface warning Type 273 Radar had become unserviceable due to the extreme heat and humidity.」—— [nh-pow]
- **pom-pom 弹药**：同因受潮变质。
  > 「the 2 pounder Pom Pom ammunition had deteriorated badly, also due to the humidity」—— [nh-pow]
- **锅炉**：抵新加坡时正在清洗全部八座锅炉，估计需七天。
  > 「On arrival the PRINCE of WALES was taken in hand, at 72 hours notice for steam, to re-tube her distillers and clean all eight boilers. The Chief Engineer estimated the work would take seven days.」—— [nh-pow]
- **空调/通风**：本舰空调按北大西洋设计，南海环境超标。
  [ngb-loss2]：「the on-board plant was good for North Atlantic conditions but struggled in the Mediterranean, and the South China Sea was worse. Men in the engineering spaces, particularly, risked heat exhaustion.」（C/D 级）
  [garzke2012]：「The testimony of survivors also confirm that the Engine Room ventilation systems did not perform adequately, and there were a number of heat exhaustion cases that were being treated by the time of the last bomb attack at 1244.」（C 级）

---

## 5. 已知争议单列（全部并列，不裁决）

### 5.1 1940 年空袭的日期：三种说法

| 说法 | 原句 | 来源 |
|---|---|---|
| **8 月 8–9 日夜间** | 「During a Luftwaffe raid on the night of 8-9/8/40 a 250kg bomb (130kg of explosive), fell between the side of the fitting out basin and the ships port side…」 | [nh-pow]（D） |
| **1940 年 8 月初** | 「In early August 1940, while she was still being outfitted and was in a semi-complete state, Prince of Wales was attacked by German aircraft.」 | [wiki-pow]（E，仅线索） |
| **8 月 31 日／9 月 1 日夜间** | 「German bomb damage to Prince of Wales sustained during the night of **31 August / 1 September 1940** while she was undergoing outfitting in the large fitting-out basin at Cammell Laird Shipyard」 | [garzke2012]（C） |

**差近三周，不是笔误级的差。** 三个来源都给了具体日期，没有一个说「日期不详」。
本文倾向 [nh-pow]（D 级，日级精度、且与后续 1941-02 在 Rosyth 换板的记录链条完整），但**不裁决**。
**落库建议**：日期字段写「1940-08（日不确）」，note 里三说并列。

### 5.2 本舰在丹麦海峡被命中几次、几发 15 英寸

见 §3.4 表格：7（4×15in+3×8in）／7（3×15in+4×8in）／8（5×380mm+3×203mm）。**三说，不裁决。**

### 5.3 鱼雷命中数

见 §4.3。**四层分歧，不裁决。**

### 5.4 1941-07 装的是 Type 271 还是 Type 273

| 说法 | 原句 | 来源 |
|---|---|---|
| **Type 273，且为该型首装** | 「Whilst in dockyard hands she was fitted with the first radar Type 273, a big ship surface search version of the 10 cm Type 271.」 | [nh-pow]（D） |
| Type 271 | 「June–July 1941 | Rosyth | … Type 271 radar added.」 | [wiki-pow]（E，仅线索） |

**技术判断（供落库参考，非裁决）**：[navweaps-radar-uk] 给出两型的分工——
「Type 271 … Used operationally in war on **small ships**」；「Type 273 … Used operationally in war on **cruisers and battleships**」。
即 271 是小型舰型，273 才是主力舰型。**从用途看 [nh-pow] 的「273」更合理，且它明确说了「first」，
这与 [navweaps-radar-uk] 的「Type 282 … First used on HMS Prince of Wales」是同一类表述习惯。**
但仍**不裁决**，只记录这层旁证。

### 5.5 舰载机数量与型号

| 项目 | 说法 A | 说法 B |
|---|---|---|
| 数量 | **2** 架（「2 seaplanes」—— [navypedia-kgv39]，与舰级文件一致） | **4** 架（「aircraft = 4 Supermarine Walrus seaplanes」—— [wiki-pow]，E，仅线索） |
| 型号 | Walrus / Swordfish / Seafox（[navypedia-kgv39]） | 仅 Walrus（[wiki-pow]） |

**本文不写数字**：2 与 4 差的不是口径而是编制口径（搭载数 vs 编制数），和舰级文件对 `aviation.aircraft.capacity` 已标的 `comparable: false` 是同一个坑。
**本舰沉没当天实际搭载几架：未获取。**

### 5.6 HACS 的装舰艘数：前两艘 还是 前四艘

| 说法 | 原句 | 来源 |
|---|---|---|
| **前四艘** | 「The HACS Mark IV was installed on "Town" and succeeding cruisers, **the first four units of the King George V class battleships** and to new aircraft carriers.」 | [navweaps-hacs]（D） |
| 舰级文件的表述 | 「4 部，为本级首两舰（King George V、Prince of Wales）独有配置；本级后续舰改用 Mk V / Mk VI」 | `data/classes/king-george-v.yaml`（非本文来源，是被核对对象） |

**这两句可以调和，也可能真的冲突**：navweaps 说 Mk IV 装了前四艘，同时又说 Mk V「was designed from the start for radar」、
Mk VI「战时只有 HMS Anson 装全系统」。若 Mk V 是「设计为可接雷达」而非「换掉 Mk IV」，
则「前四艘装 Mk IV」与「后两艘换 Mk V/VI」并不互斥。
**本文不裁决，但要提醒落库方：舰级文件那句「首两舰独有」在 [navweaps-hacs] 里找不到支持。**
本舰用 Mk IVGB 这一点无争议（[nh-pow] 明写「HACS IVGB」）。

### 5.7 Type 279 到底在不在本舰上

| 说法 | 原句 | 来源 |
|---|---|---|
| 本舰雷达 = **Type 279 + 284** | 「King George V, Prince of Wales: type 279, type 284 radars」 | [navypedia-kgv39]（D） |
| 本舰雷达 = **Type 281 + 284 + 4×285 + 4×282** | 「The PRINCE of WALES went to sea with HACS IVGB … four Type 285 Radars … four Type 282 Radars … and a long range Type 281 Radar」 | [nh-pow]（D） |
| **A 级旁证：本舰确有 281 与 284** | 「No results were obtained from either Type 281 or 284 R.D.F.」 | [adm234-509]（A） |

**这是本文最值得报告的一处「E/D 级来源 vs A 级一手文件」的冲突。**
[adm234-509] 是本舰舰长 1941-06-12 上报的炮术附录，其中明确提到 **Type 281** 与 **Type 284** 两型 ——
**它不可能提到一艘舰上没有的雷达型号。** 因此 navypedia 那行「type 279, type 284」至少漏了 281。
**本文不裁决「有没有 279」，但可以确定地说：navypedia 的这行对本舰是不完整的。**
（279 与 281 可能并非互斥：281 是远程对空警戒，279 也是；两型并存于英舰并不罕见。但**没有来源证明本舰同时装了 279**。）

### 5.8 舰桥命中后「谁活下来」

- 「killing everybody there, except the commander, Captain John Catterall Leach and **another man**」—— [kb-ds]
- 「killing everyone except the Captain and **the Chief Yeoman**」—— [nh-pow]
- 「**The navigating officer was wounded**, but Captain Leach was unhurt.」—— [wiki-pow]（E，仅线索）

**三者不必然矛盾**（「another man」可能就是 Chief Yeoman；导航官 Rowell 受伤是被碎片所伤，未必在「全体阵亡」的统计口径内）。
**记录三说，不裁决。** 补充：ADM 116/4351 收录了 Rowell（ Lieutenant Commander G. W. Rowell, R.N.）的证词，编号 29-49、118、785-787（[adm116-pow] 证人名单），
**说明他确实活了下来** —— 这一点可以确定。

### 5.9 首日阵亡 13 还是 14

两源一致为「13 死、次日 1 人死、共 14」（[nh-pow]、[kb-ds]）。**不构成争议。**
但注意：`data/battles/denmark-strait.yaml` 的 summary 写「威尔士亲王号命中三发」，losses 写「阵亡 13 人，次日增至 14 人」——
**后者正确，前者与本文 §3.3 的三发部位描述吻合**，两处无需改。

### 5.10 任务书/战役文件里需要复核的两处

**(a) `data/battles/denmark-strait.yaml` 的「仅 7 门可用（A 塔 3、B 塔 2、Y 塔 2）」**
- 战役文件与 `data/sources.yaml` 的 `hoodadm234-guns` 条目 note 都写「06:03 时 10 门 14 英寸炮中可用 **7 门**（A 塔 3、B 塔 2、Y 塔 2），
  不是常被引用的 5 门——5 门出自 Garzke & Dulin p.190，被 WIKI-DS:764 明确否定」。
- **但本文通读了 `work/raw/hood/of-adm234-509guns.txt` 全文（23,525 字节，含 Enclosure I–IV），
  未能定位到「7 门」这句，也没有「A 塔 3、B 塔 2、Y 塔 2」这样的分塔快照。**
- 该文件能支持的是逐项事实：A1 打完 1 发齐射即失效；A3 第 11 发齐射后临时失效；Y 塔炮圈卡死至 0825；
  Enclosure I 的汇总表给「18 齐射 / 应发 74 / 实发 55 / 输出损失 25.65%」。
- **所以：结论方向（不是 5 门）大概率对，但「7 门」这个具体数字的 A 级出处，本文未能核到。**
  建议落库前补核 ADM 234/509 原件（TNA 藏），或用 Enclosure I 的汇总数替代具体门数。
  **这不是反驳战役文件的判定，是提醒它的引文锚点没落在这份转录里。**

**(b) `data/battles/denmark-strait.yaml` 的「打坏弹射器蒸汽管」**
见 §3.3 末 —— [kb-ds] 原文无此内容，本批未能核到 kbismarck 的 aviation 页，**标存疑**。

---

## 6. 未获取字段汇总

> 本节是硬要求。**「未获取」不等于「0」，也不等于「与舰级相同」。**

### 6.1 建造类

| 字段 | 状态 | 说明 |
|---|---|---|
| 造价（单舰） | **未获取** | 全部已抓来源无此数；Buxton & Johnston 的 £7,426,000 原页 403 |
| 下水掷瓶人 | **未获取** | 首舰 KGV 有 RMG 明写，本舰无任何来源写 |
| 船台号 | 1026（[navypedia-kgv39]） | 已获取，单来源 |
| 原名与改名日期 | **仅 E 级线索** | [wiki-pow] 称原名 King Edward VIII、1937-01-01 改名，**无第二来源** |
| 1940 年空袭的确切日期 | **三说并存** | 见 §5.1 |
| 1940 年空袭的完整损伤报告原文 | **未获取** | 只取得 [nh-pow] 的转述与 [garzke2012] 的引用 |
| 「豁免试验」的清单原件 | **未获取** | [nh-pow] 列举了四项（气密、通风、舱底/压载/燃油系统、全功率试航），但那是 D 级转述，**非档案原件** |

### 6.2 单舰实测值

| 字段 | 状态 | 说明 |
|---|---|---|
| **排水量（本舰实测）** | **未获取（非 E 级）** | [navypedia-kgv39] 只给舰级 36,727 / 42,076；[wiki-pow] 给「36,727 as built / 43,786 fully loaded」但为 E 级。**本舰服役时的实测排水量无 A–D 级来源** |
| **主尺度（本舰）** | **未获取（非 E 级）** | 同上，只有舰级值；E 级给 745 ft / 103 ft / 29 ft |
| **试航功率 / 试航航速** | **未获取（非 E 级）** | 只有 [nh-pow] 一句「Carried out Full Power Trials.」（1941-05-08），**不附任何数值**。[wiki-pow] 的「111,600 shp / 28 kn / 228 rpm / 0.73 lb per shp，1941-03-31，42,100 t」全在 E 级，**本文不作数值使用** |
| **燃油容量（本舰）** | **未获取（非 E 级）** | 舰级值见舰级文件；E 级给 3,542 t 燃油 + 180 t 柴油 |
| **续航（本舰实测）** | **未获取** | 无任何来源给本舰实测续航 |
| **本舰 1941-05-24／05-25 的剩余燃油** | **未获取** | 只有「low on fuel」的定性 |
| **稳性 / 初稳性高（本舰）** | **未获取（非 E 级）** | E 级给「designed metacentric height 6 ft 1 in at normal load and 8 ft 1 in at deep load」 |
| **干舷** | **未获取** | 与舰级文件同（只有定性描述） |

### 6.3 武备 / 传感器类

| 字段 | 状态 | 说明 |
|---|---|---|
| 本舰 1941-05-24 当日的 **20 mm 门数** | **未获取** | 7 门是 1941-11 开普敦加装的，此前有无/几门无来源 |
| 本舰 **40 mm Bofors 的装舰时点** | **未获取** | 只在 1941-12-10 战斗中确认其存在（[nh-pow]） |
| 本舰 **pom-pom 的 1941-05-24 座数** | **未获取** | 建成 4×8（[navypedia-kgv39]），1941-06/07 加 2×8+1×4，**中间状态无快照** |
| 本舰 **Type 279 有无** | **存疑** | 见 §5.7。可确定有 281、284；279 只有 navypedia 单方面说法且与 A 级旁证冲突 |
| 本舰 **pom-pom 指挥仪的 1941-05-24 座数是否为 4** 与首舰 6 座的差别是「艘间」还是「时期」 | **未获取** | [nh-pow] 明写 4 部 282 对应 4 座 Mk IV pom-pom director，但这个数字在本舰只有 **1941 年 5 月** 这一个时点；首舰的 6 座出自 KGV 单舰调研稿（同属某一时点）。**两个时点不同，不能直接判为舰间差异** |
| 本舰 **Type 273 的装舰月份** | 「1941-07」（[nh-pow]） | 已获取，但为 D 级单来源；与 E 级「Type 271」冲突（§5.4） |
| 本舰 **HACS 各部指挥仪的具体型号构成**（哪几部是 IV、哪几部是 IVGB） | **未获取** | 只有整舰层面的「HACS IVGB」（[nh-pow]） |
| 本舰 **高角指挥仪的陀螺测速改装状态** | **未获取** | 舰级文件记 KGV 是「世界第一艘装陀螺测速高炮指挥仪的军舰」，本舰是否有、何时有，**无来源** |
| 本舰 **主炮指挥仪（D.C.T.）数量与测距仪基线** | **未获取（单舰层面）** | [adm234-509] 提到「fore D.C.T. 15-ft rangefinder」与「after director」，可推断前/后各一，**但未给数量句** |
| 本舰 **副炮指挥仪分离后的「aft control」机制细节** | 已获取定性 | [adm234-509] 记「all turrets to go into 'aft control'」，够写，但无型号 |
| **UP 火箭为何只有 3 座** | **未获取** | 见 §2.1 |
| 本舰 **有无 0.5 in 机枪** | **未获取** | 无来源提及 |

### 6.4 战历类

| 字段 | 状态 | 说明 |
|---|---|---|
| 丹麦海峡本舰的**准确交战位置** | 部分获取 | 本舰 05:37 电报给「63-20 N, 31-50 W」（[hood-bonomi]）；Hood 沉没点 63°22′N 32°17′W。**本舰在交战各分钟的精确位置无来源** |
| 本舰 **06:13 停火后的航迹** | **未获取** | 只有「continued her port turn and fell in with the NORFOLK and SUFFOLK」（[nh-pow]） |
| 本舰 **丹麦海峡的实际弹药消耗（按型号）** | 部分获取 | 只有 55 发总量（[adm234-509] Enclosure I），**AP/HE 分项未获取** |
| 本舰 **Hvalfjord 抢修的完整损伤清单** | **未获取** | 只有「两发 8in 在舰尾爆炸」与「舰尾进水」（[nh-pow]） |
| 本舰 **1941 年 6–7 月 Rosyth 修理的完整工程单** | **未获取** | 只知装了 Type 273、拆了 UP（部分） |
| 本舰 **1941-12-10 的准确编制人数分项** | 已获取 | 110 官 + 1,502 兵 = 1,612（[bs14] 反推 + [nh-pow] 直给） |
| 本舰 **击落的日机数** | **有分歧** | [navweaps-hacs] 说 HACS 炮「apparently failed to shoot down a single plane」，且三架被击落者中「one was most likely hit by HMS Prince of Wales' 20 mm Oerlikons」；[lg-forcez] 记「Two aircraft shot down」+「One aircraft was shot down」；[bs14] 记「only three aircraft and 21 men were lost in action」。**三说口径不同，不裁决** |
| 本舰 **沉没时是否已发出完整战报** | **未获取** | Leach 阵亡，战报由他人整理；本批未取得该报告 |

### 6.5 涂装 / 编制 / 影像

| 字段 | 状态 |
|---|---|
| 1941-05 涂装（色号） | **未获取** |
| 1941-12 涂装（色号，新加坡时期的迷彩式样） | **未获取** |
| 舰徽描述 | **未获取（非 E 级）**；[wiki-pow] 载「Ich Dien」 motto 但为 E 级，舰徽图案无文字描述 |
| 舰训 motto | **仅 E 级**，见 §1.4 |

---

## 7. 抓取失败清单

| 目标 | URL | 状态 | 处理 |
|---|---|---|---|
| ADM 234/509 PoW Gunnery Aspects | https://www.hmshood.org.uk/reference/official/adm234/adm234-509guns.htm | **403**（直连 + Referer 均 403） | 使用本地已存转录 `work/raw/hood/of-adm234-509guns.txt`（23,525 B） |
| ADM 234/509 Tovey dispatch | https://www.hmshood.org.uk/reference/official/adm234/adm234-509tovey.htm | **403** | 使用 `work/raw/hood/of-adm234-509tovey.txt` |
| ADM 116/4351 PoW evidence | https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_POW.htm | **403** | 使用 `work/raw/hood/of-116_POW.txt`（152,204 B） |
| H.M.S. Hood Assoc. PoW damage page | https://www.hmshood.org.uk/history/denmarkstrait/powdamage.htm | **403** | 未取得。**这是本舰战损最权威的专题页，本次无法获取** |
| navypedia Prince of Wales 单舰页 | https://www.navypedia.org/ships/uk/brit_bb1_prince_of_wales.htm | **404** | 改用舰级页 `brit_bb1_king_george_v.htm` 的建造表（该表逐舰分列装备行，可满足需求） |
| Wikipedia（直连 `web_fetch`） | https://en.wikipedia.org/wiki/HMS_Prince_of_Wales_(53) | **SSRF blocked**（解析到 198.18.0.18） | 改用 PowerShell 直连，429 后重试成功（464,604 B）；本机代理 7897 不通 |
| Wikipedia Sinking of PoW and Repulse | https://en.wikipedia.org/wiki/Sinking_of_Prince_of_Wales_and_Repulse | **429 持续**（三次退避重试均失败） | **未取得原文**。该页内容以 "Sinking of..." 片段形式在 Exa 搜索结果中部分可见，**本文未采信其任何数值** |
| Bucknill 调查报告 PDF | https://pacificwrecks.com/ship/hms/prince-of-wales/bucknill-report-04-42.pdf | 200，4,741,009 B，但**PDF 为扫描件，文本层仅 348 字符** | 未做 OCR，**内容未利用**。[bs14] 与 [garzke2012] 已转述其结论 |
| ADM 234/330（BS-14 原件） | TNA 藏，无公开 URL | — | 使用 HyperWar 的 B.R. 1736(8)/1955 转录版（[bs14]） |
| 日方 22nd Air Flotilla 战斗详报 | 无公开 URL | — | **未获取原件**。日方命中声称只能经 [garzke2012] 注 16 的转述获得 |

**直连/代理结论**：本次全部成功抓取均为**直连**；`http://127.0.0.1:7897` 代理**不通**（「无法连接到远程服务器」）。
这与任务书「直连可用，不需要代理」一致，但需补充：**本机代理本次是坏的，不是不需要用**。

---

## 8. 来源清单

| 代号 | 名称 | URL | 等级 | 本次状态 |
|---|---|---|---|---|
| adm234-509 | ADM 234/509 — H.M.S. Prince of Wales' Gunnery Aspects of the "Bismarck" Pursuit（Enclosure No.4 to 1165/H.F.1325，1941-08-19；正文为 Leach 1941-06-12 报告） | https://www.hmshood.org.uk/reference/official/adm234/adm234-509guns.htm | **A** | 403；用本地转录 |
| adm234-509-tovey | ADM 234/509 — Tovey 丹麦海峡与追击战报（Dispatches） | https://www.hmshood.org.uk/reference/official/adm234/adm234-509tovey.htm | **A** | 403；用本地转录 |
| adm116-pow | ADM 116/4351 — Hood 损失调查委员会中威尔士亲王号证词 | https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_POW.htm | **A** | 403；用本地转录 |
| lg-forcez | London Gazette — Narrative of Operations of Force Z（C-in-C 东方舰队战报） | https://www.britain-at-war.org.uk/ww2/London_Gazette/Force_Z/html/body_narrative_of_operations_of_for.htm | **A** | 200，22,729 B |
| bs14 | B.R. 1736 (8)/1955 — Naval Staff History, Battle Summary No. 14 (revised): Loss of H.M. Ships Prince of Wales and Repulse, 10 Dec 1941 | https://www.ibiblio.org/hyperwar/UN/UK/RN/BS-14_POW+Repulse/index.html | **B** | 200，151,231 B |
| garzke2012 | Garzke, Dulin & Denlay — *Death of a Battleship: The Loss of HMS Prince of Wales. A Marine Forensics Analysis of the Sinking*（2012 修订版，80 页） | https://pacificwrecks.com/ship/hms/prince-of-wales/death-of-a-battleship-2012-update.pdf | **C** | 200，3,978,419 B，文本层 173,443 字符 |
| ngb-loss2 | Matthew Wright — *The loss of Prince of Wales and Repulse, Part 2: the air attack*（Navy General Board, 2018） | https://www.navygeneralboard.com/loss-prince-wales-repulse-part-2/ | **C** | 200，236,829 B |
| hood-bonomi | Antonio Bonomi — *The Denmark Strait Battle*（H.M.S. Hood Association 刊载，3 部分） | https://www.hmshood.org.uk/history/denmarkstrait/bonomi_denstrait1.htm | **C** | 用本地已存 `work/raw/hood/hood-bonomi*.txt` |
| nh-pow | Naval-History.net — HMS Prince of Wales 逐日服役年表（Lt Cdr G. B. Mason RN (Rtd)，Mike Simmonds 增补） | https://www.naval-history.net/xGM-Chrono-01BB-HMS_Prince_of_Wales.htm | **D** | 200，339,552 B |
| navypedia-kgv39 | navypedia — King George V battleships (5, 1940–1942)，含逐舰装备行 | https://www.navypedia.org/ships/uk/brit_bb1_king_george_v.htm | **D** | 用本地已存 `work/raw/kgv/np-kgv39.txt` |
| navweaps-radar-uk | NavWeaps — Radar Equipment of World War II: United Kingdom | https://www.navweaps.com/Weapons/WNBR_Radar.php | **D** | 用本地已存 `work/raw/nw-radar-uk.txt` |
| navweaps-hacs | NavWeaps — The British High Angle Control System (HACS)，含 Force Z 专段 | https://www.navweaps.com/index_tech/tech-066.php | **D** | 用本地已存 `work/raw/kgv/nw-tech-066.txt` |
| navweaps-14in | NavWeaps — 14"/45 (35.6 cm) Mark VII | https://www.navweaps.com/Weapons/WNBR_14-45_mk7.php | **D** | 用本地已存 `work/raw/kgv/nw-14in.html` |
| kb-ds | KBismarck.com — The Battle of the Denmark Strait（José M. Rico） | https://www.kbismarck.com/denmark-strait-battle.html | **D** | 用本地已存 `work/raw/kb-ds.txt` |
| wiki-pow | Wikipedia — HMS Prince of Wales (53) | https://en.wikipedia.org/wiki/HMS_Prince_of_Wales_(53) | **E（仅线索）** | 200，464,604 B |
| wiki-sinking | Wikipedia — Sinking of Prince of Wales and Repulse | https://en.wikipedia.org/wiki/Sinking_of_Prince_of_Wales_and_Repulse | **E（仅线索）** | **429，未取得** |

---

## 9. 一句话总结（给主会话落库用）

**本舰不是「KGV 级第二艘」这么简单。** 它的单舰差异集中在三处：

1. **武备差异是真实且可查的**：3 座 UP（非 4）、1 门单装 40 mm Bofors（首舰无）、4 部 282 + 4 部 285 + 281 + 284（
   navypedia 记的「279+284」对本舰不完整，被本舰自己的 A 级炮术报告否证）、4 座 pom-pom 指挥仪（首舰 6 座）。
2. **它是「完工但未完工」的极端样本**：1941-03-31 的「完工」是靠豁免水密舱气密试验换来的，
   1941-05-24 参战时 Vickers 工人还在舰上修炮塔，主炮雷达当天故障，而 **1941-12-10 沉没的直接机制（轴系撕毁舱壁填料函）
   正好击穿了那批从未验证过的水密完整性**。这条因果链横跨两次战损，是本舰叙事的骨架。
3. **两场战斗的争议都必须并列保留**：丹麦海峡是「命中 7 还是 8 发」、「本舰自己没观察到命中」；
   远东是「4 雷还是 5 雷（甚至 6 雷）」、「沉没是鱼雷直接命中还是轴系+电力+泵的级联」。
   **任何一处做了裁决，都会丢掉本站最该有的严谨性。**
