from pathlib import Path
import re

profiles = {
    'damian-aldunate.html': {
        'name':'Damián Aldunate','role':'Co-Founder & CMO','kicker':'CO-FOUNDER & CMO · LOWSIGNAL',
        'positioning':'Marca, contenido y growth para convertir atención en <strong>crecimiento sostenido.</strong>',
        'summary':'Lidera estrategia de marca, marketing y crecimiento en lowsignal, conectando posicionamiento, contenido, campañas y ejecución comercial.',
        'about_title':'Marca que se <span>convierte en crecimiento.</span>',
        'about':['Trabaja en la intersección entre estrategia de marca y ejecución de marketing, buscando que cada punto de contacto tenga una función clara dentro del crecimiento.','En lowsignal conecta narrativa, contenido, paid media y dirección creativa para construir presencia de marca con intención comercial.'],
        'expertise':[('01','Brand strategy','Posicionamiento, narrativa y sistemas de marca.'),('02','Growth marketing','Adquisición, campañas y experimentación.'),('03','Content systems','Estrategia editorial, formatos y distribución.'),('04','Creative direction','Dirección de piezas y consistencia visual.')],
        'selected':[('Brand & Growth','Posicionamiento, contenido y campañas conectadas.'),('B2B / B2C','Estrategias para compañías y marcas de consumo.'),('lowsignal','Co-fundador y responsable de marketing y marca.')]
    },
    'matias-bussinger.html': {
        'name':'Matías Bussinger','role':'AI Engineer','kicker':'AI ENGINEER · LOWSIGNAL',
        'positioning':'IA, automatización y producto para convertir procesos complejos en <strong>sistemas más simples.</strong>',
        'summary':'Construye soluciones con inteligencia artificial, automatización e integraciones para productos y operaciones de lowsignal.',
        'about_title':'Tecnología aplicada a <span>problemas reales.</span>',
        'about':['Su foco está en llevar inteligencia artificial y automatización desde la idea a soluciones utilizables.','En lowsignal trabaja conectando modelos, datos, APIs e interfaces para construir productos y flujos que reduzcan trabajo manual y aumenten capacidad operativa.'],
        'expertise':[('01','AI engineering','Modelos, agentes y capacidades inteligentes.'),('02','Automation','Workflows, triggers e integraciones.'),('03','Product building','Prototipos y soluciones digitales.'),('04','Systems thinking','Conexión entre datos, herramientas y operación.')],
        'selected':[('Low Flow','Automatización e IA aplicada a operaciones.'),('Low Apps','Construcción de productos y capacidades digitales.'),('AI systems','Integraciones, agentes y workflows inteligentes.')]
    },
    'martin-alvarado.html': {
        'name':'Martín Alvarado','role':'Audiovisual Producer','kicker':'AUDIOVISUAL PRODUCER · LOWSIGNAL',
        'positioning':'Producción audiovisual para transformar ideas en <strong>historias que se sienten propias.</strong>',
        'summary':'Lidera producción audiovisual para contenidos, campañas y piezas de marca en lowsignal.',
        'about_title':'Producción con <span>intención de marca.</span>',
        'about':['Trabaja desde la planificación hasta la captura para que cada pieza tenga una intención clara, una estética coherente y material suficiente para distintos formatos.','En lowsignal participa en jornadas de contenido, campañas y producciones para clientes de distintas industrias.'],
        'expertise':[('01','Producción','Planificación y ejecución audiovisual.'),('02','Dirección','Criterio visual y coordinación de rodaje.'),('03','Contenido','Piezas para social, campañas y marca.'),('04','Formatos','Adaptación a distintos canales y necesidades.')],
        'selected':[('Content production','Jornadas de foto y video para marcas.'),('Campaigns','Producción para campañas y lanzamientos.'),('Low Social','Contenido audiovisual dentro de sistemas editoriales.')]
    },
    'jorge-munoz.html': {
        'name':'Jorge Muñoz','role':'Audiovisual Editor','kicker':'AUDIOVISUAL EDITOR · LOWSIGNAL',
        'positioning':'Edición y postproducción para convertir material en <strong>historias claras y memorables.</strong>',
        'summary':'Trabaja la edición audiovisual y postproducción de contenidos, campañas y piezas de marca en lowsignal.',
        'about_title':'Edición que ordena <span>ritmo y mensaje.</span>',
        'about':['Su trabajo se centra en transformar material bruto en piezas con ritmo, intención y consistencia visual.','En lowsignal edita contenidos para social, campañas y formatos audiovisuales adaptados a distintas plataformas.'],
        'expertise':[('01','Editing','Montaje, ritmo y estructura narrativa.'),('02','Postproduction','Ajustes visuales, sonido y terminaciones.'),('03','Social formats','Reels, piezas verticales y adaptaciones.'),('04','Brand consistency','Continuidad visual entre piezas y campañas.')],
        'selected':[('Social content','Edición de piezas para plataformas sociales.'),('Campaign assets','Formatos audiovisuales para campañas.'),('Low Social','Postproducción dentro de sistemas de contenido.')]
    },
    'lia-morice.html': {
        'name':'Lía Morice','role':'Content Creator','kicker':'CONTENT CREATOR · LOWSIGNAL',
        'positioning':'Contenido pensado para que las marcas se vean, se entiendan y <strong>conecten mejor.</strong>',
        'summary':'Crea contenido para redes, campañas y formatos digitales, conectando ideas de marca con piezas nativas de cada plataforma.',
        'about_title':'Contenido que entiende <span>cómo se consume.</span>',
        'about':['Su foco está en traducir ideas de marca a contenidos naturales, claros y adaptados al lenguaje de cada plataforma.','En lowsignal participa en creación de piezas, formatos sociales y jornadas de contenido para clientes de distintas industrias.'],
        'expertise':[('01','Content creation','Piezas pensadas para consumo digital.'),('02','Social formats','Reels, stories y formatos nativos.'),('03','Brand voice','Adaptación de tono y mensaje.'),('04','On-camera content','Contenido cercano y orientado a plataforma.')],
        'selected':[('Low Social','Creación de contenido para sistemas editoriales.'),('Campaign content','Piezas para campañas y activaciones.'),('B2B / B2C','Contenido adaptado a distintas audiencias y marcas.')]
    }
}

