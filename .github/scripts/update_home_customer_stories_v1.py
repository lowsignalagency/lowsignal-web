from pathlib import Path
import re

p=Path('index.html')
s=p.read_text()

section='''<section class="lsr-testimonials lsr-cases home-stories-v2" id="customer-stories">
  <div class="lsr-wrap">
    <div class="home-stories-v2-head">
      <div>
        <div class="lsr-eyebrow lsr-reveal">Customer Stories</div>
        <h2 class="lsr-reveal">Historias reales. <strong>Crecimiento real.</strong></h2>
      </div>
      <p class="home-stories-v2-intro lsr-reveal">Tres industrias. Un mismo enfoque: entender el negocio, construir mejor y hacer que cada sistema trabaje para crecer.</p>
    </div>

    <div class="home-stories-v2-grid">
      <article class="home-story-v2 lsr-reveal" style="--story-bg:url('https://lowsignal.cl/assets/comunidad-rech.jpg')">
        <div class="home-story-v2-panel">
          <span class="home-story-v2-tag">EDUCATION</span>
          <img class="home-story-v2-logo" src="https://lowsignal.cl/assets/rech-logo-full-white-trim.png" alt="Red Educacional Camilo Henríquez">
          <blockquote>“lowsignal se ha convertido en un aliado estratégico para nuestra red. Entendieron nuestra visión y se involucraron de verdad en el proyecto.”</blockquote>
          <div class="home-story-v2-person">
            <img src="https://lowsignal.cl/assets/nicolas-munoz.jpg" alt="Nicolás Muñoz">
            <div><b>Nicolás Muñoz</b><span>Director Ejecutivo, RECH</span></div>
            <a href="https://lowsignal.cl/casos/rech">Ver caso ↗</a>
          </div>
        </div>
      </article>

      <article class="home-story-v2 lsr-reveal" style="--story-bg:url('https://lowsignal.cl/assets/galpon-merk.jpg')">
        <div class="home-story-v2-panel">
          <span class="home-story-v2-tag">B2B</span>
          <img class="home-story-v2-logo" src="https://lowsignal.cl/assets/rikdom.png" alt="Rikdom">
          <blockquote>“lowsignal entendió lo que queríamos mostrar con Rikdom y lo llevó a una web clara, moderna y fácil de navegar.”</blockquote>
          <div class="home-story-v2-person">
            <img src="https://lowsignal.cl/assets/rodrigo.jpg" alt="Rodrigo Cuevas">
            <div><b>Rodrigo Cuevas</b><span>Socio fundador, Rikdom</span></div>
            <a href="https://lowsignal.cl/casos/rikdom">Ver caso ↗</a>
          </div>
        </div>
      </article>

      <article class="home-story-v2 lsr-reveal" style="--story-bg:url('https://lowsignal.cl/assets/dulce-reino-pasteleria.jpg')">
        <div class="home-story-v2-panel">
          <span class="home-story-v2-tag">B2C</span>
          <img class="home-story-v2-logo" src="https://lowsignal.cl/assets/dulcereino-logo-trim.png" alt="DulceReino">
          <blockquote>“En lowsignal encontré versatilidad, compromiso y un equipo que se involucra de verdad. Entienden el negocio, no solo ejecutan.”</blockquote>
          <div class="home-story-v2-person">
            <img src="https://lowsignal.cl/assets/david-suazo.jpg" alt="David Suazo">
            <div><b>David Suazo</b><span>Founder, DulceReino</span></div>
            <a href="https://lowsignal.cl/casos/dulce-reino">Ver caso ↗</a>
          </div>
        </div>
      </article>
    </div>

    <div class="lsr-cases-footer home-stories-v2-footer">
      <p>Proyectos y alianzas construidas junto a clientes de distintas industrias.</p>
      <a href="https://lowsignal.cl/casos">Ver más historias <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>'''

pattern=r'<section class="lsr-testimonials lsr-cases" id="customer-stories">.*?</section>\s*(?=<section class="lsr-tech-partners">)'
s,n=re.subn(pattern,section+'\n\n',s,count=1,flags=re.S)
if n!=1:
    raise RuntimeError(f'customer stories section replace failed: {n}')

