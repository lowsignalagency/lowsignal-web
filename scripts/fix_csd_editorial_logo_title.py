from pathlib import Path

# Fix current CSD page.
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')
s = s.replace(
    '<div class="case-editorial-client">\n          <img src="https://lowsignal.cl/assets/logo-dali-darkbg.png" alt="Colegio Salvador Dalí">',
    '<div class="case-editorial-client">\n          <img src="https://lowsignal.cl/assets/logo-dali-maipu.png" alt="Colegio Salvador Dalí">',
    1
)
s = s.replace(
    'Un colegio con mucho que mostrar.<br><strong>Una experiencia digital que debía hacerlo visible.</strong>',
    'Un colegio con mucho que mostrar. <strong>Una experiencia digital que debía hacerlo visible.</strong>',
    1
)

# Keep the Instagram capture anchored to its top edge so the header is visible.
style = '''\n<style id="csd-editorial-image-position-v1">\n.case-editorial-pair img[src*="dali-ig.jpg"]{object-position:center top!important}\n</style>\n'''
if 'id="csd-editorial-image-position-v1"' not in s:
    s = s.replace('</head>', style + '</head>', 1)

p.write_text(s, encoding='utf-8')

# Persist the same fixes in the editorial template config/style.
for path in ['scripts/apply_editorial_case_layout.py']:
    q = Path(path)
    if not q.exists():
        continue
    t = q.read_text(encoding='utf-8')
    t = t.replace(
        "'logo': 'https://lowsignal.cl/assets/logo-dali-darkbg.png'",
        "'logo': 'https://lowsignal.cl/assets/logo-dali-maipu.png'",
        1
    )
    t = t.replace(
        "'context_title': 'Un colegio con mucho que mostrar.<br><strong>Una experiencia digital que debía hacerlo visible.</strong>'",
        "'context_title': 'Un colegio con mucho que mostrar. <strong>Una experiencia digital que debía hacerlo visible.</strong>'",
        1
    )
    css_rule = '.case-editorial-pair img[src*="dali-ig.jpg"]{object-position:center top!important}\\n'
    anchor = '.case-editorial-pair figure:nth-child(2) img{height:100%}\\n'
    if css_rule not in t and anchor in t:
        t = t.replace(anchor, anchor + css_rule, 1)
    q.write_text(t, encoding='utf-8')
