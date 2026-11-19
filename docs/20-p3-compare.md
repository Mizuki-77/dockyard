# P3 对比器 · 开工方案

> 2026-11-18 起 · 基于对 `data/` 的实测（`work/p3_facts.py`、`work/p3_matrix.py`、`work/p3_bore2.py`）
> 状态：**P3 全部完成并验收**（阶段 0–3）。`validate` 0/0、`selftest` 32 例全过、`build` 72 页。

---

## P3 完工记录（2026-11-19 12:54）

### 交付物

| 项 | 结果 |
|---|---|
| 对比器页面 | **`/compare`**，顶栏已加「对比器」入口 |
| 索引 | `buildCompareIndex()` 在 `src/lib/data.ts`，预生成 **50.0 KB** 内联 JSON |
| 可比较字段 | **33 个**（41 个 `compare:true` 里剔掉武器/炮位层与 string/table 类型） |
| 覆盖 | 5 舰 × 33 字段，共 **139 个时间窗** |
| 校验 | `validate` 0 错误 0 警告；`selftest` **32 例**（原 29 + 3 个 comparable 用例） |
| 构建 | 72 页 |

### 实测验证过的行为（用浏览器自检页跑的，不是靠看截图猜）

| 行为 | 结果 |
|---|---|
| 每舰独立滑块 | ✅ 拖提尔皮茨 → 2 cm 高炮 **12 → 32 → 78** 三档正确 |
| 同步到同一时刻 | ✅ 拖俾斯麦到 1940-08，两舰锁到共同交集 **1941-02-25** |
| 无交集时 | ✅ 表头插入黄条警告「这两艘舰没有同时在世的时段」，不假装同步成功 |
| 三态格 | ✅ 有值 38 / 未记载 2 / 已沉没斜纹 0（该时刻两舰都在世） |
| 最值高亮 | ✅ 只在 better=higher/lower + 双方真数值 + 无 incomparable 时才标 |
| 口径存疑 | ✅ 光辉级全长 229.6 m 显示为斜体 + 「口径存疑」，不参与高低 |
| 分歧展开 | ✅ 「另有 N 说」可点开，42,900 t / 253.6 m 等落选说法都在 |
| 移动端 390 | ✅ `documentElement.scrollWidth=375 < 390`，表格内部滚动 `352>339` |

### 四个踩过的坑（都会静默出错，值得记）

1. **Astro scoped CSS 打不到 JS 动态生成的节点。**
   `tbody` / `thead` 的 HTML 全是脚本用 `innerHTML` 拼的，那些节点上没有
   `data-astro-cid-xxx`，普通 `.cmp-td { }` 一条都命中不了。
   症状极其迷惑：**class 明明加上了（能 dump 到 `class="cmp-td is-best"`），
   但样式就是不生效**。凡是动态生成的 DOM，样式必须写 `:global()`。

2. **`innerHTML = ` 会清掉之前 `appendChild` 的节点。**
   初版边拼边 `appendChild`，最后又来一句 `tbody.innerHTML = rows.join('')`，
   结果数据行全没了、只剩分组标题。

3. **索引阶段不能照抄「单舰有值就只用单舰层」。**
   `buildTimelinePayload` 那条规则是给「整条生命只取一个主值」的；
   按时刻查询必须**全量带上**，让浏览器按 t 过滤。
   反例：KGV 的搭载机数单舰层只有 1944 年起的 0，若索引阶段就把舰级那条
   「2 架水上飞机（1940 起）」丢掉，拖回 1942 年这格会变成空的。

4. **命中多条时间窗 ≠ 分歧。**
   提尔皮茨编制 1941 起 2,065、1943 起 2,608，两条都 open-ended，
   1943 年后**两条都命中**。那是时序演进，主值取新的（2,608）；
   标「多种说法」等于把演进讲成争议。真分歧只看同一 `(from,to)` 窗内的多值，
   这个标记在建索引时就算好（`disputed`）。

### 默认显示哪些字段（一个刻意的设计选择）

不只看「两舰都有值」，而是**两类的并集**：

- 两舰都有值的（能横向比的）
- **任一被选舰上随时间变化的**（拖时间轴有反应的）

只留前者会让时间轴变装饰：现收录 5 舰的长/宽/排水量一辈子一个值，
真正会变的（提尔皮茨 20 mm 炮 32→78、雷达换型、涂装、编制）
恰恰多半只有一舰有值。

