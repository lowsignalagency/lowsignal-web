from pathlib import Path
import re

p = Path('casos/rech.html')
s = p.read_text(encoding='utf-8')

repls = {
'La infraestructura digital<br> que impulsa a las<br> <strong>comunidades de la RECH.</strong>': 'Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong>',
'Una red de colegios con muchas comunidades y una sola identidad. Construimos el sistema digital que las conecta.': 'Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.',
'Muchas comunidades.<br><strong>Una sola identidad.</strong>': 'De una red dispersa<br><strong>a un sistema que se entiende.</strong>',
'El desafío era construir coherencia a nivel de red sin borrar la identidad propia de cada colegio y cada comunidad educativa.': 'La RECH no necesitaba simplemente “verse mejor”. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.',
'Una red visible.<br><strong>Una comunidad conectada.</strong>': 'No diseñamos una página.<br><strong>Construimos un sistema digital.</strong>',
'El trabajo conectó identidad, web y contenido para ordenar la comunicación de la red y dar espacio a las historias de cada comunidad.': 'Cada pieza tenía que cumplir un rol: explicar la red, representar a sus colegios, ordenar la información y hacer visible la vida que ocurre dentro de sus comunidades.'
}
for a,b in repls.items():
    s = s.replace(a,b)

story_start = s.index('<section class="case-new-story case-rech-story">')
story_end = s.index('</section>', story_start) + len('</section>')
story = s[story_start:story_end]
pat = re.compile(r'<div class="case-new-steps">\s*<article.*?</article>\s*<article.*?</article>\s*<article.*?</article>\s*</div>', re.S)
new_cards = '''<div class="case-new-steps rech-v4-steps">
        <article><span>01</span><div><small>LO QUE ENCONTRAMOS</small><h3>Una red con múltiples colegios, audiencias y puntos de contacto, pero sin una experiencia digital que mostrara esa escala con claridad.</h3></div></article>
        <article><span>02</span><div><small>LO QUE CONSTRUIMOS</small><h3>Un sistema digital común: identidad, arquitectura web y contenido conectados para que la red se vea coherente sin borrar la personalidad de cada comunidad.</h3></div></article>
        <article class="is-highlight"><span>03</span><div><small>LO QUE CAMBIÓ</small><h3>La RECH pasó de comunicar piezas aisladas a tener una presencia más ordenada, reconocible y preparada para crecer junto a sus colegios.</h3></div></article>
      </div>'''
story2, n = pat.subn(new_cards, story, count=1)
if n != 1:
    raise RuntimeError(f'RECH cards replacement failed: {n}')
s = s[:story_start] + story2 + s[story_end:]

work_start = s.index('<section class="case-new-work case-rech-work">')
gallery_match = re.search(r'<div class="[^"]*case-new-gallery[^"]*">', s[work_start:])
if not gallery_match:
    raise RuntimeError('RECH gallery not found')
gallery_pos = work_start + gallery_match.start()
if 'rech-v4-build-grid' not in s[work_start:gallery_pos]:
    ribbon = '''<div class="rech-v4-build-grid" aria-label="Lo que construimos">
        <article><span>01</span><div><b>Arquitectura digital</b><p>Una experiencia común para entender la red y navegar sus comunidades con menos fricción.</p></div></article>
        <article><span>02</span><div><b>Identidad consistente</b><p>Un lenguaje visual y editorial que conecta a la RECH sin volver idénticos a sus colegios.</p></div></article>
        <article><span>03</span><div><b>Contenido con propósito</b><p>Historias, hitos y vida escolar convertidos en señales de confianza para familias y comunidad.</p></div></article>
        <article><span>04</span><div><b>Base para crecer</b><p>Un sistema más claro para sumar nuevos contenidos, campañas y puntos de contacto sin partir de cero.</p></div></article>
      </div>\n      '''
    s = s[:gallery_pos] + ribbon + s[gallery_pos:]

if 'rech-v4-outcome-band' not in s:
    anchor = '<section class="case-new-testimonial case-rech-testimonial">'
    outcome = '''<section class="rech-v4-outcome-band">
    <div class="container rech-v4-outcome-inner">
      <p class="case-new-eyebrow">LA TRANSFORMACIÓN</p>
      <h2>Más que una nueva presencia digital: <strong>una red más fácil de entender, recorrer y reconocer.</strong></h2>
      <p>El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.</p>
    </div>
  </section>\n\n  '''
    s = s.replace(anchor, outcome + anchor, 1)

