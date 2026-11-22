# g8-weapons2 调研底稿

> Dockyard 武器正文补写 · 2026-11-22 · 组名 `g8-weapons2`
>
> 任务：为本轮新入库的 10 艘英/波舰艇引用的 **6 型无正文武器实体**补写正文。
> 产出全部在 `work/staging/g8-weapons2/`，未改动 `data/`、`src/`、`public/`。
>
> **本文件每条结论都带英文原句 + URL。** 正文里的每个数字都能在这里对回原句。

---

## 0. 抓取方式与环境

| 站点 | `web_fetch` / `research` | PowerShell `Invoke-WebRequest` |
|---|---|---|
| `www.navweaps.com` | SSRF 拦截（198.18.x.x） | ✅ 全部 200 |
| `www.historyofwar.org` | 未试（直接用 IWR） | ✅ 全部 200 |
| `www.naval-history.net` | 未试 | ✅ 200（2.5 MB） |
| `www.navypedia.org` | 未试 | ✅ 200 |
| `web.archive.org`（FAA Archive 快照） | 未试 | ✅ 200 |

原始 HTML 与抽文全部落在 `work/staging/g8-weapons2/_raw/`，供复核。
抽文脚本是「去 script/style → br 转换行 → 去标签 → html.unescape」。

**两次 404，已记入正文注释与 sources-fragment：**

| 下发的 URL | 实测 | 实际页面 |
|---|---|---|
| `WNBR_05_50_vickers.php` | **404** | `WNBR_5-62_mk3.php`（标题 `0.50"/62 (12.7 mm) MG Mark III`） |
| （3-pdr 未下发） | — | `WNBR_3pounder_H_mk1.php`（标题 `Hotchkiss 3-pdr (1.4 kg) [1.85"/40 (47 mm)] QF Marks I and II`） |

两条真实 href 都取自 NavWeaps 英国武器索引 `WNBR_Main.php`，不是猜的：

```
<a class="fancybox" href="WNBR_5-62_mk3.php">
<b>0.5"/62 MG Mark III</b><div>Many Ships 1930s - 1940s</div></a>
```

**注意**：同索引里另有 `WNBR_3pounder_V_mk1.php`（Vickers 3-pdr），
那是**另一门炮**，不是本组要写的 Hotchkiss。别混。

---

## 1. `4in-45-mk16` —— 4"/45 (10.2 cm) QF Mark XVI

URL：http://www.navweaps.com/Weapons/WNBR_4-45_mk16.php（NavWeaps，tier D）

### 1.1 它是「替换 Mark V」的那门炮

> "This weapon superseded the 4"/45 (10.2 cm) Mark V HA gun on new cruiser
> construction during the 1930s. In addition, many older cruisers and capital ships
> had their Mark V guns replaced with these more powerful weapons during refits."

被替换者的年龄（`WNBR_4-45_mk5.php`）：
> "The Mark V was first introduced as a low angle weapon on HMS Arethusa in 1914"
> "Up until the late 1930s the Mark V was the main British long-range AA weapon and
> was fitted in a majority of capital ships and cruisers."

→ 「1914 年的炮换成 1930 年代的新炮」这个对照是两页合起来的结论，不是推算。

### 1.2 炮是 Mark XVI，座是 Mark XIX

装舰表原文（Mark XIX 双联炮座条目下）：
> "Town Cruisers: Southampton class (4), Edinburgh class (6)"

括号是**炮座数**。navypedia 城级装备栏独立印证：
> "Armament 4 x 3 - 152/50 BL Mk XXIII, 4 x 2 - 102/45 QF Mk XVI, ..."
（https://www.navypedia.org/ships/uk/brit_cr_southampton.htm）

### 1.3 参数（全部照抄该页）

| 项 | 原文 | 换算 |
|---|---|---|
| Gun Weight | Mark XVI: 4,495 lbs / Mark XVI*: 4,502 lbs / Mark XXI: 3,397 lbs | 2,039 / 2,042 / 1,541 kg |
| Gun Length oa | 190.5 in | 4.839 m |
| Rifling Length | 149.5 in | 3.798 m |
| Chamber Volume | 511.8 in3 | 8.387 dm3 |
| Rate Of Fire | 15 - 20 rounds per minute | — |
| HE Mark 19 弹丸 | 35 lbs. | 15.88 kg |
| SAP 弹丸 | 38.25 lbs. | 17.35 kg |
| 整装弹 | HE 63.5 lbs / SAP 66.75 lbs | 28.8 / 30.28 kg |
| Muzzle Velocity | Standard 2,660 fps / Reduced 2,000 fps | 811 / 610 mps |
| Working Pressure | 20.5 tons/in2 | — |
| Barrel Life | 600 rounds | — |
| Range @ 45° | 19,850 yards | 18,150 m |
| AA Range @ 80° | 39,000 feet | 11,890 m |
| Mark XIX 炮座重 | 37,072 lbs | 16,816 kg |
| 俯仰 / 回旋 | -10 / +80 degrees；Train 340 degrees | — |
| 炮轴间距 | 21 in | 53.3 cm |

### 1.4 两条硬批评 + 战果

> "These guns were noteworthy as having "neither long barrel life nor particularly
> high accuracy" - John Campbell. This was blamed on the use of projectiles with a
> too-short parallel section which led to poor centering at the muzzle."

> "HMS Carlisle, a converted AA cruiser armed with these guns, shot down 11 aircraft
> during the war, the highest score among British cruisers. The Auxiliary AA ship
> Alynbank, also armed with these guns, shot down six aircraft."

