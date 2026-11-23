# TG 17.2 重巡组调研底稿 —— 阿斯托里亚号（CA-34）与波特兰号（CA-33）

> 2026-11-23 · subagent `us-tg172` · 工作目录 `D:\deepseek harness\website-warships`
> 只写 `work/staging/tg172/`。原始页面在 `_raw/`（78 个文件、约 5.0 MB）。

---

## 0. 一句话交代这次做了什么

按 SCHEMA §3.1 的 35 个骨架字段采集两舰与两级的技术数据与战历，产出
2 个舰级文件、2 个单舰文件、1 个来源分片（13 条新来源）。
**查不到的一律写「未获取」，两源打架的一律并列不裁。**

---

## 1. 抓取方式（先把这件事说清楚，因为它决定了后面所有 URL 的形状）

### 1.1 `web_fetch` / `research` 确实不能用

按 SCHEMA §9.1 用 Python urllib + User-Agent 直连。**但这一轮的实际障碍
比 SCHEMA 预想的更严重**，有两类：

**A 类：TLS 握手阶段就被断开（不是 SSRF，是连接层失败）**

`history.navy.mil`（NHHC 官方站）在本机完全不可达：

| 工具 | 报错原文 |
|---|---|
| Python urllib | `urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1082)` |
| PowerShell Invoke-WebRequest | `基础连接已经关闭: 发送时发生错误。` |
| curl.exe | `curl: (35) schannel: failed to receive handshake, SSL/TLS connection failed` |
| http:// 明文 | `ConnectionResetError` |

三种客户端、两种协议全挂。**这是本机网络环境问题，不是站点问题**
（同一个站点在 Wayback 上有正常快照）。

**B 类：HTTP 502 / 403**

| 站点 | 状态 | 处置 |
|---|---|---|
| `navsource.org` | 502（http 与 https 都是） | 改用 Wayback 快照 |
| `ibiblio.org/hyperwar/USN/rep/` 目录 | 403 | 从已知子路径逐个试 |
| `ww2db.com` | 403 | 放弃 |
| `ussastoria.org` | 200 但返回 114 字节 | 已跳转到域名停放页（`window.location.href="/lander"`），改用 Wayback |

### 1.2 救命的办法：`web.archive.org` 通

实测 `web.archive.org` 可以直连，且能取到上面所有失效站点的快照。
两个用法：

```
https://web.archive.org/web/20210120073955/https://www.navsource.org/archives/04/034/04034.htm
https://web.archive.org/web/2021id_/https://www.history.navy.mil/.../uss-quincy-...-war-damage-report-no29.html
```

**`id_` 后缀是关键**：不加它，Wayback 会往页面里注入自己的工具栏和脚本，
正文会被污染；加了它拿到的是原始字节。

**注意 429**：Wayback 对密集请求限流，本组撞到两次（`HTTP 429`）。
间隔 4 秒重试 + 一次只抓一个页面即可。

### 1.3 本组实际可用的站点清单

| 站点 | 可达性 | 用途 |
|---|---|---|
| `navweaps.com` | 直连 200 | 主炮/副炮/高炮/雷达 |
| `navypedia.org` | 直连 200 | 主尺度/排水量/装甲/改装表（**本组骨架主力**） |
| `ibiblio.org/hyperwar` | 直连 200（部分路径 403） | DANFS 转录本、NWC 萨沃岛报告、Midway OOB |
| `web.archive.org` | 直连 200 | navsource、NHHC 战损报告、ussastoria.org |
| `naval-encyclopedia.com` | 直连 200 | 波特兰级雷达/防空改装（交叉核对） |
| `history.navy.mil` | **不通** | 只能走 Wayback |
| `navsource.org` | **502** | 只能走 Wayback |
| `ussastoria.org` | **已停放** | 只能走 Wayback |

原始页面全部落在 `_raw/`，文件名 = 来源 id，`.html` + `.txt` 双份
（`.txt` 是去标签后的纯文本，方便 grep 原句）。

---

## 2. 关于任务书里那几条史实陈述的核实结果

任务书说「任何史实陈述都当待核实」，逐条结果如下。

| 任务书原话 | 核实结果 | 依据 |
|---|---|---|
| 两舰 1942-06 中途岛时属 **TG 17.2** | ✅ **完全正确** | navweaps Midway OOB 原文「Task Group 17.2 Cruiser Group / RA William Ward Smith / Position: ComCruTF-17 / USS Astoria (CA-34) (flagship) / USS Portland (CA-33)」 |
| TG 17.2 是弗莱彻 TF 17 的巡洋舰群 | ✅ 正确 | 同上，OOB 把 17.2 排在 Task Force 17 之下（同页还有 17.4 驱逐舰群、17.5 航母群） |
| RA **William W. Smith** | ✅ 正确，原文全名 William Ward Smith | 同上 + `USNA09 [95]` 注 |
| **阿斯托里亚为旗舰** | ✅ 正确 | 同上，原文 `(flagship)` |
| 阿斯托里亚属**新奥尔良级** | ✅ 正确，但需补充 | DANFS「cl. New Orleans」；**且她是 CA-32/34/36 这一组，不是整级 7 艘共享同一套装甲与炮座** |
| 波特兰属**波特兰级** | ✅ 正确 | DANFS「cl. Indanapolis」（原文拼错，见 §4.4） |
| 阿斯托里亚 1942-08 萨沃岛被击沉 | ✅ 正确，精确到 1215 | DANFS + WDR No.29 双源 |
| 波特兰活到战后拆解 | ✅ 正确，1959-10-06 出售 | DANFS |
| 中途岛时**还没装 40mm Bofors** | ✅ 正确，而且两舰整个生涯中途岛前都没装 | navypedia 改装表：本级 40 mm 首次出现在「late 1943, all survived」（新奥尔良级）与「5/1943, both」（波特兰级）；阿斯托里亚 1942-08 已沉没，从未进入该改装 |
| 副炮是 5"/25 **不是 5"/38** | ✅ 正确 | navweaps 5"/25 页「Ship Class Used On」明列 New Orleans (CA-32) 与 Portland (CA-33) 两级 |
| 主炮型号 Mk 9 vs Mk 14「待核实」 | ⚠️ **已核实：中途岛时是 Mk 9 系列，不是 Mk 14** | navweaps 8"/55 页：「Mark 9 was the original design and was used on ships built in the 1920s」「The Mark 14 was used for most regunnings during World War II」 |

