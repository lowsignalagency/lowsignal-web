from pathlib import Path
import re

STYLE_ID = 'case-editorial-layout-v1'
SCRIPT_ID = 'case-editorial-scrollspy-v1'

style = r'''
<style id="case-editorial-layout-v1">
.case-editorial{background:#F6F7FA;padding:118px 0 124px;color:#071022}
.case-editorial-grid{display:grid;grid-template-columns:290px minmax(0,1fr);gap:88px;align-items:start}
.case-editorial-aside{position:sticky;top:120px;align-self:start;padding-right:28px}
.case-editorial-client{padding-bottom:28px;border-bottom:1px solid #DDE3EC}
.case-editorial-client img{display:block;max-width:180px;max-height:64px;object-fit:contain;object-position:left center;margin-bottom:22px}
.case-editorial-client h3{margin:0;font-size:18px;line-height:1.35;letter-spacing:-.025em;font-weight:600;color:#0C1630}
.case-editorial-meta{display:grid;gap:24px;padding:28px 0;border-bottom:1px solid #DDE3EC}
.case-editorial-meta span,.case-editorial-nav-label{display:block;margin-bottom:7px;color:#8B96AA;font-size:9px;line-height:1;letter-spacing:.16em;font-weight:700;text-transform:uppercase}
.case-editorial-meta p{margin:0;color:#4F5C74;font-size:13px;line-height:1.65}
.case-editorial-nav{padding-top:28px}
.case-editorial-nav-label{margin-bottom:14px}
.case-editorial-nav a{position:relative;display:flex;align-items:center;min-height:34px;padding-left:18px;color:#8A94A7;font-size:12px;font-weight:500;transition:color .22s ease,transform .22s ease}
.case-editorial-nav a:before{content:"";position:absolute;left:0;top:50%;width:5px;height:5px;border-radius:50%;background:#CAD1DE;transform:translateY(-50%);transition:background .22s ease,transform .22s ease}
.case-editorial-nav a:hover{color:#1419E0;transform:translateX(2px)}
.case-editorial-nav a.is-active{color:#1419E0;font-weight:650}
.case-editorial-nav a.is-active:before{background:#1419E0;transform:translateY(-50%) scale(1.45)}
.case-editorial-content{min-width:0}
.case-editorial-block{scroll-margin-top:118px;padding:0 0 96px;margin:0 0 96px;border-bottom:1px solid #DDE3EC}
.case-editorial-block:last-child{margin-bottom:0;padding-bottom:0;border-bottom:0}
.case-editorial-eyebrow{margin:0 0 18px;color:#1419E0;font-size:10px;letter-spacing:.18em;font-weight:700;text-transform:uppercase}
.case-editorial-block h2{max-width:900px;margin:0;font-size:clamp(42px,4.35vw,62px);line-height:1.03;letter-spacing:-.052em;font-weight:300;color:#081226}
.case-editorial-block h2 strong{color:#1419E0;font-weight:400}
.case-editorial-lead{max-width:820px;margin:28px 0 0;color:#59667D;font-size:17px;line-height:1.82}
.case-editorial-number{display:flex;align-items:center;gap:12px;margin-bottom:20px;color:#1419E0;font-size:11px;font-weight:700;letter-spacing:.08em}
.case-editorial-number:after{content:"";width:48px;height:1px;background:#C9D1E0}
.case-editorial-block h3{max-width:820px;margin:0;font-size:clamp(30px,3vw,44px);line-height:1.08;letter-spacing:-.045em;font-weight:400;color:#0A1428}
.case-editorial-copy{max-width:760px;margin:22px 0 0;color:#647086;font-size:15px;line-height:1.8}
.case-editorial-media{margin:44px 0 0;border-radius:20px;overflow:hidden;background:#E9EDF5;box-shadow:0 22px 54px rgba(7,15,34,.08)}
.case-editorial-media img{display:block;width:100%;height:min(54vw,640px);object-fit:cover}
.case-editorial-pair{display:grid;grid-template-columns:1.18fr .82fr;gap:16px;margin-top:44px}
.case-editorial-pair figure{margin:0;border-radius:18px;overflow:hidden;background:#E9EDF5;box-shadow:0 18px 42px rgba(7,15,34,.07)}
.case-editorial-pair img{display:block;width:100%;height:420px;object-fit:cover}
.case-editorial-pair figure:nth-child(2) img{height:100%}
.case-editorial-callout{margin-top:18px;padding:28px 30px;border-radius:18px;background:#071022;color:#fff}
.case-editorial-callout span{display:block;color:#8EA3FF;font-size:9px;letter-spacing:.16em;font-weight:700;text-transform:uppercase}
.case-editorial-callout h4{margin:12px 0 0;font-size:26px;line-height:1.18;letter-spacing:-.035em;font-weight:400}
.case-editorial-callout p{margin:12px 0 0;color:#AEB8CB;font-size:13px;line-height:1.75}
.case-editorial-result{padding:44px;border-radius:22px;background:#fff;box-shadow:0 20px 52px rgba(7,15,34,.06)}
.case-editorial-result h3{font-size:clamp(34px,3.45vw,50px)}
.case-editorial-result p{max-width:760px}
.case-editorial-reveal{opacity:0;transform:translateY(24px);transition:opacity .72s cubic-bezier(.2,.7,.2,1),transform .72s cubic-bezier(.2,.7,.2,1)}
.case-editorial-reveal.is-visible{opacity:1;transform:none}
@media(max-width:1000px){
 .case-editorial{padding:92px 0 104px}
 .case-editorial-grid{grid-template-columns:230px minmax(0,1fr);gap:48px}
 .case-editorial-aside{top:104px;padding-right:12px}
 .case-editorial-pair{grid-template-columns:1fr}
 .case-editorial-pair img,.case-editorial-pair figure:nth-child(2) img{height:360px}
}
@media(max-width:760px){
 .case-editorial{padding:68px 0 78px}
 .case-editorial-grid{grid-template-columns:1fr;gap:48px}
 .case-editorial-aside{position:relative;top:auto;padding:0}
 .case-editorial-client{display:grid;grid-template-columns:120px 1fr;gap:18px;align-items:center}
 .case-editorial-client img{max-width:120px;max-height:50px;margin:0}
 .case-editorial-meta{grid-template-columns:1fr 1fr;gap:18px}
 .case-editorial-nav{display:flex;gap:8px;overflow-x:auto;padding:22px 0 4px;scrollbar-width:none}
 .case-editorial-nav::-webkit-scrollbar{display:none}
 .case-editorial-nav-label{display:none}
 .case-editorial-nav a{flex:0 0 auto;min-height:34px;padding:0 13px;border:1px solid #DDE3EC;border-radius:999px;background:#fff}
 .case-editorial-nav a:before{display:none}
 .case-editorial-nav a.is-active{color:#fff;background:#1419E0;border-color:#1419E0}
 .case-editorial-block{scroll-margin-top:92px;padding-bottom:68px;margin-bottom:68px}
 .case-editorial-block h2{font-size:36px}
 .case-editorial-lead{font-size:15px;line-height:1.72}
 .case-editorial-block h3{font-size:29px}
 .case-editorial-media{margin-top:30px;border-radius:16px}
 .case-editorial-media img{height:330px}
 .case-editorial-pair{margin-top:30px;gap:12px}
 .case-editorial-pair img,.case-editorial-pair figure:nth-child(2) img{height:280px}
 .case-editorial-callout{padding:24px}
 .case-editorial-result{padding:28px 24px}
}
@media(prefers-reduced-motion:reduce){.case-editorial-reveal{opacity:1!important;transform:none!important;transition:none!important}}
</style>
'''

