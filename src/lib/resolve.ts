// ============================================================================
// 纯函数层 —— 不碰 fs，服务端与浏览器共用。
// 时间轴交互就是靠这一层在浏览器里重算的，所以这里不能 import 任何 node: 模块。
// ============================================================================
import type {
  BiText,
  ClassFile,
  Fact,
  FieldDef,
  Lang,
  Narrative,
  Position,
  ShipFile,
  SourceDef,
} from './types';

export type {
  BiText,
  ClassFile,
  Fact,
  FieldDef,
  Lang,
  Narrative,
  Position,
  ShipFile,
  SourceDef,
};

// ------------------------------------------------------------- 日期归一

/**
 * YAML 会把 `1939` 读成数字、`1936-07-01` 读成字符串、加引号时还可能读成 Date。
 * 全部归一成 "YYYY" / "YYYY-MM" / "YYYY-MM-DD"。
 */
export function normDate(v: unknown): string | undefined {
  if (v === null || v === undefined || v === '') return undefined;
  if (v instanceof Date) return v.toISOString().slice(0, 10);
  if (typeof v === 'number') return String(v);
  const s = String(v).trim();
  const m = s.match(/^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?/);
  if (!m) return s;
  return m[3] ? `${m[1]}-${m[2]}-${m[3]}` : m[2] ? `${m[1]}-${m[2]}` : m[1];
}

/** 把 YYYY / YYYY-MM / YYYY-MM-DD 补成可直接比较的整数 YYYYMMDD。 */
export function dateNum(d: string | undefined, edge: 'start' | 'end'): number {
  if (!d) return edge === 'start' ? 0 : 99999999;
  const p = d.split('-').map(Number);
  const y = p[0] ?? 0;
  const mo = p[1] ?? (edge === 'start' ? 1 : 12);
  const da = p[2] ?? (edge === 'start' ? 1 : 28);
  return y * 10000 + mo * 100 + da;
}

