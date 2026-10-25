from pathlib import Path
import re

path = Path('equipo/felipe-quiroz.html')
s = path.read_text(encoding='utf-8')

# Remove previous generated logo styles if re-run.
s = re.sub(r'\n?<style id="felipe-experience-logos-v1">.*?</style>\s*', '\n', s, flags=re.S)

css = r'''
<style id="felipe-experience-logos-v1">
.fq-role-brand{min-height:48px;display:flex;align-items:center;margin:0 0 8px}
.fq-role-brand img{display:block;width:auto;height:auto;max-height:38px;object-fit:contain;object-position:left center}
.fq-role-brand--low img{max-width:132px;max-height:34px}
.fq-role-brand--geo img{max-width:148px;max-height:40px}
.fq-role-brand--tether img{max-width:138px;max-height:38px;transform:translateX(-8px)}
@media(max-width:760px){
  .fq-role-brand{min-height:42px;margin-bottom:7px}
  .fq-role-brand--low img{max-width:122px;max-height:31px}
  .fq-role-brand--geo img{max-width:136px;max-height:36px}
  .fq-role-brand--tether img{max-width:128px;max-height:35px;transform:translateX(-6px)}
}
</style>
'''

# Normalize the three experience meta blocks to logo-first presentation.
patterns = [
    (
        r'<div class="fq-role-meta"><b>lowsignal</b><span>Co-Founder &amp; COO</span><small>Growth Systems</small></div>|<div class="fq-role-meta"><b>lowsignal</b><span>Co-Founder & COO</span><small>Growth Systems</small></div>',
        '<div class="fq-role-meta"><div class="fq-role-brand fq-role-brand--low"><img src="https://lowsignal.cl/assets/lowsignal-logo-blue.png" alt="lowsignal"></div><span>Co-Founder & COO</span><small>Growth Systems</small></div>'
    ),
    (
        r'<div class="fq-role-meta"><b>GeoVictoria</b><span>Product Manager</span><small>B2B SaaS · Workforce Management · LATAM / US / EU · 40\+ países</small></div>',
        '<div class="fq-role-meta"><div class="fq-role-brand fq-role-brand--geo"><img src="https://lowsignal.cl/assets/logo-geovictoria.png" alt="GeoVictoria"></div><span>Product Manager</span><small>B2B SaaS · Workforce Management · LATAM / US / EU · 40+ países</small></div>'
    ),
    (
        r'<div class="fq-role-meta"><b>Tether Education</b><span>Head of Partnerships</span><small>EdTech · GovTech · LATAM / US / EU</small></div>',
        '<div class="fq-role-meta"><div class="fq-role-brand fq-role-brand--tether"><img src="https://lowsignal.cl/assets/logo_tether.png" alt="Tether Education"></div><span>Head of Partnerships</span><small>EdTech · GovTech · LATAM / US / EU</small></div>'
    )
]

for pattern, replacement in patterns:
    s = re.sub(pattern, replacement, s, count=1)

s = s.replace('</head>', css + '\n</head>', 1)
path.write_text(s, encoding='utf-8')
