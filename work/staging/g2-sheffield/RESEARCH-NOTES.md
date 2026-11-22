# 调研底稿 —— HMS Sheffield（谢菲尔德号，C24）／Town class（城级）

> 调研：2026-11-22 · 组名 g2-sheffield
> 产出目录：`work/staging/g2-sheffield/`
> 本文件是立站之本那一条：**每条结论都在下面带英文原句 + URL**。
> 主体事实已落进 YAML，本文件记录的是「为什么是这个值」以及「哪里没拿到」。

---

## 0. 关于抓取方式的一个重要发现（会影响其他组）

任务书提示「navypedia 可能被 SSRF 拦」。本轮实测的实际情况**正好相反**：

| 站点 | web_fetch 工具 | Python urllib 直连 |
|---|---|---|
| `www.naval-history.net` | **SSRF 拦截**（解析到 198.18.0.99） | ✅ 正常，339 kB |
| `www.navweaps.com` | **SSRF 拦截**（198.18.0.50） | ✅ 正常 |
| `navypedia.org` | 未试（先用了 urllib） | ✅ 正常 |
| `uboat.net` | SSRF 拦截（198.18.0.101） | ✅ 正常 |
| `www.arctic.org.nz` | ✅ 正常 | ✅ 正常 |
| `www.hmshood.org.uk` | — | ❌ 403（带 Referer 也 403） |

**结论：本轮所有关键来源都是绕过 `web_fetch`、用 `urllib.request` + `User-Agent` 直连抓下来的。**
`web_fetch` 在本机把一批域名解析到 198.18.0.x（典型的本机代理/透明劫持网段），
于是被判成内网地址。凡是英国的舰艇专题站，都建议直接走 urllib。

编码陷阱：`naval-history.net` 是 **cp1252**，按 utf-8 解会出乱码。

`www.hmshood.org.uk` 的 Tovey 战报（`hmshood-tovey-dispatch`）本轮抓不到 403，
但该来源已在 `data/sources.yaml` 登记且 `work/raw/lb-*` 里已有本地副本，
故本组**直接引用已登记来源**，不重复抓。

---

## 1. 舰级划分：Town 不是一个设计，是三份

**结论：`town` 是通称，Sheffield 属 Southampton 子级。本轮只建一个 class 文件，
在 note 里把三个子级的差异说清楚，不为子级各建文件。**

navypedia 把城级拆成三个独立分级页，各自有独立的 Ships 表与技术数据：
- `SOUTHAMPTON light cruisers (5, 1937)`
- `GLOUCESTER light cruisers (3, 1938 - 1939)`
- `EDINBURGH light cruisers (2, 1939)`

三组的技术数据并排比对（全部来自 navypedia 各页 Technical data 段）：

| 项 | Southampton | Gloucester | Edinburgh |
|---|---|---|---|
| 标准排水量（navypedia 表头 t，实为长吨） | 9,100 | 9,400 | 10,550 |
| 全长 oa | 180.3 m | 180.3 m | 187.0 m |
| 宽 | 18.8 m | 19.0 m | 19.3 m |
| 深载吃水 | 6.20 m | 6.27 m | 6.48 m |
| 功率 | 75,000 hp | 82,500 hp | 80,000 hp |
| 航速 | 32 kn | 32.3 kn | 32.5 kn |
| 燃油 | 1,925–2,070 t | 1,950–2,100 t | 2,250 t |
| 炮塔装甲 | **25 mm** | 102 / 51 mm | 102 / 51 mm |
| 甲板 | 38–32 mm | 51–32 mm | 76–38 mm |
| 4 英寸副炮 | 4 座双联 | 4 座双联 | **6 座双联** |
| 编制 | 748 | 748 | 850 |

原句（Southampton 页）：
> "Protection in comparison with predecessors was increased: both a belt length
> and thickness. Thus the symbolical 25mm protection of turrets became an obvious
> discord."

