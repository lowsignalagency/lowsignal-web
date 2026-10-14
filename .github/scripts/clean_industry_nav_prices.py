from pathlib import Path

replacements = {
    ' · Planes desde 5 UF + IVA / mes.': '.',
    ' · Planes desde 6 UF + IVA / mes.': '.',
    ' · Planes desde 8 UF + IVA / mes.': '.',
    ' · Planes desde 10 UF + IVA / mes.': '.',
    ' · Planes desde 11 UF + IVA / mes.': '.',
    ' · Planes desde 12 UF + IVA / mes.': '.',
    ' · Planes desde 14 UF + IVA / mes.': '.',
    ' · Planes desde 5 UF': '',
    ' · Planes desde 6 UF': '',
    ' · Planes desde 8 UF': '',
    ' · Planes desde 10 UF': '',
    ' · Planes desde 11 UF': '',
    ' · Planes desde 12 UF': '',
    ' · Planes desde 14 UF': '',
}

changed=[]
for path in sorted(Path('.').rglob('*.html')):
    if any(part.startswith('.') for part in path.parts[:-1]):
        continue
    text = path.read_text(encoding='utf-8')
    original = text
    for old,new in replacements.items():
        text = text.replace(old,new)
    if text != original:
        path.write_text(text,encoding='utf-8')
        changed.append(str(path))

print(f'Updated {len(changed)} HTML files')
for p in changed: print(p)

remaining=[]
for path in sorted(Path('.').rglob('*.html')):
    if any(part.startswith('.') for part in path.parts[:-1]):
        continue
    text=path.read_text(encoding='utf-8')
    if 'Planes desde ' in text:
        remaining.append(str(path))
print('Remaining Planes desde:', remaining)
if remaining:
    raise SystemExit(2)