css = '''
<style id="rech-story-refresh-v4">
.case-rech-hero h1{max-width:1020px!important}
.case-rech-hero .case-new-hero-grid>div:first-child>p{max-width:780px!important;color:#C7D0E2!important}
.case-rech-story .case-new-story-head{align-items:start!important}
.case-rech-story .case-new-steps.rech-v4-steps{gap:18px!important;margin-top:58px!important}
.case-rech-story .rech-v4-steps article{position:relative!important;min-height:290px!important;padding:30px!important;border-radius:20px!important;background:#F8FAFD!important;border:1px solid #E1E6F0!important;overflow:hidden!important}
.case-rech-story .rech-v4-steps article:after{content:"";position:absolute;right:-42px;top:-44px;width:150px;height:150px;border-radius:50%;border:1px solid rgba(20,25,224,.08);background:rgba(20,25,224,.025)}
.case-rech-story .rech-v4-steps article>span{position:relative;z-index:2;display:inline-flex!important;align-items:center!important;justify-content:center!important;width:42px!important;height:42px!important;border-radius:12px!important;background:#E9EDFF!important;color:#1419E0!important;font-size:10px!important;font-weight:700!important}
.case-rech-story .rech-v4-steps article>div{position:relative;z-index:2;margin-top:auto!important}
.case-rech-story .rech-v4-steps small{display:block!important;color:#7A86A0!important;font-size:9px!important;font-weight:700!important;letter-spacing:.17em!important}
.case-rech-story .rech-v4-steps h3{max-width:95%!important;margin:14px 0 0!important;color:#17224F!important;font-size:19px!important;line-height:1.48!important;letter-spacing:-.02em!important;font-weight:450!important}
.case-rech-story .rech-v4-steps .is-highlight{background:linear-gradient(145deg,#1419E0 0%,#2447F5 100%)!important;border-color:transparent!important;box-shadow:0 22px 48px rgba(20,25,224,.20)!important}
.case-rech-story .rech-v4-steps .is-highlight:after{border-color:rgba(255,255,255,.14);background:rgba(255,255,255,.035)}
.case-rech-story .rech-v4-steps .is-highlight>span{background:rgba(255,255,255,.14)!important;color:#fff!important}
.case-rech-story .rech-v4-steps .is-highlight small{color:#C9D2FF!important}.case-rech-story .rech-v4-steps .is-highlight h3{color:#fff!important}
.rech-v4-build-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;margin-top:52px;border:1px solid rgba(255,255,255,.12);border-radius:22px;overflow:hidden;background:rgba(255,255,255,.10)}
.rech-v4-build-grid article{min-height:230px;padding:26px;display:flex;flex-direction:column;justify-content:space-between;background:#0B1530;transition:background .22s ease}
.rech-v4-build-grid article:hover{background:#101D3B}.rech-v4-build-grid article>span{color:#8297FF;font-size:10px;font-weight:700}.rech-v4-build-grid b{display:block;color:#fff;font-size:18px;line-height:1.25;font-weight:500;letter-spacing:-.02em}.rech-v4-build-grid p{margin:10px 0 0;color:#AAB5CE;font-size:12px;line-height:1.65}
.case-rech-work .case-new-gallery{margin-top:22px!important}.case-rech-work .case-new-gallery figure,.case-rech-work .case-new-gallery-copy{border-radius:18px!important}.case-rech-work .case-new-gallery-main{box-shadow:0 26px 60px rgba(0,0,0,.24)!important}
.rech-v4-outcome-band{padding:100px 0;background:#F3F6FC}.rech-v4-outcome-inner{display:grid;grid-template-columns:.36fr 1.18fr .78fr;gap:54px;align-items:start}.rech-v4-outcome-inner .case-new-eyebrow{margin-top:10px;color:#1419E0!important}.rech-v4-outcome-inner h2{margin:0;color:#071022;font-size:clamp(38px,4.1vw,56px);line-height:1.06;letter-spacing:-.05em;font-weight:300}.rech-v4-outcome-inner h2 strong{color:#1419E0;font-weight:300}.rech-v4-outcome-inner>p:last-child{margin:8px 0 0;color:#65718B;font-size:14px;line-height:1.8}
@media(max-width:980px){.rech-v4-build-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.rech-v4-outcome-inner{grid-template-columns:1fr;gap:22px}}
@media(max-width:760px){.case-rech-story .case-new-steps.rech-v4-steps{gap:12px!important;margin-top:34px!important}.case-rech-story .rech-v4-steps article{min-height:235px!important;padding:22px!important}.case-rech-story .rech-v4-steps h3{font-size:17px!important;max-width:100%!important}.rech-v4-build-grid{grid-template-columns:1fr;border-radius:18px}.rech-v4-build-grid article{min-height:185px;padding:22px}.rech-v4-outcome-band{padding:72px 0}.rech-v4-outcome-inner h2{font-size:34px}}
</style>
'''
s = re.sub(r'<style id="rech-story-refresh-v4">.*?</style>\s*', '', s, flags=re.S)
s = s.replace('</head>', css + '\n</head>', 1)
p.write_text(s, encoding='utf-8')
