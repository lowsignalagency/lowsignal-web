from pathlib import Path

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')

s = s.replace('.fq-home-cta-inner{width:min(1220px,calc(100% - 128px));min-height:136px;', '.fq-home-cta-inner{width:min(1220px,calc(100% - 128px));min-height:208px;', 1)
s = s.replace('@media(max-width:900px){.fq-home-cta-inner{width:calc(100% - 48px);min-height:148px}}', '@media(max-width:900px){.fq-home-cta-inner{width:calc(100% - 48px);min-height:176px}}', 1)
s = s.replace('@media(max-width:560px){.fq-home-cta-inner{width:calc(100% - 40px);min-height:210px;padding:34px 0;align-items:stretch;justify-content:center;flex-direction:column;gap:24px}', '@media(max-width:560px){.fq-home-cta-inner{width:calc(100% - 40px);min-height:176px;padding:28px 0;align-items:stretch;justify-content:center;flex-direction:column;gap:22px}', 1)

p.write_text(s, encoding='utf-8')
print('matched Felipe CTA sizing to Damian')
