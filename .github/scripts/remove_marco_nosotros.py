from pathlib import Path
import re

p = Path('nosotros.html')
s = p.read_text(encoding='utf-8')

# Remove Marco team card.
s = re.sub(
    r'\s*<article class="person">\s*<div class="person-photo"><img src="https://lowsignal\.cl/assets/team_marco-1\.png" alt="Marco Kroeger"></div>\s*<div class="person-meta"><div class="person-name">Marco Kroeger</div><div class="person-role">Business Development Representative</div>\s*<a class="profile-link" href="https://lowsignal\.cl/equipo/marco-kroeger"><span class="circle">→</span> Ver perfil</a></div>\s*</article>',
    '',
    s,
    count=1,
    flags=re.S
)

# Remove legacy JS profile data for Marco, if present.
s = re.sub(
    r'\s*marco:\{name:\'Marco Kroeger\'.*?\},\n',
    '\n',
    s,
    count=1
)

p.write_text(s, encoding='utf-8')
print('Removed Marco Kroeger from nosotros.html')
