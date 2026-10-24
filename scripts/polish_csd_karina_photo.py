from pathlib import Path
import re

# Keep Karina Ravanal's testimonial avatar simple and natural:
# normal 56px circle, no zoom/transform, only a slightly higher crop.
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

plain = '<div class="rechx-person"><img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal"><div><b>Karina Ravanal</b><span>Directora, Colegio Salvador Dalí</span></div></div>'
wrapped = '<div class="rechx-person"><span class="csd-karina-crop"><img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal"></span><div><b>Karina Ravanal</b><span>Directora, Colegio Salvador Dalí</span></div></div>'
if plain in s:
    s = s.replace(plain, wrapped, 1)

style = '''\n<style id="csd-karina-photo-polish">\n.csd-karina-crop{\n  width:56px;\n  height:56px;\n  flex:0 0 56px;\n  border-radius:50%;\n  overflow:hidden;\n  border:1px solid rgba(255,255,255,.28);\n  display:block;\n}\n.csd-karina-crop img{\n  width:100%!important;\n  height:100%!important;\n  max-width:none!important;\n  border:0!important;\n  border-radius:0!important;\n  object-fit:cover!important;\n  object-position:center 18%!important;\n  transform:none!important;\n}\n</style>\n'''

s = re.sub(r'\n?<style id="csd-karina-photo-polish">.*?</style>\s*', '\n', s, flags=re.S)
s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')
