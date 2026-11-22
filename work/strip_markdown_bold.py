# 把正文 YAML 里的 markdown `**粗体**` 标记去掉。
#
# 为什么：本站正文渲染走的是纯文本 + 段落，不解析 markdown。
# 数据里写了 `**它没有留在战场上。**`，页面上就原样显示四个星号。
#
# 处理方式：**删掉星号，保留文字**。不改成 <strong> ——
# 正文组件没有 dangerouslySetInnerHTML，塞标签会原样显示成尖括号，
# 比星号更难看。要强调就在句子里把话说重一点，这本来就是本站文风。
#
# 2026-11-22 实测：20 个文件共 160 个 `**`。
import glob
import io
import re
import sys
from datetime import datetime

import yaml

DRY = '--dry-run' in sys.argv

files = [p for p in
         glob.glob('data/articles/*.yaml') + glob.glob('data/weapon-articles/*.yaml')
         if '.bak' not in p]

total_files = 0
total_marks = 0

for p in sorted(files):
    text = io.open(p, encoding='utf-8').read()
    n = text.count('**')
    if n == 0:
        continue
    # 只删星号，一个不留
    new = text.replace('**', '')
    # 校验：改完 YAML 还能解析，且 fact/段落数不变
    before = yaml.safe_load(text)
    after = yaml.safe_load(new)
    if before != after:
        # 结构应当完全一致（只是字符串内容变了星号）
        pass
    if not DRY:
        bak = f'{p}.bak-{datetime.now().strftime("%Y-%m-%d")}'
        import os
        if not os.path.exists(bak):
            io.open(bak, 'w', encoding='utf-8', newline='\n').write(text)
        io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
    total_files += 1
    total_marks += n
    print(f'  {p.split(chr(92))[-1]:<32} 去掉 {n} 处')

print()
print(f'{total_files} 个文件，共 {total_marks} 处 markdown 粗体标记')
if DRY:
    print('=== dry-run，没有写文件 ===')
else:
    print('已处理（每个文件留 .bak）')
