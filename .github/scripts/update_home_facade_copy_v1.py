from pathlib import Path

# Home facade copy refresh v3 — shorten Education and B2C headlines
path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = {
    '<h2>Marca, admisión y experiencia digital para instituciones que quieren crecer con más claridad.</h2>':
        '<h2>Marca, admisión y experiencia digital.</h2>',

    '<h2>Contenido, performance y conversión para marcas que quieren ganar atención y ventas.</h2>':
        '<h2>Contenido, performance y conversión.</h2>',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Missing expected text: {old}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
