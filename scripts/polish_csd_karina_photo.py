from pathlib import Path
import re

# Keep Karina Ravanal's testimonial avatar at its normal size,
# but shift the crop upward so her face sits more naturally inside the circle.
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

style = '''\n<style id="csd-karina-photo-polish">\n.rechx-person img{\n  width:56px!important;\n  height:56px!important;\n  object-fit:cover!important;\n  object-position:center 12%!important;\n}\n.case-new-testimonial .case-new-person img{\n  width:58px!important;\n  height:58px!important;\n  object-fit:cover!important;\n  object-position:center 12%!important;\n}\n</style>\n'''

s = re.sub(r'\n?<style id="csd-karina-photo-polish">.*?</style>\s*', '\n', s, flags=re.S)
s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')
