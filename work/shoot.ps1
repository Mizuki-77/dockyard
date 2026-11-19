param(
  [string[]]$Pages = @(
    'weapons', 'weapons/38cm-sk-c34', 'weapons/15in-42-mk1',
    'battles', 'battles/denmark-strait',
    'ships/bismarck', 'ships/king-george-v'
  ),
  [int]$W = 1440
)
$out = "$env:TEMP\dshshots"
New-Item -ItemType Directory -Force -Path $out | Out-Null
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
foreach ($p in $Pages) {
  $slug = ($p -replace '/', '-')
  $f = Join-Path $out "$slug.png"
  & $chrome --headless=new --disable-gpu --hide-scrollbars --no-first-run `
    --user-data-dir="$env:TEMP\prof2" --window-size="$W,2200" `
    --virtual-time-budget=9000 --screenshot="$f" "http://localhost:4321/$p/" 2>$null | Out-Null
  if (Test-Path $f) {
    Copy-Item $f "work\shots\tree\$slug.png" -Force
    $kb = [math]::Round((Get-Item $f).Length / 1KB)
    Write-Output "OK  $p  ->  work\shots\tree\$slug.png ($kb KB)"
  } else {
    Write-Output "FAIL $p"
  }
}
