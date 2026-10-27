from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')
old='Felipe cofundó lowsignal, donde lidera operaciones, estrategia comercial, client delivery y el desarrollo de productos y sistemas internos de growth. Antes lideró partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, trabajando en iniciativas de tecnología y educación pública que alcanzaron a 20.000+ familias y 35.000+ estudiantes, y luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, desarrollando productos de workforce management para clientes enterprise en Latinoamérica. Su trabajo conecta negocio, producto, tecnología y ejecución.'
new='Felipe cofundó lowsignal, donde lidera operaciones, estrategia comercial, client delivery y el desarrollo de productos y sistemas internos de growth. Antes fue Head of Partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, una startup GovTech y SaaS basada en Estados Unidos, con presencia en 7+ mercados de Latinoamérica, Estados Unidos y Europa. Luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, una compañía B2B SaaS de Workforce Management con 10.000+ clientes en 40+ países. Su experiencia conecta negocio, producto, tecnología y growth.'
if old not in s:
    raise SystemExit('old bio not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('updated Felipe profile bio')
