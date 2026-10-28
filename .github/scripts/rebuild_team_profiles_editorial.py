from pathlib import Path

UPDATES = {
    'equipo/damian-aldunate.html': (
        'Marca, contenido y growth para convertir atención en crecimiento sostenido. Lidera estrategia de marca, marketing y crecimiento en lowsignal, conectando posicionamiento, contenido, campañas y ejecución comercial.',
        'Marca, contenido y growth para convertir atención en crecimiento sostenido. Lidera estrategia de marca, marketing y crecimiento en lowsignal, conectando posicionamiento, contenido, campañas y ejecución comercial. También ha trabajado como Embajador de Innovación Educativa en <a href="https://www.consiliumbots.com/" target="_blank" rel="noopener noreferrer">ConsiliumBots</a>, acercando tecnología y datos públicos a comunidades educativas y sociales.'
    ),
    'equipo/matias-bussinger.html': (
        'IA, automatización y revenue para convertir procesos complejos en sistemas que generan crecimiento. Construye agentes, automatizaciones e integraciones que conectan datos, procesos comerciales y tecnología para acelerar adquisición, conversión y eficiencia.',
        'IA, automatización y revenue para convertir procesos complejos en sistemas que generan crecimiento. Construye agentes, automatizaciones e integraciones que conectan datos, procesos comerciales y tecnología para acelerar adquisición, conversión y eficiencia. También ha trabajado como Embajador de Innovación Educativa en <a href="https://www.consiliumbots.com/" target="_blank" rel="noopener noreferrer">ConsiliumBots</a>, conectando tecnología y datos públicos con comunidades educativas y sociales.'
    ),
}

for filename, (old_bio, new_bio) in UPDATES.items():
    path = Path(filename)
    s = path.read_text(encoding='utf-8')

    if old_bio not in s and new_bio not in s:
        raise SystemExit(f'Editorial bio not found in {filename}')
    if old_bio in s:
        s = s.replace(old_bio, new_bio, 1)

    marker = 'consiliumbots-logo.svg'
    idx = s.find(marker)
    if idx != -1:
        start = s.rfind('<section', 0, idx)
        end = s.find('</section>', idx)
        if start == -1 or end == -1:
            raise SystemExit(f'Could not locate old Consilium section in {filename}')
        end += len('</section>')
        s = s[:start] + s[end:]

    path.write_text(s, encoding='utf-8')
    print('updated', filename)
