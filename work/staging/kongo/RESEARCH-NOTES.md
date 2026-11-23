# 金刚型（榛名・雾岛）调研底稿

> Dockyard 二战战舰资料站 · 分片组 `kongo` · 2026-11-23
> 交付目录：`work/staging/kongo/`
> 依据：`work/staging/SCHEMA.md`、`data/fields.yaml`

---

## 0. 抓取方式与可用性

按 SCHEMA §9.1，**全程未使用 `web_fetch` / `research`**，一律 Python `urllib.request`
带 `User-Agent` 直连，原页存 `_raw/`。

| 站点 | 结果 | 备注 |
|---|---|---|
| navypedia.org（Kongo 级页） | ✅ 200 / 56,591 B | 一次成功 |
| combinedfleet.com `haruna.htm` | ✅ 200 / 78,280 B | |
| combinedfleet.com `Kirishima.htm` | ✅ 200 / 67,304 B | **小写 404**，必须 `Kirishima` |
| combinedfleet.com `kongo.htm` | ✅ 200 / 84,006 B | 仅作旁证 |
| combinedfleet.com `hiei.htm` | ✅ 200 / 25,982 B | 备用，本轮未引数据 |
| japanese-warship.com 榛名 / 雾岛 / 金刚 | ✅ 各 200 / 约 47–50 KB | 日文，本轮关键来源 |
| navweaps.com `WNJAP_14-45_t41.php` | ✅ 200 / 41,436 B | |
| navweaps.com `WNJAP_6-50_t41.php` | ✅ 200 / 28,349 B | |
| navweaps.com `WNJAP_5-40_t89.php` | ✅ 200 / 44,668 B | **既有来源已登记，直接复用** |
| navweaps.com `WNJAP_25mm-60_mg.php` | ✅ 200 / 32,042 B | **既有来源已登记，直接复用** |
| navweaps.com `WNJAP_13mm-76_mg.php` | ✅ 200 / 18,795 B | 抓到，本轮未用（金刚型无 13 mm 增装记录） |
| ibiblio.org/hyperwar `Japan/IJN/` | ⚠️ 200 但只有 3 条外链 | 目录页，无舰级参数，放弃 |

**URL 陷阱（留给后来者）**：
- `combinedfleet.com/haruna_t.htm` → 404。正确是 `haruna.htm`。
- `combinedfleet.com/kirishima.htm` → 404。正确是 `Kirishima.htm`（首字母大写）。
  **同一站内大小写规则不统一**，抓之前两种都试。
- `navypedia.org/ships/japan/jap_bb.htm` → 404（没有日本战列舰索引页）。
- `ibiblio.org/hyperwar/Japan/IJN/JCA-13/index.html` → 404。

---

## 1. 任务书史实陈述的逐条核实结果

> 规则：查到的与任务书不符，**以来源为准**，并指出任务书写错了哪条。

### ❌ 错误 1：「榛名与雾岛都是英国建造（维克斯/阿姆斯特朗）」

**这条是错的。** 金刚级四舰里**只有金刚**在英国造，另外三舰全是日本造。

原文（navypedia，Ships 表逐舰给 Builder）：

> 金剛 [Kongo] | 414 | **Vickers, Barrow, UK** | 17.1.1911 | 18.5.1912 | 16.8.1913 | sunk 21.11.1944
> 比叡 [Hiei] | | **Yokosuka K K** | 4.11.1911 | 21.11.1912 | 4.8.1914 | sunk 13.11.1942
> 霧島 [Kirishima] | 225 | **Mitsubishi, Nagasaki** | 17.3.1912 | 1.12.1913 | 19.4.1915 | sunk 15.11.1942
> 榛名 [Haruna] | | **Kawasaki, Kobe** | 16.3.1912 | 14.12.1913 | 19.4.1915 | sunk 28.7.1945

原文（combinedfleet 榛名 TROM，1912-03-16）：

> Kobe. Battlecruiser HARUNA is laid down on No. 4 slip at **Kawasaki's shipyard**.
> HARUNA will be built based on plans for KONGO designed by Sir George Thurston of
> the British shipbuilding firm of Vickers-Armstrong.

原文（combinedfleet 雾岛 TROM，1912-03-17）：

> Nagasaki. A battlecruiser is laid down at **Mitsubishi Zosen Kaisha's shipyard**.
> She will be built based on plans for KONGO designed by Sir George Thurston of the
> British shipbuilding firm of Vickers-Armstrong. **Most of the parts used in her
> construction are manufactured in Japan.**

原文（日文来源，榛名页）：

> 初の超弩級戦艦【金剛】、初の国産超弩級戦艦【比叡】、そしてこの【榛名】は、
> 四番艦【霧島】とともに、**初の民間造船所建造の戦艦**となりました。
> 【榛名】を建造した川崎造船所と【霧島】を建造した三菱長崎造船所が、
> 激しいライバル争いを繰り広げる事にもなりました。

**结论**：榛名 = 川崎造船所（神户），雾岛 = 三菱长崎造船所，**都是日本民间船厂**，
且是日本**第一批由民间船厂建造的战列舰**。英国只出了图纸（Thurston 设计）
和金刚这一艘实舰。任务书这条把「设计是英国的」误记成了「建造是英国的」。

**这处错误在数据文件里怎么处理的**：没有为它单立 fact（负面事实不是字段），
而是写进 `classes/kongo.yaml` 的文件头注释与
`identity.building_program`、两舰 `construction.builder` 的 note 里，
防止后来者按任务书原话回填。

### ⚠️ 待修正 2：「两舰 1930 年代大改装完成时间：榛名 1934、雾岛 1936？」

**方向对，具体日需要补精确。**

- 榛名第二次改装完成：**1934-09-30**
  > 30 September 1934: The Second Reconstruction is officially completed.（combinedfleet 榛名）
- 雾岛第二次改装完成：**1936-06-08**
  > 8 June 1936: The second reconstruction is completed.（combinedfleet 雾岛）

即任务书猜的年份正确，但**日文来源对雾岛只给到「昭和11年/1936年」**
（约在 SPECIFICATIONS 段的时点标注），不到日。上面的日来自 combinedfleet。

**两舰差了约 20 个月**，这个差距对数据文件有实质影响 —— 见 §5 的
`date_convention_note`。

### ✅ 基本正确 3：「雾岛 1942-11 瓜岛第二次夜战被华盛顿号击沉」

正确。原文（combinedfleet 雾岛 TROM）：

> Undetected, WASHINGTON approaches to within 5,800 yards and opens fire at
> KIRISHIMA around 0000. First straddled, KIRISHIMA attempts to return fire, but
> her forward turrets are quickly disabled and a fire breaks out in the forward
> wireless station.

> 0325: KIRISHIMA suddenly rolls over and capsizes to port 7.5 miles NW of Savo
> Island at 09-05S, 159-42E. A total of 212 crewmen are lost. ASAGUMO, TERUZUKI
> and SAMIDARE rescue Captain Iwabuchi, his Executive Officer Cdr (Rear Admiral,
> posthumously) Ono Koro … and 1,098 survivors.

**需要补一句任务书没说的**：这是**太平洋战争中第一场战列舰对战列舰的交战**：

> The first battleship vs. battleship encounter in the Pacific War is over, as is
> Admiral Yamamoto's "decisive naval battle" for Guadalcanal.

### ✅ 基本正确 4：「榛名活到 1945 年被空袭坐沉」

正确，但要补精确：**1945-07-28 坐底于浅水**，且此前 07-24 已被重创。

> 28 July 1945: At Kure. From 0800 to 1700, HARUNA is attacked again by USS WASP's
> (CV-18) Air Group 86, SHANGRI-LA (CV-38) and other aircraft from Task Force 38.
> She receives many hits and near misses. …
> At 1615, HARUNA comes under a final heavy attack, and is holed portside. This
> causes a list that brings the gash inflicted on 24 July under water. HARUNA
> takes on tons of water and **sinks in shallow water next to a pier at 34-15N,
> 132-29E**. In the two days of attacks, HARUNA receives 13 bomb hits and 10 near
> misses. 65 officers and men are lost.

**「坐沉」的准确含义**：不是沉入深海，是**坐底在码头边**，舰体大部分露出水面，
战后浮扬解体：

> 1946-1948: The wreck of HARUNA is raised and broken up.

日文来源另给一个不同的解体日（见 §6 分歧 8）。

### ✅ 正确 5：「两舰参加了 1942-06 中途岛（机动部队第 3 战队第 2 小队）」

