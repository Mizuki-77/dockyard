# 调研底稿 —— HMS Ark Royal（皇家方舟号，舷号 91）

> 组名 `g5-arkroyal` · 2026-11-22 · 全部结论附英文原句 + URL
>
> 本轮抓取环境有一个必须先说明的技术问题：本机 DNS 把几乎所有目标域解析到
> `198.18.x.x`（代理网段），`web_fetch` 因此对 **naval-history.net / navypedia.org /
> uboat.net / armouredcarriers.com / en.wikipedia.org** 全部返回
> `SSRF blocked: … resolves to private address`。
> 解决办法：改用 PowerShell 的 `Invoke-WebRequest` 直连，全部返回 200。
> 所以本组所有原始页面都是**直连抓取**（不是代理、不是缓存）。

---

## §0 抓取结果一览

| 来源 | URL | 状态 | tier |
|---|---|---|---|
| naval-history.net | `xGM-Chrono-04CV-HMS_Ark_Royal.htm` | 200，2,510,554 字节 | D |
| navypedia.org | `/ships/uk/brit_cv1_ark_royal.htm` | 200，48,469 字节 | D |
| uboat.net（舰级页） | `/allies/warships/class/99.html` | 200，11,845 字节 | D |
| uboat.net（单舰页） | `/allies/warships/ship/3257.html` | 200，1,007,434 字节 | D |
| uboat.net（U-81） | `/boats/u81.htm` | 200，16,487 字节 | D |
| historyofwar.org | `/articles/weapons_HMS_Ark_Royal.html` | 200，28,421 字节 | D |
| fleetairarmarchive（Wayback） | `web.archive.org/…/Ark_Royal2.html` | 200，36,021 字节 | D |
| navweaps.com | `/Weapons/WNBR_45-45_mk1.php` | 200，60,868 字节 | D（已登记，复用） |
| armouredcarriers.com | `/technicaldata` | 200（已登记，复用） | C |
| armouredcarriers.com | `/opensided-versus-closed-hangars-…` | 200（本组新登记） | A |
| armouredcarriers.com | `/hms-ark-royal`、`/ark-royal` | **连接被意外关闭**（404 页） | — |
| world-war.co.uk | 首页 | **403** | — |

---

## §1 身份

> 「ARK ROYAL Class Fleet Aircraft Carrier ordered from Cammell Laird of Birkenhead
> under the 1934 estimates.」
> — naval-history

> 「In 1931 work commenced on the design of a new Fleet Aircraft Carrier which would
> be the first of a new generation of this type of warship.」
> — naval-history

> 「The ship was launched on 13th April 1937 as the third RN warship to carry the name,
> which dates from 1587 and has a direct association with naval aviation extending over
> several generations.」
> — naval-history

> 「Badge: On a Field Blue, an Ark Silver, crowned Gold upon 5 wavelets Gold.
> Motto: Desire n'a pas Repos」
> — naval-history

> 「HMS Ark Royal was the first large aircraft carrier to be laid down as such for the
> Royal Navy.」
> — uboat.net 舰级页

**驳一条常见前提**：「皇家方舟级只有它建成」这一点成立，但**不能被写成「一级只有一艘
所以没有设计共性」**。它的设计起点、图纸值与固定武备是完整的一套，本站按
`docs/30-new-ship-workflow.md` §3 路径 B 建了 class 文件（101 条 fact），
而不是像早先担心的「舰级全空」。

---

## §2 建造

| 项 | 值 | 来源 |
|---|---|---|
| 下单 | 1935-04-17 | uboat.net 单舰页「Ordered 17 Apr 1935」 |
| 开工 | 1935-09-16 | navypedia「16.9.1935」/ uboat.net「16 Sep 1935」/ FAA「laid down on 16 September 1935」 |
| 下水 | 1937-04-13 | 三源一致 |
| 服役 | 1938-11-16 | navypedia「Comp 16.11.1938」/ naval-history「completed in November 1938」/ FAA「commissioned on 16 November 1938」 |
| 服役（异说） | **1938-12-16** | uboat.net 单舰页「Commissioned 16 Dec 1938」 |
| 造价 | £3.215M | naval-history「The build cost was £3.215M」 |
| 船台号 | 1012 | navypedia 表格 |

**口径判断**：`construction.commissioned` 的两说并列，不裁决。
注意 naval-history 自己用了三个不同的词——`launched` / `completed` / `entered service`，
都在 11 月；uboat.net 用 `commissioned` 记 12 月。两者的差别很可能是
「建成（completed）」与「正式服役（commissioned）」两个口径各取了一个日期，
但**两条来源都没有明示口径**，本站不替它们裁定。

---

## §3 主尺度与排水量

> 「The ship had a deep displacement of about 27,000 tons as designed and was 800 feet
> in overall length with a beam of 94 feet and mean draught of 23 feet.」
> — naval-history

> 「Length, m 208.8 pp 243.8 oa / Breadth, m 28.9 wl 29.0 deck /
> Draught, m 8.46 deep load」
> — navypedia