/** YYYYMMDD 整数 → "YYYY-MM-DD"。 */
export function fromNum(n: number): string {
  const y = Math.floor(n / 10000);
  const m = Math.floor((n % 10000) / 100);
  const d = n % 100;
  return `${y}-${String(m).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
}

/** 展示用。接受 YAML 里可能出现的三种类型（string / number / Date）：
 *  YAML 把 `1939` 读成数字、`1936-07-01` 读成字符串，直接打印会得到 1939 与
 *  1936-07-01 两种精度混排。统一走 normDate。 */
export function displayDate(d: unknown): string {
  return normDate(d) ?? '';
}

// ------------------------------------------------------------- 解析与继承

export interface ResolvedFact extends Fact {
  from: string | undefined;
  to: string | undefined;
  /** 这条 fact 来自单舰还是舰级 */
  origin: 'ship' | 'class';
}

export function toResolved(f: Fact, origin: 'ship' | 'class'): ResolvedFact {
  return {
    ...f,
    from: normDate(f.valid?.from),
    to: normDate(f.valid?.to),
    src: f.src ?? [],
    origin,
  };
}

/** 某舰的全部 fact（单舰 + 舰级），不分字段。 */
export function allFacts(ship: ShipFile, cls?: ClassFile): ResolvedFact[] {
  const own = (ship.facts ?? []).map((f) => toResolved(f, 'ship'));
  const inherited = (cls?.facts ?? []).map((f) => toResolved(f, 'class'));
  return [...own, ...inherited];
}

/**
 * 解析顺序（框架 §3.6）：单舰 fact 命中即覆盖舰级，**不与舰级值构成分歧**。
 * 这里把「单舰覆盖」与「真分歧」分开：
 *   - 若某字段在单舰层有命中，则只在单舰层内找分歧；
 *   - 单舰层无命中才回落到舰级层。
 */
export function candidatesAt(
  facts: ResolvedFact[],
  field: string,
  t: number,
  about?: string,
): ResolvedFact[] {
  const hits = facts.filter((f) => {
    if (f.field !== field) return false;
    if ((f.about ?? '') !== (about ?? '')) return false;
    const a = dateNum(f.from, 'start');
    const b = dateNum(f.to, 'end');
    return a <= t && t <= b;
  });
  const fromShip = hits.filter((f) => f.origin === 'ship');
  return fromShip.length > 0 ? fromShip : hits;
}

// ------------------------------------------------------------- 主值选取

export interface PrimaryDeps {
  /** source id -> 证据层级分数（A=4 … E=0） */
  tierOf: (srcId: string) => number;
  /** source id -> 采集日期，用于"新者优先" */
  fetchedOf: (srcId: string) => string;
}

/**
 * 主值选取（框架 §3.9）：
 *   证据层级高者优先 → 层同则口径明确者优先（有 note 说明者优先）→
 *   再同则采集时间新者优先 → 仍平按 source id 字母序（构建可复现）。
 */
export function pickPrimary(items: ResolvedFact[], deps: PrimaryDeps): ResolvedFact | null {
  if (items.length === 0) return null;
  if (items.length === 1) return items[0];

  const scored = items.map((f) => {
    const tier = f.src.length === 0 ? -1 : Math.max(...f.src.map((s) => deps.tierOf(s)));
    const fetched =
      f.src
        .map((s) => deps.fetchedOf(s))
        .sort()
        .pop() ?? '';
    return {
      f,
      tier,
      hasNote: f.note ? 1 : 0,
      fetched,
      key: [...f.src].sort().join(','),
    };
  });

  scored.sort((a, b) => {
    if (a.tier !== b.tier) return b.tier - a.tier;
    if (a.hasNote !== b.hasNote) return b.hasNote - a.hasNote;
    if (a.fetched !== b.fetched) return a.fetched < b.fetched ? 1 : -1;
    return a.key.localeCompare(b.key);
  });
  return scored[0].f;
}

/** 同一时间窗出现两个不同值 = 分歧（框架 §3.2 规则 4）。 */
export function isDisputed(items: ResolvedFact[]): boolean {
  if (items.length < 2) return false;
  const vals = new Set(items.map((f) => JSON.stringify(f.value)));
  return vals.size > 1;
}

/** 只要出现两个不同的 (from,to) 窗口，这个字段就是"会随时间变"的。 */
export function hasTimeVariance(items: ResolvedFact[]): boolean {
  const keys = new Set(items.map((f) => `${f.from ?? ''}~${f.to ?? ''}`));
  return keys.size > 1;
}

// ------------------------------------------------------------- 格式化

const UNIT_LABEL: Record<string, string> = {
  t: 't',
  kg: 'kg',
  m: 'm',
  cm: 'cm',
  mm: 'mm',
  kn: 'kn',
  mps: 'm/s',
  nmi: 'nmi',
  km: 'km',
  hp: 'hp',
  kW: 'kW',
  deg: '°',
  celsius: '°C',
  s: 's',
  rpm: 'rpm',
  atm: 'atm',
  dm3: 'dm³',
  count: '',
  persons: '人',
  ratio: '',
  pct: '%',
  date: '',
};

export function unitLabel(u?: string | null): string {
  if (!u) return '';
  return UNIT_LABEL[u] ?? u;
}

const ENUM_LABEL: Record<string, BiText> = {
  battleship: { zh: '战列舰', en: 'Battleship' },
  battlecruiser: { zh: '战列巡洋舰', en: 'Battlecruiser' },
  heavy_cruiser: { zh: '重巡洋舰', en: 'Heavy cruiser' },
  light_cruiser: { zh: '轻巡洋舰', en: 'Light cruiser' },
  armored_cruiser: { zh: '装甲巡洋舰', en: 'Armoured cruiser' },
  protected_cruiser: { zh: '防护巡洋舰', en: 'Protected cruiser' },
  aircraft_carrier: { zh: '航空母舰', en: 'Aircraft carrier' },
  escort_carrier: { zh: '护航航母', en: 'Escort carrier' },
  seaplane_carrier: { zh: '水上机母舰', en: 'Seaplane carrier' },
  destroyer: { zh: '驱逐舰', en: 'Destroyer' },
  destroyer_leader: { zh: '驱逐领舰', en: 'Destroyer leader' },
  torpedo_boat: { zh: '鱼雷艇', en: 'Torpedo boat' },
  frigate: { zh: '护卫舰', en: 'Frigate' },
  corvette: { zh: '轻型护卫舰', en: 'Corvette' },
  submarine: { zh: '潜艇', en: 'Submarine' },
  monitor: { zh: '浅水重炮舰', en: 'Monitor' },
  coastal_defence_ship: { zh: '岸防舰', en: 'Coastal defence ship' },
  minelayer: { zh: '布雷舰', en: 'Minelayer' },
  auxiliary: { zh: '辅助舰', en: 'Auxiliary' },
  other: { zh: '其他', en: 'Other' },
  ww1: { zh: '一战', en: 'First World War' },
  interwar: { zh: '战间期', en: 'Interwar' },
  ww2: { zh: '二战', en: 'Second World War' },
  cold_war: { zh: '冷战', en: 'Cold War' },
  modern: { zh: '现代', en: 'Modern' },
  germany: { zh: '德国', en: 'Germany' },
  united_kingdom: { zh: '英国', en: 'United Kingdom' },
  united_states: { zh: '美国', en: 'United States' },
  japan: { zh: '日本', en: 'Japan' },
  italy: { zh: '意大利', en: 'Italy' },
  france: { zh: '法国', en: 'France' },
  soviet_union: { zh: '苏联', en: 'Soviet Union' },
  china: { zh: '中国', en: 'China' },
  netherlands: { zh: '荷兰', en: 'Netherlands' },
  australia: { zh: '澳大利亚', en: 'Australia' },
  canada: { zh: '加拿大', en: 'Canada' },
  poland: { zh: '波兰', en: 'Poland' },
  norway: { zh: '挪威', en: 'Norway' },
  sweden: { zh: '瑞典', en: 'Sweden' },
  greece: { zh: '希腊', en: 'Greece' },
  turkey: { zh: '土耳其', en: 'Turkey' },
  spain: { zh: '西班牙', en: 'Spain' },
  finland: { zh: '芬兰', en: 'Finland' },
  romania: { zh: '罗马尼亚', en: 'Romania' },
  sunk_by_enemy: { zh: '战沉', en: 'Sunk by enemy' },
  sunk_by_scuttling: { zh: '自沉', en: 'Sunk by scuttling' },
  sunk_by_own_forces: { zh: '己方摧毁', en: 'Sunk by own forces' },
  sunk_cause_disputed: { zh: '沉没原因存在争议', en: 'Sinking cause disputed' },
  scuttled: { zh: '自沉', en: 'Scuttled' },
  scrapped: { zh: '拆解', en: 'Scrapped' },
  preserved: { zh: '保存为博物馆舰', en: 'Preserved' },
  wrecked: { zh: '搁浅损毁', en: 'Wrecked' },
  expended_as_target: { zh: '作为靶舰消耗', en: 'Expended as target' },
  naval_gun: { zh: '舰炮', en: 'Naval gun' },
  coastal_gun: { zh: '岸防炮', en: 'Coastal gun' },
  anti_aircraft_gun: { zh: '高射炮', en: 'AA gun' },
  torpedo: { zh: '鱼雷', en: 'Torpedo' },
  depth_charge: { zh: '深水炸弹', en: 'Depth charge' },
  mine: { zh: '水雷', en: 'Mine' },
  rocket: { zh: '火箭', en: 'Rocket' },
  // 以下三个是 weapon.category 的取值，2026-11-22 补：
  // 首页站内地图按武器类别分组时才发现它们没有中文标签，
  // 页面上会直接显示 radar / aircraft / fire_control 三个英文枚举名。
  radar: { zh: '雷达', en: 'Radar' },
  fire_control: { zh: '火控系统', en: 'Fire control' },
  aircraft: { zh: '舰载机', en: 'Aircraft' },
  twin_turret: { zh: '双联装炮塔', en: 'Twin turret' },
  triple_turret: { zh: '三联装炮塔', en: 'Triple turret' },
  quad_turret: { zh: '四联装炮塔', en: 'Quadruple turret' },
  single_turret: { zh: '单装炮塔', en: 'Single turret' },
  casemate: { zh: '炮廓', en: 'Casemate' },
  open_mount: { zh: '敞开式炮座', en: 'Open mount' },
  shielded_mount: { zh: '带护盾炮座', en: 'Shielded mount' },
  tube: { zh: '发射管', en: 'Tube' },
  rack: { zh: '投放架', en: 'Rack' },
  fore: { zh: '舰首', en: 'Fore' },
  aft: { zh: '舰尾', en: 'Aft' },
  midships: { zh: '舯部', en: 'Midships' },
  port: { zh: '左舷', en: 'Port' },
  starboard: { zh: '右舷', en: 'Starboard' },
  superfiring_fore: { zh: '前部背负', en: 'Superfiring fore' },
  superfiring_aft: { zh: '后部背负', en: 'Superfiring aft' },
  wing: { zh: '舷侧', en: 'Wing' },
  steam_turbine: { zh: '蒸汽轮机', en: 'Steam turbine' },
  steam_reciprocating: { zh: '往复式蒸汽机', en: 'Steam reciprocating' },
  diesel: { zh: '柴油机', en: 'Diesel' },
  diesel_electric: { zh: '柴电', en: 'Diesel-electric' },
  gas_turbine: { zh: '燃气轮机', en: 'Gas turbine' },
  nuclear: { zh: '核动力', en: 'Nuclear' },
  combined_diesel_gas: { zh: '柴燃联合', en: 'CODAG' },
  turbo_electric: { zh: '涡轮电力', en: 'Turbo-electric' },
  all_or_nothing: { zh: '全部或全无', en: 'All or nothing' },
  incremental: { zh: '渐进式', en: 'Incremental' },
  turtle_back: { zh: '龟背式', en: 'Turtle back' },
  german_method: { zh: '德制算法', en: 'German method' },
  usa_uk_method: { zh: '美英制算法', en: 'US/UK method' },
  unknown: { zh: '未知', en: 'Unknown' },
  elevation_only: { zh: '仅俯仰随动', en: 'Elevation only' },
  train_only: { zh: '仅回转随动', en: 'Train only' },
  both: { zh: '俯仰与回转随动', en: 'Both' },
  none: { zh: '无', en: 'None' },
  apc: { zh: '被帽穿甲弹', en: 'APC' },
  ap: { zh: '穿甲弹', en: 'AP' },
  he: { zh: '高爆弹', en: 'HE' },
  he_base_fuze: { zh: '底发引信高爆弹', en: 'HE (base fuze)' },
  he_nose_fuze: { zh: '头发引信高爆弹', en: 'HE (nose fuze)' },
  sap: { zh: '半穿甲弹', en: 'SAP' },
  aa: { zh: '防空弹', en: 'AA' },
  coastal: { zh: '岸防弹', en: 'Coastal' },
  special: { zh: '特种弹', en: 'Special' },
  belt: { zh: '舷侧装甲带', en: 'Belt' },
  upper_belt: { zh: '上装甲带', en: 'Upper belt' },
  lower_belt: { zh: '下装甲带', en: 'Lower belt' },
  deck: { zh: '装甲甲板', en: 'Armour deck' },
  slope: { zh: '倾斜甲板', en: 'Slope' },
  bulkhead: { zh: '舱壁', en: 'Bulkhead' },
  splinter_belt: { zh: '防破片纵壁', en: 'Splinter belt' },
  turret: { zh: '炮塔', en: 'Turret' },
  barbette: { zh: '炮座', en: 'Barbette' },
  conning_tower: { zh: '司令塔', en: 'Conning tower' },
  funnel_uptake: { zh: '烟道', en: 'Funnel uptake' },
  // 航母部位：战列舰的装甲是「带 + 甲板 + 炮塔」，航母的装甲是
  // 「飞行甲板 + 机库侧壁 + 机库甲板」——装甲航母的全部设计争论都落在这三处。
  flight_deck: { zh: '飞行甲板', en: 'Flight deck' },
  hangar_side: { zh: '机库侧壁', en: 'Hangar side' },
  hangar_deck: { zh: '机库甲板', en: 'Hangar deck' },
  magazine: { zh: '弹药库', en: 'Magazine' },
  main: { zh: '主要', en: 'Main' },
  upper: { zh: '上部', en: 'Upper' },
  lower: { zh: '下部', en: 'Lower' },
  face: { zh: '正面', en: 'Face' },
  side: { zh: '侧面', en: 'Side' },
  rear: { zh: '后部', en: 'Rear' },
  roof: { zh: '顶部', en: 'Roof' },
  top: { zh: '上缘', en: 'Top' },
  bottom: { zh: '下缘', en: 'Bottom' },
  splinter: { zh: '防破片', en: 'Splinter' },
  in_production: { zh: '在产', en: 'In production' },
  discontinued: { zh: '停产', en: 'Discontinued' },
  injection: { zh: '注塑', en: 'Injection' },
  resin: { zh: '树脂', en: 'Resin' },
  wood: { zh: '木质', en: 'Wood' },
  photo_etch: { zh: '蚀刻片', en: 'Photo-etch' },
  '3d_print': { zh: '3D 打印', en: '3D print' },
  mixed: { zh: '混合', en: 'Mixed' },
  pd: { zh: '公有领域', en: 'Public domain' },
  cc0: { zh: 'CC0', en: 'CC0' },
  cc_by: { zh: 'CC BY', en: 'CC BY' },
  cc_by_sa: { zh: 'CC BY-SA', en: 'CC BY-SA' },
  non_commercial: { zh: '仅限非商业', en: 'Non-commercial' },
  editorial_only: { zh: '仅限编辑用途', en: 'Editorial only' },
  prohibited: { zh: '不可使用', en: 'Prohibited' },
  bow: { zh: '舰首', en: 'Bow' },
  stern: { zh: '舰尾', en: 'Stern' },
  broadside: { zh: '舷侧', en: 'Broadside' },
  overhead: { zh: '俯视', en: 'Overhead' },
  detail: { zh: '细节', en: 'Detail' },
  underwater: { zh: '水下', en: 'Underwater' },
  superstructure: { zh: '上层建筑', en: 'Superstructure' },
  funnel: { zh: '烟囱', en: 'Funnel' },
  mast: { zh: '桅杆', en: 'Mast' },
  bridge: { zh: '舰桥', en: 'Bridge' },
  aircraft_handling: { zh: '航空作业', en: 'Aircraft handling' },
  catapult: { zh: '弹射器', en: 'Catapult' },
  crane: { zh: '吊车', en: 'Crane' },
  propeller: { zh: '螺旋桨', en: 'Propeller' },
  rudder: { zh: '舵', en: 'Rudder' },
  anchor: { zh: '锚', en: 'Anchor' },
  boat: { zh: '舰载艇', en: 'Boat' },
  hull_side: { zh: '舷侧外板', en: 'Hull side' },
  hull_bottom: { zh: '舰底', en: 'Hull bottom' },
  rp_c32: { zh: 'RP C/32', en: 'RP C/32' },
  rp_c38: { zh: 'RP C/38', en: 'RP C/38' },
  rp_c40: { zh: 'RP C/40', en: 'RP C/40' },
  single: { zh: '整装', en: 'Single' },
};

export function enumLabel(v: string, lang: Lang = 'zh'): string {
  const e = ENUM_LABEL[v];
  if (!e) return v;
  return (lang === 'en' ? e.en : e.zh) ?? e.zh;
}

export function formatValue(v: unknown, lang: Lang = 'zh'): string {
  if (v === null || v === undefined) return '—';
  if (typeof v === 'boolean') return v ? '是' : '否';
  if (typeof v === 'number') {
    if (!Number.isInteger(v)) return String(v);
    // 四位数不当千分位处理：1939 是年份不是 1,939；口径 380 也不该变成 380。
    // 五位数以上（排水量、弹药数）才加分隔符。
    if (Math.abs(v) < 10000) return String(v);
    return v.toLocaleString('en-US');
  }
  if (typeof v === 'string') {
    if (/^\d{4}(-\d{2})?(-\d{2})?$/.test(v)) return v;
    if (ENUM_LABEL[v]) return enumLabel(v, lang);
    return v;
  }
  return JSON.stringify(v);
}

/** 限定词的中文说明，如 { charge_part: 'fore' } → "前段装药"。 */
const QUAL_CTX: Record<string, Record<string, string>> = {
  // charge_part 的 fore/rear 指装药的两个分装段，不是舰首舰尾 —— 不能借用 mount.position 的标签
  charge_part: { fore: '前段装药', rear: '后段装药', main: '主装药', single: '整装药' },
};

export function qualLabel(qual: Record<string, unknown> | undefined, lang: Lang = 'zh'): string {
  if (!qual) return '';
  const parts: string[] = [];
  for (const [k, v] of Object.entries(qual)) {
    const key = String(v);
    const ctx = QUAL_CTX[k];
    const vs = ctx?.[key] ?? enumLabel(key, lang);
    parts.push(vs);
  }
  return parts.join(' · ');
}

/** 长文本（型号全名、注释式取值）按字宽折行，页面不出现横向溢出。 */
const LONG_TEXT = 42;

export function isLongText(s: string): boolean {
  return [...s].length > LONG_TEXT;
}

/** 同一字段的多条 fact 合并成一行显示。
 *
 *  为什么要合并：一门炮的「弹重」按弹种有三条记录（穿甲弹 800 kg、底发引信
 *  高爆弹 800 kg、头发引信高爆弹 800 kg）。逐条铺开会让一个参数占三行，
 *  读者以为那是三个不同的指标；压成一个「800 kg」又把「三种弹都这么重」
 *  这个信息丢了。所以按限定词配对成 `弹种 → 重量`。
 *
 *  争议判定：只有在「一条限定词都没有、值却不同」时才是真争议。
 *  带不同限定词的多值不是争议，是不一样的东西。
 */
export interface MergedRow {
  field: string;
  pairs: { q: string; t: string }[];
  text: string;
  disputed: boolean;
  conf?: string;
}

export function mergeFactRows(
  facts: { field: string; value: unknown; unit?: string; qual?: Record<string, unknown>; confidence?: string }[],
  lang: Lang = 'zh',
): MergedRow[] {
  const byField = new Map<string, typeof facts>();
  for (const f of facts) {
    const arr = byField.get(f.field) ?? [];
    arr.push(f);
    byField.set(f.field, arr);
  }
  return [...byField.entries()].map(([field, fs]) => {
    const pairs = fs.map((f) => ({ q: qualLabel(f.qual, lang), t: formatFact(f, lang) }));
    const allQualified = pairs.every((p) => p.q);
    const distinct = new Set(pairs.map((p) => p.t)).size;
    const conf = fs.find((f) => f.confidence)?.confidence;
    return {
      field,
      // 每条都有限定词就逐条列（弹重三种弹型各一行），值相同也不合并——
      // 「三种弹都是 800 kg」本身是信息，压成一个 800 kg 就丢了。
      pairs: allQualified ? pairs : [],
      text: pairs.map((p) => p.t).join(' / '),
      disputed: allQualified ? false : distinct > 1,
      conf,
    };
  });
}

/** 完整显示：值 + 单位。 */
export function formatFact(f: { value: unknown; unit?: string }, lang: Lang = 'zh'): string {
  const v = formatValue(f.value, lang);
  const u = unitLabel(f.unit);
  return u ? `${v} ${u}` : v;
}
