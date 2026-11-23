# Đổi tên miền trong bản sao từ sihylens.vn sang sihy.vn; canonical giữ về sihylens.vn (tránh trùng lặp nội dung trên Google).
import os, re, sys
root = sys.argv[1] if len(sys.argv) > 1 else '.'
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d not in ('.git', 'images', '.github')]
    for f in fn:
        if not f.endswith(('.html', '.js', '.json', '.xml', '.txt', '.css')): continue
        p = os.path.join(dp, f); s = open(p, encoding='utf-8').read(); o = s
        s = s.replace('<link rel="canonical" href="https://sihylens.vn', '@@CAN@@')
        s = s.replace('https://sihylens.vn', 'https://sihy.vn').replace('>sihylens.vn<', '>sihy.vn<').replace(' sihylens.vn', ' sihy.vn')
        s = s.replace('@@CAN@@', '<link rel="canonical" href="https://sihylens.vn')
        if s != o: open(p, 'w', encoding='utf-8').write(s)
