from pathlib import Path
import re

p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

main = r'''<main id="top" class="dalix">
  <section class="dalix-hero">
    <div class="container dalix-wrap">
      <div class="dalix-kicker">CUSTOMER STORY <span>·</span> EDUCACIÓN</div>
      <div class="dalix-hero-grid">
        <div>
          <h1>Hacer visible la vida del colegio.<br><strong>Y acercarla a nuevas familias.</strong></h1>
          <p>Junto al Colegio Salvador Dalí conectamos contenido, campañas y web para transformar su día a día en una experiencia digital capaz de informar, generar confianza y acompañar a las familias durante la admisión.</p>
          <div class="dalix-meta">
            <div><span>CLIENTE</span><b>Colegio Salvador Dalí</b></div>
            <div><span>TRABAJO</span><b>Social · Paid Media · Web</b></div>
          </div>
        </div>
        <aside class="dalix-side-note">
          <span>EL FOCO</span>
          <p>No mostrar un colegio “desde afuera”. Hacer sentir, desde digital, cómo se vive dentro.</p>
        </aside>
      </div>
      <figure class="dalix-cover"><img src="https://lowsignal.cl/assets/dali-patio-nueva.jpg" alt="Colegio Salvador Dalí"></figure>
    </div>
  </section>

  <section class="dalix-intro">
    <div class="container dalix-wrap dalix-intro-grid">
      <div>
        <div class="dalix-eyebrow">EL CASO</div>
        <h2>La experiencia ya existía.<br><strong>Había que hacerla visible.</strong></h2>
      </div>
      <p>El colegio tenía comunidad, actividades, proyectos y una vida escolar activa. El desafío era ordenar esa experiencia y convertirla en una presencia digital capaz de hablarle mejor a quienes ya eran parte del colegio y a quienes recién lo estaban conociendo.</p>
    </div>
  </section>

  <section class="dalix-journey">
    <div class="container dalix-wrap">
      <div class="dalix-journey-head">
        <div class="dalix-eyebrow">EL RECORRIDO</div>
        <h2>De descubrir el colegio<br>a <strong>querer ser parte.</strong></h2>
      </div>
      <div class="dalix-flow">
        <article><span>01</span><div><small>TE DESCUBRE</small><h3>Contenido que muestra vida real.</h3><p>La comunidad, sus actividades y sus historias pasan a ser la primera señal de lo que significa estudiar ahí.</p></div></article>
        <article><span>02</span><div><small>TE INVESTIGA</small><h3>Una web que ordena lo importante.</h3><p>Proyecto educativo, admisión e información clave presentados de forma más clara para familias que necesitan entender antes de decidir.</p></div></article>
        <article><span>03</span><div><small>TE CONSIDERA</small><h3>Campañas que vuelven a poner al colegio frente a la familia correcta.</h3><p>Paid media conectado al contenido y la web para acompañar el interés y llevarlo hacia acciones concretas.</p></div></article>
        <article><span>04</span><div><small>CONFÍA</small><h3>Una experiencia consistente en cada punto de contacto.</h3><p>La misma propuesta, el mismo tono y la misma comunidad reconocible desde redes hasta la postulación.</p></div></article>
      </div>
    </div>
  </section>

  <section class="dalix-work">
    <div class="container dalix-wrap">
      <div class="dalix-work-head">
        <div><div class="dalix-eyebrow dalix-eyebrow-dark">EL TRABAJO</div><h2>No se trataba de publicar más.<br><strong>Se trataba de conectar mejor.</strong></h2></div>
        <p>Contenido, campañas y web dejaron de ser piezas separadas y empezaron a cumplir funciones distintas dentro de una misma experiencia para familias y comunidad.</p>
      </div>
      <div class="dalix-showcase">
        <figure class="dalix-showcase-main"><img src="https://lowsignal.cl/assets/dali-patio-nueva.jpg" alt="Comunidad Colegio Salvador Dalí"></figure>
        <div class="dalix-showcase-copy"><span>SOCIAL · PAID · WEB</span><h3>Un sistema digital que acompaña la decisión.</h3><p>Desde el contenido cotidiano que genera cercanía hasta la información que una familia necesita cuando evalúa postular.</p></div>
      </div>
    </div>
  </section>

  <section class="dalix-outcome">
    <div class="container dalix-wrap dalix-outcome-grid">
      <div class="dalix-eyebrow">LA TRANSFORMACIÓN</div>
      <h2>Una presencia digital más cercana, más clara y <strong>más conectada con admisión.</strong></h2>
      <p>El resultado fue una experiencia capaz de mostrar mejor quién es el colegio, fortalecer la relación con su comunidad y acompañar a nuevas familias en el proceso de conocerlo.</p>
    </div>
  </section>

  <section class="dalix-quote">
    <div class="container dalix-wrap dalix-quote-inner">
      <div class="dalix-quote-mark">“</div>
      <blockquote>Con lowsignal fortalecimos nuestras redes, nos acercamos a la comunidad y potenciamos las habilidades de nuestros estudiantes.</blockquote>
      <div class="dalix-person"><img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal"><div><b>Karina Ravanal</b><span>Directora, Colegio Salvador Dalí</span></div></div>
    </div>
  </section>

  <section class="dalix-next">
    <div class="container dalix-wrap">
      <div class="dalix-next-head"><div><div class="dalix-eyebrow">CUSTOMER STORIES</div><h2>Más trabajo.<br>Menos promesas.</h2></div><a href="https://lowsignal.cl/casos">Ver todos los casos ↗</a></div>
    </div>
  </section>

  <section class="lsr-band"><div class="lsr-wrap lsr-band-inner"><p>¿Construimos lo que viene?</p><a href="https://calendly.com/felipe-lowsignal/30min" target="_blank" rel="noopener noreferrer">Hablemos</a></div></section>
</main>'''

