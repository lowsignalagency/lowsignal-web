from pathlib import Path

path = Path('equipo/felipe-quiroz.html')
html = path.read_text(encoding='utf-8')

old = '''<p class="fq-editorial-bio">Felipe cofundó lowsignal, donde lidera la estrategia de la compañía, crecimiento, desarrollo comercial y evolución de sus productos y sistemas internos. Antes fue Head of Partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, una startup GovTech y SaaS basada en Estados Unidos, con presencia en 7+ mercados de Latinoamérica, Estados Unidos y Europa. Luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, una compañía B2B SaaS de Workforce Management con 10.000+ clientes en 40+ países. Su experiencia conecta negocio, producto, tecnología y growth, con foco en construir y escalar compañías, productos y sistemas de crecimiento.</p>'''

new = '''<p class="fq-editorial-bio">Felipe cofundó lowsignal y lideró sus primeros meses de operación como COO, construyendo la operación y estrategia comercial de la compañía. Actualmente, como CEO, lidera la estrategia general, crecimiento, desarrollo comercial y evolución de sus productos y sistemas internos. Antes fue Head of Partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, una startup GovTech y SaaS basada en Estados Unidos, con presencia en 7+ mercados de Latinoamérica, Estados Unidos y Europa, y luego Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, una compañía B2B SaaS de Workforce Management con 10.000+ clientes en 40+ países. Su experiencia conecta negocio, producto, tecnología y growth, con foco en construir y escalar compañías, productos y sistemas de crecimiento.</p>'''

if old not in html:
    raise SystemExit('Target Felipe profile bio paragraph not found')

html = html.replace(old, new, 1)
path.write_text(html, encoding='utf-8')
print('Updated Felipe profile bio')
