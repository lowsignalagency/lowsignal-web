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

    # Remove all visible back-link variants, both absolute and relative URLs.
    s = re.sub(
        r'\s*<a class="(?:fq-back|tp-back)" href="(?:https://lowsignal\.cl)?/nosotros">← (?:Volver al equipo|Equipo)</a>\s*',
        '\n', s, count=1
    )

    # Keep the same visual breathing room the profile had when the back link was present.
    s = s.replace('.fq-profile{margin-top:-100px;padding:214px 0 82px;', '.fq-profile{margin-top:-100px;padding:290px 0 82px;')
    s = s.replace('.fq-profile{margin-top:-100px;padding:274px 0 82px;', '.fq-profile{margin-top:-100px;padding:290px 0 82px;')
    s = s.replace('.tp-profile{margin-top:-100px;padding:214px 0 86px;', '.tp-profile{margin-top:-100px;padding:290px 0 86px;')
    s = s.replace('.tp-profile{margin-top:-100px;padding:274px 0 86px;', '.tp-profile{margin-top:-100px;padding:290px 0 86px;')

    if s != before:
        p.write_text(s, encoding='utf-8')
        print(f'Updated {p}')
    else:
        print(f'No changes needed in {p}')

print('team-profile-spacing-v3')
