from pathlib import Path
import re

pages = {
    'soluciones/low-ads.html': 'ads-new-process',
    'soluciones/low-web.html': 'web-new-process',
    'soluciones/low-flow.html': 'flow-new-process',
    'soluciones/low-apps.html': 'apps-new-process',
    'soluciones/low-scale.html': 'scale-new-process',
}

for filename, section_class in pages.items():
    p = Path(filename)
    s = p.read_text()
    pattern = rf'\s*<section class="{re.escape(section_class)}"[^>]*>.*?</section>\s*'
    s, n = re.subn(pattern, '\n', s, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError(f'Expected one {section_class} section in {filename}, found {n}')
    p.write_text(s)
