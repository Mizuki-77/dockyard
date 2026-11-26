# 遗留三条的处置：Mk12/15 合并 + 20cm No.1 补图（2026-11-26）

> 状态：**待最终验收**（构建进行中）
> 来源：`项目交接-Dockyard-完整报告-2026-11-26.md` §10.1 的三条遗留

---

## 0. 一句话

交接报告列的三条遗留，按用户决定分别处理：**① Mk 12 / Mk 15 合并为一个实体**、
**② 做不成的武器图放弃**、**③ 20cm No.1 补图**。
其中 ① 顺带修掉了一个此前隐藏的渲染缺陷（同值字段重复渲染），
③ 找到并使用了 Commons 上唯一能直接看到 No.1 炮廓炮的画面。

---

## 1. ① `8in-55-mk12` 并入 `8in-55-mk15`

### 1.1 为什么这个方向

两个实体原本各自成页，但：

- navweaps **把两型写在同一个页面**（`WNUS_8-55_mk12.php`），
  标题就是「USA 8"/55 (20.3 cm) Marks 12 and 15」；
- 炮身重量那一栏**两型不分**，来源没有分别给值；
- `8in-55-mk12` 那半页**永远没有正文**（交接 §10.1 第 1 条），
  因为它引用的来源本来就与 mk15 同一份。

所以合并方向取「并进 mk15」而不是反过来：
**URL `/weapons/8in-55-mk15` 不变，不产生死链**，而被并掉的
`/weapons/8in-55-mk12` 本来就是个只有参数、没有正文的空壳页。

### 1.2 改了什么

| 文件 | 改动 |
|---|---|
| `data/classes/new-orleans.yaml` | 11 条 fact 的 `about: weapon:8in-55-mk12` → `weapon:8in-55-mk15` |
| `data/weapon-articles/8in-55-mk15.yaml` | 文件头注释说明合并；`updated` 改 2026-11-26；intro lead 重写为「两型并列」；新增一段「同族两根炮管」讲清差异 |
| `src/lib/data.ts` | `getShipEntities()` 补「同值去重」 |

**没有动的**：`sources.yaml` 里的来源条目 `navweaps-8in-55-mk12` 保留原名 ——
它指的是 navweaps 那个 URL，URL 本身就叫 mk12，改名会与来源实际标题不符。
fact 里引用它是对的。

### 1.3 两型的差异写在哪（不能当成一门炮）

合并成**一个实体**不等于当成**一门炮**。正文新增的段落逐条分写：

| 项 | Mk 12 | Mk 15 |
|---|---|---|
| 药室 | 与 Mk 15 不同 | 4,860 in³（79.6 dm³） |
| 膛线缠度 | 等齐右旋 1:35 | 1:25（同 Mk 14） |
| 装舰 | Tuscaloosa 子级 CA-37/38/39/44、Wichita CA-45、Baltimore CA-68 | 巴尔的摩级其余、俄勒冈城级 CA-122 |
| 炮身重 | 17.11–17.17 t（两型同栏，来源未分给） | 同左 |
| 炮管寿命 | 715 发 | 715 发 |

### 1.4 顺带修的渲染缺陷

`getShipEntities()` 的文档写着「单舰层命中即覆盖舰级层，不与舰级值构成分歧」，
但实现只在 **weapon id** 层面做了 `Map.set`，**字段层面没有**。
合并后同一个 id 在舰级与单舰两层都有 fact，于是：

- `weapon.bore` / `nation` / `category` / `caliber_length` / `weight` / `rate_of_fire`
  六个字段在明尼阿波利斯页会渲染成「203 mm / 203 mm」这种同一件事写两遍的样子。

第一版修法写成「舰级一律让位给单舰」，跑完全量对账后**立刻发现它是错的**：

> `ark-royal` 的 2pdr 八联装：舰级记 `mount.count = 4`（1938-11-16 起），
> 单舰记 `mount.count = 6`（1941-05-01 起）—— 这是**时序演进**，
> 不是分歧，更不是重复。按框架 §3.2 规则 3「命中多条时间窗 ≠ 分歧」，两条都必须留。

改成**只去重值完全相同**的条目。全量影响面实测：

| 类型 | 条数 |
|---|---|
| 值相同、被去重（应去） | 6（全部在 minneapolis 的 8in-55-mk15） |
| 值不同、被保留（应留） | 3（minneapolis 型号 + ark-royal 两条） |

