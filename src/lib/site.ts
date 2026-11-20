/**
 * 站点级常量。
 *
 * 仓库地址只在这一处配 —— 换账号、换仓库名、迁移到组织名下，都只改这里。
 * 纠错入口（ReportIssue.astro）与 /help 页面都从 REPO_URL 推出来。
 */
export const REPO_URL = 'https://github.com/Mizuki-77/dockyard';

/** 纠错入口用的 issue 表单模板（放在 .github/ISSUE_TEMPLATE/ 下） */
export const ISSUE_TEMPLATE = 'correction.yml';

/**
 * 生成「报告这条数据有误」的 GitHub issue 链接。
 *
 * 设计要点（见 docs/00-framework.md §6.1）：
 * - 带上上下文，不带上下文等于全站一个「联系我们」
 * - 不预填结论，投稿人只需要补「正确的值 + 你的来源」
 *
 * 一个关键约束（实测过）：
 * **issue form（模板带 body:/fields:）会忽略 URL 里的 body 参数。**
 * 只认「和表单字段 id 同名」的查询参数。所以这里传的是
 * entity / page / claim 三个字段名，而不是一大段 markdown。
 * 若哪天把模板换回 markdown 模板（.md），则要改回 body 参数。
 */
export function issueUrl(opts: {
  /** 舰 / 武器 / 战役的实体 id */
  entity: string;
  /** 人类可读的实体名，如「赤城」「俾斯麦」 */
  entityLabel: string;
  /** 字段 id，如 displacement.standard。战役页的事件流没有字段概念，留空 */
  field?: string;
  /** 字段的中文名 */
  fieldLabel?: string;
  /**
   * 这一条是什么 —— 用于没有 field 的场合（战役事件流的某一条事件、某条伤亡数字）。
   * 有 field 时不用填，会自动用 fieldLabel。
   */
  itemLabel?: string;
  /** 页面当前显示的值 */
  current?: string;
  /** 当前值的来源 id 列表 */
  sources?: string[];
  /** 数据所在页的完整 URL */
  pageUrl: string;
  /** 实体类型，决定 issue 标题的分类 */
  kind?: 'ship' | 'class' | 'weapon' | 'battle' | 'operation' | 'other';
}): string {
  const {
    entity,
    entityLabel,
    field,
    fieldLabel,
    itemLabel,
    current,
    sources = [],
    pageUrl,
  } = opts;

  const subject = fieldLabel
    ? `${entityLabel} · ${fieldLabel}`
    : itemLabel
      ? `${entityLabel} · ${itemLabel}`
      : entityLabel;

  // 把字段与来源写进「你认为正确的是什么」的预填正文里 ——
  // 表单没有专门的字段栏给它们，但这段文本用户能直接编辑，位置也合理。
  const context: string[] = [];
  if (current) context.push(`站点当前显示：${current}`);
  if (field) context.push(`字段：${fieldLabel ?? field}（${field}）`);
  else if (itemLabel) context.push(`条目：${itemLabel}`);
  if (sources.length) context.push(`当前来源：${sources.join('、')}`);
  context.push('');
  context.push('我认为正确的是：');
  context.push('');

  const params = new URLSearchParams({
    template: ISSUE_TEMPLATE,
    title: `[纠错] ${subject}`,
    entity: `${entityLabel}（${entity}）`,
    page: pageUrl,
    claim: context.join('\n'),
  });

  return `${REPO_URL}/issues/new?${params.toString()}`;
}
