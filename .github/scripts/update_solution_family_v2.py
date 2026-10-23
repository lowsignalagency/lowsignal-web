from pathlib import Path
import re

configs = {
  'soluciones/low-ads.html': {
    'name':'Low Ads','process':'ads-new-process',
    'cards':[
      ('Estrategia de demanda','Definimos qué acción necesita generar la pauta y qué rol cumple cada campaña dentro del crecimiento.'),
      ('Medición confiable','Construimos una lectura clara de conversiones para decidir con señales reales, no con métricas de vanidad.'),
      ('Creatividad que aprende','Tratamos cada pieza como una hipótesis: probamos mensajes, formatos y ángulos para descubrir qué mueve resultados.'),
      ('Canales coordinados','Meta, Google, LinkedIn y TikTok cumplen funciones distintas dentro de una misma estrategia.'),
      ('Inversión eficiente','Movemos presupuesto hacia lo que demuestra tracción y reducimos gasto donde no hay señal.'),
      ('Aprendizaje de performance','Cada ciclo deja información útil para mejorar audiencias, creatividad, oferta y conversión.')],
    'includes':[
      ('Estrategia',['Objetivos y funnel','Plan de medios','Audiencias prioritarias','Distribución de presupuesto','Roadmap de campañas']),
      ('Tracking',['Píxeles y eventos','Conversiones','UTMs','Configuración analítica','Dashboard de performance']),
      ('Creatividad',['Conceptos para ads','Copywriting','Piezas gráficas','Video ads','Variantes para testing']),
      ('Gestión & optimización',['Meta Ads','Google Ads','LinkedIn / TikTok','Tests A/B','Optimización y reportes'])]
  },
  'soluciones/low-web.html': {
    'name':'Low Web','process':'web-new-process',
    'cards':[
      ('Propuesta digital clara','Ordenamos el mensaje para que cada persona entienda rápido qué haces, por qué importa y qué debe hacer después.'),
      ('Experiencia que guía','Diseñamos recorridos simples y coherentes que reducen fricción y acercan al usuario a la acción.'),
      ('Arquitectura de conversión','Cada página cumple un objetivo dentro del journey: informar, generar confianza, captar o convertir.'),
      ('Velocidad & confianza','Construimos una experiencia rápida, responsive y sólida que se siente profesional en cualquier dispositivo.'),
      ('Ecosistema conectado','La web conversa con CRM, agenda, pagos, analítica y las herramientas que sostienen la operación.'),
      ('Evolución continua','Después del lanzamiento seguimos leyendo comportamiento y mejorando lo que realmente mueve resultados.')],
    'includes':[
      ('Estrategia',['Discovery de negocio','Arquitectura de información','Mapa de páginas','Journey del usuario','Objetivos de conversión']),
      ('Diseño',['UX/UI a medida','Wireframes','Diseño responsive','Sistema visual','Copy y contenido web']),
      ('Desarrollo',['Desarrollo web','CMS cuando aplica','SEO técnico','Performance','QA y publicación']),
      ('Integraciones & evolución',['Formularios y CRM','Agenda / pagos','Analytics','Mantención','Mejoras continuas'])]
  },
  'soluciones/low-flow.html': {
    'name':'Low Flow','process':'flow-new-process',
    'cards':[
      ('Fricción visible','Detectamos tareas repetitivas, dobles registros y puntos donde la operación pierde tiempo o información.'),
      ('Operación conectada','Hacemos que herramientas y datos trabajen como un sistema en lugar de vivir en silos.'),
      ('Automatización por eventos','Diseñamos flujos que reaccionan a lo que ocurre y ejecutan acciones sin depender de trabajo manual.'),
      ('IA aplicada','Integramos IA donde realmente agrega valor: clasificar, resumir, responder, enriquecer o apoyar decisiones.'),
      ('Trazabilidad','Cada flujo deja señales para saber qué ocurrió, dónde falló y qué se puede mejorar.'),
      ('Operación escalable','Convertimos procesos repetitivos en infraestructura que soporta más volumen sin sumar la misma fricción.')],
    'includes':[
      ('Diagnóstico',['Mapeo de procesos','Cuellos de botella','Inventario de herramientas','Casos de uso','Priorización por impacto']),
      ('Automatización',['Workflows automáticos','Triggers y reglas','Notificaciones','Sincronización de datos','Aprobaciones']),
      ('IA & integraciones',['Agentes de IA','OpenAI / modelos','CRM','Email / formularios','APIs y webhooks']),
      ('Operación & mejora',['Pruebas','Monitoreo','Documentación','Ajustes','Nuevos flujos'])]
  },
  'soluciones/low-apps.html': {
    'name':'Low Apps','process':'apps-new-process',
    'cards':[
      ('Claridad de producto','Aterrizamos problema, usuario y oportunidad antes de convertir ideas en funcionalidades.'),
      ('Experiencia centrada en uso','Diseñamos flujos simples y comprensibles para que el producto sea fácil de adoptar.'),
      ('Validación rápida','Construimos lo suficiente para aprender temprano y evitar invertir meses en supuestos.'),
      ('Construcción robusta','Desarrollamos una base técnica preparada para crecer, integrarse y evolucionar.'),
      ('Capacidades inteligentes','Sumamos IA cuando mejora de verdad la experiencia o hace al producto más útil.'),
      ('Evolución de producto','Usamos feedback y métricas para priorizar lo siguiente y mantener el producto avanzando.')],
    'includes':[
      ('Discovery',['Problema y usuarios','Hipótesis','Priorización','Alcance','Roadmap inicial']),
      ('Diseño',['User flows','Wireframes','Prototipos','UX/UI','Design system']),
      ('Desarrollo',['MVP','Web apps','Mobile cuando aplica','Backend e integraciones','QA y despliegue']),
      ('Producto & evolución',['Métricas de uso','Analytics','IA en producto','Iteración','Nuevas capacidades'])]
  },
  'soluciones/low-scale.html': {
    'name':'Low Scale','process':'scale-new-process',
    'cards':[
      ('Claridad de crecimiento','Identificamos qué está frenando el crecimiento y dónde existe la oportunidad con mayor impacto.'),
      ('Un solo roadmap','Marca, adquisición, conversión, automatización y datos avanzan bajo prioridades compartidas.'),
      ('Adquisición conectada','Contenido, pauta y web trabajan juntos para generar y capturar demanda.'),
      ('Conversión & seguimiento','Conectamos CRM y procesos para que las oportunidades no se pierdan después del primer contacto.'),
      ('Medición compartida','Unimos señales de distintos canales para entender qué mueve el negocio de verdad.'),
      ('Escala sistemática','Repetimos, automatizamos y expandimos lo que funciona en lugar de crecer a punta de iniciativas aisladas.')],
    'includes':[
      ('Estrategia',['Diagnóstico de crecimiento','Objetivos y prioridades','Growth roadmap','Hipótesis','Plan de experimentos']),
      ('Adquisición',['Low Social','Low Ads','Low Web','Contenido y campañas','Optimización de conversión']),
      ('Operación',['CRM','Low Flow','Automatizaciones','Integraciones','Seguimiento comercial']),
      ('Datos & escala',['Dashboard','Métricas clave','Insights','Experimentación','Optimización continua'])]
  }
}