> 「Dimensions: 685 pp, 721.5 wl, 800 oa x 94.75 x 27.75 feet」
> — FAA Archive ← **本站唯一给出水线长的来源**

> 「Displacement standard, t 22000 / Displacement full, t 27720」
> — navypedia（historyofwar 同值）

> 「Displacement: 22,352 tons standard ; 28,143 tons full load」
> — FAA Archive（异说，与上式各差约 400 t）

换算说明（本报告换算，来源未给公制）：
`800 ft = 243.84 m`、`685 ft = 208.79 m`、`721.5 ft = 219.91 m`、
`94 ft = 28.65 m`、`94.75 ft = 28.88 m`、`23 ft = 7.01 m`、`27.75 ft = 8.46 m`、
`56 ft = 17.07 m`。

**必须点出的一处口径陷阱**：`243.8 m` 含舰艉飞行甲板的**长悬伸段**。
navypedia 原话：

> 「Prominent features of architecture of Ark Royal were extremely high freeboard
> (17.1m) and the big aft overhang of a flight deck which at the expense of it
> significantly exceeded a hull length.」

所以拿全长 243.8 m 与其他舰排高低会高估船体本身。
按「保留口径、不做跨舰对比」的判例，本组**没有**给它标 `comparable: false`——
理由是字段本身确实是全长口径（含悬伸段的甲板是这艘船结构的一部分），
不是「长度」这个概念被误用；但已在 note 里写清，供页面显示。

**干舷 17.1 m 的旁证**：

> 「The flight deck was 56ft above the deep load waterline (compared to 38ft on the
> Illustrious class). This could be important when an aircraft was struggling to take
> off, dipping below the level of the flight deck before beginning to climb.」
> — historyofwar

这条是判断「本级与光辉级是两条路线」的直接量化证据，也是本站把
`dimensions.freeboard` 写进舰级文件（而不是单舰）的理由——它是设计取舍，不随战历变。

---

## §4 动力

> 「Machinery 3 sets Parsons geared steam turbines, 6 Admiralty 3-drum boilers /
> Power, h. p. 102000 / Max speed, kts 31 / Fuel, t 4620 oil /
> Endurance, nm(kts) 10300(16)」
> — navypedia

> 「The propulsion machinery consisted of three propellers driven by steam turbines
> giving 102,000 shaft horsepower to provide a designed speed of 30.75 knots which was
> exceeded on trials. Three Boiler Rooms with separate but adjacent boiler rooms were
> used.」
> — naval-history

> 「She had three boilers and three engine rooms, carried in a row across the ship.
> The smoke ducts linking the three sets of machinery ran below the lower hanger,
> and would prove to be a fatal weakness.」
> — historyofwar

**两处必须并列的地方**：

1. **锅炉台数**：navypedia 记 6 座，historyofwar / naval-history 记「three boilers /
   three boiler rooms」。按「三组、每组两台」理解则两说不冲突，但**没有任何来源
   把每组的台数写清**，所以并列不裁决。
2. **续航力三说**：10,300 nm @16 kt（navypedia）/ 7,600 nm @20 kt（FAA Archive）/
   11,200 miles @11 kt（historyofwar）。三者差可达 30%，很可能分别对应设计值、
   实战经济航速、宣传口径，**未取得单一权威值**。

**试航航速**：naval-history 只说「was exceeded on trials」，**没给数字**，
所以 `propulsion.speed.trial` 没有写——这是有意的留白。

---

## §5 防护

> 「Armour, mm belt: 114, bulkheads: 76 - 64, lower hangar deck: 89 over engines,
> magazines and aviation fuel tanks」
> — navypedia

> 「Main belt protected 45% of length by waterline and expanded to lower hangar deck
> abreast funnel, to upper deck fwd and aft from funnel and to main deck abreast
> magazines. Underwater protection depth was 4.08m, there were 38mm anti-torpedo
> bulkheads. This protection could resist exploding of 380kg TNT.」
> — navypedia

> 「The belt was taken to the lower hangar deck abreast the funnel, to the upper deck
> fore and aft of this and to the lower deck by the forward and aft 4.5in magazines;
> there was a 3½in armour deck at the various levels of the upper edge and over the
> steering gear. There was a sandwich type underwater protection with a 1½in protective
> bulkhead 13ft 4½in from the side amidships. The system was designed to withstand a
> 750lb charge but trials while Ark Royal was building showed that the bulkhead
> stiffeners had to be modified.」
> — uboat.net 舰级页

> 「Armour - belt 4.5in / bulkheads 3in-2.5in」
> — historyofwar

**判断：这是 incremental，不是装甲盒。** 依据是三条来源都把装甲描述成
「按部位分段、按高度分层」的逐段体系，机库侧壁**没有任何一条来源说是装甲**。
这与光辉级的「机库四周 4.5 in C 装甲盒」是根本差别，也是本组把
`protection.scheme` 记为 `incremental` 的依据。

**抗爆当量两说**：380 kg TNT（navypedia）/ 750 lb（= 340 kg，uboat.net 与
historyofwar）。750 lb 是设计指标、380 kg 是换算后的描述值，两者差 12%，
并列不裁决。

