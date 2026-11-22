import io
import re

h = io.open('dist/index.html', encoding='utf-8').read()

# 去掉 astro 注入的 data-astro-cid 属性，方便正则
h2 = re.sub(r'\s*data-astro-cid-\w+', '', h)

print('=== 舰艇清单 ===')
for m in re.finditer(r'<span class="smgroup__nation">([^<]+)</span>\s*<span class="smgroup__n">(\d+)</span>', h2):
    name, n = m.group(1), m.group(2)
    # 找该分组后面的所有 smlink
    start = m.end()
    end = h2.find('</div>', start)
    seg = h2[start:end]
    links = re.findall(r'class="smlink" href="([^"]+)"[^>]*>\s*([^<]+?)\s*</a>', seg)
    print(f'  {name} ({n}): {", ".join(x[1] for x in links)}')

print()
print('=== 战役与进度 ===')
for m in re.finditer(r'class="smlink smlink--row" href="([^"]+)"[^>]*>\s*<span>([^<]+)</span>\s*<span class="(smprog[^"]*)">\s*(\d+/\d+)', h2):
    href, name, cls, prog = m.groups()
    full = '✓全通' if 'smprog--full' in cls else '  缺'
    print(f'  {name:<12} {prog:<6} {full}  {href}')

print()
print('=== 行动分组 ===')
for m in re.finditer(r'<span class="smgroup__nation">([^<]+)</span>', h2):
    print(f'  {m.group(1)}')

print()
print('=== 按类别浏览 ===')
for m in re.finditer(r'class="smcut" href="([^"]+)"[^>]*>\s*<span class="smcut__label">([^<]+)</span>\s*<span class="smcut__n">(\d+)', h2):
    print(f'  {m.group(2)}: {m.group(3)}')

print()
print('=== 行链接 ===')
for m in re.finditer(r'class="smrowlink" href="([^"]+)"[^>]*>\s*([^<]+?)\s*(?:<span class="smrowlink__n">(\d+)</span>)?\s*→', h2):
    n = f' ({m.group(3)})' if m.group(3) else ''
    print(f'  {m.group(2).strip()}{n}  -> {m.group(1)}')

print()
print('=== 武器类别 ===')
for m in re.finditer(r'<span class="smwcat">\s*([^<]+?)\s*<span class="smwcat__n">(\d+)', h2):
    print(f'  {m.group(1)}: {m.group(2)}')

print()
print(f'侧栏链接总数: {len(re.findall(r"class=.smlink", h2)) + len(re.findall(r"class=.smcut", h2)) + len(re.findall(r"class=.smrowlink", h2))}')