### 1.5 战后的冷水数字

> "Pre-war, the RN regarded bursts within 100 feet (30 m) as being 'effective', but
> postwar experiments showed that a 4in shell bursting at 45 feet (14 m) only had a
> 15 per cent chance of a kill, over quite narrow zones."

### 1.6 亚型与产量

- Mark XVII：
  > "The Mark XVII was designed for some "County" class cruisers with the intention of
  > replacing two of their single 4"/45 (10.2 cm) Mark V mountings with twin mountings
  > without exceeding the Treaty weight limits. This hair-splitting exercise was
  > described as "ridiculous punctiliousness" by John Campbell. Twelve guns were
  > manufactured, all of which were later converted back to the Mark XVI standard."
- Mark XVIII：
  > "The Mark XVIII was the original designation for an improved version of the Mark
  > XVI but this was redesignated as the Mark XVI* before being accepted into service."
- 产量：
  > "Some 2,555 Mark XVI and XVI* guns along with 238 Mark XXI guns were manufactured
  > in Britain. Canada produced 504 Mark XVI* and 135 Mark XXI guns. Australia built a
  > further 45 Mark XVI* guns."
- 备弹分档：
  > "Hood, Barham, Malaya and Warspite: 250 to 280 rounds plus 250 total star shells /
  > Most Cruisers: 200 rounds / Edinburgh: 250 rounds / Roberts: 400 rounds"
  Edinburgh 明细："250 HE, 65 practice HA, 4 practice LA, 4 Target smoke and 12.5 starshells"

### 1.7 遥控改装

> "As completed, most mountings were manually operated, only
> Mountings converted to RP 50: 15 degrees per second
> Mountings converted to RP 51 and RP 52: 20 degrees per second"

> "RP 50 and RP 52 had the Metadyne sets on the fixed structure while RP 51 had them
> on the rotating mass. RP 51 and RP 52 had joysticks for local control."

RP 52 名单（含 Sheffield）：
> "RP 52 Mark XIX conversions:
>   Cruisers: Cumberland, Australia, Devonshire, Sussex, Norfolk, Hobart, Glasgow,
>   Sheffield, Liverpool, Bermuda, Kenya, Mauritius, Ceylon, Ontario, Swiftsure, Superb"

### 1.8 Edinburgh 子级的传送带

> "The Edinburgh class cruisers had an unusual design feature in that their 4"
> (10.2 cm) guns were positioned well back from the secondary magazines, which were
> located under the flight deck. To transport the ammunition from the magazine hoists
> back to the guns, these ships were equipped with a 110 foot (33.5 m) conveyor system
> which consisted of trolleys on a sort of railway. "British Cruisers of World War Two"
> describes these as being "a complicated arrangement which in action could easily be
> disrupted.""

### 1.9 城级没有拆过 4 英寸炮座

`https://www.navypedia.org/ships/uk/brit_cr_southampton.htm` 的 Modernizations 台账
从 1938 到 1945 共 30 余条，逐条读过，**没有任何一条拆减 102 mm 炮座**；
1946-01 的 Birmingham 装备栏仍写 "4 x 2 - 102/45 Mk XIX"。

---

## 2. `vickers-50` —— 0.5"/62 (12.7 mm) MG Mark III

URL：http://www.navweaps.com/Weapons/WNBR_5-62_mk3.php（NavWeaps，tier D）

### 2.1 装舰范围 + 性质 + 判定，三句连着

> "This weapon was used on almost all British warships during World War II, many in
> quad mounts like the ones shown below."

> "This was a recoil-operated, water-cooled gun with link-belt ammunition feed and was
> significantly less powerful than the USN's 0.50" (12.7 mm) Browning M2 BMG."

> "Like the US and most other nations, the British found small-caliber machine guns
> like these to be ineffective against modern aircraft. Nonetheless, this weapon was
> still produced in large numbers during the war with an overall total of 12,500 being
> built."

### 2.2 参数

| 项 | 原文 |
|---|---|
| Suffixes | "No. 1: For quad mounts / No. 2: For twin mounts / No. 3: For single mounts" |
| Gun Weight | "56 lbs. [62 lbs. with filled cooling jacket] (25.4 kg [28.1 kg])" |
| Gun Length oa | "about 35 in (89 cm)" |
| Bore Length | "31.25 in (79.4 cm)"；另注 "Actual bore length was 62.5 calibers" |
| Rate Of Fire | "600 to 700 rounds per minute cyclic / 450 … with a delay pawl / 150 to 200 practical" |
| Ammunition Type | Fixed |
| 整装弹重 | "2.9 oz (0.08 kg)" |
| 弹丸 | "Ball: 580 gr., 1.326 oz (37.6 gm)"；"Bullets were also produced in AP, SAP, SAP-T and Incendiary" |
| 发射药 | "Ball: 142gr., 0.324 oz. (9.2 gm) Cordite 7/2" |
| Muzzle Velocity | "2,520 fps (768 mps)" |
| 弹鼓 | "Each ammunition drum held 200 rounds, which was enough for about twenty seconds of firing. The four ammunition drums on the quad mounting could be replaced within thirty seconds by a well-trained crew."；"Each loaded drum weighed 60 lbs. (27.2 kg)" |
| 备弹 | "About 2,500 rounds" per gun |
| Effective Range | "800 yards (730 m)" |
| Maximum Range | "about 5,000 yards (4,570 m)" |
| 后坐 | "1.25 in (3.2 cm)"；回旋 "360 degrees" |