正确，两份 TROM 各自写明，但**出发日差两天**（见 §6 分歧 5）。

combinedfleet 榛名页：

> 29 May 1942: Operation "MI" - The Battle of Midway: The Support Group's BatDiv 3,
> Section 2's HARUNA and KIRISHIMA depart Hashirajima for Midway with Vice Admiral
> Nagumo's First Mobile Force, Carrier Strike Force: CarDiv 1's AKAGI and KAGA,
> CarDiv 2's HIRYU and SORYU, CruDiv 8's TONE and CHIKUMA, DesRon 10's light
> cruiser NAGARA and 11 destroyers.

combinedfleet 雾岛页：

> 27 May 1942: Rear Admiral Abe Hiroaki's (former CO of FUSO) Support Group,
> BatDiv 3, Section 2's KIRISHIMA and HARUNA depart Hashirajima with Vice Admiral
> Nagumo's First Mobile Force, Carrier Strike Force: …

**任务书的「机动部队第 3 战队第 2 小队」需要一点精确化**：两舰编在
**阿部弘毅少将的支援部队（Support Group）**，随第一机动部队行动，
但**不属于航母本队**，任务是护卫。这一点在两份 TROM 里是一致的。

**还要注意「第 3 战队第 2 小队」这个编成只存在于中途岛这一次作战**：

> 14 July 1942: HARUNA is assigned to the Second Fleet. Vice Admiral Kurita Takeo
> … assumes command of the resized BatDiv 3's KONGO (F) and HARUNA… HIEI and
> KIRISHIMA are reassigned to the new BatDiv 11.（榛名页）

> 14 July 1942: KIRISHIMA and HIEI (F) are reassigned from the First Fleet to Vice
> Admiral Nagumo's Third Fleet in Rear Admiral Abe Hiroaki's new BatDiv 11.（雾岛页）

即 1942-07-14 起，榛名与金刚同队、雾岛与比叡同队，此后直到雾岛沉没再未同队。
1941-11-29 时第二小队也是榛名＋**金刚**（不是雾岛）。

---

## 2. 核心结论与英文原句（按主题）

### 2.1 本级分类与命名

navypedia 页标题即定性：

> **KONGO battlecruisers (1913 - 1915)**

日文来源写改装后的转变：

> 第一次改装後は25ノットだった速度は、第二次改装によって30ノットを超え、
> 【**高速戦艦**　榛名】が誕生しました。（榛名页）

combinedfleet 对雾岛用同一措辞：

> Sasebo. KIRISHIMA is reconstructed to transform her into a **fast battleship**.

→ 本站 `identity.ship_type` 分两段：`battlecruiser`（1915-04-19 起）→
`battleship`（各舰第二次改装完成日起：榛名 1934-09-30 / 雾岛 1936-06-08）。

**改级令的具体日期未获取**（没有找到「某年某月某日海军省令改为战舰」这类原文），
故只按「改装完成」这个工程节点切换，并在 note 说明是工程节点而非编制命令。

命名原文（榛名）：

> 5 June 1911: Vice Admiral Saito Makoto (6), the current Navy Minister, issues an
> order to name the third vessel of the KONGO class HARUNA **after a volcano in
> Gumma Prefecture**.

**雾岛的命名来源（霧島山）没有原文**，只有「Launched and named KIRISHIMA」。
故雾岛文件里只记命名事实，命名来源写在 note 里并标明是推断。

### 2.2 建造日期（三源互证）

| 项 | 榛名 | 雾岛 |
|---|---|---|
| 开工 | 1912-03-16 | 1912-03-17 |
| 下水 | 1913-12-14 | 1913-12-01 |
| 竣工 | 1915-04-19 | 1915-04-19 |

navypedia：`16.3.1912 / 14.12.1913 / 19.4.1915`（榛名）、`17.3.1912 / 1.12.1913 / 19.4.1915`（雾岛）
日文来源：`明治45年/1912年3月16日` 等，与 navypedia 一致。

**同日竣工的原因（日文来源，只此一家）**：

> この事件から、予定通りならば【霧島】が先に竣工することになるのですが
> 両者は竣工日を合わせ、**ともに4月19日生まれ**となったのです。

前面提到的「この事件」是榛名竣工前的缺陷返工：

> しかし完成直前で発覚した欠陥の修復のために工期が6日遅れることになると、
> 川崎造船所造機工作部長の篠田恒太郎が責任を感じ自刃するという不幸な出来事もありました。

### 2.3 排水量四口径（本级最容易混的一块）

navypedia 的表是**三个状态 × 若干列**，其中标准排水量一列的处理很关键：

```
Data variant            | as completed | 1928-1931 modernization | 1934-1940 modernization
Displacement standard,t | ---          | 29330                   | Kongo: 31720  Hiei: 32350
                        |              |                         | Kirishima: 31980  Haruna: 32156
Displacement normal, t  | 27500        |                         |
Displacement full, t    | 32200        | 31785                   | 36601
```

**四条必须记住的口径规则**：

1. **as completed 列的标准排水量是「---」**，navypedia 只给 `normal 27,500 t`。
   `normal` 与条约 `standard` 不是同一口径，**不能拿 27,500 当标准排水量**。
   本站的 26,330 t 取自日文来源的「基準排水量 ① 26,330t」。
2. **第二次改装后的标准排水量是逐舰给的**（31,720 / 32,350 / 31,980 / 32,156），
   而其余各项（全长、宽、吃水、马力、燃油、续航、装甲）全级共用一个值。
   **不可把逐舰值当全级值，也不可反过来把全级值当逐舰值。**
3. 日文来源的 ① 26,330 / ② 29,330 / ③ 32,156（榛名）、③ 31,980（雾岛）
   与 navypedia 的逐舰值互证（32,156 / 31,980 完全对得上）。
4. **试验排水量（displacement.trial）本轮未获取**，四舰都没有倾斜试验记录。

**试航排水量、深载排水量、空载排水量：全部未获取。**

### 2.4 主尺度（含 1.7 m 的宽度分歧）

长度三源一致度较高：

> Length, m | 212.1 wl 214.5 oa | 212.1 wl 215.2 oa | 219.6 wl 222.1 oa（navypedia）

日文来源给水线长：`① 212.00m / ③ 219.61m`（榛名、雾岛同值）。

**舰尾延长的幅度两源不同**（见 §6 分歧 2）。

**宽度是本节最大分歧**（见 §6 分歧 1）：

- navypedia：`Breadth, m | 28.0 | 29.3 | 29.3`，且明写
  > Bulges were fitted, **breadth rose to 29.3m**. 4 TT were removed.
- 日文来源：`水線下幅 ① 28.04m / ② 31.02m / ③ 31.01m`

差 1.7 m。可能不是同一测量位置（日文写「水線下幅」= 水线下宽，
英文 `Breadth` 通常指最大宽），但**两源都没有明说测量定义**，
本站**两说并列、不裁决**，且 `dimensions.beam.wl` 取 navypedia 的 29.3。

吃水只有 navypedia 一家：`8.40 / 8.65 / 9.72`，**未标明对应的排水量状态**
（注册表 `dimensions.draught.mean` 的 note 要求必须与排水量状态绑定），
已在每条 note 里注明这个缺口。

### 2.5 动力 —— **本级最关键的两舰差异**

这是任务书特别点名要查的一项，结论是：**两舰的大改装动力配置不同，且与金刚/比叡也分组不同。**

navypedia（Machinery 行，三段）：

> **as completed**: Kongo, Hiei, Kirishima: 4 Parsons steam turbines, 36 Yarrow
> boilers / Haruna: 4 Brown-Curtis steam turbines, 36 Yarrow boilers
>
> **1928-1931**: Kongo, Kirishima: 4 Parsons steam turbines, **10** Kampon boilers /
> Haruna: 4 Brown-Curtis steam turbines, **16** Kampon boilers
>
> **1934-1940**: Kongo, Kirishima: 4 sets Kampon geared steam turbines, **8** Kampon
> boilers / Haruna, Hiei: 4 sets Kampon geared steam turbines, **11** Kampon boilers

日文来源（榛名页，逐期给，且区分混烧/专烧）：

> ① ロ号艦本式ボイラー（**混焼**）　36基[1-P88][2-P30] ／ ブラウン・カーチス式タービン　2基4軸
> ② ロ号艦本式ボイラー　**混焼10基、重油専焼6基**[1-P88] ／ ブラウン・カーチス式タービン　2基4軸
> ③ ロ号艦本式ボイラー（**重油専焼**）　11基[1-P88] ／ 艦本式ギアード・タービン　4基4軸

