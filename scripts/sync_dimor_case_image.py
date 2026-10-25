from pathlib import Path

OLD = 'https://lowsignal.cl/assets/dimor-truck.jpg'
NEW = 'https://lowsignal.cl/assets/dimor-concesionario.png'
OLD_REL = 'assets/dimor-truck.jpg'
NEW_REL = 'assets/dimor-concesionario.png'

changed = []
for pattern in ('*.html', '*.css', '*.js'):
    for path in Path('.').rglob(pattern):
        if '.git' in path.parts:
            continue
        try:
            s = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        out = s.replace(OLD, NEW).replace(OLD_REL, NEW_REL)
        if out != s:
            path.write_text(out, encoding='utf-8')
            changed.append(str(path))

print('Updated:', ', '.join(changed) if changed else 'no matching files')
