from pathlib import Path
import re

p = Path('industrias/marcas-b2c.html')
s = p.read_text(encoding='utf-8')

original_url = 'https://lowsignal.cl/assets/logo-centro-comunicaar.png'
broken_url = 'https://lowsignal.cl/assets/logo-centro-comunicaar-transparent.png'
logo = f'<img class="b2cr-trust-comunicaar" src="{original_url}" alt="Centro Comunicaar">'

# Always use the original artwork; remove the light background in-browser with an SVG filter.
s = s.replace(broken_url, original_url)

if original_url not in s:
    needle = '<img src="https://lowsignal.cl/assets/dimor-logo-white-cutout.svg" alt="DIMOR Automotora">'
    if needle not in s:
        raise RuntimeError('DIMOR trust logo anchor not found')
    s = s.replace(needle, needle + logo, 1)

svg_filter = '''<svg id="b2cr-comunicaar-filter-defs" aria-hidden="true" width="0" height="0" style="position:absolute;overflow:hidden;pointer-events:none">
  <defs>
    <filter id="b2cr-comunicaar-key" color-interpolation-filters="sRGB">
      <feColorMatrix type="matrix" values="
        1 0 0 0 0
        0 1 0 0 0
        0 0 1 0 0
        -1.2 -1.2 -1.2 0 3.1"/>
    </filter>
  </defs>
</svg>'''

if 'id="b2cr-comunicaar-filter-defs"' not in s:
    anchor = '<main id="top" class="b2cr-main">'
    if anchor not in s:
        raise RuntimeError('B2C main anchor not found')
    s = s.replace(anchor, svg_filter + '\n' + anchor, 1)

css = '''
<style id="b2c-comunicaar-trust-v1">
.b2cr-trust-grid img.b2cr-trust-comunicaar{
  width:auto!important;
  max-width:68px!important;
  max-height:62px!important;
  object-fit:contain!important;
  object-position:center!important;
  filter:url(#b2cr-comunicaar-key)!important;
  opacity:.95!important;
}
@media(max-width:760px){
  .b2cr-trust-grid img.b2cr-trust-comunicaar{
    max-width:60px!important;
    max-height:54px!important;
  }
}
</style>
'''

pat = re.compile(r'<style id="b2c-comunicaar-trust-v1">.*?</style>', re.S)
if pat.search(s):
    s = pat.sub(css.strip(), s, count=1)
else:
    s = s.replace('</head>', css + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('b2c-comunicaar-trust-v3-keyed-original')
