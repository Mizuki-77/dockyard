# 分片写作规范（给 subagent 用）

> Dockyard（二战战舰资料站）· 2026-11-22 · 主会话下发
>
> **你只能写 `work/staging/<你的组名>/` 目录。绝对不要碰 `data/`、`src/`、`public/`、`docs/`。**
> 主会话会用脚本合并你的分片。写错位置 = 白干。

---

## 0. 你要产出什么

| 文件 | 内容 |
|---|---|
| `classes/<class-id>.yaml` | 舰级公共数据（该级所有舰共享的设计值） |
| `ships/<ship-id>.yaml` | 单舰**差异**数据（只写与舰级不同的、本舰特有的） |
| `slices/<ship-id>.yaml` | 状态切片（该舰外形/配置随时间的变化分界） |
| `articles/<ship-id>.yaml` | 舰艇正文（简介 + 历史） |
| `sources-fragment.yaml` | 你新登记的所有来源 |
| `RESEARCH-NOTES.md` | 调研底稿：每条结论的英文原句 + URL |

**不写**：`data/images.yaml`（配图由主会话统一处理）、`data/fields.yaml`、`data/sources.yaml` 本体。

---

## 1. 三条红线（违反即返工）

1. **查不到就写查不到。** 不要用姊妹舰的值填充，不要推算后当成事实写进 fact。
   拿不到就整条不写，在 `RESEARCH-NOTES.md` 里记一句「未获取」。
2. **有争议的说法一条都不删。** 两个来源打架就两条都写，各带自己的 `src`，
   并在 `note` 里写「两说并列，不裁决」。
3. **推断值不进 fact。** 「主炮/副炮/防空炮」这种分类不是史料字段，不要写成 fact。
   推断过程写在 `RESEARCH-NOTES.md`。

---

## 2. fact 的格式（最核心）

```yaml
facts:
  - field: displacement.standard        # 必须在 data/fields.yaml 注册过
    value: 41700
    unit: t                             # 注册表要求单位时必须给，且必须与注册表一致
    src: [naval-history-norfolk]        # 至少一个，必须已在 sources 里登记
    valid: { from: 1940-08-24, to: 1941-05-27 }
    confidence: A                       # 只有 A / B / C。D 是来源层级，不是置信度
    note: 德方标准排水量口径
```

### 2.1 硬规则

| 规则 | 说明 |
|---|---|
| `field` 必须在 `data/fields.yaml` 里 | 先读该文件确认。**没有的字段不要自己造** |
| `value` 类型要对 | `number`/`integer` 字段不能带引号；`string` 可以是中文；`enum` 必须是枚举值；`bool` 是 true/false |
| `unit` 必须和注册表一致 | 注册表写 `unit: t` 你就必须写 `t`，不能写 `tons`。注册表 `unit: None` 的就不写 unit |
| `src` 至少一个 | 引用的 id 必须在你 `sources-fragment.yaml` 或现有 `data/sources.yaml` 里登记过 |
| `valid.from` 必填 | 格式 `YYYY` / `YYYY-MM` / `YYYY-MM-DD` |
| `valid.to` 留空要写 `note` | 或者文件顶层写一次 `open_ended_note` 说明 |
| `confidence` 只有 A/B/C | 来源是 D 级专题站，confidence 填 C（或留空） |
| 来源 tier E（百科）不能当 fact 的来源 | 维基只能用来找线索，顺着它的引用找到原始出处 |

### 2.2 带限定词的字段

`protection.armor.thickness` / `armor.angle` / `armor.material` 必须给 `qual`：

```yaml
  - field: protection.armor.thickness
    value: 114
    unit: mm
    qual: { part: belt, region: main }     # 两个键都要给
    src: [...]
    valid: { from: 1937-08-05 }
    confidence: A
```

- `qual.part` 合法值：`belt / upper_belt / lower_belt / deck / slope / bulkhead / turret / barbette / conning_tower / funnel_uptake / splinter_belt / main_belt_aft / flight_deck / hangar_side / hangar_deck / magazine`
- `qual.region` 合法值：`main / fore / aft / upper / lower / face / side / rear / roof / top / bottom / torpedo / splinter`

`weapon.projectile_weight` / `weapon.muzzle_velocity` 需要 `qual: { shell_type: ... }`
（`apc / ap / he / he_base_fuze / he_nose_fuze / sap / aa / coastal / special`）。
**不确定弹种就别写这两条字段。**

---

## 3. 常用字段清单（照抄，别自已挑）

### 3.1 每艘舰都该有的 35 个骨架字段

`identity` 组：`name_original` / `name_zh` / `name_en` / `operator` / `ship_type` / `nation` / `era` / `building_program`

`dimensions` 组：`displacement.standard` / `length.oa` / `beam.wl` / `draught.mean`