日文来源并特别点出这一项是四舰里唯一的差别：

> 改装の内容は【金剛】を参照にしていただければと思いますが、**1点異なる点があります**。
> ボイラーについては、第一次改装で混焼缶10基を残し、重油専焼缶6基を装備していまししたが、
> 第二次改装では**重油専焼缶11基**の構成となりました。[1-P88]

日文来源（雾岛页，第一次改装锅炉**自己并列两说**）：

> ロ号艦本式ボイラー　重油専焼10基[1-P88] **or** 重油専焼4基＋混焼6基[5]

combinedfleet（榛名，第一次改装）：

> During the rebuild all of HARUNA's 36 Yarrow boilers are replaced with **16
> Kampon RO-Go type boilers**. The number of funnels is reduced from three to
> two, deleting the fore funnel. As a result of the changes in the boiler room
> layout, **two remaining funnels are now more widely spaced than in other vessels
> of that class**.

combinedfleet（榛名，第二次改装）：

> All boilers are replaced with **11 oil-firing Kampon boilers** and she receives
> new geared turbines. Her speed is increased to 30 knots.

combinedfleet（雾岛，第二次改装）：

> All boilers are removed and replaced with **8 Kampon boilers** and she receives
> new geared turbines. Her speed is increased to 30 knots.

**汇总表（写进数据文件的结论）**：

| 状态 | 榛名 | 雾岛 |
|---|---|---|
| 建成时锅炉 | 36 座（日文：ロ号艦本式混烧 / navypedia：Yarrow） | 36 座（同上） |
| 一次改装后 | **16 座**（混烧 10 + 重油专烧 6） | **10 座**（专烧 10 或 混烧 6+专烧 4，两说） |
| 二次改装后 | **11 座**（重油专烧） | **8 座**（重油专烧） |
| 涡轮（建成） | **Brown-Curtis** 2 台 4 轴 | **Parsons** 2 台 4 轴 |
| 涡轮（二次改装后） | 艦本式齿轮传动 4 台 | 艦本式齿轮传动 4 台 |
| 设计马力 | 64,000 → 136,000 hp | 64,000 → 136,000 hp |
| 试航实测 | **未获取** | **136,940 hp @ 29.80 kn**；144,500 hp @ 30.08 kn |

**任务书的「混烧还是重油专烧？两舰改装不同」——核实结果**：
不是「一舰混烧一舰专烧」，而是**座数不同（16→11 vs 10→8）、
改装节奏不同（榛名两次都领先约 20 个月）**，且混烧/专烧的**过渡方式也不同**
（榛名一次改装明确留 10 座混烧 + 6 座专烧；雾岛一次改装时
日文来源自己就给了两种构成）。

雾岛试航数据原文（**四舰唯一有实测的一艘**）：

> 第二次改装後の公試運転では、公試全力で**29.80ノット・136,940軸馬力**、
> 過荷全力で**30.08ノット・144,500軸馬力**を記録しています[3]。
> 上記の136,000馬力[1-P88]は、これらの公試実測値とは区別して記載しています。

出处 [3] 为『軍艦霧島第二回改装公試運転成績』（一手试航记录）。

**榛名的马力栏只有设计值，没有实测**（见 §7 未获取清单），
故 `ships/haruna.yaml` **没有** `propulsion.power.trial` / `speed.trial` 两条 fact。
**严禁用雾岛值代入。**

### 2.6 续航（数值与对应航速双分歧）

> Endurance, nm(kts) | 8000(14) | 10000(18) | 10000(18)（navypedia）

日文来源逐舰逐期给，且**第一次改装后用的是 14 kn、第二次才是 18 kn**：

| 舰 | ① 建成 | ② 一次改装后 | ③ 二次改装后 |
|---|---|---|---|
| 榛名 | 14 kn : 8,000 | **14 kn : 9,500** | 18 kn : **10,000** |
| 雾岛 | 14 kn : 8,000 | **14 kn : 10,000** | 18 kn : **9,850** |
| 金刚（旁证） | 14 kn : 8,000 | 14 kn : 10,000 | 18 kn : 9,800 |

→ 与 navypedia 的 `10000(18)` 在**第一次改装后**这一状态上，
**不但数值不同，连对应航速都不同**（14 vs 18 kn）。两说并列不裁决。

### 2.7 防护（表格与文字有若干处对不上）

navypedia 装甲行（三段，**几乎全同，只有弹药库上方与炮座有变化**）：

> **as completed**: belt: 203 - 76, bulkheads: 203 - 127, deck: 57 - 38,
> barbettes: 254, turrets: 229 - 76, casemates: 152, CT: 254
>
> **1928-1931**: belt: 203 - 76, bulkheads: 203 - 127, deck: 57 - 38,
> **over magazines: 120, over machinery: 80**, barbettes: **305**, turrets: 229 - 152,
> casemates: 152, CT: 254
>
> **1934-1940**: …(同上)… **over magazines: 152**, over machinery: 80, barbettes: 305,
> turrets: 229 - 152, casemates: 152, CT: 254

同页的文字段落（Ship protection）：

> 3.8m-high main belt extended from No1 to No4 barbettes and had 203mm thickness
> between barbettes. It closed by 152-127mm bulkhead abreast No1 barbette and
> 203-152mm bulkhead abreast No4 barbette. Ship ends from end barbettes to ship
> ends were protected by 76mm belt. Upper 152mm belt extended from main belt to
> upper deck and from No1 to No4 barbette. It was closed by 152mm bulkheads.
> Casemates had also 152mm armor. **Main 19mm deck connected with lower edge of
> main belt by 19mm slopes.** Forecastle deck and upper deck aft from No3 barbette
> had 38mm protection.

第二次改装后追加：

> **There was 51-40mm anti-torpedo longitudinal bulkhead.**

**两处表格与文字对不上，已在数据文件里逐条标注**：

1. **`deck: 57 - 38` 中的 57 在文字里找不到对应部位**。文字只提到
   「Main **19mm** deck」「19mm slopes」「Forecastle deck and upper deck aft …
   38mm」，以及改装后「increased to 80mm over machinery and 152mm over magazines」。
   57 这个数没有归属。本站照抄表格值并标存疑，**不自行解释**。
2. **`barbettes: 254` → `305`，但同时又说「Barbettes under main deck were
   strengthened to 152-140 mm.」** 305 与 152-140 显然不是同一段，
   本站把 305 记为 `region: main`，152-140 只留在 note。

**装甲总重、水下防护纵深：未获取。** navypedia 只有一句
`Underwater protection could resist exploding of 200kg TNT.`
——这是**抗爆当量**，不是纵深米数，**不能填 `protection.underwater.depth`**。

**`protection.scheme` 是分类判断，来源没用过 incremental 这个词**，
已在 fact 的 note 里写明判据（分部位削薄 + 多层叠加 + 甲板与主带用斜板相接），
confidence 记 C。若日后找到明写防护体系的文献，应以文献为准。

### 2.8 武备

#### 主炮（金刚装英造，另三舰装日产 —— 这是修正误解的关键）

navweaps 原文（命名沿革）：

> The original design was submitted by Vickers to the Japanese in November 1910.
> In an effort to hide their true size, Vickers designated these guns on their
> internal documents as the 12-in Vickers Mark "J" and the Japanese documented
> them as the 12-in Meiji 43 Type (the 43rd year of the Meiji era being 1910).
> Later, the guns built by Vickers were known as the **14-in Vickers Mark "A"** and
> to the Japanese as the **14-in 43rd Year Type (Model 1910)**. Guns manufactured
> in Japan were known as **14-in 41st Year Type (Model 1908)**. In 1917, when the
> Japanese converted to metric, all of these guns were then designated as 36 cm
> (14.2 inches) but **their bores remained unchanged at 14.0 inches (35.6 cm)**.

navypedia 装甲行亦按此分：

> Kongo: 4 x 2 - 356/45 **43-shiki**, … **others: 4 x 2 - 356/45 41-shiki**

→ **金刚装英造 43rd Year Type，榛名/雾岛装日产 41st Year Type。** 两者性能相近
（navweaps：`and they and the Vickers guns had similar performance and can be
considered together`），但型号名不同，不可互写。

主要数据（navweaps）：