**任务书里没有错的。** 唯一需要「纠正」的是语气上的松紧：
主线陈述全部成立，但有两处值得收紧，见 §3。

---

## 3. 三条需要主会话特别注意的收紧点

### 3.1 「新奥尔良级三舰」不是一个均质概念

任务书写「阿斯托里亚/新奥尔良/明尼阿波利斯是同批，注意主炮型号可能不同」。
核实后的结论比这个更强：**这三艘与同级另四艘在装甲与炮座上分属两组不同设计**。

navypedia 同级页把 7 艘分三组写：

> 「CA32, 34, 36: belt: 127 - 76, bulkheads: 76 - 38, deck: 57,
> **barbettes: 127**, turrets: 203 - 38, CT: 127
> CA37, 38: ... **barbettes: 152**, turrets: 203 - 38, CT: 127
> CA39, 44: ... **barbettes: 133**, turrets: 203 - 38, CT: 127」

主炮也是两组：

> 「Armament | CA32, 34, 36: 3 x 3 - 203/55 Mk 9.11.13/14
> CA37 - 39, 44: 3 x 3 - 203/55 Mk 12.15」

而炮座本身还有第三种差别，来自 navweaps：

> 「The later mountings used on New Orleans (CA-32), Astoria (CA-34) and
> Minneapolis (CA-36) were classified as "triple turrets" as they did have a
> rotating stalk.」
> 「Triple Mounts: Pensacola (2), Northampton (3) and Indianapolis (3)
>  Triple Turrets: New Orleans (CA-32, 34 and 36 only) (3)」
> 「Twin Mounts: 187 tons (190 mt) / Triple Mounts: 247 - 250 tons (251 - 254 mt)
>  Triple Turrets: 294 tons (299 mt)」

**即：阿斯托里亚号的炮座（294 t，有旋转 stalk）比波特兰号的炮座（247-250 t，
无 stalk）重 45 吨。** 这是两舰之间最容易漏掉的一处硬差别，
也是「Mk 9 系列」这个共同点之外唯一站得住的同类项。

### 3.2 「Mk 9 vs Mk 14」的答案是：中途岛时是 Mk 9，而且这两艘从未装过 Mk 12/15

正面依据（navweaps 8"/55 Mk 9 页）：

> 「Mark 9 was the original design and was used on ships built in the 1920s.」
> 「The Mark 14 was used for most regunnings during World War II but at least
> USS Minneapolis (CA-36) was regunned in 1945 with the Mark 15 Mod 1」
> 「^The Mark 9 originally had a muzzle velocity of 3,000 fps (914 mps), but
> barrel life was only about 500 rounds and accuracy was poor.」
> 「Marks 9, 10, 11 and 13 guns: 2,800 fps (853 mps) / Mark 14 guns only:
> 2,700 fps (823 mps)」

反面依据（navweaps 8"/55 Mk 12/15 页）：

> 「Mark 12: Tuscaloosa (CA-37) sub-class, Wichita (CA-45) and Baltimore (CA-68)」
> 「Mark 15: All other Baltimore class and Oregon City (CA-122) class」
> 「The Tuscaloosa sub-class consisted of Tuscaloosa (CA-37), San Francisco
> (CA-38), Quincy (CA-39) and Vincennes (CA-44).」
> 「Minneapolis (CA-36) was regunned with Mark 15 Mod 1 in 1945」

**CA-32/34/36 三艘一艘都不在 Mk 12/15 的装舰名单里。** CA-36 是 1945 年
单独换 Mk 15 Mod 1 的；CA-34 阿斯托里亚 1942-08 已沉；CA-32 新奥尔良号
无换装记录。

**所以任务书里「Mk 9 vs Mk 14 待核实」这一项，答案是 Mk 9。**
Mk 14 是「战时换装用的再换衬里版」，1943-44 年才普及，与 1942-06 无关。

### 3.3 波特兰号在瓜岛登陆时**不在**萨沃岛，这一条必须记住

任务书没直接说错，但两舰在中途岛同属 17.2 这个事实很容易让人顺推
「瓜岛也在一起」。实际不是。

DANFS 只说：「Portland provided cover and support for the Marine landings at
Tulagi and Guadalcanal, the Solomons 7 through 9 August.」——**不给编队号**。

编队号在 NWC 萨沃岛分析报告第 3 章的兵力编成表里：

> 「(b) TG 61.2, Amphibious Force (TF 62 plus SW Pac TF 44)
>  (1) TG 62.1, Transport Group XRAY …
>  (3) **TG 62.3 Fire Support Group LOVE**
>  Quincy, Vincennes, **Astoria**, Hull, Dewey, Ellet, Wilson 4 DD
>  (4) TG S62.4 Fire Support Group MIKE
>  San Juan 1 CL (AA) / Monssen, Buchanan 2 DD」
>
> 「(2) **TG 61.1.2 (Pacific Fleet Task Force 16)**
>  Enterprise (38 VF, 36 VD, 10 VT) 1 CV
>  North Carolina 1 BB / **Portland 1 CA** / Atlanta 1 CL (AA)
>  Balch, Maury, Gwin, Benham, Grayson 5 DD」

**波特兰号在 TG 61.1.2（企业号群），阿斯托里亚号在 TG 62.3。**
这就解释了为什么 1942-08-09 的损失名单里没有波特兰号。

---

## 4. 逐字段的英文原句与 URL

以下按文件与字段组织。**每条都是原文照抄，不翻译。**

### 4.1 舰级公共数据 —— `classes/new-orleans.yaml`