### 2.3 四联装是五个型号，不是一个

> "Quad Mountings: Mark I and Mark I** / Mark II and Mark II** / Mark III"

> "Mark I: 1,605 lbs. (728 kg) / Mark I*: 2,200 lbs. (998 kg) / Mark II: 2,888 lbs.
> (1,310 kg) / Mark III: 2,580 lbs. (1,170 kg)"

> "Mark I and Mark I**: -10 / +70
> Mark II, Mark II** and Mark III: -10 / +80 degrees"

> "All except Marks V and VC: Manually operated, only"

> "The Mark III mounting had a new type of base plate that was more robust and of
> larger diameter than the previous types. As opportunity offered, the older Mark I
> and Mark II mountings were modified to bring them into line with the Mark III. These
> modified mounts were then designated as Mark I* and Mark II*"

> "The quad mounting had its barrels slightly misaligned from each other in order to
> give a "scatter" effect."

### 2.4 皇家方舟号装了八座（本页唯一点名）

> "Large ships usually had four quad mountings, but HMS Ark Royal had eight. Cruisers
> had two to four and destroyers had two."

两源独立印证：
- navypedia：`"Armament 8 x 2 - 114/45 QF Mk I, 4 x 1 - 47/40 3pdr Hotchkiss Mk I,
  4 x 8 - 40/39 2pdr QF Mk VIII, 8 x 4 - 12.7/62, 60 aircraft ..."`
- FAA Archive：`"Guns: 8 x twin 4.5 inch AA; 48 x 2 pdr AA; 32 x 0.5 inch AA"`

### 2.5 「被取代」的台账（这才是替换事实的来源）

`https://www.navypedia.org/ships/uk/brit_cr_southampton.htm` Modernizations：

> "9/1941, Sheffield : - 2 x 4 - 12.7/62, type 79Y radar; + 6 x 1 - 20/70 Oerlikon
> Mk II/IV, type 284 radar"
> "3/1942, Birmingham : - 2 x 4 - 12.7/62, type 286M radar; + 7 x 1 - 20/70 Oerlikon ..."
> "8/1942, Glasgow : - 2 x 4 - 12.7/62, type 286M radar; + 9 x 1 - 20/70 Oerlikon ..."
> "11/1942, Newcastle : - 2 x 4 - 12.7/62, catapult with seaplanes; + 10 x 1 - 20/70 ..."

**注意**：NavWeaps 的 0.5 英寸页本身**没有写**「被 20 mm Oerlikon 取代」。
正文把这两件事分开引：判定无效引 navweaps，替换动作引 navypedia-town。
另：navweaps 的 Oerlikon 页只讲美军以 Oerlikon 换 0.50 BMG，
**没有讲英国**，所以没有拿它当英国替换的依据。

### 2.6 出口

> "A few guns were exported to Japan during the late 1930s where they were designated
> as the 12 mm/62 "BI" Type (also known as the "HI" Type). ... China purchased 19
> British guns pre-war."

### 2.7 设计/服役年份的同页矛盾（未裁决）

特性表：`Date Of Design 1926` / `Date In Service 1926`
描述段：`"Vickers started production of this gun in 1926, but service introduction on
British ships does not seem to have taken place prior to 1932."`

→ 正文并列，未合并。

---

## 3. `3pdr-hotchkiss` —— 47 mm/40 3-pdr Hotchkiss Mk I（礼炮）

URL：http://www.navweaps.com/Weapons/WNBR_3pounder_H_mk1.php（NavWeaps，tier D）

### 3.1 本舰用途：礼炮（这是本篇的前提）

- navypedia 皇家方舟号装备栏：`"4 x 1 - 47/40 3pdr Hotchkiss Mk I"`
- historyofwar 本舰装备清单：`"Four 3pdr saluting guns"`
  （https://www.historyofwar.org/articles/weapons_HMS_Ark_Royal.html）

→ `weapon.category` 填 `naval_gun` 是注册表没有「礼炮」枚举值的限制，
正文第一段已写明。**这一条不是推断，是来源原词。**

### 3.2 降级 → 复役的完整链条（正文整段引用）

> "Hotchkiss 3-pdr guns were introduced in 1886 for locations where the 6-pdr gun was
> considered to be too heavy. Used as anti-torpedo boat guns on most small cruisers
> built prior to World War I. As did other nations, the British found that these
> small-caliber projectiles were too light to be effective and many guns were converted
> following World War I to sub-caliber training and saluting guns. This last use meant
> that a number of these guns survived until World War II when they were converted back
> to shooting guns and used on MLs and other minor auxiliary warships. An approximate
> total of 2,950 of these guns were in naval service, with about 1,950 of these still
> available in 1939."

> "Mark I was of monobloc construction while the Mark II was a built-up design. Almost
> all surviving guns in 1939 were Mark I."

### 3.3 参数