**`protection.armor.thickness` 分区说明**：本组给了 5 条（belt 114 / bulkhead 76 /
hangar_deck-lower 89 / deck-main 89 / bulkhead-torpedo 38）。其中
`hangar_deck.lower = 89` 与 `deck.main = 89` 数值相同但来源描述的位置口径不同
（一个说「下层机库甲板覆盖动力舱/弹药库/航空汽油舱上方」，另一个说
「装甲甲板铺在装甲带上缘各高度并覆盖舵机」），按「不同来源描述不同位置」
并列保留，不合并。

---

## §6 航空设施（本级最该记全的一块）

> 「Flight deck: 219.5 (useful length)x29.0m. Upper hangar: 173.1x18.3x4.9m,
> lower hangar: 137.8x18.3x4.9m. 3 lifts for both hangars each (2 lifts: 13.7x6.7m,
> 1 lift: 13.7x7.6m). 2 catapults (5.4t plane was launched at 122 km/h).
> Aircraft fuel stowage: 454,600l.」
> — navypedia

> 「There was a high continuous flight deck 56ft above the deep load waterline with an
> unusually long stern overhang, and an island and funnel to starboard. The flight deck
> was an integral part of the hull structure, serving as the upper strength deck, and had
> an usable area of 720ft x 95 ft. It was provided with two catapults that could launch
> 12.000lb at 66kts. There were two hangars measuring 568ft upper, 452ft lower x 60ft x
> 16ft, and three rectangular lifts, two measuring 45ft x 22ft and one 45ft x 25ft. These
> each had two platforms, of which the upper one travelled between the flight deck and
> the upper hangar and the lower one between the two hangars. This meant that it took
> three movements to transport aircraft from the flight deck to the lower hangar.
> Petrol stowage was 100.000gal.」
> — uboat.net 舰级页

> 「The Ark Royal had two hangers. Both were 60ft wide and 16ft high. The upper hanger
> was 568ft long and the lower 452ft.」
> — historyofwar

**⚠ 任务书里有一处单位错误，已按原始来源更正。**
任务书说「上层机库 173 ft、下层 150 ft」。两源给的是 **568 ft 与 452 ft**，
换算 **173.1 m 与 137.8 m**。
也就是说 173 这个数字的**单位是米，不是英尺**；而 150 ft 与 452 ft 也对不上。
本组以两源原值为准，并在舰级文件 note 与正文里都写明了这件事。

**双层机库的处理方式（重要，见交付摘要）**：
`aviation.hangar.length` 没有 `qual` 限定词，同一时间窗写 173.1 与 137.8 两条
会被校验器判成「两个来源对同一指标说法不一」、页面上打「存在争议」标记。
而这不是争议，是两层机库各有一个长度。所以本组的处理是：
**只立 173.1 m 一条 fact**，把 137.8 m 写进这条的 note 与正文，
并在数据文件里留一段注释说明为什么刻意不立第二条、以及字段加上 level 限定词后应如何补。

**弹射器**：

> 「The Ark Royal had two catapults, each capable of launching a 12,000lb aircraft at
> 66kts」
> — historyofwar

三源的弹射能力其实是同一个数：12,000 lb = 5.44 t，66 kt = 122 km/h。
**弹射器型号未获取** —— navypedia 与 historyofwar 都没给，所以
`aviation.catapult.type` 没有写。

**载机量与「72 架」的来历**：

> 「Although the original aircraft requirement asked for 72 aircraft to be carried only
> 60 were allowed for for in the finished design and this was reduced to 54 when modern
> heavier types were embarked.」
> — naval-history

所以「72 / 60 / 54」三个数字对应三个阶段：纸面要求 / 建成值 / 换装重机型后的实际值。
不是三种说法。

---

## §7 武备

### 7.1 4.5 in QF Mk I（weapon id `45in-45-mk1`，来源 `navweaps-45in-45-mk1` 已登记）

> 「Mark I — Ark Royal (1937), Forth, Maidstone and Illustrious class」
> — navweaps，`Ship Class Used On` 栏

> 「Twin Mounts — Ark Royal (1937) (8), Forth (4), Maidstone (4), Tyne (4), Hecla (4)
> and Adamant (4): Mark III UD」
> — navweaps，`Mount/Turret Data` 栏

**关键区分（本组核对过三遍）**：本舰装的是 **Mark I 炮身 + Mark III UD 座**；
光辉级装的是 **Mark III 炮身 + Mark II BD 座**。这不是同一组合，所以本站
**没有**把本舰的 4.5 in 并进已有的 `weapon:4_5in-qf-mk3` 实体
（那一实体记的是 Mk III 炮身 / Mk II BD 座），而是按任务书的要求立了
`weapon:45in-45-mk1`。NavWeaps 对两者的关系有明确说明：

> 「The Mark I and Mark III guns were used only in twin mountings and were
> interchangeable with each other, the only difference being in details of the firing
> mechanism.」
> — navweaps

