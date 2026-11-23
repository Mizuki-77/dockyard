# 中途岛参战序列核实（§14.2 清单逐条对账）

> 2026-11-23 · 交接报告 §14.6 要求的「开工第一件事」
> 状态：**核实完成** · 未改动任何 `data/` 文件

---

## 0. 一句话

**交接报告 §14.2 那份 21 艘的清单，有 4 条站不住：3 条完全不在中途岛参战序列，1 条（隼鹰）跨到了阿留申。**
其余 17 条成立，但**编队归属有 6 条写错**。下表逐条给出判定与原文。

---

## 1. 来源与方法

| 项 | 内容 |
|---|---|
| 主来源 | NavWeaps《Orders of Battle - Battle of Midway and Aleutians》<https://www.navweaps.com/index_oob/OOB_WWII_Pacific/OOB_WWII_Midway.php> |
| 交叉源 | HyperWar《Battle of Midway: 4-7 June 1942 — US Order of Battle》<https://www.ibiblio.org/hyperwar/PTO/TideTurns/Midway/Midway-OOB.html> |
| 佐证源 | microWorks《Japanese OOB at Midway》<http://www.microworks.net/pacific/orders_of_battle/midway_japan.htm> |
| 本地留档 | `work/raw/navweaps-midway-oob.html` / `.txt`、`work/raw/hyperwar-midway-oob.html` / `.txt`、`work/raw/microworks-midway-japan.html` |
| 方法 | 抓全文 → 按「Midway / Aleutians」分段 → 逐舰名对账，**不靠记忆** |

**关键前提**：NavWeaps 这一页**同时收录中途岛与阿留申两场作战**（`Aleutians Force` 起始于原文第 15159 字符处）。
不做分段就搜舰名，会把阿留申的舰误判成中途岛的。檀香山号就是这么错的。

---

## 2. 判定总表（21 条）

### 2.1 日本侧 8 条

| 交接报告的说法 | 判定 | 实际归属（来源原文） |
|---|---|---|
| 榛名 · 金刚级 · 护航战列舰（第 3 战队） | ✅ 在场，编队名不准 | **第 3 战队第 2 小队**（`Battle Division 3, Section 2`），属**机动部队支援部队**（`Support Group`, RA Abe Hiroaki），不是笼统的「护航」 |
| 雾岛 · 金刚级 | ✅ 在场 | 同上，与榛名同小队。原文并列 `BC Haruna` / `BC Kirishima` |
| 利根 · 利根级重巡 | ✅ 在场 | **第 8 巡洋舰战队旗舰**（`CA Tone (flagship)`），属机动部队支援部队。**发现美航母的是利根 4 号机**——这条战功成立 |
| 筑摩 · 利根级 | ✅ 在场 | `CA Chikuma`，与利根同战队 |
| 长良 · 长良级轻巡 | ✅ 在场 | **第 10 水雷战队旗舰**（`CL Nagara (flagship)`），属机动部队本队。报告写的「第 10 水雷战队旗舰」正确 |
| 川内 · 川内级轻巡 | ❌ **编队错** | 在场，但**不在机动部队**。原文：`Destroyer Squadron 3 / CL Sendai (flagship)`，属**主力部队（Main Body，山本亲率）**的水雷战队旗舰，伴随中途岛攻略部队护航。报告把它写成「护卫队旗舰」含混，实际是 **DesRon 3 旗舰** |
| 凤翔 · 凤翔级轻母 | ✅ 在场 | `CVL Hosho`，属**主力部队（Main Body）的 Carrier Group**，载 8 架九六式舰攻（`8 x Type 96 B4Y1`） |
| 隼鹰 · 隼鹰级 | ❌ **不在中途岛** | 原文归在 `Aleutians Force → 2nd Carrier Striking Force → Carrier Division 4`（RA Kakuta Kakuji），与**龙骧**同队。**参加的是阿留申作战（AL）**，报告 §14.4 提醒的正是这条 —— 确认成立 |

### 2.2 美国侧 13 条

