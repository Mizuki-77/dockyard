# 全站 bug 排查与修复

> 2026-11-22 · 用户要求「排一遍全站的 bug，修好全部我们再继续」
> 状态：**五类体检全部归零，已部署**

---

## 0. 总览

| 体检项 | 修前 | 修后 |
|---|---|---|
| `astro check` | **7 errors** / 8 hints | **0 / 0 / 0** |
| 内部链接指向不存在的页面 | 0 | 0 |
| 锚点不存在 | **107 处** | **0** |
| 图片文件缺失 | 0 | 0 |
| 切片覆盖缺口 | **17 条** | **0** |
| 渲染脏数据（`[object Object]` 等） | **101 处** | **0** |
| 空区块 | 0 | 0 |
| 页面缺 `<h1>` | 1 | 0 |
| 多 `<h1>` | 4 | 0 |

---

## 1. `astro check` 的 7 个类型错误

### 1.1 事件流详略切换（5 处，`battles/[id].astro`）

```ts
// 错：querySelector 返回 Element，Element 上没有 dataset
const wrap = document.querySelector('.btl');
const btns = document.querySelectorAll('.density__btn');
function apply(mode) { wrap.dataset.density = mode; ... }

// 对：显式收窄类型 + 给 mode 标注联合类型
const found = document.querySelector<HTMLElement>('.btl');
const btns = document.querySelectorAll<HTMLElement>('.density__btn');
if (!found || !btns.length) return;
const wrap: HTMLElement = found;   // 闭包里 TS 不认 if 的收窄，赋 const 再进
type Density = 'major' | 'all';
function apply(mode: Density) { ... }
```

顺带修了一个**潜在运行时 bug**：`btns.forEach((b) => apply(b.dataset.density))`
里 `dataset` 是 `string | undefined`，直接传给 `apply` 会让
`data-density` 变成字符串 `"undefined"`。现在收窄后再传。

### 1.2 武器页 `ROLE_LABEL[role as never]`（2 处）

`roleOf()` 返回 `WeaponRole`，`ROLE_LABEL` 是 `Record<WeaponRole, ...>`，
类型本来就对。`as never` 是之前为绕过某个已不存在的问题加的，删掉即可。

---

## 2. 锚点不存在（107 处）

### 2.1 页脚链接全站失效

`Footer.astro` 链的是 `/help#license`，但帮助页的锚点是 `#image`。
**106 个页面共享同一个页脚，所以 106 处失效。**

顺带把 `/help` 改成 `/help#feedback`（更精确）。

### 2.2 首页「最近增补」指向不存在的 `#narrative`

正确锚点是 `#disputes`。

**但更大的问题是这个区块整体过期了**：硬编码着 `2026-11-17`、
「来源登记表扩至 80 条」——站里现在 237 条来源、15 艘舰。
等于在首页挂假数据。

改成从数据层现算：按舰艇最新年份倒序取 4 艘 + 来源总数。

---

## 3. 切片覆盖缺口（17 条）

### 3.1 原因一：武器事实污染舰的时间轴（14 艘中的 2 艘）

`buildShipView()` 计算时间轴上下界时只排除了 `identity.*`，
**没有排除带 `about` 的 `weapon.*` / `mount.*`**。

后果：飞龙的武器 fact 带 `1932` 日期、光辉带 `1930`——
把舰的时间轴起点拉到了开工前十几年。

```ts
// 修前
const dated = facts.filter((f) => !f.field.startsWith('identity.'));

// 修后：about 是「这型武器何时存在」，不是「这艘舰何时是那样」
const dated = facts.filter(
  (f) => !f.field.startsWith('identity.') && !f.about,
);
```

修后飞龙时间轴从 1932 变成 1936-07-08（与开工日对齐）。

### 3.2 原因二：13 艘舰缺「建造期」切片

时间轴左端有一大段没有切片的高亮区。拖动滑块时下方一片空白，
读者以为数据缺失。

最严重的是提尔皮茨：1936-06 开工，首个切片从 **1941-02** 开始，
**中间 5 年全空**。

已给 13 艘各补一个 `订购与建造` 前置切片（代码用 `X00`，如 `A0` → `A00`）。
节点文字从 `construction.*` fact 现算（订购 / 开工 / 承造厂 / 下水）。

### 3.3 原因三：企业号缺战后切片

末切片停在 1943-10，但 fact 记录到 1960 年拆解。补了 `E7`（战后）与
`E8`（封存与拆解）。

---

## 4. 一个真实的数据错误

### 威尔士亲王号显示了它沉没三年后才存在的排水量

排查切片缺口时发现 PoW 的最晚 fact 在 1945-01，但它 1941-12 就沉了。

追下去：`classes/king-george-v.yaml` 里有一条

```yaml
- field: displacement.standard
  value: 39100
  valid: { from: 1945-01-01 }
  note: 1945 年状态（经 1944 年改装增重）
```

挂在**舰级**上。而 PoW 是 KGV 级的成员，会继承这条 ——
于是它的页面显示了 39,100 吨，一个它不可能有的数字。