| 字段 | 值 | 英文原句 | URL |
|---|---|---|---|
| `displacement.standard` | 10,136 t | 「Displacement standard, t \| 10136」 | https://www.navypedia.org/ships/usa/us_cr_new_orleans.htm |
| `displacement.full` | 12,463 t | 「Displacement full, t \| 12463」 | 同上 |
| `dimensions.length.oa` | 179.2 m | 「Length, m \| 176.2 wl 179.2 oa」 | 同上 |
| `dimensions.length.wl` | 176.2 m | 同上 | 同上 |
| `dimensions.beam.wl` | 18.8 m | 「Breadth, m \| 18.8」 | 同上 |
| `dimensions.draught.mean` | 5.92 m | 「dr. 19'5" (mean)」 | https://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca34.html |
| `dimensions.draught.max` | 6.86 m | 「588' 0" (oa) x 61' 9" x 22' 6" (Max)」 | https://web.archive.org/web/20210120073955/https://www.navsource.org/archives/04/034/04034.htm |
| `propulsion.plant_type` | steam_turbine | 「4 sets Westinghouse geared steam turbines」 | navypedia-neworleans |
| `propulsion.shafts` | 4 | 「No of shafts \| 4」 | 同上 |
| `propulsion.boiler.count` | 8 | 「8 Babcock & Wilcox boilers」 | 同上 |
| `propulsion.power.design` | 107,000 hp | 「Power, h. p. \| 107000」 | 同上 |
| `propulsion.speed.design` | 32.7 kn | 「Max speed, kts \| 32.7」 | 同上 |
| `propulsion.fuel.capacity` | 1,861 t | 「Fuel, t \| oil 1241 - 1861」 | 同上 |
| `propulsion.range.max` | 10,000 nmi | 「Endurance, nm(kts) \| 10000 (15)」 | 同上 |
| `propulsion.range.at_speed` | 15 kn | 同上 | 同上 |

**装甲（全部来自同一句，故只列一次原文）：**

> 「Main belt abreast machinery extended to 1.5m below and 2.86m over waterline.
> It was 127mm thick (76mm at lower edge) on 19mm STS plating. There were narrow
> belts abreast magazines. Thickness of these belts was 102mm decreasing to 76mm
> at lower edge. Magazines were protected by 37mm bulkheads fore and aft,
> machinery and magazines were separated by 76-51mm bulkheads. Armoured deck
> over main belt was 57mm over the machinery (on 2nd deck level) and magazines
> (on 1st platform level). Its thickness decreased to 32mm fwd from fore
> magazines. Barbettes were 127mm thick. Turrets had 203mm faces, 95-38mm sides,
> 38mm rears and 70mm crowns.」
> —— https://www.navypedia.org/ships/usa/us_cr_new_orleans.htm

navsource 的独立互证（不同来源，不是同一句的转引）：

> 「Armor, 5" Belt, 8" Turrets, 2 1/4" Deck, 5" Conning Tower.」
> —— https://web.archive.org/web/20210120073955/https://www.navsource.org/archives/04/034/04034.htm

**装甲占比：**

> 「The protection weight made 15% of standard displacement.」
> —— navypedia-neworleans

### 4.2 舰级公共数据 —— `classes/portland.yaml`

| 字段 | 值 | 英文原句 | URL |
|---|---|---|---|
| `displacement.standard` | 10,258 t | 「Displacement standard, t \| 10258」 | https://www.navypedia.org/ships/usa/us_cr_portland.htm |
| `displacement.full` | 12,755 t | 「Displacement full, t \| 12755」 | 同上 |
| `dimensions.length.oa` | 185.9 m | 「Length, m \| 180.4 wl 185.9 oa」 | 同上 |
| `dimensions.beam.wl` | 20.1 m | 「Breadth, m \| 20.1」 | 同上 |
| `dimensions.draught.mean` | 5.21 m | 「dr. 17'1"」 | https://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca33.html |
| `dimensions.draught.max` | 6.40 m | 「Draught, m \| 6.40 full load」 | navypedia-portland |
| `propulsion.boiler.type` | Yarrow | 「8 Yarrow boilers」 | 同上 |
| `propulsion.turbine.type` | Parsons | 「4 sets Parsons geared steam turbines」 | 同上 |
| `propulsion.power.design` | 107,000 hp | 「Power, h. p. \| 107000」 | 同上 |
| `propulsion.speed.design` | 32.5 kn | 「Max speed, kts \| 32.5」 | 同上 |
| `propulsion.fuel.capacity` | 2,125 t | 「Fuel, t \| oil 1417 - 2125」 | 同上 |

**装甲（同一句）：**

> 「Main belt extended to 1.5m below and 3m over waterline. Middle part of the
> belt abreast machinery was 127mm thick (83mm at lower edge) on 19mm STS
> plating and end parts abreast magazines were 146mm. Belt was closed by 64mm
> bulkheads and middle and end parts were separated by 25mm bulkheads.
> Armoured deck over main belt was 54mm thick over magazines and 64mm over
> machinery. Barbettes were 38mm thick. Turrets had 64mm faces, 25mm sides,
> 19mm rears and 51mm crowns.」
> —— https://www.navypedia.org/ships/usa/us_cr_portland.htm

**无鱼雷管的否定句（本组最重要的一句否定证据）：**

> 「Portland class differed from predecessors by absence of TTs and doubled
> number of 127mm AA guns.」
> —— 同上

**首获免疫区的自述：**

> 「…and for the first time USN ships had immune zone under 203mm shells, the
> truth, it concerned magazines only (fore magazines between 60 and 115 cables,
> and aft ones between 60 and 102 cables).」
> —— 同上

### 4.3 主炮 —— 8"/55 (20.3 cm) Marks 9/14

URL：https://www.navweaps.com/Weapons/WNUS_8-55_mk9.php