css = r'''
<style id="team-profile-editorial-v1">
:root{--tp-navy:#070F22;--tp-lav:#8AA4FF;--tp-lav2:#A8B8FF;--tp-text:#F6F8FC;--tp-muted:#9CA8C1;--tp-line:rgba(180,196,230,.16)}
.profile-hero,.focus,.links-section{display:none!important}
.tp-profile,.tp-about,.tp-expertise,.tp-selected{font-family:"Be Vietnam Pro",system-ui,sans-serif}
.tp-shell{width:min(1220px,calc(100% - 128px));margin:0 auto}
.tp-profile{margin-top:-100px;padding:214px 0 86px;background:radial-gradient(720px 480px at 78% 18%,rgba(138,164,255,.08),transparent 68%),var(--tp-navy);color:var(--tp-text)}
.tp-back{display:inline-flex;margin-bottom:42px;color:#8D99B6;font-size:12px;font-weight:500}.tp-back:hover{color:#fff}
.tp-grid{display:grid;grid-template-columns:minmax(360px,.86fr) minmax(0,1.14fr);gap:76px;align-items:center}
.tp-photo-wrap{position:relative;min-height:610px;border-radius:28px;overflow:hidden;background:#0B1220;border:1px solid rgba(255,255,255,.08);box-shadow:0 30px 80px rgba(0,0,0,.28)}
.tp-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top;filter:grayscale(100%) contrast(1.04)}
.tp-photo-wrap:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 58%,rgba(7,15,34,.78) 100%)}
.tp-photo-note{position:absolute;z-index:2;left:22px;bottom:18px;color:#C3CCE0;font-size:10px;letter-spacing:.08em;text-transform:uppercase}
.tp-kicker,.tp-eyebrow{color:var(--tp-lav);font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase}
.tp-copy h1{margin:20px 0 0;font-size:clamp(58px,6.4vw,90px);line-height:1;letter-spacing:-.06em;font-weight:300}.tp-copy h1 span{display:block;color:var(--tp-lav2);font-weight:500}
.tp-positioning{max-width:660px;margin:30px 0 0;color:#E8ECF5;font-size:clamp(21px,2vw,28px);line-height:1.38;letter-spacing:-.025em;font-weight:300}.tp-positioning strong{color:#fff;font-weight:600}
.tp-summary{max-width:610px;margin:22px 0 0;color:var(--tp-muted);font-size:14px;line-height:1.75}
.tp-about{padding:110px 0;background:#F5F7FB;color:#0D1420}.tp-about-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:100px}.tp-about h2,.tp-head h2,.tp-selected h2{margin:18px 0 0;font-size:clamp(40px,4.3vw,58px);line-height:1.05;letter-spacing:-.05em;font-weight:300}.tp-about h2 span,.tp-head h2 span{color:#5E73D8;font-weight:500}.tp-about-copy{padding-top:30px}.tp-about-copy p{margin:0 0 20px;color:#53617A;font-size:15px;line-height:1.8}
.tp-expertise{padding:112px 0 120px;background:var(--tp-navy);color:#fff}.tp-head{max-width:720px}.tp-head h2 span{color:var(--tp-lav2)}.tp-expertise-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:56px}.tp-expertise-grid article{min-height:235px;padding:24px 22px;border-top:1px solid rgba(138,164,255,.32);background:rgba(255,255,255,.025)}.tp-expertise-grid article>span{color:var(--tp-lav);font-size:10px}.tp-expertise-grid h3{margin:44px 0 0;font-size:19px;letter-spacing:-.025em}.tp-expertise-grid p{margin:11px 0 0;color:#9DA9C2;font-size:12px;line-height:1.65}
.tp-selected{padding:106px 0;background:#F5F7FB}.tp-selected-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:90px}.tp-selected-list{border-top:1px solid #D7DFEB}.tp-selected-list>div{display:grid;grid-template-columns:180px 1fr;gap:30px;padding:23px 0;border-bottom:1px solid #D7DFEB}.tp-selected-list b{color:#121A2A;font-size:14px}.tp-selected-list span{color:#647087;font-size:13px;line-height:1.6}
@media(max-width:1050px){.tp-shell{width:calc(100% - 64px)}.tp-grid{grid-template-columns:.9fr 1.1fr;gap:48px}.tp-photo-wrap{min-height:540px}.tp-about-grid,.tp-selected-grid{gap:58px}.tp-expertise-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.tp-shell{width:calc(100% - 40px)}.tp-profile{padding:172px 0 62px}.tp-back{display:none}.tp-grid{grid-template-columns:1fr;gap:34px}.tp-photo-wrap{min-height:480px;border-radius:20px}.tp-copy h1{font-size:58px}.tp-positioning{font-size:21px}.tp-about,.tp-expertise,.tp-selected{padding:76px 0}.tp-about-grid,.tp-selected-grid{grid-template-columns:1fr;gap:32px}.tp-about-copy{padding-top:0}.tp-about h2,.tp-head h2,.tp-selected h2{font-size:39px}.tp-expertise-grid{grid-template-columns:1fr;gap:12px}.tp-expertise-grid article{min-height:200px}.tp-selected-list>div{grid-template-columns:1fr;gap:8px}}
</style>
'''

