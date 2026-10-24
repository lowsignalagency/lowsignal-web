from pathlib import Path
import re

# Keep Karina Ravanal's testimonial avatar at the normal 56px size,
# but crop closer while pulling the face upward inside the fixed circular frame.
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

# Normalize the testimonial markup so the image can zoom inside a fixed-size circle.
plain = '<div class="rechx-person"><img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal"><div><b>Karina Ravanal</b><span>Directora, Colegio Salvador Dalí</span></div></div>'
wrapped = '<div class="rechx-person"><span class="csd-karina-crop"><img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal"></span><div><b>Karina Ravanal</b><span>Directora, Colegio Salvador Dalí</span></div></div>'
if plain in s:
    s = s.replace(plain, wrapped, 1)

style = '''\n<style id="csd-karina-photo-polish">\n.csd-karina-crop{\n  width:56px;\n  height:56px;\n  flex:0 0 56px;\n  border-radius:50%;\n  overflow:hidden;\n  border:2px solid rgba(255,255,255,.5);\n  display:block;\n}\n.csd-karina-crop img{\n  width:100%!important;\n  height:100%!important;\n  max-width:none!important;\n  border:0!important;\n  border-radius:0!important;\n  object-fit:cover!important;\n  object-position:center 26%!important;\n  transform:scale(1.32);\n  transform-origin:center bottom;\n}\n</style>\n'''

s = re.sub(r'\n?<style id="csd-karina-photo-polish">.*?</style>\s*', '\n', s, flags=re.S)
s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')
