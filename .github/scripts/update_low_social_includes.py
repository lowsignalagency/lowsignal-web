from pathlib import Path

p = Path('soluciones/low-social.html')
s = p.read_text()

marker = '  <section class="ls-social-smart">'
block = '''  <section class="ls-social-includes" aria-labelledby="ls-social-includes-title">
    <div class="ls-social-shell">
      <p class="ls-social-section-kicker">TODO LO QUE INCLUYE</p>
      <h2 id="ls-social-includes-title">Todo lo que incluye <strong>Low Social.</strong></h2>
      <div class="ls-social-includes-grid">
        <div class="ls-social-includes-col">
          <h3>Estrategia</h3>
          <ul>
            <li>Estrategia de contenido</li><li>Pilares editoriales</li><li>Planificación mensual</li><li>Definición de formatos</li><li>Calendario de publicaciones</li>
          </ul>
        </div>
        <div class="ls-social-includes-col">
          <h3>Contenido</h3>
          <ul>
            <li>Reels y videos</li><li>Posts y carruseles</li><li>Stories</li><li>Copywriting</li><li>Diseño gráfico</li>
          </ul>
        </div>
        <div class="ls-social-includes-col">
          <h3>Producción</h3>
          <ul>
            <li>Jornadas de contenido</li><li>Dirección creativa</li><li>Fotografía y video</li><li>Edición</li><li>Adaptación por plataforma</li>
          </ul>
        </div>
        <div class="ls-social-includes-col">
          <h3>Gestión & optimización</h3>
          <ul>
            <li>Publicación</li><li>Community management</li><li>Análisis de desempeño</li><li>Aprendizajes mensuales</li><li>Optimización continua</li>
          </ul>
        </div>
      </div>
    </div>
  </section>\n\n'''

if 'class="ls-social-includes"' not in s:
    if marker not in s:
        raise SystemExit('Content System marker not found')
    s = s.replace(marker, block + marker, 1)

css = '''
<style id="low-social-includes-v1">
.ls-social-includes{padding:104px 0 108px;background:#F7F8FA;color:#101010}
.ls-social-includes .ls-social-section-kicker{color:#1419E0}
.ls-social-includes h2{max-width:980px;margin:18px 0 0;font-size:clamp(38px,4vw,56px);line-height:1.06;letter-spacing:-.045em;font-weight:300;color:#101010}
.ls-social-includes h2 strong{color:#1419E0;font-weight:300}
.ls-social-includes-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:56px;margin-top:72px}
.ls-social-includes-col h3{margin:0 0 30px;color:#68707C;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono",monospace;font-size:12px;line-height:1.2;font-weight:500;letter-spacing:.12em;text-transform:uppercase}
.ls-social-includes-col ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:18px}
.ls-social-includes-col li{position:relative;padding-left:44px;color:#202020;font-size:14px;line-height:1.48}
.ls-social-includes-col li:before{content:"✓";position:absolute;left:0;top:-1px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:#E9F2FF;color:#1682FF;font-size:12px;font-weight:700}
@media(max-width:980px){.ls-social-includes-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:52px 48px}}
@media(max-width:760px){.ls-social-includes{padding:74px 0 78px}.ls-social-includes h2{font-size:38px}.ls-social-includes-grid{grid-template-columns:1fr;gap:42px;margin-top:48px}.ls-social-includes-col h3{margin-bottom:22px}.ls-social-includes-col li{font-size:13px;padding-left:42px}}
</style>
'''
if 'low-social-includes-v1' not in s:
    s = s.replace('</head>', css + '</head>', 1)

old = '''        <details class="ls-social-faq-item"><summary>¿Qué incluye el servicio de Low Social?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Conectamos estrategia, planificación, diseño, producción y copywriting. También podemos incluir publicación, gestión de comunidad y análisis de resultados, según los objetivos y el alcance que definamos juntos.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿Low Social se adapta a mi industria?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Sí. Trabajamos con organizaciones de educación, empresas B2B y marcas B2C. Adaptamos los contenidos al negocio, su audiencia y la forma en que cada marca necesita crecer.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿Tengo que entregarles las fotos y los videos?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Podemos trabajar con material que ya tengas o planificar nuevas piezas gráficas y audiovisuales. Definimos el formato y la producción según la estrategia y los recursos de cada proyecto.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿También publican y gestionan las redes?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Podemos encargarnos de la publicación y la gestión de comunidad como parte del servicio. Acordamos esos canales y responsabilidades al definir el alcance mensual.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿Cómo medimos si el contenido está funcionando?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Revisamos el desempeño de las piezas y los canales para reconocer qué genera interés, interacción o demanda. Con esos aprendizajes ajustamos la planificación del siguiente ciclo.</p></div></details>'''

new = '''        <details class="ls-social-faq-item"><summary>¿Cómo se define cuántas piezas hacemos al mes?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>La frecuencia se define según el plan, los canales prioritarios y los objetivos de la marca. Buscamos un volumen que permita mantener consistencia, producir bien y aprender de lo que funciona.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿Low Social se adapta a mi industria?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Sí. Trabajamos con organizaciones de educación, empresas B2B y marcas B2C. Adaptamos la estrategia, los formatos y el tono al negocio, su audiencia y la forma en que necesita crecer.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿Tengo que entregarles las fotos y los videos?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>No necesariamente. Podemos trabajar con material existente o planificar jornadas de producción para generar nuevas piezas gráficas, fotografía y video según la estrategia.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿Pueden trabajar junto a nuestro equipo interno?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Sí. Podemos complementar a marketing, diseño, comunicaciones o dirección, definiendo responsabilidades claras para que la producción y la gestión mensual funcionen como un solo sistema.</p></div></details>
        <details class="ls-social-faq-item"><summary>¿Cómo medimos si el contenido está funcionando?<span class="ls-social-faq-icon" aria-hidden="true"></span></summary><div class="ls-social-faq-answer"><p>Revisamos el desempeño de piezas y canales para identificar qué genera atención, interacción, tráfico o demanda. Con esos aprendizajes ajustamos la planificación del siguiente ciclo.</p></div></details>'''

if old in s:
    s = s.replace(old, new, 1)
elif '¿Cómo se define cuántas piezas hacemos al mes?' not in s:
    raise SystemExit('FAQ block not found')

p.write_text(s)
