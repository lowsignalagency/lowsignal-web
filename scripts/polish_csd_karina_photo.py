from pathlib import Path
import re

# Match the Karina Ravanal portrait framing used on the Education page,
# while keeping the original testimonial avatar sizes in the case study.
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

style = '''\n<style id="csd-karina-photo-polish">\n.rechx-person img{\n  width:56px!important;\n  height:56px!important;\n  object-fit:cover!important;\n  object-position:center 26%!important;\n}\n.case-new-testimonial .case-new-person img{\n  width:58px!important;\n  height:58px!important;\n  object-fit:cover!important;\n  object-position:center 26%!important;\n}\n</style>\n'''

s = re.sub(r'\n?<style id="csd-karina-photo-polish">.*?</style>\s*', '\n', s, flags=re.S)
s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')