---



---

## 0. 一句话

**构建期把「5 舰 × 37 个 `compare: true` 字段」预生成一份约 39 KB 的 JSON，页面里用现成的 `src/lib/resolve.ts` 在浏览器算主值。不新增后端、不新增依赖、不新增构建步骤。**

`docs/00-framework.md §3.4` 早就把这件事定义完了：

> 对比器 = 取两艘舰、遍历 `compare: true` 的字段、各自解析主值、表格渲染。**不需要为每对舰艇写任何定制代码。**

注册表、继承覆盖、主值规则、分歧判据，四项地基全部到位。缺的只有索引和页面。

---

## 1. 数据现在到底够不够（实测）

`fields.yaml` 196 个字段里 **45 个 `compare: true`**：

| 层 | 个数 | 说明 |
|---|---|---|
| 舰体层（class / ship） | **37** | 对比器的主体 |
| 武器/炮位层 | 8 | `weapon.bore` / `muzzle_velocity` / `range.max` / `range.aa_max` / `rate_of_fire` / `barrel_life` / `ammo_outfit` / `mount.count` |

37 个舰体字段的五舰覆盖情况：

| 覆盖 | 字段数 | 代表字段 |
|---|---|---|
| 5/5 齐 | **13** | `displacement.standard`、`dimensions.length.oa`、`propulsion.speed.design`、`propulsion.power.design`、`service.complement.standard`、`protection.underwater.depth` … |
| 1–4/5 | **19** | `displacement.full`(4)、`propulsion.range.max`(3)、`armament.broadside_weight`(2) … |
| 0/5 | **5** | `armament.mine.capacity`、`aviation.fuel.capacity`、`displacement.standard_metric`、`propulsion.speed.cruise`、`propulsion.turning_diameter` |

**结论：够开。** 有 13 个字段能立刻做出满格对比表，这是能上线的量。

---

## 2. 三个决定架构的坑（都是实测发现的）

### 2.1 时刻对齐的坑：为什么不能用「一条全场时间轴」

五舰同时在世的交集：

```
bismarck       1940-08-24 .. 1941-05-27
hood           1920-03-29 .. 1941-05-24
illustrious    1940-05-25 .. 1956-11-01
king-george-v  1940-10-01 .. 1958-01-01
tirpitz        1941-02-25 .. 1944-11-12
→ 交集 = 1941-02-25 .. 1941-05-24，只有 3 个月
```

如果强行要求「所有舰对齐同一个时刻」，任意两舰组合大概率落在交集外，表格全灰。

**但时间轴仍然可以是主角——只要它是每舰一条，不是全场一条。**

（2026-11-18 用户拍板：时间轴非常重要，不接受把它降级成可选开关。原方案 §2.1 已按此改写。）

### 2.1.1 主值模式是什么（用大白话说清楚）

同一项指标，本站常有**好几条记录、写着不同数字**。举例，胡德号的标准排水量：

| 来源 | 值 | 它自己怎么说的 |
|---|---|---|
| navypedia | 42,670 t | 记的是 "normal" |
| 专题站 Light 口径 | 42,037 t | 1931 年 Light 状态 |

两条都留着。那么页面上默认先给你看哪个？这就叫**主值**。选定规则写死在 `docs/00-framework.md §3.9`：

```
1. 来源等级高（A>B>C>D>E）先
2. 同等级，口径说明清楚的先
3. 同等级同口径，采集时间新的先
4. 还平，按 source id 字母序（保证每次构建结果一样）
```

**关键：主值不是「正确答案」，只是「默认先给你看哪个」。** 其余说法一条不删，点开就能看。

所以：

- **「主值模式」**（我上一轮推荐的）= 不定时刻，每艘船直接拿它全生命里的默认值摆一张表。问题是很平，时间轴没戏份。
- **「时间模式」** = 拖到某一时刻，看那一刻每艘船的状态。这才是这个站真正值钱的地方。

### 2.1.2 改后的设计：每舰独立时间轴

一条全局时间轴 = 被 3 个月交集卡死。**改成每艘舰各自一条滑块**，可以拖到不同年份：

```
俾斯麦   [——————●————]  1941-05（出击前）
提尔皮茨 [——————————●]  1944-11（沉没前）
```

这样能比的正是读者真正想问的：**「俾斯麦 1941 年出击时的状态 vs 提尔皮茨 1944 年挨炸前的状态」**——两船从没在同一时刻处于战备状态，全局时间轴永远做不到这个对比。

