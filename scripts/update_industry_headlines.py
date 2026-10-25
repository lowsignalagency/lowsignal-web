from pathlib import Path

changes = {
    Path('industrias/b2b.html'): [
        (
            'Growth para empresas que necesitan <strong>abrir conversaciones.</strong>',
            'Growth para empresas que quieren <strong>convertir interés en oportunidades.</strong>'
        ),
    ],
    Path('industrias/marcas-b2c.html'): [
        (
            'Growth para marcas que quieren <strong>ser elegidas.</strong>',
            'Growth para marcas que quieren <strong>convertir atención en ventas.</strong>'
        ),
        (
            'La decisión empieza <strong>mucho antes.</strong>',
            'La compra empieza <strong>antes del checkout.</strong>'
        ),
    ],
}

for path, replacements in changes.items():
    s = path.read_text(encoding='utf-8')
    original = s
    for old, new in replacements:
        if old not in s:
            raise SystemExit(f'Missing expected text in {path}: {old}')
        s = s.replace(old, new, 1)
    if s != original:
        path.write_text(s, encoding='utf-8')
        print(f'Updated {path}')

# Education intentionally unchanged.
