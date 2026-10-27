from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')

# Align the profile and CTA exactly to the visible desktop navbar edges.
s=s.replace('.fq-editorial-shell{width:min(1480px,calc(100% - 160px));margin:0 auto}', '.fq-editorial-shell{width:min(1220px,calc(100% - 128px));margin:0 auto}', 1)
s=s.replace('.fq-editorial-grid{display:grid;grid-template-columns:minmax(400px,.78fr) minmax(0,1.22fr);gap:84px;align-items:center;max-width:1320px;margin:0 auto}', '.fq-editorial-grid{display:grid;grid-template-columns:minmax(380px,.82fr) minmax(0,1.18fr);gap:76px;align-items:center}', 1)
s=s.replace('@media(max-width:1440px){.fq-editorial-shell{width:calc(100% - 112px)}}\n@media(max-width:900px){.fq-editorial-profile{padding:124px 0 68px}.fq-editorial-shell{width:calc(100% - 48px)}', '@media(max-width:1100px) and (min-width:761px){.fq-editorial-shell{width:calc(100% - 48px)}}\n@media(max-width:900px){.fq-editorial-profile{padding:124px 0 68px}.fq-editorial-shell{width:calc(100% - 48px)}', 1)

s=s.replace('.fq-home-cta-inner{width:min(1480px,calc(100% - 160px));min-height:136px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:40px}', '.fq-home-cta-inner{width:min(1220px,calc(100% - 128px));min-height:136px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:40px}', 1)
s=s.replace('@media(max-width:1440px){.fq-home-cta-inner{width:calc(100% - 112px)}}\n@media(max-width:900px){.fq-home-cta-inner{width:calc(100% - 48px);min-height:148px}}', '@media(max-width:1100px) and (min-width:761px){.fq-home-cta-inner{width:calc(100% - 48px)}}\n@media(max-width:900px){.fq-home-cta-inner{width:calc(100% - 48px);min-height:148px}}', 1)

p.write_text(s, encoding='utf-8')
print('aligned Felipe profile and CTA exactly to visible navbar margins')