---

## 2. ③ `20cm-3ns`（No.1）补图

### 2.1 素材现实

Commons 上**不存在**赤城/加贺炮廓的近景特写，也没有
`Category:Casemates of Akagi` 之类子分类。检索覆盖：

| 分类 | 文件数 |
|---|---|
| `Category:20 cm/50 3rd Year Type naval gun` | 20 |
| `Category:Akagi (ship, 1927)` | 48 + 2 子类 |
| `Category:Kaga (ship, 1928)` | 34 + 2 子类 |
| `Category:Akagi (three flight decks)` | 10 |
| `Category:Kaga (three flight decks)` | 9 |
| `Category:Short Barrel 20 cm naval gun` | 8（岸炮，无关） |

逐个核证 metadata 约 50 个。`Category:20 cm/50 3rd Year Type naval gun` 里的 20 个文件
**绝大多数是 No.2（Mark II，203.2 mm）**，必须排除。

### 2.2 最终采用

**`File:Japanese Navy Aircraft Carrier Kaga 1928.jpg`**，从全舰照裁出炮廓段。

- 官方图注原文：`Japanese Navy Aircraft Carrier Kaga being fitted out in 1928. Note the long funnel below the flight deck and **the three 8-inch guns in casemates**`
- 许可 `Public domain`（PD-1996 / PD-Japan-oldphoto）→ **A 档，可下载**
- 原图 3510×2376；裁出区 (1386, 1259, 2421, 1841) → **落盘 1035×582**
- 出处：広島県呉市海事歴史科学館所蔵品
- 落盘 `/img/weapons/20cm-3ns-kaga-casemate.jpg`，141,394 字节，文件头 `FFD8`

**为什么判它合格**：主体判定的两条硬依据都过 ——
原始文件名含本舰（Kaga），描述里第一个出现的舰名也是本舰，
且描述**直接点名 casemate 与 8-inch guns**，不是我从外形猜的。

**人眼复核结果**（本站规矩，自动筛选不可信）：裁剪段内**三门炮廓炮并排可见**，
炮身朝左伸出，炮廓开口与舰体线条清楚。裁切为原生像素，**未放大、未调色**。

### 2.3 明确排除的

| 文件 | 排除依据 |
|---|---|
| `203-mm turret on Takao.jpg` | 高雄级 Type E，Mark II（No.2） |
| `Haguro-1942.jpg` | 1942，已换 Mark II |
| `NH 73026/73027 MAYA` | 摩耶 Type E 55°，Mark II |
| `Main battery of Kako.jpg` | 明确 E2 + 1937 后改装，Mark II |
| `Akagi AA gun position.jpg` | **12cm 高炮，与本炮无关**（搜 `Akagi gun` 时排第一，极易误取） |
| `Akagi 1929.jpg` | Type B 炮塔确装 No.1 炮身，但 496×965 太小、且是炮塔非炮廓，未采用 |
| `Myoko 1931.jpg` | 1931 卡在换装窗口，无法确证仍是 No.1，未采用 |

---

## 3. ② 其余武器图：不做

用户决定「不好做的就算了」。本轮只补了 `20cm-3ns` 这一张。
`audit_data` 的武器无图数从 **9 降到 7**：

`13mm-76-t93` `14cm-50-3ns` `21in-mk15` `36cm-45-t41` `45in-45-mk1` `8in-55-mk15` `8in-55-mk9`

沿用 `docs/52` §3.3、`docs/53` §3.3、`docs/54` 的结论：这些的候选图
**都曾被抓到并被人眼否决**，属于 Commons 素材上限，不是遗漏。宁缺不放。

---

## 4. 验收

| 检查 | 结果 |
|---|---|
| `validate.py` | 0 错误 / 0 警告 |
| `selftest.py` | 32 例全过 |
| `astro check` | 41 文件 0/0/0 |
| `audit_data.py` | 0 硬问题 / 0 切片问题 / 0 孤儿 |
| 武器实体 | 89 → **88** |
| 无正文的武器 | 1 → **0** |
| 武器无图 | 9 → **7** |
| 页面数 | 199 → **198**（少掉被合并的那一页） |
| 全站残留 `/weapons/8in-55-mk12` 链接 | **0** |
