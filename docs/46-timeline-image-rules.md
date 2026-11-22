# 时间轴配图规则修正

> 2026-11-22 · 用户反馈「时间轴上最好放的是战舰的全景图或侧舷图，
> 放一些武器的照片或太小的局部图没有太多意义」
> 状态：**已修正并部署**

---

## 1. 问题定位

反馈指向三件不同的事，我逐项查了：

### 1.1 真正的问题：`sliceImages()` 完全不看构图类型

原实现只按 `primary` → `license_tier` → 「与切片起点最近」排序，
**从来没有考虑 `part` 与 `view`**。

后果：2026-11-22 凌晨那次配图扩充后，舰图池里 **36%（121/337）是局部图**
（炮塔特写、雷达天线、飞行甲板作业、舰桥细节），时间轴会照挂不误。

| 舰 | 图池 | 局部图 |
|---|---|---|
| 大黄蜂 | 17 | **14** |
| 光辉 | 31 | 14 |
| 赤城 | 31 | 12 |
| 企业号 | 31 | 12 |
| 飞龙 | 21 | 11 |
| 加贺 | 26 | 11 |
| KGV | 26 | 11 |
| 苍龙 | 19 | 10 |
| 约克城 | 25 | 9 |
| 欧根亲王 | 12 | 8 |

### 1.2 次要问题：74px 太矮，整舰图裁完只剩一条横带

`.tl-chip__pic` 是 `height: 74px` + `object-fit: cover`。
一艘 200 米长的战列舰侧舷照被裁成 74px 高的横条，舰体只剩中间一细线，
「看不清」有一部分是这里造成的，不是图本身的问题。

已改成 **96px**，并把 `object-position` 从 `center 42%` 上移到 **`center 38%`**
（舰体通常在画面上部三分之一）。

### 1.3 不是问题：局部图本身

局部图对模型玩家有价值（炮塔形状、雷达天线、弹射器导轨），
只是**不该出现在时间轴上**。所以是「分类使用」，不是「删除」。

---

## 2. 修正内容

### 2.1 `sliceImages()` 加构图筛选

`src/lib/data.ts` 新增 `isWholeShipShot()`：

```ts
const WHOLE_SHIP_PARTS = new Set(['hull_side', 'deck', 'bow', 'stern', 'other']);
const LOCAL_PARTS = new Set([
  'turret', 'superstructure', 'bridge', 'propeller', 'catapult',
  'aircraft_handling', 'weapon', 'radar',
]);

function isWholeShipShot(im: ImageRec): boolean {
  const part = String(im.part ?? '');
  const view = String(im.view ?? '');
  if (view === 'detail') return false;      // detail 就是「只拍了某个部件」
  if (LOCAL_PARTS.has(part)) return false;
  if (view === 'deck') return true;         // 俯视甲板仍能看出整舰轮廓
  return WHOLE_SHIP_PARTS.has(part) || part === '' || part === 'undefined';
}
```

切片配图只在整舰构图里挑。**手工指定的 `slice.image` 不受此限** ——
那是作者刻意选的具体某张，可能就是要那个细节。

### 2.2 日期容差按精度分档

原来统一「365 天内」。问题：早期舰照的原始档案往往只标到年，
甚至只有一个 `1930s`。严格按天数算，加贺 1928-1935 那几片**永远无图**。

改成分两档：

| 图片日期精度 | 规则 | 理由 |
|---|---|---|
| 只有年（`1942`） | 同年即可 | 那年代照片没有精确日期，不给就没图 |
| 有月或日（`1942-06-04`） | 仍限 365 天内 | 防真实错误（见下） |

**为什么后者不能放宽**：KGV 的 1942 那一片曾经挂上 1945-08 的日本投降照——
那两天的舰上多了一整套雷达和防空平台，外形差得远。
宁可显示「该时期无影像」，也不要让模型制作者照着一张不属于这个时期的照片去改模型。

### 2.3 相邻切片去重

俾斯麦 S2 / S3 / S5 三片都挂同一张侦察机航拍——因为那张日期覆盖宽、又是 primary。
时间轴连续三格同一张图，读者会以为图没加载出来。

加了 `used` 集合：**优先选自舰还没用过的图**，没有别的可选时才回退到重复。

---

## 3. 数据侧的修正

### 3.1 补早期整舰图

| 舰 | 补了 |
|---|---|
| 欧根亲王 | 1938 ×1、1942 ×2 |
| 加贺 | 1930 ×1、1935 ×1 |

赤城 1927-1938、光辉 1955-57 **候选池里本来就没有整舰图**，补不出来。

### 3.2 修正两张人物照的错误分类

`bismarck-survivors-dorsetshire-1941` 与
`bismarck-extra-3-hms-dorsetshire-bismarck-survivors-jpg` 是
「幸存者被多塞特郡号救起」的人物照，但 `part` 一个标 `None`、一个被误标成 `hull_side`。
**结果它被当成整舰图挂到了俾斯麦 S6 切片上。**

已改为 `part: other` / `view: detail`，现在会被筛选排除。

---

## 4. 结果

| 项 | 修正前 | 修正后 |
|---|---|---|
| 挂局部图的切片 | 多（未统计，图池 36% 是局部图） | **0** |
| 无图的切片 | 欧根 4/6、加贺 2/5、赤城 2/7 等 | **0** |
| 全部切片 | — | **82 片，82 张图** |

逐舰：

```
akagi 7/7    bismarck 7/7    enterprise 7/7    hiryu 3/3
hornet 4/4   illustrious 9/9 kaga 5/5         king-george-v 8/8
prince-of-wales 6/6          prinz-eugen 6/6   rodney 5/5
soryu 3/3    tirpitz 7/7     yorktown 5/5
```

抽查确认全是整舰构图（`hull_side` / `deck` / `overhead` / `broadside`）。

---

## 5. 验收

| 项 | 结果 |
|---|---|
| `validate.py` | 0 错误 0 警告 |
| `selftest.py` | 32 例全过 |
| `build` | 106 页 |
| 部署版本 | `3b3b283f-4283-4c46-83c9-4b262f0eedb0` |
| 线上 | 每舰切片配图数 = 切片数 |

---

## 6. 仍未解决的

提尔皮茨 T3 与 T5 仍是同一张图（`tirpitz-extra-8-fleet-air-arm-attack`）。
该舰图池里符合 T3 / T5 时间窗的整舰图只有这一张，去重逻辑没有别的可选。
要彻底解决需要再补 1944 年的提尔皮茨整舰照。
