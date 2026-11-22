// ============================================================================
// 数据层（构建期）—— 读 data/ 下的 YAML 并附上"取主值需要的外部信息"。
// 这里可以 import node: 模块；纯逻辑全在 resolve.ts，浏览器侧复用那一份。
// ============================================================================
import fs from 'node:fs';
import path from 'node:path';
import YAML from 'yaml';

import type {
  ArticleFile,
  BattleFile,
  BiText,
  ClassFile,
  Fact,
  FieldDef,
  ImageRec,
  ImageRegFile,
  Lang,
  Narrative,
  OperationFile,
  OperationPhase,
  ShipFile,
  SourceDef,
  WeaponArticleFile,
} from './types';

import {
  allFacts,
  candidatesAt,
  dateNum,
  enumLabel,
  formatFact,
  isDisputed,
  normDate,
  pickPrimary,
  toResolved,
  type PrimaryDeps,
  type ResolvedFact,
} from './resolve';

export * from './resolve';
export type { BattleFile, BiText, ClassFile, Fact, FieldDef, ImageRec, Lang, Narrative, ShipFile, SourceDef };
export type { ArticleFile, ArticleSection, ArticleEvent, ArticlePara } from './types';
export type { WeaponArticleFile } from './types';
export type { OperationFile, OperationPhase } from './types';

const ROOT = process.cwd();
const DATA = path.join(ROOT, 'data');

// ------------------------------------------------------------------ 读取

function readYaml<T>(file: string): T | null {
  const p = path.join(DATA, file);
  if (!fs.existsSync(p)) return null;
  return YAML.parse(fs.readFileSync(p, 'utf8'), { uniqueKeys: false }) as T;
}

function readDir<T>(dir: string): T[] {
  const p = path.join(DATA, dir);
  if (!fs.existsSync(p)) return [];
  return fs
    .readdirSync(p)
    .filter((f) => f.endsWith('.yaml') || f.endsWith('.yml'))
    .map((f) => readYaml<T>(path.join(dir, f)))
    .filter((x): x is T => x !== null);
}

// ------------------------------------------------------------- 字段注册表

export interface GroupDef {
  id: string;
  label: BiText;
  order: number;
}

interface FieldRegFile {
  units: Record<string, string>;
  rejected_units?: Record<string, string>;
  namespaces: Record<string, string>;
  groups: GroupDef[];
  fields: FieldDef[];
}

let _reg: FieldRegFile | null = null;

function reg(): FieldRegFile {
  if (!_reg) {
    const r = readYaml<FieldRegFile>('fields.yaml');
    if (!r) throw new Error('data/fields.yaml 缺失');
    _reg = r;
  }
  return _reg;
}

export function getFields(): FieldDef[] {
  return reg().fields;
}

export function getField(id: string): FieldDef | undefined {
  return reg().fields.find((f) => f.id === id);
}

export function getGroups(): GroupDef[] {
  return [...reg().groups].sort((a, b) => a.order - b.order);
}

export function getGroup(id: string): GroupDef | undefined {
  return reg().groups.find((g) => g.id === id);
}

export function getUnits() {
  return reg().units;
}

export function getNamespaces() {
  return reg().namespaces;
}

// ------------------------------------------------------------- 来源登记表

interface SourcesRegFile {
  tiers: Record<string, { label: BiText; desc: string }>;
  roles?: Record<string, { label?: BiText; desc?: string }>;
  sources: SourceDef[];
  todo?: string[];
}

let _src: SourcesRegFile | null = null;

function srcReg(): SourcesRegFile {
  if (!_src) {
    const r = readYaml<SourcesRegFile>('sources.yaml');
    if (!r) throw new Error('data/sources.yaml 缺失');
    _src = r;
  }
  return _src;
}

export function getSources(): SourceDef[] {
  return srcReg().sources;
}

export function getSource(id: string): SourceDef | undefined {
  return srcReg().sources.find((s) => s.id === id);
}

export function getTiers(): { id: string; label: BiText; desc: string }[] {
  const t = srcReg().tiers;
  return Object.entries(t).map(([id, v]) => ({ id, label: v.label, desc: v.desc }));
}

export function getSourceRoles() {
  return srcReg().roles ?? {};
}

const TIER_RANK: Record<string, number> = { A: 4, B: 3, C: 2, D: 1, E: 0 };

/** pickPrimary 需要的外部信息（注册表在构建期只读一次）。 */
export const deps: PrimaryDeps = {
  tierOf: (id) => TIER_RANK[getSource(id)?.tier ?? 'E'] ?? 0,
  fetchedOf: (id) => getSource(id)?.fetched ?? '',
};

// ------------------------------------------------------------------ 舰艇

export function getShips(): ShipFile[] {
  return readDir<ShipFile>('ships').sort((a, b) => a.id.localeCompare(b.id));
}

export function getShip(id: string): ShipFile | undefined {
  return getShips().find((s) => s.id === id);
}

export function getClasses(): ClassFile[] {
  return readDir<ClassFile>('classes').sort((a, b) => a.id.localeCompare(b.id));
}

export function getClass(id: string): ClassFile | undefined {
  return getClasses().find((c) => c.id === id);
}

// ------------------------------------------------------------------ 叙事

export type ShipNarrative = Narrative & { ship: string };

export function getNarratives(shipId?: string): ShipNarrative[] {
  const files = readDir<{ ship: string; narratives: Narrative[] }>('narratives');
  const all = files.flatMap((f) =>
    (f.narratives ?? []).map((n) => ({ ...n, ship: f.ship })),
  );
  return shipId ? all.filter((n) => n.ship === shipId) : all;
}

// ------------------------------------------------------------------ 战役

export function getBattles(): BattleFile[] {
  return readDir<BattleFile>('battles').sort((a, b) => String(a.date?.from ?? '').localeCompare(String(b.date?.from ?? '')));
}

export function getBattle(id: string): BattleFile | undefined {
  return getBattles().find((b) => b.id === id);
}

// -------------------------------------------------------------- 战役系列

export function getOperations(): OperationFile[] {
  return readDir<OperationFile>('operations').sort((a, b) =>
    String(a.date?.from ?? '').localeCompare(String(b.date?.from ?? '')),
  );
}

export function getOperation(id: string): OperationFile | undefined {
  return getOperations().find((o) => o.id === id);
}

/** 某场战役属于哪个系列。没写 operation 字段的返回 undefined。 */
export function operationOf(battleId: string): OperationFile | undefined {
  return getOperations().find((o) => (o.phases ?? []).some((p) => p.battle === battleId));
}

/** 把系列里的每一站解析成「完整战斗对象 + 定位」，供总览页与导航用。 */
export interface ResolvedPhase {
  phase: OperationPhase;
  battle?: BattleFile;
}

export function resolvePhases(op: OperationFile): ResolvedPhase[] {
  return (op.phases ?? []).map((p) => ({
    phase: p,
    battle: p.battle ? getBattle(p.battle) : undefined,
  }));
}

// ------------------------------------------------------- 单舰视图装配

export interface FactView {
  field: string;
  group: string;
  about?: string;
  label: BiText;
  /** 已格式化的主值文本 */
  text: string;
  raw: unknown;
  unit?: string;
  /** 命中该字段的时间窗条数 >1 且值不同 */
  disputed: boolean;
  /** 该字段在整条生命里换过值 */
  varies: boolean;
  confidence?: 'A' | 'B' | 'C';
  src: string[];
  note?: string;
  /** 该字段全部时间窗（时间轴交互用） */
  windows: { from?: string; to?: string }[];
}

export interface ShipView {
  id: string;
  name: BiText;
  classId?: string;
  className?: BiText;
  facts: ResolvedFact[];
  narratives: ShipNarrative[];
  /** 单舰与舰级出现过的全部日期边界，时间轴用 */
  range: { from: string; to: string };
  slices: Slice[];
}

