from pathlib import Path
import re

src = Path('casos/rech.html').read_text(encoding='utf-8')
s = src

# Page metadata
s = re.sub(r'<title>.*?</title>', '<title>Colegio Salvador Dalí | Customer Story · lowsignal</title>', s, count=1, flags=re.S)
s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Cómo lowsignal conectó contenido, campañas y web para acercar la vida del Colegio Salvador Dalí a nuevas familias.">', s, count=1)
s = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://lowsignal.cl/casos/salvador-dali">', s, count=1)

# Keep the exact RECH visual system/classes and only swap the case content.
replacements = {
    'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>': 'La vida del colegio.<br><strong>Más cerca de las familias.</strong>',
    'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.': 'Conectamos redes, campañas y web para mostrar la experiencia del Colegio Salvador Dalí y acompañar a nuevas familias desde el primer contacto hasta la postulación.',
    'Red Educacional Camilo Henríquez': 'Colegio Salvador Dalí',
    'Web · Social · Contenido': 'Social · Paid Media · Web',
    'https://lowsignal.cl/assets/rech-logo-full-white-trim.png': 'https://lowsignal.cl/assets/logo-dali-darkbg.png',
    'Una identidad común para conectar colegios, familias y comunidades sin perder la voz propia de cada establecimiento.': 'Una presencia digital conectada para mostrar lo que se vive dentro del colegio y acompañar a las familias durante la admisión.',
    'https://lowsignal.cl/assets/comunidad-rech.jpg': 'https://lowsignal.cl/assets/dali-patio-nueva.jpg',
    'Comunidad Colegio Salvador Dalí': 'Colegio Salvador Dalí',
    'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>': 'Un colegio con mucho que mostrar.<br><strong>Una experiencia digital que debía hacerlo visible.</strong>',
    'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.': 'El desafío no era simplemente publicar más. Era traducir la vida cotidiana del colegio en una presencia digital capaz de informar, generar confianza y acompañar a nuevas familias durante su decisión.',
    'Muchas voces, poca lectura de red.': 'Mucho valor dentro del colegio, pero poco visible fuera de él.',
    'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.': 'La comunidad vive experiencias, actividades y aprendizajes todos los días, pero sus canales digitales no alcanzaban a transmitir esa riqueza de forma consistente.',
    'Un sistema común, sin borrar identidades.': 'Un recorrido conectado entre contenido, campañas y web.',
    'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.': 'Ordenamos los puntos de contacto para que redes mostraran la vida del colegio, las campañas acercaran nuevas familias y la web ayudara a profundizar antes de postular.',
    'Una presencia más clara, reconocible y preparada para crecer.': 'Una presencia más cercana, clara y útil para decidir.',
    'La red dejó de comunicar piezas aisladas y pasó a tener una experiencia más ordenada para familias, estudiantes y comunidades.': 'El colegio pasó a tener una experiencia digital más coherente, capaz de conectar su día a día con el proceso de admisión y la relación con su comunidad.',
    'No hicimos una página.<br><strong>Construimos una forma de presentar la red.</strong>': 'No mostramos una institución.<br><strong>Mostramos cómo se vive dentro.</strong>',
    'Cada pieza tenía que cumplir un rol: explicar la RECH, representar a sus colegios, ordenar la información y hacer visible la vida que ocurre dentro de sus comunidades.': 'Cada canal debía cumplir un rol distinto, pero todos tenían que contar la misma historia del colegio y acompañar a las familias en una experiencia continua.',
    'https://lowsignal.cl/assets/reunion-rech.jpg': 'https://lowsignal.cl/assets/dali-ig.jpg',
    'Reunión de la Colegio Salvador Dalí': 'Contenido digital Colegio Salvador Dalí',
    'WEB · SOCIAL · CONTENIDO': 'SOCIAL · PAID MEDIA · WEB',
    'Una experiencia común sin volver idénticos a sus colegios.': 'Del primer scroll a la postulación.',
    'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.': 'Contenido para descubrir, campañas para llegar a nuevas familias y una experiencia web que ayuda a entender el proyecto educativo antes de tomar una decisión.',
    'Más que una nueva presencia digital: <strong>una red más fácil de entender, recorrer y reconocer.</strong>': 'Más que presencia digital: <strong>una forma más cercana de mostrar el colegio y acompañar a sus familias.</strong>',
    'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.': 'El resultado fue una experiencia más coherente entre lo que ocurre dentro del colegio y lo que una familia puede descubrir, entender y sentir desde afuera.',
    'lowsignal se ha convertido en un aliado estratégico para nuestra red. Entendieron nuestra visión y se involucraron de verdad en el proyecto.': 'Con lowsignal fortalecimos nuestras redes, nos acercamos a la comunidad y potenciamos las habilidades de nuestros estudiantes.',
    'https://lowsignal.cl/assets/nicolas-munoz.jpg': 'https://lowsignal.cl/assets/karina-csd.jpg',
    'Nicolás Muñoz': 'Karina Ravanal',
    'Director Ejecutivo, Colegio Salvador Dalí': 'Directora, Colegio Salvador Dalí',
    'https://lowsignal.cl/casos/salvador-dali': 'https://lowsignal.cl/casos/fcct',
    'https://lowsignal.cl/assets/dali-patio-nueva.jpg" alt="Colegio Salvador Dalí"><div class="rechx-next-overlay"': 'https://lowsignal.cl/assets/crecer-ninos.png" alt="Fundación Crecer con Todos"><div class="rechx-next-overlay"',
    '<h3>Colegio Salvador Dalí</h3><b>Ver caso ↗</b>': '<h3>Fundación Crecer con Todos</h3><b>Ver caso ↗</b>',
}
for old, new in replacements.items():
    s = s.replace(old, new)

# Correct visible image alts after broad client-name replacement.
s = s.replace('alt="Colegio Salvador Dalí"></figure>\n        <figure><img src="https://lowsignal.cl/assets/dali-patio-nueva.jpg" alt="Colegio Salvador Dalí"></figure>',
              'alt="Contenido digital Colegio Salvador Dalí"></figure>\n        <figure><img src="https://lowsignal.cl/assets/dali-patio-nueva.jpg" alt="Colegio Salvador Dalí"></figure>')

# Ensure quote role text is exact.
s = s.replace('Director Ejecutivo, Colegio Salvador Dalí', 'Directora, Colegio Salvador Dalí')

Path('casos/salvador-dali.html').write_text(s, encoding='utf-8')
