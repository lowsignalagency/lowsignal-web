from pathlib import Path

p = Path('equipo/damian-aldunate.html')
s = p.read_text(encoding='utf-8')

old = '''<p class="team-editorial-bio">Marca, contenido y growth para convertir atención en crecimiento sostenido. Lidera estrategia de marca, marketing y crecimiento en lowsignal, conectando posicionamiento, contenido, campañas y ejecución comercial. También ha trabajado como Embajador de Innovación Educativa en <a href="https://www.consiliumbots.com/" target="_blank" rel="noopener noreferrer">ConsiliumBots</a>, acercando tecnología y datos públicos a comunidades educativas y sociales.</p>'''
new = '''<p class="team-editorial-bio">Damián cofundó lowsignal, donde lidera estrategia de marca, marketing y growth, conectando posicionamiento, contenido, campañas y ejecución comercial. También ha trabajado como Embajador de Innovación Educativa en <a href="https://www.consiliumbots.com/" target="_blank" rel="noopener noreferrer">ConsiliumBots</a>, una ONG que usa tecnología para conectar datos del gobierno con la comunidad y ayudar a las personas a tomar decisiones mejor informadas.</p>'''

if old not in s:
    raise SystemExit('Current Damián bio not found')

p.write_text(s.replace(old, new, 1), encoding='utf-8')
print('updated Damián bio')