原句（Gloucester 页）：
> "This lack was corrected on three ships of 2nd group which have received
> turrets with 102mm armour."

→ 也就是说 navypedia 自己就把「25 mm 炮塔」定性为第一组的缺陷，第二组修正了它。
这是「Sheffield 属第一组」最直接的一条证据，也解释了为什么不能把三组的值混在一个
class 文件里。

`arctic.org.nz` 也印证了舰名归属：
> "HMS Sheffield (C24) was one of the Southampton sub class of the Town class
> cruisers of the Royal Navy during the Second World War."

---

## 2. 主炮：炮身 Mk XXIII，炮座 Mark XXII —— 别混

这是本轮最容易写错的一处。正确配对：

**炮身** = `6"/50 (15.2 cm) BL Mark XXIII`（`navweaps-6in-50-mk23`）
**炮座** = `Mark XXII`（三联装，Southampton 与 Gloucester 两组用）

navweaps 装舰表原句：
> "Three-gun Turrets
>   Southampton ["Town"] (4) and Gloucester ["Later Town"] (4): Mark XXII
>   Edinburgh ["Modified Town"] (4), Fiji ("Colony") (4), Ceylon ("Improved
>   Colony") (3) and Swiftsure (3): Mark XXIII"

→ 也就是说 **Edinburgh 子级才用 Mark XXIII 炮座**。把 Sheffield 写成
「Mk XXIII 炮塔」是把炮身型号安到了炮座上。

炮座重量原句：
> "Southampton Mark XXII: 146 tons (148 mt)"
> "Gloucester Mark XXII: About 182 tons (185 mt)"

装甲差异原句（注 9b）：
> "For the Mark XXII, HMS Southampton had 1 inch (2.54 cm) (40 lbs.) armor all
> around while HMS Gloucester had 3.9 inch (10 cm) (160 lbs.) glacis plate armor
> with the rest 2 in (5.1 cm) (80 lbs.)."

→ 这是「25 mm 全周」的第二个独立来源，与 navypedia 的 "turrets: 25" 互为印证。

### 2.1 一处 navweaps 自身的单位错误（已在 fact note 里点明）

原页写：
> "Gun Length oa 309.8 in (7.869 m)"
> "Bore Length 309.7 in (7.620 m)"
> "Rifling Length 255.4 in (6.486 m)"

309.7 in 换算应为 **7.867 m**，与它自己标的 7.620 m 不符。
按 50 倍径算（6 in × 50 = 300 in = 7.620 m），7.620 m 才是膛线部长度。
故 `weapon.length.bore` 取 7.620 m 并降 B，note 里说明这是原页标注错误、
不是两说并列。

### 2.2 条约口径的坑（值得单独记一笔）

原页注 6a：
> "For Treaty compliance purposes, the "Town" class cruisers were rated at a
> magazine capacity of 150 rounds per gun, but they actually had space for 200
> rounds. All other classes, including the "Modified Town" class, were rated at
> 200 rounds per gun."

→ 对外申报 150、实际 200。`weapon.ammo_outfit` 存 200，note 里写清两套口径。

### 2.3 散布问题的公案（写进正文，不进 fact）

原页整段讲了 Southampton 级早期型的三联装散布问题：
> "The early Southampton ("Town") class cruisers experienced dispersion problems
> with spreads up to 700 yards (640 m) being recorded."

成因是药包小于药室、燃烧时上部压力高于下侧，导致炮管振动不均；高速摄影证实部分
弹丸在炮口已偏斜。对策是加延时电路错开中炮击发时间。这一段属于武器沿革，
本轮放在武器实体的 note 与底稿里，未做成字段（注册表没有对应字段）。

---

## 3. 排水量：navypedia 的表头是错的，不能直接当公吨用

navypedia Southampton 页写：
> "Displacement standard, t 9100"
> "Displacement full, t 11350 (later 12190)"

9,100 与 11,350 恰是皇家海军的长吨设计值（9,100 lt = 9,246 t）。
navypedia 把表头单位改成 t 但没换算数值。

**处理方式：不擅自换算，两条都登记原值并标 `comparable: false`，note 里写清。**
理由：换算了就成了我算的数，不是来源的数；而按公吨口径直接与其他舰对比又会系统性偏低。

---

## 4. 吃水：只有深载值，没有标准状态值

原句：
> "Draught, m 6.20 deep load (later 6.55)"

→ 落在 `dimensions.draught.max`，**不填 `draught.mean`**。
标准排水量状态的平均吃水本轮未获取，不推算。

---

## 5. 装甲体系：注册表没有 box 这一档

navypedia 原词是 box protection：
> "Armour, mm box protection to magazines: 114 - 25, belt: 114, bulkheads: 64,
> barbettes: 51 - 25, turrets: 25, deck: 38 - 32"

注册表 `protection.scheme` 的合法值只有
`all_or_nothing / incremental / turtle_back / other`。
**填 `other` 并在 note 里保留原词 box protection，不做强行归类。**
理由：英式巡洋舰的箱形防护与美式 all-or-nothing、德式 incremental 都不同类，
硬塞进 incremental 会掩盖它「装甲箱 + 两端 64 mm 舱壁」的实际结构。

---

## 6. 1941-05-26：一天之内的两件事，必须分开

### 6.1 上午到下午：被派出去跟踪 + 被自己人投雷

Admiralty War Diary（`kbismarck-admiralty-war-diary`，tier A）原句：
> "SHEFFIELD was detached to shadow; she made contact at 1740 and continued to
> shadow so throughout the day."
> "SHEFFIELD, detached from Force H was in touch with the enemy at 1747."
> "A striking force from ARK ROYAL left at 1500/B. It failed to make direct
> contact and was forced to search. A ship was eventually located in poor
> visibility and was unsuccessfully attacked by aircraft. This was apparently
> the SHEFFIELD, who avoided all torpedoes."

kbismarck `chase`（`kbismarck-chase`）给了 11 枚鱼雷的三种归宿：
> "At 1550, they obtained radar contact with a ship and dived to attack. The
> attack, however, turned out to be a failure since the ship sighted was actually
> the light cruiser Sheffield (Captain Charles A. Larcom) which had been detached
> from Force H to make contact with the Bismarck. Luckily for the British, the
> Sheffield was not hit by any of the 11 torpedoes launched because they had
> faulty magnetic pistols. Two torpedoes exploded upon hitting the water, three
> on crossing the cruiser wake, and the other six were successfully avoided."

→ **三个必须分开写的点**：
1. 根因是磁引信故障 + 情报没往下传（飞行员不知道有友舰），**不是舰认错目标**；
2. 她一炮未还；
3. 这一事件**零伤亡**。

补一条背景（wiki 线索，已顺着找到原始表述）：
皇家方舟号当时不确定目标是俾斯麦还是欧根亲王号，故第一波鱼雷定深 30 英尺而非 34 英尺。
→ 这条在 `work/raw/last-battle.md` 的 05-26 14:50 条目里已有一手口径转述，
正文引用时挂在 `hmshood-tovey-dispatch` 与 `kbismarck-chase` 名下。

### 6.2 晚间：被真炮弹打

两源各自的原句：
- Admiralty War Diary（tier A）："At 2140 the enemy fired 6 accurate salvoes at
  her and caused some casualties and slight damage."
- kbismarck `chase`："Bismarck fired a total of six salvoes and the British
  cruiser turned away to the north under the cover of a smoke screen. The
  Sheffield was not hit, but some splinters disabled her radar and injured
  twelve men of whom three died later."

三名死者（kbismarck `chase` 注 9，逐名）：
> "On board Sheffield, Ordinary Seaman David T. George died on 26 May 1941,
> Able Seaman Ambrose Ling died on 27 May 1941, and Able Seaman Raymond C. Taylor
> died on 28 May 1941."

时间口径差异：Admiralty 记 **2140**，kbismarck `chase` 记 **约 2145**，
`histoperi` 记 **2130–2155** 区间且写「六次齐射、距离九英里、无命中」。
三个时刻都在同一小时内，属记录口径差，**不构成分歧**，正文统一写「约 2140」。

---

## 7. 改装台账：两份来源月份不一致的地方

naval-history（逐月叙述）与 navypedia（Modernizations 台账）在几处月份对不上。
**处理原则：都保留，各带自己的 src，在 note 里写「两说并列，不裁决」。**

| 事项 | naval-history | navypedia | 处理 |
|---|---|---|---|
| + Type 284（前部主炮火控） | 1941-07（Rosyth） | 9/1941 | 两条 fact 并存 |
| + Type 273 / 281 / 285 | 1942-04（Tyne 大修） | 7/1942 | 取 naval-history 的 4 月为主，note 里记 navypedia 的 7 月 |
| + 6 门 20 mm | 1941-07 | 9/1941 | 取 1941-07，note 说明 |
| - Type 79Y | 1942-04 被 281 取代 | 记了两次（9/1941 与 7/1942） | **同源自相矛盾**，见下 |

### 7.1 navypedia 的一处自相矛盾（已在 fact note 里点明）

同一页的 Modernizations 台账里：
> "9/1941, Sheffield: - 2 x 4 - 12.7/62, type 79Y radar; + 6 x 1 - 20/70
> Oerlikon Mk II/IV, type 284 radar"
> "7/1942, Sheffield: - type 79Y radar; + 3 x 1 - 20/70 Oerlikon Mk II/IV,
> type 273, type 281, type 285 radars"

**79Y 被拆了两次。** 一台雷达只可能拆一次，故这两条至少有一条的拆项是记错了。
naval-history 的口径清楚（1942-04 由 281 取代），本组以它为准，
navypedia 的拆雷达部分不采信，但在 fact 的 note 里写明不采信的理由。

### 7.2 X 炮塔拆除的时间

navypedia 把「- 1 x 3 - 152/50 ("X")」记在 **5/1945**，即波士顿大修（1944-07-25 进厂）
结束那一刻。也就是说拆除动作发生在这次大修期内，**来源没给具体日期**。
正文与切片按「1944-07 至 1945-05 之间」表述，不编具体日。

---

## 8. 20 mm 数量：两个来源能对上，构成交叉印证

naval-history 给了一个明确的总数：
> "21st - Under refit at Greenock. (Note: Further 20mm Oerlikon weapons added
> making total of 22)"

