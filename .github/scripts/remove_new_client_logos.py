from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Remove Ryuki / Vandalo / Se Remonta entries from both marquee tracks.
patterns = [
    r'\n\s*<div class="lsr-trust-logo">\s*<img src="https://lowsignal\.cl/assets/ryuki-white\.png" alt="[^"]*">\s*</div>',
    r'\n\s*<div class="lsr-trust-logo">\s*<img src="https://lowsignal\.cl/assets/vandalo-white\.png" alt="[^"]*">\s*</div>',
    r'\n\s*<div class="lsr-trust-logo">\s*<img src="https://lowsignal\.cl/assets/seremonta-white\.png" alt="[^"]*">\s*</div>',
]
for pat in patterns:
    s, n = re.subn(pat, '', s)
    print(f'Removed {n} matches for {pat}')

# Remove the specific CSS block added for those logos.
s, n = re.subn(r'\n?<style id="v68-new-client-logos">.*?</style>\n?', '\n', s, flags=re.S)
print(f'Removed v68 style blocks: {n}')

p.write_text(s, encoding='utf-8')
