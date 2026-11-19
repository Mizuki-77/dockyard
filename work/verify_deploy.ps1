$urls = @(
  'https://archive.dockyard.workers.dev/',
  'https://archive.dockyard.workers.dev/weapons/',
  'https://archive.dockyard.workers.dev/weapons/38cm-sk-c34/',
  'https://archive.dockyard.workers.dev/weapons/type-284/',
  'https://archive.dockyard.workers.dev/weapons/swordfish/',
  'https://archive.dockyard.workers.dev/battles/',
  'https://archive.dockyard.workers.dev/battles/denmark-strait/',
  'https://archive.dockyard.workers.dev/ships/',
  'https://archive.dockyard.workers.dev/ships/bismarck/',
  'https://archive.dockyard.workers.dev/ships/illustrious/',
  'https://archive.dockyard.workers.dev/ships/hood/',
  'https://archive.dockyard.workers.dev/ships/king-george-v/',
  'https://archive.dockyard.workers.dev/ships/tirpitz/',
  'https://archive.dockyard.workers.dev/classes/illustrious/',
  'https://archive.dockyard.workers.dev/operations/rheinubung/',
  'https://archive.dockyard.workers.dev/sources/',
  'https://archive.dockyard.workers.dev/help/',
  'https://archive.dockyard.workers.dev/img/weapons/type-284-hood-1941-last-photo.jpg',
  'https://archive.dockyard.workers.dev/img/weapons/swordfish-hms-victorious-bismarck-strike.jpg',
  'https://archive.dockyard.workers.dev/img/ships/illustrious-1945-far-east-overhead.jpg'
)
foreach ($u in $urls) {
  $code = curl.exe -x http://127.0.0.1:7897 -s -o NUL -w "%{http_code} %{size_download}" --max-time 45 $u
  Write-Output "$code  $u"
}