script = r'''
<script id="case-editorial-scrollspy-v1">
(() => {
  const root = document.querySelector('.case-editorial');
  if (!root) return;
  const links = [...root.querySelectorAll('.case-editorial-nav a')];
  const sections = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const revealTargets = [...root.querySelectorAll('.case-editorial-block, .case-editorial-result')];
  revealTargets.forEach(el => el.classList.add('case-editorial-reveal'));
  if (reduce || !('IntersectionObserver' in window)) {
    revealTargets.forEach(el => el.classList.add('is-visible'));
  } else {
    const revealObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      });
    }, {threshold:.12, rootMargin:'0px 0px -8% 0px'});
    revealTargets.forEach(el => revealObserver.observe(el));
  }
  if (!sections.length || !('IntersectionObserver' in window)) return;
  const activate = id => links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + id));
  const spy = new IntersectionObserver(entries => {
    const visible = entries.filter(e => e.isIntersecting).sort((a,b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (visible) activate(visible.target.id);
  }, {rootMargin:'-28% 0px -56% 0px', threshold:[0,.15,.35,.6]});
  sections.forEach(section => spy.observe(section));
  if (sections[0]) activate(sections[0].id);
})();
</script>
'''

configs = {
    'casos/rech.html': {
        'client': 'Red Educacional Camilo Henríquez',
        'logo': 'https://lowsignal.cl/assets/rech-logo-full-white-trim.png',
        'objective': 'Ordenar la presencia digital de la red y conectar sus comunidades bajo una experiencia común.',
        'work': 'Web · Social · Contenido',
        'context_title': 'De una red dispersa<br>a una presencia que <strong>se entiende.</strong>',
        'context_copy': 'La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.',
        'context_image': 'https://lowsignal.cl/assets/comunidad-rech.jpg',
        'finding_title': 'Muchas voces, poca lectura de red.',
        'finding_copy': 'Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.',
        'build_title': 'Un sistema común, sin borrar identidades.',
        'build_copy': 'Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.',
        'image1': 'https://lowsignal.cl/assets/reunion-rech.jpg',
        'image2': 'https://lowsignal.cl/assets/comunidad-rech.jpg',
        'callout': 'Una experiencia común sin volver idénticos a sus colegios.',
        'callout_copy': 'El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.',
        'result_title': 'Una presencia más clara, reconocible y <strong>preparada para crecer.</strong>',
        'result_copy': 'El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.'
    },
    'casos/salvador-dali.html': {
        'client': 'Colegio Salvador Dalí',
        'logo': 'https://lowsignal.cl/assets/logo-dali-maipu.png',
        'objective': 'Mostrar la vida del colegio y acompañar a nuevas familias desde el primer contacto hasta la postulación.',
        'work': 'Social · Paid Media · Web',
        'context_title': 'Un colegio con mucho que mostrar. <strong>Una experiencia digital que debía hacerlo visible.</strong>',
        'context_copy': 'El desafío no era simplemente publicar más. Era traducir la vida cotidiana del colegio en una presencia digital capaz de informar, generar confianza y acompañar a nuevas familias durante su decisión.',
        'context_image': 'https://lowsignal.cl/assets/dali-patio-nueva.jpg',
        'finding_title': 'Mucho valor dentro del colegio, pero poco visible fuera de él.',
        'finding_copy': 'La comunidad vive experiencias, actividades y aprendizajes todos los días, pero sus canales digitales no alcanzaban a transmitir esa riqueza de forma consistente.',
        'build_title': 'Un recorrido conectado entre contenido, campañas y web.',
        'build_copy': 'Ordenamos los puntos de contacto para que redes mostraran la vida del colegio, las campañas acercaran nuevas familias y la web ayudara a profundizar antes de postular.',
        'image1': 'https://lowsignal.cl/assets/dali-ig.jpg',
        'image2': 'https://lowsignal.cl/assets/dali-patio-nueva.jpg',
        'callout': 'Del primer scroll a la postulación.',
        'callout_copy': 'Contenido para descubrir, campañas para llegar a nuevas familias y una experiencia web que ayuda a entender el proyecto educativo antes de tomar una decisión.',
        'result_title': 'Una presencia más cercana, clara y <strong>útil para decidir.</strong>',
        'result_copy': 'El resultado fue una experiencia más coherente entre lo que ocurre dentro del colegio y lo que una familia puede descubrir, entender y sentir desde afuera.'
    }
}