`propulsion` 组：`plant_type` / `shafts` / `boiler.count` / `boiler.type` / `turbine.count` / `turbine.type` / `power.design` / `speed.design` / `fuel.capacity`

`construction` 组：`builder` / `builder_location` / `laid_down` / `launched` / `commissioned` / `fate_date`

`protection` 组：`scheme` / `armor.thickness`（带 qual）/ `armor.weight` / `underwater.depth`

`service` 组：`complement.standard` / `fate_category`

`aviation` 组：`aircraft.types`（连驱逐舰都能写「无」，但没数据就不写）

**这 35 个拿齐页面就是完整的。拿不全就先写拿到的。**

### 3.2 关键枚举值（写错会校验失败）

- `identity.ship_type`：`battleship / battlecruiser / heavy_cruiser / light_cruiser / armored_cruiser / aircraft_carrier / escort_carrier / seaplane_carrier / destroyer / destroyer_leader / frigate / corvette / submarine / other`
- `identity.nation`：`germany / united_kingdom / united_states / japan / italy / france / soviet_union / poland / norway / ... / other`
- `identity.era`：`ww1 / interwar / ww2 / cold_war / modern`
- `construction.fate_type`：`sunk_by_enemy / sunk_by_scuttling / scuttled / scrapped / preserved / wrecked / expended_as_target / other`
- `protection.scheme`：`all_or_nothing / incremental / turtle_back / other`
- `propulsion.plant_type`：`steam_turbine / steam_reciprocating / diesel / other`
- `weapon.category`：`naval_gun / anti_aircraft_gun / torpedo / depth_charge / rocket / radar / fire_control / aircraft / other`
- `weapon.nation`：`germany / united_kingdom / united_states / japan / italy / france / soviet_union / other`（**没有 poland**）

---

## 4. 武器实体怎么写

武器不是独立文件，是挂在舰级/单舰 `facts` 里、用 `about:` 指过去的 fact 组。

```yaml
  - about: weapon:8in-50-mk8
    field: weapon.designation
    value: 8"/50 (20.3 cm) Mark VIII
    src: [navweaps-8in-50-mk8]
    valid: { from: 1927 }
    confidence: A

  - about: weapon:8in-50-mk8
    field: weapon.category
    value: naval_gun
    src: [navweaps-8in-50-mk8]
    valid: { from: 1927 }
    confidence: A
```

炮位（一个具体炮塔）用 `about: mount:<id>`，必写 `mount.weapon: weapon:<id>`：

```yaml
  - about: mount:county-a-turret
    field: mount.weapon
    value: weapon:8in-50-mk8
    src: [naval-history-norfolk]
    valid: { from: 1928-02-14 }
    confidence: B
```

**注意**：`about: weapon:*` 的 fact **不参与舰的时间轴计算**（这是设计如此）。
所以「这舰什么时候装了什么炮」要另外用 `armament.mount.summary` 这类**不带 about** 的字段记。

武器放在**舰级**文件里（同型舰共享），只有某舰独有的才放单舰文件。

### 4.1 本轮涉及的武器 id（统一用这些，别自创）

| id | 型号 | 装在哪 |
|---|---|---|
| `8in-50-mk8` | 8"/50 (20.3 cm) Mk VIII | 郡级重巡 |
| `6in-50-mk23` | 6"/50 (15.2 cm) Mk XXIII | 城级轻巡 |
| `45in-45-mk1` | 4.5"/45 (11.4 cm) QF Mk I | 皇家方舟号 |
| `47in-45-mk12` | 4.7"/45 (12 cm) QF Mk XII | 部族级、N 级驱逐舰 |
| `2pdr-mk8` | 40 mm 2-pdr Mk VIII | **已存在**，直接复用 |
| `20mm-oerlikon` | 20 mm Oerlikon | **已存在**，直接复用 |
| `type-286` / `type-271` 等雷达 | 按 `sensors.radar.installed` 字段记即可，不必建武器实体 |

---

## 5. 舰级 vs 单舰怎么分工

- **舰级文件**放该级所有舰共享的设计值：主尺度、动力、装甲方案、固定武备布置。
  文件名 `classes/<class-id>.yaml`，必须有 `id` / `name{zh,en}` / `facts`，
  推荐再写 `class_of: [船1, 船2, ...]` 和 `open_ended_note`。
- **单舰文件**只写差异：建造日期、改装、战历、本舰独有的值（覆盖舰级）。
  文件名 `ships/<ship-id>.yaml`，必须有 `id` / `name{zh,en}` / `class` / `facts`。

**判据：这个值换一艘同级舰就变了吗？** 会变 → 写单舰；不变 → 写舰级。

`open_ended_note` 模板（舰级文件请抄这段）：