export interface Slice {
  code: string;
  title: string;
  from: string;
  to?: string;
  note?: string;
  /**
   * 手工指定这一片用哪张图（填 images.yaml 的 id）。
   * 不填就走自动匹配：在该片时间窗内找这张舰的照片，见 sliceImages()。
   */
  image?: string;
}

export function buildShipView(shipId: string): ShipView | null {
  const ship = getShip(shipId);
  if (!ship) return null;
  const cls = ship.class ? getClass(ship.class) : undefined;
  const facts = allFacts(ship, cls);
  const slices = readSlices(shipId);

  // 时间轴上下界只看「有意义的日期」，不看 to 为空（无限延续）造成的哨兵值。
  // 上界取 max(所有 from) 与 max(所有显式 to)，因为一条 to 为空的记录
  // 并不代表历史延续到 9999 年——它只代表「此后无新记载」。
  // identity.* 组排除在外：设计案（Plan Z / Ersatz Hannover）的日期是文书日期，
  // 不是舰的状态起始，把它算进去时间轴会从建造计划那年就开始，谎报两年空白期。
  const dated = facts.filter((f) => !f.field.startsWith('identity.'));
  let lo = Infinity;
  let hi = -Infinity;
  for (const f of dated) {
    const a = dateNum(f.from, 'start');
    lo = Math.min(lo, a);
    hi = Math.max(hi, a);
    if (f.to) hi = Math.max(hi, dateNum(f.to, 'end'));
  }
  if (!Number.isFinite(lo)) lo = dateNum('1900', 'start');
  if (!Number.isFinite(hi)) hi = dateNum('1950', 'end');
  // 末端留 3 个月余量，免得最后一个节点贴在轨道最右边。
  // 注意不能直接 hi + 900：YYYYMMDD 不是十进制天数，19410614+900 会变成
  // 19411514（第 15 个月），必须按月进位。
  const hiPad = addMonths(hi, 3);

  return {
    id: ship.id,
    name: ship.name,
    classId: ship.class,
    className: cls?.name,
    facts,
    narratives: getNarratives(shipId),
    range: { from: numToDate(lo), to: numToDate(hiPad) },
    slices,
  };
}

/** YYYYMMDD + n 个月，按月进位，不产生非法日期。 */
function addMonths(n: number, months: number): number {
  const y = Math.floor(n / 10000);
  const m = Math.floor((n % 10000) / 100);
  const d = n % 100;
  const total = y * 12 + (m - 1) + months;
  const ny = Math.floor(total / 12);
  const nm = (total % 12) + 1;
  const daysInMonth = new Date(Date.UTC(ny, nm, 0)).getUTCDate();
  return ny * 10000 + nm * 100 + Math.min(d, daysInMonth);
}

