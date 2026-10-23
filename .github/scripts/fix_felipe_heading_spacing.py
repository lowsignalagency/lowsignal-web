from pathlib import Path

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')

old = '.fq-hero-copy h1{margin:20px 0 0;font-size:clamp(64px,7vw,96px);line-height:.92;letter-spacing:-.065em;font-weight:300}.fq-hero-copy h1 span{color:var(--fq-lav2);font-weight:500}'
new = '.fq-hero-copy h1{margin:20px 0 0;font-size:clamp(64px,7vw,96px);line-height:1;letter-spacing:-.065em;font-weight:300}.fq-hero-copy h1 span{display:inline-block;margin-top:.04em;color:var(--fq-lav2);font-weight:500}'

if old not in s:
    raise SystemExit('Felipe heading styles not found')

s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
print('Updated Felipe heading spacing')
