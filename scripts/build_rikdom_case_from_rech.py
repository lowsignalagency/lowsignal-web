from pathlib import Path

# Rebuild Rikdom from the current RECH editorial system.
src = Path('casos/rech.html').read_text(encoding='utf-8')
s = src

repls = {
    '<title>Red Educacional Camilo Henríquez | Customer Story | lowsignal</title>': '<title>Rikdom | Customer Story | lowsignal</title>',
    'CUSTOMER STORY · EDUCACIÓN': 'CUSTOMER STORY · B2B',
    'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>': 'Del terreno a lo digital.<br><strong>Una web que muestra mejor lo que hacen.</strong>',
    'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.': 'Ayudamos a Rikdom a transformar su experiencia en terreno en una presencia digital clara, moderna y preparada para presentar mejor sus soluciones, productos y proyectos.',
    'Red Educacional Camilo Henríquez': 'Rikdom',
    'Web · Social · Contenido': 'Web · Estrategia · Contenido',
    'Ordenar la presencia digital de la red y conectar sus comunidades bajo una experiencia común.': 'Ordenar la propuesta de Rikdom y llevarla a una experiencia web clara para clientes, proyectos y nuevas oportunidades.',
    'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>': 'Mucho valor en terreno.<br>Una web que debía <strong>hacerlo evidente.</strong>',
    'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.': 'Rikdom no necesitaba solo una web nueva. Necesitaba una experiencia capaz de ordenar su oferta, mostrar mejor sus productos y proyectos, y hacer más fácil entender cómo puede aportar en cada obra.',
    'Muchas voces, poca lectura de red.': 'Una oferta amplia, difícil de recorrer.',
    'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.': 'Servicios, especialidades y productos convivían sin una experiencia digital que ayudara a recorrerlos con claridad y conectarlos con las necesidades de cada cliente.',
    'Un sistema común, sin borrar identidades.': 'Una experiencia simple para una propuesta compleja.',
    'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.': 'Rediseñamos la arquitectura, el lenguaje visual y la presentación de productos y servicios para que la propuesta de Rikdom fuera más clara, navegable y comercialmente útil.',
    'Una experiencia común sin volver idénticos a sus colegios.': 'Del trabajo en terreno a una web que lo cuenta mejor.',
    'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.': 'La nueva experiencia reúne la información clave de Rikdom, presenta mejor sus soluciones y acerca sus productos a quienes buscan respuestas concretas para sus proyectos.',
    'Una presencia más clara, reconocible y <strong>preparada para crecer.</strong>': 'Una experiencia más clara, moderna y <strong>preparada para convertir.</strong>',
    'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.': 'El resultado fue una web que traduce mejor la experiencia de Rikdom, ordena su propuesta y permite a sus clientes entender más rápido qué hace, qué ofrece y cómo avanzar.',
    'lowsignal se ha convertido en un aliado estratégico para nuestra red. Entendieron nuestra visión y se involucraron de verdad en el proyecto.': 'lowsignal entendió lo que queríamos mostrar con Rikdom y lo llevó a una web clara, moderna y fácil de navegar. Hoy nuestros productos se ven mucho mejor y es más fácil para los clientes conocerlos.',
    'Nicolás Muñoz': 'Rodrigo Cuevas',
    'Director Ejecutivo, Red Educacional Camilo Henríquez': 'Socio fundador, Rikdom',
    'https://lowsignal.cl/assets/nicolas-munoz.jpg': 'https://lowsignal.cl/assets/rodrigo.jpg',
    'https://lowsignal.cl/assets/rech-logo-full.png': 'https://lowsignal.cl/assets/rikdom.png',
    'https://lowsignal.cl/assets/rech-logo-full-white-trim.png': 'https://lowsignal.cl/assets/rikdom.png',
    'https://lowsignal.cl/assets/comunidad-rech.jpg': 'https://lowsignal.cl/assets/galpon-merk.jpg',
    'https://lowsignal.cl/assets/reunion-rech.jpg': 'https://lowsignal.cl/assets/rikdom_web.jpg',
    'https://lowsignal.cl/casos/salvador-dali': 'https://lowsignal.cl/casos/dimor',
    'https://lowsignal.cl/assets/dali-patio-nueva.jpg': 'https://lowsignal.cl/assets/dimor-truck.jpg',
    'Colegio Salvador Dalí': 'Dimor',
    'EDUCACIÓN · CUSTOMER STORY': 'B2B · CUSTOMER STORY',
}

for old, new in repls.items():
    s = s.replace(old, new)

polish = '''\n<style id="rikdom-editorial-polish">\n.case-editorial-client img{max-height:58px;width:auto;object-fit:contain;object-position:left center;opacity:1}\n.case-editorial-pair{grid-template-columns:1fr!important;gap:0!important}\n.case-editorial-pair figure:first-child{display:block!important;width:100%;height:clamp(420px,46vw,620px)!important;overflow:hidden!important;background:#F4F4F2!important}\n.case-editorial-pair figure:first-child img{display:block;width:100%!important;height:100%!important;object-fit:cover!important;object-position:center 50%!important;transform:scale(1.01);transform-origin:center center}\n.case-editorial-pair figure:nth-child(2){display:none!important}\n.rechx-person img{object-position:center 18%!important}\n@media(max-width:1000px){\n  .case-editorial-pair figure:first-child{height:440px!important}\n  .case-editorial-pair figure:first-child img{object-position:center 50%!important}\n}\n@media(max-width:760px){\n  .case-editorial-pair figure:first-child{height:320px!important}\n  .case-editorial-pair figure:first-child img{object-position:center 50%!important;transform:none}\n}\n</style>\n'''
s = s.replace('</head>', polish + '</head>', 1)

Path('casos/rikdom.html').write_text(s, encoding='utf-8')
