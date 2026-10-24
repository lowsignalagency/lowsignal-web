from pathlib import Path
import re

# Rebuild DulceReino from the RECH editorial system.
src = Path('casos/rech.html').read_text(encoding='utf-8')
s = src

repls = {
    '<title>Red Educacional Camilo Henríquez | Customer Story | lowsignal</title>': '<title>DulceReino | Customer Story | lowsignal</title>',
    'CUSTOMER STORY · EDUCACIÓN': 'CUSTOMER STORY · B2C',
    'CUSTOMER STORY <span>·</span> EDUCACIÓN': 'CUSTOMER STORY <span>·</span> B2C',
    'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>': 'Una marca para antojar.<br><strong>Una presencia para hacerla crecer.</strong>',
    'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.': 'Ayudamos a DulceReino a ordenar su presencia digital, mostrar mejor sus productos y conectar contenido y campañas con nuevas visitas al local.',
    'Red Educacional Camilo Henríquez': 'DulceReino',
    'Web · Social · Contenido': 'Social · Paid Media · Contenido',
    'Ordenar la presencia digital de la red y conectar sus comunidades bajo una experiencia común.': 'Convertir la experiencia de DulceReino en una presencia digital capaz de despertar deseo y atraer nuevas visitas.',
    'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>': 'De mostrar productos<br>a construir una marca <strong>que se antoja.</strong>',
    'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.': 'DulceReino ya tenía productos y una experiencia atractiva en el local. El desafío era traducir eso a digital con una presencia consistente, reconocible y capaz de mover a nuevas personas desde el contenido hacia una visita real.',
    'Muchas voces, poca lectura de red.': 'Buen producto, una presencia que podía contar mucho más.',
    'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.': 'El producto tenía fuerza visual, pero faltaba una línea de contenido capaz de mostrarlo con consistencia y conectar esa atención con el negocio.',
    'Un sistema común, sin borrar identidades.': 'Una línea visual reconocible para producto, local y experiencia.',
    'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.': 'Ordenamos la producción de fotos y reels, el lenguaje visual y las campañas para que cada pieza mostrara mejor la experiencia de DulceReino y trabajara sobre un mismo objetivo comercial.',
    'Una experiencia común sin volver idénticos a sus colegios.': 'Contenido que abre el apetito antes de llegar.',
    'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.': 'Producto, ambiente y campañas se conectan en una misma experiencia digital para transformar atención en intención de visita.',
    'Una presencia más clara, reconocible y <strong>preparada para crecer.</strong>': 'Una marca más consistente, deseable y <strong>preparada para atraer.</strong>',
    'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.': 'El resultado fue una presencia digital más coherente con la experiencia real de DulceReino, con contenido y campañas trabajando juntos para generar deseo, reconocimiento y nuevas visitas.',
    'https://lowsignal.cl/assets/rech-logo-full.png': 'https://lowsignal.cl/assets/dulcereino-logo-trim.png',
    'https://lowsignal.cl/assets/rech-logo-full-white-trim.png': 'https://lowsignal.cl/assets/dulcereino-logo-trim.png',
    'https://lowsignal.cl/assets/comunidad-rech.jpg': 'https://lowsignal.cl/assets/dulce-reino-pasteleria.jpg',
    'https://lowsignal.cl/assets/reunion-rech.jpg': 'https://lowsignal.cl/assets/dulce-mesa.jpg',
    'No hicimos una página.<br><strong>Construimos una forma de presentar la red.</strong>': 'No hicimos solo contenido.<br><strong>Construimos una vitrina digital que invita a entrar.</strong>',
    'EDUCACIÓN · CUSTOMER STORY': 'B2C · CUSTOMER STORY',
}

for old, new in repls.items():
    s = s.replace(old, new)

# Replace inherited RECH testimonial with DulceReino's approved testimonial.
dulce_quote = '''
<section class="rechx-quote">
  <div class="container rechx-wrap rechx-quote-inner">
    <div class="rechx-quote-mark">“</div>
    <blockquote>En lowsignal encontré versatilidad, compromiso y un equipo que se involucra de verdad. Entienden el negocio, no solo ejecutan.</blockquote>
    <div class="rechx-person"><img src="https://lowsignal.cl/assets/david-suazo.jpg" alt="David Suazo"><div><b>David Suazo</b><span>Founder, DulceReino</span></div></div>
  </div>
</section>
'''
s = re.sub(r'<section[^>]*class="[^"]*rechx-quote[^"]*"[^>]*>.*?</section>\s*', dulce_quote + '\n', s, count=1, flags=re.S | re.I)

# Keep RECH as the next case.
s = s.replace('https://lowsignal.cl/casos/salvador-dali', 'https://lowsignal.cl/casos/rech')
s = s.replace('https://lowsignal.cl/assets/dali-patio-nueva.jpg', 'https://lowsignal.cl/assets/comunidad-rech.jpg')
s = s.replace('Colegio Salvador Dalí', 'Red Educacional Camilo Henríquez')

polish = '''
<style id="dulce-editorial-polish">
.case-editorial-client img{
  max-width:150px!important;
  max-height:62px!important;
  width:auto!important;
  height:auto!important;
  object-fit:contain!important;
  object-position:left center!important;
  margin-left:0!important;
}
.case-editorial-media img{object-position:center 52%!important}
.case-editorial-pair figure:first-child img{object-position:center 46%!important}
.case-editorial-pair figure:nth-child(2) img{object-position:center 50%!important}
.rechx-person img{object-position:center 18%!important}
@media(max-width:760px){
  .case-editorial-client img{max-width:116px!important;max-height:48px!important}
  .case-editorial-media img{object-position:center 48%!important}
}
</style>
'''
s = s.replace('</head>', polish + '</head>', 1)

Path('casos/dulce-reino.html').write_text(s, encoding='utf-8')