| 项 | 值 | 原文 |
|---|---|---|
| 炮身重 | 86,000 kg | `Gun Weight 189,586 lbs. (86,000 kg)` |
| 全长 | 16.469 m | `Gun Length oa 648.4 in (16.469 m)` |
| 膛线长 | 13.737 m | `Rifling Length 540 in (13.737 m)` |
| 药室 | 294.9 dm³ | `Chamber Volume 17,996 in3 (294.9 dm3)` |
| 射速 | 2 rpm | `Rate Of Fire 2 rounds per minute` |
| 炮管寿命 | 250–280 发 | `Approximate Barrel Life 250 - 280 rounds` |
| 弹药基数 | 80 发/炮（平时设计） | `Ammunition stowage per gun 80 rounds` |
| 战时基数 | 约 110 发/炮 | `When the war started the outfit was increased to about 110 rounds per gun` |
| 发射药 | 142.3 kg（四药包） | `Propellant Charge 313.8 lbs. (142.3 kg) 85 DC` / `The propellant charge was in four bags.` |

弹重与初速（**初速原文是区间，本站只收下限并在 note 保留区间，不取平均**）：

> APC Type 91: 1,485 lbs. (673.5 kg) — 初速 2,526 - 2,543 fps (770 - 775 mps)
> Common Type 0 HE: 1,378 lbs. (625 kg) — 初速 2,641 fps (805 mps)
> Common Type 3 IS: 1,371 lbs. (622 kg) — 初速 2,641 fps (805 mps)

仰角三阶段（原文）：

> As commissioned: -5 / +25 degrees
> As modified in the 1920s: -5 / +33 degrees
> As rebuilt in the 1930s: -5 / +43 degrees

射程（APC Type 91，43.0° = 炮塔最大仰角）：`38,770 yards (35,450 m)`

**弹道染料（1941 起，识别弹着的实用数据，原文）**：

> Kongô: Red
> **Haruna: Black**
> **Kirishima: Blue**
> Hiei: None (White)

**炮塔侧面曲面的外形差异（日文来源，模型制作者最需要）**：

> 【榛名】と【霧島】の類似点としては、**砲塔の側面に曲面があるところ**。
> 【金剛】と【比叡】は平面で構成されています。

#### 副炮 15.2 cm（四舰撤除台账两源冲突）

navweaps 页内脚注（**直接点了榛名与金刚的撤除数**）：

> Kongô had two more guns removed in early 1943 and a further four removed in
> January 1944. **Haruna had six guns removed in March 1943.** Removed guns were
> replaced with 12.7 cm/40 Type 89 and 25 mm AA guns.

combinedfleet 榛名的记载拆得更细：

> Two foremost casemate guns are landed.（1937-11～1938-11）
> Two secondary guns are landed.（1943-03～04）
> **Four secondary guns are landed.**（1943-12-16～1944-02-26）

→ **冲突**：navweaps 说榛名 1943-03 一次撤 6 门；combinedfleet 说 1943-03 只撤 2 门、
1944 年初再撤 4 门（合计也是 6 门，但**节点不同**）。
两说并列不裁决，详见 §6 分歧 9。

日文来源的终点状态可作裁决参考（但只覆盖到 1944-10）：

> 50口径15.2cm単装砲　**8基8門**（1944-10-05 兵装表）

16 − 2（1938）− 2（1943）− 4（1944）= 8，与 combinedfleet 的记账吻合。
**但本站仍不裁决**，只把三说都记下（见 `ships/haruna.yaml` 的 `armament.mount.summary` note）。

主要数据（navweaps）：

> Gun Weight 18,430 lbs. (8,360 kg) / Gun Length oa 310.1 in (7.876 m)
> Rate Of Fire — Theoretical: 10 rounds per minute / **Effective: 5 - 6 rounds per minute**
> Muzzle Velocity — All except ASW: 2,790 - 2,805 fps (850 - 855 mps)
> Approximate Barrel Life 500 - 600 Rounds

仰角：`Kongô and Fuso: -5 / +20 degrees as built, +30 degrees as modernized`

#### 高炮 12.7 cm 八九式（**两舰座数差别的关键**）

navweaps 原文一句话把四舰都钉住了：

