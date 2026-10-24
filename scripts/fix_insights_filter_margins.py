from pathlib import Path
import re

path = Path('recursos/insights.html')
s = path.read_text(encoding='utf-8')

# Keep the filter bar on the same editorial width as the featured content.
# Works whether the generated CSS is formatted or minified.
s = re.sub(
    r'width:min\((?:var\(--insights-content,1480px\)|1480px),calc\(100% - 160px\)\)!important;\s*max-width:(?:var\(--insights-content,1480px\)|1480px)!important;',
    'width:min(1360px,calc(100% - 160px))!important;max-width:1360px!important;',
    s
)

path.write_text(s, encoding='utf-8')