| 项 | 原句 |
|---|---|
| 型号 | 「Designation \| 8"/55 (20.3 cm) Marks 9, 10, 11, 13 and 14」 |
| 装舰 | 「Lexington (CV-2), Pensacola (CA-24), Northampton (CA-26), New Orleans (CA-32, 34 and 36 only) and Portland (CA-33) classes」 |
| 设计年 | 「Date Of Design \| 1922」 |
| 服役年 | 「Date In Service \| 1927」 |
| 炮身重 | 「Gun Weight \| 30.0 tons (30.48 mt)」 |
| 全长 | 「Gun Length \| 449.0 in (11.405 m)」 |
| 膛长 | 「Bore Length \| 440.1 in (11.179 m)」 |
| 膛线长 | 「Rifling Length \| 373.65 in (9.491 m)」 |
| 药室 | 「Marks 9, 10, 11 and 13: 5,300 in3 (86.8 dm3) / Mark 14: 4,860 in3 (79.6 dm3)」 |
| 射速 | 「Rate Of Fire \| 3 - 4 rounds per minute」 |
| 弹重 | 「AP Mark 19 Mods 1 to 6: 260 lbs. (118 kg)」 |
| 初速 | 「Marks 9, 10, 11 and 13 guns: 2,800 fps (853 mps)」 |
| 炮管寿命 | 「Approximate Barrel Life \| 715 rounds」 |
| 每炮备弹 | 「Ammunition stowage per gun \| 150 rounds」 |
| 最大射程 | 「45.00 degrees \| 32,330 yards (29,563 m)」 |
| 炮座重 | 「Triple Turrets: 294 tons (299 mt)」 |
| 仰角 | 「Elevation \| -10 / +41 degrees」 |
| 装填角 | 「Mounts: +5 degrees / Turrets: +9 degrees」 |
| 有 stalk | 「The later mountings used on New Orleans (CA-32), Astoria (CA-34) and Minneapolis (CA-36) were classified as "triple turrets" as they did have a rotating stalk.」 |
| 无超重弹 | 「None of these ships ever carried the "super-heavy" AP projectiles as their ammunition hoists could not accommodate the longer, heavier round.」 |
| 备弹变化 | 「During the early part of the war, the Northampton (CA-26) and Portland (CA-33) classes carried 1,500 rounds per ship, but this was reduced during refits after July 1942 to just over 1,300 rounds in order to allow for added AA weapons. The New Orleans (CA-32) class was reduced during refits after August 1942 to 125 rounds per gun.」 |

### 4.4 副炮 —— 5"/25 (12.7 cm) Marks 10/11/13/17

URL：https://www.navweaps.com/Weapons/WNUS_5-25_mk10.php

| 项 | 原句 |
|---|---|
| 型号 | 「Designation \| 5"/25 (12.7 cm) Marks 10, 11, 13 and 17」 |
| 装舰 | 「Pensacola (CA-24), Northampton (CA-26), New Orleans (CA-32), Portland (CA-33) and Brooklyn (CL-40) classes」 |
| 设计/服役 | 「Date Of Design \| 1921」「Date In Service \| 1926」 |
| 炮身重 | 「Barrel Weight (all except Mark 17): 2,105 lbs. (955 kg)」「Weight with housing: about 4,270 lbs. (1,937 kg)」 |
| 全长 / 膛长 | 「Gun Length oa \| 142.25 in (3.613 m)」「Bore Length \| 125 in (3.175 m)」 |
| 射速 | 「Rate Of Fire \| 15 - 20 rounds per minute」 |
| 炮座（关键） | 「Cruisers \| Pensacola (4), Northampton (8), Portland (8) and New Orleans (except Quincy and Vincennes) (8): Mark 19」 |
| 仰角 | 「Marks 17, 19, 23 and 27: -15 / +85 degrees」 |
| 驱动 | 「Mark 19: Manual operation, only」（注：战时多数 Mk 19 加了 1 hp 俯仰电机与 1-1.5 hp 方向电机） |

### 4.5 高炮 —— 1.1"/75 (28 mm) Mark 1

URL：https://www.navweaps.com/Weapons/WNUS_1-1-75_mk1.php

| 项 | 原句 |
|---|---|
| 型号 | 「Designation \| 1.1"/75 (28 mm) Mark 1」 |
| 设计/服役 | 「Date Of Design \| 1929」「Date In Service \| 1937」 |
| 炮身重 | 「Gun Weight \| 556 lbs. (252 kg) (without breech)」 |
| 射速 | 「Cyclic: 150 rounds per minute / Practical: About 100 rounds per minute」 |
| 炮座 | 「Quadruple Mounts \| Mark 1 / Mark 2 Mod 1, Mark Mods 2 - 6」 |
| 炮座重 | 「Mark 2 Mod 2: 10,500 lbs. (4,763 kg)」 |
| 仰角 | 「-15 / +110 degrees」 |
| 与本舰有关的两条图注 | 「Newly added 1.1" (28 mm) anti-aircraft mount on USS Astoria (CA-34) in July 1941」「1.1" (28 mm) anti-aircraft mounts on fantail of USS Astoria (CA-34) in July 1941. Note that Mark 44 Directors have not yet been installed.」 |

### 4.6 阿斯托里亚号建造与结局 —— `ships/astoria.yaml`

URL（DANFS）：https://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca34.html

> 「The second Astoria (CL-34) was laid down on 1 September 1930 at the Puget
> Sound Navy Yard; reclassified as a heavy cruiser, CA-34, on 1 July 1931;
> launched on 16 December 1933, sponsored by Miss Leila C. McKay, a descendant
> of one of the partners in the Astor expedition that founded Astoria, Oreg.;
> and commissioned on 28 April 1934, Capt. Edmund S. Root in command.」

> 「(CA-34: dp. 9.950; l. 588'0"; b. 61'9" (l.); dr. 19'5" (mean); s. 32.7 k.;
> cpl. 899; a. 9 8", 8 5", 2 3-pdrs., 8 .50-cal. mg.; cl. New Orleans)」

> 「Astoria turned over on her port beam, rolled slowly, and settled by the
> stern, disappearing completely by 1215.」

> 「Suffering from the effects of at least 65 hits, Astoria fought for her life.」

**1941-07 改装（DANFS）：**

> 「During her refit, she received quadruple-mount 1.1-inch antiaircraft machine
> guns and a pedestal fitted at her foremast in anticipation of the imminent
> installation of the new air-search radar.」

**同一件事的另一个说法（ussastoria.org）：**

> 「In April 1941, USS ASTORIA returned to the West Coast to undergo a yard
> period at Mare Island, Vallejo, CA. She was modernized with the addition of
> quad 1.1-inch antiaircraft guns fore and aft. Her masts were cropped in
> preparation to receive a new technology that was a closely guarded secret:
> Radar.」
> —— https://web.archive.org/web/20210120073955/http://ussastoria.org/The_Pineapple_Fleet.html

**1942-06 改装（ussastoria.org）：**

> 「On 14 June 1942, the day after ASTORIA returned to Pearl Harbor, she
> underwent a Change of Command Ceremony. CAPT William G. Greenman relieved
> Francis W. Scanland as 7th commanding officer of the ship. At this time
> ASTORIA also received upgrades including the addition of new main battery
> fire control radar and blast bags for her 8" rifles.」
> —— https://web.archive.org/web/20130317235737id_/http://ussastoria.org:80/Offensive_Preparations.html