for fname, d in profiles.items():
    p = Path('equipo') / fname
    s = p.read_text(encoding='utf-8')
    # extract current profile photo
    m = re.search(r'<section class="profile-hero">.*?<img src="([^"]+)"[^>]*>', s, re.S)
    if not m:
        raise SystemExit(f'profile/photo not found in {fname}')
    photo = m.group(1)
    parts = d['name'].split(' ',1)
    first, last = parts[0], parts[1] if len(parts)>1 else ''
    exp = ''.join(f'<article><span>{n}</span><h3>{h}</h3><p>{p}</p></article>' for n,h,p in d['expertise'])
    sel = ''.join(f'<div><b>{h}</b><span>{p}</span></div>' for h,p in d['selected'])
    paras = ''.join(f'<p>{x}</p>' for x in d['about'])
    new = f'''
<section class="tp-profile">
  <div class="tp-shell">
    <a class="tp-back" href="/nosotros">← Volver al equipo</a>
    <div class="tp-grid">
      <div class="tp-photo-wrap"><img class="tp-photo" src="{photo}" alt="{d['name']}"><div class="tp-photo-note">Santiago, Chile · lowsignal</div></div>
      <div class="tp-copy">
        <div class="tp-kicker">{d['kicker']}</div>
        <h1>{first}<span>{last}</span></h1>
        <p class="tp-positioning">{d['positioning']}</p>
        <p class="tp-summary">{d['summary']}</p>
      </div>
    </div>
  </div>
</section>
<section class="tp-about"><div class="tp-shell tp-about-grid"><div><div class="tp-eyebrow">ENFOQUE</div><h2>{d['about_title']}</h2></div><div class="tp-about-copy">{paras}</div></div></section>
<section class="tp-expertise"><div class="tp-shell"><div class="tp-head"><div class="tp-eyebrow">EXPERTISE</div><h2>Capacidades que conectan <span>idea y ejecución.</span></h2></div><div class="tp-expertise-grid">{exp}</div></div></section>
<section class="tp-selected"><div class="tp-shell tp-selected-grid"><div><div class="tp-eyebrow">EN LOWSIGNAL</div><h2>Donde aporta <span>más valor.</span></h2></div><div class="tp-selected-list">{sel}</div></div></section>
'''
    s2, n = re.subn(r'\s*<section class="profile-hero">.*?</section>', '\n'+new, s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'profile section not replaced in {fname}')
    if 'team-profile-editorial-v1' not in s2:
        s2 = s2.replace('</head>', css+'\n</head>',1)
    p.write_text(s2, encoding='utf-8')
    print('updated', fname)
