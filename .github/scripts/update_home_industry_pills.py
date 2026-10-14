from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = {
    '<a class="lsr-pill" href="https://lowsignal.cl/industrias/educacion">Para Educación</a>': '<a class="lsr-pill" href="#industrias">PARA COLEGIOS / PROVEEDORES DE EDUCACIÓN</a>',
    '<a class="lsr-pill" href="https://lowsignal.cl/industrias/b2b">Para Empresas B2B</a>': '<a class="lsr-pill" href="#industria-b2b">PARA B2B / EMPRESAS</a>',
    '<a class="lsr-pill" href="https://lowsignal.cl/industrias/b2c">Para Marcas B2C</a>': '<a class="lsr-pill" href="#industria-b2c">PARA B2C / MARCAS</a>',
    '<section class="low-industry-section low-industry-b2b">': '<section class="low-industry-section low-industry-b2b" id="industria-b2b">',
    '<section class="low-industry-section low-industry-b2c">': '<section class="low-industry-section low-industry-b2c" id="industria-b2c">',
}

for old, new in replacements.items():
    if old not in s:
        raise SystemExit(f'Missing expected text: {old}')
    s = s.replace(old, new, 1)

style = '''\n<style id="home-industry-anchor-offset-v1">\n#industrias,#industria-b2b,#industria-b2c{scroll-margin-top:96px}\n</style>\n'''
if 'home-industry-anchor-offset-v1' not in s:
    s = s.replace('</head>', style + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('Updated Home industry pills and internal anchors')
