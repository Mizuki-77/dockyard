// 对比器纠错链接的实际渲染验证。
//
// 为什么不数构建产物：tbody 里的 HTML 全是脚本用 innerHTML 拼的，
// 静态分析只能看到拼装代码，看不到结果。这里用最小的 DOM stub
// 把页面脚本真跑一遍，然后检查拼出来的 <tr>/<td> 里有没有纠错链接、
// 参数解出来对不对。

const fs = require('fs');
const path = require('path');

const HTML = path.join(__dirname, '..', 'dist', 'compare', 'index.html');
const html = fs.readFileSync(HTML, 'utf8');

const scripts = [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
if (scripts.length === 0) {
  console.error('没有找到内联脚本');
  process.exit(1);
}

// ---------------------------------------------------------------- DOM stub
class El {
  constructor(tag = 'div') {
    this.tagName = tag.toUpperCase();
    this._html = '';
    this.children = [];
    this.style = {};
    this.dataset = {};
    this.classList = { add() {}, remove() {}, toggle() {}, contains: () => false };
    this.attributes = {};
    this._listeners = {};
  }
  get innerHTML() {
    return this._html;
  }
  set innerHTML(v) {
    this._html = String(v);
    // 极简解析：只记录 td/tr 数量，够做断言
    this.children = [];
    const trs = [...this._html.matchAll(/<tr\b[^>]*>([\s\S]*?)<\/tr>/g)];
    for (const tr of trs) {
      const row = new El('tr');
      row._html = tr[1];
      this.children.push(row);
    }
  }
  setAttribute(k, v) {
    this.attributes[k] = v;
  }
  getAttribute(k) {
    return this.attributes[k];
  }
  appendChild(n) {
    this.children.push(n);
    return n;
  }
  addEventListener(t, fn) {
    (this._listeners[t] = this._listeners[t] || []).push(fn);
  }
  removeEventListener() {}
  // 页面脚本假设「按选择器一定找得到元素」（真实 DOM 里确实有）。
  // stub 里也返回元素而不是 null，否则脚本在第一批 picker 就崩了，
  // 根本走不到 render()，断言就测不到东西。
  querySelector() {
    return new El();
  }
  querySelectorAll() {
    return [new El()];
  }
  closest() {
    return new El();
  }
  getBoundingClientRect() {
    return { left: 0, top: 0, width: 100, height: 20, right: 100, bottom: 20 };
  }
  focus() {}
}

const registry = new Map();
const document = {
  getElementById(id) {
    if (!registry.has(id)) registry.set(id, new El());
    return registry.get(id);
  },
  querySelector(sel) {
    return new El();
  },
  querySelectorAll() {
    return [];
  },
  createElement(tag) {
    return new El(tag);
  },
  addEventListener() {},
  documentElement: { scrollWidth: 1200, clientWidth: 1200 },
  body: new El('body'),
};

const localStorageStub = {
  _d: {},
  getItem(k) {
    return this._d[k] ?? null;
  },
  setItem(k, v) {
    this._d[k] = String(v);
  },
  removeItem(k) {
    delete this._d[k];
  },
};

const windowStub = {
  addEventListener() {},
  matchMedia: () => ({ matches: false, addEventListener() {} }),
  location: { search: '', pathname: '/compare/', href: 'http://localhost/compare/' },
  localStorage: localStorageStub,
  history: { replaceState() {}, pushState() {} },
  navigator: { userAgent: 'node' },
};

// ---------------------------------------------------------------- 跑脚本
const sandboxGlobals = {
  document,
  window: windowStub,
  localStorage: localStorageStub,
  navigator: windowStub.navigator,
  history: windowStub.history,
  location: windowStub.location,
  console,
  URLSearchParams,
  URL,
  Math,
  Date,
  JSON,
  parseInt,
  parseFloat,
  isNaN,
  Number,
  String,
  Object,
  Array,
  Set,
  Map,
  RegExp,
  Error,
  encodeURIComponent,
  decodeURIComponent,
  requestAnimationFrame: (fn) => fn(),
  setTimeout,
  clearTimeout,
};

let code = scripts[0];
const names = Object.keys(sandboxGlobals);
const fn = new Function(...names, code);

try {
  fn(...names.map((n) => sandboxGlobals[n]));
} catch (e) {
  console.error('=== 脚本执行抛出：' + e.message + ' ===');
  console.error(e.stack.split('\n').slice(0, 6).join('\n'));
  console.error('');
}

// ---------------------------------------------------------------- 断言
const tbody = registry.get('cmp-tbody');
if (!tbody) {
  console.error('FAIL: 脚本没有写入 cmp-tbody');
  process.exit(1);
}

const rows = tbody.innerHTML;
console.log('tbody 长度：', rows.length);
console.log('数据行数：', (rows.match(/<tr class="cmp-row"/g) || []).length);
console.log('纠错链接数：', (rows.match(/class="cmp-rept"/g) || []).length);

const first = rows.match(/<a class="cmp-rept" href="([^"]+)"/);
if (!first) {
  console.error('FAIL: 没生成任何纠错链接');
  process.exit(1);
}

const raw = first[1].replace(/&amp;/g, '&');
const u = new URL(raw);
console.log('');
console.log('第一个链接的参数：');
for (const [k, v] of u.searchParams) {
  console.log(`  ${k}: ${v.replace(/\n/g, '\\n')}`);
}

// 校验关键参数非空且合理
const checks = [
  ['template', (v) => v === 'correction.yml'],
  ['title', (v) => v.startsWith('[纠错] ')],
  ['entity', (v) => v.includes('（') && v.includes('）')],
  ['page', (v) => v.includes('/compare/')],
  ['claim', (v) => v.includes('字段：') && v.includes('我认为正确的是')],
];
let ok = true;
for (const [k, test] of checks) {
  const v = u.searchParams.get(k);
  if (!v || !test(v)) {
    console.error(`FAIL: 参数 ${k} 不合格 → ${v}`);
    ok = false;
  }
}

console.log('');
console.log(ok ? 'PASS：对比器纠错链接渲染与参数均正确' : 'FAIL');
process.exit(ok ? 0 : 1);