上面再加一个**「同步到同一时刻」**按钮：按下后所有滑块锁到同一个 T，此时交集外的舰显示「已沉没 / 未服役」，而不是留空。

| 元素 | 位置 | 说明 |
|---|---|---|
| 每舰滑块 | 表格表头下方 | 主交互，首屏就有 |
| 时刻标签 | 滑块右端 | 显示 `1941-05-18`，并标该舰当下所处的切片代号（S3 等） |
| 同步按钮 | 工具栏 | 锁同一 T；可再解锁 |
| 无数据态 | 格子内 | 分三态：**未记载**（灰）/ **已沉没/未服役**（斜纹）/ **口径存疑**（斜体+角标） |

首屏**默认就落在时间模式的某一点**（取该舰服役期的中点），不做「主值表」。主值表降级为「不选时刻」时才出现的兜底视图。

### 2.2 口径不可比是真实存在的，而且已经写在 note 里了

| 舰 | 字段 | 值 | note 自述 |
|---|---|---|---|
| hood | `displacement.standard` | 42670 | navypedia 记「normal 42,670 t」……**normal 本身不是标准排水量** |
| hood | `dimensions.beam.wl` | 28.9 | 原值约 95 ft，最大 31.7 / 舷宽 32.0 / **水线 28.9，口径不同** |
| king-george-v | `aviation.aircraft.capacity` | 2 | navypedia 记 2 架 **seaplanes** |
| illustrious | `aviation.aircraft.capacity` | 33 | 舰载机 |
| tirpitz | `aviation.aircraft.capacity` | 6 | 「4 架在库 + 2 架停甲板」 |

**如果对比器只按 `better: higher` 着色，它会当场把整站最值钱的东西——「来源自证口径」——变成假象。** Hood 的 42,670 t 会被排成"最轻的战列舰"，而它其实不是标准排水量。

对比器必须做每格三态：**有值 / 未记载 / 口径存疑**。第三态不做高低判定，只显示值 + 「口径存疑」标记 + note 原文。

### 2.3 武器层不能复用舰体层

`buildTimelinePayload()` 里有一行 `if (about) continue;`——武器和炮位实体被有意排除在主时间轴表外，因为它们按 `about: weapon:<id>` 挂在别的实体上。

48 型炮的横向对比（`weapon.bore` / `rate_of_fire` / `muzzle_velocity`）是**另一套索引**，要走 `getWeaponIndex()` 那条路，不是舰体那套。**建议 P3 只做舰体对比，武器对比留 P3.1。** 一次做两套会把工期翻倍而没有增量价值。

#### 2.3.1 口径单位（2026-11-18 已定）

实测 17 条 `weapon.bore`，**全部存 mm，全部 `unit: mm`**，且 `fields.yaml` 里该字段的 `unit` 就写死是 `mm`：

```
38cm-sk-c34      380 mm        14in-45-mk7     356 mm
15cm-sk-c28      150 mm        15in-42-mk1     381 mm
10_5cm-sk-c33    105 mm        4_5in-qf-mk3    114 mm
525in-50-mk1     133 mm        g7a-t1          533 mm
```

**存储层保持 mm，不改。** 理由：`rejected_units` 里明确拒收 `in`（要求换算成 cm/mm），注册表是全站单位口径的唯一权威，一动就要动校验器和全部既有 fact。

**但显示层要按习惯改**——这是用户提的点，且是对的：

| 场景 | 显示 | 理由 |
|---|---|---|
| 德/英舰炮 | **380 mm（"38 cm SK C/34"）** | mm 为准，括号里给型号本名。德制型号自带 cm，英制自带 inch，两个习惯都保留 |
| 排序 / 着色 | 一律按 mm 数值 | 380 与 381 差 1 mm，视觉上几乎无差，但 Hood 的 15 in 确实略大 |
| 小口径高炮 | **20 / 37 / 40 mm** | 这几个本来就只说 mm，没人说 2 cm |

对比表里**不能只写「38 cm」**——那样 38 与 37（mm 高炮）会被读成同一量级；也不能只写 380 而不给型号缩写，读者对不上自己记的名字。两个都给。

---

## 3. 分阶段

### 阶段 0 · 拧紧数据闸门（半天）