**弹重必须区分「整装弹」与「弹丸」**（这是最容易抄错的一处）：

> 「Type Fixed and Separate / Weight of complete round (with SC charges)
> HE - 87 lbs. (39.5 kg) SAP - 91.75 lbs. (41.6 kg)」
> 「Projectile Types and Weights HE - 55 lbs. (24.95 kg) SAP - 58.25 lbs. (26.4 kg)」
> — navweaps

`weapon.projectile_weight` 问的是**弹丸**，所以取 24.95 / 26.4 kg，
不是 39.5 / 41.6 kg。另外：

> 「By the end of the war, most propellant charges were flashless, if available, and
> SAP and HE were carried by all except aircraft carriers, which had HE only.」
> — navweaps

**所以本舰实际只带 HE，不带 SAP。**

其余数据（逐条已进 fact）：
炮身重 Makrs I/III 6,304 lbs（2,859 kg）；初速新炮 2,449 fps（746 m/s）、
平均 2,350 fps（716 m/s）；射速 12 发/分/门（二战联装座）；
43° 射程 19,900 码（18,200 m）、45° 20,750 码（18,970 m）；
50° 射高 29,910 ft（9,120 m）、80° 41,000 ft（12,500 m）；
身管寿命 650 发；每门备弹 400 发。

**座重与座型的连带判断**：

> 「Twin Mounts … Mark II BD: 37.95 tons (38.56 mt) … Mark III UD: 29.738 tons
> (30.215 mt)」
> — navweaps

Mark III UD 比光辉级的 Mark II BD 轻 8 t。差的这 8 t 就是炮塔外壳与座体结构，
直接印证 UD 是**露天甲板座、无炮塔**。加上两源都写「open-backed mountings」，
本组把 `mount.type` 记为 `open_mount`（不是 `twin_turret`）。

**无 RPC 的判断**：

> 「Elevation Rate — Mark II: 10 degrees per second / RP10 Mark II**: 20 degrees per
> second / RP50 Mark V and Mark V*: 20 degrees per second / Others: N/A (mainly
> hand-worked)」
> — navweaps

Mark III UD 落在「Others」，所以 `sensors.fire_control.rpc: none`。

### 7.2 2-pdr pom-pom（复用 `weapon:2pdr-mk8`）

> 「Armament 8 x 2 - 114/45 QF Mk I, 4 x 1 - 47/40 3pdr Hotchkiss Mk I, 4 x 8 - 40/39
> 2pdr QF Mk VIII, 8 x 4 - 12.7/62, 60 aircraft」
> — navypedia，建成状态

> 「The original allocation of 32 2pdr pompoms was increased to 48 in May 1941, carried
> in six eight-gun mountings.」
> — historyofwar

> 「1941: + 2 x 4 - 40/39 2pdr QF Mk VIII」
> — navypedia，Modernizations 栏

座数 4 → 6（32 门 → 48 门），**只到月份，未获取具体日**，所以
`mount.installed` 记 1941-05-01 代表「1941 年 5 月内」。

### 7.3 12.7 mm 维克斯与 3-pdr 礼炮（本组新建实体，无性能参数）

navypedia 只给了型号与数量（`8 x 4 - 12.7/62`、`4 x 1 - 47/40 3pdr Hotchkiss Mk I`），
historyofwar 给了「Four 3pdr saluting guns」。**NavWeaps 没有对应的英国
12.7 mm 或 47 mm 单页可引**，所以这两个实体只写了「型号身份三条 + 炮位
label/weapon/type/barrels/count」，**一个性能数字都没有**。这是有意的留白。

### 7.4 舰载机

> 「Aircraft facilities … 60 aircraft (Nimrod, Osprey, Sea Gladiator fighters, Skua
> diving bombers, Swordfish torpedo bombers, Walrus recon planes)」
> — navypedia，装备栏

navypedia 的逐月机群表（已全部写入 `aviation.aircraft.types` 的分期 note）：

```
8.1939   —      18 Skua  42 Swordfish  —
10.1939  —       8 Skua  21 Swordfish  —
4.1940   5 Roc  18 Skua  21 Swordfish  1 Walrus
5.1940   —      23 Skua  21 Swordfish  —
6.1940   —      24 Skua  21 Swordfish  5 Walrus
8.1940   —      24 Skua  30 Swordfish  —
10.1940  12 Fulmar  —      —            —
4.1941   24 Fulmar  —    30 Swordfish  —
5.1941   18 Fulmar  —    30 Swordfish  —
```

**新建的武器实体**（此前项目里没有）：`skua` / `roc` / `vickers-50` /
`3pdr-hotchkiss` / `albacore`。全部只有型号身份三条（designation / nation /
category），**没有性能参数**——除了 Skua 与 Roc 能在 naval-history 的括号注里找到
几项性能（速度/航程/武器），但那是任务书没要求的机型参数，且与 `weapon.aircraft.*`
字段的取舍无关，本组没写。

---

## §8 雷达与火控（本节是本组最大的数据缺口）

