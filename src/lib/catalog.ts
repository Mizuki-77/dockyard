// ============================================================================
// 本站分类表 —— 不进 data/
// ----------------------------------------------------------------------------
// 为什么要单独放这里，而不是写进 data/classes/*.yaml 的 fact：
//
// 「主炮 / 副炮 / 防空炮」不是史料里的字段，是**本站给模型制作者做的检索分类**。
// 同一门 5.25 in 在英舰上既是副炮又是高平两用炮，皇家海军自己的文件里叫
// "secondary armament" 或 "HA/LA mounting"，并没有一个「role」栏。
// 把它写成 fact 就等于把本站的推断塞进数据层，违反框架 §两条红线 的第二条
// （推断值不进 data/，只记布尔事实）。
//
// 所以：data/ 里只留 weapon.category（naval_gun / anti_aircraft_gun / torpedo …，
// 这是有出处的粗类），下面这张表负责把「粗类 + 型号」映射成树上的位置。
// 表格改了不影响任何一条数据的可信度，页面也会标明这是本站分类。
//
// 新增武器时：先看 ROLE_BY_WEAPON 有没有登记；没有就按 category 退化，
// 退化结果会进「其他」，页面会显示出来 —— 不会静默消失。
// ============================================================================

/** 武器树的第一层。顺序即显示顺序。 */
export type WeaponRole =
  | 'main_battery'
  | 'secondary_battery'
  | 'anti_aircraft'
  | 'torpedo'
  | 'rocket'
  | 'radar'
  | 'fire_control'
  | 'aircraft'
  | 'other';

export const ROLE_ORDER: WeaponRole[] = [
  'main_battery',
  'secondary_battery',
  'anti_aircraft',
  'torpedo',
  'rocket',
  'radar',
  'fire_control',
  'aircraft',
  'other',
];

export const ROLE_LABEL: Record<WeaponRole, { zh: string; en: string; hint: string }> = {
  main_battery: {
    zh: '主炮',
    en: 'Main battery',
    hint: '对舰主武装。战列舰一般是 14–38 cm 的重炮，装在装甲炮塔里。',
  },
  secondary_battery: {
    zh: '副炮',
    en: 'Secondary battery',
    hint: '对舰副武装，多数同时具备一定对空能力（高平两用）。',
  },
  anti_aircraft: {
    zh: '防空炮',
    en: 'Anti-aircraft',
    hint: '专职对空。从 2 cm 机关炮到 10.5 cm 重型高炮都在这层。',
  },
  torpedo: {
    zh: '鱼雷',
    en: 'Torpedo',
    hint: '舰载鱼雷兵器。战列舰上的鱼雷管在二战中争议很大。',
  },
  rocket: {
    zh: '火箭',
    en: 'Rocket',
    hint: '无制导火箭兵器，如英制 UP 防空火箭。',
  },
  radar: {
    zh: '雷达',
    en: 'Radar',
    hint: '对空搜索、对海搜索、炮术雷达。型号按英/德命名体系区分。',
  },
  fire_control: {
    zh: '火控',
    en: 'Fire control',
    hint: '射击指挥仪、测距仪、稳定瞄准装置。它决定炮打不打得准。',
  },
  aircraft: {
    zh: '舰载机',
    en: 'Aircraft',
    hint: '舰载机型。航母的战斗力本体，也是战列舰弹射器上的侦察机。',
  },
  other: {
    zh: '其他',
    en: 'Other',
    hint: '未归类，或本站分类表还没登记的新条目。',
  },
};

/**
 * 单件武器的分类。
 *
 * 判据不是「历史上怎么叫」，是「模型制作者会把它放在模型哪个部位」：
 * 一个 10.5 cm SK C/33 的模型件属于上层建筑两侧的高炮平台，
 * 所以进「防空炮」而不是「副炮」，哪怕它同时承担对舰任务。
 */