navypedia 给的是逐次增量：
- 9/1941：+6 x 1 → 6
- 7/1942：+3 x 1 → 9
- 6/1943：+5 x 1 → 14
- 1/1944：+8 x 1 → 22

14 + 8 = 22，与 naval-history 的「total of 22」**吻合**。
这是本组最漂亮的一处交叉印证，两条都写进 fact 的 note。

**注意**：我在 fact 里存的是 22（来源直接给的总数），
不是把四个增量加起来算出的数 —— 虽然两者恰好相等。

---

## 9. 触雷与修理时长：两说并列

- naval-history："4th - Detonated mine off NE Iceland when on passage to provide
  cover for Russian Convoy PQ12. Major damage was sustained aft and a RM sentry
  was killed."（1942-03-04）
- navypedia Naval service 段："Sheffield was damaged by a mine 4.3.1942, repair
  lasted 4 months."

**日期一致（3-04），修理时长不一致**：naval-history 的流水（4-02 进厂、
5–6 月续修、7 月试航、7-24 归建）实际约 3 个多月；navypedia 说 4 个月。
两者都留着，不取整。`arctic-convoys-ships` 记 3 月 3 日，与两份更专的来源冲突，不取。

---

## 10. 巨浪损伤：日期两说

- naval-history："18th - Sustained extensive structural damage in appalling
  weather during passage. (Note: Top of "A" Turret was completely removed"
  （1943-02-18）
- 另有叙述写 2 月 19 日。

本组取 naval-history 的 2-18，正文不写具体日以避免无谓争议，
切片里写 2-18 并注明来源。

---

## 11. PQ-17：任务书的说法本轮**未获证实**

任务书要求写「PQ-17 的灾难中它在场」。本轮查到的结果是：

- `naval-history-sheffield` 的 1942 年 6 月段落：**没有 PQ17 的记录**。
  该页 1942-04 到 1942-09 之间只有大修与 7 月归建，没有护航编号。
- `arctic-convoys-ships` 给的完整护航清单：
  > "HMS Sheffield sailed in convoys: PQ5 + PQ18 + QP14 + JW51a + JW51b + JW52 +
  > JW55a + JW55b + RA51 + RA52 + RA55a"
  **清单里没有 PQ17，也没有 JW55B 之外的 1944 年护航。**
- 帕洛马雷斯（Palomares）那条 PQ17 记录是**另一艘船**的，我在初读时误拿了
  一句话（"In June 1942, she sailed as an escort in the infamous Convoy PQ-17"），
  核对后确认主语是 HMS Palomares，不是 Sheffield。

→ **结论：本组不写「Sheffield 在 PQ-17 中在场」。** 这属于「查不到就写查不到」。
她确实在场的是 PQ5、PQ12（1942-03 那次是为它提供掩护时触的雷）、PQ18、QP14
以及 JW/RA 系列的 8 个编号。**PQ18 才是她 1942 年 9 月那次真正的北极护航。**

**这一条请主会话注意：如果其他组/叙述文件里已经写了 Sheffield 在 PQ-17，
那需要复核。**

---

## 12. 未获取 / 查不到的项（明确列出，不留空猜）

| 项 | 状态 | 说明 |
|---|---|---|
| 装甲总重 | **未获取** | 整级一个数都没有。不要用别级的值填充 |
| 装甲占排水量比 | **未获取** | 同上 |
| 重量分配表 | **未获取** | navypedia 不提供 |
| 标准排水量状态的平均吃水 | **未获取** | 只给深载 6.20 m |
| 型深 / 方形系数 / 水线面积 / 干舷 | **未获取** | — |
| 锅炉蒸汽压力 / 温度 | **未获取** | 只知道是 Admiralty 三鼓 |
| 发电机总功率 | **未获取** | — |
| 螺旋桨直径 / 舵面积 | **未获取** | — |
| 造价 | **未获取** | — |
| 战时编制 | **未获取** | 有叙述称 1942 年 796 人，但只见于百科层，不取 |
| 本舰单独的主尺度实测值 | **未获取** | navypedia 只给子级统一值 |
| 1941-05-26 本舰弹药消耗 | **未获取** | Tovey 战报抓不到（403），本地副本里未见本舰逐发数 |
| 首任舰长姓名 | **未获取** | naval-history 未记；Larcom 是 1941-05 时的舰长 |
| PQ-17 是否在场 | **证伪方向** | 见 §11，两份来源的护航清单都没有它 |

---

## 13. 来源清单与可信度

| id | tier | 用途 | 关键性 |
|---|---|---|---|
| `naval-history-sheffield` | D | 逐月战历、改装月份、雷达型号、伤亡、拆解 | **主力**，本组 60% 的事实出自它 |
| `navypedia-town` | D | 主尺度、动力、装甲分项、武备、编制、改装台账 | 骨架数据 |
| `navypedia-gloucester` | D | 子级划分旁证 | 仅旁证 |
| `navypedia-edinburgh` | D | 子级划分旁证 | 仅旁证 |
| `navweaps-6in-50-mk23` | D | 主炮炮身全部参数、炮座型号与重量 | 已登记，直接复用 |
| `navweaps-4in-45-mk16` | D | 副炮/两用炮全部参数 | **本轮新登记** |
| `navweaps-2pdr-mk8` | D | pom-pom 炮座重量与仰角 | 已登记，直接复用 |
| `arctic-convoys-ships` | D | 护航编号清单、子级归属印证 | **本轮新登记** |
| `hmshood-tovey-dispatch` | **A** | 1941-05-26 的英方一手战报 | 已登记，直接复用 |
| `kbismarck-admiralty-war-diary` | **A** | 同日英海军部战争日记 | 已登记，直接复用 |
| `kbismarck-chase` | D | 逐分钟叙述、11 雷归宿、三名死者 | 已登记，直接复用 |
| `kbismarck-histoperi` | D | 时间线交叉核对 | 已登记，直接复用 |

**维基百科（tier E）本轮只用来找线索**，没有作为任何 fact 或正文的来源。
具体用法：由它找到 arctic.org.nz 这份老兵协会名录，再从那一名录拿到护航清单。

---

## 14. 发现一处既有来源登记错误（请主会话修正）

`data/sources.yaml` 里：
```yaml
  - id: navweaps-45in-45-mk16
    title: 'British 4.5"/45 (11.4 cm) QF Mark XVI'
    url: https://www.navweaps.com/Weapons/WNBR_4-45_mk16.php
```

**标题写的是 4.5 英寸，url 指向的是 4 英寸的页面。** 本组实际抓取了该 url，
返回页面标题为：
> "United Kingdom / Britain 4"/45 (10.2 cm) QF Mark XVI, Mark XVII and Mark XXI"

4.5 英寸 Mk XVI 的正确页面应为 `WNBR_45-45_mk16.php`。

本组不改 `data/`，另立 `navweaps-4in-45-mk16`（标题正确、url 同为本次实测页面）
用于城级副炮。**既有那条 `navweaps-45in-45-mk16` 需要改名或作废** ——
它现在被 `data/classes/illustrious.yaml` 的 `weapon:4_5in-qf-mk3` 引用着，
若作废会连带改写；从数值看 illustrious 记的是 114 mm / 45 倍径 / 弹重 39.5 kg，
那确实是 4.5 英寸炮的参数，所以**很可能是 url 写错、标题与数值都对**。
建议：把那条的 url 改成 `WNBR_45-45_mk16.php`。

---

## 15. 写作时的取舍说明

### 15.1 为什么 `protection.scheme` 填 other 而不是 incremental

见 §5。英式箱形防护与美式 all-or-nothing 的核心差别是「有没有一条连续的装甲带
围成闭合箱子」，而 incremental 通常指多层薄甲 + 分散布置。城级是前者。
注册表缺 box 档，填 other 并保留原词是最不误导的做法。

### 15.2 为什么把 `weapon.caliber_method` 填 usa_uk_method 并降 B

navweaps 只说 50 倍径，没声明量法。英制通例按膛线长计（bore length），
与美制一致。这是按通例判定，不是来源直接写明的，故降 B。

### 15.3 为什么 `mount.position` 多处填 B

navypedia 只说「沿上层建筑两舷布置」，没有逐座标位（A/B/X/Y 的确切位置）。
英制主炮塔 A（最前）、B（超射于 A 上方）、X（后部超射）、Y（最尾）是标准命名，
但 navweaps 与 navypedia 都没有逐座给出射界或位置表。
故 `mount:town-6in-ab` / `mount:town-6in-xy` 的 position 值降 B 并在 note 里
写明「按本级标准布置登记，来源未逐座标位」。

### 15.4 舰钟与「Shiny Sheff」绰号

先纠正一处我自己的初步判断：舰钟这一条**不是只有百科依据**。
`arctic-convoys-ships`（tier D）原句：
> "The stainless steel ship's bell, which was made by Hadfield's of Sheffield,
> was preserved and today hangs in Sheffield Cathedral along with her battle
> ensign."

故「不锈钢舰钟由谢菲尔德的 Hadfield's 制造、现存谢菲尔德大教堂、与战旗同处」
这一句有 tier D 来源支撑，**正文保留，src 里已加上 `arctic-convoys-ships`**。

但**「Shiny Sheff」这个绰号本身、以及「全舰用不锈钢替代黄铜以减少保养」这个成因**，
naval-history / navypedia / arctic.org.nz 三份 tier D 来源都没有提，只见于百科层。
→ **未写成 fact，正文亦未使用绰号**，只保留可查证的舰钟事实。

顺带记一处两源冲突（未进 fact，因为不在任何字段的覆盖范围）：
- `naval-history-sheffield`：1959 年转入预备役后任「**预备舰队**旗舰
  （Flagship of the Reserve Fleet），接替 Vanguard」。
- `arctic-convoys-ships`：写成「became flagship of the **Home Fleet** until
  September 1964」。
两说对「哪支舰队的旗舰」不一致。本组取 naval-history（它同时给出接替 Vanguard
这一可核对的细节），切片与正文按「预备舰队旗舰」写。

### 15.5 巴伦支海「首发命中」的措辞

`naval-history-sheffield` 在北角海战那一段写：
> "In action with BELFAST and NORFOLK against German battleship SCHARNHORST and
> obtained hits with second salvo."

注意这是**北角**（12-26），不是巴伦支海（12-31）。
巴伦支海那一段写的是：
> "Engaged and sank German destroyer FRIEDRICH ECKOLDT"

→ 「首发命中」属北角，我在正文里写的是「首发即命中」（对应 second salvo），
一字之差容易读成「第一发」，已在正文用「首发即命中」并保留原文 second salvo 的语义。
**严格说 second salvo 是「第二次齐射」，正文应写「以第二次齐射命中」** ——
这是本组一处措辞需收紧的地方，已在下方争议里标出。

---

## 16. 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/town.yaml`，**123** 条 fact = 舰级本体 43 + 武器实体 42 + 炮位实体 38） |
| 单舰文件 | 1（`ships/sheffield.yaml`，**40** 条 fact） |
| 切片文件 | 1（`slices/sheffield.yaml`，**7** 片，P0–P6，首尾相接无空档） |
| 正文文件 | 1（`articles/sheffield.yaml`，intro **4** 段 + history **5** 节 **26** 条事件） |
| 新登记来源 | **6** 个 id（`naval-history-sheffield` / `navypedia-town` / `navypedia-gloucester` / `navypedia-edinburgh` / `navweaps-4in-45-mk16` / `arctic-convoys-ships`） |

自检结果（`python` + PyYAML，2026-11-22）：
- 全部 4 份 YAML 可解析。
- 逐条 fact 与 `data/fields.yaml` 对拷：**0 处**字段未注册 / 单位不符 / 类型不符 /
  枚举越界 / qual 缺失或越界 / src 未登记 / tier E 支撑 / confidence 越界 /
  缺 valid.from；`comparable: false` 的两条均带 note。
- 正文模糊词扫描（据说/有人认为/有人称/据信/或许/大概/应该是）：**0 命中**
  （4 份文件全扫，含 note 与切片）。

**用项目自带校验器跑过一遍**（`python scripts/validate.py --data _tmp/g2_valdata`，
把本组 4 份 YAML + 合并后的 sources 拷进临时数据目录后执行）：
**0 错误 / 1 警告**。

那 1 条警告的内容与原因：

> `ships/sheffield.yaml#service.casualties[37]`
> 来源 `kbismarck-chase` 的 role 不含 data —— 确认它真能支撑数据。

说明：本舰 1941-05-26 那三名死者的**姓名与死亡日期**（David T. George / 5-26、
Ambrose Ling / 5-27、Raymond C. Taylor / 5-28）只有 `kbismarck-chase` 的注 9
给到逐名程度；`kbismarck-admiralty-war-diary`（tier A）只说
"caused some casualties and slight damage"，没有数字也没有姓名。
而 `kbismarck-chase` 在 `data/sources.yaml` 里登记的 role 是 `[narrative]`，
不含 `data`，于是触发警告。

本组不为了消警告而改别人的登记（改 role 会影响所有引用它的既有舰艇文件），
**保留警告并在此说明**。若主会话认可该来源也承担 data 角色，
把 `kbismarck-chase` 的 role 改为 `[data, narrative]` 即可消掉 —— 一并交给主会话决定。

### 卡住的地方

1. **`www.hmshood.org.uk` 403** —— Tovey 战报（ADM 234/509）直连与带 Referer 均 403，
   未能重新抓取。该来源已登记且有本地副本，故引用已登记来源，但没有新读到原文。
2. **PQ-17 是否在场证伪** —— 见 §11。两份来源的护航清单都没有 PQ17，
   任务书给的这一条未能证实，本组不写。
3. **装甲总重 / 占比 / 重量分配** —— 整级零数据，未填。
4. **1941-05-26 本舰弹药消耗** —— 未见任何来源给逐发数（同日的 Rodney/KGV 有）。
5. **首任舰长** —— naval-history 段落里只出现 1941 年时的 Larcom，建造期舰长未记。
6. **标准状态平均吃水** —— navypedia 只给深载。
7. **`web_fetch` 全线不可用于英国舰艇站** —— 见 §0，必须用 urllib。
   这一条对后续所有组都有影响，建议主会话写进 SCHEMA 或环境说明。

### 有争议的记载

| # | 事项 | A 说 | B 说 | 本组处理 |
|---|---|---|---|---|
| 1 | Type 284 装舰时间 | naval-history：1941-07 Rosyth 改装 | navypedia：9/1941 | 两条 fact 并存，note 写「两说并列，不裁决」 |
| 2 | 273/281/285 装舰时间 | naval-history：1942-04 Tyne 大修 | navypedia：7/1942 | 取 4 月为主 fact，note 记 7 月 |
| 3 | 79Y 拆除时间 | naval-history：1942-04 被 281 取代 | navypedia：9/1941 与 7/1942 各记一次（自相矛盾） | 以 naval-history 为准，note 写明 navypedia 拆项不采信 |
| 4 | 触雷后修理时长 | naval-history 流水推算约 3 个多月 | navypedia：4 months | 两说并存，不取整 |
| 5 | 触雷日期 | naval-history / navypedia：1942-03-04 | arctic-convoys-ships：3-03 | 取 3-04，后者不采信 |
| 6 | 巨浪损伤日期 | naval-history：1943-02-18 | 另有叙述：2-19 | 取 2-18，正文不写具体日 |
| 7 | 被俾斯麦炮击时刻 | Admiralty War Diary：2140 | kbismarck chase：约 2145；histoperi：2130–2155 | 同一小时内，不构成分歧；正文写「约 2140」 |
| 8 | 「首发命中」措辞 | naval-history 原文 "obtained hits with second salvo"（第二次齐射） | — | **已改为「以第二次齐射命中」**，不再用「首发命中」 |
| 9 | 舰钟与战旗现存谢菲尔德大教堂 | `arctic-convoys-ships`（tier D）明确记载，Hadfield's 造 | naval-history 与 navypedia 均未提 | 有 tier D 支撑，正文保留，src 加上 arctic-convoys-ships |
| 10 | 1959 年后是哪支舰队的旗舰 | naval-history：**预备舰队**旗舰，接替 Vanguard | arctic-convoys-ships：**本土舰队**旗舰，至 1964-09 | 取 naval-history（带可核对的接替对象），正文与切片按「预备舰队」写 |
| 11 | 「Shiny Sheff」绰号及不锈钢成因 | 仅百科层 | 三份 tier D 来源均未提 | **未写成 fact，正文未用绰号** |
