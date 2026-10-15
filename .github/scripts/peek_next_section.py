from pathlib import Path

files = [
    ('industrias/educacion.html', 'edu-new'),
    ('industrias/b2b.html', 'b2b'),
]

for path, prefix in files:
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    style_id = f'industry-next-section-peek-v1-{prefix}'
    if style_id in s:
        print('Already present', path)
        continue

    hero = f'.{prefix}-hero'
    context = f'.{prefix}-context'
    style = f'''\n<style id="{style_id}">\n/* Keep the next section visible sooner after the hero */\n{hero}{{padding:140px 0 52px !important;}}\n{context}{{padding-top:76px !important;}}\n@media(max-width:760px){{\n  {hero}{{padding:118px 0 44px !important;}}\n  {context}{{padding-top:62px !important;}}\n}}\n</style>\n'''
    s = s.replace('</head>', style + '</head>', 1)
    p.write_text(s, encoding='utf-8')
    print('Updated', path)
