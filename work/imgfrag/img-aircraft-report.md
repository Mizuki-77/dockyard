# 舰载机配图报告（img-aircraft）

产物：`work/imgfrag/img-aircraft.yaml`（19 条，顶层 `images:`）+ `public/img/weapons/` 下 19 个 jpg。
未动 `data/images.yaml`、`data/` 与 `src/` 任何文件。

## 总览

| 型号 | 条数 | 档位 | 像素 | 场景 |
|---|---|---|---|---|
| swordfish 剑鱼 | 2 | A / A | 1007×737、800×599 | 甲板机群、折翼下升降机 |
| fulmar 海燕 | 2 | A / A | 800×602、800×602 | 机库折翼排、甲板逆光折翼 |
| sea-gladiator 海斗士 | 2 | A / A | 800×587、1280×1015 | 着舰钩特写、马耳他「信仰」 |
| corsair 海盗 | 2 | A / A | 1280×966、800×603 | FAA 甲板列队、折翼瞬间 |
| avenger 复仇者 | 2 | A / A | 1280×955、800×608 | 挂弹、弹射起飞 |
| walrus 海象 | 2 | A / A | 1268×939、800×602 | 吊离弹射甲板、弹射离舰 |
| seafox 海狐 | 2 | A / A | 800×613、763×800 | 落水滑行、机头检修 |
| arado-196 | 2 | A / A | 1280×914、1280×910 | 格奈森瑙弹射器、舍尔上将号 |
| flycatcher 捕蝇鸟 | 2 | A / A | 1280×946、1101×584 | 1923 整机、飞越鹰号 |
| fairy-iiif 费雷 IIIF | 1 | A | 740×552 | 着舰暴怒号 |

全部 A 档（`pd`），无 B 档，无 C 档。18 条的 `note` 带 IWM 判例句；另 3 条（两条 Ar 196、费雷 IIIF）是 PD-USGov、无 IWM credit，不需要该句。

## 逐条

### swordfish
- `swordfish-hms-victorious-bismarck-strike`（主图）IWM A 4090，1941-05-24。胜利号后甲板机群出击俾斯麦号前。
  选它：唯一同时给出「甲板停放 + 具体行动」的全景，鱼雷挂载与系留索可见。放弃：`A19718`/`A19719`（Tracker 号着舰/折翼，与 `A18270` 信息重复且分辨率更低）。
- `swordfish-hms-activity-lift-wings-folded` IWM A 18270。824 中队折翼下升降机。
  选它：后向折翼的四个铰点与撑杆最清楚，模型做折翼机构要看这个。

### fulmar
- `fulmar-hms-victorious-hangar-row`（主图）IWM A 7279。机库内中间一排海燕、两侧 Albacore。
  选它：双座串列舱盖 + 短机头，与 Albacore 的区分度比空中照高得多；机库净高余量直接可量。
- `fulmar-hms-victorious-wings-folded-deck` IWM A 7977。斯卡帕湾逆光折翼。
  选它：折翼后翼前端上翻角度。缺点已写进 note（曝光偏暗）。

### sea-gladiator
- `sea-gladiator-hms-victorious-landing`（主图）IWM A 6974。着舰钩放下接近胜利号。
  选它：全型号唯一舰上影像，钩架是全站最想要的细节。
- `sea-gladiator-malta-faith-n5520` IWM ZZZ 3915E，1940-09。马耳他 N5520「Faith」。
  选它：三机小队唯一存世机的地面全景。note 明确写了「不在舰上」+ 换发换桨的差异。
  放弃：`Category:Gloster Sea Gladiator` 全库只有 3 件，第 3 件是 1531 px 的机队合影，信息量不如上面两张。

### corsair
- `corsair-hms-formidable-ranged-deck`（主图）IWM A 24787，1944-07。可畏号甲板列队，FAA 涂装。
  选它：满足「FAA 涂装 + 航母甲板」双条件的最好一张，系留间距可量。
- `corsair-hms-victorious-wings-folding` IWM A 23036。着舰后原地折翼，左右翼对比。
  选它：倒海鸥翼折线 + 折叠后高度。
  放弃：`A20997`（光辉号着舰）与 `A24278`（光辉号机库）——**已被 `data/images.yaml` 以 ship:illustrious 收录**，再登记就是同一张图进两次。另有 `Corsair on outrigger aboard HMS Khedive` 分辨率仅 800 px 且说明称该舰并不使用 Corsair，未取。

