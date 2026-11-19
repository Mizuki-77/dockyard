param(
  [int]$W = 1440,
  [string]$Prefix = ""
)
$pages = @(
  'weapons', 'weapons/38cm-sk-c34',
  'battles', 'battles/denmark-strait',
  'ships/bismarck'
)
$out = "$env:TEMP\dshshots"
New-Item -ItemType Directory -Force -Path $out | Out-Null
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
foreach ($p in $pages) {
  $slug = ($p -replace '/', '-')
  $name = "$Prefix$slug-$W"
  $f = Join-Path $out "$name.png"
  if (Test-Path $f) { Remove-Item $f -Force }
  & $chrome --headless=new --disable-gpu --hide-scrollbars --no-first-run `
    --user-data-dir="$env:TEMP\prof3" --window-size="$W,1800" `
    --virtual-time-budget=9000 --screenshot="$f" "http://localhost:4321/$p/" 2>$null | Out-Null
  if (Test-Path $f) {
    Copy-Item $f "work\shots\tree\$name.png" -Force
    Write-Output "OK  $p @${W}  ->  $name.png"
  } else {
    Write-Output "FAIL $p @${W}"
  }
}