css='''
<style id="home-customer-stories-v2">
.home-stories-v2{padding:108px 0 116px!important;background:#071022!important;color:#fff}
.home-stories-v2-head{display:grid;grid-template-columns:1fr .72fr;gap:72px;align-items:end}
.home-stories-v2-head h2{max-width:780px;margin:18px 0 0;color:#F4F6FF;font-size:clamp(38px,4vw,56px);line-height:1.07;letter-spacing:-.045em;font-weight:300}
.home-stories-v2-head h2 strong{color:#8EA3FF;font-weight:300}
.home-stories-v2-intro{margin:0;color:#8995B4;font-size:13px;line-height:1.7;max-width:430px;justify-self:end}
.home-stories-v2-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:48px}
.home-story-v2{position:relative;min-height:500px;border-radius:22px;overflow:hidden;background-image:linear-gradient(180deg,rgba(5,10,24,.08),rgba(5,10,24,.38)),var(--story-bg);background-size:cover;background-position:center;isolation:isolate;transition:transform .24s ease,box-shadow .24s ease}
.home-story-v2:before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,10,24,.06) 0%,rgba(5,10,24,.16) 35%,rgba(5,10,24,.58) 100%);z-index:-1}
.home-story-v2:hover{transform:translateY(-4px);box-shadow:0 24px 70px rgba(0,0,0,.28)}
.home-story-v2-panel{position:absolute;left:18px;right:18px;bottom:18px;min-height:290px;padding:24px;display:flex;flex-direction:column;background:rgba(5,10,24,.91);border:1px solid rgba(255,255,255,.09);color:#fff;box-shadow:0 20px 55px rgba(0,0,0,.22)}
.home-story-v2-tag{color:#8EA3FF;font-size:9px;font-weight:700;letter-spacing:.16em}
.home-story-v2-logo{height:30px;width:auto;max-width:138px;object-fit:contain;object-position:left center;margin:16px 0 20px}
.home-story-v2 blockquote{margin:0;color:#F5F7FF;font-size:15px;line-height:1.55;font-weight:300;letter-spacing:-.015em}
.home-story-v2-person{display:grid;grid-template-columns:42px 1fr auto;gap:11px;align-items:center;margin-top:auto;padding-top:22px}
.home-story-v2-person>img{width:42px;height:42px;border-radius:50%;object-fit:cover;border:1px solid rgba(255,255,255,.16)}
.home-story-v2-person b{display:block;color:#fff;font-size:11px;font-weight:650}
.home-story-v2-person span{display:block;margin-top:3px;color:#A7B1CB;font-size:9px;line-height:1.35}
.home-story-v2-person a{color:#A8B8FF;font-size:9px;font-weight:700;white-space:nowrap}
.home-stories-v2-footer{margin-top:26px!important}
@media(max-width:1100px){.home-stories-v2-grid{grid-template-columns:1fr}.home-story-v2{min-height:430px}.home-story-v2-panel{max-width:560px}.home-stories-v2-head{grid-template-columns:1fr;gap:18px}.home-stories-v2-intro{justify-self:start}}
@media(max-width:760px){.home-stories-v2{padding:82px 0 90px!important}.home-stories-v2-head h2{font-size:42px}.home-stories-v2-grid{margin-top:32px;gap:14px}.home-story-v2{min-height:440px;border-radius:18px}.home-story-v2-panel{left:14px;right:14px;bottom:14px;min-height:300px;padding:21px}.home-story-v2 blockquote{font-size:14px}.home-story-v2-person{grid-template-columns:40px 1fr}.home-story-v2-person a{grid-column:2;margin-top:6px}.home-stories-v2-footer{display:flex!important;flex-direction:column!important;align-items:flex-start!important;gap:18px!important}}
@media(prefers-reduced-motion:reduce){.home-story-v2{transition:none}}
</style>
'''

if 'home-customer-stories-v2' not in s:
    s=s.replace('</head>',css+'\n</head>',1)

p.write_text(s)
