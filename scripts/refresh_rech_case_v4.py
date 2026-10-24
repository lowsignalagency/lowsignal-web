from pathlib import Path
import re

p = Path('casos/rech.html')
s = p.read_text(encoding='utf-8')

main = r'''<main id="top" class="rechx">
  <section class="rechx-hero">
    <div class="container rechx-wrap">
      <a class="rechx-back" href="https://lowsignal.cl/casos">← Customer Stories</a>
      <div class="rechx-hero-grid">
        <div class="rechx-hero-copy">
          <div class="rechx-kicker">CUSTOMER STORY <span>·</span> EDUCACIÓN</div>
          <h1>Una red. Muchas comunidades.<br><strong>Una experiencia digital que las conecta.</strong></h1>
          <p>Ayudamos a la Red Educacional Camilo Henríquez a ordenar su presencia digital, conectar sus colegios y convertir una identidad compartida en una experiencia clara para familias, estudiantes y comunidades.</p>
          <div class="rechx-meta">
            <div><span>CLIENTE</span><b>Red Educacional Camilo Henríquez</b></div>
            <div><span>TRABAJO</span><b>Web · Social · Contenido</b></div>
          </div>
        </div>
        <div class="rechx-logo-card">
          <img src="https://lowsignal.cl/assets/rech-logo-full-white-trim.png" alt="Red Educacional Camilo Henríquez">
          <p>Una identidad común para conectar colegios, familias y comunidades sin perder la voz propia de cada establecimiento.</p>
        </div>
      </div>
      <figure class="rechx-cover"><img src="https://lowsignal.cl/assets/comunidad-rech.jpg" alt="Comunidad Red Educacional Camilo Henríquez"></figure>
    </div>
  </section>

  <section class="rechx-intro">
    <div class="container rechx-wrap rechx-intro-grid">
      <div>
        <div class="rechx-eyebrow">EL CASO</div>
        <h2>De una red dispersa<br>a una presencia que <strong>se entiende.</strong></h2>
      </div>
      <p>La RECH no necesitaba simplemente verse mejor. Necesitaba una forma común de comunicar la red, dar espacio a cada colegio y hacer más fácil entender quiénes son, qué hacen y cómo se conectan sus comunidades.</p>
    </div>
  </section>

  <section class="rechx-story">
    <div class="container rechx-wrap">
      <div class="rechx-row">
        <div class="rechx-num">01</div>
        <div class="rechx-label">LO QUE ENCONTRAMOS</div>
        <div class="rechx-row-copy"><h3>Muchas voces, poca lectura de red.</h3><p>Múltiples colegios, audiencias y puntos de contacto convivían sin una experiencia digital que hiciera visible la escala de la red con claridad.</p></div>
      </div>
      <div class="rechx-row">
        <div class="rechx-num">02</div>
        <div class="rechx-label">LO QUE CONSTRUIMOS</div>
        <div class="rechx-row-copy"><h3>Un sistema común, sin borrar identidades.</h3><p>Conectamos arquitectura web, lenguaje visual y contenido para que la RECH se viera coherente como red, manteniendo espacio para la personalidad de cada comunidad.</p></div>
      </div>
      <div class="rechx-row">
        <div class="rechx-num">03</div>
        <div class="rechx-label">LO QUE CAMBIÓ</div>
        <div class="rechx-row-copy"><h3>Una presencia más clara, reconocible y preparada para crecer.</h3><p>La red dejó de comunicar piezas aisladas y pasó a tener una experiencia más ordenada para familias, estudiantes y comunidades.</p></div>
      </div>
    </div>
  </section>

  <section class="rechx-work">
    <div class="container rechx-wrap">
      <div class="rechx-work-head">
        <div><div class="rechx-eyebrow rechx-eyebrow-dark">EL TRABAJO</div><h2>No hicimos una página.<br><strong>Construimos una forma de presentar la red.</strong></h2></div>
        <p>Cada pieza tenía que cumplir un rol: explicar la RECH, representar a sus colegios, ordenar la información y hacer visible la vida que ocurre dentro de sus comunidades.</p>
      </div>
      <div class="rechx-gallery">
        <figure class="rechx-gallery-main"><img src="https://lowsignal.cl/assets/reunion-rech.jpg" alt="Reunión de la Red Educacional Camilo Henríquez"></figure>
        <figure><img src="https://lowsignal.cl/assets/comunidad-rech.jpg" alt="Comunidad Red Educacional Camilo Henríquez"></figure>
        <div class="rechx-gallery-copy"><span>WEB · SOCIAL · CONTENIDO</span><h3>Una experiencia común sin volver idénticos a sus colegios.</h3><p>El sistema digital organiza la red, hace más clara su propuesta y permite que cada comunidad tenga voz dentro de una misma experiencia.</p></div>
      </div>
    </div>
  </section>

  <section class="rechx-outcome">
    <div class="container rechx-wrap rechx-outcome-grid">
      <div class="rechx-eyebrow">LA TRANSFORMACIÓN</div>
      <h2>Más que una nueva presencia digital: <strong>una red más fácil de entender, recorrer y reconocer.</strong></h2>
      <p>El resultado no fue una colección de piezas nuevas. Fue una forma más coherente de presentar la RECH y de conectar el trabajo de sus colegios bajo una misma experiencia.</p>
    </div>
  </section>

  <section class="rechx-quote">
    <div class="container rechx-wrap rechx-quote-inner">
      <div class="rechx-quote-mark">“</div>
      <blockquote>lowsignal se ha convertido en un aliado estratégico para nuestra red. Entendieron nuestra visión y se involucraron de verdad en el proyecto.</blockquote>
      <div class="rechx-person"><img src="https://lowsignal.cl/assets/nicolas-munoz.jpg" alt="Nicolás Muñoz"><div><b>Nicolás Muñoz</b><span>Director Ejecutivo, Red Educacional Camilo Henríquez</span></div></div>
    </div>
  </section>

  <section class="rechx-next">
    <div class="container rechx-wrap">
      <div class="rechx-next-head"><div><div class="rechx-eyebrow">SIGUIENTE CASO</div><h2>Más trabajo.<br>Menos promesas.</h2></div><a href="https://lowsignal.cl/casos">Ver todos los casos</a></div>
      <a class="rechx-next-card" href="https://lowsignal.cl/casos/salvador-dali"><img src="https://lowsignal.cl/assets/dali-patio-nueva.jpg" alt="Colegio Salvador Dalí"><div class="rechx-next-overlay"></div><div class="rechx-next-copy"><span>EDUCACIÓN · CUSTOMER STORY</span><h3>Colegio Salvador Dalí</h3><b>Ver caso ↗</b></div></a>
    </div>
  </section>

  <section class="lsr-band"><div class="lsr-wrap lsr-band-inner"><p>¿Construimos lo que viene?</p><a href="https://calendly.com/felipe-lowsignal/30min" target="_blank" rel="noopener noreferrer">Hablemos</a></div></section>
</main>'''

