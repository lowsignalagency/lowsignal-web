from pathlib import Path
import re

# Rebuild hUB from the current RECH editorial system.
src = Path('casos/rech.html').read_text(encoding='utf-8')
s = src

repls = {
    '<title>Red Educacional Camilo Henríquez | Customer Story | lowsignal</title>': '<title>hUB | Customer Story | lowsignal</title>',
    'CUSTOMER STORY · EDUCACIÓN': 'CUSTOMER STORY · B2C',
    'CUSTOMER STORY <span>·</span> EDUCACIÓN': 'CUSTOMER STORY <span>·</span> B2C',
    'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>': 'Una experiencia que ya funcionaba.<br><strong>Una presencia digital para hacerla crecer.</strong>',
    'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.': 'Ayudamos a hUB a ordenar su presencia digital, mostrar mejor la experiencia de sus espacios y conectar contenido y campañas con nuevas visitas y reservas.',
    'Red Educacional Camilo Henríquez': 'hUB',
    'Web · Social · Contenido': 'Social · Paid Media · Contenido',
    'Ordenar la presencia digital de la red y conectar sus comunidades bajo una experiencia común.': 'Mostrar mejor la experiencia de hUB y convertir la atención digital en visitas, reservas y crecimiento.',
    'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>': 'Una experiencia potente.<br>Una presencia digital que debía <strong>estar a la altura.</strong>',
    'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.': 'hUB ya tenía una propuesta atractiva en el mundo físico. El desafío era lograr que esa experiencia también se entendiera online y que el contenido ayudara a mover a nuevas audiencias desde el descubrimiento hacia la reserva.',
    'Muchas voces, poca lectura de red.': 'Una buena experiencia, poco traducida al canal digital.',
    'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.': 'Los espacios, la propuesta y la experiencia existían, pero faltaba una línea digital capaz de mostrarlos con consistencia y transformar atención en intención de visita.',
    'Un sistema común, sin borrar identidades.': 'Contenido y campañas trabajando juntos.',
    'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.': 'Ordenamos la línea visual y la producción de contenido, y la conectamos con campañas orientadas a llevar nuevas audiencias hacia hUB y sus reservas.',
    'Una experiencia común sin volver idénticos a sus colegios.': 'La experiencia empieza antes de llegar.',
    'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.': 'Instagram y paid media se convierten en el primer punto de contacto: muestran el ambiente, los espacios y las razones para visitar hUB antes de que una persona llegue físicamente.',
    'Una presencia más clara, reconocible y <strong>preparada para crecer.</strong>': 'Una presencia más atractiva, consistente y <strong>orientada a conversión.</strong>',
    'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.': 'El resultado fue una presencia digital más coherente con la experiencia de hUB, con contenido y campañas trabajando sobre un mismo objetivo: generar interés y acercarlo a la reserva.',
    'https://lowsignal.cl/assets/rech-logo-full.png': 'https://lowsignal.cl/assets/hub-logo-white-new-trim.png',
    'https://lowsignal.cl/assets/rech-logo-full-white-trim.png': 'https://lowsignal.cl/assets/hub-logo-white-new-trim.png',
    'https://lowsignal.cl/assets/comunidad-rech.jpg': 'https://lowsignal.cl/assets/hub-bg.jpg',
    'https://lowsignal.cl/assets/reunion-rech.jpg': 'https://lowsignal.cl/assets/hub-ig.jpg',
    'https://lowsignal.cl/casos/salvador-dali': 'https://lowsignal.cl/casos/dulce-reino',
    'https://lowsignal.cl/assets/dali-patio-nueva.jpg': 'https://lowsignal.cl/assets/dulce-reino-pasteleria.jpg',
    'Colegio Salvador Dalí': 'DulceReino',
    'EDUCACIÓN · CUSTOMER STORY': 'B2C · CUSTOMER STORY',
}

for old, new in repls.items():
    s = s.replace(old, new)

# hUB has no approved customer testimonial in the current case. Remove the inherited RECH testimonial block.
s = re.sub(r'<section class="rechx-testimonial".*?</section>\s*', '', s, flags=re.S)

polish = '''
<style id="hub-editorial-polish">
.case-editorial-client img{
  max-width:150px!important;
  max-height:58px!important;
  width:auto!important;
  height:auto!important;
  object-fit:contain!important;
  object-position:left center!important;
  filter:brightness(0) saturate(100%)!important;
  margin-left:0!important;
}
.case-editorial-media img{object-position:center 46%!important}
.case-editorial-pair figure:first-child img{object-position:center top!important}
.case-editorial-pair figure:nth-child(2) img{object-position:center 50%!important}
@media(max-width:760px){
  .case-editorial-client img{max-width:112px!important;max-height:44px!important}
  .case-editorial-media img{object-position:center 45%!important}
}
</style>
'''
s = s.replace('</head>', polish + '</head>', 1)

Path('casos/hub.html').write_text(s, encoding='utf-8')
