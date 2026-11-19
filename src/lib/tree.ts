// ============================================================================
// 左树数据装配 —— 两个栏目的三层树
// ----------------------------------------------------------------------------
//   武器与装备   类别 → 国别 → 型号   buildWeaponTree()
//   海战历史     海区 → 年份 → 战斗   buildBattleTree()
//
// 为什么单独成文件：这两套分组逻辑原先在各自的列表页与详情页各写了一遍
// （共 4 份），加一层就得改 4 处，漏一处两边树就不一样。这里收成一份，
// 列表页和详情页都调同一个函数。
//
// 为什么都做成三层：
//   武器 —— 二层树在 48 型之后不够用。防空炮那 8 型里英德各 4，
//   全平铺在一层，读者扫一眼分不出哪些是德国的。
//   海战 —— 用户草图原文就是「按地点 → 按年份」，且同一片海里
//   一年可能有七八场护航战，年份必须能单独折叠。
//
// 国别这一层是**本站的分类**（与 weapon.category 不同，那个有出处），
// 但国别本身来自 fact 的 weapon.nation，是硬数据；
// 海区同理，来自 battle 文件的 theater 字段，不是从 location 文本猜的。
// ============================================================================
import type { BattleFile, WeaponSummary } from './data';
import {
  roleOf,
  ROLE_ORDER,
  ROLE_LABEL,
  nationLabel,
  theaterLabel,
  theaterRank,
  type WeaponRole,
} from './catalog';

/** 三层树的叶子永远是单件武器。 */
export interface WeaponLeaf {
  /** 型号显示名（同一型在不同来源里写法不同时取首个 designation） */
  label: string;
  /** 该型装过哪些舰 / 舰级，写进 title 让鼠标悬停就知道 */
  meta: string;
  href: string;
  /** 同一型在几个来源里登记过，>1 说明参数有多个口径 */
  sources: number;
}

/** 中间层：某个类别下的某个国别。 */
export interface NationNode {
  key: string;
  label: string;
  en: string;
  count: number;
  weapons: WeaponLeaf[];
}

/** 顶层：类别。 */
export interface RoleNode {
  key: WeaponRole;
  label: string;
  en: string;
  hint: string;
  count: number;
  nations: NationNode[];
}

function nationsOf(w: WeaponSummary): string[] {
  return w.nations.length > 0 ? w.nations : ['other'];
}

function leafOf(w: WeaponSummary): WeaponLeaf {
  const owners = [...w.classIds, ...w.shipIds].length;
  return {
    label: w.label,
    meta: owners > 0 ? `${owners} 个来源` : '',
    href: `/weapons/${w.id}`,
    sources: w.sources.length,
  };
}

/**
 * 把武器总表装配成三层树。
 *
 * 一件武器可能同时有多个 nation（比如同型炮在英德两边都有缴获使用记录），
 * 这时它在每个国别下都会出现一次。**这是有意的**：读者按国别找东西时，
 * 不该因为「主国别不是这个」就找不到它。但同一国别下不会重复。
 */
export function buildWeaponTree(all: WeaponSummary[]): RoleNode[] {
  // role -> nation -> weapons
  const byRole = new Map<WeaponRole, Map<string, WeaponSummary[]>>();

  for (const w of all) {
    const role = roleOf(w.id, w.categories[0]);
    if (!byRole.has(role)) byRole.set(role, new Map());
    const byNation = byRole.get(role)!;
    for (const n of nationsOf(w)) {
      if (!byNation.has(n)) byNation.set(n, []);
      byNation.get(n)!.push(w);
    }
  }

  const roles = [...byRole.keys()].sort(
    (a, b) => ROLE_ORDER.indexOf(a) - ROLE_ORDER.indexOf(b),
  );

  return roles.map((role) => {
    const byNation = byRole.get(role)!;
    const nations = [...byNation.entries()]
      .sort((a, b) => nationLabel(a[0]).zh.localeCompare(nationLabel(b[0]).zh, 'zh'))
      .map(([key, list]) => {
        // 同一国别下按型号名排序；用 Map 去重防止一件武器被推两次
        const uniq = [...new Map(list.map((w) => [w.id, w])).values()];
        uniq.sort((a, b) => a.label.localeCompare(b.label, 'zh'));
        return {
          key,
          label: nationLabel(key).zh,
          en: nationLabel(key).en,
          count: uniq.length,
          weapons: uniq.map(leafOf),
        };
      });

    const total = nations.reduce((n, x) => n + x.count, 0);
    return {
      key: role,
      label: ROLE_LABEL[role].zh,
      en: ROLE_LABEL[role].en,
      hint: ROLE_LABEL[role].hint,
      count: total,
      nations,
    };
  });
}

