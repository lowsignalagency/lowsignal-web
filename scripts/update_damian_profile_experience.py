from pathlib import Path
import re

path = Path('equipo/damian-aldunate.html')
s = path.read_text(encoding='utf-8')

# Remove previous generated variants if this runs again.
s = re.sub(r'\n?<style id="damian-experience-v1">.*?</style>\s*', '\n', s, flags=re.S)
s = re.sub(r'\n?<section class="tp-experience damian-experience"[^>]*>.*?</section>\s*', '\n', s, count=1, flags=re.S)
s = re.sub(r'\n\s*<div class="tp-profile-links" aria-label="Enlaces de Damián">.*?</div>', '', s, count=1, flags=re.S)

summary = '<p class="tp-summary">Lidera estrategia de marca, marketing y crecimiento en lowsignal, conectando posicionamiento, contenido, campañas y ejecución comercial.</p>'
links = '''\n        <div class="tp-profile-links" aria-label="Enlaces de Damián">\n          <a href="https://www.linkedin.com/in/damianaldunate/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>\n        </div>'''
s = s.replace(summary, summary + links, 1)

css = r'''
<style id="damian-experience-v1">
.tp-profile-links{display:flex;flex-wrap:wrap;gap:10px 24px;margin-top:32px;padding-top:24px;border-top:1px solid rgba(138,164,255,.14)}
.tp-profile-links a{color:#C2CBE0;font-size:11px;font-weight:600;transition:color .18s ease}
.tp-profile-links a:hover{color:#fff}
.tp-experience{padding:112px 0 120px;background:#fff;color:#0D1420}
.tp-experience-head{max-width:760px}
.tp-experience-head h2{margin:18px 0 0;font-size:clamp(40px,4.3vw,58px);line-height:1.05;letter-spacing:-.05em;font-weight:300}
.tp-experience-head h2 span{color:#5E73D8;font-weight:500}
.tp-experience-head>p{max-width:640px;margin:20px 0 0;color:#6B7890;font-size:14px;line-height:1.7}
.tp-timeline{margin-top:58px;border-top:1px solid #DDE4F0}
.tp-role{display:grid;grid-template-columns:70px 260px minmax(0,1fr);gap:34px;padding:32px 0;border-bottom:1px solid #DDE4F0}
.tp-role-index{color:#8393B1;font-size:11px;padding-top:4px}
.tp-role-brand{min-height:58px;display:flex;align-items:center;margin-bottom:7px}
.tp-role-brand img{width:138px;height:auto;max-height:52px;object-fit:contain;object-position:left center}
.tp-role-meta span{display:block;margin-top:6px;color:#53617A;font-size:12px}
.tp-role-meta small{display:block;margin-top:10px;color:#8490A7;font-size:9px;letter-spacing:.08em;text-transform:uppercase}
.tp-role-body h3{margin:0;color:#111A2B;font-size:24px;line-height:1.22;letter-spacing:-.035em;font-weight:400}
.tp-role-body p{max-width:720px;margin:12px 0 0;color:#647087;font-size:13px;line-height:1.72}
@media(max-width:760px){
  .tp-profile-links{margin-top:24px;padding-top:20px;gap:10px 18px}
  .tp-experience{padding:76px 0}
  .tp-experience-head h2{font-size:39px}
  .tp-role{grid-template-columns:1fr;gap:8px;padding:26px 0}
  .tp-role-index{padding-top:0}
  .tp-role-brand{min-height:50px;margin:4px 0 8px}
  .tp-role-brand img{width:126px;max-height:46px}
}
</style>
'''

experience = r'''
<section class="tp-experience damian-experience" aria-labelledby="damian-experience-title">
  <div class="tp-shell">
    <div class="tp-experience-head">
      <div class="tp-eyebrow">EXPERIENCIA</div>
      <h2 id="damian-experience-title">Tecnología con <span>impacto real.</span></h2>
      <p>Experiencias donde innovación, comunicación y trabajo con comunidades se conectan con problemas concretos.</p>
    </div>
    <div class="tp-timeline">
      <article class="tp-role">
        <div class="tp-role-index">01</div>
        <div class="tp-role-meta">
          <div class="tp-role-brand">
            <img src="https://lowsignal.cl/assets/consiliumbots-logo.svg" alt="ConsiliumBots">
          </div>
          <span>Embajador de Innovación Educativa</span>
          <small>ONG · US / LATAM</small>
        </div>
        <div class="tp-role-body">
          <h3>Acercar tecnología y datos públicos a comunidades.</h3>
          <p>En ConsiliumBots trabajó conectando innovación tecnológica con comunidades educativas y sociales, apoyando iniciativas orientadas a transformar datos del gobierno en información más accesible y útil para las personas. Contribuyó desde comunicación, contenidos, outreach y vínculo con instituciones para ampliar el acceso a educación, vivienda y otros beneficios públicos, reforzando la misión de la organización de generar impacto social y económico mediante tecnología.</p>
        </div>
      </article>
    </div>
  </div>
</section>
'''

s = s.replace('</head>', css + '\n</head>', 1)
s = s.replace('<section class="tp-expertise">', experience + '\n<section class="tp-expertise">', 1)

path.write_text(s, encoding='utf-8')