css = '''
<style id="solution-family-includes-v2">
.solution-family-includes{padding:112px 0 116px;background:#F7F9FD;color:#101010;border-top:1px solid #E2E8F3;border-bottom:1px solid #E2E8F3}
.solution-family-includes .ls-social-section-kicker{color:#1419E0}
.solution-family-includes h2{max-width:980px;margin:18px 0 0;font-size:clamp(38px,4vw,56px);line-height:1.06;letter-spacing:-.045em;font-weight:300;color:#101010}
.solution-family-includes h2 strong{color:#1419E0;font-weight:300}
.solution-family-includes-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:56px;margin-top:72px}
.solution-family-includes-col h3{margin:0 0 30px;color:#68707C;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono",monospace;font-size:12px;line-height:1.2;font-weight:500;letter-spacing:.12em;text-transform:uppercase}
.solution-family-includes-col ul{list-style:none;margin:0;padding:0}
.solution-family-includes-col li{position:relative;min-height:28px;margin:0 0 18px;padding:4px 0 0 42px;color:#343942;font-size:14px;line-height:1.45}
.solution-family-includes-col li:before{content:"✓";position:absolute;left:0;top:-1px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:#DCE9FF;color:#1419E0;font-size:12px;font-weight:700}
@media(min-width:761px){.ls-social-faq-item summary{min-height:56px!important;padding:14px 0!important;font-size:14px!important}.ls-social-faq-answer p{font-size:13px!important}}
@media(max-width:980px){.solution-family-includes-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:48px 52px}}
@media(max-width:760px){.solution-family-includes{padding:80px 0 84px}.solution-family-includes h2{font-size:36px}.solution-family-includes-grid{grid-template-columns:1fr;gap:42px;margin-top:54px}.solution-family-includes-col h3{margin-bottom:24px}.solution-family-includes-col li{font-size:14px}}
@media(prefers-reduced-motion:reduce){.solution-family-includes .ls-scroll-reveal,.solution-family-includes .ls-scroll-stagger,.solution-family-includes .ls-scroll-stagger>*{opacity:1!important;transform:none!important;transition:none!important}}
</style>
'''

