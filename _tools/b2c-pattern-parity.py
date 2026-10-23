from pathlib import Path
import re

p = Path('industrias/marcas-b2c.html')
s = p.read_text()

# Outcomes: add decorative visuals matching the B2B / Education card system.
old = '''<div class="b2cr-outcomes-grid"><a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-social"><small>CONTENIDO & COMUNIDAD</small><h3>Una marca que se mantiene presente.</h3><p>Contenido, formatos, storytelling y distribución para construir atención, identidad y conversación.</p><span>Fortalecer marca →</span></a><a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-ads"><small>PERFORMANCE & CONVERSIÓN</small><h3>Más intención llegando a tu negocio.</h3><p>Campañas y audiencias diseñadas para transformar atención en tráfico, reservas, compras y visitas.</p><span>Generar demanda →</span></a><a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-web"><small>EXPERIENCIA DIGITAL</small><h3>Menos fricción entre mirar y comprar.</h3><p>Webs y landings que ordenan propuesta, información y llamados a la acción para facilitar la decisión.</p><span>Mejorar experiencia →</span></a><a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-flow"><small>RETENCIÓN & AUTOMATIZACIÓN</small><h3>Más valor después de la primera compra.</h3><p>Seguimiento, automatizaciones y datos para conectar campañas, clientes y operación.</p><span>Conectar el sistema →</span></a></div>'''
new = '''<div class="b2cr-outcomes-grid">
<a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-social"><div class="b2cr-outcome-visual" aria-hidden="true"><svg viewBox="0 0 108 78"><circle cx="22" cy="39" r="8"/><circle cx="54" cy="20" r="8"/><circle cx="85" cy="38" r="8"/><circle cx="55" cy="59" r="8"/><path d="M29 34 47 24M62 24l16 9M78 44 62 55M47 54 29 44"/></svg></div><small>CONTENIDO & COMUNIDAD</small><h3>Una marca que se mantiene presente.</h3><p>Contenido, formatos, storytelling y distribución para construir atención, identidad y conversación.</p><span>Fortalecer marca →</span></a>
<a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-ads"><div class="b2cr-outcome-visual" aria-hidden="true"><svg viewBox="0 0 108 78"><path d="M16 61h76"/><path d="M24 57V43h14v14M47 57V31h14v26M70 57V20h14v37"/><path d="m21 29 20-9 18 5 25-14"/></svg></div><small>PERFORMANCE & CONVERSIÓN</small><h3>Más intención llegando a tu negocio.</h3><p>Campañas y audiencias diseñadas para transformar atención en tráfico, reservas, compras y visitas.</p><span>Generar demanda →</span></a>
<a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-web"><div class="b2cr-outcome-visual" aria-hidden="true"><svg viewBox="0 0 108 78"><rect x="12" y="12" width="84" height="54" rx="8"/><path d="M12 25h84"/><circle cx="23" cy="19" r="2"/><circle cx="31" cy="19" r="2"/><path d="M24 39h28M24 48h45M24 57h35"/></svg></div><small>EXPERIENCIA DIGITAL</small><h3>Menos fricción entre mirar y comprar.</h3><p>Webs y landings que ordenan propuesta, información y llamados a la acción para facilitar la decisión.</p><span>Mejorar experiencia →</span></a>
<a class="b2cr-outcome b2cr-reveal" href="https://lowsignal.cl/soluciones/low-flow"><div class="b2cr-outcome-visual" aria-hidden="true"><svg viewBox="0 0 108 78"><rect x="12" y="29" width="22" height="20" rx="5"/><rect x="74" y="12" width="22" height="20" rx="5"/><rect x="74" y="47" width="22" height="20" rx="5"/><circle cx="54" cy="39" r="8"/><path d="M34 39h12M62 35l12-10M62 43l12 11"/></svg></div><small>RETENCIÓN & AUTOMATIZACIÓN</small><h3>Más valor después de la primera compra.</h3><p>Seguimiento, automatizaciones y datos para conectar campañas, clientes y operación.</p><span>Conectar el sistema →</span></a>
</div>'''
if old not in s:
    raise SystemExit('outcomes markup not found')
s = s.replace(old, new, 1)

