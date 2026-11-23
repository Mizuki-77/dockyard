# 从构建产物里抽出「历任指挥官」区块，核对内容与链接。
import io
import os
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else 'dist/ships/cossack/index.html'
html = io.open(path, encoding='utf-8').read()

i = html.find('历任指挥官')
if i < 0:
    print('没找到「历任指挥官」区块')
    sys.exit(1)

seg = html[i:i + 6000]
# 只取到下一个 section 结束
end = seg.find('cmdrbox__note')
if end > 0:
    seg = seg[:end + 400]

text = re.sub(r'<[^>]+>', '|', seg)
text = re.sub(r'\|{2,}', '|', text)
text = re.sub(r'\s+', ' ', text)
print('=== 区块文本 ===')
print(text[:1800])

print()
print('=== 其中的链接 ===')
for m in re.finditer(r'href="([^"]+)"[^>]*>', seg):
    print('  ', m.group(1))
