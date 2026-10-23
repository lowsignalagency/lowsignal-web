from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = {
    'Reducimos fricción y conectamos las capacidades que hacen crecer una compañía.':
        'Marketing, producto y tecnología trabajando como un solo sistema.',

    '<h2>Visibilidad, admisión y experiencia digital.</h2>':
        '<h2>Marca, admisión y experiencia digital para instituciones que quieren ser elegidas.</h2>',

    '<h2>Contenido, performance y conversión para marcas que quieren crecer.</h2>':
        '<h2>Contenido, performance y conversión para marcas que quieren ser elegidas.</h2>',

    '<div><small>FOCUS</small><strong>SaaS + Tech</strong><span>servicios profesionales e industria.</span></div>':
        '<div><small>FOCUS</small><strong>4 segmentos</strong><span>SaaS, tecnología, servicios profesionales e industria.</span></div>',

    'En lowsignal estamos construyendo una Growth Company para compañías que necesitan algo más que campañas aisladas: sistemas capaces de conectar estrategia, tecnología y ejecución.':
        'En lowsignal construimos sistemas de growth que conectan estrategia, tecnología y ejecución para aprender, mejorar y crecer con el tiempo.',

    '<h2>Less noise. More growth.</h2>':
        '<h2>Sistemas sobre acciones aisladas.</h2>',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Missing expected text: {old}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