function numToDate(n: number): string {
  const y = Math.floor(n / 10000);
  const m = Math.floor((n % 10000) / 100);
  const d = n % 100;
  return `${y}-${String(m).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
}

// ------------------------------------------------------------ 状态切片

/**
 * 切片定义写在 data/slices/<ship>.yaml，因为它只对某一艘舰成立
 * （同级舰的改装节奏不同，切片边界不能继承）。
 */
function readSlices(shipId: string): Slice[] {
  const raw = readYaml<{ ship: string; slices: Slice[] }>(path.join('slices', `${shipId}.yaml`));
  if (!raw) return [];
  return (raw.slices ?? []).map((s) => ({ ...s, from: normDate(s.from)!, to: normDate(s.to) }));
}

// ------------------------------------------------------- 字段视图装配

/** 在某一天上取某字段的主值。 */
export function viewAt(facts: ResolvedFact[], field: string, t: number, about?: string) {
  const items = candidatesAt(facts, field, t, about);
  return {
    items,
    primary: pickPrimary(items, deps),
    disputed: isDisputed(items),
  };
}

export interface TimelinePayload {
  range: { from: string; to: string };
  /**
   * 切片除了文字，还带一张该时期的照片。
   * 不能把整个 ImageRec 塞进去：payload 会序列化到页面脚本里，
   * 每条图记录带着 license_raw、credit 那种几百字符的法律声明，
   * 九片切片就是几 KB 的屎山。这里只挑页面要显示的字段。
   */
  slices: (Slice & { pic?: SlicePic })[];
  groups: { id: string; label: BiText }[];
  fields: {
    id: string;
    group: string;
    about?: string;
    label: BiText;
    /** 每个时间窗一条，浏览器按 t 自己算命中 */
    windows: {
      from?: string;
      to?: string;
      text: string;
      disputed: boolean;
      conf?: string;
      note?: string;
      src: string[];
    }[];
  }[];
}

/** 切片配图在 payload 里的精简形态。 */
export interface SlicePic {
  file: string;
  title: string;
  credit: string;
  tier: 'A' | 'B' | 'C';
  url?: string;
  note?: string;
  /** in_range = 照片日期落在切片窗内；nearest = 窗外最近一张，页面要注明 */
  how: 'explicit' | 'in_range' | 'nearest';
}

/**
 * 生成要塞给浏览器的时间轴数据。
 * 只包含"存在于数据里"的字段，不列空字段 —— 页面上不出现一排"—"。
 */
export function buildTimelinePayload(view: ShipView): TimelinePayload {
  const groups = getGroups();
  const groupOrder = new Map(groups.map((g, i) => [g.id, i]));

  // 字段 -> 时间窗 -> 命中条目
  const buckets = new Map<string, ResolvedFact[]>();
  for (const f of view.facts) {
    const key = `${f.about ?? ''}::${f.field}`;
    const arr = buckets.get(key) ?? [];
    arr.push(f);
    buckets.set(key, arr);
  }

  const out: TimelinePayload['fields'] = [];

  for (const [key, all] of buckets) {
    const [about, field] = key.split('::');
    const def = getField(field);
    if (!def) continue;
    // weapon / mount 实体单独成节，不进主时间轴表
    if (about) continue;

    // 框架 §3.6：单舰层出现过该字段，就完全按单舰层展开，舰级值不再参与。
    // 覆盖不是分歧——漏了这一步，页面会把"单舰写了一遍舰级值"当成两种说法。
    const items = all.some((f) => f.origin === 'ship')
      ? all.filter((f) => f.origin === 'ship')
      : all;

    // 按时间窗归组，同一窗内多条（分歧）合成一条
    const byWin = new Map<string, ResolvedFact[]>();
    for (const f of items) {
      const k = `${f.from ?? ''}~${f.to ?? ''}`;
      const arr = byWin.get(k) ?? [];
      arr.push(f);
      byWin.set(k, arr);
    }

    // 同一时间窗 + 同一值去重（多来源互证同值，页面上只写一次）
    const seen = new Set<string>();
    const windows = [...byWin.values()]
      .filter((win) => {
        const sig = JSON.stringify(win.map((w) => w.value).sort());
        if (seen.has(sig)) return false;
        seen.add(sig);
        return true;
      })
      .map((win) => {
        const primary = pickPrimary(win, deps)!;
        const uniq = new Set(win.map((w) => JSON.stringify(w.value)));
        return {
          from: primary.from,
          to: primary.to,
          text: formatFact(primary),
          disputed: uniq.size > 1,
          conf: primary.confidence,
          note: primary.note,
          src: primary.src,
        };
      });

    // 有多个窗口的字段按时间排序
    windows.sort((a, b) => dateNum(a.from, 'start') - dateNum(b.from, 'start'));

    out.push({
      id: field,
      group: def.group,
      label: def.label,
      windows,
    });
  }

  out.sort((a, b) => {
    const ga = groupOrder.get(a.group) ?? 99;
    const gb = groupOrder.get(b.group) ?? 99;
    if (ga !== gb) return ga - gb;
    return a.label.zh.localeCompare(b.label.zh);
  });

  const usedGroups = new Set(out.map((f) => f.group));
  const groupsOut = groups
    .filter((g) => usedGroups.has(g.id))
    .map((g) => ({ id: g.id, label: g.label }));

  // 每片切片配一张图。自动匹配的逻辑在 sliceImages()，这里只做瘦身：
  // 塞进 payload 的图只留页面真正显示的字段。
  const pics = sliceImages(view.id, view.slices);
  const slicesOut = pics.map(({ slice, image, how }) => ({
    ...slice,
    pic:
      image && image.file
        ? {
            file: image.file,
            title: image.title.zh,
            credit: imageCredit(image),
            tier: image.license_tier,
            url: image.source_url,
            note: image.note,
            how: how === 'none' ? ('in_range' as const) : how,
          }
        : undefined,
  }));

  return { range: view.range, slices: slicesOut, groups: groupsOut, fields: out };
}

// ------------------------------------------------------------ 武器实体

export interface WeaponEntity {
  id: string;
  label: string;
  facts: ResolvedFact[];
  /** 该武器在某舰上的炮位 */
  mounts: MountEntity[];
}

export interface MountEntity {
  id: string;
  label: string;
  facts: ResolvedFact[];
  weaponId?: string;
}

/**
 * 从某舰级的文件里抽出 weapon / mount 实体。
 *
 * @deprecated 只读舰级，会漏掉武器数据挂在单舰上的那一半舰。
 *             新代码请用 getShipEntities()，它同时吃单舰和舰级。
 */
export function getEntities(cls: ClassFile | undefined) {
  const weapons = new Map<string, ResolvedFact[]>();
  const mounts = new Map<string, ResolvedFact[]>();
  if (!cls) return { weapons: [], mounts: [] };

  for (const raw of cls.facts ?? []) {
    const f = toResolved(raw, 'class');
    const about = f.about ?? '';
    if (about.startsWith('weapon:')) {
      const id = about.slice(7);
      const arr = weapons.get(id) ?? [];
      arr.push(f);
      weapons.set(id, arr);
    } else if (about.startsWith('mount:')) {
      const id = about.slice(6);
      const arr = mounts.get(id) ?? [];
      arr.push(f);
      mounts.set(id, arr);
    }
  }

  const mountToWeapon = new Map<string, string>();
  for (const [id, facts] of mounts) {
    const w = facts.find((f) => f.field === 'mount.weapon');
    if (w && typeof w.value === 'string') mountToWeapon.set(id, w.value);
  }

  const weaponEntities: WeaponEntity[] = [...weapons.entries()].map(([id, facts]) => {
    const desig = facts.find((f) => f.field === 'weapon.designation');
    return {
      id,
      label: typeof desig?.value === 'string' ? desig.value : id,
      facts: sortFacts(facts),
      mounts: [...mounts.entries()]
        .filter(([mid]) => mountToWeapon.get(mid) === `weapon:${id}`)
        .map(([mid, mf]) => mkMount(mid, mf)),
    };
  });

  return { weapons: weaponEntities.sort((a, b) => a.label.localeCompare(b.label)) };
}

function mkMount(id: string, facts: ResolvedFact[]): MountEntity {
  const name = facts.find((f) => f.field === 'mount.label_name');
  const desig = facts.find((f) => f.field === 'mount.turret_designation');
  const parts = [
    typeof name?.value === 'string' ? name.value : id,
    typeof desig?.value === 'string' ? desig.value : null,
  ].filter(Boolean);
  return { id, label: parts.join(' · '), facts: sortFacts(facts) };
}

/**
 * 单舰页专用：把「单舰自己的」和「舰级继承的」weapon / mount 实体合并。
 *
 * 为什么需要这一层（2026-11-21 修的 bug）：
 *
 * 本项目里武器数据的存放位置**不统一**，这是历史遗留：
 *   - 俾斯麦级 / 光辉级 / KGV 级：武器写在 data/classes/*.yaml（舰级）
 *   - 赤城 / 加贺 / 苍龙 / 飞龙：武器写在 data/ships/*.yaml（单舰）
 *   - 约克城级：舰级；企业号 / 约克城 / 大黄蜂三舰：单舰
 *
 * 旧的 getEntities(cls) 只读舰级，于是 12 艘舰里有 8 艘的「武器配置」区
 * **整块没有渲染** —— 页面不报错，只是那一段消失了。直到做「舰→武器」
 * 跳转时统计链接数才发现：赤城页 0 个武器链接，而它明明有 6 个武器实体。
 *
 * 合并规则与 fact 继承一致（框架 §3.6）：单舰层命中即覆盖舰级层，
 * 不与舰级值构成分歧。这里按 weapon id 合并，同 id 时单舰 fact 优先。
 */
export function getShipEntities(
  ship: ShipFile | undefined,
  cls: ClassFile | undefined,
) {
  const weapons = new Map<string, ResolvedFact[]>();
  const mounts = new Map<string, ResolvedFact[]>();

  // 先吃舰级，再吃单舰 —— 后写入的同 id 会覆盖先写入的（Map.set 语义），
  // 于是「单舰覆盖舰级」自动成立，不需要额外的去重逻辑。
  const sources: { facts: Fact[]; origin: 'ship' | 'class' }[] = [];
  if (cls) sources.push({ facts: cls.facts ?? [], origin: 'class' });
  if (ship) sources.push({ facts: ship.facts ?? [], origin: 'ship' });

  for (const { facts, origin } of sources) {
    for (const raw of facts) {
      const f = toResolved(raw, origin);
      const about = f.about ?? '';
      if (about.startsWith('weapon:')) {
        const id = about.slice(7);
        const arr = weapons.get(id) ?? [];
        arr.push(f);
        weapons.set(id, arr);
      } else if (about.startsWith('mount:')) {
        const id = about.slice(6);
        const arr = mounts.get(id) ?? [];
        arr.push(f);
        mounts.set(id, arr);
      }
    }
  }

  const mountToWeapon = new Map<string, string>();
  for (const [id, facts] of mounts) {
    const w = facts.find((f) => f.field === 'mount.weapon');
    if (w && typeof w.value === 'string') mountToWeapon.set(id, w.value);
  }

  const weaponEntities: WeaponEntity[] = [...weapons.entries()].map(([id, facts]) => {
    const desig = facts.find((f) => f.field === 'weapon.designation');
    return {
      id,
      label: typeof desig?.value === 'string' ? desig.value : id,
      facts: sortFacts(facts),
      mounts: [...mounts.entries()]
        .filter(([mid]) => mountToWeapon.get(mid) === `weapon:${id}`)
        .map(([mid, mf]) => mkMount(mid, mf)),
    };
  });

  return { weapons: weaponEntities.sort((a, b) => a.label.localeCompare(b.label)) };
}

/** fact 列表按字段注册顺序排，页面表格才不会乱序。 */
export function sortFacts(facts: ResolvedFact[]): ResolvedFact[] {
  const idx = new Map(getFields().map((f, i) => [f.id, i]));
  return [...facts].sort(
    (a, b) => (idx.get(a.field) ?? 9999) - (idx.get(b.field) ?? 9999),
  );
}

// ------------------------------------------------------------ 武器总表

/**
 * 全站武器总表 —— 「武器与装备」左树和武器详情页都读这一份。
 *
 * 为什么要在舰级/单舰之间再做一层合并：
 *   同一门 20 mm Oerlikon 同时登记在光辉级和英王乔治五世级里，
 *   两边参数有出入（弹重 0.123 vs 0.12、初速 844 vs 844、aa_max 3048 vs 未记）。
 *   左树上出现两个「20 mm Oerlikon」会让人以为这是两种炮。
 *   所以这里按 weapon id 合并：参数不合并（各舰级保留自己的值，页面并列显示），
 *   但「这一型炮一共装过哪几艘船」是合并后的信息。
 */
export interface WeaponSummary {
  id: string;
  /** 合并后的显示名：取首个有值的 designation，但不代表其他舰级的写法不算数 */
  label: string;
  /** 全部 designation 写法（不同舰级可能记法不同，全部保留） */
  designations: string[];
  /** 出现过的 category 值（去重） */
  categories: string[];
  /** 出现过的 nation 值（去重） */
  nations: string[];
  /** 事实来源：每个舰级/单舰各自的 fact 组，页面按类分块显示 */
  sources: {
    ownerId: string;
    ownerName: string;
    ownerKind: 'class' | 'ship';
    facts: ResolvedFact[];
    mounts: MountEntity[];
  }[];
  /** 装过的舰级 id（去重） */
  classIds: string[];
  /** 装过的单舰 id（去重） */
  shipIds: string[];
}

let _weaponIdx: Map<string, WeaponSummary> | null = null;

export function getWeaponIndex(): Map<string, WeaponSummary> {
  if (_weaponIdx) return _weaponIdx;

  const idx = new Map<string, WeaponSummary>();

  function add(
    ownerId: string,
    ownerName: string,
    ownerKind: 'class' | 'ship',
    weapons: WeaponEntity[],
  ) {
    for (const w of weapons) {
      const cur =
        idx.get(w.id) ??
        ({
          id: w.id,
          label: w.label,
          designations: [],
          categories: [],
          nations: [],
          sources: [],
          classIds: [],
          shipIds: [],
        } as WeaponSummary);

      cur.sources.push({ ownerId, ownerName, ownerKind, facts: w.facts, mounts: w.mounts });

      const desig = w.facts.find((f) => f.field === 'weapon.designation');
      if (typeof desig?.value === 'string' && !cur.designations.includes(desig.value)) {
        cur.designations.push(desig.value);
      }
      for (const [field, bucket] of [
        ['weapon.category', cur.categories],
        ['weapon.nation', cur.nations],
      ] as const) {
        const f = w.facts.find((x) => x.field === field);
        if (typeof f?.value === 'string' && !bucket.includes(f.value)) bucket.push(f.value);
      }

      if (ownerKind === 'class') {
        if (!cur.classIds.includes(ownerId)) cur.classIds.push(ownerId);
      } else if (!cur.shipIds.includes(ownerId)) {
        cur.shipIds.push(ownerId);
      }

      idx.set(w.id, cur);
    }
  }

  for (const c of getClasses()) {
    add(c.id, c.name.zh, 'class', getEntities(c).weapons);
  }
  for (const s of getShips()) {
    const cls = s.class ? getClass(s.class) : undefined;
    // 单舰也放武器：有些武器（如胡德的 15 in、提尔皮茨的鱼雷）直接写在单舰文件里，
    // 只读 classes/ 会漏掉它们。
    //
    // 2026-11-22：原来这里写的是 getEntities(s as unknown as ClassFile)，
    // 用强制类型转换把 ShipFile 冒充 ClassFile —— 字段恰好同名所以能跑，
    // 但语义是错的，也没法复用「单舰覆盖舰级」的合并逻辑。
    // 改用 getShipEntities(s, cls)：同时读两边，同 id 时单舰优先。
    add(s.id, s.name.zh, 'ship', getShipEntities(s, cls).weapons);
  }

  _weaponIdx = idx;
  return idx;
}

export function getWeapon(id: string): WeaponSummary | undefined {
  return getWeaponIndex().get(id);
}

// ------------------------------------------------------------------ 图片

let _imgs: ImageRec[] | null = null;

export function getImages(): ImageRec[] {
  if (!_imgs) {
    const r = readYaml<ImageRegFile>('images.yaml');
    _imgs = r?.images ?? [];
  }
  return _imgs;
}

/** 按 subject 取图，如 'ship:bismarck'。 */
export function getImagesFor(subject: string): ImageRec[] {
  return getImages().filter((i) => i.subject === subject);
}

/** 按 id 精确取一张图。
 *  首页大图这类「就是要这一张」的场景用它——比 subject + primary 更直接，
 *  也不会因为以后给该舰加了新图、primary 标记变化而悄悄换掉首页。 */
export function getImage(id: string): ImageRec | undefined {
  return getImages().find((i) => i.id === id);
}

/** 某对象的主图。
 *  优先取标了 primary: true 的（人对"哪张最适合当门面"的判断）；
 *  没有标记时退化为：A 档优先，其次第一条。
 *  不按授权档排序选主图——合法授权不等于好看，很多时候 B 档的实照比 A 档的模型照更像这个舰。
 */
export function primaryImage(subject: string): ImageRec | undefined {
  const list = getImagesFor(subject);
  const flagged = list.find((i) => i.primary && i.file);
  if (flagged) return flagged;
  return list.find((i) => i.license_tier === 'A' && i.file) ?? list.find((i) => i.file) ?? list[0];
}

/** 图注用：作者 + 授权 + 收藏机构，缺项自动省略。
 *  credit 字段在 Commons 上常是一整段法律声明（Bundesarchiv 那句有 200 多字符），
 *  直接铺在图注里会盖掉三条街的版面，所以压成「首个句号之前」再加省略号。
 */
export function imageCredit(img: ImageRec): string {
  const bits: string[] = [];
  if (img.author) bits.push(stripHtml(img.author));
  if (img.license_raw) bits.push(img.license_raw);
  else if (img.license) bits.push(img.license.toUpperCase());
  const credit = shorten(img.credit);
  if (credit && credit !== img.author) bits.push(credit);
  return bits.join(' · ');
}

/**
 * 去掉 Commons extmetadata 里夹带的 HTML。
 *
 * `Artist` 字段本来就是 HTML 片段（`<div class="fn value"><span
 * style="display:none">Unknown author</span>Unknown author</div>`），
 * 直接渲染就会在页面上打出这串标签。
 * 这里剥标签 + 解实体 + 去重复（Commons 常把同一名字放两份：
 * 一份给屏幕阅读器、一份给显示）。
 */
export function stripHtml(s: string | undefined): string {
  if (!s) return '';
  let t = s
    .replace(/<[^>]*>/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#0?39;/g, "'")
    .replace(/&nbsp;/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  // 「Unknown author Unknown author」→「Unknown author」
  const half = Math.floor(t.length / 2);
  if (t.length % 2 === 1 && t.slice(0, half) === t.slice(half + 1)) {
    t = t.slice(0, half);
  } else if (t.length % 2 === 0 && t.slice(0, half) === t.slice(half)) {
    t = t.slice(0, half);
  }
  return t;
}

/** 机构署名压缩：超过 52 字符就截到第一个句号 / 分号，再不行硬截。 */
export function shorten(s: string | undefined, max = 52): string {
  if (!s) return '';
  const t = s.replace(/\s+/g, ' ').trim();
  if (t.length <= max) return t;
  const cut = t.slice(0, max);
  const stop = Math.max(cut.lastIndexOf('.'), cut.lastIndexOf(';'), cut.lastIndexOf(','));
  return (stop > max * 0.5 ? cut.slice(0, stop) : cut).replace(/[\s,;.]+$/, '') + '…';
}

// ---------------------------------------------------- 切片配图（时间条用）

/**
 * 每一条状态切片配一张图。
 *
 * 不靠手工给 30 多个切片逐一配图——那样每加一艘船就要重配一遍，而且
 * 只要有人补了一张更贴切的照片，切片还是挂老图。这里改成按时间窗自动匹配：
 *
 *   1. 切片里显式写了 image: 就用它（人工意见永远优先）；
 *   2. 否则在 ship:<id> 的图里找 date 落在 [from, to] 内的；
 *   3. 同窗口多张时，优先 primary → A 档 → 日期最接近切片中点的；
 *   4. 一个都没有就返回 undefined，页面显示「该时期无影像」，不拿邻期的图顶。
 *
 * 标签日期只到年（"1941"）或到月（"1941-05"）时按区间处理，
 * 不能当字符串比大小——"1941" 在字典序上小于 "1941-05"，直接比会把全年的图判掉。
 */
export interface SliceImage {
  slice: Slice;
  image?: ImageRec;
  /** 自动匹配时用的匹配方式，便于页面说明「这张是按年份对上的」。 */
  how: 'explicit' | 'in_range' | 'nearest' | 'none';
}

/** 把 "1941" / "1941-05" / "1941-05-24" 展开成 [起, 止] 两个可比较的日期数。 */
function dateSpan(s?: string): [number, number] | null {
  if (!s) return null;
  const str = String(s).trim();
  const m = str.match(/^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?$/);
  if (!m) return null;
  const y = Number(m[1]);
  const mo = m[2] ? Number(m[2]) : null;
  const d = m[3] ? Number(m[3]) : null;
  const pad = (n: number) => String(n).padStart(2, '0');
  if (d !== null) {
    const one = dayNum(`${y}-${pad(mo!)}-${pad(d)}`);
    return [one, one];
  }
  if (mo !== null) {
    const first = dayNum(`${y}-${pad(mo)}-01`);
    const lastDay = new Date(Date.UTC(y, mo, 0)).getUTCDate();
    return [first, dayNum(`${y}-${pad(mo)}-${pad(lastDay)}`)];
  }
  return [dayNum(`${y}-01-01`), dayNum(`${y}-12-31`)];
}

function dayNum(s: string): number {
  const p = s.split('-').map(Number);
  return Date.UTC(p[0]!, (p[1] ?? 1) - 1, p[2] ?? 1) / 86400000;
}

/** 区间是否有交集（切片与图片标签都可能是年 / 月 / 日精度）。 */
function spanOverlap(a: [number, number], b: [number, number]): boolean {
  return a[0] <= b[1] && b[0] <= a[1];
}

/** 区间距离：0 表示相交，否则是相隔天数。 */
function spanGap(a: [number, number], b: [number, number]): number {
  if (spanOverlap(a, b)) return 0;
  return a[1] < b[0] ? b[0] - a[1] : a[0] - b[1];
}

/**
 * 切片缩略图的构图分类。
 *
 * 为什么需要这个（2026-11-22 用户反馈）：
 * 时间轴每片只有 74px 高，object-fit: cover 会居中裁一条横带。
 * 挂一张「炮塔特写」或「雷达天线」进去，裁完只剩一块钢板；
 * 挂一张「飞行甲板作业」进去，看到的是甲板和飞机，不是这艘舰。
 *
 * 用户的话：「时间轴上最好放的是战舰的全景图或侧舷图，放武器照片
 * 或太小的局部图没有太多意义」。
 *
 * 所以切片配图必须优先整舰构图。这里把「什么算整舰」写死一份，
 * 不依赖 part/view 的字面值 —— 那两列是登记时逐条判断的，
 * 有 None、有 other、有各种拼写。
 */
const WHOLE_SHIP_PARTS = new Set(['hull_side', 'deck', 'bow', 'stern', 'other']);
const LOCAL_PARTS = new Set([
  'turret', 'superstructure', 'bridge', 'propeller', 'catapult',
  'aircraft_handling', 'weapon', 'radar',
]);

/** 这张图能不能体现「整艘舰的外形」。 */
function isWholeShipShot(im: ImageRec): boolean {
  const part = String(im.part ?? '');
  const view = String(im.view ?? '');
  // detail 一律视为局部：它表达的正是「只拍了某个部件」
  if (view === 'detail') return false;
  if (LOCAL_PARTS.has(part)) return false;
  if (view === 'deck') return true; // 俯视甲板仍能看出整舰轮廓
  return WHOLE_SHIP_PARTS.has(part) || part === '' || part === 'undefined';
}

export function sliceImages(shipId: string, slices: Slice[]): SliceImage[] {
  const all = getImagesFor(`ship:${shipId}`).filter((i) => i.file);
  const byId = new Map(all.map((i) => [i.id, i]));

  // 切片配图只在「整舰构图」里挑。手工指定的 slice.image 不受此限 ——
  // 那是作者刻意选的具体某张，可能就是要那个细节。
  const imgs = all.filter(isWholeShipShot);

  /**
   * 已分配给前几个切片的图，用于尽量让相邻切片不撞图。
   *
   * 为什么需要（2026-11-22 发现）：俾斯麦 S2 / S3 / S5 三片都挂了同一张
   * 「英军侦察机航拍」—— 因为那张图日期覆盖范围宽、又是 primary。
   * 时间轴上连续三格是同一张图，读者以为图没加载出来。
   *
   * 规则不是禁止重复（图池小的舰做不到），而是**优先选没用过的**：
   * 用过的只在没有别的可选时才回退。
   */
  const used = new Set<string>();

  return slices.map((slice) => {
    if (slice.image) {
      const hit = byId.get(slice.image);
      if (hit) {
        used.add(hit.id);
        return { slice, image: hit, how: 'explicit' as const };
      }
      // 手工填了 id 但图不在本舰名下：不悄悄忽略，退到自动并把 how 标成 none，
      // 页面会因此显示「该时期无影像」，比挂错图好查。
    }

    const span = dateSpan(slice.from);
    if (span) {
      const toSpan = dateSpan(slice.to);
      const win: [number, number] = [span[0], toSpan ? toSpan[1] : span[1]];

      // 先找相交的
      const inRange = imgs
        .map((im) => ({ im, sp: dateSpan(im.date) }))
        .filter((x): x is { im: ImageRec; sp: [number, number] } => Boolean(x.sp) && spanOverlap(win, x.sp!));

      if (inRange.length > 0) {
        // 同窗口内挑：primary 优先，其次 A 档，再其次与切片起点最近的
        const mid = win[0];
        inRange.sort((a, b) => {
          const pa = a.im.primary ? 0 : 1;
          const pb = b.im.primary ? 0 : 1;
          if (pa !== pb) return pa - pb;
          const ta = a.im.license_tier === 'A' ? 0 : 1;
          const tb = b.im.license_tier === 'A' ? 0 : 1;
          if (ta !== tb) return ta - tb;
          return Math.abs(a.sp[0] - mid) - Math.abs(b.sp[0] - mid);
        });
        // 优先挑本舰还没用过的
        const fresh = inRange.find((x) => !used.has(x.im.id));
        const pick = fresh ?? inRange[0]!;
        used.add(pick.im.id);
        return { slice, image: pick.im, how: 'in_range' as const };
      }

      // 没有相交的：找时间上最近的一张。
      //
      // 容差分两档，按图片日期的精度决定 —— 这是 2026-11-22 的修正：
      //
      //  - 图片只有年份（date: 1942）：按「同一年内」接受，即切片窗口与该年
      //    有交集就可用。理由：早期舰照的原始档案往往只标到年，甚至只有
      //    一个「1930s」。严格按天数算，加贺 1928-1935 那几片永远无图，
      //    因为那年代的照片没有精确日期。
      //
      //  - 图片有月或日（date: 1942-06-04）：仍要求 365 天内。
      //    这条保留是因为它防的是真实错误：KGV 的 1942 那一片曾经挂上
      //    1945-08 的日本投降照——那两天的舰上多了一整套雷达和防空平台，
      //    外形差得远。宁可显示「该时期无影像」，也不要让模型制作者
      //    照着一张不属于这个时期的照片去改模型。
      const cand = imgs
        .map((im) => ({ im, sp: dateSpan(im.date) }))
        .filter((x): x is { im: ImageRec; sp: [number, number] } => Boolean(x.sp))
        .map((x) => ({ ...x, gap: spanGap(win, x.sp) }))
        .filter((x) => {
          if (x.gap <= 365) return true;
          const precision = String(x.im.date ?? '').trim().length;
          if (precision === 4) {
            const imgYear = Math.floor(x.sp[0] / 10000);
            const wFrom = Math.floor(win[0] / 10000);
            const wTo = Math.floor(win[1] / 10000);
            return imgYear >= wFrom && imgYear <= wTo;
          }
          return false;
        })
        .sort((a, b) => a.gap - b.gap);
      if (cand.length > 0) {
        const fresh = cand.find((x) => !used.has(x.im.id));
        const pick = fresh ?? cand[0]!;
        used.add(pick.im.id);
        return { slice, image: pick.im, how: 'nearest' as const };
      }
    }

    return { slice, how: 'none' as const };
  });
}


// ------------------------------------------------------------------ 正文

let _arts: Map<string, ArticleFile> | null = null;

export function getArticles(): ArticleFile[] {
  if (!_arts) {
    _arts = new Map();
    for (const d of readDir<ArticleFile>('articles')) {
      if (d?.ship) _arts.set(d.ship, d);
    }
  }
  return [..._arts.values()];
}

export function getArticle(shipId: string): ArticleFile | undefined {
  if (!_arts) getArticles();
  return _arts?.get(shipId);
}

// ------------------------------------------------------------ 武器正文

let _wepArts: Map<string, WeaponArticleFile> | null = null;

export function getWeaponArticles(): WeaponArticleFile[] {
  if (!_wepArts) {
    _wepArts = new Map();
    for (const d of readDir<WeaponArticleFile>('weapon-articles')) {
      if (d?.weapon) _wepArts.set(d.weapon, d);
    }
  }
  return [..._wepArts.values()];
}

export function getWeaponArticle(weaponId: string): WeaponArticleFile | undefined {
  if (!_wepArts) getWeaponArticles();
  return _wepArts?.get(weaponId);
}


// ------------------------------------------------------------------ 分类
//
// 分类是三层：主维度（时代 / 国家 / 舰种）→ 舰种子层 → 舰级 → 单舰。
// 之所以先定时代而不是舰种：本站覆盖顺序是二战 > 现代 > 一战，
// 以后舰队规模上去以后，「二战里有哪些战列舰」比「所有战列舰里哪些是二战的」
// 更符合读者的起点。舰种仍然保留为第二层和独立入口。
//
// 每个主维度的分组都带一个 sub 子层（舰种），这样一屏能直接看出
// 「二战 → 战列舰 → 俾斯麦级 → 俾斯麦」的完整路径。

export type TreeMode = 'era' | 'nation' | 'type';

/** 主维度的显示顺序与标签。未列进这里的一律排到末尾。 */
const ERA_ORDER = ['ww2', 'modern', 'cold_war', 'interwar', 'ww1'];
const TYPE_ORDER = [
  'battleship',
  'battlecruiser',
  'aircraft_carrier',
  'escort_carrier',
  'seaplane_carrier',
  'heavy_cruiser',
  'light_cruiser',
  'armored_cruiser',
  'protected_cruiser',
  'destroyer_leader',
  'destroyer',
  'torpedo_boat',
  'frigate',
  'corvette',
  'submarine',
  'monitor',
  'coastal_defence_ship',
  'minelayer',
  'auxiliary',
  'other',
];
const NATION_ORDER = [
  'germany',
  'united_kingdom',
  'united_states',
  'japan',
  'italy',
  'france',
  'soviet_union',
  'china',
  'netherlands',
  'australia',
  'canada',
  'poland',
  'norway',
  'sweden',
  'greece',
  'turkey',
  'spain',
  'finland',
  'romania',
  'other',
];

const MODE_ORDER: Record<TreeMode, string[]> = {
  era: ERA_ORDER,
  type: TYPE_ORDER,
  nation: NATION_ORDER,
};

/** 主维度对应的字段；秩序表里没有的取值 = 未分类。 */
const MODE_FIELD: Record<TreeMode, string> = {
  era: 'identity.era',
  type: 'identity.ship_type',
  nation: 'identity.nation',
};

/**
 * 服役年份 → 时代。舰艇数据里没写 identity.era 时用它兜底。
 * 边界取「服役期落在哪个战争/年代」，不是设计年份：
 * 一艘 1943 年服役、跑到 1980 年的舰算二战，因为它的服役身份是二战舰。
 */
export function eraFromYear(year: number): string | undefined {
  if (!Number.isFinite(year)) return undefined;
  if (year <= 1918) return 'ww1';
  if (year <= 1938) return 'interwar';
  if (year <= 1945) return 'ww2';
  if (year <= 1991) return 'cold_war';
  return 'modern';
}

export interface TreeClass {
  id: string;
  name: BiText;
  /** 第二层（一般是舰种）的标签，卡片左侧 kicker 用 */
  kicker?: string;
  /** 主维度中该舰级的另一个身份，例如按国家看时的舰种 / 按舰种看时的国家 */
  sub?: string;
  subLabel?: string;
  ships: { id: string; name: BiText }[];
}

export interface TreeSub {
  key: string;
  label: string;
  count: number;
  classes: TreeClass[];
}

export interface TreeGroup {
  key: string;
  label: string;
  count: number;
  subs: TreeSub[];
  /** 没有归入任何舰级的单舰 */
  loose: { id: string; name: BiText }[];
}

/** 取某舰某字段的主值（单舰优先，其次舰级）。 */
export function primaryValue(shipId: string, field: string): string | undefined {
  const ship = getShip(shipId);
  if (!ship) return undefined;
  const cls = ship.class ? getClass(ship.class) : undefined;
  const shipFacts = (ship.facts ?? []).filter((f) => f.field === field);
  const clsFacts = (cls?.facts ?? []).filter((f) => f.field === field);
  const raw = shipFacts.length > 0 ? shipFacts : clsFacts;
  if (raw.length === 0) return undefined;
  const origin = shipFacts.length > 0 ? 'ship' : 'class';
  const items = raw.map((f) => toResolved(f, origin));
  const best = pickPrimary(items, deps);
  if (!best) return undefined;
  return typeof best.value === 'string' ? best.value : String(best.value);
}

/** 舰级取主值（只查舰级自身 facts）。 */
function classPrimaryValue(cls: ClassFile, field: string): string | undefined {
  const raw = (cls.facts ?? []).filter((f) => f.field === field && !f.about);
  if (raw.length === 0) return undefined;
  const items = raw.map((f) => toResolved(f, 'class'));
  const best = pickPrimary(items, deps);
  if (!best) return undefined;
  return typeof best.value === 'string' ? best.value : String(best.value);
}

/** 取某舰某维度的值；era 允许从服役年份推。 */
function dimValue(shipId: string, mode: TreeMode): string {
  const direct = primaryValue(shipId, MODE_FIELD[mode]);
  if (direct) return direct;
  if (mode === 'era') {
    const y = primaryValue(shipId, 'construction.commissioned');
    const year = y ? Number(String(y).slice(0, 4)) : NaN;
    const era = eraFromYear(year);
    if (era) return era;
  }
  return '';
}

/** 舰级某维度的值：先看舰级自身，再看成员舰是否全一致；不一致就返回空。 */
function classDimValue(cls: ClassFile, mode: TreeMode, ships: ShipFile[]): string {
  if (mode !== 'era') {
    const own = classPrimaryValue(cls, MODE_FIELD[mode]);
    if (own) return own;
  } else {
    const own = classPrimaryValue(cls, 'identity.era');
    if (own) return own;
  }
  const keys = new Set(
    ships.filter((s) => s.class === cls.id).map((s) => dimValue(s.id, mode)),
  );
  keys.delete('');
  return keys.size === 1 ? [...keys][0] : '';
}

/**
 * 把已收录的舰艇组织成三层树：主维度 → 舰种 → 舰级 → 单舰。
 * 归组优先看舰级自身声明，没有就退回看成员舰是否全一致，
 * 仍不一致归到「未分类」而不是瞎猜。
 */
export function buildTree(mode: TreeMode): TreeGroup[] {
  const ships = getShips();
  const classes = getClasses();
  // 第二层固定用舰种（主维度本身就是舰种时，改用时代）
  const subMode: TreeMode = mode === 'type' ? 'era' : 'type';
  const subLabel = mode === 'type' ? '时代' : '舰种';

  const groupOf = new Map<string, string>();
  const subOf = new Map<string, string>();
  for (const c of classes) {
    groupOf.set(c.id, classDimValue(c, mode, ships));
    subOf.set(c.id, classDimValue(c, subMode, ships));
  }

  const buckets = new Map<string, TreeGroup>();
  const subsOf = new Map<string, Map<string, TreeSub>>();

  const ensureGroup = (key: string): TreeGroup => {
    let g = buckets.get(key);
    if (!g) {
      g = { key, label: key ? enumLabel(key, 'zh') : '未分类', count: 0, subs: [], loose: [] };
      buckets.set(key, g);
      subsOf.set(key, new Map());
    }
    return g;
  };
  const ensureSub = (g: TreeGroup, key: string): TreeSub => {
    const m = subsOf.get(g.key)!;
    let s = m.get(key);
    if (!s) {
      s = { key, label: key ? enumLabel(key, 'zh') : '未分类', count: 0, classes: [] };
      m.set(key, s);
      g.subs.push(s);
    }
    return s;
  };

  for (const c of classes) {
    const g = ensureGroup(groupOf.get(c.id) ?? '');
    const sub = ensureSub(g, subOf.get(c.id) ?? '');
    const members = ships
      .filter((s) => s.class === c.id)
      .map((s) => ({ id: s.id, name: s.name }));

    // 卡片副标题：主维度之外，再给一个身份（按舰种看时给国家，按国家看时给舰种）
    const otherField = mode === 'era' ? 'identity.nation' : 'identity.nation';
    let sub2 = classPrimaryValue(c, otherField);
    if (!sub2 && members.length > 0) {
      const keys = new Set(members.map((m) => primaryValue(m.id, otherField) ?? ''));
      keys.delete('');
      if (keys.size === 1) sub2 = [...keys][0];
    }

    sub.classes.push({
      id: c.id,
      name: c.name,
      kicker: subLabel,
      sub: sub2 ? enumLabel(sub2, 'zh') : undefined,
      subLabel: '国家',
      ships: members,
    });
    sub.count += members.length;
    g.count += members.length;
  }

  for (const s of ships) {
    if (s.class && classes.some((c) => c.id === s.class)) continue;
    const g = ensureGroup(dimValue(s.id, mode));
    g.loose.push({ id: s.id, name: s.name });
    g.count += 1;
  }

  const order = MODE_ORDER[mode];
  const rank = (key: string): number => {
    if (!key) return 9999; // 未分类永远垫底
    const i = order.indexOf(key);
    return i < 0 ? 900 + key.charCodeAt(0) : i;
  };

  const arr = [...buckets.values()].filter((g) => g.count > 0);
  arr.sort((a, b) => rank(a.key) - rank(b.key));
  for (const g of arr) {
    g.subs = g.subs.filter((s) => s.count > 0);
    g.subs.sort((a, b) => {
      // 子层按舰种表顺序排，未分类垫底
      const ra = a.key ? TYPE_ORDER.indexOf(a.key) : 9999;
      const rb = b.key ? TYPE_ORDER.indexOf(b.key) : 9999;
      const fa = ra < 0 ? 900 : ra;
      const fb = rb < 0 ? 900 : rb;
      return fa - fb || b.count - a.count;
    });
    for (const s of g.subs) {
      s.classes.sort(
        (a, b) => b.ships.length - a.ships.length || a.name.zh.localeCompare(b.name.zh),
      );
    }
  }
  return arr;
}

/** 某舰级的成员舰（给舰级页复用）。 */
export function shipsOfClass(classId: string): ShipFile[] {
  return getShips().filter((s) => s.class === classId);
}

// ------------------------------------------------------------------ 统计

export function stats() {
  const ships = getShips();
  const classes = getClasses();
  const facts =
    ships.reduce((n, s) => n + (s.facts?.length ?? 0), 0) +
    classes.reduce((n, c) => n + (c.facts?.length ?? 0), 0);
  return {
    ships: ships.length,
    classes: classes.length,
    fields: getFields().length,
    sources: getSources().length,
    narratives: getNarratives().length,
    facts,
  };
}

// ============================================================== 对比器索引

/**
 * 对比器预生成索引（框架 §3.4）。
 *
 * 「对比器 = 取两艘舰、遍历 compare: true 的字段、各自解析主值、表格渲染。
 *  不需要为每对舰艇写任何定制代码。」—— 索引就是把这句话需要的东西
 * 一次性在构建期算好，塞进页面脚本里。
 *
 * 三个必须写进 payload 的东西，漏一个页面就废：
 *
 *  1. `fields` —— 只有 compare: true **且属于舰体层**的字段。武器/炮位层的
 *     `weapon.bore` 之类不进来（那是另一套实体，另一套索引）。
 *  2. `deps`  —— pickPrimary() 在浏览器里要 tierOf / fetchedOf 两个函数，
 *     而 data.ts 的 deps 是构建期对象、直接闭包 getSources()。
 *     浏览器里没有 fs，不把这两张表序列化过去，主值规则当场退化成
 *     「取第一条」——这跟框架 §3.9 承诺的完全不是一回事。
 *  3. `cells` —— 每舰每字段的**全部时间窗**，不是只有主值。
 *     时间轴要能拖，就必须让浏览器自己按 t 过滤，所以窗口边界和
 *     comparable 标记都得带过去。
 *
 * 体积：实测约 39 KB（note 截断到 160 字符）。整页内联，不开额外请求。
 */
export interface CompareField {
  id: string;
  label: BiText;
  group: string;
  unit: string | null;
  better: 'higher' | 'lower' | 'context' | 'none';
  type: string;
  /** 字段级 note（口径要求、量纲提醒），渲染在行标题的悬浮说明里 */
  note?: string;
}

export interface CompareCell {
  from?: string;
  to?: string;
  /** 已格式化的显示文本（值 + 单位） */
  text: string;
  /** 原始数值，着色排序用；非数值字段为 null */
  num: number | null;
  conf?: string;
  src: string[];
  /** 来源自己承认口径对不上 → 不参与高低判定，也不参与「最值」高亮 */
  incomparable?: boolean;
  /** 这一条是单舰覆盖舰级的值（页面上可标「本舰自有」） */
  own?: boolean;
  /** 同一时间窗内有多个不同值 —— 真分歧，不是时序演进 */
  disputed?: boolean;
  /**
   * 该时间窗内的全部并列说法（含主值本身），只在 disputed 时给。
   * 页面把它做成可展开的「另有 N 说」——点开能看到 42,900 t 这种
   * 落选但保留的说法。只给主值等于把本站最值钱的特性藏起来。
   */
  alts?: { text: string; conf?: string; src: string[]; note?: string }[];
  note?: string;
}

export interface CompareShip {
  id: string;
  name: BiText;
  classId?: string;
  className?: BiText;
  /** 该舰时间轴上可拖动的边界（服役 → 沉没/退役），YYYY-MM-DD */
  span: { from: string; to: string };
  /** 该舰的状态切片，滑块上标代号用 */
  slices: { code: string; title: string; from: string; to?: string }[];
  /** 主图（表头缩略图），没有就是 undefined */
  pic?: { file: string; title: string; credit: string };
}

export interface CompareIndex {
  ships: CompareShip[];
  fields: CompareField[];
  groups: { id: string; label: BiText }[];
  /** 序列化的 PrimaryDeps —— 浏览器侧 pickPrimary 靠这两张表复现主值规则 */
  deps: { tier: Record<string, number>; fetched: Record<string, string> };
  /** cells[shipId][fieldId] = 该字段的全部时间窗（同一窗内多值已合并为主值） */
  cells: Record<string, Record<string, CompareCell[]>>;
  /** 双舰同时在世的交集；空表示没有交集，界面不启用「同步时刻」 */
  overlap?: { from: string; to: string };
}

/** 舰体层字段：applies_to 缺省即 [class, ship]。 */
function isHullField(f: FieldDef): boolean {
  const at = f.applies_to ?? ['class', 'ship'];
  return at.includes('class') || at.includes('ship');
}

/** 只取能上表格的类型：数值 / 整数 / 枚举 / 布尔 / 日期。
 *  string / table / ref 拼成一张表没有意义（装备清单合成一格只会失真）。 */
function isComparableType(t: string): boolean {
  return t === 'number' || t === 'integer' || t === 'enum' || t === 'bool' || t === 'date';
}

export function buildCompareIndex(): CompareIndex {
  const groups = getGroups();
  const groupOrder = new Map(groups.map((g, i) => [g.id, i]));

  const fields = getFields()
    .filter((f) => f.compare && isHullField(f) && isComparableType(f.type))
    .sort((a, b) => {
      const ga = groupOrder.get(a.group) ?? 99;
      const gb = groupOrder.get(b.group) ?? 99;
      return ga - gb || a.label.zh.localeCompare(b.label.zh);
    })
    .map<CompareField>((f) => ({
      id: f.id,
      label: f.label,
      group: f.group,
      unit: f.unit,
      better: f.better,
      type: f.type,
      note: f.note,
    }));
  const fieldIds = new Set(fields.map((f) => f.id));

  const ships: CompareShip[] = [];
  const cells: Record<string, Record<string, CompareCell[]>> = {};

  for (const s of getShips()) {
    const cls = s.class ? getClass(s.class) : undefined;
    const view = buildShipView(s.id);
    if (!view) continue;

    // span 用「服役 → 结局」而不是 view.range：range 为了时间轴留了 3 个月余量、
    // 还含建造期。对比器的滑块应该是「这艘船活着的时间」，所以单独算。
    const comm = primaryValue(s.id, 'construction.commissioned');
    const fate = primaryValue(s.id, 'construction.fate_date');
    const span = {
      from: comm ? (normDate(comm) ?? view.range.from) : view.range.from,
      to: fate ? (normDate(fate) ?? view.range.to) : view.range.to,
    };

    const perField: Record<string, CompareCell[]> = {};

    for (const fid of fieldIds) {
      const all = view.facts.filter((f) => f.field === fid && !f.about);
      if (all.length === 0) continue;

      // 这里**不能**照抄 buildTimelinePayload 的「单舰层出现过就只用单舰层」。
      //
      // 那条规则对「整条生命只看一个主值」是对的，对**按时刻查询**是错的：
      // KGV 的 aviation.aircraft.capacity 在单舰层有一条 1944-07-01 起的 0
      //（拆弹射器后不再载机），但舰级那条「2 架水上飞机」覆盖的是 1940–1944。
      // 若在索引阶段就把舰级值丢掉，拖动滑块回到 1942 年时这一格会变成空，
      // 而实际上那时候是真有 2 架水机的。
      //
      // 正确做法：**全量带过去**，交给浏览器按 t 过滤 —— 也就是 resolve.ts 的
      // candidatesAt()：先按时间窗筛，筛完若单舰层有命中就只用单舰层。
      // 这样「单舰覆盖舰级」的语义在每一个时刻上都成立，而不是整条生命一刀切。
      const byWin = new Map<string, ResolvedFact[]>();
      for (const f of all) {
        const k = `${f.from ?? ''}~${f.to ?? ''}`;
        const arr = byWin.get(k) ?? [];
        arr.push(f);
        byWin.set(k, arr);
      }

      const out: CompareCell[] = [];
      for (const win of byWin.values()) {
        const primary = pickPrimary(win, deps);
        if (!primary) continue;
        const raw = primary.value;
        const num =
          typeof raw === 'number' && Number.isFinite(raw) ? raw : null;
        // 同一时间窗里出现两个不同值 = 真分歧（框架 §3.2 规则 4）。
        // 注意这跟「命中多条时间窗」完全是两回事：tirpitz 编制 1941→2065、
        // 1943→2608 是时序演进，不是争议；同一窗内 41700 vs 43978 才是争议。
        const distinctVals = new Set(win.map((w) => JSON.stringify(w.value)));
        const disputed = distinctVals.size > 1;
        out.push({
          from: primary.from,
          to: primary.to,
          text: formatFact(primary),
          num,
          conf: primary.confidence,
          src: primary.src,
          incomparable: primary.comparable === false ? true : undefined,
          // own = 这一格的值来自单舰层。浏览器在某个时刻同时命中 own 与非 own
          // 的窗口时，按框架 §3.6 只取 own 那几条（单舰覆盖舰级）。
          own: primary.origin === 'ship' ? true : undefined,
          disputed: disputed ? true : undefined,
          // 分歧时把并列的说法全部带上（去重、按层级排序），页面可展开看。
          // 排序不能两两调 pickPrimary 来排（那不是稳定排序），
          // 直接用同一套判据算一个分数：层级高、有 note、采集新者靠前。
          alts: disputed
            ? (() => {
                const scored = win.map((w) => ({
                  w,
                  tier: w.src.length ? Math.max(...w.src.map((s) => deps.tierOf(s))) : -1,
                  hasNote: w.note ? 1 : 0,
                  fetched: w.src.map((s) => deps.fetchedOf(s)).sort().pop() ?? '',
                  key: [...w.src].sort().join(','),
                }));
                scored.sort(
                  (a, b) =>
                    b.tier - a.tier ||
                    b.hasNote - a.hasNote ||
                    (a.fetched < b.fetched ? 1 : a.fetched > b.fetched ? -1 : 0) ||
                    a.key.localeCompare(b.key),
                );
                const seen = new Set<string>();
                return scored
                  .map((x) => x.w)
                  .filter((w) => {
                    const t = formatFact(w);
                    if (seen.has(t)) return false;
                    seen.add(t);
                    return true;
                  })
                  .map((w) => ({
                    text: formatFact(w),
                    conf: w.confidence,
                    src: w.src,
                    note: shorten(w.note, 120),
                  }));
              })()
            : undefined,
          note: shorten(primary.note, 160),
        });
      }
      if (out.length === 0) continue;
      out.sort((a, b) => dateNum(a.from, 'start') - dateNum(b.from, 'start'));
      perField[fid] = out;
    }

    cells[s.id] = perField;

    const img = primaryImage(`ship:${s.id}`);
    ships.push({
      id: s.id,
      name: s.name,
      classId: s.class,
      className: cls?.name,
      span,
      slices: (view.slices ?? []).map((x) => ({
        code: x.code,
        title: x.title,
        from: x.from,
        to: x.to,
      })),
      pic: img?.file
        ? { file: img.file, title: img.title.zh, credit: imageCredit(img) }
        : undefined,
    });
  }

  ships.sort((a, b) => a.name.zh.localeCompare(b.name.zh));

  // deps 序列化：只带「真的被某条 fact 引用过」的来源，别把 171 条全搬进页面。
  const usedSrc = new Set<string>();
  for (const perField of Object.values(cells)) {
    for (const arr of Object.values(perField)) {
      for (const c of arr) for (const s of c.src) usedSrc.add(s);
    }
  }
  const tier: Record<string, number> = {};
  const fetched: Record<string, string> = {};
  for (const id of usedSrc) {
    const src = getSource(id);
    tier[id] = TIER_RANK[src?.tier ?? 'E'] ?? 0;
    fetched[id] = src?.fetched ?? '';
  }

  const usedGroups = new Set(fields.map((f) => f.group));
  const groupsOut = groups
    .filter((g) => usedGroups.has(g.id))
    .map((g) => ({ id: g.id, label: g.label }));

  // 双舰交集只在「两艘都有明确服役与结局日期」时才算得准。
  // 这里先给整站范围的交集（全舰同时在世），页面选了具体两艘再按它们算。
  let lo = '0000-00-00';
  let hi = '9999-12-31';
  for (const s of ships) {
    if (s.span.from > lo) lo = s.span.from;
    if (s.span.to < hi) hi = s.span.to;
  }
  const overlap = lo <= hi ? { from: lo, to: hi } : undefined;

  return { ships, fields, groups: groupsOut, deps: { tier, fetched }, cells, overlap };
}
