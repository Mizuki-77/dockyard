# 莱茵演习三舰入库 · 完工记录

> 2026-11-22 · 用户指令「以 A 为主，适度找德文资料，注意 token，动工」
> 状态：**三艘舰 + 四型武器全部入库并部署**

---

## 1. 交付

### 三艘舰

| 舰 | id | 舰级 | fact | 正文 | 图 | 切片 |
|---|---|---|---|---|---|---|
| 威尔士亲王号 | `prince-of-wales` | king-george-v（**已有**，复用） | 20 | 6 段 | 2 张 | 6 片 |
| 欧根亲王号 | `prinz-eugen` | hipper（**新建**） | 22 | 6 段 | 2 张 | 6 片 |
| 罗德尼号 | `rodney` | nelson（**新建**） | 27 | 7 段 | 2 张 | 5 片 |

### 四型武器（用户要求每型都要有各自的页面）

| 武器 | id | 正文 | 图 | 装舰 |
|---|---|---|---|---|
| 16"/45 Mark I | `16in-45-mk1` | 3 段 | ✅ | 罗德尼 |
| 6"/50 Mark XXII | `6in-50-mk22` | 3 段 | ✅ | 罗德尼 |
| 4.7"/40 Mark VIII | `47in-40-mk8` | 3 段 | ✅ | 罗德尼 |
| 20.3 cm SK C/34 | `20-3cm-sk-c34` | 4 段 | ✅ | 欧根亲王 |

威尔士亲王号的武器全部继承 KGV 级已有页面，不需要新建。

### 战役闭合

| 战役 | 之前 | 现在 |
|---|---|---|
| **丹麦海峡** | 2/4 可点 | **4/4 全通** |
| 最终战 | 2/13 | 3/13（主要战斗舰全通） |
| 中途岛 | 7/7 | 7/7（本来就全通） |

---

## 2. 一个重要的判断失误（必须记下来）

**我最初判定欧根亲王「资料最差」，那是错的。**

我在启动前实测了 `kbismarck.com/prinz-eugen.html` 和 `prinz_eugen.html`，
两个都 404，于是判断「该站没有这个舰的页面」，并写进了文档，
还建议用户接受「该舰未获取会更多」。

**实际上正确地址是 `prinzeugen.html` —— 无连字符。**
该页是完整的单舰页，并且挂着本舰**战争日志全译本（122 页 PDF，A 级）**的入口。

结果：欧根亲王成了三艘里一手材料最丰富的一艘——有战争日志、军医报告、
OKM 鱼雷调查三份 A 级档案。

**教训**：URL 404 只说明那个 URL 错了，不说明资源不存在。
判定「没有」之前应该至少试过站内索引或 sitemap。

---

## 3. 三份调研各自的贡献

### 3.1 罗德尼（work/raw/rodney-tech.md，737 行 + nelson-class.md，814 行）

**最大贡献是抓到了项目级错误：**

Rodney 的副炮是 **6"/50 Mark XXII**，不是 Mark XXIII。
项目里曾把 Mk XXIII 登记成「Rodney 副炮」，`work/raw/last-battle.md`
的武备行也跟着写错了。

- 硬证据：Mk XXII 页装舰栏写 "Nelson Class"；Mk XXIII 页装舰栏全是巡洋舰
  （Leander / Perth / Arethusa / Town / Edinburgh / Fiji / Ceylon / Swiftsure），**通篇没有 Nelson class**
- 错因推测：两型弹重巧合都是 112 lbs（50.8 kg），初速不同（898 vs 841 mps），
  当初按弹重对号没核装舰栏
- **validate.py 抓不到这种错**（不核型号与装舰对应），只能靠人眼

已修：`sources.yaml` 的 note、`last-battle.yaml` 的武备行与来源、
`work/raw/last-battle.md` 的三处。

另外还发现 **`last-battle.md` 第 720 行「Sheffield 火炮未获取」已过期** ——
Mk XXIII 页就是 Sheffield（Town 级）的炮，一直有，只是被贴错标签。

### 3.2 威尔士亲王（work/raw/prince-of-wales-tech.md，872 行）

**纠正了任务书 4 处前提：**

1. **「1941-03-31 服役」不成立** —— 那是**完工**；服役是 **1941-01-19**
   （原文 "Commissioned, incomplete, and with only half her crew, for trials"）
2. **「没追击是因为燃油」是错的因果** —— 05-24 的理由是战备状态；
   燃油要到 05-25 才成为理由，而且那天真正缺油的是 KGV（1,200 t / 32%）
3. **「鱼雷 vs 抽水泵」是伪二选一** —— 真实是三条独立破坏链，
   其中「螺旋桨轴把舱壁铰穿」是 Garzke 2012 残骸法证的核心发现
4. **navypedia 记本舰雷达为 279 + 284 不完整** —— 舰长 A 级报告提到 281

### 3.3 欧根亲王（work/raw/prinz-eugen-tech.md，1304 行 + hipper-class.md，602 行）

**纠正了任务书 5 处前提，其中三处是常见误传：**

1. **不是「1942 年瑟堡空袭」** —— 实为 **1941-07-02 布列斯特**，60 死（含副舰长）
2. **不是「1960 年代倾覆」** —— **1946-12-22** 倾覆于夸贾林 Enubuj 礁
3. **丹麦海峡一雷未发不是装备故障** —— OKM 专门出调查文件，
   结论是鱼雷官训练不足 + 火控雷达分配不当