> Older battleships of the Kongô, Fuso, Ise and Nagato classes had their 8 cm (3")
> 41st Year Type and 3rd Year Type AA guns removed during their 1930s rebuilds and
> replaced with the new 12.7 cm/40 (5") Type 89 in **four twin mounts**. **Kongô and
> Haruna had two additional twin mountings added in 1944.** Ise and Hyuga were given
> four additional twin mountings in 1943 when they were converted to hybrid carriers.

→ **① 四舰都从 4 座起步；② 1944 年只有金刚与榛名各加 2 座（→ 6 座）；
③ 雾岛 1942-11 就已战没，终生只有 4 座 8 门。**

这是两舰最容易被写成「同级同型」的一处，已在
`ships/kirishima.yaml` 的 `armament.mount.summary` 里明确写出对比。

炮座型号：`Kongô (4), Fuso (4), Ise (4) and Nagato (4): A1`，
A1 释义：`The A1 mount was unshielded.`

主要数据：

> Gun Weight 3.05 tons (3.1 mt) / 炮身全长 5.284 m
> Rate Of Fire — Type 89: **14 rounds per minute initially, 8 rounds per minute sustained**
> Muzzle Velocity — Common Type 0 HE: 2,360 - 2,379 fps (700 - 725 mps)
> AA Ceiling @ 75 degrees — 30,840 feet (9,400 m)
> Range of IS projectiles @ 45° — 16,185 yards (14,800 m)
> Elevation — Type 89: -7 / +90 degrees (one source says -8 / +85 degrees)
> Approximate Barrel Life 800 - 1500 rounds

#### 机炮 25 mm 九六式（数量随时间变化，且两舰差别极大）

navweaps：

> Rate Of Fire — Cyclic: 200 - 260 rounds per minute, **220 standard** /
> **Effective: 110 - 120 rounds per minute**
> Muzzle Velocity 2,953 fps (900 mps)
> Elevation -10 / +85 degrees
> Approximate Barrel Life 12,000 rounds / Ammunition stowage per gun 2,000 rounds

**装舰数量台账（榛名，逐节点）**：

| 时点 | 管数 | 依据原文 |
|---|---|---|
| 1938 | 20（10×2） | combinedfleet：`Twenty 25-mm Type 96 AA guns (10x2) and four Type 95 HA directors are installed.` |
| 1943-04 | 26（+2×3） | combinedfleet：`Two 25-mm triple mounts are installed.` |
| 1944-02 | 38（+4×3） | combinedfleet：`…and twelve 25-mm AA guns (4x3) are added.` |
| 1944-10-05 | **108** | 日文来源逐型：`25mm三連装機銃 28基84挺／25mm連装機銃 2基4挺／25mm単装機銃 20基20挺` |
| 1945-01 | +17 单装 | navypedia：`1/1945, Haruna: + 17 x 1 - 25/60 96-shiki` |

**雾岛：沉没时仍是 20 挺（10×2），终生未获大幅增装。**

> Kirishima, Hiei: … 10 x 2 - 25/60 96-shiki（navypedia）

combinedfleet 唯一相关记载是**移位**而非加装：

> 11 May 1942: At Sasebo. Drydocked. **25-mm AA guns Nos. 7 and 8 are relocated**
> from the upper deck to the vicinity of the forward funnel to provide better arcs
> of fire.

**注意 navweaps 引 USNTMJ O-47(N)-2 的同级表**：

> Ise, Fuso and Kongô classes | Triples 20 | Twins 6 | Singles 30

——这是该报告统计的该级某艘（很可能是 1945 年状态最重的一舰）的合计，
**不能直接套到任一单舰**。已在数据文件 note 里明确警告。

#### 13.2 mm 与 40 mm 维克斯（两源冲突）

combinedfleet 榛名 1932-05-22：

> The 8 cm/40 3rd Year Type AA guns and 7.7 mm Type 92 machine guns are replaced
> by **eight 12.7-cm/40 Type 89 AA guns (4x2)** and **four 40-mm Vickers AA guns (2x2)**.

日文来源第二次改装栏：

> 40mm連装機銃　2基4挺　⇒のちいずれも撤去　25mm連装機銃 10基20挺

navypedia 第二次改装后（榛名）：

> Haruna: 4 x 2 - 356/45 41-shiki, 14 x 1 - 152/50 41-shiki, 4 x 2 - 127/40 89-shiki,
> **4 x 2 - 13.2/76**, 1 catapult, 3 seaplanes (E7K2)

→ **navypedia 说榛名改装后装的是 13.2 mm（4×2），
combinedfleet 与日文来源说装的是 40 mm 维克斯 4 挺，且后来撤除换 25 mm。**
两说并列不裁决，详见 §6 分歧 6。

（注意：`armament.aa_40mm.count` 字段的注册表注释写的是「美军 40 mm Bofors」，
榛名装的是**英制维克斯**，口径同为 40 mm。已在 fact note 里注明型号不同。）

#### 鱼雷发射管（明确拆除 → 记 0，不是未获取）

| 时点 | 数量 | 原文 |
|---|---|---|
| 建成 | 8 | navypedia：`8 - 533 TT (beam)`；日文：`53.3cm魚雷発射管 8門（水中）` |
| 一次改装后 | 4 | navypedia：`4 TT were removed`；日文：`53.3cm魚雷発射管 4門（水中）` |
| 二次改装后 | **0** | 日文鱼雷栏直接写 `撤去`；navypedia 装备栏已无 TT 项 |

#### 建成时的 7.6 cm 炮：两源分列方式不同

> navypedia（as completed）：`8 x 1 - 76/40 41-shiki`
> 日文来源（榛名竣工时）：`40口径短7.6cm単装砲 4基4門` + `40口径8cm単装砲 8基8門`

即 navypedia 8 门 vs 日文 4+8=12 门。**两源冲突，未裁决**，
已写进 `classes/kongo.yaml` 的 `armament.mount.summary` note。

### 2.9 航空

弹射器与机型的逐期变化（榛名，combinedfleet）：

> **1928（一次改装）**：A derrick boom is rigged to the superstructure starboard aft
> for one Yokosho E1Y3 Type 14 and one Nakajima E2N1 Type 15 floatplane. An aircraft
> handling deck is fitted between the aft turrets (Nos. 3 and 4). [**无弹射器**]
> 日文来源同期：`水上機　3機（**射出機なし**）`
>
> **1932-05-22**：The aircraft handling deck is extended to accommodate a **Kure Type
> No. 2 Model 3 catapult** installed on the port side aft of No. 3 turret. One E1Y3
> and two Nakajima E2N Type 15 floatplanes are embarked.
>
> **1933-08-01（二次改装）**：A **centerline Kure Type No. 2 Model 3 Mk. 1 catapult**
> and a collapsibe derrick are installed. Two Nakajima E4N2 Type 90 No. 2 Model 2 and
> one Kawanishi E7K1 Type 94 ("Alf") floatplanes are embarked.
>
> **1937-11～1938-11**：A new **Kure Type No. 2 Mod. 5** catapult is installed for a
> Kawanishi E7K1 Type 94 ("Alf") and two Nakajima E8N1 Type 95 ("Dave") floatplanes.
>
> **1942-07-14**：Her floatplane complement is now **three E8N2s**.
>
> **1943-02-25～04-01**：The aircraft complement is changed to one Aichi E13A Type 0
> and two Mitsubishi F1M Type 0s.
>
> **1944-08-15**：Two E13A1 floatplanes are embarked.

雾岛机型：

> 1933（late）：Aircraft handling deck is extended to accommodate a catapult.
> **Two to three** Nakajima E4N2 Type 90-2-2 floatplanes are embarked.
>
> 1936-06-08（二次改装）：She is reequipped with **two Nakajima E8N1 Type 95 Dave and
> one Kawanishi E7K1 Type 94 Alf** floatplanes.
>
> 1942-07-14：… they receive **one Aichi E13A1 "Jake"** reconnaissance floatplane and
> **two Mitsubishi Type F1M2 "Pete"** floatplanes, **tail codes CIII-x (in red)**.

**雾岛的弹射器型号未获取**：

> Late 1933: Aircraft handling deck is extended to accommodate a catapult.
> 1939-11-15: … A new catapult is fitted (**probably earlier**).

combinedfleet 自己标了 `(probably earlier)`，navypedia 只写 `1 catapult`，
**两源都没给型号**。故 `ships/kirishima.yaml` 的 `aviation.catapult.type`
记「弹射器 1 座（型号未获取）」，**不使用榛名的吴式型号代入**。

### 2.10 雷达（雾岛有一个明确的否定性结论）

**雾岛：沉没时无雷达。** combinedfleet 专门立注驳斥流行说法：

> [3] Several sources suggest that KIRISHIMA was fitted with a "Type 21 Model 1"
> radar in early August. **This is not correct**: KIRISHIMA was scheduled to
> receive a Type 21 radar, but **departed without it**.

→ 这条已写进 `ships/kirishima.yaml` 的 `sensors.radar.installed`，
value 写「未获取（沉没时无雷达）」，note 全文引上述原句。

**榛名：多型并存，但只有两型的装设期能确定。**

> 1943-02-25～04-01：A **Type 21 radar** and Type 3 radar detectors are installed.
> 1944-06-27～08-10：**Type 13 radar** and additional 25-mm AA guns are installed.
> The **existing Type 22 radars** are fitted with superheterodyne receivers.

→ 1944-08 时已有二二号电探（`existing`），**但装设日期来源没给**。
日文来源的 1944-10-05 兵装表给的是**存在状态**不是装设日：

> 21号対空電探　1基／22号対水上電探　2基／13号対空電探　2基

故 `sensors.radar.installed` 的二二号一条**不写**（缺 valid.from），
只把存在状态写进 `sensors.radar.count`（5 基，分型相加，非推算）。

### 2.11 中途岛与瓜岛战历

**中途岛（1942-06）**：

> 4 June 1942（榛名）：At 0430, HARUNA catapults a "Dave" floatplane to search for
> American carriers northeast of the Striking Force. … At 0817, HARUNA and
> KIRISHIMA are attacked by 11 Midway-based obsolete Marine SB2U-3 "Vindicator"
> dive-bombers, but they only score near-misses. **When KAGA is set afire, HARUNA
> briefly closes to assist.**
> At 1020, two SBDs from YORKTOWN approach HARUNA from her starboard beam and score
> two very near misses. The battleship disappears behind the waterspouts and some
> lookouts on nearby vessels report her as lost.

> 4 June 1942（雾岛）：KIRISHIMA is steaming abreast with AKAGI on her starboard
> beam when the Strike Force is attacked by four USAAF torpedo-carrying Martin B-26
> "Marauders" … KIRISHIMA helps to repel the attack, firing her main caliber guns.
> Two of the B-26s are shot down.
> 0825: LtCdr William H. Brockman in USS NAUTILUS (SS-168) fires a Mark 14 steam
> torpedo at KIRISHIMA from 4,500 yards but misses. … KIRISHIMA opens fire with her
> starboard batteries unsuccessfully at the submarine's periscope.

> 1730（雾岛）：Captain Iwabuchi is ordered to standby to tow HIRYU with KIRISHIMA.

**两舰在中途岛均未受损**（只有近失弹）。榛名 6 月 5 日另有一次空袭：

> At about 1600, HARUNA is attacked by SBDs not far from where TANIKAZE was attacked.
> **HARUNA suffers but minor damage.**

**瓜岛 — 第一次所罗门夜战（1942-11-13）**：两舰都**没有直接参战**。

> 13 November 1942（榛名）：BatDiv 3, cruising near Ontong Java Atoll, provides
> **distant support** for Kondo's Emergency Bombardment Force against Henderson Field.

雾岛参加了第一夜（作为阿部部队一员），但当天主要损失是比叡：

> During the battle, KIRISHIMA fires 27 Type 1 AP, 22 Type 3 and 8 Type 0 incendiary
> 14-in shells, plus 313 secondary caliber shells.

**第二次所罗门夜战（1942-11-14/15）**：雾岛沉没；榛名**在外围**。

> 15 November 1942（榛名）：After the loss of BatDiv 11's KIRISHIMA off Savo Island,
> BatDiv 3 departs the area for Truk.

雾岛当夜的开火记录（**三源数字不同，见 §6 分歧 11**）：

> Around 2353, KIRISHIMA and ATAGO illuminate SOUTH DAKOTA with their searchlights
> and then open fire, followed by TAKAO; ATAGO also launches a salvo of eight
> torpedoes. Within the next few minutes **KIRISHIMA fires a total of 117 14-inch
> shells (68 Type 3 incendiaries, 22 Type 0 Common and 27 Type 1 APC)**, scoring
> multiple hits with secondary and main guns. One Type 1 APC explodes against
> SOUTH DAKOTA's No. 3 turret's barbette.

**榛名 1942-10-13 对亨德森机场的炮击（本级最著名的一次火力投射）**：

> Beginning at 0133, BatDiv 3 bombards Henderson Field, Guadalcanal. HARUNA and
> KONGO fire **918 (483 and 435 respectively) 14-in shells** including Type 3
> "Sanshikidan" incendiary shells originally designed as AA rounds. After the HE
> shells are expended, BatDiv 3 continues the bombardment with less effective AP
> shells. Kurita's battleships destroy more than 40 U.S. aircraft on the ground.

即**榛名 483 发、金刚 435 发**。

### 2.12 结局

**雾岛**：1942-11-15 03:25 翻覆沉没于萨沃岛西北 7.5 海里（09-05S, 159-42E），
阵亡 212、生还 1,098，1942-12-20 除籍。

> 20 December 1942: BatDiv 11 is deactivated and KIRISHIMA is removed from the Navy List.
> August 1992: Oceanographer Dr. Robert D. Ballard discovers the wreck of KIRISHIMA in
> 4,000 feet of water, **resting upside down with its bow blown off**.

**榛名**：1945-07-24 / 07-28 两日空袭，坐底于吴港码头边（34-15N, 132-29E），
阵亡 65，1945-11-20 除籍，1946–1948 浮扬解体。

> 20 November 1945: Removed from Navy List.
> 1946-1948: The wreck of HARUNA is raised and broken up.

日文来源的另一种说法（**与上冲突，见 §6 分歧 8**）：

> 退役日（解体）昭和21年/1946年7月4日

日文来源另有一段评价与「浮炮台」的细节：

> この被害も重なった【榛名】は、潜水艦の襲撃を護衛艦とともにくぐり抜け、
> せっかく無事に帰投できたものの、燃料もなくなったために**呉で浮き砲台**としての
> 任務につくことになりました。
> 昭和20年/1945年6～7月の間、幾度と無くアメリカ軍の空襲を受け、**ついに大破着底**。
> しかし弾薬庫は浸水しておらず、砲撃は依然可能であったため
> 「着底したのなら、もう沈むことはない！」と士気はより一層高まったと言われています。

---

## 3. 舰级 vs 单舰的分工

| 内容 | 放哪 | 理由 |
|---|---|---|
| 主尺度三段（长/宽/吃水） | 舰级 | 四舰同一图纸，同一改装方案 |
| 排水量（三段） | 舰级 + 单舰 | 前两段全级同值（舰级）；第二次改装后**逐舰不同**（单舰） |
| 轴数、动力型式、设计马力、续航（navypedia 值） | 舰级 | 全级共用一个数 |
| **锅炉座数与型号** | **单舰** | **榛名 11 座 vs 雾岛 8 座，本级最关键差异** |
| **涡轮厂牌** | **单舰** | 榛名 Brown-Curtis vs 雾岛 Parsons |
| **试航实测马力/航速** | **单舰** | 只有雾岛有 |
| 装甲各部位 | 舰级 | 同一改装方案，全级同值 |
| 武器本体（weapon:*） | 舰级 | 同型炮共享 |
| **12.7 cm / 25 mm 座数** | **单舰** | **雾岛 4 座/20 挺，榛名 6 座/108 挺** |
| 弹射器型号、机型 | 单舰 | 逐舰、逐期不同 |
| 雷达 | 单舰 | 雾岛无雷达，榛名三型并存 |
| 编制 | 单舰 | 逐舰（虽 navypedia 全级同值，但时间窗逐舰不同） |
| 建造日期、舰长、战历、结局 | 单舰 | 逐舰 |

---

## 4. 交付清单

| 文件 | 状态 | fact 数 |
|---|---|---|
| `classes/kongo.yaml` | ✅ 完成 | 132 |
| `ships/haruna.yaml` | ✅ 完成 | 69 |
| `ships/kirishima.yaml` | ✅ 完成 | 54 |
| `sources-fragment.yaml` | ✅ 完成 | 9 条新来源 |
| `RESEARCH-NOTES.md` | ✅ 本文件 | — |

**校验结果**（`scripts/validate.py` 跑在 `_raw/_valdata/` 的合并副本上）：

```
通过：0 错误 / 0 警告
classes/kongo.yaml: 132 条 fact，0 处同日窗分歧，其中 27 条为多来源互证
ships/haruna.yaml:   69 条 fact，0 处同日窗分歧，其中 19 条为多来源互证
ships/kirishima.yaml: 54 条 fact，1 处同日窗分歧，其中 16 条为多来源互证
```

> 那 1 处「分歧」是故意的：`ships/kirishima.yaml` 的
> `propulsion.speed.max` 同时记了 navypedia 的 30.5 kn 与日文实测的 30.08 kn，
> 两者都是有效记载、都写了 note，校验器判为合法分歧（不报错）。
> 这是「两说并列不裁决」的正常形态，不是缺陷。

**未做**：`slices/`（状态切片）与 `articles/`（正文）。
任务书只要求 4 个 yaml + 本笔记，切片与正文按主会话后续合并时再生成；
若需要，本文件的 §2 已把切片边界（1928-07-31 / 1930-04-16 / 1934-09-30 /
1936-06-08 / 1937-11 / 1942-07-14 / 1943-03 / 1944-08 / 1945-07-28）
和事件原文都准备好了。

---

## 5. ⚠️ 舰级文件时间窗的已知简化（合并时必须知道）

`classes/kongo.yaml` 的三段式时间窗用的是**榛名的改装完成日**：

| 段 | 舰级文件用的日期 | 依据 |
|---|---|---|
| 建成时 | 1915-04-19 起 | 两舰同日竣工，无争议 |
| 第一次改装后 | **1928-07-31** 起 | 榛名完成日 |
| 第二次改装后 | **1934-09-30** 起 | 榛名完成日 |

**但雾岛的两个节点分别是 1930-04-16 与 1936-06-08，比榛名各晚约 20 个月。**
所以在 `1928-07-31～1930-04-16` 与 `1934-09-30～1936-06-08` 这两段里，
舰级文件按「已改装」给出的宽、吃水、燃油、续航、武备值，**对雾岛尚未生效**。

这一点已写进 `classes/kongo.yaml` 顶层的 `date_convention_note`，明示：
**逐舰真实节点以 `ships/<id>.yaml` 为准，主会话合并做逐舰时间轴时，
应以单舰文件的窗口覆盖舰级文件的窗口。**

未做逐条拆窗的原因：拆开会把 51 处同名日期改成逐舰一对，属结构性重写；
而按 SCHEMA §5「判据：这个值换一艘同级舰就变了吗？」，
这些值本身（宽 29.3 m、吃水 9.72 m、燃油 6,330 t 等）**同级不变**，
只是生效时刻不同 —— 生效时刻的差异本来就该由单舰文件表达。

---

## 6. 有争议的记载（两边原话并列，不裁决）

> SCHEMA §1.2：有争议的说法一条都不删，两边原话并列，不自己裁决。
> 以下 12 处全部在两边的数据文件里各留了一条 fact + note。

### 分歧 1：改装后的舰宽（29.3 m vs 31.02 m，差 1.7 m）

**A（navypedia）**
> Breadth, m | 28.0 | 29.3 | 29.3
> Bulges were fitted, **breadth rose to 29.3m**.

**B（日文来源，榛名/雾岛页）**
> 水線下幅 ① 28.04m ② **31.02m**
> 水線下幅 ① 28.04m ② 31.02m ③ **31.01m**（雾岛）

**判断**：可能不是同一测量位置（日文写「水線下幅」，英文 `Breadth` 通常指最大宽），
但两源都没给测量定义。**`dimensions.beam.wl` 取 29.3**，31.02 保留在 note 里。

### 分歧 2：第二次改装舰尾延长的幅度

**A（combinedfleet 榛名）**
> HARUNA's stern is lengthened by **7.47 m (24.5 ft)**.

**B（combinedfleet 雾岛）**
> Her stern is lengthened by **26-feet**.

→ 7.47 m vs 26 ft（≈7.92 m），差约 0.45 m。两舰是否真的延长了不同长度，
来源没说。全级全长 222.1 m（navypedia）不因此分歧（那是独立测量值）。

### 分歧 3：建成时主锅炉的型号名

**A（navypedia）**
> Kongo, Hiei, Kirishima: 4 Parsons steam turbines, **36 Yarrow boilers**
> Haruna: 4 Brown-Curtis steam turbines, **36 Yarrow boilers**

**B（日文来源）**
> 榛名/雾岛页：**ロ号艦本式ボイラー（混焼）**　36基
> 金刚页：**ヤーロー式ボイラー（混焼）** 36基

→ 座数 36 三源一致；**型号名只有金刚写 Yarrow**，另两舰日文来源写
ロ号艦本式（即艦本式，国产）。navypedia 对四舰一律写 Yarrow。
两说并列，`classes/kongo.yaml` 的 `propulsion.boiler.type` 取 navypedia 的 Yarrow
并在 note 里列出日文说法。

### 分歧 4：第一次改装后的最大航速

**A（navypedia，全级）**
> Max speed, kts | 27.5 | **25.9** | 30.5

**B（日文来源，逐舰）**
> 榛名 ② **25.9**ノット ／ 雾岛 ② **26.3**ノット ／ 金刚 ② **26.0**ノット

→ 榛名的 25.9 与 navypedia 一致；雾岛的 26.3、金刚的 26.0 与 navypedia 冲突。
**三舰值都不同，说明 navypedia 的 25.9 很可能只是抄了其中一艘**。
数据文件里：舰级文件留 navypedia 的 25.9（note 说明是「全级统一值，实际逐舰不同」），
雾岛单舰文件另记 26.3 并注明冲突。

### 分歧 5：中途岛出发日（05-27 vs 05-29）

**A（combinedfleet 榛名页）**
> **29 May 1942**: … HARUNA and KIRISHIMA depart Hashirajima for Midway …

**B（combinedfleet 雾岛页）**
> **27 May 1942**: … KIRISHIMA and HARUNA depart Hashirajima …

→ 同一事件、同一站、两页差两天。两说并列。
`ships/haruna.yaml` 记 05-29，`ships/kirishima.yaml` 记 05-27，各带各的 note。

### 分歧 6：榛名第二次改装后的轻型机炮到底是 40 mm 维克斯还是 13.2 mm

**A（navypedia）**
> Haruna: … 4 x 2 - 127/40 89-shiki, **4 x 2 - 13.2/76**, 1 catapult, 3 seaplanes (E7K2)
> 1936, Haruna: - 4 x 2 - 13.2/76; + 10 x 2 - 25/60 96-shiki

**B（combinedfleet + 日文来源）**
> combinedfleet：The 8 cm/40 3rd Year Type AA guns and 7.7 mm Type 92 machine guns are
> replaced by eight 12.7-cm/40 Type 89 AA guns (4x2) and **four 40-mm Vickers AA guns
> (2x2)**.（1932-05-22）… 第二次改装时 The **40-mm Vickers** AA guns are landed.
>
> 日文：40mm連装機銃　2基4挺　⇒のちいずれも撤去

→ 两源说的是两种不同口径的武器（40 mm vs 13.2 mm），
但都声称是榛名在那个时点的轻型机炮。**可能两者都装过（40 mm 1932 装、1936 撤；
13.2 mm 另一批）**，但没有来源直接说清先后。两说并列。
数据文件里 `armament.aa_40mm.count` 记 4 挺（1932-05-22～1934-09-30）→ 0（撤除后），
13.2 mm 无对应字段，只在 note 里保留 navypedia 的原话。

### 分歧 7：25 mm 增装的记账方式（榛名 1943-03）

**A（combinedfleet）**
> Two **25-mm triple mounts** are installed.（→ +2 座 = +6 挺）

**B（navypedia）**
> 3/1943, Haruna: … **+ 7 x 2 - 25/60 96-shiki**（→ +7 座双联 = +14 挺）

→ 差 8 挺。combinedfleet 的 26 挺（20+6）是按其记账算的；
若按 navypedia 则应为 34 挺。两说并列，`ships/haruna.yaml` 取 combinedfleet 的 26 并注明。

### 分歧 8：榛名的解体完成日

**A（combinedfleet）**
> **1946-1948**: The wreck of HARUNA is raised and broken up.

**B（日文来源）**
> 退役日（解体）**昭和21年/1946年7月4日**

→ 英方给两年区间，日方给具体日。可能日方指「浮扬完成日」、英方指「解体作业全程」。
两说并列，`construction.fate_date` 取沉没日 1945-07-28（无争议），
解体日只在 note 里并列。

### 分歧 9：榛名 15.2 cm 副炮的撤除节点

**A（navweaps 脚注）**
> **Haruna had six guns removed in March 1943.** Removed guns were replaced with
> 12.7 cm/40 Type 89 and 25 mm AA guns.

**B（combinedfleet）**
> Two secondary guns are landed.（1943-03～04）
> **Four secondary guns are landed.**（1943-12-16～1944-02-26）

→ A 说 1943-03 一次撤 6 门；B 说 1943-03 撤 2 门、1944 年初再撤 4 门（合计同样 6 门）。
**总数一致、节点不同。** 日文来源的 1944-10 终点状态（8 门）与 B 的记账吻合，
但本站**仍不裁决**，三说都记。

### 分歧 10：榛名 1945-07 两日空袭的命中数

**A（combinedfleet）**
> In the two days of attacks, HARUNA receives **13 bomb hits and 10 near misses**.
> 65 officers and men are lost.

**B（navypedia）**
> 24 and 28.7.1945 during American carrier aircraft raids of TF.38 to Kure she
> received **3 and 9 direct hits** respectively and sunk on shallow water.

→ A 记两日合计 13 发命中，B 记 3+9=12 发。差 1 发。
注：combinedfleet 另记 07-24 当天「HARUNA is hit by one bomb portside aft which
causes light damage.」——与 B 的 3 发也不完全吻合。
两说并列，`service.fate_category` 的 note 里两段原文都保留。

### 分歧 11：雾岛在第二次所罗门夜战中的命中数

**三说并存**，combinedfleet 注 [5] 自己列了出来：

**A（USSBS 战后分析）**
> USSBS postwar analysis based on interviews with almost hundred IJN officers
> suggests that KIRISHIMA received **nine 16-inch shell hits and forty 5-inch shell
> hits**.

**B（Adm. Lee 战报）**
> This is consistent with Admiral Lee's estimate of **eight 16-inch shell hits** as
> documented in his action report.

**C（Robert Lundgren 重析）**
> However, using a post-action sketch shown in an article written by LtCdr Ikeda
> Tsuruki (assistant gunnery officer of KIRISHIMA), naval researcher Robert Lundgren
> has completed an analysis suggesting that the real number might be **some 20 major
> caliber hits and seventeen smaller caliber hits**.

→ 本站**不采用任何单一数字**作事实。`ships/kirishima.yaml` 的 `service.fate_category`
note 里三说全录。雾岛自己打出去的弹数（117 发）三源无争议，已入库。

### 分歧 12：雾岛第一次改装后的锅炉构成

**A（日文来源引 [1-P88] 矢杉正一）**
> 重油専焼**10基**

**B（日文来源引 [5] 另一本书）**
> 重油専焼4基＋混焼6基

→ **同一个来源（日文页）自己就并列了两说**，脚注指向两本不同的书。
combinedfleet / navypedia 只说「10 Kampon boilers」不分混烧专烧。
两说并列，`ships/kirishima.yaml` 的 `propulsion.boiler.type` 的 value 就把两说都写进去。

---

## 7. 卡住的地方（未获取清单）

> 规则：查不到就写「未获取」，**不推算、不跨来源拼凑、不按姊妹舰类推、不凭记忆填**。
> 以下每一项都是「试过、确实没有」，不是「没查」。

### 7.1 榛名的试航实测数据（`propulsion.power.trial` / `speed.trial`）

**未获取，两条 fact 都没有写。**

日文来源榛名页的马力栏只有两个**设计值**：

> 馬　力　① 　64,000馬力[1-P88]　／　③ 　136,000馬力[1-P88]

**没有雾岛页那样的试航实测**（雾岛有 `公試全力で29.80ノット・136,940軸馬力、
過荷全力で30.08ノット・144,500軸馬力`，出处是一手试航记录）。

试过的地方：navypedia（只有 `Power, h. p. 136000`，设计值）、
combinedfleet 榛名 TROM（第一次改装记 `Her speed is increased to 30 knots`，
是定性描述不是实测）、navweaps（炮的数据，无舰的数据）。

**不得以雾岛的 136,940 / 29.80 / 30.08 代入。** 这是硬规矩第 2 条。

### 7.2 榛名二二号电探的装设日期（`sensors.radar.installed` 缺一条）

**未获取，该型不写 fact。**

combinedfleet 只在 1944-08 的改装里说 `existing Type 22 radars`（**已装**），
没给装设日期；日文来源给的是 1944-10-05 的**存在状态**（`2基`），也不是装设日。

已入库的只有两型（二一号 1943-03、一三号 1944-08），
二二号只在 `sensors.radar.count`（5 基）里体现存在。

### 7.3 雾岛的弹射器型号（`aviation.catapult.type`）

**未获取。**

combinedfleet 只写 `Aircraft handling deck is extended to accommodate a catapult`，
后面 1939-11-15 又写 `A new catapult is fitted (**probably earlier**)`
——作者自己标了不确定。navypedia 只写 `1 catapult`。

**不得以榛名的「吴式二号三型 / 二号五型」代入。**

### 7.4 装甲总重与水下防护纵深

**两个字段都未获取。**

- `protection.armor.weight`：所有来源都没给装甲总吨位。
- `protection.underwater.depth`：navypedia 只有
  `Underwater protection could resist exploding of 200kg TNT.`
  ——这是**抗爆当量**，不是纵深米数。**不能换算、不能填。**

### 7.5 排水量的另外两个口径

- `displacement.trial`（试验排水量）：**未获取**，四舰都没有倾斜试验记录。
- `displacement.deep` / `displacement.empty`：**未获取**。

navypedia 只有 standard / normal / full 三个口径，日文来源只有基準排水量一个。

### 7.6 吃水与排水量状态的对应关系

navypedia 给 `Draught, m 8.40 / 8.65 / 9.72`，但**没说明各值对应哪个排水量状态**。
而注册表 `dimensions.draught.mean` 的 note 明确要求「必须与排水量状态绑定，
否则不可比」。已按状态分三段记入，但每条的 note 都注明「来源未标明对应状态」。

### 7.7 改级令的日期

**未获取。** 没有找到「某年某月某日海军省令将金刚型由巡洋戦艦改为戦艦」
这类原文。故 `identity.ship_type` 只按**工程节点**（第二次改装完成日）切换，
并在 note 里说明这是工程节点而非编制命令。

### 7.8 战时编制（`service.complement.wartime`）

**未获取。** navypedia 只给三个时点的平时编制（1,221 / 1,118 / 1,437），
没有战时定员。日文来源无编制数据。

### 7.9 中途岛时的具体战时状态（任务书点名要查的一项）

**部分获取。** 已确认的：

- 编成：阿部弘毅少将支援部队，第三战队第二小队（榛名＋雾岛）
- 航空：榛名 1942-07-14 起为 3 架 E8N2（**中途岛当时**的机型，
  combinedfleet 只写 1942-06-04 当天 `HARUNA catapults a "Dave" floatplane`，
  Dave = E8N，可确认是九五式；但**具体几架没写**）
- 雾岛 1942-05-11 在佐世保入坞，把 No.7/8 号 25 mm 炮移位
- 两舰均未受损（只有近失弹）

**未确认的**：中途岛当时两舰的确切编制人数、燃油搭载量、弹药基数实载。
所有来源都没给。**没有推算。**

### 7.10 雾岛舰名由来（霧島山）

**没有原文。** 只有 `1 December 1913: Launched and named KIRISHIMA`。
「以霧島山命名」按金刚型统一的山名命名规则可推知，但**属推断**，
故只在 `identity.name_note` 的 note 里说明，不作为 value 单独立 fact。

（对比：榛名有明确原文 `after a volcano in Gumma Prefecture`。）

---

## 8. 一处主动驳回的流传说法

**「榛名 1917 年触雷受损」——本站不采用。**

combinedfleet 榛名 TROM 注 [1] 主动质疑此事：

> Some sources claim that in the summer of 1917, while on a training exercise in
> the South Pacific, HARUNA hit a mine and was damaged severely. She flooded, but
> managed to make port. The sources claim the mine was laid by Fregattenkapitän
> (later Kapitän z.S.) Karl A. Nerger's Imperial German Navy commerce
> raider/minelayer WOLF. Other sources say the mine was laid by raider BERLIN.
> **No photographic evidence of the damage, or any record of repairs is known to
> exist, which casts doubt on the veracity of this event.** In fact, Mr. Nakagawa
> Tsutomu, a well-known Japanese naval historian, states that **HARUNA never hit a
> mine at any time during her career.**

→ navypedia 也照抄了这个说法（`In 1917 Haruna received battle damages, having
stricken by a mine layd by German auxiliary cruiser Wolf.`），
**但 combinedfleet 给出了具体的反证逻辑**。本站按「无修理记录 + 无照片 +
当事国史家否认」，**不采信**，也不写进任何 fact。

同理，`_raw/` 里保留了两边的原文，供日后复核。

---

## 9. 原始文件清单

`work/staging/kongo/_raw/`：

| 文件 | 说明 |
|---|---|
| `navypedia-kongo.html` / `.txt` | navypedia 金刚级页 |
| `combinedfleet-haruna.html` / `.txt` | 榛名 TROM（Rev 22） |
| `combinedfleet-kirishima.html` / `.txt` | 雾岛 TROM（Rev 19） |
| `combinedfleet-kongo.html` / `.txt` | 金刚 TROM（Rev 22），旁证 |
| `combinedfleet-hiei.html` / `.txt` | 比叡 TROM，备用 |
| `jw-haruna.html` / `.txt` | 日文 榛名页 |
| `jw-kirishima.html` / `.txt` | 日文 雾岛页 |
| `jw-kongo.html` / `.txt` | 日文 金刚页，旁证 |
| `navweaps-36cm-45-t41.html` / `.txt` | 36 cm/45 四一式 |
| `navweaps-15cm-50-t41.html` / `.txt` | 15 cm/50 四一式 |
| `navweaps-127cm-89.html` / `.txt` | 12.7 cm/40 八九式 |
| `navweaps-25mm-96.html` / `.txt` | 25 mm/60 九六式 |
| `navweaps-13mm-76.html` / `.txt` | 13 mm/76 九三式（抓了未用） |
| `navweaps-40mm-hi.html` / `.txt` | 40 mm 九一式（抓了未用） |
| `fetch.py` / `fetch2.py` / `fetch_jw.py` | 抓取脚本（urllib + UA） |
| `find_links.py` / `probe.py` / `probe2.py` | 探测脚本（含 404 排查过程） |
| `parse_navypedia.py` / `parse_navypedia2.py` | 表格解析（含 colspan/rowspan 还原） |
| `selfcheck.py` | 自写校验（字段/单位/枚举/qual/src） |
| `run_validator.py` | 把分片合进临时 data 目录跑官方 `validate.py` |
| `_valdata/` | 上述临时合并目录（可删） |

---

## 10. 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/kongo.yaml`，132 fact） |
| 单舰文件 | 2（`ships/haruna.yaml` 69 fact、`ships/kirishima.yaml` 54 fact） |
| 切片文件 | 0（按任务书范围未做，边界数据已在 §4 备好） |
| 正文文件 | 0（同上） |
| 新登记来源 | 9 |
| 复用既有来源 | 2（`navweaps-127cm-89`、`navweaps-25mm-96`） |
| fact 合计 | 255 |

### 卡住的地方（详见 §7）

1. **榛名的试航实测马力/航速** —— 日文来源只给设计值，**不用雾岛值代入**。
2. **榛名二二号电探装设日期** —— 只有存在状态，无装设日，该型不写 fact。
3. **雾岛弹射器型号** —— 两源都没给，作者自己标 `(probably earlier)`。
4. **装甲总重、水下防护纵深** —— 抗爆当量不能当纵深。
5. **试验/空载/深载排水量** —— 三口径都缺。
6. **改级令日期** —— 只能用工程节点（改装完成日）替代。
7. **战时编制** —— 只有平时值。
8. **吃水对应的排水量状态** —— 来源未标明。

### 有争议的记载（详见 §6，12 处，全部并列不裁决）

1. 改装后舰宽 29.3 m vs 31.02 m
2. 舰尾延长 7.47 m vs 26 ft
3. 建成时锅炉 Yarrow vs ロ号艦本式
4. 一次改装后航速 25.9 / 26.0 / 26.3 kn
5. 中途岛出发日 05-27 vs 05-29
6. 榛名轻型机炮 40 mm 维克斯 vs 13.2 mm
7. 榛名 1943-03 的 25 mm 增装 +6 挺 vs +14 挺
8. 榛名解体日 1946-1948 vs 1946-07-04
9. 榛名副炮撤除 一次 6 门 vs 2+4 门
10. 榛名 1945-07 命中 13 发 vs 3+9 发
11. 雾岛被弹数 9+40 / 8 / 20+17 三说
12. 雾岛一次改装锅炉 专烧 10 基 vs 专烧 4+混烧 6
