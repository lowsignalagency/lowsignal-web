from pathlib import Path
import re

p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

# Remove prior correction layer if rerun.
s = re.sub(r'\n?<style id="csd-final-alignment-fix">.*?</style>\s*', '\n', s, flags=re.S)

# Restore the CSD media that belonged to the case before the rebuild.
s = s.replace('https://lowsignal.cl/assets/csd_visita.jpg', 'https://lowsignal.cl/assets/dali-ig.jpg')
# In the work gallery, the secondary image should be the school/patio image.
s = re.sub(
    r'(<figure><img src=")https://lowsignal\.cl/assets/dali-ig\.jpg(" alt="Contenido digital Colegio Salvador Dalí"></figure>)',
    r'\1https://lowsignal.cl/assets/dali-patio-nueva.jpg\2',
    s,
    count=1
)
# Restore the next-case visual used by the original FCCT card.
s = s.replace('https://lowsignal.cl/assets/lanzamiento-web_fcct.jpg', 'https://lowsignal.cl/assets/crecer-ninos.png')

# Final, high-specificity alignment layer: same visible guide as the RECH/nav layout.
style = r'''
<style id="csd-final-alignment-fix">
.csdx .csdx-wrap{
  width:min(1220px,calc(100vw - 128px))!important;
  max-width:1220px!important;
  margin-left:auto!important;
  margin-right:auto!important;
}
.csdx .csdx-quote-inner{max-width:1220px!important}
@media(max-width:1000px){
  .csdx .csdx-wrap{
    width:calc(100vw - 48px)!important;
    max-width:calc(100vw - 48px)!important;
  }
}
@media(max-width:760px){
  .csdx .csdx-wrap{
    width:calc(100vw - 24px)!important;
    max-width:calc(100vw - 24px)!important;
  }
}
</style>
'''
s = s.replace('</head>', style + '\n</head>', 1)

# Trigger note: keep this fixer as the canonical post-rebuild correction layer.
p.write_text(s, encoding='utf-8')
