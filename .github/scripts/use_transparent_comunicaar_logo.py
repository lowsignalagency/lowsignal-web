from pathlib import Path

p = Path('industrias/marcas-b2c.html')
s = p.read_text(encoding='utf-8')
s = s.replace(
    'https://lowsignal.cl/assets/logo-centro-comunicaar.png',
    'https://lowsignal.cl/assets/logo-centro-comunicaar-transparent.png'
)
p.write_text(s, encoding='utf-8')
print('use-transparent-comunicaar-logo')
