$urls = @(
  'https://archive.dockyard.workers.dev/weapons/',
  'https://archive.dockyard.workers.dev/weapons/15in-42-mk1/',
  'https://archive.dockyard.workers.dev/weapons/type-284/'
)
foreach ($u in $urls) {
  $code = curl.exe -x http://127.0.0.1:7897 -s -o NUL -w "%{http_code}" --max-time 45 $u
  Write-Output "$code  $u"
}

# 抓线上 HTML，确认三层树真的在
$body = curl.exe -x http://127.0.0.1:7897 -s --max-time 45 "https://archive.dockyard.workers.dev/weapons/"
$branch = ([regex]::Matches($body, 'ctree__branch')).Count
$group  = ([regex]::Matches($body, 'ctree__group')).Count
$leaf   = ([regex]::Matches($body, 'ctree__leaf"')).Count
$nat    = ([regex]::Matches($body, 'natblock__label')).Count
Write-Output "branch=$branch group=$group leaf=$leaf natblock=$nat"

# 抽几个路径样例
$gl = [regex]::Matches($body, 'ctree__glabel[^>]*>([^<]+)<')
$ll = [regex]::Matches($body, 'ctree__llabel[^>]*>([^<]+)<')
Write-Output "国别组: $($gl.Count)  型号叶子: $($ll.Count)"
$gl | Select-Object -First 6 | ForEach-Object { Write-Output "  - $($_.Groups[1].Value)" }