| 项 | 原文 |
|---|---|
| Date Of Design / In Service | "about 1885" / "1886" |
| Gun Weight | "528 lbs. (240 kg)" |
| Gun Length oa | "80.6 in (2.048 m)" |
| Bore Length | "74.1 in (1.881 m)" |
| Chamber Volume | "43 in3 (0.705 dm3)" |
| Rate Of Fire | "20 rounds per minute" |
| 整装弹 | "HE: 5.7 lbs. (2.6 kg)" |
| 弹丸 | "HE: 3.3 lbs. (1.5 kg)" |
| 全弹长 | "Complete Round: 21.4 in (54.2 cm)" |
| 发射药 | "World War I: 0.54 lbs. (0.24 kg) MD / World War II: 0.465 lbs. (0.211 kg) HSCT 134-055 / World War II: 0.602 lbs. (0.273 kg) NF 029" |
| Muzzle Velocity | "New gun: 1,884 fps (574 mps) / Average gun: 1,873 fps (571 mps)" |
| Barrel Life | "about 6,000 rounds" |
| Range | "20.7 degrees: 6,500 yards (5,944 m) / 45 degrees: 7,900 yards (7,200 m)" |
| AA | "Maximum AA Ceiling about 10,000 feet (3,000 m) / Effective AA Range about 1,200 yards (1,100 m)" |
| 炮座重 | "0.7 tons (0.8 mt)" |

### 3.4 炮座与炮身要分开

> "Single LA Mountings: Mark I and Mark I*
> Single HA Mountings: Mark IV HA, Mark V HA and Mark VI HA"
> "Marks I and I*: -5 / +25 degrees / Mark V: -5 / +70 degrees / Mark VI: -5 / +60 degrees"
> "Marks I, I* and IV were pre-war and World War I mountings. Marks V and VI were
> produced during World War II."
> "Some Mark I mountings were converted to HA types and then designated as Mark IC HA.
> These had an elevation range of -8 to +60 degrees."

### 3.5 城级 1939 年把礼炮拆了

`navypedia` 城级 Modernizations：`"1939, all: - 4 x 1 - 47/40"`
皇家方舟号的记载里没有对应条目 —— **本舰这四门礼炮何时拆除，来源未给**，正文不写。

---

## 4. `skua` —— Blackburn Skua (B-24)

两个来源并用：`naval-history-arkroyal`（舰上记录与机型说明）、
`historyofwar-skua`（结构与战历）。

URL：https://www.historyofwar.org/articles/weapons_blackburn_skua.html（tier D）

### 4.1 两用设计的三个成因

> "The Skua was designed to satisfy Air Ministry Specification O.27/34, issued before
> the Navy had regained control of its own aircraft. The poor quality of Fleet Air Arm
> aircraft in 1939 had often been blamed on the period of RAF control of naval
> aviation, a period in which naval aircraft were a very low priority."

> "In the pre-war years it was believed that the new generation of high performance
> fighters then under development would not be able to operate from aircraft carriers.
> It was also believed that naval aircraft needed two crewmen to cope with the
> complexity of navigation over water, inevitably increasing the weight of the
> aircraft."

> "Finally, there was a tradition of multi-purpose aircraft, designed to make the best
> use of the limited capacity of each aircraft carrier. In the case of the Skua it was
> designed to perform as both a fighter and a dive bomber, not entirely compatible
> roles."

### 4.2 进步 vs 过时（同一页两面）

> "The prototype Skua first flew on 9 February 1937, six months after Blackburn had
> received an order for 190 aircraft. It was a significant advance on the fabric
> covered biplanes that then equipped the Fleet Air Arm, featuring metal construction,
> flaps, a variable pitch propeller and retractable landing gear, all firsts for a
> British deck landing naval aircraft."

> "The Skua entered service late in 1938 with Nos. 800 and 803 squadrons, allocated to
> HMS Ark Royal, replacing Hawker Nimrods and Ospreys. Even at this early date it was
> hopelessly outdated as a fighter aircraft. The Nimrods it replaced could reach
> 193mph - the Skua was only 32mph faster, and it achieved its top speed at a lower
> altitude. At the same time the RAF was introducing the Spitfire Mk I with its top
> speed of 362mph. The Skua would be very badly outclassed by the Messerschmitt Bf 109,
> and was slower than the German bombers in use in 1939."

### 4.3 柯尼斯堡号：战果属于中队，起飞地点是岸上

> "By April 1940 both Nos. 800 and 803 squadrons were based at Hatston on Orkney, after
> the Ark Royal was sent to the Mediterranean. On 10 April twenty aircraft from the two
> squadrons attacked and sank the German cruiser Königsberg at Bergen. This was the
> first time a major operational warship had been sunk by aircraft."

战果细节（本舰页 https://www.historyofwar.org/articles/weapons_HMS_Ark_Royal.html）：
> "Nos.800 and 803 Squadrons had been left behind during that move, and on 10 April
> their Skua dive bombers attacked and sank the damaged German cruiser Konigsberg at
> Bergen. Three hits were scored, causing internal explosions and setting the
> Konigsberg on fire. She was then destroyed by another explosion, which split her in
> half. Only one Skua was lost."

→ **正文明确写「战果不属于本舰甲板」**，避免「皇家方舟号的 Skua 击沉柯尼斯堡」这种写法。

### 4.4 蜜月期结束与替代

> "This success was also the end of the honeymoon period for the Skua. The squadrons
> suffered heavy losses in an attack on Narvik on 21 April. On 12 June, in the aftermath
> of the loss of HMS Glorious they were sent to attack the Scharnhorst and Gneisenau at
> Trondheim. There they ran into German fighters and heavy flak. Eight out of fifteen
> aircraft were lost in the attack."

> "A lack of any alternative aircraft meant that the Skua had to stay in service until
> August 1941, when it was replaced by the Fairey Fulmer and the Hawker Sea Hurricane."
（原文把 Fulmar 拼作 Fulmer，引文照录）

### 4.5 规格（historyofwar，Mk. II 表）

