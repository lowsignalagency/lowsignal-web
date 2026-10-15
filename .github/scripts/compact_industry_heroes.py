from pathlib import Path

files = [
    ('industrias/educacion.html','edu-new','planes-education'),
    ('industrias/b2b.html','b2b','planes-b2b'),
    ('industrias/marcas-b2c.html','b2c-new','planes-b2c'),
]

for path, prefix, plans_id in files:
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    s = s.replace(f'href="#sistema">Ver sistema</a>', f'href="#{plans_id}">Ver planes</a>', 1)

    style_id = f'industry-hero-compact-stats-v1-{prefix}'
    if style_id in s:
        p.write_text(s, encoding='utf-8')
        continue

    hero = f'.{prefix}-hero'
    meta = f'.{prefix}-hero-meta'

    style = f'''\n<style id="{style_id}">\n/* Shorter industry hero + separated proof band */\n{hero}{{\n  padding:156px 0 48px !important;\n}}\n{meta}{{\n  margin-top:40px !important;\n  border-top:0 !important;\n  border:1px solid #DCE3F2 !important;\n  border-radius:16px !important;\n  background:#F4F6FC !important;\n  overflow:hidden !important;\n  box-shadow:0 18px 44px rgba(7,15,34,.14) !important;\n}}\n{meta}>div{{\n  padding:20px 26px !important;\n  border-right:1px solid #DCE3F2 !important;\n  border-bottom:0 !important;\n}}\n{meta}>div:first-child{{padding-left:26px !important;}}\n{meta}>div:last-child{{border-right:0 !important;}}\n{meta} strong{{\n  color:#10193C !important;\n  font-size:27px !important;\n}}\n{meta} span{{\n  color:#6F7C9D !important;\n  font-size:10px !important;\n}}\n@media(max-width:760px){{\n  {hero}{{padding:124px 0 40px !important;}}\n  {meta}{{\n    margin-top:32px !important;\n    grid-template-columns:1fr !important;\n    border-radius:14px !important;\n  }}\n  {meta}>div,\n  {meta}>div:first-child{{\n    padding:16px 18px !important;\n    border-right:0 !important;\n    border-bottom:1px solid #DCE3F2 !important;\n  }}\n  {meta}>div:last-child{{border-bottom:0 !important;}}\n  {meta} strong{{font-size:24px !important;}}\n}}\n</style>\n'''
    s = s.replace('</head>', style + '</head>', 1)
    p.write_text(s, encoding='utf-8')
    print('Updated', path)
