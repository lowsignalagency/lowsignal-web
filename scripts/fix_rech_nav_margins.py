from pathlib import Path
import re

p = Path('casos/rech.html')
s = p.read_text(encoding='utf-8')

# Remove the top back link if it still exists.
s = re.sub(r'\s*<a class="rechx-back"[^>]*>.*?</a>\s*', '\n', s, count=1, flags=re.S)

# Remove previous override block if present.
s = re.sub(r'\s*<style id="rech-nav-aligned-margins">.*?</style>\s*', '\n', s, flags=re.S)

override = '''
<style id="rech-nav-aligned-margins">
/* RECH content aligned 1:1 with the desktop/tablet/mobile navbar guides. */
.rechx .rechx-wrap{
  width:min(1220px,calc(100% - 128px)) !important;
  max-width:1220px !important;
  margin-inline:auto !important;
}
@media(max-width:1100px) and (min-width:761px){
  .rechx .rechx-wrap{
    width:calc(100% - 48px) !important;
    max-width:none !important;
  }
}
@media(max-width:760px){
  .rechx .rechx-wrap{
    width:calc(100% - 24px) !important;
    max-width:none !important;
  }
}
</style>
'''

s = s.replace('</head>', override + '\n</head>', 1)
p.write_text(s, encoding='utf-8')