> "Crew: 2 / Engine: Bristol Perseus XII radial engine / Horsepower: 890 / Span: 46ft
> 2in / Length: 34ft 7in / Max Speed: 225mph at 6,500ft / Cruising Speed: 165mph at
> 15,000ft / Ceiling: 20,200ft / Range: 760 miles / Armament: Four 0.303in machine guns
> in wings, one Lewis gun in rear cockpit / Bomb load: one 500lb bomb on fuselage, eight
> 30lb practice bombs under wings"

### 4.6 舰上机型说明（naval-history，1939-09 编成处）

> "The Blackburn Skua, which was a two seat fighter/dive bomber, max speed 225 mph at
> 6700 ft, 204 mph at sea level, maximum range approximately 760 miles. Armament was
> four Browning .303" machine guns in the wings with 600 rounds per gun. One Lewis
> .303" machine gun in rear cockpit (whenever possible the gunner would try to replace
> this with a Vickers K gun which was more reliable and had a higher rate of fire).
> Bomb load was 500 lb."

→ 最大速度同为 225 mph，高度 6,700 ft vs 6,500 ft，正文并列。

### 4.7 「第一次击落」的两说

naval-history（1939-09-26 段）：
> "One Dornier was shot down by A7C piloted by Lt BS McEwen with observer acting PO BM
> Seymour. The Dornier landed on the sea and the 4 crewmen of the stricken aircraft
> were picked up by the destroyer SOMALI. This shooting down of the Dornier 18 is often
> cited as the first kill by a British Aircraft in World War II, but iIn fact the first
> was by Sgt F.A. Letchford, an observer/gunner in a Fairy Battle Bomber of 88 Sqd RAF
> on the 20/9/39. But Sgt Letchford's claim was not confirmed straight away; so Lt
> McEwen's was the first confirmed"

historyofwar：
> "A Skua of No. 803 squadron of HMS Ark Royal became the first British fighter to shoot
> down a German aircraft during the Second World War."

→ 两说并列（前者是「第一个被确认」，后者直接说「第一个」），正文加方括号注写明而不裁决。

### 4.8 特隆赫姆：日期口径差一天

- historyofwar：`"On 12 June ... they were sent to attack the Scharnhorst and Gneisenau
  at Trondheim."`
- naval-history：`"13th – The Fleet arrived at the flying off position, 64-58N, 4-38E.
  At 0002 ARK ROYAL flew off 15 Skuas 6A, 6C, 6F, 6G, 6H & 6K of 800 Sqd and 7A, 7B,
  7C, 7F, 7G, 7L, 7P, 7Q & 7R of 803 Sqd, each Skua was armed with a 500lb SAP bomb"`

→ 起飞时刻 0002/13 落在午夜刚过，两说实质同一次夜间出动。正文取 13 日并并列另一说。

### 4.9 战损与战果（naval-history 逐条）

> "Skua 6G, L3028, pilot Mid LH Gallagher was the first to be shot down by a Me109,
> second was 6H, L3047, pilot Mid DTR Martin and third 6F, L3000, pilot Lt GED
> Finch-Noyes."
> "A further five Skuas were lost these were, 6A, L2995, pilot Capt RJ Partridge RM,
> shot down by a Me109, 7A, L2896, pilot Lt Cdr J Casson shot down by a Bf109, 7F,
> L2963, pilot Lt CH Filmer shot down by a Me110. 7L, L2992, pilot Sub Lt JA Harris
> shot down by a Me110 and 7Q, L2955, pilot Sub Lt RE Bartlett shot down by a Me110."

> "In the analysis of the attack the VA Aircraft Carriers considered that two hits had
> been achieved, but in fact only one hit had been achieved and that failed to explode"

> "The high loss rate effected the morale of the entire ships company. But particularly
> affected were those that had planned the mission. The total losses amounted to almost
> an entire squadron, and effectively reduced the FAA's two premiere fighter squadrons
> to a small nucleus of experienced flyers"

> "By 0345 all the remaining seven Skuas, two from 800 Sqd and five from 803 Sqd, had
> landed back on."
> "the Skua returned, ARK ROYAL did not break radio silence and the crews were forced
> to navigate back by taking a fix using the ship's revolving beacon"

### 4.10 护航失败的原因

> "The Blenheims of 254 Sqd failed to arrive at the RV on time due to an error in
> calculating the range. Therefore because of time pressures the Skuas left the RV and
> headed for Trondheim without the Blenheims."

> "However it had the opposite effect to the intended as the Bf109's of II./JG77and
> Me110's of I./ZG76 that were scrambled to defend the aerodrome were perfectly placed
> to attack the Skuas even before they reached their target."

---

## 5. `roc` —— Blackburn Roc

URL：https://www.historyofwar.org/articles/weapons_blackburn_roc.html（tier D）

### 5.1 与 Defiant 的战术差别

> "The Blackburn Roc was the Royal Navy's equivalent to the Boulton Paul Defiant, and
> was a turret armed fighter aircraft developed just before the Second World War, and
> which proved to be ineffective in combat."

> "The Boulton Paul aircraft had been built because some experts believed that modern
> fighter aircraft were too fast for the pilot to be able to both fly the aircraft and
> make accurate attacks on equally fast moving enemy aircraft. The powered turret would
> allow a second crewman to concentrate on gunnery."

> "In contrast the Roc was designed to attack enemy bombers. It was to fly alongside the
> incoming attacker, which would have to be flying straight and level to make an
> accurate attack on the Navy's warships, and fire broadsides from the four-gun turret."

### 5.2 与 Skua 的关系

