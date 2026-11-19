# 部署与发布

## 现在的正式地址

**https://archive.dockyard.workers.dev**

Cloudflare Workers 静态资源部署（不是 Pages）。账号 `977373497@qq.com's Account`，
workers.dev 子域 `dockyard`，worker 名 `archive`。

> worker 名之所以不叫 `dockyard`：子域已经占用了 `dockyard`，
> 再叫 `dockyard` 地址就会变成 `dockyard.dockyard.workers.dev`，重复。

## 发布一条命令

```powershell
cmd /c "npm.cmd run deploy"
```

等价于 `astro build && wrangler deploy`。改完 `data/` 里的 YAML 必须重新 build，
`wrangler deploy` 只上传 `dist/` 里的成品。

**注意 PowerShell 执行策略禁 `npm.ps1`**，直接敲 `npm` 会报
`无法加载文件 ...npm.ps1，因为在此系统上禁止运行脚本`，所以要走 `npm.cmd`。

## 配置在哪

- `wrangler.toml`：worker 名 `archive`、`[assets] directory = "./dist"`、`preview_urls = false`。
- `astro.config.mjs:7`：`const site = process.env.PUBLIC_SITE ?? 'https://archive.dockyard.workers.dev';`
  这是 canonical 与 og:image 的唯一来源。临时换域名分享时：
  ```powershell
  $env:PUBLIC_SITE='https://xxx.trycloudflare.com'; cmd /c "npm.cmd run build"
  ```

## 登录状态

`npx wrangler login` 已完成，凭据在
`C:\Users\mizuki\AppData\Roaming\xdg.config\.wrangler\config\default.toml`。
token 过期后重新执行一次 `wrangler login` 即可。

**踩过的坑**：
- 未验证邮箱时 `wrangler deploy` 报 `You need to verify your email address to use Workers. [code: 10034]`。
- `wrangler pages project create` 同样被邮箱验证拦住（`Your user email must been verified [code: 8000077]`）。
- 首次 `wrangler deploy` 会要求注册 workers.dev 子域，非交互环境下它会自动选 no 然后失败；
  用 API 注册：`PUT /accounts/{id}/workers/subdomain` body `{"subdomain":"dockyard"}`。

## 部署后必查

新版本刚 deploy 时部分路由会短暂 404（边缘节点传播，约 5–10 秒）。等一会儿再测。

```powershell
$u='https://archive.dockyard.workers.dev'
foreach ($p in @('/','/ships/','/ships/by-type/','/ships/by-nation/','/ships/bismarck/',
                 '/classes/','/classes/bismarck/','/battles/','/battles/denmark-strait/',
                 '/weapons/','/sources/','/help/')) {
  "{0,-28} {1}" -f $p, (curl.exe -sL -x http://127.0.0.1:7897 -m 40 -o NUL -w "%{http_code}" "$u$p")
}
```

**国内直连这个域名会超时（curl 返回 000）**，必须经代理 `http://127.0.0.1:7897`（SakuraCat）。
别人从国内访问也可能不稳，这是 workers.dev 的常态。

## 待办：自定义域名

`dockyard.top` 续费 32 元/年、5 年 142 元（腾讯云价目表），是当前最便宜的可用后缀。
买下后：
1. 把域名 NS 指到 Cloudflare（注册商会问要不要直接用 Cloudflare 解析）。
2. Cloudflare 后台 Workers → archive → Settings → Domains & Routes → Add custom domain。
3. 改 `astro.config.mjs:7` 的默认值，重新 `npm.cmd run build` + `wrangler deploy`。