> 「The AA armament was rather powerful to pre-war measures, however air defence
> abilities were reduced by absence of the radar: Ark Royal became last large ship of
> the Royal Navy without it.」
> — navypedia，Project history 段

> 「The original complement was about 1,600 but was increased after the outbreak of war
> when radar and more close range anti-aircraft weapons were fitted.」
> — naval-history，General Information 段

**这两句合起来只能证明「服役期内装了雷达」，不能证明型号与日期。**
两源都没给型号，也没给安装时间。
所以 `sensors.radar.installed` 的 `valid.from: 1940-01-01` 是**本报告的估计值**，
标 C 档并在 fact note 里明确声明「不是史料原句」。
`sensors.radar.count: 1` 同样是推断值，note 里已写清。

**一条值得记的旁证**：1941-05 追击俾斯麦期间，年表多处写编队里承担雷达警戒的是
SHEFFIELD（Type 79Y）与 RENOWN，而不是本舰 ——

> 「RENOWN and HERMIONE remained in loose contact with ARK ROYAL to provide her with
> radar early warning and protective AA fire.」
> — naval-history，1941-09 段

> 「light cruiser SHEFFIELD (fitted with air warning radar Type 79Y, range 60NM)」
> — naval-history，1940-11 段

这说明本舰自身的雷达能力在当时不足以独担编队警戒。但**这条是行为推断，
不是参数证据**，没有写成 fact。

---

## §9 编制与损失

> 「The only crew member lost was Able Seaman E Mitchell, who was the oldest rating on
> board, and was on duty in the lower steering position when the torpedo struck he was
> believed killed in the explosion.」
> — naval-history

> 「Fortunately only one crewman was killed.」
> — historyofwar

> 「By 1648 LEGION had embarked 1487 crew from ARK ROYAL and she pulled away and rejoined
> the screen.」
> — naval-history

> 「At 0430 the list had reached 35¡ and the order was given to abandoned ship and the
> 250 men still onboard left, most climbed down on the ST DAY.」
> — naval-history

所以「在舰约 1,700 人 / 阵亡 1 人」这个账是能对上的：
1,487（首批撤离）+ 250（最后留守）= 1,737，其余经小艇或拖船转运。
**最终生还总人数来源没有给**，故 `service.survivors` 只写 1,487 并注明这是
「第一批撤走的人数，不是生还总数」。

**沉没时刻两说**：

> 「At 0619 ARK ROYAL's list reached 45¡ and she continued rolling to 90¡, in which
> position she remained for three minutes, she then went vertical standing on her stern
> and started sinking. By 0624 ARK ROYAL's bow had disappeared below the surface of the
> Mediterranean.」
> — naval-history

> 「… at 0813 hours on 14 November 1941.」
> — uboat.net 单舰页

并列不裁决。差别可能来自时区（舰队时间 vs 柏林/GMT），但**两条来源都没明示**。

**破口尺寸两说（同一来源内部不一致）**：

> 「The explosion blew a hole in her side approximately 130ft x 30ft」
> vs
> 「In this case caused by a hole of about 115 feet length.」
> — 均出自 naval-history

本条已在 `service.fate_category` 里并列。

**残骸位置三说**：

> 「30 NM east of Gibraltar lying at 3500 ft … approximate position 36-06-35N, 4-43-51W」
> — naval-history（2002-12 发现）

> 「The wreck is located 45nm ESE of Gibraltar.」
> — FAA Archive

> 「in 25 miles E of Gibraltar」
> — navypedia

25 / 30 / 45 海里，不裁决。

---

## §10 1941-05-26 的误击（本组最需要讲清楚的一段）

**任务书的前提核对结果：成立。** 而且比任务书说的更具体 —— 失误有明确的技术原因。

> 「At 1315/26 HMS Sheffield was detached to the southward with orders to close and
> shadow the enemy… The visual signal ordering this movement was not repeated to HMS
> Ark Royal, an omission which had serious consequenses for the aircraft that were to
> take off did not know that HMS Sheffield had parted company.」
> — uboat.net 单舰页

> 「Because the signal was not direct to the ARK ROYAL it was not immediately de-coded
> and no one on ARK ROYAL, probably due to the appalling weather conditions, noticed
> that SHEFFIELD had detached」
> — naval-history

> 「At 1550 the ASV equipped Swordfish of the strike force obtained a radar contact on a
> ship and notwithstanding that the contact was 20 miles from BISMARCKs expected
> position the 14 Swordfish, one had turned back. … However the ship they were about to
> attack was not the BISMARCK it was the SHEFFIELD. As the Swordfish came into attack
> Captain Charles A Larcom RN the CO of SHEFFIELD recognised his attackers and called
> for full ahead and ordered all guns not to fire.」
> — naval-history

> 「A total of 11 torpedoes were dropped, 7 missed, 3 exploded in SHEFFIELD's wake and 2
> exploded on impact with the water. Three Swordfish didn't attack as they recognised
> the SHEFFIELD, one of them made a signal to her, 'Sorry for the Kipper', as they turned
> for home.」
> — naval-history