```yaml
open_ended_note: |
  本文件绝大多数 fact 的 valid.to 都留空，这是结构性的，不是漏填：
  舰级设计参数的生效期从设计定案/服役起，到该级最后一艘损失或拆解为止，
  期间不因改装而改变；实际战备状态随时间的变化写在 data/ships/<id>.yaml 的
  状态切片里，由单舰 fact 覆盖。因此这里的 open 时间窗表示「无已知终止事件」。
```

---

## 6. 切片格式

文件名 `slices/<ship-id>.yaml`：

```yaml
ship: norfolk
slices:
  - code: P0
    title: 建造与服役（1926-1930）
    from: 1926-07-08
    to: 1930-05-01
    note: >-
      1926-07-08 在 Fairfield 开工，1928-02-14 下水，1930-05-01 服役。
  - code: P1
    title: 二战前改装（1930-1939）
    from: 1930-05-02
    to: 1939-09-02
    note: >-
      1930 年代加装 HACS 高角火控与 4 英寸高炮。
```

- `code` 是 `P0/P1/P2...` 顺序编号
- `from` 必填，`to` 可省（表示延续）
- `note` 写**这一片到底变在哪**，不要只抄日期
- 切片边界要落在该舰日期范围内，不要超出
- 3~8 片即可。**小舰不要硬凑片数**

---

## 7. 正文格式

文件名 `articles/<ship-id>.yaml`：

```yaml
ship: norfolk
updated: 2026-11-22

intro:
  lead:
    zh: 一句话概括这艘舰是谁、最值得记住的是什么。
    en: One-sentence summary in English.
  paragraphs:
    - heading: 小标题
      text:
        zh: 一段话。
        en: One paragraph.
      src: [naval-history-norfolk]

history:
  - id: build
    title: { zh: 建造, en: Building }
    range: { from: 1926, to: 1930 }
    events:
      - date: 1926-07-08
        text:
          zh: 在 Fairfield 开工。
          en: Laid down at Fairfield.
        src: [naval-history-norfolk]
```

硬规则：

| 规则 | 说明 |
|---|---|
| 顶层必须有 `ship` / `intro` / `history` | 缺一个校验就红 |
| `intro.lead` 必须有 `zh` | `en` 强烈建议也给 |
| `intro.paragraphs` 至少一段 | 每段必须有 `heading` + `text.zh` + `src` |
| `history` 至少一节 | 每节有 `id` / `title{zh}` / `events`，每节至少一条事件 |
| 每条 event 必须有 `date` + `text{zh}` + `src` | 日期格式 `YYYY` / `YYYY-MM` / `YYYY-MM-DD` |
| **正文不许出现**：据说 / 有人认为 / 有人称 / 据信 / 或许 / 大概 / 应该是 | 校验器会警告。有争议就写明「X 说 A，Y 说 B」 |
| 每段 `src` 不能引 tier E | 维基不能当正文来源 |

**篇幅要求（按主会话给的「重要度」定，别超）**：
- 普通小舰：`intro` 2~3 段 + `history` 2~3 节、共 8~15 条事件
- 有特殊意义的舰：`intro` 3~4 段 + `history` 3~4 节、共 15~25 条事件

---

## 8. 来源分片格式

文件 `sources-fragment.yaml`：

```yaml
sources:
  - id: naval-history-norfolk
    title: HMS Norfolk — Service History (Royal Navy Warships in World War 2)
    url: https://www.naval-history.net/xGM-Chrono-10CA-HMS_Norfolk.htm
    type: website
    tier: D
    role: [data, narrative]
    operator: Naval-History.net（Gordon Smith 编辑）
    lang: en
    access: direct
    fetched: 2026-11-22
    license: all_rights_reserved
    note: 逐月服役年表。口径提示：……
```

**必填**：`id` / `title` / `url` / `type` / `tier` / `role`

- `tier` 只能是 `A` / `B` / `C` / `D` / `E`
  - A 一手档案（战报、日志、审判记录）
  - B 同期官方出版物（Jane's、海军部手册、DANFS）
  - C 权威二次文献（Conway's、Campbell、NavWeaps、专题学术站）
  - D 专题网站（naval-history.net、uboat.net、Navypedia、combinedfleet）
  - E 百科（维基）——**只能当线索，不能作 fact 来源**
- `role` 只能从 `data` / `narrative` / `rights` / `lead` / `image` 里选
- `type` 建议值：`website` / `document` / `archive` / `official_publication` / `primary_archive` / `paper` / `encyclopedia` / `database`
- `access`：`direct` 或 `proxy`
- `fetched`：你今天抓的日期，`2026-11-22`
- `id` 命名：`naval-history-<ship>` / `uboat-<ship>` / `navypedia-<class>` / `navweaps-<gun>` / `iwm-<ship>` 这类

