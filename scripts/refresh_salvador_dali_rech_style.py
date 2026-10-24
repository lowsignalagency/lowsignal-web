from pathlib import Path
import re

p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

# Remove prior CSD rebuild style/script if rerun.
s = re.sub(r'\n?<style id="csd-rech-style-v1">.*?</style>\s*', '\n', s, flags=re.S)
s = re.sub(r'\n?<script id="csd-rech-reveal-v1">.*?</script>\s*', '\n', s, flags=re.S)

style = r'''
<style id="csd-rech-style-v1">
.csdx{background:#fff;color:#071022}.csdx-wrap{width:min(1220px,calc(100% - 128px))!important;max-width:1220px!important;margin-inline:auto!important}.csdx-hero{padding:158px 0 0;background:#070F22;color:#fff}.csdx-hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:72px;align-items:end}.csdx-kicker,.csdx-eyebrow{font-size:10px;letter-spacing:.18em;font-weight:700;color:#8EA3FF}.csdx-kicker span{opacity:.55;margin:0 7px}.csdx-hero h1{max-width:900px;margin:18px 0 0;font-size:clamp(54px,5.1vw,74px);line-height:1.01;letter-spacing:-.058em;font-weight:300}.csdx-hero h1 strong{color:#A9B5FF;font-weight:400}.csdx-hero-copy>p{max-width:760px;margin:28px 0 0;color:#C2CAE0;font-size:17px;line-height:1.72}.csdx-meta{display:grid;grid-template-columns:1fr 1fr;gap:28px;max-width:760px;margin-top:34px;padding-top:18px;border-top:1px solid rgba(255,255,255,.16)}.csdx-meta span,.csdx-logo-card span{display:block;color:#8EA3FF;font-size:9px;letter-spacing:.14em;font-weight:700}.csdx-meta b{display:block;margin-top:7px;color:#fff;font-size:13px;font-weight:500}.csdx-logo-card{min-height:214px;padding:28px;border:1px solid rgba(255,255,255,.11);border-radius:18px;background:#101A31;display:flex;flex-direction:column;justify-content:space-between}.csdx-logo-card img{width:auto;max-width:220px;max-height:76px;object-fit:contain;object-position:left center}.csdx-logo-card p{margin:20px 0 0;color:#AEB8CE;font-size:13px;line-height:1.7}.csdx-cover{margin:54px 0 -92px;height:min(50vw,650px);border-radius:18px;overflow:hidden;box-shadow:0 28px 70px rgba(0,0,0,.28)}.csdx-cover img{width:100%;height:100%;object-fit:cover;object-position:center 42%;transition:transform .65s cubic-bezier(.2,.7,.2,1)}
.csdx-intro{padding:178px 0 92px;background:#fff}.csdx-intro-grid{display:grid;grid-template-columns:1fr .7fr;gap:82px;align-items:end}.csdx-intro h2,.csdx-work h2,.csdx-outcome h2{margin:16px 0 0;font-size:clamp(42px,4.2vw,58px);line-height:1.04;letter-spacing:-.052em;font-weight:300}.csdx-intro h2 strong,.csdx-outcome h2 strong{color:#1419E0;font-weight:400}.csdx-intro-grid>p,.csdx-work-head>p,.csdx-outcome-grid>p{margin:0;color:#66728B;font-size:15px;line-height:1.8}
.csdx-story{padding:0 0 112px;background:#fff}.csdx-row{display:grid;grid-template-columns:72px 190px 1fr;gap:28px;padding:30px 0;border-top:1px solid #DEE4EE}.csdx-row:last-child{border-bottom:1px solid #DEE4EE}.csdx-num{color:#1419E0;font-size:12px;font-weight:700}.csdx-label{color:#8A94A8;font-size:9px;letter-spacing:.15em;font-weight:700;padding-top:4px}.csdx-row-copy h3{margin:0;font-size:25px;line-height:1.2;letter-spacing:-.035em;font-weight:500}.csdx-row-copy p{max-width:760px;margin:10px 0 0;color:#68748C;font-size:14px;line-height:1.75}
.csdx-work{padding:110px 0 118px;background:#070F22;color:#fff}.csdx-work .csdx-eyebrow{color:#8EA3FF}.csdx-work h2{color:#fff}.csdx-work h2 strong{color:#A9B5FF;font-weight:400}.csdx-work-head{display:grid;grid-template-columns:1.05fr .68fr;gap:80px;align-items:end}.csdx-work-head>p{color:#AAB4C8}.csdx-gallery{display:grid;grid-template-columns:1.2fr .8fr;grid-template-rows:280px 260px;gap:16px;margin-top:50px}.csdx-gallery figure,.csdx-gallery-copy{margin:0;border-radius:16px;overflow:hidden}.csdx-gallery-main{grid-row:1 / span 2}.csdx-gallery img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.2,.7,.2,1)}.csdx-gallery figure:nth-child(2) img{object-position:center 45%}.csdx-gallery-copy{padding:30px;background:#101A31;border:1px solid rgba(255,255,255,.08);display:flex;flex-direction:column;justify-content:flex-end}.csdx-gallery-copy span{color:#8EA3FF;font-size:9px;letter-spacing:.14em;font-weight:700}.csdx-gallery-copy h3{margin:14px 0 0;font-size:29px;line-height:1.16;letter-spacing:-.04em;font-weight:400}.csdx-gallery-copy p{margin:13px 0 0;color:#AAB4C8;font-size:13px;line-height:1.75}
.csdx-outcome{padding:108px 0;background:#F4F6FB}.csdx-outcome-grid{display:grid;grid-template-columns:.30fr 1.12fr .68fr;gap:52px}.csdx-outcome h2{margin:0}.csdx-outcome-grid>p{margin-top:6px}.csdx-quote{padding:92px 0;background:#1419E0;color:#fff}.csdx-quote-inner{max-width:1080px!important}.csdx-quote-mark{font-size:72px;line-height:.7;color:rgba(255,255,255,.45)}.csdx-quote blockquote{max-width:930px;margin:18px 0 30px;font-size:clamp(30px,3vw,42px);line-height:1.22;letter-spacing:-.04em;font-weight:300}.csdx-person{display:flex;align-items:center;gap:14px}.csdx-person img{width:56px;height:56px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.45)}.csdx-person b{display:block;font-size:14px}.csdx-person span{display:block;margin-top:4px;color:#D6DEFF;font-size:11px}
.csdx-next{padding:92px 0 106px;background:#fff}.csdx-next-head{display:flex;justify-content:space-between;align-items:end;gap:40px;margin-bottom:30px}.csdx-next-head h2{margin:12px 0 0;font-size:38px;line-height:1.08;letter-spacing:-.045em;font-weight:300}.csdx-next-head a{color:#1419E0;font-size:13px;font-weight:600;transition:transform .2s ease,color .2s ease}.csdx-next-card{position:relative;display:block;height:470px;border-radius:18px;overflow:hidden;box-shadow:0 14px 36px rgba(7,15,34,.08);transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s ease}.csdx-next-card img{width:100%;height:100%;object-fit:cover;transition:transform .65s cubic-bezier(.2,.7,.2,1),filter .45s ease}.csdx-next-overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,15,34,.02) 20%,rgba(7,15,34,.82) 100%);transition:background .4s ease}.csdx-next-copy{position:absolute;left:34px;right:34px;bottom:32px;color:#fff;transition:transform .35s cubic-bezier(.2,.7,.2,1)}.csdx-next-copy span{font-size:9px;letter-spacing:.14em;font-weight:700;color:#CBD4F7}.csdx-next-copy h3{margin:8px 0 10px;font-size:34px;letter-spacing:-.04em}.csdx-next-copy b{display:inline-block;font-size:12px;transition:transform .3s ease}
@media(hover:hover){.csdx-cover:hover img,.csdx-gallery figure:hover img{transform:scale(1.02)}.csdx-next-head>a:hover{transform:translateX(4px);color:#0D13B9}.csdx-next-card:hover{transform:translateY(-6px);box-shadow:0 28px 64px rgba(7,15,34,.18)}.csdx-next-card:hover img{transform:scale(1.035)}.csdx-next-card:hover .csdx-next-copy{transform:translateY(-5px)}.csdx-next-card:hover .csdx-next-copy b{transform:translateX(5px)}}
.csdx-reveal{opacity:0;transform:translateY(28px);transition:opacity .68s ease,transform .78s cubic-bezier(.2,.75,.2,1)}.csdx-reveal.is-visible{opacity:1;transform:translateY(0)}
@media(max-width:1000px){.csdx-wrap{width:calc(100% - 48px)!important}.csdx-hero-grid,.csdx-intro-grid,.csdx-work-head,.csdx-outcome-grid{grid-template-columns:1fr;gap:34px}.csdx-logo-card{max-width:440px}.csdx-row{grid-template-columns:54px 150px 1fr}.csdx-gallery{grid-template-columns:1fr;grid-template-rows:420px 300px 240px}.csdx-gallery-main{grid-row:auto}.csdx-outcome-grid{gap:22px}}
@media(max-width:760px){.csdx-wrap{width:calc(100% - 24px)!important}.csdx-hero{padding-top:134px}.csdx-hero h1{font-size:42px}.csdx-hero-copy>p{font-size:15px}.csdx-meta{grid-template-columns:1fr}.csdx-cover{height:330px;margin:38px 0 -56px;border-radius:15px}.csdx-intro{padding:118px 0 68px}.csdx-intro h2,.csdx-work h2,.csdx-outcome h2{font-size:34px}.csdx-story{padding-bottom:72px}.csdx-row{grid-template-columns:42px 1fr;gap:14px;padding:24px 0}.csdx-label{grid-column:2}.csdx-row-copy{grid-column:2}.csdx-row-copy h3{font-size:21px}.csdx-work{padding:76px 0 82px}.csdx-gallery{grid-template-rows:310px 260px 220px;margin-top:34px}.csdx-gallery-copy{padding:24px}.csdx-gallery-copy h3{font-size:25px}.csdx-outcome{padding:72px 0}.csdx-quote{padding:72px 0}.csdx-quote blockquote{font-size:28px}.csdx-next{padding:70px 0 82px}.csdx-next-head{flex-direction:column;align-items:flex-start}.csdx-next-card{height:350px}.csdx-next-copy{left:22px;right:22px;bottom:22px}.csdx-next-copy h3{font-size:28px}}
@media(prefers-reduced-motion:reduce){.csdx-reveal{opacity:1!important;transform:none!important;transition:none!important}}
</style>
'''