4. `data/narratives/bismarck.yaml` 里**没有**「谁打沉了胡德」条目
   （现存五条无一是这个主题），实际材料在 `work/raw/hood-sinking.md` §争议二
5. `data/ships/hood.yaml` 第 941 行「另见 narrative」是**悬空引用**，指向不存在的条目

**最重要的一条自律**：它列了 17 项「差点用姊妹舰数据填、最后没填」。
其中 5 项（标准排水量 14,240 / 燃油 4,250 / 续航 6,800 / 型深 12.45 / 测距仪 5×7）
在 KB 的 PrinzEugen 页与 Admiral Hipper 页**逐字相同**，
而本舰战争日志记载实测油量 3,233 m³ 与 KB 的 4,250 mt 差约 1,000 t ——
判定为复制痕迹，全部改标冲突。这是正确的做法。

---

## 4. 德文资料：实测结论（用户要求「适度找找」）

不值得再投入。实测结果：

| 尝试 | 结果 |
|---|---|
| Bundesarchiv 首页 | 200，但站内搜不到舰船档案 |
| Lexikon der Wehrmacht | 200，len 仅 243（空壳） |
| Württembergische Landesbibliothek | URLError |
| deutsche-kriegsmarine.de | URLError |
| kriegsmarine.de | URLError |
| de.wikipedia.org | **403**（被封） |

**唯一的收获是发现 kbismarck 的 URL 拼写规律**（见 §2），
以及它挂着 `pg-ktb.zip`（122 页战争日志英译本）。
德文原始档案这条线基本走不通，成本收益不划算，停止。

---

## 5. 图片：三艘舰的图早就在库里

一个有意思的发现：**三艘舰的图早在 2026-11-17 就下载并登记好了**，
每艘 2 张、全是 A 档 PD、主图已标记，只是一直没有舰页去引用。

| 舰 | 主图 | 副图 |
|---|---|---|
| 罗德尼 | 1940 年代舷侧 | 1928 年舷侧 |
| 威尔士亲王 | 1941-08 阿真舍 | 1941-12-10 与反击号 |
| 欧根亲王 | 1945-05 航行中 | 1946-03 巴拿马运河 |

说明当初规划时就为这三艘预留了素材。

四型武器的图是本轮新抓的，全部按 Commons 分类浏览、
`thumb.wikimedia.org` 下载（`upload.` 域会 429）。

---

## 6. 新增/修改的文件

### 数据

| 文件 | 说明 |
|---|---|
| `data/ships/{rodney,prince-of-wales,prinz-eugen}.yaml` | 新建 |
| `data/classes/{nelson,hipper}.yaml` | 新建 |
| `data/slices/{rodney,prince-of-wales,prinz-eugen}.yaml` | 新建 |
| `data/articles/{rodney,prince-of-wales,prinz-eugen}.yaml` | 新建 |
| `data/weapon-articles/{16in-45-mk1,6in-50-mk22,47in-40-mk8,20-3cm-sk-c34}.yaml` | 新建 |
| `data/fields.yaml` | **新增 `armament.gun_failures` 字段**（炮术故障记录，string 型） |
| `data/sources.yaml` | 新增 17 条来源（222 → 249） |
| `data/images.yaml` | 新增 4 张武器主图（282 → 286） |
| `data/battles/denmark-strait.yaml` | 挂上 prince-of-wales / prinz-eugen |
| `data/battles/last-battle.yaml` | 挂上 rodney；修 Mk XXIII → Mk XXII |

### 关于新字段

罗德尼的炮术故障清单原本想塞进 `armament.broadside_weight`，
但那个字段是 `number` 型、单位 kg，塞文本会被校验器拒绝。

**正确做法是往 `fields.yaml` 加字段，不是硬塞。** 新增：

```yaml
- id: armament.gun_failures
  label: { zh: 炮术故障记录, en: Gun failures in action }
  type: string, group: armament
```

---

## 7. 验收

| 项 | 结果 |
|---|---|
| `validate.py` | **0 错误 0 警告** |
| `selftest.py` | **32 例全过** |
| `build` | **106 页**（原 97 + 9） |
| 部署版本 | `04a96e46-1936-479e-b5ff-4885a5190362` |
| 线上验证 | 三舰 + 四武器全部 200，图与正文均渲染 |

页面篇幅（正文字符数，不含导航）：

```
prince-of-wales  37,722
rodney           23,350
prinz-eugen      21,118
```

---

## 8. 已知的遗留

1. **最终战还有 10 艘未入库**（Norfolk / Dorsetshire / Sheffield / Ark Royal /
   Victorious / Cossack / Maori / Zulu / Sikh / Piorun），页面已标「本站尚未收录」
2. **欧根亲王的舰体数据大面积未获取** —— 垂线间长、干舷、系数、GM、
   装甲总重等，各来源都没有。这是资料现状，不是遗漏
3. **纳尔逊级的装甲总重与占比**是全项目空白，KGV 级有 RMG 给的值，本级一个没有
4. **`data/ships/hood.yaml:941` 的悬空 narrative 引用**未修（subagent 报告，本轮未动）