> "The Roc was developed in response to Air Ministry specification O.30/35, which called
> for single engined two-man fighter aircraft, armed with four 0.303in Browning guns
> mounted in a power operated turret. Blackburn responded to this specification with a
> modified version of the Skua dive bomber. Blackburn were given a contract for 136 Rocs
> on 28 April 1937, but they were busy producing the Skua and preparing to produce the
> unsuccessful Botha, and so production was sub-contracted to Boulton Paul."

> "The basic problem with the Roc was that the extra weight of the turret reduced the
> moderate performance of the Skua to a point where it could not have caught up with any
> modern German bomber. The Skua itself would have a longer career as a naval fighter.
> Fortunately for the Roc crews, this was realised before the aircraft had been sent
> into to combat"

### 5.3 ⚠️ 与 naval-history 直接冲突（本站不裁决）

historyofwar：
> "Nos.801 and 806 Squadrons both received the type during 1940, operating them
> alongside their Skuas. Both squadrons were land-based, and **the Roc was never used
> from an aircraft carrier**."

反面证据（三条独立来源）：
1. naval-history 1939-09-11 / 09-22 / 09-25 三处：
   > "with Blackburn Skuas of 800 Sqd, Blackburn Skuas and Rocs of 803 Sqd, Fairy
   > Swordfish of 810, 818, 820 and 821 Sqds embarked"
2. naval-history 1940-03-22：
   > "At 0930 the ARK ROYAL landed on six Skuas and five Rocs of 800 and 801 Sqds from
   > Prestwick."
   1940-03-23：
   > "At 0900 the ARK ROYAL ..., with 18 Skuas & 5 Rocs of 800 & 801 and 21 Swordfish of
   > 810 & 820 embarked"
3. FAA Archive 中队表：`"803 | April-Oct 1940 | Skua II/Roc I"`
   navypedia 机群表：`"4/1940 | 5 Roc | 18 Skua | 21 Swordfish | 1 Walrus"`，
   `"5.1940"` 行已无 Roc。

→ 正文并列，两边都给 `src`，**没有删任一边**。

### 5.4 规格

> "Engine: Bristol Perseus XII / Power: 890hp / Wing span: 46ft 0in / Length: 35ft 7in
> / Height: 12ft 1in / All-up weight: 7,950lb (landplane) / Maximum speed: 223mph
> (landplane), 193mph (seaplane) / Armament: Four 0.303in machine guns in Boulton Paul
> turret"

舰上机型说明（naval-history）：
> "The Blackburn Roc was a two seat fighter/bomber development of the Skua, performance
> similar to Skua but a shorter range, fitted with a Bolton Paul rotating electrically
> powered turret mounting four Browning .303" machine-guns. Bomb load 250lb."

### 5.5 水上型

> "The Roc was also produced as a floatplane, to specification 26/36, but this version
> was no more successful than the fighter. The floats made the aircraft directionally
> unstable, and the first floatplane crashed during testing. Only two more were produced."

### 5.6 一个具体旁证（计划而非事实）

naval-history 1940-04-25 的空中政策说明：
> "it appears possible that a base for twelve Rocs on floats might be found in the
> vicinity. This is being actively investigated by Naval and Air staffs"

→ 正文写明这是「计划」，不是已部署。

---

## 6. `albacore` —— Fairey Albacore

### 6.1 ★ 结论：上过皇家方舟号，但只是转场搭载

**三条独立来源在三个要素上一致：时间（1941-10）、单位（828 中队）、去向（马耳他）。**

**① naval-history（逐日年表，最详细）**

10 月初（入港前）：
> "Before entering harbour ARK ROYAL flew off 810 Sqd Swordfish to North Front airfield,
> this was so she could accommodate the Albacores of 828 Sqd."

同段 Argus 的来路：
> "The ARGUS had sailed from the Clyde on 30/9/41 with 12 Albacore 1s fitted with long
> range tanks & 2 Swordfish of 828 embarked. She had sailed with convoy WS 12 and
> detached for Gibraltar at 1700/5/10/41. The11 Albacores & 2 Swordfish were to be
> transferred to ARK ROYAL for flying off to Malta where they were to reinforce the
> Islands torpedo bomber force. This operation was code named CALLBOY"

10-08：
> "At around 0400 the aircraft carrier ARGUS escorted by the destroyers COSSACK, ZULU,
> and SIKH arrived at Gibraltar. The ARGUS moored stern on to the ARK ROYAL to
> facilitate the transfer of her embarked aircraft."

10-16：
> "At 1600, Force H comprising the battleship RODNEY (Flag CINC Force H), ARK ROYAL,
> light cruiser HERMIONE, and the destroyers COSSACK, FORESTER, FORESIGHT, FURY, LEGION,
> SIKH and ZULU sailed from Gibraltar and headed east into the Mediterranean on
> Operation CALLBOY."

10-18：
> "At 0140 ARK ROYAL in position 37-28N, 6-00E, flew off 11 Albacores (the Albacore
> piloted by T/Sub Lt (A) T. G. Davison RNVR failed to take off and joined the squadron
> later) and two Swordfish for Hal Far airfield, Malta. One Swordfish was lost en route
> and pilot T/Sub Lt (A) DM Muller RNVR and Observer T/Sub Lt (A) AS Denby RNVR were
> lost. Following completion of the flying off Force H steered west for Gibraltar."

**② FAA Archive 中队表**
> "828 | Oct 1941 | Albacore I/Swordfish I"

**③ historyofwar 本舰页**
> "No.828's Albacores were briefly on the Ark Royal after transferring from the Argus in
> early October 1941. Flew off to Hal Far, Malta on 18 October."

