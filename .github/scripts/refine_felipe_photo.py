from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')

# Restore breathing room below the fixed desktop navbar.
s=s.replace('.fq-editorial-profile{padding:112px 0 72px;background:#fff;color:#0D1420}', '.fq-editorial-profile{padding:142px 0 82px;background:#fff;color:#0D1420}', 1)

# Match the Home content container instead of using a narrower profile-only shell.
s=s.replace('.fq-editorial-shell{width:min(1180px,calc(100% - 96px));margin:0 auto}', '.fq-editorial-shell{width:min(1480px,calc(100% - 160px));margin:0 auto}', 1)

# Keep the actual profile composition comfortably editorial inside the wider site margins.
s=s.replace('.fq-editorial-grid{display:grid;grid-template-columns:minmax(380px,.82fr) minmax(0,1.18fr);gap:76px;align-items:center}', '.fq-editorial-grid{display:grid;grid-template-columns:minmax(400px,.78fr) minmax(0,1.22fr);gap:84px;align-items:center;max-width:1320px;margin:0 auto}', 1)

# Responsive profile margins follow the same Home rhythm.
s=s.replace('@media(max-width:900px){.fq-editorial-profile{padding:104px 0 60px}.fq-editorial-shell{width:calc(100% - 48px)}', '@media(max-width:1440px){.fq-editorial-shell{width:calc(100% - 112px)}}\n@media(max-width:900px){.fq-editorial-profile{padding:124px 0 68px}.fq-editorial-shell{width:calc(100% - 48px)}', 1)
s=s.replace('@media(max-width:560px){.fq-editorial-shell{width:calc(100% - 32px)}.fq-editorial-profile{padding:98px 0 48px}', '@media(max-width:560px){.fq-editorial-shell{width:calc(100% - 40px)}.fq-editorial-profile{padding:112px 0 54px}', 1)

# Tighten the Home-style CTA band and match its inner content margins to the site container.
s=s.replace('.fq-home-cta-inner{width:min(1180px,calc(100% - 96px));min-height:208px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:40px}', '.fq-home-cta-inner{width:min(1480px,calc(100% - 160px));min-height:136px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:40px}', 1)
s=s.replace('@media(max-width:900px){.fq-home-cta-inner{width:calc(100% - 48px);min-height:190px}}', '@media(max-width:1440px){.fq-home-cta-inner{width:calc(100% - 112px)}}\n@media(max-width:900px){.fq-home-cta-inner{width:calc(100% - 48px);min-height:148px}}', 1)
s=s.replace('@media(max-width:560px){.fq-home-cta-inner{width:calc(100% - 32px);min-height:190px;align-items:flex-start;justify-content:center;flex-direction:column}', '@media(max-width:560px){.fq-home-cta-inner{width:calc(100% - 40px);min-height:156px;align-items:flex-start;justify-content:center;flex-direction:column}', 1)

p.write_text(s, encoding='utf-8')
print('aligned Felipe profile to site margins, restored navbar breathing room, tightened CTA band')
