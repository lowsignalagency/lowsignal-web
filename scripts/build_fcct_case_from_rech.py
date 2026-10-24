from pathlib import Path

# Build FCCT from the current RECH editorial customer-story system.
src = Path('casos/rech.html').read_text(encoding='utf-8')
s = src

repls = {
    '<title>Red Educacional Camilo Henríquez | Customer Story | lowsignal</title>': '<title>Fundación Educacional Crecer con Todos | Customer Story | lowsignal</title>',
    'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>': 'Una misión que transforma.<br><strong>Una experiencia digital que la hace visible.</strong>',
    'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.': 'Ayudamos a Fundación Educacional Crecer con Todos a transformar su impacto en una experiencia digital clara, cercana y preparada para conectar con comunidades, aliados y nuevas oportunidades.',
    'Red Educacional Camilo Henríquez': 'Fundación Educacional Crecer con Todos',
    'Web · Social · Contenido': 'Web · Estrategia · Contenido',
    'Ordenar la presencia digital de la red y conectar sus comunidades bajo una experiencia común.': 'Ordenar la historia de la fundación y hacer visible su impacto a través de una experiencia digital clara y cercana.',
    'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>': 'Mucho impacto por contar.<br>Una presencia que debía <strong>hacerlo visible.</strong>',
    'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.': 'La fundación no necesitaba simplemente una web nueva. Necesitaba una forma más clara de contar su misión, ordenar sus programas y hacer visible el impacto que genera junto a niños, niñas, familias y comunidades.',
    'Muchas voces, poca lectura de red.': 'Mucho impacto, difícil de recorrer.',
    'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.': 'La historia, los programas y los resultados de la fundación existían, pero la experiencia digital no permitía entenderlos con la misma claridad con la que se viven en terreno.',
    'Un sistema común, sin borrar identidades.': 'Una experiencia que ordena la historia.',
    'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.': 'Rediseñamos la arquitectura, el lenguaje visual y la forma de presentar los programas para que cada persona pudiera entender qué hace la fundación, por qué importa y cómo conectarse con ella.',
    'Una experiencia común sin volver idénticos a sus colegios.': 'Una web que convierte impacto en una historia fácil de entender.',
    'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.': 'La nueva experiencia digital organiza programas, misión e impacto en un recorrido más claro, humano y preparado para crecer junto a la fundación.',
    'Una presencia más clara, reconocible y <strong>preparada para crecer.</strong>': 'Una misión más visible, accesible y <strong>preparada para crecer.</strong>',
    'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.': 'El resultado no fue solo una nueva web. Fue una forma más clara de presentar la fundación, mostrar lo que ya ha construido y acercar su impacto a personas, comunidades y futuros aliados.',
    'lowsignal se ha convertido en un aliado estratégico para nuestra red. Entendieron nuestra visión y se involucraron de verdad en el proyecto.': 'lowsignal entendió nuestra misión desde el inicio, ayudándonos a contar nuestra historia y mostrar el impacto que generamos. Todo el proceso fue cercano y profesional.',
    'Nicolás Muñoz': 'Valentina Wagenreld',
    'Director Ejecutivo, Fundación Educacional Crecer con Todos': 'Directora Ejecutiva, Fundación Educacional Crecer con Todos',
    'https://lowsignal.cl/assets/nicolas-munoz.jpg': 'https://lowsignal.cl/assets/valentina-w.jpg',
    'https://lowsignal.cl/assets/rech-logo-full.png': 'https://lowsignal.cl/assets/crecer-primerolee-trim.png',
    'https://lowsignal.cl/assets/rech-logo-full-white-trim.png': 'https://lowsignal.cl/assets/crecer-primerolee-white.png',
    'https://lowsignal.cl/assets/comunidad-rech.jpg': 'https://lowsignal.cl/assets/crecer-ninos.png',
    'https://lowsignal.cl/assets/reunion-rech.jpg': 'https://lowsignal.cl/assets/web-fcct.png',
    'https://lowsignal.cl/casos/salvador-dali': 'https://lowsignal.cl/casos/san-jorge',
    'https://lowsignal.cl/assets/dali-patio-nueva.jpg': 'https://lowsignal.cl/assets/case-san-jorge.webp',
    'Colegio Salvador Dalí': 'Colegio San Jorge de Las Condes',
}

for old, new in repls.items():
    s = s.replace(old, new)

# Use the same background photo featured in the FCCT testimonial on the Education page
# for the first large FCCT image.
s = s.replace('https://lowsignal.cl/assets/crecer-ninos.png', 'https://lowsignal.cl/assets/impacto-principal.jpg', 1)

# Foundation-specific polish.
# The website screenshot becomes the only visual in the pair. The image is enlarged
# slightly and shifted up/left so the browser chrome disappears and the purple hero
# gets enough breathing room on its left edge.
polish = '''\n<style id="fcct-editorial-polish">\n.case-editorial-client img{max-height:68px;width:auto;object-fit:contain;object-position:left center}\n.case-editorial-pair{grid-template-columns:1fr!important;gap:0!important;align-items:stretch}\n.case-editorial-pair figure:first-child{display:block!important;width:100%;height:clamp(420px,46vw,620px)!important;background:#7545D8!important;overflow:hidden!important}\n.case-editorial-pair figure:first-child img{display:block;width:100%!important;height:100%!important;object-fit:cover!important;object-position:42% 58%!important;transform:scale(1.08) translate(-2.5%,-6.5%)!important;transform-origin:center center!important}\n.case-editorial-pair figure:nth-child(2){display:none!important}\n@media(max-width:1000px){\n  .case-editorial-pair figure:first-child{height:440px!important}\n  .case-editorial-pair figure:first-child img{height:100%!important;object-position:42% 58%!important;transform:scale(1.08) translate(-2.5%,-6%)!important}\n}\n@media(max-width:760px){\n  .case-editorial-pair figure:first-child{height:320px!important}\n  .case-editorial-pair figure:first-child img{height:100%!important;object-position:40% 58%!important;transform:scale(1.1) translate(-2%,-5%)!important}\n}\n</style>\n'''
s = s.replace('</head>', polish + '</head>', 1)

Path('casos/fcct.html').write_text(s, encoding='utf-8')