s, n = re.subn(r'<main id="top".*?</main>', main, s, count=1, flags=re.S)
if n != 1:
    raise RuntimeError('Could not replace Salvador Dali main')

css = r'''
<style id="salvador-dali-editorial-v1">
.dalix{background:#fff;color:#071022}.dalix-wrap{width:min(1220px,calc(100% - 128px))!important;max-width:1220px!important;margin-inline:auto!important}.dalix-hero{padding:158px 0 0;background:#F5F7FB}.dalix-kicker,.dalix-eyebrow{font-size:10px;letter-spacing:.18em;font-weight:700;color:#1419E0}.dalix-kicker span{opacity:.45;margin:0 7px}.dalix-hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:78px;align-items:end;margin-top:24px}.dalix-hero h1{max-width:930px;margin:0;font-size:clamp(54px,5vw,72px);line-height:1.01;letter-spacing:-.058em;font-weight:300}.dalix-hero h1 strong,.dalix-intro h2 strong,.dalix-journey h2 strong,.dalix-work h2 strong,.dalix-outcome h2 strong{color:#1419E0;font-weight:400}.dalix-hero-grid>div>p{max-width:760px;margin:28px 0 0;color:#52617D;font-size:17px;line-height:1.72}.dalix-meta{display:grid;grid-template-columns:1fr 1fr;gap:28px;max-width:760px;margin-top:34px;padding-top:18px;border-top:1px solid rgba(20,25,224,.14)}.dalix-meta span,.dalix-side-note span{display:block;color:#7E8AA2;font-size:9px;letter-spacing:.14em;font-weight:700}.dalix-meta b{display:block;margin-top:7px;color:#15204D;font-size:13px;font-weight:500}.dalix-side-note{padding:26px 0 4px;border-top:1px solid #D9E0EC}.dalix-side-note p{margin:15px 0 0;color:#26324D;font-size:14px;line-height:1.7}.dalix-cover{margin:54px 0 -90px;height:min(50vw,650px);border-radius:20px;overflow:hidden;box-shadow:0 28px 70px rgba(7,15,34,.15)}.dalix-cover img{width:100%;height:100%;object-fit:cover;object-position:center 42%;transition:transform .7s cubic-bezier(.2,.7,.2,1)}
.dalix-intro{padding:176px 0 96px}.dalix-intro-grid{display:grid;grid-template-columns:1fr .72fr;gap:86px;align-items:end}.dalix-intro h2,.dalix-journey h2,.dalix-work h2,.dalix-outcome h2{margin:16px 0 0;font-size:clamp(42px,4.2vw,58px);line-height:1.04;letter-spacing:-.052em;font-weight:300}.dalix-intro-grid>p,.dalix-work-head>p,.dalix-outcome-grid>p{margin:0;color:#66728B;font-size:15px;line-height:1.8}
.dalix-journey{padding:0 0 112px}.dalix-journey-head{display:grid;grid-template-columns:.35fr 1fr;gap:54px;align-items:start;padding-bottom:36px}.dalix-flow{border-top:1px solid #DEE4EE}.dalix-flow article{display:grid;grid-template-columns:74px 1fr;gap:22px;padding:30px 0;border-bottom:1px solid #DEE4EE}.dalix-flow article>span{color:#1419E0;font-size:12px;font-weight:700}.dalix-flow small{color:#8993A7;font-size:9px;letter-spacing:.15em;font-weight:700}.dalix-flow h3{margin:8px 0 0;font-size:25px;letter-spacing:-.035em;font-weight:500}.dalix-flow p{max-width:760px;margin:10px 0 0;color:#68748C;font-size:14px;line-height:1.75}
.dalix-work{padding:110px 0 118px;background:#070F22;color:#fff}.dalix-eyebrow-dark{color:#8EA3FF}.dalix-work h2{color:#fff}.dalix-work h2 strong{color:#A9B5FF}.dalix-work-head{display:grid;grid-template-columns:1.05fr .68fr;gap:80px;align-items:end}.dalix-work-head>p{color:#AAB4C8}.dalix-showcase{display:grid;grid-template-columns:1.2fr .8fr;gap:16px;margin-top:50px}.dalix-showcase figure,.dalix-showcase-copy{margin:0;border-radius:18px;overflow:hidden}.dalix-showcase-main{height:560px}.dalix-showcase-main img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.2,.7,.2,1)}.dalix-showcase-copy{padding:34px;background:#101A31;border:1px solid rgba(255,255,255,.08);display:flex;flex-direction:column;justify-content:flex-end}.dalix-showcase-copy span{color:#8EA3FF;font-size:9px;letter-spacing:.14em;font-weight:700}.dalix-showcase-copy h3{margin:16px 0 0;font-size:32px;line-height:1.16;letter-spacing:-.04em;font-weight:400}.dalix-showcase-copy p{margin:14px 0 0;color:#AAB4C8;font-size:13px;line-height:1.75}
.dalix-outcome{padding:108px 0;background:#F4F6FB}.dalix-outcome-grid{display:grid;grid-template-columns:.30fr 1.12fr .68fr;gap:52px}.dalix-outcome h2{margin:0}.dalix-outcome-grid>p{margin-top:6px}
.dalix-quote{padding:92px 0;background:#1419E0;color:#fff}.dalix-quote-inner{max-width:1080px!important}.dalix-quote-mark{font-size:72px;line-height:.7;color:rgba(255,255,255,.45)}.dalix-quote blockquote{max-width:920px;margin:18px 0 30px;font-size:clamp(30px,3vw,42px);line-height:1.22;letter-spacing:-.04em;font-weight:300}.dalix-person{display:flex;align-items:center;gap:14px}.dalix-person img{width:56px;height:56px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.45)}.dalix-person b{display:block;font-size:14px}.dalix-person span{display:block;margin-top:4px;color:#D6DEFF;font-size:11px}
.dalix-next{padding:92px 0 106px}.dalix-next-head{display:flex;justify-content:space-between;align-items:end;gap:40px}.dalix-next-head h2{margin:12px 0 0;font-size:38px;line-height:1.08;letter-spacing:-.045em;font-weight:300}.dalix-next-head a{color:#1419E0;font-size:13px;font-weight:600;transition:transform .2s ease,color .2s ease}
@media(hover:hover){.dalix-cover:hover img,.dalix-showcase-main:hover img{transform:scale(1.02)}.dalix-next-head a:hover{transform:translateX(4px);color:#0D13B9}}
@media(max-width:1000px){.dalix-wrap{width:calc(100% - 48px)!important}.dalix-hero-grid,.dalix-intro-grid,.dalix-work-head,.dalix-outcome-grid{grid-template-columns:1fr;gap:34px}.dalix-side-note{max-width:420px}.dalix-journey-head{grid-template-columns:1fr;gap:18px}.dalix-showcase{grid-template-columns:1fr}.dalix-showcase-main{height:470px}.dalix-showcase-copy{min-height:260px}.dalix-outcome-grid{gap:22px}}
@media(max-width:760px){.dalix-wrap{width:calc(100% - 24px)!important}.dalix-hero{padding-top:134px}.dalix-hero h1{font-size:42px}.dalix-hero-grid>div>p{font-size:15px}.dalix-meta{grid-template-columns:1fr}.dalix-cover{height:330px;margin:38px 0 -56px;border-radius:15px}.dalix-intro{padding:118px 0 68px}.dalix-intro h2,.dalix-journey h2,.dalix-work h2,.dalix-outcome h2{font-size:34px}.dalix-journey{padding-bottom:72px}.dalix-flow article{grid-template-columns:44px 1fr;padding:24px 0}.dalix-flow h3{font-size:21px}.dalix-work{padding:76px 0 82px}.dalix-showcase{margin-top:34px}.dalix-showcase-main{height:310px}.dalix-showcase-copy{min-height:220px;padding:24px}.dalix-showcase-copy h3{font-size:25px}.dalix-outcome{padding:72px 0}.dalix-quote{padding:72px 0}.dalix-quote blockquote{font-size:28px}.dalix-next{padding:70px 0 82px}.dalix-next-head{flex-direction:column;align-items:flex-start}}
</style>
'''

