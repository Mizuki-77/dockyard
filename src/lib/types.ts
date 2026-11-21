// ============================================================================
// 共享类型 —— 服务端（build）与浏览器（时间轴交互）都要用，故独立成文件。
// ============================================================================

export type Lang = 'zh' | 'en';

export interface BiText {
  zh: string;
  en?: string;
}

export interface Fact {
  field: string;
  value: unknown;
  unit?: string;
  src: string[];
  valid: { from?: string | number | Date; to?: string | number | Date };
  confidence?: 'A' | 'B' | 'C';
  note?: string;
  qual?: Record<string, string>;
  about?: string;
  /**
   * 这条 fact 不进对比器的优劣判定。默认缺省 = 可比。
   *
   * 只在**来源自己承认口径不是该字段要求的那个**时才用，典型是
   * 胡德号的 displacement.standard = 42,670（navypedia 自己写的是 "normal"）。
   * 数值照样显示、照样可以追溯，但对比器不能拿它排高低——否则会把
   * 「口径不同的两个数」当作「同一件事的两种说法」，正是本站存在的理由。
   *
   * 不要拿它当「数据可疑」的垃圾桶：值本身没问题，是口径对不上。
   */
  comparable?: boolean;
}

export interface FieldDef {
  id: string;
  label: BiText;
  type: string;
  unit: string | null;
  group: string;
  compare: boolean;
  better: 'higher' | 'lower' | 'context' | 'none';
  values?: string[];
  qual_keys?: string[];
  qual_values?: Record<string, string[]>;
  note?: string;
  /**
   * 这个字段挂在哪些实体上。缺省 = [class, ship]（舰体字段）。
   * 对比器只取含 class / ship 的那些 —— weapon / mount / image / kit
   * 的字段属于另一套实体（`weapon.bore` 之类），横向比舰时不能混进来。
   */
  applies_to?: string[];
  /**
   * 同一时间窗内允许多条并存（不同型号各占一条），校验器不判它们为分歧。
   * 例：sensors.radar.installed —— 一艘船同时装三型雷达是常态。
   */
  multi?: boolean;
}

export interface SourceDef {
  id: string;
  title: string;
  url: string;
  type: string;
  tier: 'A' | 'B' | 'C' | 'D' | 'E';
  role: string[];
  operator?: string;
  lang?: string;
  access?: string;
  ua?: string;
  status?: 'ok' | 'not_fetched' | 'blocked' | 'gone';
  fetched?: string;
  license?: string;
  note?: string;
  local_copy?: string;
}

export interface TierDef {
  label: BiText;
  desc: string;
}

export interface Position {
  id: string;
  claim: BiText;
  held_by: string[];
  evidence?: string;
  source_refs?: string[];
}

export interface Narrative {
  id: string;
  question: BiText;
  positions: Position[];
  status: 'disputed' | 'settled' | 'minority';
  current_consensus?: string | null;
  note?: string;
}

export interface ShipFile {
  id: string;
  name: BiText;
  class?: string;
  note?: string;
  open_ended_note?: string;
  facts: Fact[];
}

export interface ClassFile {
  id: string;
  name: BiText;
  class_of?: string[];
  note?: string;
  open_ended_note?: string;
  facts: Fact[];
}

// ---------------------------------------------------------------- 图片

export interface ImageRec {
  id: string;
  file?: string;
  title: BiText;
  /** ship:<id> / weapon:<id> / battle:<id> / general */
  subject: string;
  part?: string;
  view?: string;
  date?: string;
  license: string;
  license_tier: 'A' | 'B' | 'C';
  license_raw?: string;
  author?: string;
  credit?: string;
  source_url?: string;
  download_url?: string;
  width?: number;
  height?: number;
  note?: string;
  /** 人工指定为门面图。不给就按 A 档优先 + 落盘顺序退化。 */
  primary?: boolean;
}

export interface ImageRegFile {
  version?: number;
  updated?: string;
  note?: string;
  images: ImageRec[];
}

// ---------------------------------------------------------------- 战役

export interface BattleShip {
  name: string;
  /** 指向 data/ships/<id>.yaml。没有这一项时战役页只显示纯文本，不可点 */
  ship_id?: string;
  role?: BiText;
  /**
   * 关于这场战斗里这一艘舰的补充说明。
   * 目前主要用来写「本站尚未收录该舰单页」，让读者知道那不是漏做了链接，
   * 而不是看到一个点不开的舰名去猜。
   */
  note?: string;
}

export interface Belligerent {
  side: 'axis' | 'allies' | 'neutral' | string;
  label: BiText;
  ships: BattleShip[];
}

export interface ForceLine {
  side: string;
  guns?: BiText;
  note?: BiText;
}

