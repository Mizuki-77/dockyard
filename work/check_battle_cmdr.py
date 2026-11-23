# 核对战役页的「参战指挥官」区块。
import io
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else 'dist/battles/last-battle/index.html'
html = io.open(path, encoding='utf-8').read()

i = html.find('参战指挥官')
print(f'{path}: {"找到" if i >= 0 else "没找到"} 「参战指挥官」 at {i}')
if i < 0:
    sys.exit(0)

seg = html[i:i + 3500]
text = re.sub(r'<[^>]+>', '|', seg)
text = re.sub(r'\|{2,}', '|', text)
text = re.sub(r'\s+', ' ', text)
print()
print('=== 区块文本 ===')
print(text[:1200])

print()
print('=== 链接 ===')
for m in re.finditer(r'href="(/commanders/[^"]+)"', seg):
    print('  ', m.group(1))