s = re.sub(r'<style id="salvador-dali-editorial-v1">.*?</style>\s*', '', s, flags=re.S)
s = s.replace('</head>', css + '\n</head>', 1)

# Native scroll + reveal animations only.
s = re.sub(r'<script id="dalix-scroll-reveal">.*?</script>\s*', '', s, flags=re.S)
reveal = r'''
<style id="dalix-reveal-style">
.dalix-reveal{opacity:0;transform:translateY(26px);transition:opacity .65s ease,transform .78s cubic-bezier(.2,.75,.2,1)}
.dalix-reveal.is-visible{opacity:1;transform:none}.dalix-reveal-img{opacity:0;transform:translateY(20px) scale(.985);transition:opacity .72s ease,transform .9s cubic-bezier(.2,.75,.2,1)}.dalix-reveal-img.is-visible{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.dalix-reveal,.dalix-reveal-img{opacity:1!important;transform:none!important;transition:none!important}}
</style>
<script id="dalix-scroll-reveal">
document.addEventListener('DOMContentLoaded',()=>{const selectors=['.dalix-hero-grid','.dalix-cover','.dalix-intro-grid','.dalix-journey-head','.dalix-flow article','.dalix-work-head','.dalix-showcase','.dalix-outcome-grid','.dalix-quote-inner','.dalix-next-head'];const els=selectors.flatMap(sel=>[...document.querySelectorAll(sel)]);els.forEach(el=>el.classList.add(el.matches('.dalix-cover,.dalix-showcase')?'dalix-reveal-img':'dalix-reveal'));if(!('IntersectionObserver' in window)){els.forEach(el=>el.classList.add('is-visible'));return}const io=new IntersectionObserver((entries,obs)=>{entries.forEach(entry=>{if(!entry.isIntersecting)return;entry.target.classList.add('is-visible');obs.unobserve(entry.target)})},{threshold:.12,rootMargin:'0px 0px -8% 0px'});els.forEach(el=>io.observe(el))});
</script>
'''
s = re.sub(r'<style id="dalix-reveal-style">.*?</style>\s*', '', s, flags=re.S)
s = s.replace('</body>', reveal + '\n</body>', 1)

p.write_text(s, encoding='utf-8')