### avenger
- `avenger-hms-illustrious-bombing-up`（主图）IWM A 24250，1944-05-17。光辉号挂弹。
  选它：弹舱开口 + 挂架 + 起落架支柱同框，腹部结构最清楚。
- `avenger-hms-trumpeter-catapult` IWM A 25377。846 中队弹射起飞。
  选它：唯一拍到「刚离弹射器」的姿态，与挂弹图互补。

### walrus
- `walrus-hms-prince-of-wales-catapult-deck`（主图）IWM A 3868。吊离弹射甲板，旁边是双联 5.25 in。
  选它：机库门高度、吊臂摆幅、炮塔射界三者同框，战列舰航空设施的空间关系最直观。
- `walrus-hms-mauritius-catapult-launch` IWM A 9272。弹射离舰瞬间。
  选它：与上一条正好覆盖弹射器的「吊放 / 弹射」两端。
  放弃：`A100`（Rodney 吊上弹射器）与 `A15442`（KGV 回收）——前者与威尔士亲王那张作业相同、信息重复；后者是 KGV 的吊放，与本站 KGV 页已有的船体照不构成新的机型信息。

### seafox
- `seafox-hms-canton-alighting`（主图）IWM A 6654。广州号弹射侦察后落水。
- `seafox-fitters-at-work-maharagama` IWM A 22229。锡兰检修，正面结构。
  **说明**：`Category:Fairey Seafox` 全库 4 件，能用的只有这 2 件（另 1 件是 355 px 机型小图、1 件是 1938 年百慕大场地照）。全库 `insource:"Seafox"` 检索到的都是现代无人潜航器同名件。**舰上甲板/弹射器上的海狐式影像在 Commons 上不存在**，已在 note 里写明「此处不给不存在的场景」。

### arado-196
- `arado-196-gneisenau-aboard`（主图）USN NH 83610，约 1940。格奈森瑙号弹射器上整机。
  选它：全库唯一把「德舰弹射器 + 整机 + 吊臂」拍全的一张。note 里写明格奈森瑙属沙恩霍斯特级，与俾斯麦级布置不同，不可照搬尺寸。
- `arado-196-catapult-admiral-scheer` USN NH 71324，1942。舍尔上将号，T3+EK / Wk.Nr. 196 0232。
  **说明**：Commons `Category:Arado Ar 196` 里没有提尔皮茨号本舰的影像（全库 `insource:"Arado 196 Tirpitz"` 只命中 1 份无关 PDF）。按红线不拿姊妹舰冒充本舰，因此只归到机型。Bundesarchiv 的那两件（Bild 101II-MW-1949-03 / MW-6081-11）虽是 CC BY-SA 3.0 de 可作 B 档，但都是巡洋舰上的「装载/停放」，信息量不如这两张 NHHC 的 A 档弹射器照，且能全批保持 A 档，未取。
  放弃：`Ar 196 catapult test 1947 NAN8-47`（战后美方测试，非德舰作战状态）。

### flycatcher
- `flycatcher-1923-prototype-n164`（主图）IWM ATP 430B，1923。整机四分之三侧后。
- `flycatcher-401-flight-hms-eagle` PD-UKGov，1930。低空掠过鹰号甲板。
  **说明**：`Category:Fairey Flycatcher` 全库 11 件，其中 2 件是 GFDL 1.2、2 件是复制品（Duxford 1990s），只剩上述 2 件历史照。**胡德号本舰搭载捕蝇鸟式的影像未在 Commons 检出**（`Category:HMS Hood (51)` 无舰载机子类，`insource:"Flycatcher" insource:"Hood"` 命中全为鸟类图册），故只归到机型。N164 是否为原型已在 note 里标出（Commons 另一件把 N164 标作第二架原型机）。

### fairy-iiif
- `fairy-iiif-hms-furious-landing`（主图）USN Naval Historical Center。费雷 IIIF 着舰暴怒号，1930 年代初，高架拦阻索。
  **说明**：`Category:Fairey IIIF` 为空分类；`Category:Fairey III` 22 件中，能用的只有这一件（另有智利、阿根廷各一件，分辨率 400/250 px 以下，且非英国舰载）。胡德号本舰影像同样未检出。原始落盘即 740 px，未再缩放，已在 note 中说明。