> 「USS ASTORIA CA-34 moored in berth C-3 at Pearl Harbor circa 1-7 July 1942.
> A new Mk 3 main battery fire control radar has been attached to her forward
> Mk 38 director.」
> —— 同上

**萨沃岛（一手战报转录）：**

> 「Out of a total of 83 officers, 990 enlisted men, and one civilian newspaper
> correspondent, Joe J. Custer, on board, incomplete information now at hand
> indicated 61 officers, the news correspondent and 629 men were rescued.
> Of this number 7 officers and 78 men are wounded, many seriously.
> 20 officers known dead, 2 unaccounted for. 138 enlisted men are known to be
> dead.」
> —— https://web.archive.org/web/20121030054211id_/http://www.ussastoria.org:80/Iron_Bottom_Sound.html

> 「ASTORIA FC [fire control] radar range gave 5640 yards.」
> —— 同上

**萨沃岛沉没过程（BuShips 战损报告 No.29，A 级）：**

URL：https://web.archive.org/web/2021id_/https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/w/war-damage-reports/uss-quincy-ca39-astoria-ca34-vincennes-ca44-war-damage-report-no29.html

> 「9. U.S.S. VINCENNES, U.S.S. QUINCY and U.S.S. ASTORIA, plus two destroyers
> on the night of August 8-9, 1942 comprised Task Group 62.3.」

> 「The five airplanes on each ship except QUINCY had been drained of all
> gasoline.」

> 「24. … ASTORIA sustained an unknown number of hits from 8", 5", and 20mm
> projectiles of which about 63 were reported in references (a) and (b).」

> 「The fire by now had reached the lower 5" and 1.1" hoists as frequent
> explosions were heard below decks.」

> 「This list was 10° by about 1130 when a heavy explosion took place on the port
> side in way of the forward 5" magazines. The ship listed about 15° to port.」

> 「ASTORIA capsized to port, settling by the stern and disappeared at 1215.」

> 「E. Conclusions / 94. … In ASTORIA the initial heel was caused by the
> flooding of port side compartments due to the explosion of the 5" magazine.」

**报告自述的可靠性限制（引用时刻数据必须带上这句）：**

> 「8. … As a result, there is a great deal of information which, naturally, is
> contradictory in many instances. The times and even the sequence of events
> differ to such an extent in the various reports that it has been impossible to
> construct an account in which all the details agree with the basic elements.」

**逐条炮位失效（`armament.gun_failures` 的来源）：**

> 「The sixth 8" salvo hit the face plate and barbette of turret I putting it out
> of action and killing the personnel within the turret and the barbette.」
> 「Gun No. 2, although not hit, was out of action because of the explosion and
> fire in turret II and the fire in forward 20mm clipping room.」
> 「47. The first hit (No. 36) received by the ship was in mount No. 3 of the
> after 1.1" battery. … Structural fragments from the No. 3 mount put No. 4
> mount out of action.」
> 「By about 0200 the port and starboard secondary batteries, except gun No. 1,
> were completely out of commission due to direct hits and to the fire amidships
> on the upper deck.」

### 4.7 波特兰号建造与结局 —— `ships/portland.yaml`

URL（DANFS）：https://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca33.html

> 「(CA-33: dp. 9,950; l. 610'3", b. 66'1"; dr. 17'1"; s. 32.7 k.; cpl. 848;
> a. 9 8", 8 5", 8 .50 cal.; cl. Indanapolis)」

> 「The first Portland (CA-33), a heavy cruiser, was authorized 13 February 1929;
> laid down by Bethlehem Steel Co., Shipbuilding Div., Quincy, Mass.
> 17 February 1930; launched 21 May 1932; sponsored by Mrs. Ralph D. Brooks of
> Portland; and commissioned 23 February 1933, Captain H. F. Leary in command.」

> 「During this action 13 November 1942, Portland took a torpedo hit at 0158 on
> the starboard quarter, which blew off both inboard propellers, jammed the
> rudder five degrees right, and jammed number three turret in train and
> elevation. A four degree list was quickly corrected by shifting ballast, but
> the steering casualty could not be overcome and the ship was forced to steam
> in circles to starboard.」

> 「she decommissioned at Philadelphia 12 July 1946 and was maintained in reserve
> status until struck from the Navy List 1 March 1959. The cruiser was sold to
> Union Mineral and Alloys Corp., New York, N.Y. 6 October 1959 and scrapped.」

> 「Portland received sixteen battle stars for World War II service.」

**navsource 的舰级数据行（不同来源，可互证）：**

> 「CLASS - PORTLAND / Displacement 9,950 Tons, Dimensions, 610' 3" (oa) x
> 66' 1" x 24' (Max) / Armament 9 x 8"/55, 8 x 5"/25, 8 x 0.5" 4 Aircraft. /
> Armor, 5" Belt, 2 1/2 Turrets, 2 1/2" Deck, 1 1/4 Conning Tower. /
> Machinery, 107,000 SHP; Geared Turbines, 4 screws /
> Speed, 32.7 Knots, Crew 621.」
> —— https://web.archive.org/web/20210120073807/https://www.navsource.org/archives/04/033/04033.htm

### 4.8 雷达与改装序列

**新奥尔良级 CA32/34/36 的改装表**（https://www.navypedia.org/ships/usa/us_cr_new_orleans.htm）：

> 「Astoria, 6.1941; New Orleans, Minneapolis, 11.1941; Tuscaloosa, San
> Francisco, Quincy, Vincennes 12.1941 - 4.1942: + 4 x 4 - 28/75 Mk 1」
> 「mid-1942, all: - 8 x 1 - 12.7/90; + 6 x 1 - 20/70 Mk 4, SC, Mk 3 radars」
> 「late 1942, all survived: + (6 - 10) x 1 - 20/70 Mk 4」
> 「late 1943, all survived: - 4 x 4 - 28/75, 1 catapult, SC radar; + 6 x 4 -
> 40/56 Mk 1.2, 2x SG, SK, Mk 4 radars. CT was removed.」

**波特兰级的改装表**（https://www.navypedia.org/ships/usa/us_cr_portland.htm）：

