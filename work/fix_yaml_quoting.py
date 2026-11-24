# 修复写入 images.yaml 时产生的 YAML 语法错误
#
# 根因：author / note 字段里含换行或单引号，我手写文本拼接时只替换了 ' → ''，
# 但没处理换行（换行在单引号标量里会变成多行续接，破坏结构）。
# 正确做法：改用 yaml.safe_dump 生成单条文本再嵌入 —— 但它会改写整篇。
# 折中：先把所有单行化（换行 → 空格），再检查引号配对。
import io
import re
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
IMGS = 'data/images.yaml'

text = io.open(IMGS, encoding='utf-8').read()
lines = text.split('\n')
fixed = 0
out = []
i = 0
while i < len(lines):
    line = lines[i]
    # 检测「以 ' 开头但同一行没有闭合」的行
    stripped = line.strip()
    if stripped.startswith(('author:', 'note:', 'credit:', 'title:', 'license_raw:', 'en:', 'zh:')):
        # 数该行里未转义的单引号
        s = line
        # 已经是安全单行的正常跳过
        if s.count("'") % 2 == 1:
            # 未闭合：把后续行合并进来，直到引号配平
            merged = s
            j = i + 1
            while j < len(lines) and merged.count("'") % 2 == 1:
                merged = merged.rstrip('\n') + ' ' + lines[j].strip()
                j += 1
            # 合并后仍不配平 → 强行在末尾补一个引号
            if merged.count("'") % 2 == 1:
                merged = merged + "'"
            out.append(merged)
            fixed += 1
            i = j
            continue
    out.append(line)
    i += 1

new_text = '\n'.join(out)

# 校验
try:
    d = yaml.safe_load(new_text)
    print(f'YAML 解析 OK，{len(d["images"])} 条图片')
    shutil.copy2(IMGS, f'{IMGS}.bak-broken-{STAMP}')
    with io.open(IMGS, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_text)
    print(f'修复 {fixed} 处换行引号问题，已写回')
except Exception as e:
    print('仍有语法错误:', str(e)[:300])
    # 定位
    m = re.search(r'line (\d+)', str(e))
    if m:
        n = int(m.group(1))
        for k in range(max(0, n - 4), min(len(out), n + 3)):
            print(f'  {k+1}: {out[k][:130]}')