# Why cards: replace numeric markers with actual icons.
old = '''<div class="b2cr-why-grid"><article><i>01</i><h3>Velocidad para ejecutar</h3><p>Contenido y campañas preparados para moverse con temporadas, lanzamientos y oportunidades.</p></article><article><i>02</i><h3>Consistencia de marca</h3><p>Cada punto de contacto refuerza una misma idea, estética y experiencia.</p></article><article><i>03</i><h3>Creatividad con performance</h3><p>No separamos lo que se ve de lo que convierte: ambas cosas trabajan juntas.</p></article><article><i>04</i><h3>Un sistema conectado</h3><p>Contenido, Ads, web, automatización y datos alrededor del mismo objetivo.</p></article></div>'''
new = '''<div class="b2cr-why-grid">
<article><div class="b2cr-proof-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m13 2-7 11h6l-1 9 7-12h-6l1-8Z"/></svg></div><h3>Velocidad para ejecutar</h3><p>Contenido y campañas preparados para moverse con temporadas, lanzamientos y oportunidades.</p></article>
<article><div class="b2cr-proof-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 4V2M20 12h2M12 20v2M4 12H2"/></svg></div><h3>Consistencia de marca</h3><p>Cada punto de contacto refuerza una misma idea, estética y experiencia.</p></article>
<article><div class="b2cr-proof-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 18V10M10 18V6M16 18v-4M3 20h18"/><path d="m14 4 .8 1.8L17 6.6l-1.8.8-.8 1.8-.8-1.8-1.8-.8 1.8-.8L14 4Z"/></svg></div><h3>Creatividad con performance</h3><p>No separamos lo que se ve de lo que convierte: ambas cosas trabajan juntas.</p></article>
<article><div class="b2cr-proof-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="3" y="9" width="6" height="6" rx="2"/><rect x="15" y="3" width="6" height="6" rx="2"/><rect x="15" y="15" width="6" height="6" rx="2"/><path d="M9 12h3c2 0 3-1 3-3M12 12c2 0 3 1 3 3"/></svg></div><h3>Un sistema conectado</h3><p>Contenido, Ads, web, automatización y datos alrededor del mismo objetivo.</p></article>
</div>'''
if old not in s:
    raise SystemExit('why markup not found')
s = s.replace(old, new, 1)

# Testimonial arrows: use the same SVG arrow system as B2B / Education.
old = '''<div class="b2cr-controls"><button class="b2cr-prev" aria-label="Testimonio anterior">←</button><button class="b2cr-next" aria-label="Siguiente testimonio">→</button></div>'''
new = '''<div class="b2cr-controls" aria-label="Navegar testimonios"><button class="b2cr-control b2cr-prev" type="button" aria-label="Testimonio anterior"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m15 6-6 6 6 6"/><path d="M9 12h10"/></svg></button><button class="b2cr-control b2cr-next" type="button" aria-label="Siguiente testimonio"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 6 6 6-6 6"/><path d="M5 12h10"/></svg></button></div>'''
if old not in s:
    raise SystemExit('testimonial controls markup not found')
s = s.replace(old, new, 1)

css = r'''<style id="b2c-pattern-parity-v1">
/* Match the card visual language used by B2B / Education */
.b2cr-outcome{position:relative!important;overflow:hidden!important;padding:30px!important}
.b2cr-outcome-visual{position:absolute;right:28px;top:28px;width:108px;height:78px;color:#D9DFFE;opacity:.82;transition:transform .22s ease,color .22s ease,opacity .22s ease;pointer-events:none}
.b2cr-outcome-visual svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.b2cr-outcome h3{max-width:68%!important;margin-top:44px!important}
.b2cr-outcome p{max-width:82%!important}
.b2cr-outcome:hover .b2cr-outcome-visual{transform:translateY(-3px);color:#B9C5FF;opacity:1}

/* Same proof icon system as B2B */
.b2cr-why-grid i{display:none!important}
.b2cr-proof-icon{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:rgba(138,164,255,.10);color:#8AA4FF;transition:background .2s ease,color .2s ease,transform .2s ease}
.b2cr-proof-icon svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.b2cr-why-grid article:hover .b2cr-proof-icon{transform:translateY(-2px);background:rgba(138,164,255,.16);color:#AFC0FF}

/* Exact testimonial arrow treatment */
.b2cr-controls{position:absolute!important;left:76px!important;bottom:54px!important;top:auto!important;right:auto!important;z-index:5!important;display:flex!important;gap:10px!important}
.b2cr-control{width:48px!important;height:48px!important;padding:0!important;border:1px solid rgba(255,255,255,.28)!important;border-radius:50%!important;background:rgba(5,10,24,.38)!important;color:#fff!important;display:grid!important;place-items:center!important;cursor:pointer!important;transition:background .2s ease,border-color .2s ease,transform .2s ease!important}
.b2cr-control svg{width:19px!important;height:19px!important;fill:none!important;stroke:currentColor!important;stroke-width:1.8!important;stroke-linecap:round!important;stroke-linejoin:round!important}
.b2cr-control:hover{transform:translateY(-2px)!important;background:rgba(255,255,255,.12)!important;border-color:rgba(255,255,255,.46)!important}
.b2cr-control:focus-visible{outline:2px solid #A8B8FF!important;outline-offset:3px!important}

@media(max-width:760px){
  .b2cr-outcome{padding:24px!important;min-height:225px!important}
  .b2cr-outcome-visual{right:22px;top:22px;width:92px;height:66px}
  .b2cr-outcome h3{max-width:72%!important;margin-top:40px!important;font-size:22px!important}
  .b2cr-outcome p{max-width:100%!important}
  .b2cr-controls{left:auto!important;right:24px!important;top:24px!important;bottom:auto!important}
  .b2cr-control{width:40px!important;height:40px!important}
  .b2cr-control svg{width:17px!important;height:17px!important}
}
</style>'''

if 'b2c-pattern-parity-v1' in s:
    s = re.sub(r'<style id="b2c-pattern-parity-v1">.*?</style>', css, s, count=1, flags=re.S)
else:
    s = s.replace('</head>', css + '\n</head>', 1)

p.write_text(s)