const ROLE_BY_WEAPON: Record<string, WeaponRole> = {
  // ---- 德国 ----
  '38cm-sk-c34': 'main_battery',
  '15cm-sk-c28': 'secondary_battery',
  '10_5cm-sk-c33': 'anti_aircraft', // 重型高炮，双联 LC/37 炮座
  '37mm-sk-c30': 'anti_aircraft',
  '20mm-c30': 'anti_aircraft',
  '20mm-c38': 'anti_aircraft', // 含四联 Vierling
  'g7a-t1': 'torpedo',

  // ---- 英国 ----
  '15in-42-mk1': 'main_battery', // 胡德
  '14in-45-mk7': 'main_battery', // 英王乔治五世级
  '525in-50-mk1': 'secondary_battery', // 高平两用副炮
  '4_5in-qf-mk3': 'anti_aircraft', // 光辉级舷台炮，主要对空
  '4in-bofors': 'anti_aircraft',
  '2pdr-mk8': 'anti_aircraft', // 八联 pom-pom
  '40mm-bofors': 'anti_aircraft',
  '20mm-oerlikon': 'anti_aircraft',
  'up-rocket': 'rocket',
};

/** 粗类兜底：型号没登记时按 weapon.category 退化。 */
const ROLE_BY_CATEGORY: Record<string, WeaponRole> = {
  naval_gun: 'secondary_battery', // 没登记的主力炮会落这里，页面标「其他」
  coastal_gun: 'other',
  anti_aircraft_gun: 'anti_aircraft',
  torpedo: 'torpedo',
  depth_charge: 'other',
  mine: 'other',
  rocket: 'rocket',
  radar: 'radar',
  fire_control: 'fire_control',
  aircraft: 'aircraft',
  other: 'other',
};

export function roleOf(weaponId: string, categoryValue?: unknown): WeaponRole {
  const direct = ROLE_BY_WEAPON[weaponId];
  if (direct) return direct;
  if (typeof categoryValue === 'string') {
    const byCat = ROLE_BY_CATEGORY[categoryValue];
    if (byCat) return byCat;
  }
  return 'other';
}

/** 该分类是不是本站推断出来的（用于页面上打标）。 */
export function roleIsCurated(weaponId: string): boolean {
  return Boolean(ROLE_BY_WEAPON[weaponId]);
}

// ---------------------------------------------------------------- 国别

export const NATION_LABEL: Record<string, { zh: string; en: string }> = {
  germany: { zh: '德国', en: 'Germany' },
  united_kingdom: { zh: '英国', en: 'United Kingdom' },
  united_states: { zh: '美国', en: 'United States' },
  japan: { zh: '日本', en: 'Japan' },
  italy: { zh: '意大利', en: 'Italy' },
  france: { zh: '法国', en: 'France' },
  soviet_union: { zh: '苏联', en: 'Soviet Union' },
  other: { zh: '其他', en: 'Other' },
};

export function nationLabel(v?: unknown): { zh: string; en: string } {
  if (typeof v === 'string' && NATION_LABEL[v]) return NATION_LABEL[v];
  return { zh: '未标注', en: 'Unspecified' };
}

// ---------------------------------------------------------------- 海区

/**
 * 海战树的第一层：海区。
 *
 * 为什么不从 location 文本里猜：location 是给人读的一句话
 *（「丹麦海峡，格陵兰与冰岛之间」），拿它做分组键会把同一片海切成七八个组。
 * 所以每份 battle 文件显式写 theater:，这里只负责把它翻译成中文并排序。
 */
export const THEATER_ORDER = [
  'atlantic',
  'north_sea',
  'mediterranean',
  'indian_ocean',
  'pacific',
  'arctic',
  'baltic',
  'other',
];

export const THEATER_LABEL: Record<string, { zh: string; en: string }> = {
  atlantic: { zh: '大西洋', en: 'Atlantic' },
  north_sea: { zh: '北海', en: 'North Sea' },
  mediterranean: { zh: '地中海', en: 'Mediterranean' },
  indian_ocean: { zh: '印度洋', en: 'Indian Ocean' },
  pacific: { zh: '太平洋', en: 'Pacific' },
  arctic: { zh: '北极海域', en: 'Arctic' },
  baltic: { zh: '波罗的海', en: 'Baltic' },
  other: { zh: '其他海域', en: 'Other' },
};

export function theaterLabel(id?: string): { zh: string; en: string } {
  if (id && THEATER_LABEL[id]) return THEATER_LABEL[id];
  return THEATER_LABEL.other!;
}

export function theaterRank(id?: string): number {
  const i = THEATER_ORDER.indexOf(id ?? 'other');
  return i < 0 ? THEATER_ORDER.length : i;
}