export interface BattleEvent {
  /** 战役内的时间标记，'05:52' 或 '05:52:30'。同一天内不需要日期。 */
  time?: string;
  text: BiText;
  src: string[];
  /**
   * 关键节点标记。事件流支持「概览 / 逐条」两种密度：
   * 概览只显示 major: true 的条目，逐条显示全部。
   *
   * 为什么不按时间间隔自动抽稀：中途岛那种「一小时内六波攻击」的段落，
   * 抽稀会把转折点砍掉、留下无关紧要的相邻条。**哪几条是骨架，只有写的人知道。**
   * 不标的话默认在概览里隐藏；一场战斗至少要有 3–5 条 major，否则概览视图就是空的。
   */
  major?: boolean;
}

export interface BattleLoss {
  side: string;
  ships_lost?: BiText;
  killed?: number;
  survivors?: number;
  note?: BiText;
}

export interface BattleFile {
  id: string;
  name: BiText;
  date: { from: string | number; to?: string | number | null };
  period?: BiText;
  /**
   * 海区：atlantic / north_sea / mediterranean / indian_ocean / pacific /
   * arctic / baltic / other。给「海战历史」左树做第一层分组用。
   *
   * 不能从 location 文本里猜：location 是给人读的一句话
   *（「丹麦海峡，格陵兰与冰岛之间」），拿它当分组键会把同一片海切碎。
   */
  theater?: string;
  location?: BiText;
  coordinates?: string;
  scale?: BiText;
  summary?: BiText;
  belligerents?: Belligerent[];
  forces?: ForceLine[];
  timeline: BattleEvent[];
  hits_received?: BattleEvent[];
  consequences?: BattleEvent[];
  losses?: BattleLoss[];
  outcome?: BiText;
  narrative_refs?: string[];
  /** 所属行动（战役系列）的 id，如 'rheinubung'。 */
  operation?: string;
}

// ---------------------------------------------------------------- 战役系列

/**
 * 战役系列：把同一场作战里先后发生的几场战斗串成一条线。
 *
 * 与 BattleFile 的区别是「层级」不是「内容」——德国海军把一次出击称为一个
 * Unternehmen（行动），莱茵演习里包含丹麦海峡交战、追击、最终战三个环节，
 * 三者各有独立的参战兵力和判决，硬塞进一个时间轴会变成一锅粥。
 * 所以 series 只存「顺序 + 每一站的定位」，战斗本身仍归 battles。
 */
export interface OperationPhase {
  /** 指向 data/battles/<id>.yaml；为空时这一站还没有独立战史页。 */
  battle?: string;
  label: BiText;
  date: { from: string | number; to?: string | number | null };
  summary: BiText;
  src?: string[];
}

export interface OperationFile {
  id: string;
  name: BiText;
  /** 德方行动代号原文，如 Rheinübung。 */
  codename?: string;
  date: { from: string | number; to?: string | number | null };
  belligerents?: Belligerent[];
  summary?: BiText;
  objective?: BiText;
  phases: OperationPhase[];
  outcome?: BiText;
  forces?: ForceLine[];
  narratives?: string[];
  src?: string[];
}

// ---------------------------------------------------------------- 舰艇正文

export interface ArticlePara {
  /**
   * 小标题。**是字符串，不是 BiText** —— 页面模板直接 `{p.heading}` 渲染，
   * 写成 `{ zh: ..., en: ... }` 会渲染成 [object Object]。
   * 现有 5 篇舰艇正文全是字符串，此为其约定。
   */
  heading?: string;
  text: BiText;
  src?: string[];
}

export interface ArticleEvent {
  date: string | number;
  text: BiText;
  src?: string[];
}

export interface ArticleSection {
  id: string;
  title: BiText;
  range?: { from?: string | number | null; to?: string | number | null };
  lead?: BiText;
  events: ArticleEvent[];
}

export interface ArticleFile {
  ship: string;
  updated?: string;
  intro: {
    lead?: BiText;
    paragraphs?: ArticlePara[];
  };
  history: ArticleSection[];
}

// ---------------------------------------------------------------- 武器正文

/**
 * 武器条目正文。结构与舰艇正文同形（简介段落 + 历史分节），
 * 但用 weapon 而不是 ship 作 key —— 武器是独立实体，
 * 同一门炮装在三艘舰上也只有这一份正文。
 */
export interface WeaponArticleFile {
  weapon: string;
  updated?: string;
  intro: {
    lead?: BiText;
    paragraphs?: ArticlePara[];
  };
  /**
   * 武器不一定有「历史」意义上的服役史（很多炮从设计到退役横跨几十年，
   * 中间没有可拆的战役节点），所以这一段允许为空，
   * 但页面会明确写「本站尚未整理该武器的服役史」，不留白块。
   */
  history?: ArticleSection[];
  /** 派生自哪些舰级 / 出自哪个国家，用于面包屑与交叉链接 */
  nations?: string[];
}