1. **处理 5 个 0 覆盖的 `compare: true` 字段**：要么补数据，要么改 `compare: false` 并在注册表 note 里写「暂无数据，暂不参与对比」。留着 = 注册表和现实脱节。
2. **`validate.py` 加一条检查**：`compare: true` 但全库 0 条 fact → `warn`。防止下一个人再往注册表里加空气字段。
3. **给命中的 6 条口径存疑 fact 加 `comparable: false`**（见 §2.2）。

### 阶段 1 · 索引（半天～1 天）

`src/lib/data.ts` 新增 `buildCompareIndex()`，输出：

```ts
{
  ships:  [{ id, name, classId, span: [from, to] }],           // span 用构造/沉没日期
  fields: [{ id, label, unit, group, better }],                 // 只含 compare:true 且舰体层
  deps:   { tier: { srcId: 4 }, fetched: { srcId: '2026-11-12' } },  // ★ 非显然项
  cells:  { bismarck: { 'displacement.standard': [ { from, to, value, conf, src, note, origin } ] } }
}
```

**`deps` 必须序列化进 payload。** `pickPrimary()` 在浏览器侧重算主值时需要 `tierOf` 和 `fetchedOf` 两个函数，而现在的 `deps`（`data.ts:159`）是构建期对象，直接引用 `getSources()`，浏览器里没有。漏了这一步，浏览器会退化成"取第一条"，主值规则当场失效。

实测体积：**38.9 KB**（含 note 截断到 120 字符）。可以整页内联，跟 `ships/[id].astro:421` 的 `<script define:vars={{ payload }}>` 同一个路子，不必额外开 `public/*.json`。

### 阶段 2 · 页面（1.5～2.5 天）

新页 `/compare`，形态：

- 顶部两个舰选择器（5 舰，带缩略图）
- **每舰一条独立滑块**（§2.1.2）；工具栏有「同步到同一时刻」按钮
- 表格按 `fields.yaml` 的 `group.order` 分组（尺寸与排水 → 动力 → 装甲防护 → 武备 → 航空 → 服役）
- 每格三态：值 / 「未记载」（灰）/ 「已沉没·未服役」（斜纹）/ 「口径存疑」（斜体 + 角标）
- `better: higher|lower` 且有值且口径不存疑 → 差值着色；`better: context|none` → 不着色
- 字段随期变化（如 tirpitz `armament.aa_20mm.count` 12 → 32）→ 主值 + 「随期变化」角标，可展开窗口表
- 滑块右端标出该舰当下所处的切片代号（S3 / T1 等），点击跳该舰详情页对应锚点

**0 和未记载必须分开显示。** KGV 的 `armament.torpedo.tubes = 0` 是真实的 0（它真没鱼雷管），不是缺数据。混在一起就是造假。

浏览器端逻辑直接调 `resolve.ts` 的 `candidatesAt()` / `pickPrimary()` / `isDisputed()`，与 `ships/[id].astro` 的时间轴同一套代码。**这页的脚本会跟 `[id].astro` 那段（第 421~615 行）一样长，是主要风险点。**

### 阶段 3 · 校验与自测（半天）

`selftest.py` 加 4 例：
1. 两舰同字段都有值 → 主值按 tier 选
2. 单舰 fact 覆盖舰级 → 不判为分歧
3. 同窗两值 → `disputed: true`
4. 口径存疑标记生效

---

## 3.5 阶段 0 完工记录（2026-11-18 23:42 ~ 23:55 · 已完成）

**结论：阶段 0 全部做完，`validate` 0 错误 0 警告，41 个 `compare: true` 字段全部有数据。**

### 3.5.1 五个空字段的最终判定

不是「一刀切改 false」——逐个查了 `work/raw/` 的 11 份原始材料：

| 字段 | 查到的实情 | 处置 |
|---|---|---|
| `displacement.standard_metric` | **有真数据**：kbismarck `bsweights` 原值 43,313 mt 的 Typverdrängung | ✅ **补进 `classes/bismarck.yaml`**，保留 `compare: true` |
| `armament.mine.capacity` | 11 份材料零命中（`mine capacity` / `mines carried` / `载雷` / `mine rails` 全无）。这 5 舰本来就都不是布雷舰 | 改 `compare: false` |
| `propulsion.speed.cruise` | 只有「续航 @ 某航速」的条件值，反推巡航航速属于推断，违反红线 §2.2 | 改 `compare: false` |
| `propulsion.turning_diameter` | 只在 `field-design-refs.md`（别人的字段方案）里出现，没有一条真实战术直径 | 改 `compare: false` |
| `aviation.fuel.capacity` | 来源只给体积（illustrious 230,000 L），换算成吨要乘随温度变化的密度 | 改 `compare: false` |

