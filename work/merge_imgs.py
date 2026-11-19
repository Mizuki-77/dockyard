"""把 work/imgfrag/*.yaml 的分片合并进 data/images.yaml。

为什么不用 yaml.dump 重写整个文件：
  images.yaml 顶部有 10 行注释记录授权三档规则与 IWM 判例，yaml.dump 会把
  注释和 flow 排版全部丢掉。所以这里只做文本追加——读分片、逐条序列化成
  块式映射、接在主表末尾。

字段顺序照主表现有条目：id/file/subject/title/part/view/date/license/
license_tier/license_raw/author/credit/source_url/width/height[/primary]/note
"""
import yaml, glob, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REQ = ['id', 'file', 'subject', 'title', 'part', 'view', 'date', 'license',
       'license_tier', 'license_raw', 'author', 'credit', 'source_url',
       'width', 'height']


def q(v: str) -> str:
    """YAML 双引号标量。note 里常有 `: ` 和引号，不转义就会把文档写坏。"""
    s = str(v).replace('\\', '\\\\').replace('"', '\\"')
    return f'"{s}"'


base = yaml.safe_load(open('data/images.yaml', encoding='utf-8'))
existing = {x['id'] for x in base['images']}
existing_files = {x.get('file') for x in base['images'] if x.get('file')}
print(f'主表现有 {len(existing)} 条')

blocks, added, skipped = [], 0, []
for f in sorted(glob.glob('work/imgfrag/*.yaml')):
    d = yaml.safe_load(open(f, encoding='utf-8'))
    for x in d.get('images') or []:
        if x['id'] in existing:
            skipped.append(f"重复 id {x['id']}")
            continue
        if x.get('file') and x['file'] in existing_files:
            skipped.append(f"重复 file {x['file']}")
            continue
        if not os.path.exists('public' + x['file']):
            skipped.append(f"文件不存在 {x['file']}")
            continue
        miss = [k for k in REQ if k not in x]
        if miss:
            skipped.append(f"缺字段 {x['id']}: {miss}")
            continue

        L = [f"  - id: {x['id']}",
             f"    file: {x['file']}",
             f"    subject: {x['subject']}",
             "    title:",
             f"      zh: {q(x['title']['zh'])}",
             f"      en: {q(x['title']['en'])}"]
        for k in ['part', 'view', 'date', 'license', 'license_tier']:
            if x.get(k) is not None:
                L.append(f"    {k}: {x[k]}")
        for k in ['license_raw', 'author', 'credit', 'source_url']:
            if x.get(k):
                L.append(f"    {k}: {q(x[k])}")
        L.append(f"    width: {x['width']}")
        L.append(f"    height: {x['height']}")
        if x.get('primary'):
            L.append("    primary: true")
        if x.get('note'):
            n = str(x['note']).replace('\n', ' ')
            # 双引号会转义，保留 YAML 语义
            L.append(f"    note: {q(n)}")
        blocks.append('\n'.join(L))
        added += 1

if skipped:
    print('跳过：')
    for s in skipped:
        print('  -', s)

text = open('data/images.yaml', encoding='utf-8').read().rstrip('\n')
text += '\n\n' + '\n\n'.join(blocks) + '\n'
open('data/images.yaml', 'w', encoding='utf-8', newline='\n').write(text)

# 回读验证
chk = yaml.safe_load(open('data/images.yaml', encoding='utf-8'))
print(f'新增 {added} 条；合并后 {len(chk["images"])} 条')
ids = [x['id'] for x in chk['images']]
assert len(ids) == len(set(ids)), '存在重复 id'
print('id 唯一性 OK')