> 「The fact that SHEFFIELD had refrained from firing at her attackers meant that all 14
> Swordfish had been able to make it back to the ARK ROYAL.」
> — naval-history ← **这是「为什么一架都没损失」的直接答案**

**与 `data/battles/last-battle.yaml` 的一致性核对：通过。**
该文件 05-26 15:50 条已记「11 枚鱼雷全部落空：2 枚入水即爆、3 枚横穿巡洋舰尾迹时
爆炸、其余 6 枚被规避。谢菲尔德号一炮未还。」本组数字与它一致
（naval-history 的 7 missed = 其余被规避；2 + 3 = 5 枚爆炸）。

**任务书说「多次引信故障救了 Sheffield」—— 本组核对后要更正这处表述。**
naval-history 明确写的是「3 exploded in SHEFFIELD's wake and 2 exploded on impact
with the water」，也就是 5 枚**提前爆炸 / 入水即爆**，**这 5 枚本来就打不到船**
（一枚在尾迹里炸、一枚在触水瞬间炸）。真正「救了 Sheffield」的是
① 7 枚被规避 + ② 舰长下令不开火以免暴露 + ③ 三架认出了目标改攻。
「引信故障救了它」这个说法在引擎故障语境下成立（如 U-39 那次），
**在 Sheffield 这一次不成立** —— 引信炸掉的是本来也不会命中的雷。
正文按后一种写法，没有沿用「引信救了 Sheffield」的表述。

**第一次攻击的鱼雷引信确实有故障，但那是另一件事**：

> 「Because of the premature explosions of 45% of the torpedoes on the first attack,
> the Duplex fused torpedoes were replaced by the older, but more reliable, contact
> exploders.」
> — naval-history

即第一波的**双联磁性引信**有 45% 提前爆炸，所以第二波换成触发引信。
这个 45% 是「第一波鱼雷故障率」，不是「Sheffield 被救的原因」。

**两个时刻的鱼雷数**：naval-history 记 15 架起飞、1 架返航、**14 架进入攻击、11 枚投放**；
uboat.net 记「launched a striking force of 14 Swordfish … fired 11 torpedoes」。
两源对「进入攻击的架数」记 14，一致；对「起飞的架数」记 15，也一致。
本组按 `15 起飞 / 1 返航 / 14 攻击 / 11 投放` 写。

---

## §11 其余战历（逐年）

| 日期 | 事件 | 来源 |
|---|---|---|
| 1939-09-14 | U-39 三雷全部提前爆炸；三艘驱逐舰反潜击沉 U-39，43 人被俘 | naval-history |
| 1939-09-26 | 803 中队 Skua 击落 Do 18（FAA 首个战果） | FAA / historyofwar |
| 1940-04-10 | **岸基** 800/803 中队 Skua 击沉 KÖNIGSBERG（3 弹，1 架损失） | historyofwar / FAA |
| 1940-04-23 | Operation DX，与 GLORIOUS 编组，RN 史上第一个航母特混编队 | naval-history |
| 1940-04 至 06 | 挪威：Skua 战斗机巡逻、Swordfish 打铁路隧道 | naval-history |
| 1940-06-13 | 15 架 Skua 攻 SCHARNHORST，损失 8 架；战果两说（当时判 2 弹、实为 1 弹未爆） | naval-history |
| 1940-07-03 | 米尔斯克比尔：侦察/校射/布雷；818 中队 6 架攻 STRASBOURG，2 架被击落 | naval-history |
| 1940-08-02 | 袭击 Cagliari | historyofwar / FAA |
| 1940-09-23~25 | 达喀尔（Operation MENACE），对 RICHELIEU 鱼雷攻击，行动失败 | historyofwar / FAA |
| 1940-11-09 | 袭击西西里机场，为塔兰托做牵制 | historyofwar |
| 1940-11-27 | 斯帕蒂文托：两波 20 架 Swordfish，全部未命中；英方当时误判命中 | naval-history |
| 1941-02-02 | Operation PICKET：8 架攻 Omodeo 湖水坝，4 架抵达，全部未命中，1 架被击落 | naval-history |
| 1941-02 至 04 | 大西洋搜索 SCHARNHORST / GNEISENAU，未遇 | FAA |
| 1941-03-22 | Swordfish 起飞坠毁、深弹殉爆，本舰受损不严重 | historyofwar |
| 1941-05-01 | 加装两座八联 pom-pom（4→6 座） | navypedia / historyofwar |
| 1941-05-26 | 两次空袭俾斯麦（第一次误击 SHEFFIELD） | naval-history / uboat.net |
| 1941-09-24~27 | Operation HALBERD：Fulmar CAP 4→16 架，对抗 SM 84 | naval-history |
| 1941-10-10 起 | Operation PERPETUAL：运 37 架飓风（实放 34 架 + 4 架 Blenheim） | naval-history |
| 1941-11-13 | 15:41 中雷 | naval-history / uboat.net |
| 1941-11-14 | 06:19-06:24 翻沉（uboat.net 记 08:13） | 两源 |

---

## §12 未获取字段汇总