/**
 * 拼音/拉丁字母排序用的国别顺序。
 *
 * 为什么不让中文名直接 localeCompare：`意大利` / `日本` / `法国` / `美国` / `英国` / `德国`
 * 按拼音排是 德(D) 法(F) 美(M) 日(R) 意(Y) 英(Y)，但按 zh 词典序是
 * 德 法 美 日 英 意 —— 后两个反了，读者会觉得乱。所以显式给顺序。
 */
export const NATION_TREE_ORDER = [
  'germany',
  'united_kingdom',
  'united_states',
  'japan',
  'italy',
  'france',
  'soviet_union',
  'other',
];

export function nationRank(id: string): number {
  const i = NATION_TREE_ORDER.indexOf(id);
  return i < 0 ? NATION_TREE_ORDER.length : i;
}

// ---------------------------------------------------------------- 海战树

/** 海战树的叶子：一场战斗。 */
export interface BattleLeaf {
  /** 显示名。年份已经由中间层表达，这里只写战斗名，避免「1941 · 1941 · xxx」 */
  label: string;
  en?: string;
  href: string;
  /** 上级行动名，写进 title 供悬停查看 */
  meta?: string;
  /** 用于排序与「年份下还有几场」的统计 */
  from: string;
}

/** 中间层：某海区下的某一年。 */
export interface YearNode {
  key: string;
  label: string;
  count: number;
  battles: BattleLeaf[];
}

/** 顶层：海区。 */
export interface TheaterNode {
  key: string;
  label: string;
  en: string;
  count: number;
  years: YearNode[];
}

/**
 * 把战斗列表装配成「海区 → 年份 → 战斗」三层树。
 *
 * 跨年战斗的归年规则：按 `date.from` 归，只出现一次。
 * 在两年下各出现一次会让「1942 年有几场」变成假数字——
 * 而年份计数是读者用来判断「这块要不要展开」的依据，不能虚高。
 */
export function buildBattleTree(
  battles: BattleFile[],
  opNameOf: (b: BattleFile) => string | undefined,
): TheaterNode[] {
  const byTheater = new Map<string, Map<string, BattleFile[]>>();

  for (const b of battles) {
    const th = b.theater ?? 'other';
    const y = String(b.date.from).slice(0, 4);
    if (!byTheater.has(th)) byTheater.set(th, new Map());
    const years = byTheater.get(th)!;
    if (!years.has(y)) years.set(y, []);
    years.get(y)!.push(b);
  }

  const theaters = [...byTheater.keys()].sort((a, b) => theaterRank(a) - theaterRank(b));

  return theaters.map((th) => {
    const years = [...byTheater.get(th)!.entries()]
      // 年份用数字序，别用字典序——字典序在跨世纪时会把 "999" 排到 "1000" 后面
      .sort((a, b) => Number(a[0]) - Number(b[0]))
      .map(([y, list]) => {
        const leaves = list
          .slice()
          .sort((a, b) => String(a.date.from).localeCompare(String(b.date.from)))
          .map((b) => ({
            label: b.name.zh,
            en: b.name.en,
            href: `/battles/${b.id}`,
            meta: opNameOf(b),
            from: String(b.date.from),
          }));
        return { key: y, label: y, count: leaves.length, battles: leaves };
      });

    return {
      key: th,
      label: theaterLabel(th).zh,
      en: theaterLabel(th).en,
      count: years.reduce((n, x) => n + x.count, 0),
      years,
    };
  });
}
