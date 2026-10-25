from pathlib import Path
import re

profiles = {
    'equipo/martin-alvarado.html': ('Martín', 'https://www.linkedin.com/in/martin-alvaradod'),
    'equipo/jorge-munoz.html': ('Jorge', 'https://www.linkedin.com/in/jorgemunozve'),
    'equipo/lia-morice.html': ('Lía', 'https://www.linkedin.com/in/l%C3%ADa-morice-b31521419'),
}

css = r'''
<style id="team-profile-linkedin-v1">
.tp-profile-links{display:flex;flex-wrap:wrap;gap:10px 24px;margin-top:32px;padding-top:24px;border-top:1px solid rgba(138,164,255,.14)}
.tp-profile-links a{color:#C2CBE0;font-size:11px;font-weight:600;transition:color .18s ease,transform .18s ease}
.tp-profile-links a:hover{color:#fff;transform:translateY(-1px)}
@media(max-width:760px){.tp-profile-links{margin-top:24px;padding-top:20px;gap:10px 18px}}
</style>
'''

for file_path, (name, url) in profiles.items():
    path = Path(file_path)
    s = path.read_text(encoding='utf-8')

    s = re.sub(r'\n?<style id="team-profile-linkedin-v1">.*?</style>\s*', '\n', s, flags=re.S)
    s = re.sub(r'\n\s*<div class="tp-profile-links" aria-label="Enlaces de [^"]+">.*?</div>', '', s, count=1, flags=re.S)

    link_block = f'''\n        <div class="tp-profile-links" aria-label="Enlaces de {name}">\n          <a href="{url}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>\n        </div>'''

    s, count = re.subn(r'(<p class="tp-summary">.*?</p>)', r'\1' + link_block, s, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'Could not insert LinkedIn block in {file_path}')

    s = s.replace('</head>', css + '\n</head>', 1)
    path.write_text(s, encoding='utf-8')
