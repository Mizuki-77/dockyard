import { defineConfig } from 'astro/config';

// 站点根地址只在这一处配。og:image / canonical 都从它推出来，
// 所以临时用隧道分享时可以临时覆盖：
//   $env:PUBLIC_SITE='https://xxx.trycloudflare.com'; npx astro build
// 正式域名定了以后，把下面的默认值改成它即可。
// 当前默认值 = 已部署的 Cloudflare Workers 地址（wrangler.toml 里 worker 名 archive，
// 账号的 workers.dev 子域是 dockyard）。
const site = process.env.PUBLIC_SITE ?? 'https://archive.dockyard.workers.dev';

// https://astro.build/config
export default defineConfig({
  site,
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
  build: {
    format: 'directory',
  },
  vite: {
    server: {
      watch: {
        // work/ 是调研原料与临时脚本，dist/ 是产物，node_modules 不用看。
        //
        // data/ 保留监听：YAML 改了要能触发数据层重算，这是本地校对的主要循环。
        // 但注意 —— 用脚本（尤其 Windows 上 edit 工具或 python 的写临时文件再
        // rename）批量改 data/*.yaml 时，Vite 的 chokidar 偶尔会撞上
        // `EBUSY: resource busy or locked, watch '...tmp'`，整个 dev server 直接挂。
        // 遇到就重启 `npm run dev`；不要为了这个把 data/ 从监听里去掉，
        // 那会让「改数据 → 看页面」变成每次手工重启，代价更大。
        ignored: ['**/work/**', '**/node_modules/**', '**/dist/**', '**/*.tmp', '**/*.bak*'],
      },
    },
  },
});
