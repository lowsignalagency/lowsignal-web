from pathlib import Path
import re

# Keep Karina Ravanal's testimonial portrait framed closer and higher.
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

style = '''\n<style id="csd-karina-photo-polish">\n.case-new-testimonial .case-new-person img{\n  width:68px!important;\n  height:68px!important;\n  object-fit:cover!important;\n  object-position:center 18%!important;\n}\n</style>\n'''

s = re.sub(r'\n?<style id="csd-karina-photo-polish">.*?</style>\s*', '\n', s, flags=re.S)
s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')