| 交接报告的说法 | 判定 | 实际归属（来源原文） |
|---|---|---|
| 波特兰 · 波特兰级重巡 · 第 6 巡洋舰队，护卫约克城 | ⚠️ **编队错** | 在场。`USS Portland (CA-33)` 属 **TG 17.2**（RA William W. Smith），是 **TF 17 的巡洋舰群**——「第 6 巡洋舰队」是错的，那是 TF 16 的 CruDiv 6 |
| 亚特兰大 · 亚特兰大级轻巡 · 防空巡洋舰 | ✅ 在场 | `USS Atlanta (CL-51)` 属 **TG 16.2**（RA Kinkaid，ComCruDiv 6），原文 `Escorting Hornet.` **1942-06 已服役，报告点名的疑问解除** |
| 明尼阿波利斯 · 新奥尔良级 | ⚠️ 编队表述不准 | 在场。`Escorting Hornet.`，属 TG 16.2 / CruDiv 6 |
| 北安普敦 · 北安普敦级 · 「第 6 巡洋舰队旗舰」 | ✅ 在场，❌ **旗舰说法错** | `USS Northampton (CA-26)`，原文 `Escorting Enterprise.`。**TG 16.2 的旗舰是明尼阿波利斯**（RA Kinkaid 坐舰），不是北安普敦 |
| 彭萨科拉 · 彭萨科拉级 | ✅ 在场 | `Escorting Enterprise; joined TF-17.` |
| 新奥尔良 · 新奥尔良级 | ✅ 在场 | `Escorting Hornet.` |
| 文森斯 · 新奥尔良级 · 护卫约克城 | ⚠️ **护卫对象错** | 在场，但原文 `Escorting Enterprise; joined TF-17.` —— **护的是企业号**，不是约克城 |
| 阿斯托里亚 · 新奥尔良级 · 护卫约克城 | ✅ 基本正确 | `USS Astoria (CA-34) (flagship)`，**TG 17.2 旗舰**，随 TF 17 |
| 檀香山 · 布鲁克林级 · 第 6 巡洋舰队 | ❌ **不在中途岛** | 分段核实：`USS Honolulu (CL-48)` 出现在 **Aleutians → Task Force 8** 段，**属阿留申作战**。中途岛段全文无此舰 |
| 盐湖城 · 彭萨科拉级 · 「护卫企业号」 | ❌ **两个来源都查无** | NavWeaps 与 HyperWar 的中途岛美军序列**都没有 Salt Lake City**。两个来源一致缺，不能凭记忆补。**判定：不在中途岛参战序列**（原报告 §14.6 自己也在怀疑，怀疑成立） |
| 哈曼 · 驱逐舰 · 「沉没时唯一在场的驱逐舰」 | ✅ 在场，❌ **说法要改** | `USS Hammann (DD-412) (sunk)`，属 **TG 17.4 DesRon 2**。**「唯一在场的驱逐舰」这句无法用序列来源证实**：序列只证明它的编成归属，不证明 06-06 沉没瞬间的海面态势。要写这句必须另找 06-06 当日的战斗详报/行动报告。**待补源**（HyperWar 另列 `USS Vireo (ATO-144)`，但归在 Pearl and Hermes Reef 巡逻段，与本舰沉没的直接关联尚未证实，不要当成定论） |
| 莫纳汉 · 法拉格特级 · 待核实 | ✅ 在场 | `USS Monaghan (DD-354)`，`Escorting Enterprise.`，**DesRon 1**。属**法拉格特级**（DD-354 正确） |
| 本汉 · 本汉级 · 待核实 | ✅ 在场 | `USS Benham (DD-397)`，`Escorting Enterprise; joined TF-17.`，**DesRon 6**。属**本汉级**首舰（DD-397 正确） |

---

## 3. 交接报告 §14.6 点名的四问，逐条回答