> 「early 1942, both: - 8 x 1 -12.7/90; + 4 x 4 - 28/75 Mk 1, 12 x 1 - 20/70
> Mk 4, SC, Mk 3, Mk 4 radars」
> 「5/1943, both: - 4 x 4 - 28/75, 1 catapult, SC radar; + 4 x 4 - 40/56 Mk 1.2,
> SG, SK radars. Portland can carry 2 seaplanes and Indianapolis 3.」
> 「autumn 1944, both: - Mk 3, Mk 4 radars; + Mk 8, Mk 18 radars」
> 「1/1946, Portland: 3 x 3 - 203/55 Mk 14, 8 x 1 - 127/25 Mk 19, 4 x 4 - 40/60
> Mk 2, 4 x 2 - 40/60 Mk 1, 17 x 1 - 20/70 Mk 10, 1 catapult, 2 seaplanes,
> SG, SK, Mk 8, Mk 18 radars」

**naval-encyclopedia 的独立记述**（交叉核对用）：

> 「The Portland class started the war without radar. They were however fitted in
> early 1942 with an SC, Mk 3, and Mk 4 radars. By May 1943, they received SK
> radars in addition.」
> 「starting in early 1942: Four quadruple 1.1in were fitted abreast the bridge
> and close to the 5in guns. Later, twelve 20mm guns were added instead of the
> twin 0.5 in cal HMGs.」
> 「The AA saw four extra quadruple and four twin 40 mm Bofors, plus 12
> supplementary 20 mm Oerlikon guns.」
> —— https://naval-encyclopedia.com/ww2/us/portland-class-heavy-cruisers-1931.php

### 4.9 编制

| 舰 | 值 | 原句 | 来源 |
|---|---|---|---|
| Astoria 级 | 868 | 「Complement \| 868」 | navypedia-neworleans |
| Astoria DANFS | 899 | 「cpl. 899」 | danfs-astoria |
| Astoria navsource | 800 | 「Crew 800」 | navsource-astoria |
| Astoria 战时实载 | 1,074 | 「83 officers, 990 enlisted men, and one civilian … on board」 | ussastoria-org |
| Portland 级 | 807 | 「Complement \| CA33: 807  CA35: 917 inc flag」 | navypedia-portland |
| Portland DANFS | 848 | 「cpl. 848」 | danfs-portland |
| Portland navsource | 621 | 「Crew 621」 | navsource-portland |
| 两级 HyperWar | 1042-1121 / 1229-1382 | 「Complement:1042-1121」「Complement: 1229-1382」 | https://www.ibiblio.org/hyperwar/USN/ships/ships-ca.html |

**这八个数字没有一处说明自己的口径**（平时/战时、含不含航空分队与旗舰人员），
所以本文件全部并列，不做合并。

---

## 5. 卡住的地方（明确「未获取」，不是漏查）

| 项 | 试过哪些站点 | 为什么不写 |
|---|---|---|
| **装甲总重（t）** | navypedia 两级页、DANFS、navsource、HyperWar 索引、WDR No.29 | 只有 navypedia 一句「protection weight made 15% of standard displacement」给出**比例**。用 15% × 10,136 t 反算属推算，红线 §1.1 禁止。**只有比例，没有吨数。** |
| **水下防护纵深（m）** | 同上四处 + navweaps 主炮页 | 两级都是条约型重巡，**没有防雷突出部**；navypedia 防护段逐句写完后没有一句提到纵深或 TDS。**不是没查到，是来源不说。** |
| **试航实测功率 / 试航航速** | navypedia、DANFS、navsource、HyperWar、ushmm、navalenc | 五处都只给设计值 107,000 hp / 32.5-32.7 kn。**两舰的试航实测数据一条都没有。** |
| **锅炉蒸汽压力 / 温度** | 同上全部 | 三级来源都没有。 |
| **发电机总功率 / 台数** | 同上全部 | 同上。 |
| **螺旋桨直径** | 同上全部 | 只知 4 轴，直径无来源。 |
| **造价** | 同上全部 | 无来源。 |
| **阿斯托里亚最终阵亡核定数** | DANFS（不给）、WDR No.29（只到「heavy」）、navsource（不给）、ussastoria.org（只有当时的 incomplete 数） | 唯一可用的是 1942-08 当时的「known dead 20 军官 + 138 水兵 + 2 失踪 = 160」，原文自注 `incomplete information now at hand`。**最终核定表未获取。** |
| **波特兰 1942-11-13 的伤亡数** | DANFS（不给）、navsource（只引 DANFS 同一段，不给数）、战损报告 No.35 正文（只在 navsource 图注里被引用，全文不可达） | 没有任何可达来源给出数字。**未获取。** |
| **波特兰实际拆解完成日期** | DANFS、navsource | 只有「1959-10-06 出售」，拆完时间无来源。 |
| **两舰 1941-1942 的对空搜索雷达具体型号** | navweaps 雷达页（**只列战列舰，巡洋舰一艘都没有**）、navypedia（级表只写「SC」）、ussastoria.org（只写「new air-search radar」，不给型号）、WDR No.29（不给型号） | DANFS 与 ussastoria.org 都只说「为装雷达建了基座」。**型号未获取。** navypedia 的「mid-1942, all: … SC, Mk 3 radars」是级表口径，不能直接套到单舰的具体日期上。 |
| **波特兰 1942-08-07/09 的编队** | DANFS（只说 cover and support）、navsource（无）、navalenc（无） | 最后从 NWC 萨沃岛报告第 3 章的兵力编成表查到是 **TG 61.1.2**（见 §3.3）。**这一项算查到了，列在这里是因为它差点被漏掉。** |
| **两舰主机的逐舰制造厂** | navypedia（级表给 Westinghouse / Parsons）、DANFS、navsource | 级表口径，逐舰实际装机厂无来源。 |
| **阿斯托里亚 1941-07 与 1942-06 两次改装的精确日界** | DANFS（只说「出坞日 1941-07-11」）、ussastoria.org（1941-07-09 照片、1942-06-14 换舰长）、navypedia（「6.1941」「mid-1942」） | 三个来源都不给「改装完成日」，只有出坞日与照片日期。本文件的 valid.from 取 1941-07-11（DANFS 出坞日）与 1942-06-14（换舰长日，ussastoria.org 原文），并在各 fact 的 note 里写明这是「可见的最早日期」而非「改装完成日」。 |

---

## 6. 有争议的记载（两边原话并列，一律不裁决）

### 6.1 阿斯托里亚的服役日：1934-04-28 vs 1934-06-01

- **DANFS**：「commissioned on 28 April 1934, Capt. Edmund S. Root in command.」
- **navsource**：「Commissioned 28 APR 1934」
- **navypedia**（船舶表）：「1.6.1934」