main = r'''
<main id="top" class="csdx">
  <section class="csdx-hero">
    <div class="container csdx-wrap">
      <div class="csdx-hero-grid">
        <div class="csdx-hero-copy">
          <div class="csdx-kicker">CUSTOMER STORY <span>·</span> EDUCACIÓN</div>
          <h1>La vida del colegio.<br><strong>Más cerca de las familias.</strong></h1>
          <p>Conectamos redes, campañas y web para mostrar la experiencia del Colegio Salvador Dalí y acompañar a nuevas familias desde el primer contacto hasta la postulación.</p>
          <div class="csdx-meta">
            <div><span>CLIENTE</span><b>Colegio Salvador Dalí</b></div>
            <div><span>TRABAJO</span><b>Social · Paid Media · Web</b></div>
          </div>
        </div>
        <div class="csdx-logo-card">
          <img src="https://lowsignal.cl/assets/logo-dali-darkbg.png" alt="Colegio Salvador Dalí">
          <p>Una presencia digital conectada para mostrar lo que se vive dentro del colegio y acompañar a las familias durante la admisión.</p>
        </div>
      </div>
      <figure class="csdx-cover"><img src="https://lowsignal.cl/assets/dali-patio-nueva.jpg" alt="Colegio Salvador Dalí"></figure>
    </div>
  </section>

  <section class="csdx-intro">
    <div class="container csdx-wrap csdx-intro-grid">
      <div><div class="csdx-eyebrow">EL CASO</div><h2>Un colegio con mucho que mostrar.<br><strong>Una experiencia digital que debía hacerlo visible.</strong></h2></div>
      <p>El desafío no era simplemente publicar más. Era traducir la vida cotidiana del colegio en una presencia digital capaz de informar, generar confianza y acompañar a nuevas familias durante su decisión.</p>
    </div>
  </section>

  <section class="csdx-story">
    <div class="container csdx-wrap">
      <div class="csdx-row"><div class="csdx-num">01</div><div class="csdx-label">LO QUE ENCONTRAMOS</div><div class="csdx-row-copy"><h3>Mucho valor dentro del colegio, pero poco visible fuera de él.</h3><p>La comunidad vivía experiencias, actividades y aprendizajes todos los días, pero sus canales digitales no alcanzaban a transmitir esa riqueza de forma consistente.</p></div></div>
      <div class="csdx-row"><div class="csdx-num">02</div><div class="csdx-label">LO QUE CONSTRUIMOS</div><div class="csdx-row-copy"><h3>Un recorrido conectado entre contenido, campañas y web.</h3><p>Ordenamos los puntos de contacto para que redes mostraran la vida del colegio, las campañas acercaran nuevas familias y la web ayudara a profundizar antes de postular.</p></div></div>
      <div class="csdx-row"><div class="csdx-num">03</div><div class="csdx-label">LO QUE CAMBIÓ</div><div class="csdx-row-copy"><h3>Una presencia más cercana, clara y útil para decidir.</h3><p>El colegio pasó a tener una experiencia digital más coherente, capaz de conectar su día a día con el proceso de admisión y la relación con su comunidad.</p></div></div>
    </div>
  </section>

  <section class="csdx-work">
    <div class="container csdx-wrap">
      <div class="csdx-work-head">
        <div><div class="csdx-eyebrow">EL TRABAJO</div><h2>No mostramos una institución.<br><strong>Mostramos cómo se vive dentro.</strong></h2></div>
        <p>La lógica fue simple: cada canal debía cumplir un rol distinto, pero todos tenían que contar la misma historia del colegio y acompañar a las familias en una experiencia continua.</p>
      </div>
      <div class="csdx-gallery">
        <figure class="csdx-gallery-main"><img src="https://lowsignal.cl/assets/csd_visita.jpg" alt="Comunidad Colegio Salvador Dalí"></figure>
        <figure><img src="https://lowsignal.cl/assets/dali-ig.jpg" alt="Contenido digital Colegio Salvador Dalí"></figure>
        <div class="csdx-gallery-copy"><span>SOCIAL · PAID MEDIA · WEB</span><h3>Del primer scroll a la postulación.</h3><p>Contenido para descubrir, campañas para llegar a nuevas familias y una experiencia web que ayuda a entender el proyecto educativo antes de tomar una decisión.</p></div>
      </div>
    </div>
  </section>

  <section class="csdx-outcome">
    <div class="container csdx-wrap csdx-outcome-grid">
      <div class="csdx-eyebrow">LA TRANSFORMACIÓN</div>
      <h2>Más que presencia digital: <strong>una forma más cercana de mostrar el colegio y acompañar a sus familias.</strong></h2>
      <p>El resultado fue una experiencia más coherente entre lo que ocurre dentro del colegio y lo que una familia puede descubrir, entender y sentir desde afuera.</p>
    </div>
  </section>

  <section class="csdx-quote">
    <div class="container csdx-wrap csdx-quote-inner">
      <div class="csdx-quote-mark">“</div>
      <blockquote>Con lowsignal fortalecimos nuestras redes, nos acercamos a la comunidad y potenciamos las habilidades de nuestros estudiantes.</blockquote>
      <div class="csdx-person"><img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal"><div><b>Karina Ravanal</b><span>Directora, Colegio Salvador Dalí</span></div></div>
    </div>
  </section>

  <section class="csdx-next">
    <div class="container csdx-wrap">
      <div class="csdx-next-head"><div><div class="csdx-eyebrow">SIGUIENTE CASO</div><h2>Más trabajo.<br>Menos promesas.</h2></div><a href="https://lowsignal.cl/casos">Ver todos los casos</a></div>
      <a class="csdx-next-card" href="https://lowsignal.cl/casos/fcct"><img src="https://lowsignal.cl/assets/lanzamiento-web_fcct.jpg" alt="Fundación Crecer con Todos"><div class="csdx-next-overlay"></div><div class="csdx-next-copy"><span>EDUCACIÓN · CUSTOMER STORY</span><h3>Fundación Crecer con Todos</h3><b>Ver caso ↗</b></div></a>
    </div>
  </section>

  <section class="lsr-band"><div class="lsr-wrap lsr-band-inner"><p>¿Construimos lo que viene?</p><a href="https://calendly.com/felipe-lowsignal/30min" target="_blank" rel="noopener noreferrer">Hablemos</a></div></section>
</main>
'''

s = re.sub(r'<main id="top".*?</main>', main, s, count=1, flags=re.S)
s = s.replace('</head>', style + '\n</head>', 1)

script = r'''
<script id="csd-rech-reveal-v1">
document.addEventListener('DOMContentLoaded',()=>{
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  const selectors=['.csdx-hero-grid','.csdx-cover','.csdx-intro-grid','.csdx-row','.csdx-work-head','.csdx-gallery','.csdx-outcome-grid','.csdx-quote-inner','.csdx-next-head','.csdx-next-card'];
  const els=[...new Set(selectors.flatMap(s=>[...document.querySelectorAll(s)]))];
  els.forEach(el=>el.classList.add('csdx-reveal'));
  const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');io.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -8% 0px'});
  els.forEach(el=>io.observe(el));
});
</script>
'''
s = s.replace('</body>', script + '\n</body>', 1)

p.write_text(s, encoding='utf-8')
