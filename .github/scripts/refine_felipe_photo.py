from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')
old='@media(max-width:560px){.fq-home-cta-inner{width:calc(100% - 40px);min-height:156px;align-items:flex-start;justify-content:center;flex-direction:column}.fq-home-cta p{font-size:25px}.fq-home-cta a{width:100%}}'
new='@media(max-width:560px){.fq-home-cta-inner{width:calc(100% - 40px);min-height:210px;padding:34px 0;align-items:stretch;justify-content:center;flex-direction:column;gap:24px}.fq-home-cta p{font-size:25px;line-height:1.25}.fq-home-cta a{width:100%;min-height:52px}}'
if old not in s:
    raise SystemExit('mobile CTA styles not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('improved Felipe mobile CTA spacing')