**两源对一源，且 navypedia 同页的下水日 16.12.1933 与另两源一致**——
说明它的日期栏本身没系统性偏移，只是服役日这一格错了。
本文件取 **1934-04-28**（DANFS 是官方来源，navsource 独立吻合）。

### 6.2 阿斯托里亚中弹数：65 发 vs 约 63 发

- **DANFS**：「Suffering from the effects of at least 65 hits」
- **WDR No.29**：「ASTORIA sustained an unknown number of hits from 8", 5", and
  20mm projectiles of which about 63 were reported in references (a) and (b).」

DANFS 写「at least 65」，报告写「about 63」，且报告自己注明这是「reported in
references (a) and (b)」的转述值。**两说并列。**

### 6.3 阿斯托里亚主炮齐射数：10 次 vs 12 次

- **CAPT Greenman 战报**（ussastoria.org 转录）：「Estimate ten salvos were
  fired by main battery」
- **DANFS**：「When the turret responded with Astoria's 12th and final salvo,
  the shells missed Kinugasa but struck the number 1 turret of Chokai.」

DANFS 说的是「第 12 次也是最后一次齐射」，战报说的是「估计打了 10 次」。
**注意这个 12 是 DANFS 的叙述，不是战报原话**——战报本身只说「ten salvos」。
两说并列，本文件记在 `armament.gun_failures` 的 note 里。

### 6.4 波特兰级航速：32.5 kn vs 32.7 kn

- **navypedia**：「Max speed, kts \| 32.5」
- **HyperWar 舰级索引**：「Speed: 32.5 knots」
- **DANFS**：「s. 32.7 k.」
- **navsource**：「Speed, 32.7 Knots」

**两派对峙，各两个来源。** 本文件按 navypedia 存 32.5，**但这不是裁决**。

新奥尔良级同类问题：navypedia 32.7 / DANFS 32.7（一致），
但 navsource 只给它 32.0（「Speed, 32.0 Knots」）——单源孤例。

### 6.5 波特兰级满载排水量：12,755 t vs 13,767 t

- **navypedia**：「Displacement full, t \| 12755」
- **HyperWar 舰级索引**：「13,767 tons (full load)」

相差 1,012 t，大到不像是单纯单位换算误差（1 长吨 = 1.016 t，
1,012 t 的差额不能用换算解释）。两源都没说明各自的载荷状态，
**无法判定哪个是深载。两说并列。**

### 6.6 波特兰级编制：四个数字全不一样

| 来源 | 原句 | 值 |
|---|---|---|
| navypedia | 「Complement \| CA33: 807  CA35: 917 inc flag」 | 807（CA33） |
| DANFS | 「cpl. 848」 | 848 |
| navsource | 「Crew 621」 | 621 |
| HyperWar 索引 | 「Complement: 1229-1382」 | 1229-1382 |

621 与 1,382 差一倍多，不可能是同一状态。**没有任何来源说明口径。**

### 6.7 波特兰级炮塔厚度：64 mm vs 2.5 in（63.5 mm）

- **navypedia**：「Turrets had 64mm faces, 25mm sides, 19mm rears and 51mm
  crowns.」
- **navsource**：「2 1/2 Turrets」（2.5 in = 63.5 mm）

这两个其实是同一个数（64 ≈ 63.5，是英制/公制取整差），**不是分歧**，
本文件按公制取 64 mm，note 里注明 navsource 的英寸原值。

### 6.8 阿斯托里亚 1941 年 1.1 英寸炮改装时间：1941-06 vs 1941-07

- **navypedia**：「Astoria, 6.1941; … : + 4 x 4 - 28/75 Mk 1」
- **DANFS**：「Emerging from the yard on 11 July 1941」
- **ussastoria.org**：照片日期 1941-07-09，「one of the ship's four new
  1.1-inch antiaircraft mounts」

navypedia 说的是「改装动作发生在 6 月」，DANFS 说的是「7 月 11 日出坞」——
**很可能是同一件事的两个节点（装炮 vs 出坞），不是矛盾。**
本文件 valid.from 取 1941-07-11（出坞日，三源里唯一给了确切日期的一天），
note 里并列 navypedia 的 1941-06。

### 6.9 阿斯托里亚在萨沃岛的舰载机数：4 架 vs 5 架

- **navypedia 级表**：「4 seaplanes (OL, O2U, O3U, OJ)」
- **WDR No.29**：「The five airplanes on each ship except QUINCY had been
  drained of all gasoline.」

级表给的是设计载机量，战报给的是当晚实数。**两者不矛盾**，
但两个字段都容易误读，故本文件把 4 记在 `aviation.aircraft.capacity`、
把 5 写在那条 fact 的 note 里。

### 6.10 naval-encyclopedia 关于 1944 年秋雷达改装的自相矛盾

同一句：

> 「In the autumn 1944 their electronics suite was duly modernized and both were
> installed Mk 3, Mk 4 radars and Mk 8, Mk 18 radars.」

**先说「现代化改装」，接着说「装了 Mk 3, Mk 4, Mk 8, Mk 18」**——
但 navypedia 的对应记录是「- Mk 3, Mk 4 radars; + Mk 8, Mk 18 radars」，
即 **Mk 3/4 是拆掉的，不是装上的**。navalenc 这句像是把「拆」写成了「装」
或者把「原有 + 新增」混在一起列了。

本文件按 navypedia 记录（拆 Mk3/4、装 Mk8/18），
navalenc 的措辞问题记在这里。

### 6.11 波特兰级 1943-05 的 40 mm 总数：16 管 vs 24 管

- **navypedia**：「+ 4 x 4 - 40/56 Mk 1.2」= 16 管
- **navalenc**：「The AA saw four extra quadruple and four twin 40 mm Bofors」
  = 4×4 + 4×2 = 24 管

navypedia 的改装条只写四联装，没提双联；navalenc 多给了 4 座双联。
**两说并列，本文件存 24（含双联），并在 note 里写明 navypedia 只记 16。**

---

## 7. 三条「否定证据」是怎么立起来的

写资料站最容易糊弄的是「0」和「未获取」这两件事。本组有三处 0，
每一处都不是「没查到」而是「有独立来源证明它是 0」：

### 7.1 40 mm Bofors = 0（中途岛时）