## 授权核对

- 全部 19 条 `LicenseShortName` / `UsageTerms` 均为 `Public domain`，`license_tier: A`。
- 17 条走 IWM 判例：`credit` 写 IWM 编号，`note` 写「原件藏 IWM，Commons 副本标 PD，按 §5.4 作 A 档归档；IWM 官网对其网站副本另适用非商业条款，本站引用 Commons 的公有领域版本」。
- 2 条 Ar 196 + 1 条费雷 IIIF 是 `PD-USGov-Military-Navy`（NHHC 系列），A 档，不需要 IWM 句。
- 1 条 `flycatcher-401-flight-hms-eagle` 是 `PD-UKGov`（已核 wikitext 模板，Crown Copyright 过期）。
- C 档 0 条；没有任何 IWM 官网截取件、没有 SDASM NoC 件、没有 editorial use only 件。

## 去重核对

- 19 个 `source_url` 与 `data/images.yaml`（124 条）及 `work/imgfrag/*.yaml` 现有分片**零交集**。
- 19 个 `file` 与磁盘一一对应，无「磁盘有但未登记」也无「登记了但磁盘没有」。
- 19 个 `id` 与 `data/images.yaml` 的 124 条零撞车。

## 一处需要主会话知道的冲突

`data/images.yaml` 里已有 `illustrious-1943-corsair-landing`（IWM A 20997）与 `illustrious-1944-hangar-corsairs`（IWM A 24278），都是 `ship:illustrious` 的海盗式照片。本分片**有意没有**把它们再登记一遍到 `weapon:corsair`——同一张图挂两个 subject 会构成「同一张图登记两次」。海盗式改用另外两张未被收录的 FAA 舰上照。

## 校验输出

脚本 `work/imgfrag/check-aircraft.py`，全量输出见 `work/imgfrag/check-aircraft.txt`：

```
  arado-196      2 条  主图 ['arado-196-gneisenau-aboard']
  avenger        2 条  主图 ['avenger-hms-illustrious-bombing-up']
  corsair        2 条  主图 ['corsair-hms-formidable-ranged-deck']
  fairy-iiif     1 条  主图 ['fairy-iiif-hms-furious-landing']
  flycatcher     2 条  主图 ['flycatcher-1923-prototype-n164']
  fulmar         2 条  主图 ['fulmar-hms-victorious-hangar-row']
  sea-gladiator  2 条  主图 ['sea-gladiator-hms-victorious-landing']
  seafox         2 条  主图 ['seafox-hms-canton-alighting']
  swordfish      2 条  主图 ['swordfish-hms-victorious-bismarck-strike']
  walrus         2 条  主图 ['walrus-hms-prince-of-wales-catapult-deck']

  OK   YAML 可解析（safe_load 成功）
  OK   顶层键唯一且为 images
  OK   条目数：19
  OK   title 全部为块式（无 title: { ... } 流式写法）
  OK   data/images.yaml 现有 id 数：124
  WARN ×13  宽度不在 120/250/330/500/960/1280/1920/3840 档位表内
  FAIL 0
结果：19 条记录，OK 5，WARN 13，FAIL 0
PASS
```

13 条 WARN 全部是同一类：源图本身小于 1280 px（IWM 那批 800 px 是 Commons 归档尺寸上限），站内落盘即源尺寸、未缩放，因此宽度落在档位表外。这与 `data/images.yaml` 里已有的 `37mm-sk-c30-drache-twin-mount`（800 px）等条目处理方式一致，属预期。

另用**站点自身的解析器**再验一次（`src/lib/data.ts:55` 用的是 `yaml` 包）：

```
$ node -e "...YAML.parse(fs.readFileSync('work/imgfrag/img-aircraft.yaml','utf8'),{uniqueKeys:false})"
keys: ["images"]   n: 19   probs: []    ← 字段齐、无多余键、title 双语完整、primary 全为布尔
```

脚本：`work/imgfrag/check-aircraft-node.py`，输出：`work/imgfrag/check-node.txt`。

## 遗留

- `data/images.yaml` 没有动，等主会话合并。
- `fail` 为 0，可合并。
