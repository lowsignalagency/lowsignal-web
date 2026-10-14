from pathlib import Path
import re

labels = ("Planes para instituciones", "Planes para empresas", "Planes para marcas")
changed = []
remaining = []

for path in sorted(Path('.').rglob('*.html')):
    if any(part.startswith('.') for part in path.parts[:-1]):
        continue
    text = path.read_text(encoding='utf-8')
    original = text

    # Remove any standalone nav anchor whose visible label is one of the old industry plan links.
    pattern = re.compile(
        r'<a\b[^>]*>\s*(?:<b>|<strong>)?\s*(?:Planes para instituciones|Planes para empresas|Planes para marcas)\s*(?:</b>|</strong>)?.*?</a>',
        re.IGNORECASE | re.DOTALL,
    )
    text = pattern.sub('', text)

    if text != original:
        path.write_text(text, encoding='utf-8')
        changed.append(str(path))

for path in sorted(Path('.').rglob('*.html')):
    if any(part.startswith('.') for part in path.parts[:-1]):
        continue
    text = path.read_text(encoding='utf-8')
    if any(label in text for label in labels):
        remaining.append(str(path))

print(f'Updated {len(changed)} HTML files')
for p in changed:
    print(p)
print('Remaining old industry plan links:', remaining)
if remaining:
    raise SystemExit(2)
