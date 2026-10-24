from pathlib import Path
import re

path = Path('casos/hub.html')
s = path.read_text(encoding='utf-8')

# Remove any inherited RECH quote block that may survive the hUB rebuild.
s = re.sub(r'<section[^>]*class="[^"]*rechx-quote[^"]*"[^>]*>.*?</section>\s*', '', s, flags=re.S | re.I)

# De-duplicate the hUB coming-soon band if a previous build inserted it twice.
blocks = list(re.finditer(r'<section[^>]*class="[^"]*hub-coming-soon[^"]*"[^>]*>.*?</section>\s*', s, flags=re.S | re.I))
if len(blocks) > 1:
    keep = blocks[0]
    first = s[keep.start():keep.end()]
    s = re.sub(r'<section[^>]*class="[^"]*hub-coming-soon[^"]*"[^>]*>.*?</section>\s*', '', s, flags=re.S | re.I)
    next_section = re.search(r'<section[^>]*class="[^"]*(?:rechx-next|case-new-next)[^"]*"', s, flags=re.I)
    if next_section:
        s = s[:next_section.start()] + first + '\n' + s[next_section.start():]
    else:
        s = s.replace('</main>', first + '\n</main>', 1)

path.write_text(s, encoding='utf-8')