for file_path, c in configs.items():
    p = Path(file_path)
    s = p.read_text(encoding='utf-8')
    s = re.sub(r'\n?<style id="case-editorial-layout-v1">.*?</style>\s*', '\n', s, flags=re.S)
    s = re.sub(r'\n?<script id="case-editorial-scrollspy-v1">.*?</script>\s*', '\n', s, flags=re.S)
    s = s.replace('</head>', style + '\n</head>', 1)

    editorial = f'''
  <section class="case-editorial">
    <div class="container rechx-wrap case-editorial-grid">
      <aside class="case-editorial-aside">
        <div class="case-editorial-client">
          <img src="{c['logo']}" alt="{c['client']}">
          <h3>{c['client']}</h3>
        </div>
        <div class="case-editorial-meta">
          <div><span>OBJETIVO</span><p>{c['objective']}</p></div>
          <div><span>TRABAJO</span><p>{c['work']}</p></div>
        </div>
        <nav class="case-editorial-nav" aria-label="Contenido del caso">
          <div class="case-editorial-nav-label">CONTENIDOS</div>
          <a href="#case-context">Contexto</a>
          <a href="#case-finding">Lo que encontramos</a>
          <a href="#case-build">Lo que construimos</a>
          <a href="#case-result">Resultado</a>
        </nav>
      </aside>

      <div class="case-editorial-content">
        <section class="case-editorial-block" id="case-context">
          <p class="case-editorial-eyebrow">EL CASO</p>
          <h2>{c['context_title']}</h2>
          <p class="case-editorial-lead">{c['context_copy']}</p>
          <figure class="case-editorial-media"><img src="{c['context_image']}" alt="{c['client']}"></figure>
        </section>

        <section class="case-editorial-block" id="case-finding">
          <div class="case-editorial-number">01</div>
          <h3>{c['finding_title']}</h3>
          <p class="case-editorial-copy">{c['finding_copy']}</p>
        </section>

        <section class="case-editorial-block" id="case-build">
          <div class="case-editorial-number">02</div>
          <h3>{c['build_title']}</h3>
          <p class="case-editorial-copy">{c['build_copy']}</p>
          <div class="case-editorial-pair">
            <figure><img src="{c['image1']}" alt="{c['client']}"></figure>
            <figure><img src="{c['image2']}" alt="{c['client']}"></figure>
          </div>
          <div class="case-editorial-callout"><span>{c['work']}</span><h4>{c['callout']}</h4><p>{c['callout_copy']}</p></div>
        </section>

        <section class="case-editorial-block" id="case-result">
          <div class="case-editorial-number">03</div>
          <div class="case-editorial-result">
            <p class="case-editorial-eyebrow">LA TRANSFORMACIÓN</p>
            <h3>{c['result_title']}</h3>
            <p class="case-editorial-copy">{c['result_copy']}</p>
          </div>
        </section>
      </div>
    </div>
  </section>
'''

    pattern = r'\n\s*<section class="rechx-intro">.*?<section class="rechx-outcome">.*?</section>\s*'
    new_s, n = re.subn(pattern, '\n' + editorial + '\n', s, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError(f'Could not replace central case sections in {file_path}')
    new_s = new_s.replace('</body>', script + '\n</body>', 1)
    p.write_text(new_s, encoding='utf-8')