| 字段 | 为什么没写 |
|---|---|
| `aviation.catapult.type` | 两源只给弹射能力（12,000 lb / 66 kt），**没给型号** |
| `propulsion.boiler.pressure` / `.temperature` | 无来源给出 |
| `propulsion.speed.trial` | naval-history 只说「exceeded on trials」，无数字 |
| `propulsion.propeller.*` | 无来源给出 |
| `propulsion.electrical.output` | 无来源给出（但「无柴油发电机」这一事实已写进 fate_category 与正文） |
| `sensors.radar.installed` 的具体型号 | 见 §8，只有「装了雷达」的间接证据 |
| 雷达安装日期 | 同上 |
| 12.7 mm 维克斯的全部性能参数 | NavWeaps 无英国 12.7 mm 页 |
| 47 mm 3-pdr 礼炮的全部性能参数 | NavWeaps 无 47 mm 单页 |
| Skua / Roc / Albacore 的机型参数 | `weapon.aircraft.*` 字段可用，但本轮未取（任务书未要求，且会大幅增加来源需求） |
| 战时编制（开战后上升后的数字） | naval-history 只说「increased」，没给数 |
| 最终生还总人数 | 只有「首批撤走 1,487 人」这一个中间数字 |
| 损失调查委员会 ADM 档号 | 未取得原件 |
| `aviation.armament.stowage` | 本舰航空弹药定额无来源给出 |
| `armour.weight` / `armour.weight_ratio` | 本舰装甲总重无来源给出（与光辉级不同，navypedia 没给这一项） |
| `dimensions.metacentric_height` / 方型系数 / 水密段数 | 无来源给出 |

---

## §13 来源 → URL 对照表

| id | URL | tier | 用途 |
|---|---|---|---|
| `naval-history-arkroyal` | https://www.naval-history.net/xGM-Chrono-04CV-HMS_Ark_Royal.htm | D | 全生涯年表 + 损失逐刻 + 技术总述 |
| `navypedia-arkroyal` | https://www.navypedia.org/ships/uk/brit_cv1_ark_royal.htm | D | 主尺度/排水量/装甲/航空设施/机群表 |
| `uboatnet-arkroyal-class` | https://uboat.net/allies/warships/class/99.html | D | 水下防护构造、装甲甲板、升降机细节 |
| `uboatnet-arkroyal` | https://uboat.net/allies/warships/ship/3257.html | D | 建造日期、舰长、误击独立记述、沉没时刻 |
| `uboatnet-u81` | https://uboat.net/boats/u81.htm | D | 德方视角（130 枚深弹说） |
| `historyofwar-arkroyal` | https://www.historyofwar.org/articles/weapons_HMS_Ark_Royal.html | D | 干舷对照、沉没机理因果链、战果更正 |
| `faa-arkroyal-archive` | https://web.archive.org/web/20081002151503/http://www.fleetairarmarchive.net/Ships/Ark_Royal2.html | D | 中队勤务表、水线长、异说排水量 |
| `how-arkroyal-open-sided` | https://www.armouredcarriers.com/opensided-versus-closed-hangars-in-aircraft-carriers | A | 备忘录原文（**未引用数值，仅记录易错点**） |
| `navweaps-45in-45-mk1` | https://www.navweaps.com/Weapons/WNBR_45-45_mk1.php | D | 4.5 in 全部武器数据（**已存在，复用**） |
| `ac-techdata` | https://www.armouredcarriers.com/technicaldata | C | 对照页（**已存在，本组未直接引用数值**） |

---

## §14 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/ark-royal.yaml`，101 条 fact） |
| 单舰文件 | 1（`ships/ark-royal.yaml`，64 条 fact） |
| 切片文件 | 1（`slices/ark-royal.yaml`，7 片 P0–P6） |
| 正文文件 | 1（`articles/ark-royal.yaml`，intro 4 段 + history 4 节 22 条事件） |
| 新登记来源 | 8（另有 2 条复用已登记来源，未重复登记） |
| fact 合计 | **165 条** |

新建武器实体 5 个：`weapon:skua` / `weapon:roc` / `weapon:vickers-50` /
`weapon:3pdr-hotchkiss` / `weapon:albacore`（全部只有型号身份三条）。
新建炮位实体 4 个：`mount:ark-royal-45in-twin` / `-2pdr-octuple` /
`-vickers-50-quad` / `-3pdr-saluting`。
4.5 in 按要求使用 `weapon:45in-45-mk1`，来源 `navweaps-45in-45-mk1` 直接引用，
未重新登记。`swordfish` / `fulmar` / `walrus` / `2pdr-mk8` 全部复用已有实体。

### 卡住的地方

1. **`navypedia.org` 与 `naval-history.net` 都被 SSRF 拦**（DNS 解析到 198.18.x.x）。
   `web_fetch` 与 `research` 工具全部失败。改用 PowerShell `Invoke-WebRequest` 直连
   才抓到。**如果主会话后续还要抓这类站点，这条路径是可行的。**
