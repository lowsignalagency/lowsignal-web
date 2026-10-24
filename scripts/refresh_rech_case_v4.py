from pathlib import Path
import re

p = Path('casos/rech.html')
s = p.read_text(encoding='utf-8')

# Remove the top back link entirely.
s = re.sub(r'\s*<a class="rechx-back"[^>]*>← Customer Stories</a>\s*', '\n      ', s, count=1)

# Match the horizontal rhythm used across the current site.
s = re.sub(
    r'\.rechx-wrap\{[^}]*\}',
    '.rechx-wrap{width:min(var(--content-container),calc(100% - 160px))!important;max-width:var(--content-container)!important;margin-inline:auto!important}',
    s,
    count=1
)

# Keep responsive margins aligned with the rest of the site.
s = s.replace(
    '@media(max-width:1000px){.rechx-wrap{width:calc(100% - 56px)}',
    '@media(max-width:1000px){.rechx-wrap{width:calc(100% - 48px)!important}'
)
s = s.replace(
    '@media(max-width:760px){.rechx-wrap{width:calc(100% - 40px)}',
    '@media(max-width:760px){.rechx-wrap{width:calc(100% - 40px)!important}'
)

p.write_text(s, encoding='utf-8')