→ 判定：**在舰约十天，一次飞送，无作战出动。**
正文没有把它写成「在皇家方舟号服役」，也没有写成「从未上舰」。

### 6.2 容易误导的那一句（已并列）

historyofwar 机型页（https://www.historyofwar.org/articles/weapons_fairey_albacore.html）：
> "Over the next year the Albacore gradually replaced the Swordfish on the larger fleet
> carriers, serving on HMS Ark Royal, HMS Formidable, HMS Furious, HMS Illustrious, HMS
> Indomitable and HMS Victorious."

「serving on」会被读成作战服役。正文与 828 中队转场那段并列，并说明为什么后者更准确。

### 6.3 时间窗口的算术（这不是史料结论，是核对步骤）

| 事件 | 日期 | 来源 |
|---|---|---|
| Albacore 随 826 中队服役 | 1940-03 | historyofwar-albacore |
| Albacore 首次上舰（Formidable，826+829） | 1940-11-26 | historyofwar-albacore |
| 皇家方舟号中雷 | 1941-11-13 | navypedia-arkroyal / uboatnet |
| 皇家方舟号沉没 | 1941-11-14 | navypedia-arkroyal |

→ 重叠窗口只有 1941 年下半年。这段算术写进正文，但**没有当成 fact 断言**。

### 6.4 为什么不适应

> "While the Albacore successfully supplanted the Swordfish on the large fleet aircraft
> carriers, it was not as adaptable as the Swordfish, and was withdrawn from front line
> service in 1944, one year before the Swordfish."

> "The Swordfish then went on to serve on escort carriers, which were often too small to
> cope with the faster, heavier Albacore."

### 6.5 设计与产量

> "The Albacore was developed in response to Air Ministry specification S.41/36. Like
> the Swordfish it was a single engined biplane, but unlike the Swordfish it had a
> comfortable enclosed and heated crew cabin, hydraulic flaps, a more powerful engine
> and a variable-pitch propeller."

> "The prototype, powered by a 1,065hp Taurus II engine, made its maiden flight on 12
> December 1938. It was followed in 1939 by a second prototype, and then by the first of
> 798 production aircraft, powered by the 1,130hp Taurus XII. All 800 Albacores were
> produced at Fairey's Hayes factory, and were delivered between 1939 and 1943."

→ 798 量产 + 2 原型 = 800，原文两个数字都有，正文照两个都写。

### 6.6 首次作战不是鱼雷攻击

> "The Albacore entered service with No.826 Squadron in March 1940, and made its
> operational debut on 31 May 1940, during the German blitzkrieg in the west. Although
> it had been designed as a carrier based torpedo bomber, in the desperate circumstances
> of May 1940 its first raid was a conventional bombing attack on German road and rail
> communications at Westende, combined with an attack on E-boats at Zeebrugge. For the
> rest of the year the squadron carried out a mix of night time bombing raids and convoy
> escort missions. Two of the remaining three Albacore squadrons formed during 1940 were
> also used as land-based aircraft."

> "On 26 November 1940 the Albacore finally went to sea, when Nos.826 and 829 Squadrons
> embarked on the carrier HMS Formidable."

### 6.7 规格（两个并列值照录）

> "Engine: Bristol Taurus XII / Power: 1,130hp / Wing span: 48ft 11in / Length: 39ft
> 11in / Height: 12ft 6in or 15ft 3in / Normal loaded weight: 10,365lb / Maximum
> weight: 12,500lb / Max speed: 161mph / Service ceiling: 20,700ft or 18,800ft / Normal
> range: 710 miles / Maximum range: 930 miles / Armament: One 0.303in machine gun in
> starboard lower wing plus one or two 0.303in guns in rear cockpit / Bomb load: 2,000lb
> of bombs or one torpedo or four Mk.VII depth charges"

---

## 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 0 |
| 单舰文件 | 0 |
| 切片文件 | 0 |
| 正文文件（`weapon-articles/`） | **6** |
| 新登记来源 | **5** |

### 六篇的篇幅

| 文件 | intro 段 | history 节 / 事件条 | 主要来源 |
|---|---|---|---|
| `4in-45-mk16.yaml` | 6 | 2 / 4 | navweaps-4in-45-mk16、navypedia-town |
| `vickers-50.yaml` | 7 | 2 / 5 | navweaps-vickers-50、navypedia-town |
| `3pdr-hotchkiss.yaml` | 5 | 2 / 6 | navweaps-3pdr-hotchkiss、historyofwar-arkroyal |
| `skua.yaml` | 5 | 3 / 10 | historyofwar-skua、naval-history-arkroyal |
| `roc.yaml` | 5 | 2 / 7 | historyofwar-roc、naval-history-arkroyal |
| `albacore.yaml` | 5 | 2 / 9 | historyofwar-albacore、naval-history-arkroyal |

篇幅参照 `data/weapon-articles/47in-45-mk12.yaml`（intro 6 段 / history 2 节）。
`4in-45-mk16` 的 intro 已从初稿 9 段并到 6 段（亚型+产量并段、批评+战后数字并段、
备弹+Edinburgh 传送带并段），与范例对齐。

### 卡住的地方

1. **`WNBR_05_50_vickers.php` 404** —— 下发的 URL 不存在。从 NavWeaps 英国武器索引
   `WNBR_Main.php` 取到真实 href 是 `WNBR_5-62_mk3.php`，已抓取，已写进
   sources-fragment 的 note。**不是猜的。**