> 顺带修正一处自己的口误：上一轮说「6 条口径存疑」，逐条核对后实际是 **4 条**。

### 3.5.2 新增 `comparable` 键（口径不可比的机读标记）

`types.ts` 加可选 `comparable?: boolean`，`validate.py` 加三条规则：

- 必须是布尔
- 标 `false` 必须写 `note`（说明是哪一处口径对不上），否则**报错**
- 对 `compare: false` 的字段标 `false` 是多余的，给警告

**已标的 4 条**（每个文件各 1 条）：

| 文件 | 字段 | 值 | 为什么不可比 |
|---|---|---|---|
| `ships/hood` | `displacement.standard` | 42,670 | navypedia 自己写的是 "normal"，不是条约标准口径 |
| `classes/illustrious` | `dimensions.length.oa` | 229.6 | 很可能是飞行甲板长，不是船体全长 |
| `classes/king-george-v` | `aviation.aircraft.capacity` | 2 | 数的是水上飞机，光辉级那栏是舰载机编制，不是同一度量 |
| `ships/tirpitz` | `aviation.aircraft.capacity` | 6 | 极限搭载（4 在库 + 2 在弹射器），不是机库容量 |

### 3.5.3 新增覆盖度检查

`validate.py` 每条跑完后会输出一行：

```
对比器：41 个 compare:true 字段全部有数据
```

若哪天出现全库无数据的 `compare: true` 字段，会列出字段名。**只报 info 不报 warn** —— selftest 的最小测试数据只有 1 条 fact，报 warn 会把 19 个用例全污染成「不该报警告」。

### 3.5.4 阶段 0 实际动过的文件（3 个，比预告的少）

| 文件 | 改动 |
|---|---|
| `data/fields.yaml` | 4 个字段 `compare: false` + note，`standard_metric` 的 note 补数据说明 |
| `data/classes/bismarck.yaml` | +1 条 `displacement.standard_metric` fact |
| `data/classes/illustrious.yaml`、`king-george-v.yaml`、`data/ships/hood.yaml`、`tirpitz.yaml` | 各 +1 个 `comparable: false` |
| `src/lib/types.ts` | +`comparable?: boolean` |
| `scripts/validate.py` | +comparable 校验、+覆盖度检查 |

### 3.5.5 环境注意

改 `data/` 下文件前**必须停 dev server**（`cmd /c "npm.cmd run dev"` 会锁住文件句柄，`edit` 报 `ReplaceFileW EIO Win32 1175`）。2026-11-18 23:51 踩过一次。

---

## 4. 动过的文件

| 文件 | 改动 | 状态 |
|---|---|---|
| `data/fields.yaml` | 5 个字段的 `compare` / note | ✅ |
| `scripts/validate.py` | comparable 校验 + 覆盖度检查 | ✅ |
| `src/lib/types.ts` | `comparable?: boolean`、`applies_to`、`multi` | ✅ |
| `data/classes/bismarck.yaml` 等 4 个数据文件 | +1 fact / +4 comparable | ✅ |
| `src/lib/data.ts` | `buildCompareIndex()` | ✅ |
| `src/pages/compare.astro` | 新建，约 1100 行 | ✅ |
| `src/components/TopNav.astro` | +对比器入口 | ✅ |
| `scripts/selftest.py` | +3 例（29→32） | ✅ |

**不动的**：`resolve.ts`（纯函数层已经完全够用，一行不改是这个方案最大的红利）、所有 `data/ships|classes/*.yaml` 的既有 fact、`global.css`（复用现有 design token）。

---

## 5. 已经拍板的（2026-11-18）

1. ✅ **时间轴是主角。** 上一轮我建议「时间轴降级成可选开关」，被否。改为**每舰独立一条滑块** + 「同步到同一时刻」按钮，首屏就落在时间模式。见 §2.1.2。
2. ✅ **口径存疑按推荐走。** 逐条核对后**实际是 4 条**（不是上一轮说的 6 条），已全部加 `comparable: false`。见 §3.5.2。
3. ✅ **P3.1 武器对比分开做。** 理由见 §2.3。
4. ✅ **「所有模式仿照 S1 和 S2」** —— 已找到对应会话，见 §5.1。**指的是工作模式，不是界面模式。**

