from pathlib import Path
import re

path = Path('casos.html')
s = path.read_text(encoding='utf-8')

# Remove the v3 archive-only redesign while preserving later content/image updates.
s = re.sub(r'\s*<style id="customer-stories-refresh-v3">.*?</style>\s*', '\n', s, flags=re.S | re.I)
s = re.sub(r'\s*<section class="stories-v3-proofbar">.*?</section>\s*', '\n', s, count=1, flags=re.S | re.I)

# Restore the archive copy the user approved before the v3 redesign.
replacements = {
    'Trabajo que se ve.<br><strong>Impacto que se siente.</strong>': 'Equipos que <strong>construyen.</strong>',
    'Casos reales de marcas, empresas e instituciones que transformaron su presencia digital junto a lowsignal.': 'Contenido, paid media, web y growth systems conectados a desafíos reales de negocio.',
    'Una experiencia digital que conecta a <strong>toda una comunidad educativa.</strong>': 'La infraestructura digital que impulsa a las <strong>comunidades de la RECH.</strong>',
    'Un ecosistema digital que convierte la vida del colegio en confianza para nuevas familias.': 'De las redes a la postulación: un recorrido digital para nuevas familias.',
    'Una experiencia digital para hacer visible una misión con impacto real.': 'Una plataforma para poner al frente la misión y los programas de la fundación.',
    'Una presencia digital que acerca el proyecto educativo a nuevas familias.': 'Una nueva web para conocer el proyecto educativo; sus redes muestran el día a día.',
    'De expertise técnico a una marca que se entiende y genera confianza.': 'Un servicio técnico complejo convertido en contenido claro para quienes deciden.',
    'Una presencia digital que convierte operación real en oportunidades comerciales.': 'De la operación en terreno a una presencia digital que muestra el trabajo de Dimor.',
    'Una web que ordena una operación compleja y la hace fácil de entender.': 'Una web clara para mostrar todo lo que mueve Rikdom.',
    'Contenido y performance conectados a una experiencia que se reserva.': 'Contenido y campañas que conectan la experiencia de hUB con las reservas.',
}
for new, old in replacements.items():
    s = s.replace(new, old)

# Trim the blank-line buildup left by repeated refresh runs.
s = re.sub(r'\n{5,}', '\n\n\n', s)

path.write_text(s, encoding='utf-8')