**根因**：这个项目没有「舰级 fact 只对某艘舰生效」的机制。
1945 年状态是五舰各自不同的（PoW 1941 沉、Duke of York 1949 退役、
KGV 活到 1957），本来就不该写在舰级里。

**修法**：从 `classes/` 移到 `ships/king-george-v.yaml`。

验证：PoW 页面 39,100 已清除，KGV 页面保留（它确实活到 1957）。

---

## 5. 渲染脏数据（101 处 `[object Object]`）

### 武器总览页把数组直接渲染成了字符串

```astro
<!-- 错：w.sources 是数组 -->
{w.sources.length > 1 && (
  <span class="tag tiny">{w.sources} 个来源</span>
)}

<!-- 对 -->
<span class="tag tiny">{w.sources.length} 个来源</span>
```

100+ 张武器卡每张渲染出 `[object Object][object Object][object Object] 个来源`。

**修的时候还踩了一个坑**：`tree.ts` 里 `leaf.sources` 已经是数字
（`w.sources.length`），所以同一文件第 45 行的 `x.sources > 1` 是**对的**。
我一度把两处都加了 `.length`，被 `astro check` 当场拦下
（`Property 'length' does not exist on type 'number'`）。
已回退并在两处加了注释区分。

---

## 6. 标题层级

### 6.1 首页缺 `<h1>`

从 hero 直接跳到各 section 的 `<h2>`，屏幕阅读器和 SEO 都拿不到
「这个页面是什么」。补了一个视觉上轻、语义上正的 `<h1>船坞 Dockyard</h1>`。

### 6.2 列表页有 16 个 `<h1>`

`ShipPreview.astro` 里每艘舰的舰名用了 `<h1>`。列表页渲染 15 个预览，
于是 1（页面标题）+ 15（预览）= 16 个 `<h1>`。

已降级：舰名 `h1 → h2`，简介/历史 `h2 → h3`，段落小标题 `h3 → h4`。

> ⚠️ 修的时候用了一串 `replace()` 连锁替换，`</h1>` → `</h2>` 又被
> 后续的 `</h2>` → `</h3>` 再改一遍，产生了 `<h2>...</h4>` 的错配。
> 已手工修正。教训：改标签名不要用连锁字符串替换。

---

## 7. 顺手清理的死代码

| 位置 | 内容 | 处置 |
|---|---|---|
| `compare.astro` | `cellHtml()` 30 行 | 删除（但先补回了它独有的功能） |
| `ships/[id].astro` | 未使用的 `getEntities` 导入 | 删除 |
| `weapons/[id].astro` | 未使用的 `getClasses`、`classByShip` | 删除 |
| `data.ts` | `getEntities` 的 `@deprecated` 标记 | 改注释（舰级页是合法调用方） |

### `cellHtml()` 删除前的重要发现

这个函数没人调用，但它里面的**置信度 C 角标逻辑**在内联渲染重写时漏掉了：

```ts
if (p.conf === 'C') bits.push('<span class="cmp-tag cmp-tag--conf">C</span>');
```

**对比器上 C 档数据没有任何可见标记** —— 而本站的核心承诺就是
「一眼看出这个数字有多可信」。不标等于把 C 档伪装成 A 档。

已补回内联渲染，然后删掉死函数。

另外核对了它独有的 `cmp-td--disp`（整格争议底纹）：内联版本用
`cmp-tag--disp` 表达得更精确，无需搬。

---

## 8. 三个"孤儿"其实是有意预留

`images.yaml` 里有 6 条记录指向不存在的舰：大和 4 张、衣阿华 1 张、密苏里 1 张。

核实后：**文件都在，是提前为大和/衣阿华/密苏里准备的素材**，
现在没有任何页面引用（舰还没入库）。

不是 bug，但容易被后来的维护者当成脏数据删掉。已在 YAML 里加 `PRELOAD`
注释标记，说明来由。

---

## 9. 新增的体检脚本

| 脚本 | 用途 |
|---|---|
| `work/audit_links.py` | 内链 / 锚点 / 图片完整性 |
| `work/audit_data.py` | class_of 双向、切片覆盖、孤儿、about 引用 |
| `work/audit_render.py` | 脏数据 / 空区块 / title / h1 数量 |
| `work/audit_array_render.py` | 数组被直接渲染的隐患 |

这些应该在每次大改后跑一遍。

---

## 10. 验收

| 项 | 结果 |
|---|---|
| `astro check` | **0 errors / 0 warnings / 0 hints**（项目首次） |
| `validate.py` | 0 错误 0 警告 |
| `selftest.py` | 32 例全过 |
| `build` | 106 页 |
| 链接体检 | 内链 0 / 锚点 0 / 图片 0 |
| 数据对账 | 切片问题 0 |
| 渲染体检 | 脏数据 0 / 空区块 0 / 缺 h1 0 / 多 h1 0 |
| 部署版本 | `fb555cb1-8292-443d-9ec4-1ab22ad88f46` |

线上逐项复核：6 个重点页面全部 200，`[object Object]` 与 `undefined` 均为 0。