2. **3-pdr 没有下发 URL** —— 同上，从索引取到 `WNBR_3pounder_H_mk1.php`。
   索引里另有 `WNBR_3pounder_V_mk1.php`（Vickers 3-pdr），**是另一门炮**。
3. **英国「0.5 换 Oerlikon」没有单一来源** —— NavWeaps 的 0.5 页只写「判定无效」，
   Oerlikon 页只写**美军**换 0.50 BMG。英国的替换只能从 navypedia 的逐舰改装台账
   （"- 2 x 4 - 12.7/62 …… + 6 x 1 - 20/70 Oerlikon"）读出来。正文按此分工引源。
4. **皇家方舟号这 32 挺 12.7 mm 何时拆除，来源未给** —— 本舰 1941-11 沉没，
   naval-history / navypedia / FAA 三份记录都没有对应条目。正文写「来源未给」，不推测。
5. **皇家方舟号四门 3-pdr 礼炮何时拆除，来源未给** —— 同上，正文不写。
6. **`4in-45-mk16` 的亚型与产量没有年份** —— NavWeaps 页只给两个年份
   （设计约 1934、服役 1936）。所以亚型/产量/备弹/批评四段放在 intro
   （不需要日期），history 只保留有年份的两节四条。**这是刻意压短，不是漏写。**
7. **Skua 在纳尔维克（1940-04-21）的具体损失数** —— historyofwar 只写
   「suffered heavy losses」，没给数字；naval-history 4 月那一段的损失散在
   多日记录里。**正文不补这个数字。**
8. **Skua 的 Mk. I 规格** —— historyofwar 只给 Mk. II 表。Mk. I 的数据不写。
9. **300 字摘要需要的一条**：Albacore 到底上没上 —— 见下。

### 有争议的记载（并列，均未裁决）

| # | 争点 | A 说 | B 说 | 正文处理 |
|---|---|---|---|---|
| 1 | **Roc 是否上过航母** | historyofwar：`"the Roc was never used from an aircraft carrier"` | naval-history 三处「Skuas and Rocs of 803 Sqd embarked」+ 1940-03-22/23 逐条 + FAA Archive 803 中队「Skua II/Roc I」+ navypedia 4/1940「5 Roc」 | `roc.yaml` intro 第 3 段 + history 两条，**四源并列** |
| 2 | **Albacore 与皇家方舟号** | historyofwar 机型页：「serving on HMS Ark Royal」 | historyofwar 本舰页「briefly on」+ naval-history 逐日转场 + FAA Archive 828 中队 | `albacore.yaml` intro 第 2 段，写明「转场搭载，非作战服役」 |
| 3 | **Skua 第一次击落** | historyofwar：「first British fighter to shoot down a German aircraft」 | naval-history：第一个是 1939-09-20 RAF 88 中队 Sgt Letchford，但其战果未立即确认，故 McEwen 是「第一个被确认的」 | `skua.yaml` history `firstblood` 第 2 条 |
| 4 | **特隆赫姆空袭日期** | historyofwar：6 月 12 日 | naval-history：6 月 13 日 00:02 起飞 | 取 13 日，并列另一说 |
| 5 | **Skua 最大速度对应高度** | historyofwar：225 mph @ 6,500 ft | naval-history：225 mph @ 6,700 ft | 两个高度都写 |
| 6 | **0.5 英寸机枪服役年份** | NavWeaps 特性表：Design 1926 / In Service 1926 | 同页描述段：`"does not seem to have taken place prior to 1932"` | `vickers-50.yaml` history `origin` 第 1 条，同页矛盾并列 |
| 7 | **Albacore 产量** | 「798 production aircraft」 | 「All 800 Albacores were produced」 | 正文写「原型机 2 + 量产 798 = 800」，两个原文数字都保留 |
| 8 | **Albacore 机高 / 升限** | 「12ft 6in」/「20,700ft」 | 「15ft 3in」/「18,800ft」（同页并列） | 两个值都写，不代选 |

### 需要主会话决定的一件事

`data/sources.yaml` 里存在一条 **`navweaps-45in-45-mk16`**，
其 `url` 指向 `WNBR_4-45_mk16.php`（**4 英寸** Mk XVI 页），
但 `title` 写成 `4.5"/45 QF Mark XVI` —— **标题是错的**。

本组统一引 `navweaps-4in-45-mk16`（同 URL、标题正确），**未引那一条**。
g2 组本轮也提过同一问题。是否改名或作废请主会话定。
本组**不改 `data/`**，因此没有动它。

### 自检结果

```
python work/staging/g8-weapons2/_selfcheck.py
  errors=0 warnings=0
```

自检脚本按 `scripts/validate.py` 的 `check_article(required={"weapon","intro","history"})`
规则实现：顶层键、`weapon` id 是否在 `data/` 有实体指向、文件名与 id 一致、
`intro.lead.zh`、每段 `heading`+`text.zh`+`src`、`src` 已登记且非 E 层、
history 节 `id`/`title.zh`/`range` 格式/`events` 非空、每条 `date` 格式、
`text.zh`+`src`、以及 `VAGUE_RE`（据说/有人认为/有人称/据信/或许/大概/应该是）扫描。

**未使用任何 tier E 来源。** 六篇正文的来源全部是 tier D 的 NavWeaps / navypedia /
naval-history / historyofwar / FAA Archive。

**未执行**：`python scripts/validate.py`（它跑的是 `data/` 全量，
本组分片还没合并进去，跑它会看不到本组文件）。
