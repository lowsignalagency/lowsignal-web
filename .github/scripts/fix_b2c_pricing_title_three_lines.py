from pathlib import Path

p = Path('industrias/marcas-b2c.html')
s = p.read_text(encoding='utf-8')

old = '<h2>Una base clara para crecer.<br><strong>Elige cuánto quieres acelerar.</strong></h2>'
new = '<h2>Una base clara para crecer.<br><strong>Elige cuánto quieres<br class="b2c-pricing-title-break">acelerar.</strong></h2>'
if old not in s:
    raise SystemExit('Expected B2C pricing title not found')
s = s.replace(old, new, 1)

style = '''\n<style id="b2c-pricing-title-three-lines-v1">\n@media(min-width:981px){\n  .b2c-pricing-head{\n    grid-template-columns:minmax(0,1.42fr) minmax(270px,.58fr) !important;\n    gap:48px !important;\n  }\n  .b2c-pricing-head h2{\n    max-width:820px !important;\n    font-size:clamp(42px,3.45vw,52px) !important;\n  }\n}\n@media(max-width:980px){\n  .b2c-pricing-title-break{display:none}\n}\n</style>\n'''
if 'b2c-pricing-title-three-lines-v1' not in s:
    s = s.replace('</head>', style + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('B2C pricing title set to max three lines on desktop')
