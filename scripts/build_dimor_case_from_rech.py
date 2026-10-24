from pathlib import Path

# Rebuild Dimor from the current RECH editorial system.
src = Path('casos/rech.html').read_text(encoding='utf-8')
s = src

repls = {
    '<title>Red Educacional Camilo Henríquez | Customer Story | lowsignal</title>': '<title>Dimor | Customer Story | lowsignal</title>',
    'CUSTOMER STORY · EDUCACIÓN': 'CUSTOMER STORY · B2B',
    'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>': 'Trabajo que pasa en terreno.<br><strong>Una presencia digital que lo hace visible.</strong>',
    'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.': 'Ayudamos a Dimor a transformar su operación diaria en una presencia digital más clara, consistente y comercial, mostrando mejor su trabajo, sus vehículos y la experiencia detrás de cada servicio.',
    'Red Educacional Camilo Henríquez': 'Dimor',
    'Web · Social · Contenido': 'Social · Contenido · Estrategia',
    'Ordenar la presencia digital de la red y conectar sus comunidades bajo una experiencia común.': 'Mostrar la operación real de Dimor y convertirla en contenido capaz de generar confianza, visibilidad y nuevas oportunidades comerciales.',
    'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>': 'Una operación activa.<br>Una marca que debía <strong>mostrarla mejor.</strong>',
    'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.': 'Dimor ya tenía una operación concreta, clientes y trabajo en terreno. El desafío era llevar todo eso a una presencia digital que comunicara mejor lo que hacen y acercara nuevas oportunidades de negocio.',
    'Muchas voces, poca lectura de red.': 'Mucho trabajo real, poca visibilidad digital.',
    'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.': 'La operación ocurría todos los días, pero no siempre quedaba reflejada en los canales digitales. Había una oportunidad clara de convertir terreno, vehículos, personas y servicio en contenido reconocible.',
    'Un sistema común, sin borrar identidades.': 'Contenido construido desde la operación.',
    'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.': 'Ordenamos la línea visual, el lenguaje y la producción de contenido para mostrar la operación de Dimor de forma consistente y conectar ese trabajo con una narrativa comercial más clara.',
    'Una experiencia común sin volver idénticos a sus colegios.': 'La operación como materia prima de la marca.',
    'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.': 'El contenido parte de lo que Dimor ya hace bien: terreno, logística, servicio y ejecución. A partir de ahí construimos una presencia más reconocible y útil para vender.',
    'Una presencia más clara, reconocible y <strong>preparada para crecer.</strong>': 'Una presencia más consistente, comercial y <strong>conectada con el negocio.</strong>',
    'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.': 'El resultado fue una presencia digital que representa mejor la operación de Dimor, fortalece su marca y ayuda a abrir nuevas conversaciones y oportunidades comerciales.',
    'lowsignal se ha convertido en un aliado estratégico para nuestra red. Entendieron nuestra visión y se involucraron de verdad en el proyecto.': 'lowsignal ha sido un gran aliado comercial para Dimor. Nos ha ayudado a abrir nuevas oportunidades de negocio y a crecer exponencialmente. Su equipo es muy responsable y la experiencia ha sido muy grata.',
    'Nicolás Muñoz': 'Ignacio Díaz',
    'Director Ejecutivo, Red Educacional Camilo Henríquez': 'Gerente General, Dimor',
    'https://lowsignal.cl/assets/nicolas-munoz.jpg': 'https://lowsignal.cl/assets/dimor_ignacio.jpg',
    'https://lowsignal.cl/assets/rech-logo-full.png': 'https://lowsignal.cl/assets/dimor-logo.png',
    'https://lowsignal.cl/assets/rech-logo-full-white-trim.png': 'https://lowsignal.cl/assets/dimor-logo.png',
    'https://lowsignal.cl/assets/comunidad-rech.jpg': 'https://lowsignal.cl/assets/dimor-concesionario.png',
    'https://lowsignal.cl/assets/reunion-rech.jpg': 'https://lowsignal.cl/assets/dimor-ig.jpg',
    'https://lowsignal.cl/casos/salvador-dali': 'https://lowsignal.cl/casos/hub',
    'https://lowsignal.cl/assets/dali-patio-nueva.jpg': 'https://lowsignal.cl/assets/hub-bg.jpg',
    'Colegio Salvador Dalí': 'hUB',
    'EDUCACIÓN · CUSTOMER STORY': 'B2C · CUSTOMER STORY',
}

for old, new in repls.items():
    s = s.replace(old, new)

polish = '''\n<style id="dimor-editorial-polish">\n.case-editorial-client img{\n  max-width:170px!important;\n  max-height:64px!important;\n  width:auto!important;\n  height:auto!important;\n  object-fit:contain!important;\n  object-position:left center!important;\n  margin-left:0!important;\n  filter:none!important;\n}\n.case-editorial-media img{object-position:center center!important}\n.case-editorial-pair figure:first-child img{object-position:left center!important}\n.rechx-person img{object-position:center 20%!important}\n@media(max-width:760px){\n  .case-editorial-client img{max-width:120px!important;max-height:48px!important}\n}\n</style>\n'''
s = s.replace('</head>', polish + '</head>', 1)

Path('casos/dimor.html').write_text(s, encoding='utf-8')
