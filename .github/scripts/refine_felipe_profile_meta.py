from pathlib import Path

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')

# GeoVictoria scope
s = s.replace(
    '<small>B2B SaaS · Workforce Management</small>',
    '<small>B2B SaaS · Workforce Management · LATAM / US / EU · 40+ países</small>',
    1
)

# Hero heading spacing: keep the large editorial treatment, add air between lines.
s = s.replace(
    '.fq-hero-copy h1{margin:20px 0 0;font-size:clamp(64px,7vw,96px);line-height:.92;letter-spacing:-.065em;font-weight:300}.fq-hero-copy h1 span{color:var(--fq-lav2);font-weight:500}',
    '.fq-hero-copy h1{margin:20px 0 0;font-size:clamp(64px,7vw,96px);line-height:1;letter-spacing:-.065em;font-weight:300}.fq-hero-copy h1 span{display:inline-block;margin-top:.04em;color:var(--fq-lav2);font-weight:500}',
    1
)

# Keep the back link below the floating navbar.
s = s.replace(
    '.fq-profile{margin-top:-100px;padding:162px 0 82px;',
    '.fq-profile{margin-top:-100px;padding:214px 0 82px;',
    1
)
s = s.replace(
    '@media(max-width:760px){.fq-shell{width:calc(100% - 40px)}.fq-profile{padding:132px 0 62px}',
    '@media(max-width:760px){.fq-shell{width:calc(100% - 40px)}.fq-profile{padding:158px 0 62px}',
    1
)

p.write_text(s, encoding='utf-8')
print('Refined Felipe profile metadata, heading spacing and back link spacing')