### 5.1 S1 / S2 / S3 的确切身份（2026-11-18 查实）

用户改过会话名，标题里带 S1/S2/S3 后缀。实际对应：

| 代号 | 会话 id | 标题 | 起止 | 干了什么 |
|---|---|---|---|---|
| **S1** | `session-10fa90a1-a055-426b-a2c9-e010c637ca05` | 二战战舰资料网站建设**S1** | 11-17 13:07 → 11-18 08:50 | 框架、P0–P2、俾斯麦/提尔皮茨/胡德、海战页；最后上下文爆了 |
| **S2** | `session-6de69f2c-6545-45b6-898a-0da18bfa78dc` | 二战战舰资料网站建设**S2** | 11-18 08:58 → 23:20 | 光辉号 + KGV 入库、三栏目树重构、48 篇武器正文、177 张图、交出完整报告 |
| **S3** | `session-b5cbcd94-9777-455a-8cbd-6f8a1c77ae7f` | 二战战舰资料网站建设**S3** | 11-18 23:21 → 现在 | **就是本会话**，P3 对比器 |

> 查证方式：`C:\Users\mizuki\.dsh\storages\session_projcache\sessions\*.json` 里的 `record.rows.title.val`。

### 5.2 「所有模式仿照 S1 和 S2」到底指什么

上一轮我理解错了，以为是**界面模式**。实际是**工作模式**——S2 seq=110 那句「你的所有模式都仿照『二战战舰资料网站建设』这个对话就好了」，当时的回复把「模式」定义成了六条工作方式，逐字如下（S2 seq=253）：

| 模式 | 具体做法 |
|---|---|
| **汇报格式** | 先给结论（第一句就是结果），再接表格或条目，能追到推导，不复述你的问题 |
| **调研分工** | 每条线派一个 subagent，只给主题不给答案，要求每条结论带英文原句和 URL，主会话只接收摘要 |
| **进度管理** | 多阶段任务用 todo 列表；每轮收尾报告「做完了什么、卡在哪、下一步」 |
| **验证标准** | 只报实测值：`validate` 0 错误 0 警告、`selftest` 29 例、构建页面数、路由 HTTP 200，不说「应该能跑」 |
| **文件规矩** | 状态放文件不放对话；原始抓取进 `work/raw/`，正文进 `docs/`，临时脚本进 `work/` |
| **红线** | 有争议的说法一条不删；推断值不进 `data/`；查不到就写查不到 |

**这六条本来就一直在执行**（本轮的探针脚本进 `work/`、结论先行、只报实测的 validate 输出，都是照这个来的）。所以 §3 的分阶段计划不用改，只是正式登记一下这个约定。

### 5.3 界面设计从哪来（S1/S2 里的原始依据）

界面上**没有**可以直接抄的成品——S1/S2 从没做过对比器。但有两句是硬依据，必须遵守：

1. **S1 seq=85**：「对比器由字段注册表驱动。注册表里标了 `compare: true` 的字段，才会进入对比表。要新增一个字段，只需在注册表里加一行，不需要为新舰对写代码。装甲厚度这类字段要标成 `better: context`——并非越厚越好，倾角和布置方式同样重要，所以渲染时不做高低着色。」
2. **S1 seq=59**（当时给的两个选项 B）：「舰船对比器、装甲穿深查询、交互时间轴」，用户 seq=66 选了 B 并补了时间轴的定义：「在上面拖动可以展示不同时的数据」。

也就是说对比器的骨架早在 S1 就定了，本轮做的是把它实现出来，不是重新设计。

---

## 6. 报价

| 阶段 | 工作量 | 主要成本 |
|---|---|---|
| 0 数据闸门 | 半天 | 判断 5 个空字段的去留 |
| 1 索引 | 半天～1 天 | `deps` 序列化是唯一烧脑处 |
| 2 页面 | 1.5～2.5 天 | 每舰滑块 + 三态 UI，比原计划多半天 |
| 3 校验 | 半天 | — |
| **合计** | **约 4～5 个工作单元** | 约 3~4 轮 `validate + build` 循环 |

不打折的地方：`compare.astro` 的浏览器端脚本会比 `[id].astro` 那段（421~615 行）更长，因为它要同时管 N 条滑块。这是主要风险点。
