# 配图补充 · 第十三轮记录（2026-11-25 凌晨）

> 状态：**已完成并部署**
> 校验：`validate` 0/0 · `selftest` 32 例 · `build` 187 页 · `audit_links` 图片缺失 0

---

## 0. 一句话

给中途岛扩编的 **18 艘舰补齐配图**，共新增 **189 张** A 档（PD/CC0）图。
图片记录 **534 → 723**。按用户「每舰 10-15 张」的要求，12 艘达标，6 艘为素材上限。

---

## 1. 每舰张数

| 舰 | 张 | 舰 | 张 | 舰 | 张 |
|---|---|---|---|---|---|
| 凤翔 | **15** | 新奥尔良 | 13 | 利根 | 11 |
| 雾岛 | **14** | 波特兰 | 13 | 筑摩 | 11 |
| 阿斯托里亚 | **14** | 北安普敦 | 13 | 本汉 | 11 |
| 明尼阿波利斯 | **14** | 亚特兰大 | 12 | 川内 | 6 ○ |
| 彭萨科拉 | **14** | 榛名 | 12 | 文森斯 | 6 ○ |
| | | | | 长良 | 4 ○ |
| | | | | 哈曼 | 3 ○ |
| | | | | 莫纳汉 | 3 ○ |

○ = **素材上限**，不是遗漏。这几艘舰在 Commons 上的可用 A 档图就只有这么多，
已把分类翻尽（含舰级分类、子分类），不再拿同级的其他舰顶替。

---

## 2. 技术要点（写进这里，下次别重踩）

### 2.1 网络：直连已不通，必须走代理

2026-11-24 晚实测：`commons.wikimedia.org` **直连 TLS 握手超时**，
必须走 `http://127.0.0.1:12450`。上一轮（11-23）直连还能通，环境变了。

```python
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}),
    urllib.request.HTTPSHandler(context=ctx))
```

### 2.2 Commons 分类名：必须搜，不能猜

`docs/45` §3.1 记的「日本舰用下水年」规律**不可靠**：

| 舰 | 我猜的 | 实际 |
|---|---|---|
| 利根 | `Tone (ship, 1937)` | **`Tone (ship, 1938)`** |
| 筑摩 | `Chikuma (ship, 1938)` | **`Chikuma (ship, 1939)`** |
| 榛名 | `Haruna (ship, 1913)` | **`Haruna (ship, 1915)`** |
| 雾岛 | `Kirishima (ship, 1913)` | **`Kirishima (ship, 1915)`** |
| 凤翔 | `Hōshō (ship, 1921)` | **`Hōshō (ship, 1922)`** |
| 长良 | `Nagara (ship, 1921)` | **`Nagara (ship, 1922)`** |
| 川内 | `Sendai (ship, 1923)` | **`Sendai (ship, 1924)`** |

**正确做法：用 `srnamespace=14` 搜分类命名空间**，别按规律猜。
而且搜索会返回同名地名等噪音 —— 「Tone」的搜索里出现了 `Katori, Chiba`（168 张风景照），
必须按「候选里图片数最多且名字对得上」交叉判断。

### 2.3 下载 URL：upload 域持续 429，且 API 返回值带 utm 参数

API 返回的 `url` / `thumburl` 形如：

```
https://upload.wikimedia.org/wikipedia/commons/b/b3/NAME.jpg?utm_source=commons.wikimedia.org&...
```

**两个坑**：
1. 指向 `upload.wikimedia.org`，本站对该域**持续 429**
2. 带 `?utm_` 查询串，直接改写成 thumb 路径会拼错

**正确写法**：
```python
u = u.split('?')[0]                       # 先剥查询串
# upload.../commons/b/b3/NAME.jpg → thumb.../commons/thumb/b/b3/NAME.jpg/1280px-NAME.jpg
m = re.match(r'https?://upload\.wikimedia\.org(/wikipedia/commons)/(.)/(..)/([^/]+)$', u)
base, h1, h2, fname = m.groups()
stem = fname.rsplit('.', 1)[0]
thumb = f'https://thumb.wikimedia.org{base}/thumb/{h1}/{h2}/{fname}/1280px-{stem}.jpg'
```

---

## 3. 我在本轮犯的错（三次，都记下来）

### 3.1 筛选逻辑写反：给落盘文件加 `<sid>-` 前缀后用 sid 去匹配

第一版筛选把落盘名 `tone-01-xxx.jpg` 拿去匹配「tone」，**每张都命中，等于没筛**。
必须用 `commons_title`（Commons 原名）+ `descr` 判断。

### 3.2 跨舰共享哈希去重，把 new-orleans 的 15 张全删了

用全局 `seen` 字典去重，new-orleans 与 atlanta/portland 共用几张「合影」图，
哈希相同 → 先处理者通过、后者判重复删除 → new-orleans 整组归零。

**正确做法：只在单舰内部去重。** 一张合影本来就同时属于多艘舰，
跨舰删会导致另一艘没图。

### 3.3 手写 YAML 文本拼接，把 `images.yaml` 写坏

`author` 字段含换行与单引号，我只替换了 `' → ''`，没处理换行，
生成出 `author: 'xxx.jpg: 不明\nderivative work: ...` 这种非法单引号标量，
`build` 直接报 `Missing closing 'quote at line 10756`。

而且**用 `yaml.safe_dump` 整篇重写会抹掉所有注释**（本项目 `images.yaml`
头部有 A/B/C 授权规则与 IWM 判例共 18 行注释，还有 6 张 PRELOAD 标记）。

**正确做法**：每条 dict 单独 `safe_dump` 成片段，缩进后插入原文本，
保留原有注释。见 `work/write_images2.py`。

---

## 4. 主体判定标准（本站的规矩，已成文）

一张图能不能挂在某舰名下，按这个优先级：

1. **Commons 原始文件名含本舰名** → 通过（最硬，上传者通常按主体命名）
2. 否则看 `ImageDescription` 里**第一个出现的舰名**是不是本舰 → 是通过
   （国家档案馆编号照如 `80-G-55260` 靠这条救回来，描述里明写「USS Minneapolis (CA-36)」）
3. 都没有 → 不留（宁可这艘少几张）

**剔除的典型**：
- `tone-01` 是夕立号（描述主舰 chikuma）
- `hammann-01/02` 是列克星敦号爆炸照
- `nagara-04` 是 Sentai 4（四战队合影，本舰只是远景）
- `benham-09` 是约克城号弃舰
- `monaghan-03` 是 TBD 坠落

**教训**：`docs/52` §3.3 已经记过一次「自动筛选一定混进错图」，
这轮又踩了 —— 因为第一次筛选逻辑本身有 bug，等于没筛。
**每张图都要用 `read_image` 亲眼看**，不能只信哈希和文件名。

---

## 5. 关键文件

| 文件 | 内容 |
|---|---|
| `work/commons_client.py` | 带代理的 Commons API 客户端（可复用） |
| `work/decide_images.py` | 主体判定逻辑（平衡版，最终采用的标准） |
| `work/apply_images.py` | 按判定结果重下 + 编号 |
| `work/write_images2.py` | 安全追加进 `images.yaml`（不毁注释） |

---

## 6. 仍未做

- 7 个武器实体无配图（`14cm-50-3ns` `20cm-3ns` `21in-mk15` `36cm-45-t41`
  `45in-45-mk1` `8in-55-mk15` `8in-55-mk9`）—— 上一轮抓到的候选全被人眼否决
- 6 艘舰不足 10 张是素材上限，若要再补只能放宽到 B 档（CC-BY 外链）
