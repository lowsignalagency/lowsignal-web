from pathlib import Path
import re

configs = [
    {
        'path':'industrias/educacion.html',
        'meta':'edu-new-hero-meta',
        'old_title':'<span class="edu-title-desktop">Presencia digital que<br>genera <strong>confianza.</strong></span>',
        'new_title':'<span class="edu-title-desktop">Presencia digital que<br>genera <strong>confianza.</strong></span>',
        'prefix':'edu-new',
    },
    {
        'path':'industrias/b2b.html',
        'meta':'b2b-hero-meta',
        'old_title':'<h1>Convierte presencia digital<br> en <strong>oportunidades comerciales.</strong></h1>',
        'new_title':'<h1>Convierte presencia digital<br>en <strong>oportunidades comerciales.</strong></h1>',
        'prefix':'b2b',
    },
    {
        'path':'industrias/marcas-b2c.html',
        'meta':'b2c-new-hero-meta',
        'old_title':'<h1>Marcas que la gente<br> elige y vuelve a<br> <strong>elegir.</strong></h1>',
        'new_title':'<h1>Marcas que la gente elige<br>y vuelve a <strong>elegir.</strong></h1>',
        'prefix':'b2c-new',
    },
]

for c in configs:
    p = Path(c['path'])
    s = p.read_text(encoding='utf-8')

    if c['old_title'] in s:
        s = s.replace(c['old_title'], c['new_title'], 1)
    elif c['new_title'] not in s:
        print(f"WARN title pattern not found in {c['path']}")

    # Remove the metrics/proof block immediately below the hero CTAs.
    pat = rf'\n\s*<div class="{re.escape(c["meta"])}">.*?</div>\s*</div>\s*</section>'
    m = re.search(pat, s, flags=re.S)
    if not m:
        raise SystemExit(f"Hero meta block not found in {c['path']}")
    replacement = '\n    </div>\n  </section>'
    s = s[:m.start()] + replacement + s[m.end():]

    # Replace the previous compact/meta override with a clean hero-only override.
    style_id = f'industry-hero-compact-stats-v1-{c["prefix"]}'
    s = re.sub(
        rf'\n?<style id="{re.escape(style_id)}">.*?</style>\n?',
        '\n',
        s,
        flags=re.S,
    )

    hero_class = f'.{c["prefix"]}-hero'
    h1_class = f'.{c["prefix"]}-hero h1'
    style = f'''\n<style id="industry-hero-clean-v2-{c['prefix']}">\n/* Compact industry hero without duplicated metrics */\n{hero_class}{{padding:156px 0 68px !important;}}\n{h1_class}{{max-width:1120px !important;}}\n@media(max-width:760px){{\n  {hero_class}{{padding:124px 0 52px !important;}}\n  {h1_class}{{max-width:100% !important;}}\n}}\n</style>\n'''
    if f'industry-hero-clean-v2-{c["prefix"]}' not in s:
        s = s.replace('</head>', style + '</head>', 1)

    p.write_text(s, encoding='utf-8')
    print('Updated', c['path'])