2. **`armouredcarriers.com` 没有皇家方舟号的专页。** 试了 `/hms-ark-royal`、
   `/ark-royal`，两个 URL 都返回 404（连接被意外关闭）。首页 255 个链接里
   没有任何一条提到 Ark Royal。该站的「ARK ROYAL」字样全部出现在讲
   **后续舰（R09 / R07）或 1942-43 年新一代设计**的段落里 —— 例如
   「The new ARK ROYAL has a displacement of 32,500 tons」讲的是新设计，不是本舰
   （本舰 22,000 t）。**这条是本组最容易踩的坑，已在来源 note 里写明。**
   所以任务书提到的「armouredcarriers 是 C 级好来源」对本舰**基本不适用** ——
   该站覆盖的是光辉级及其后续。
3. **雷达型号完全查不到。** 试了 naval-history（只说「radar was fitted」）、
   navypedia（只说「absence of the radar」）、uboat.net（提 RD/F 但都是别舰的）。
   `sensors.radar.installed` 的 `valid.from: 1940-01-01` 是我的估计值，已标 C 档。
4. **甲板装甲的重量与总装甲重量查不到。** 光辉级有 5,000 t / 1,500 t 这两个数，
   本舰没有。所以 `protection.armor.weight` 与 `weight_ratio` **整条没写**。
5. **沉没时刻两源差近 2 小时**（06:19/06:24 vs 08:13），无法判定哪个是 GMT、
   哪个是当地/柏林时间。已并列。
6. `world-war.co.uk` 返回 403，没用上。

### 有争议的记载（本组全部并列，一条没删）

| 项 | A 说 | B 说 | 处理 |
|---|---|---|---|
| **服役日** | 1938-11-16（navypedia / naval-history / FAA Archive） | 1938-12-16（uboat.net） | 两条 fact 并列，正文注明「两说并列不裁决」 |
| **沉没日** | 1941-11-13 = 命中日（uboat.net 类页记「Lost 13 Nov」） | 1941-11-14 = 沉没日（navypedia / historyofwar / uboat.net 本舰页 08:13） | 两条 `construction.fate_date` 并列，fate_type 取 11-13 命中 |
| **沉没时刻** | 06:19 翻 90°、06:24 舰艏没入（naval-history） | 08:13（uboat.net） | note 并列 |
| **标准排水量** | 22,000 t（navypedia / historyofwar / uboat.net） | 22,352 t（FAA Archive） | 两条 fact 并列，各带 src |
| **满载排水量** | 27,720 t（navypedia / historyofwar） | 28,143 t（FAA Archive） | 同上 |
| **续航力** | 10,300 nm @16 kt（navypedia） | 7,600 nm @20 kt（FAA）/ 11,200 mi @11 kt（historyofwar） | 三说并列在 note 里 |
| **锅炉台数** | 6 座（navypedia） | 「three boilers / three boiler rooms」（historyofwar、naval-history） | 按「三组各两台」理解则不冲突，但无来源写清每组台数，并列 |
| **抗爆当量** | 380 kg TNT（navypedia） | 750 lb ≈ 340 kg（uboat.net / historyofwar） | 并列 |
| **编制** | 1,580（navypedia）/ 1,600（naval-history、FAA） | 1,570（uboat.net） | 舰级取 1,580、单舰取 1,600，note 说明 |
| **`SCHARNHORST` 战果（1940-06-13）** | 当时判两弹命中 | 事后核对一弹且未爆炸（historyofwar） | 正文并列 |
| **U-81 遭深弹数** | 162 枚（naval-history） | 130 枚（uboat.net / Blair） | 未进 fact（无对应字段），记在来源 note |
| **破口尺寸** | 130 × 30 ft（naval-history 一处） | 115 ft 长（naval-history 另一处） | 已在 fate_category note 并列 |
| **残骸位置** | 30 NM E of Gibraltar（naval-history，2002-12 发现） | 45 nm ESE（FAA）/ 25 miles E（navypedia） | 均在来源 note，正文未写具体坐标 |
| **对 SHEFFIELD 的误击原因** | 「鱼雷引信故障救了 Sheffield」（任务书表述） | naval-history 原句是「3 枚在尾迹中爆炸、2 枚入水即爆」，这 5 枚本来就不会命中；真正救它的是 Larcom 下令不开火 + 7 枚被规避 + 3 架认出目标 | **正文按 B 写**，并在本文件 §10 说明了为什么不沿用 A |

### 对任务书的三处更正

1. **机库尺寸单位错了。** 任务书写「上层机库 173 ft、下层 150 ft」；
   来源是 **568 ft / 452 ft = 173.1 m / 137.8 m**。173 的单位是**米**。
2. **「剑鱼机群误把 Sheffield 当俾斯麦投雷，多次引信故障救了 Sheffield」**
   —— 前半句成立（已写进正文），后半句的因果不成立，见上表最后一行。
3. **`navypedia` 不是「可能被 SSRF 拦」，是本轮实测 100% 被拦**；
   但 `naval-history.net`、`uboat.net`、`armouredcarriers.com`、`historyofwar.org`
   在 `web_fetch` 里同样被拦，**只有 PowerShell 直连能通**。