s, n = re.subn(r'<main id="top".*?</main>', main, s, count=1, flags=re.S)
if n != 1:
    raise RuntimeError('Could not replace RECH main')

css = r'''
<style id="rech-editorial-v5">
.rechx{background:#fff;color:#071022}.rechx-wrap{width:min(1320px,calc(100% - 128px));max-width:1320px}.rechx-hero{padding:160px 0 0;background:#070F22;color:#fff}.rechx-back{display:inline-flex;color:#AAB5CE;font-size:12px;transition:.2s}.rechx-back:hover{color:#fff;transform:translateX(-2px)}.rechx-hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 310px;gap:70px;align-items:center;margin-top:48px}.rechx-kicker,.rechx-eyebrow{font-size:10px;letter-spacing:.18em;font-weight:700;color:#1419E0}.rechx-kicker{color:#AAB5CE}.rechx-kicker span{opacity:.5;margin:0 7px}.rechx-hero h1{max-width:980px;margin:18px 0 0;font-size:clamp(54px,5.5vw,78px);line-height:1.02;letter-spacing:-.06em;font-weight:300}.rechx-hero h1 strong{display:block;color:#A9B5FF;font-weight:500}.rechx-hero-copy>p{max-width:760px;margin:28px 0 0;color:#C4CCDC;font-size:17px;line-height:1.72}.rechx-meta{display:grid;grid-template-columns:1fr 1fr;gap:28px;max-width:760px;margin-top:36px;padding-top:18px;border-top:1px solid rgba(255,255,255,.16)}.rechx-meta span{display:block;color:#7F8BA3;font-size:9px;letter-spacing:.14em;font-weight:700}.rechx-meta b{display:block;margin-top:7px;color:#F4F6FB;font-size:13px;font-weight:500}.rechx-logo-card{padding:28px;border:1px solid rgba(255,255,255,.12);border-radius:18px;background:rgba(255,255,255,.05)}.rechx-logo-card img{height:52px;width:auto;max-width:210px;object-fit:contain}.rechx-logo-card p{margin:22px 0 0;color:#B7C1D4;font-size:12px;line-height:1.7}.rechx-cover{margin:56px 0 -92px;height:min(52vw,670px);border-radius:18px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.28)}.rechx-cover img{width:100%;height:100%;object-fit:cover;object-position:center 42%}
.rechx-intro{padding:182px 0 96px}.rechx-intro-grid{display:grid;grid-template-columns:1.1fr .75fr;gap:90px;align-items:end}.rechx-intro h2,.rechx-work h2,.rechx-outcome h2{margin:16px 0 0;font-size:clamp(42px,4.4vw,60px);line-height:1.04;letter-spacing:-.055em;font-weight:300}.rechx-intro h2 strong,.rechx-work h2 strong,.rechx-outcome h2 strong{color:#1419E0;font-weight:400}.rechx-intro-grid>p,.rechx-work-head>p,.rechx-outcome-grid>p{margin:0;color:#65718B;font-size:15px;line-height:1.8}
.rechx-story{padding:0 0 110px}.rechx-row{display:grid;grid-template-columns:80px 220px 1fr;gap:34px;align-items:start;padding:34px 0;border-top:1px solid #E2E7F0}.rechx-row:last-child{border-bottom:1px solid #E2E7F0}.rechx-num{color:#1419E0;font-size:12px;font-weight:700}.rechx-label{color:#7A869E;font-size:9px;letter-spacing:.16em;font-weight:700}.rechx-row-copy{display:grid;grid-template-columns:.78fr 1fr;gap:56px}.rechx-row-copy h3{margin:0;color:#101936;font-size:26px;line-height:1.25;letter-spacing:-.035em;font-weight:500}.rechx-row-copy p{margin:0;color:#66728A;font-size:14px;line-height:1.8}
.rechx-work{padding:112px 0 122px;background:#070F22;color:#fff}.rechx-eyebrow-dark{color:#8EA3FF}.rechx-work h2{color:#fff}.rechx-work h2 strong{color:#A9B5FF}.rechx-work-head{display:grid;grid-template-columns:1.05fr .68fr;gap:82px;align-items:end}.rechx-work-head>p{color:#AAB5CE}.rechx-gallery{display:grid;grid-template-columns:1.2fr .8fr;grid-template-rows:360px 250px;gap:14px;margin-top:52px}.rechx-gallery figure,.rechx-gallery-copy{margin:0;border-radius:16px;overflow:hidden}.rechx-gallery-main{grid-row:1/3}.rechx-gallery img{width:100%;height:100%;object-fit:cover}.rechx-gallery-copy{padding:30px;background:#101A31;border:1px solid rgba(255,255,255,.10);display:flex;flex-direction:column;justify-content:center}.rechx-gallery-copy span{color:#899EFF;font-size:9px;letter-spacing:.14em;font-weight:700}.rechx-gallery-copy h3{margin:16px 0 0;color:#fff;font-size:30px;line-height:1.18;letter-spacing:-.04em;font-weight:400}.rechx-gallery-copy p{margin:14px 0 0;color:#AAB5CE;font-size:12px;line-height:1.72}
.rechx-outcome{padding:110px 0;background:#F4F6FB}.rechx-outcome-grid{display:grid;grid-template-columns:.32fr 1.15fr .72fr;gap:56px;align-items:start}.rechx-outcome .rechx-eyebrow{margin-top:10px}.rechx-outcome h2{margin:0}.rechx-outcome-grid>p{margin-top:7px}
.rechx-quote{padding:96px 0;background:#1419E0;color:#fff}.rechx-quote-inner{max-width:1080px!important}.rechx-quote-mark{font-size:72px;line-height:.7;color:rgba(255,255,255,.45)}.rechx-quote blockquote{max-width:920px;margin:18px 0 30px;font-size:clamp(30px,3.2vw,44px);line-height:1.22;letter-spacing:-.04em;font-weight:300}.rechx-person{display:flex;align-items:center;gap:14px}.rechx-person img{width:56px;height:56px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.5)}.rechx-person b{display:block;font-size:14px}.rechx-person span{display:block;margin-top:4px;color:#D6DEFF;font-size:11px}
.rechx-next{padding:96px 0 110px}.rechx-next-head{display:flex;justify-content:space-between;gap:40px;align-items:end}.rechx-next-head h2{margin:12px 0 0;font-size:38px;line-height:1.08;letter-spacing:-.045em;font-weight:300}.rechx-next-head a{color:#1419E0;font-size:13px;font-weight:600}.rechx-next-card{position:relative;display:block;height:460px;margin-top:34px;border-radius:18px;overflow:hidden}.rechx-next-card img{width:100%;height:100%;object-fit:cover}.rechx-next-overlay{position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,rgba(7,15,34,.82) 100%)}.rechx-next-copy{position:absolute;left:34px;right:34px;bottom:30px;color:#fff}.rechx-next-copy span{font-size:9px;letter-spacing:.14em;font-weight:700;color:#D3DAEA}.rechx-next-copy h3{margin:10px 0 8px;font-size:36px;line-height:1.1;letter-spacing:-.04em;font-weight:400}.rechx-next-copy b{font-size:12px}
@media(max-width:1000px){.rechx-wrap{width:calc(100% - 56px)}.rechx-hero-grid,.rechx-intro-grid,.rechx-work-head,.rechx-outcome-grid{grid-template-columns:1fr;gap:34px}.rechx-logo-card{max-width:420px}.rechx-row{grid-template-columns:60px 180px 1fr}.rechx-row-copy{grid-template-columns:1fr;gap:14px}.rechx-gallery{grid-template-columns:1fr 1fr;grid-template-rows:430px 250px}.rechx-gallery-main{grid-column:1/3;grid-row:auto}.rechx-outcome-grid{gap:22px}}
@media(max-width:760px){.rechx-wrap{width:calc(100% - 40px)}.rechx-hero{padding-top:136px}.rechx-hero h1{font-size:43px}.rechx-hero-copy>p{font-size:15px}.rechx-meta{grid-template-columns:1fr}.rechx-cover{height:330px;margin:38px 0 -56px;border-radius:14px}.rechx-intro{padding:120px 0 68px}.rechx-intro h2,.rechx-work h2,.rechx-outcome h2{font-size:34px}.rechx-story{padding-bottom:72px}.rechx-row{grid-template-columns:44px 1fr;gap:14px;padding:26px 0}.rechx-label{grid-column:2}.rechx-row-copy{grid-column:2}.rechx-row-copy h3{font-size:22px}.rechx-work{padding:76px 0 82px}.rechx-gallery{grid-template-columns:1fr;grid-template-rows:auto;gap:10px;margin-top:34px}.rechx-gallery-main{grid-column:auto}.rechx-gallery figure{height:300px}.rechx-gallery-copy{min-height:240px}.rechx-gallery-copy h3{font-size:25px}.rechx-outcome{padding:72px 0}.rechx-quote{padding:72px 0}.rechx-quote blockquote{font-size:28px}.rechx-next{padding:72px 0 82px}.rechx-next-head{flex-direction:column;align-items:flex-start}.rechx-next-card{height:350px}.rechx-next-copy{left:22px;right:22px;bottom:22px}.rechx-next-copy h3{font-size:28px}}
</style>
'''

s = re.sub(r'<style id="rech-editorial-v5">.*?</style>\s*', '', s, flags=re.S)
s = s.replace('</head>', css + '\n</head>', 1)
p.write_text(s, encoding='utf-8')