- **正面**：navypedia 的 40 mm 首次出现时间——新奥尔良级是「late 1943, all
  survived」，波特兰级是「5/1943, both」。**阿斯托里亚 1942-08-09 沉没，
  从未进入 late 1943 那次改装。**
- **佐证**：navweaps 40 mm 页「Date In Service … USA: 1942」——
  1942 年才服役，中途岛时美军重巡普遍还没装。
- **级表佐证**：navypedia 建成配置里根本没有 40 mm 这一项。

### 7.2 鱼雷发射管 = 0

- **波特兰级**：navypedia 有否定句「Portland class differed from predecessors
  by absence of TTs」——**这是明文否定，最硬。**
- **新奥尔良级**：三份独立的逐项枚举式武备清单（navypedia Armament 行、
  navsource 装甲/武备行、DANFS 舰首行）都列全了主炮/副炮/机枪/飞机，
  **唯独没有鱼雷管**。三份清单都不约而同地漏掉同一项，
  与「本来就没有」比「三家都漏记」更合理。

### 7.3 25 mm 高炮 = 0

- navypedia 的完整武备清单里没有任何 25 mm 项。美舰不用日制 25 mm。
- 这一条本可以不写（谁都知道美舰不装日炮），但它能防止
  「同级舰横向对比时 25 mm 那栏留空被误读成没查完」。

---

## 8. 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 2（`classes/new-orleans.yaml`、`classes/portland.yaml`） |
| 单舰文件 | 2（`ships/astoria.yaml`、`ships/portland.yaml`） |
| 切片文件 | 0（见下） |
| 正文文件 | 0（见下） |
| 新登记来源 | 13 |
| fact 总数 | 228（级 83+56，舰 44+45） |

**关于切片与正文：** 任务书列的交付清单里只有
`classes/` × 2、`ships/` × 2、`sources-fragment.yaml`、`RESEARCH-NOTES.md`，
**没有要求 `slices/` 与 `articles/`**。所以这两个目录留空。
如果主会话还需要这两类文件，本底稿里的时间线材料（§4.6 / §4.7 的逐条原句、
§4.8 的改装表）足以直接生成切片，不需要重新抓取。

### 8.1 骨架字段覆盖

SCHEMA §3.1 的 35 个骨架字段，**33 个已填**，2 个明确「未获取」：

| 未填字段 | 原因 |
|---|---|
| `protection.armor.weight` | 只有比例（15%）没有吨数，反算属推算（§5） |
| `protection.underwater.depth` | 两级无防雷突出部，来源不给纵深（§5） |

另：`dimensions.length.pp`（垂线间长）、`dimensions.beam.max`、
`construction.cost`、`propulsion.power.trial`、`propulsion.speed.trial`
等**不在 35 个骨架内**的字段也有缺口，一并记在 §5。

### 8.2 自检结果（SCHEMA §10）

```
$ python -c "import yaml,glob;[yaml.safe_load(open(p,encoding='utf-8'))
  for p in glob.glob('work/staging/tg172/**/*.yaml',recursive=True)];print('yaml ok')"
yaml ok

$ python work/staging/tg172/_validate.py
ERRORS 0
WARNS 0
```

`_validate.py` 逐条检查了：
- [x] 每条 fact 的 `field` 都在 `data/fields.yaml` 里
- [x] 每条 fact 都有 `src`，且 src 全部能在 `sources-fragment.yaml` 或
      `data/sources.yaml` 里解析（实测 0 条悬空）
- [x] 每个带单位字段的 `unit` 与注册表一致（`unit: null` 的字段一律不写 unit）
- [x] `protection.armor.*` 全部带 `qual`，且 `part`/`region` 两个键都给，
      取值都在注册表允许列表内
- [x] 没有 `confidence: D`
- [x] 没有用 tier E 来源支撑 fact（本组唯一 A 级是 WDR No.29，无 E 级）
- [x] `enum` 字段的值都在注册表 `values` 里
- [x] 没有编造的数字（见 §5 的「未获取」清单与 §6 的并列清单）

另查：正文里没有出现「据说/有人认为/有人称/据信/或许/大概/应该是」——
```
$ Select-String -Path "work/staging/tg172/classes/*.yaml",
    "work/staging/tg172/ships/*.yaml" -Pattern "据说|有人认为|据信|或许|大概|应该是"
（无输出）
```

### 8.3 与 `data/sources.yaml` 的去重

开工前先做了重复检查（任务书要求）。**复用了 4 条已登记来源，没有重复登记：**

| 复用 id | 原条目 tier | 本组用途 |
|---|---|---|
| `navweaps-5in25-mk10` | C | 副炮 5"/25 全部数据 |
| `navweaps-11in75-mk1` | C | 1.1"/75 高炮全部数据（中途岛时两舰的防空主力） |
| `navweaps-20mm-oerlikon` | D | 20 mm 厄利孔（1942 年两舰已装） |
| `navweaps-40mm-bofors` | D | 证明 40 mm 服役年 1942、中途岛时未装 |

**新登记 13 条**，全部在本组第一次出现（逐条 id 与 `data/sources.yaml`
现有 363 条做过字符串比对，无碰撞）。其中：
- tier A × 1（WDR No.29）
- tier B × 2（DANFS 两舰，ibiblio 转录本）
- tier C × 4（navweaps 8"/55 两页、navweaps 雷达页、NWC 萨沃岛报告）
- tier D × 6（navypedia 两级、navsource 两舰、ussastoria.org、navalenc）

### 8.4 `access` 字段的三个取值要说明

本组 13 条来源里，`access` 有 `direct` 与 `proxy` 两类。`proxy` 的 4 条
**不是走代理服务器，是走 web.archive.org 快照**：

| id | access | 原因 |
|---|---|---|
| `nhhc-wdr29` | proxy | history.navy.mil TLS 握手即断 |
| `navsource-astoria` | proxy | navsource.org 返回 502 |
| `navsource-portland` | proxy | 同上 |
| `ussastoria-org` | proxy | 原站已跳转域名停放页 |

**这四条的 `url` 字段记的是 Wayback 快照 URL，不是原站 URL。**
理由：原站 URL 在本机取不到内容，而 `sources.yaml` 的 `url` 是用来
回溯取证的，记一个取不到的地址等于没有。原站地址已写进各条的 `note`。
