from pathlib import Path
import re

STYLE = '''\n<style id="case-hero-cleanup-v1">\n.rechx-hero-grid{grid-template-columns:1fr!important;gap:0!important}\n.rechx-logo-card,.rechx-meta{display:none!important}\n.rechx-hero-copy{max-width:1080px}\n</style>\n'''

for file_path in ['casos/rech.html','casos/salvador-dali.html']:
    p = Path(file_path)
    s = p.read_text(encoding='utf-8')
    s = re.sub(r'\n?<style id="case-hero-cleanup-v1">.*?</style>\s*', '\n', s, flags=re.S)
    s = s.replace('</head>', STYLE + '</head>', 1)
    p.write_text(s, encoding='utf-8')