scroll_js = '''
<script id="solution-family-scroll-v2">
(function(){
 function init(){
  const targets=[];
  document.querySelectorAll('.solution-family-includes .ls-social-section-kicker,.solution-family-includes h2').forEach(function(el){el.classList.add('ls-scroll-reveal');targets.push(el)});
  document.querySelectorAll('.solution-family-includes-grid').forEach(function(el){el.classList.add('ls-scroll-stagger');targets.push(el)});
  if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches){targets.forEach(function(el){el.classList.add('is-visible')});return}
  if(!('IntersectionObserver' in window)){targets.forEach(function(el){el.classList.add('is-visible')});return}
  const io=new IntersectionObserver(function(entries){entries.forEach(function(entry){if(entry.isIntersecting){entry.target.classList.add('is-visible');io.unobserve(entry.target)}})},{threshold:.12,rootMargin:'0px 0px -8% 0px'});
  targets.forEach(function(el){if(!el.classList.contains('is-visible'))io.observe(el)});
 }
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

def cards_html(cards):
  out=['      <div class="ls-social-feature-grid">']
  for i,(title,text) in enumerate(cards,1):
    out += ['        <article class="ls-social-feature-card">',f'          <div class="ls-social-feature-icon">{i:02d}</div>',f'          <h3>{title}</h3>',f'          <p>{text}</p>','        </article>']
  out.append('      </div>')
  return '\n'.join(out)

def includes_html(name, cols):
  parts=['  <section class="solution-family-includes" aria-label="Qué incluye '+name+'">','    <div class="ls-social-shell">',f'      <p class="ls-social-section-kicker">{name.upper()}</p>',f'      <h2>Todo lo que incluye <strong>{name}.</strong></h2>','      <div class="solution-family-includes-grid">']
  for heading,items in cols:
    parts += ['        <div class="solution-family-includes-col">',f'          <h3>{heading}</h3>','          <ul>']
    parts += [f'            <li>{x}</li>' for x in items]
    parts += ['          </ul>','        </div>']
  parts += ['      </div>','    </div>','  </section>']
  return '\n'.join(parts)

for filename,cfg in configs.items():
  p=Path(filename)
  s=p.read_text()

  # Replace the six execution-oriented cards with value/capability cards.
  grid=cards_html(cfg['cards'])
  s,n=re.subn(r'      <div class="ls-social-feature-grid">.*?      </div>\n    </div>\n  </section>',grid+'\n    </div>\n  </section>',s,count=1,flags=re.S)
  if n!=1:
    raise RuntimeError(f'Could not replace feature grid in {filename}: {n}')

  # Remove duplicated proof from solution pages; proof now lives on Home + Industry pages.
  s=re.sub(r'\s*<section class="solution-testimonial[^\"]*">.*?</section>\s*','\n',s,count=1,flags=re.S)

  # Add tangible scope before the process section.
  if 'solution-family-includes' not in s:
    marker=f'  <section class="{cfg["process"]}"'
    idx=s.find(marker)
    if idx<0: raise RuntimeError(f'Process marker missing in {filename}')
    s=s[:idx]+includes_html(cfg['name'],cfg['includes'])+'\n\n'+s[idx:]

  if 'solution-family-includes-v2' not in s:
    s=s.replace('</head>',css+'\n</head>',1)
  if 'solution-family-scroll-v2' not in s:
    s=s.replace('</body>',scroll_js+'\n</body>',1)

  p.write_text(s)
