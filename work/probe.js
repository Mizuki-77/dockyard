// 找出 390px 下真正把页面撑宽的元素。
// 用 Chrome headless 的 --dump-dom 拿不到计算结果，所以改成先渲染一页探针
// HTML：把 probe.js 通过 ?probe 注入不现实，这里换用 CDP 太麻烦。
// 折中：用 puppeteer 没有，就按「逐个删候选样式」的思路——先打印可疑元素列表
// 到控制台，再由 chrome --headless --enable-logging 抓。
const bad = [];
const vw = document.documentElement.clientWidth;
document.querySelectorAll('*').forEach((el) => {
  const r = el.getBoundingClientRect();
  if (r.width > vw + 1 && getComputedStyle(el).overflowX === 'visible') {
    bad.push(
      el.tagName +
        '.' +
        (typeof el.className === 'string' ? el.className : '') +
        ' w=' +
        Math.round(r.width) +
        ' left=' +
        Math.round(r.left),
    );
  }
});
console.log('VW=' + vw + ' scrollW=' + document.documentElement.scrollWidth);
console.log(bad.slice(0, 30).join('\n'));