**已经登记过的来源直接复用，不要重复登记**（尤其 `navweaps-8in-50-mk8` / `navweaps-6in-50-mk23` / `navweaps-45in-45-mk1` 已存在）。
先在 `data/sources.yaml` 里搜一下。

---

## 9. 调研注意事项

### 9.1 抓取方式：**不要用 `web_fetch` / `research`**

> 2026-11-22 晚实测，三个 subagent 各自独立撞到同一件事：

`web_fetch` 与 `research` 工具在本机对**几乎所有域名**返回
`SSRF blocked: <域名> resolves to private address 198.18.0.x`。
被拦的包括 `navypedia.org`、`naval-history.net`、`uboat.net`、
`armouredcarriers.com`、`zh.wikipedia.org`、`thegazette.co.uk`，
连 `example.com` 都被拦（凡是走系统 DNS 解析到 198.18.x.x 的全挂）。

**改用下面两种之一，都能通：**

```powershell
# PowerShell
Invoke-WebRequest -Uri "https://www.naval-history.net/xxx.htm" -UseBasicParsing `
  -OutFile work/staging/<你的组>/_raw/xxx.html
```

```python
# Python
import urllib.request
req = urllib.request.Request(url, headers={'User-Agent': 'DockyardArchive/1.0'})
data = urllib.request.urlopen(req, timeout=45).read()
```

抓下来的原始页面放 `_raw/`，正文写进 `RESEARCH-NOTES.md`。
**抓不到就换站点，三次不通就记进笔记报告主会话，别硬试。**

### 9.2 来源与站点

- **每条结论带英文原句 + URL**，写进 `RESEARCH-NOTES.md`。这是本站的立站之本。
- 优先来源顺序：一手档案 > 官方出版物 > 权威二次文献 > 专题站。
- 可用站点（本轮实测可直连）：
  - `naval-history.net` —— 英国舰逐月年表，覆盖全生涯，**本轮主力**
  - `uboat.net/allies/warships/` —— 驱逐舰/护航舰数据齐全
  - `navypedia.org` —— 主尺度/排水量骨架
  - `navweaps.com` —— 武器数据。**注意 URL 会 404**：
    4.7"/45 Mk XII 的实际页面是 `WNBR_47-45_mk9.php`（与 Mk IX 同页），
    不是 `WNBR_47-45_mk12.php`。抓之前先在站内索引里找。
  - `iwm.org.uk` —— 帝国战争博物馆（**只能外链，不能下载**，见授权规矩）。
    ⚠️ 实测本机对它有 403
  - `commons.wikimedia.org` —— 图片（**本轮不抓图，别管**）
- **不要用维基百科当事实来源。** 可以用它找线索，然后去原始出处。

### 9.3 一条救命的规矩

这轮 10 个 subagent 里有 6 个在任务书里发现了主会话写错的史实（共 7 处，
包括「锡克人号参加过圣纳泽尔突袭」这种完全错误的关联）。
它们之所以敢改，是因为任务书里写了：

> 「上表是我从记忆里写的，**你必须逐条核实**。如果查到的和上表不符，
> **以你查到的来源为准**，并在 `RESEARCH-NOTES.md` 里指出我写错了哪条。」

**照做。** 任务书里的任何史实陈述都当「待核实」处理，不是标准答案。

---

## 10. 交付前自检（必做）

```powershell
# 1. YAML 能不能解析
python -c "import yaml,glob;[yaml.safe_load(open(p,encoding='utf-8')) for p in glob.glob('work/staging/<你的组名>/**/*.yaml',recursive=True)];print('yaml ok')"
```

2. 自查清单：
- [ ] 每条 fact 的 `field` 都在 `data/fields.yaml` 里
- [ ] 每条 fact 都有 `src`，且 src 都在 `sources-fragment.yaml` 或 `data/sources.yaml` 里
- [ ] 每个带单位字段的 `unit` 与注册表一致
- [ ] `protection.armor.*` 都带 `qual`
- [ ] 没有 `confidence: D`
- [ ] 没有用 tier E 来源支撑 fact
- [ ] `articles/` 顶层有 `ship` / `intro` / `history`
- [ ] 正文没出现「据说/有人认为/据信/或许/大概/应该是」
- [ ] 没有编造的数字

---

## 11. 报告格式（回给主会话）

`RESEARCH-NOTES.md` 末尾写一节：

```markdown
## 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | N |
| 单舰文件 | N |
| 切片文件 | N |
| 正文文件 | N |
| 新登记来源 | N |

### 卡住的地方
- （具体哪一项查不到、试了哪些站点、为什么不写）

### 有争议的记载
- （哪些项两源打架，各说了什么，你怎么并列的）
```

**主会话只读摘要，不读你的全文。** 所以摘要要能独立看懂。
