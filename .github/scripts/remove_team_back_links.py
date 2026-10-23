from pathlib import Path
import re

files = [
    Path('equipo/felipe-quiroz.html'),
    Path('equipo/damian-aldunate.html'),
    Path('equipo/matias-bussinger.html'),
    Path('equipo/martin-alvarado.html'),
    Path('equipo/jorge-munoz.html'),
    Path('equipo/lia-morice.html'),
]

for p in files:
    s = p.read_text(encoding='utf-8')
    before = s
    s = re.sub(r'\s*<a class="fq-back" href="https://lowsignal\.cl/nosotros">← Volver al equipo</a>\s*', '\n', s, count=1)
    s = re.sub(r'\s*<a class="tp-back" href="https://lowsignal\.cl/nosotros">← Volver al equipo</a>\s*', '\n', s, count=1)
    s = re.sub(r'\s*<a class="(?:fq-back|tp-back)" href="https://lowsignal\.cl/nosotros">← Equipo</a>\s*', '\n', s, count=1)
    if s != before:
        p.write_text(s, encoding='utf-8')
        print(f'Removed back link from {p}')
    else:
        print(f'No back link found in {p}')

print('remove-team-back-links-v2')
