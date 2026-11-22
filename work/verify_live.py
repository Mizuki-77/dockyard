import re
import urllib.request

UA = 'DockyardArchive/1.0'


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return urllib.request.urlopen(req, timeout=40).read().decode('utf-8', 'replace')


print('=== 首页 h1 ===')
h = fetch('https://archive.dockyard.workers.dev/')
m = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S)
print(f'  {m.group(0)[:100] if m else "❌ 无 h1"}')
print(f'  h1 总数: {len(re.findall(r"<h1[ >]", h))}')

print()
print('=== 提尔皮茨切片 ===')
t = fetch('https://archive.dockyard.workers.dev/ships/tirpitz/')
codes = re.findall(r'"code":"([^"]+)"', t)
titles = re.findall(r'"title":"([^"]+)"', t)
print(f'  切片数: {len(codes)}')
print(f'  代码: {codes}')
# 找「建造」相关
for kw in ['建造', '订购', '舾装']:
    print(f'  含「{kw}」: {"✓" if kw in t else "✗"}')

print()
print('=== 企业号（补了战后切片）===')
e = fetch('https://archive.dockyard.workers.dev/ships/enterprise/')
ecodes = re.findall(r'"code":"([^"]+)"', e)
print(f'  切片: {ecodes}')

print()
print('=== 光辉（I00 起点已修）===')
i = fetch('https://archive.dockyard.workers.dev/ships/illustrious/')
icodes = re.findall(r'"code":"([^"]+)"', i)
print(f'  切片: {icodes}')

print()
print('=== 对比器 C 标记 ===')
c = fetch('https://archive.dockyard.workers.dev/compare/')
print(f'  cmp-tag--conf 逻辑: {"✓" if "cmp-tag--conf" in c else "✗"}')
