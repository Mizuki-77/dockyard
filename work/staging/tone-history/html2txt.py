import re, sys, os, html

def to_text(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    # strip script/style
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
    # block-level tags -> newline
    t = re.sub(r'(?i)<\s*(br|/p|/tr|/td|/div|/li|/h[1-6]|/pre|/blockquote)\b[^>]*>', '\n', t)
    t = re.sub(r'(?i)<\s*(p|tr|div|li|h[1-6]|pre|blockquote)\b[^>]*>', '\n', t)
    t = re.sub(r'(?i)<\s*/\s*table\s*>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    t = t.replace('\xa0', ' ')
    lines = [re.sub(r'[ \t]+', ' ', ln).strip() for ln in t.split('\n')]
    out = []
    blank = 0
    for ln in lines:
        if not ln:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    return '\n'.join(out)

if __name__ == '__main__':
    for f in sys.argv[1:]:
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_raw', f)
        txt = to_text(p)
        of = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_raw', f + '.txt')
        open(of, 'w', encoding='utf-8').write(txt)
        print(f'{f}: {len(txt)} chars -> {f}.txt')