| # | 问题 | 结论 | 依据 |
|---|---|---|---|
| 1 | 隼鹰参加的是中途岛还是阿留申？ | **阿留申（AL）** | NavWeaps 把它列在 `Aleutians Force → CarDiv 4`，与龙骧同队 |
| 2 | 莫纳汉、本汉是否真在中途岛序列里？ | **都在** | NavWeaps 与 HyperWar 双源均列，DD-354 / DD-397 |
| 3 | 盐湖城是否护卫企业号？ | **不在中途岛序列**，两个来源都查无 | NavWeaps + HyperWar 均无 Salt Lake City |
| 4 | 亚特兰大号 1942-06 是否已服役？ | **已服役，在场** | `USS Atlanta (CL-51)`，`Escorting Hornet.` |

---

## 4. 另一处需要改的结构问题

**交接报告 §14.2 把「第 6 巡洋舰队」当成了中途岛美军巡洋舰的统一归属，这是错的。**
实际上中途岛美军巡洋舰分属两个任务群，不能合并叙述：

| 任务群 | 指挥官 | 巡洋舰 | 隶属 |
|---|---|---|---|
| **TG 17.2** | RA William W. Smith | 阿斯托里亚（旗舰）、波特兰 | TF 17（弗莱彻） |
| **TG 16.2** | RA Thomas C. Kinkaid（ComCruDiv 6） | 明尼阿波利斯（旗舰）、新奥尔良、文森斯、北安普敦、彭萨科拉、亚特兰大 | TF 16（斯普鲁恩斯） |

这也印证了 `docs/32` §4 第 93 行那条已记录的纠正：「七艘重巡装的是 5"/25，只有亚特兰大装 5"/38」。

---

## 5. 修正后的清单（可直接用于开工）

### 5.1 日本侧建议收录（6 艘，去掉隼鹰、川内编队改述）

| 舰 | 级 | 编队 | 价值 |
|---|---|---|---|
| 利根 | 利根级（建级） | 机动部队支援部队 CruDiv 8 旗舰 | **发现美航母编队**，核心战功 |
| 筑摩 | 利根级 | 同上 | 与利根成对，建级后复用 |
| 榛名 | 金刚级（建级） | 机动部队 战列3战队2小队 | 战列舰字段与航母差异大 |
| 雾岛 | 金刚级 | 同上 | 同批复用 |
| 长良 | 长良级（建级） | 机动部队 DesRon 10 旗舰 | 水雷战队视角 |
| 凤翔 | 凤翔级（建级） | 主力部队 Carrier Group | 唯一随主力的轻母，8 架九六舰攻 |

> 川内号仍可收，但**必须写成「主力部队 DesRon 3 旗舰」**，不能算进机动部队。

### 5.2 美国侧建议收录（按任务群分两批）

**批 A · TG 17.2（小，2 艘）**：阿斯托里亚（旗舰）、波特兰
**批 B · TG 16.2（大，6 艘）**：明尼阿波利斯（旗舰）、新奥尔良、文森斯、北安普敦、彭萨科拉、亚特兰大
**批 C · 驱逐舰（3 艘）**：哈曼（沉没）、莫纳汉、本汉

**剔除**：盐湖城（不在序列）、檀香山（属阿留申）

> 建级复用红利：新奥尔良级一次吃 3 艘（新奥尔良 / 文森斯 / 阿斯托里亚），是本轮最大省力点。

---

## 6. 未做的事（诚实标注）

- 本文件**只做序列核实**，没有查这 14 艘的技术数据
- 各舰的 fact 数量、字段缺口、图片可行性**均未评估**
- 日方一手来源（JACAR）未查，本轮的 tier 判断（NavWeaps = C 级、HyperWar = B 级转录）**需要用 `sources.yaml` 现有惯例再对齐一次**
- 阿留申作战本身要不要单独建 `operation`，未决策
- **哈曼「唯一在场的驱逐舰」这句未证实**：序列来源只证明编成，不证明 06-06 沉没瞬间的海面态势。要保留这句话必须补 06-06 行动报告。同理，`Vireo` 与约克城拖带的关联也未证实
