from pathlib import Path
import re

p = Path('industrias/marcas-b2c.html')
s = p.read_text(encoding='utf-8')

logo = '<img class="b2cr-trust-comunicaar" src="https://lowsignal.cl/assets/logo-centro-comunicaar.png" alt="Centro Comunicaar">'

if 'logo-centro-comunicaar.png' not in s:
    needle = '<img src="https://lowsignal.cl/assets/dimor-logo-white-cutout.svg" alt="DIMOR Automotora">'
    if needle not in s:
        raise RuntimeError('DIMOR trust logo anchor not found')
    s = s.replace(needle, needle + logo, 1)

css = '''\n<style id="b2c-comunicaar-trust-v1">\n.b2cr-trust-grid img.b2cr-trust-comunicaar{max-width:138px!important;max-height:46px!important;object-fit:contain!important;object-position:center!important}\n@media(max-width:760px){.b2cr-trust-grid img.b2cr-trust-comunicaar{max-width:118px!important;max-height:40px!important}}\n</style>\n'''

pat = re.compile(r'<style id="b2c-comunicaar-trust-v1">.*?</style>', re.S)
if pat.search(s):
    s = pat.sub(css.strip(), s, count=1)
else:
    s = s.replace('</head>', css + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('b2c-comunicaar-trust-v1')
