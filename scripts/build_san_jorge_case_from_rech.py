from pathlib import Path

# Rebuild San Jorge from the current RECH editorial system.
src = Path('casos/rech.html').read_text(encoding='utf-8')
s = src

repls = {
    '<title>Red Educacional Camilo Henríquez | Customer Story | lowsignal</title>': '<title>Colegio San Jorge de Las Condes | Customer Story | lowsignal</title>',
    'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>': 'Lo que pasa dentro importa.<br><strong>Una presencia digital para mostrarlo mejor.</strong>',
    'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.': 'Ayudamos al Colegio San Jorge de Las Condes a ordenar su presencia digital, fortalecer sus redes y renovar su web para mostrar mejor lo que ocurre dentro del colegio y conectar con nuevas familias.',
    'Red Educacional Camilo Henríquez': 'Colegio San Jorge de Las Condes',
    'Web · Social · Contenido': 'Web · Social · Contenido',
    'Ordenar la presencia digital de la red y conectar sus comunidades bajo una experiencia común.': 'Ordenar la presencia digital del colegio y comunicar con más claridad su proyecto, su comunidad y su vida cotidiana.',
    'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>': 'Mucho por mostrar.<br>Una presencia que debía <strong>contarlo mejor.</strong>',
    'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.': 'El colegio no necesitaba simplemente publicar más. Necesitaba ordenar su web y sus redes para que familias y comunidad entendieran mejor su propuesta, su vida diaria y todo lo que ocurre dentro y fuera de la sala.',
    'Muchas voces, poca lectura de red.': 'Mucho contenido, poca lectura común.',
    'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.': 'La información del colegio, sus actividades y su comunidad estaban repartidas entre distintos puntos de contacto sin una experiencia digital suficientemente clara y consistente.',
    'Un sistema común, sin borrar identidades.': 'Una experiencia más clara entre web y redes.',
    'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.': 'Ordenamos la arquitectura del sitio, renovamos la experiencia web y conectamos la comunicación en redes para que ambos canales contaran una historia más coherente del colegio.',
    'Una experiencia común sin volver idénticos a sus colegios.': 'Dos canales trabajando para contar mejor una misma comunidad.',
    'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.': 'La nueva experiencia organiza la información, hace más visible la vida del colegio y permite que web y redes acompañen mejor a familias actuales y futuras.',
    'Una presencia más clara, reconocible y <strong>preparada para crecer.</strong>': 'Una presencia más clara, cercana y <strong>fácil de recorrer.</strong>',
    'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.': 'El resultado fue una presencia digital más ordenada y coherente: una web que organiza la información y unas redes que muestran la vida del colegio con mayor cercanía.',
    'lowsignal se ha convertido en un aliado estratégico para nuestra red. Entendieron nuestra visión y se involucraron de verdad en el proyecto.': 'lowsignal ha sido un aporte muy importante para nosotros. Nos ayudó a ordenar nuestras redes y nuestra web, llegar mejor a nuestro público y contar lo que hacemos. Es un equipo muy responsable.',
    'Nicolás Muñoz': 'Jorge Menay',
    'Director Ejecutivo, Red Educacional Camilo Henríquez': 'Director, Colegio San Jorge de Las Condes',
    'https://lowsignal.cl/assets/nicolas-munoz.jpg': 'https://lowsignal.cl/assets/csjo_jorge.jpg',
    'https://lowsignal.cl/assets/rech-logo-full.png': 'https://lowsignal.cl/assets/csjo-white-trim.png',
    'https://lowsignal.cl/assets/rech-logo-full-white-trim.png': 'https://lowsignal.cl/assets/csjo-white-trim.png',
    'https://lowsignal.cl/assets/comunidad-rech.jpg': 'https://lowsignal.cl/assets/sanjorge-ninos.png',
    'https://lowsignal.cl/assets/reunion-rech.jpg': 'https://lowsignal.cl/assets/csjo-web.jpg',
    'https://lowsignal.cl/casos/salvador-dali': 'https://lowsignal.cl/casos/rikdom',
    'https://lowsignal.cl/assets/dali-patio-nueva.jpg': 'https://lowsignal.cl/assets/galpon-merk.jpg',
    'Colegio Salvador Dalí': 'Rikdom',
}

for old, new in repls.items():
    s = s.replace(old, new)

# Crop Jorge tighter inside the existing avatar size (do not enlarge the circle itself).
s = s.replace(
    '<div class="rechx-person"><img src="https://lowsignal.cl/assets/csjo_jorge.jpg" alt="Jorge Menay"><div>',
    '<div class="rechx-person"><span class="sanjorge-person-crop"><img src="https://lowsignal.cl/assets/csjo_jorge.jpg" alt="Jorge Menay"></span><div>',
    1,
)

polish = '''\n<style id="sanjorge-editorial-polish">\n/* Make the white San Jorge mark readable on the light sticky panel. */\n.case-editorial-client img{\n  max-height:62px;\n  width:auto;\n  object-fit:contain;\n  object-position:left center;\n  filter:brightness(0) saturate(100%) invert(11%) sepia(17%) saturate(1754%) hue-rotate(183deg) brightness(91%) contrast(93%);\n  opacity:1;\n}\n\n/* One large website visual, anchored to the left so the hero copy stays visible. */\n.case-editorial-pair{\n  grid-template-columns:1fr!important;\n  gap:0!important;\n}\n.case-editorial-pair figure:first-child{\n  display:block!important;\n  width:100%;\n  height:clamp(420px,46vw,620px)!important;\n  overflow:hidden!important;\n  background:#0B4A86!important;\n}\n.case-editorial-pair figure:first-child img{\n  display:block;\n  width:100%!important;\n  height:100%!important;\n  object-fit:cover!important;\n  object-position:left 44%!important;\n  transform:scale(1.005);\n  transform-origin:left center;\n}\n.case-editorial-pair figure:nth-child(2){display:none!important}\n\n/* Same avatar size; tighter crop so Jorge reads as a portrait, not a full-body shot. */\n.rechx-person .sanjorge-person-crop{\n  width:56px;\n  height:56px;\n  flex:0 0 56px;\n  border-radius:50%;\n  overflow:hidden;\n  display:block;\n  border:1px solid rgba(255,255,255,.32);\n}\n.rechx-person .sanjorge-person-crop img{\n  width:100%!important;\n  height:100%!important;\n  max-width:none!important;\n  border:0!important;\n  border-radius:0!important;\n  object-fit:cover!important;\n  object-position:center 18%!important;\n  transform:scale(1.65)!important;\n  transform-origin:center 20%!important;\n}\n\n@media(max-width:1000px){\n  .case-editorial-pair figure:first-child{height:440px!important}\n  .case-editorial-pair figure:first-child img{object-position:left 44%!important;transform:scale(1.003)}\n}\n@media(max-width:760px){\n  .case-editorial-pair figure:first-child{height:320px!important}\n  .case-editorial-pair figure:first-child img{object-position:left 46%!important;transform:none}\n}\n</style>\n'''
s = s.replace('</head>', polish + '</head>', 1)

Path('casos/san-jorge.html').write_text(s, encoding='utf-8')
