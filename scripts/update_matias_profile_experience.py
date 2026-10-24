from pathlib import Path
import re

path = Path('equipo/matias-bussinger.html')
s = path.read_text(encoding='utf-8')

# Keep role language current across the profile.
s = s.replace('<title>Matías Bussinger | AI Engineer | lowsignal</title>', '<title>Matías Bussinger | AI Revenue Engineer | lowsignal</title>')
s = s.replace('<div class="tp-kicker">AI ENGINEER · LOWSIGNAL</div>', '<div class="tp-kicker">AI REVENUE ENGINEER · LOWSIGNAL</div>')
s = s.replace(
    '<p class="tp-positioning">IA, automatización y producto para convertir procesos complejos en <strong>sistemas más simples.</strong></p>',
    '<p class="tp-positioning">IA, automatización y revenue para convertir procesos complejos en <strong>sistemas que generan crecimiento.</strong></p>'
)
s = s.replace(
    '<p class="tp-summary">Construye soluciones con inteligencia artificial, automatización e integraciones para productos y operaciones de lowsignal.</p>',
    '<p class="tp-summary">Construye agentes, automatizaciones e integraciones que conectan datos, procesos comerciales y tecnología para acelerar adquisición, conversión y eficiencia.</p>'
)

# Remove generated experience section/style if this script runs again.
s = re.sub(r'\n?<style id="matias-experience-v1">.*?</style>\s*', '\n', s, flags=re.S)
s = re.sub(r'\n?<section class="tp-experience"[^>]*>.*?</section>\s*', '\n', s, count=1, flags=re.S)

css = r'''
<style id="matias-experience-v1">
.tp-experience{padding:112px 0 120px;background:#fff;color:#0D1420}
.tp-experience-head{max-width:760px}
.tp-experience-head h2{margin:18px 0 0;font-size:clamp(40px,4.3vw,58px);line-height:1.05;letter-spacing:-.05em;font-weight:300}
.tp-experience-head h2 span{color:#5E73D8;font-weight:500}
.tp-experience-head>p{max-width:640px;margin:20px 0 0;color:#6B7890;font-size:14px;line-height:1.7}
.tp-timeline{margin-top:58px;border-top:1px solid #DDE4F0}
.tp-role{display:grid;grid-template-columns:70px 260px minmax(0,1fr);gap:34px;padding:32px 0;border-bottom:1px solid #DDE4F0}
.tp-role-index{color:#8393B1;font-size:11px;padding-top:4px}
.tp-role-meta b{display:block;color:#101827;font-size:19px}
.tp-role-meta span{display:block;margin-top:6px;color:#53617A;font-size:12px}
.tp-role-meta small{display:block;margin-top:10px;color:#8490A7;font-size:9px;letter-spacing:.08em;text-transform:uppercase}
.tp-role-body h3{margin:0;color:#111A2B;font-size:24px;line-height:1.22;letter-spacing:-.035em;font-weight:400}
.tp-role-body p{max-width:720px;margin:12px 0 0;color:#647087;font-size:13px;line-height:1.72}
@media(max-width:760px){
  .tp-experience{padding:76px 0}
  .tp-experience-head h2{font-size:39px}
  .tp-role{grid-template-columns:1fr;gap:8px;padding:26px 0}
  .tp-role-index{padding-top:0}
}
</style>
'''

experience = r'''
<section class="tp-experience" aria-labelledby="matias-experience-title">
  <div class="tp-shell">
    <div class="tp-experience-head">
      <div class="tp-eyebrow">EXPERIENCIA</div>
      <h2 id="matias-experience-title">Tecnología con <span>impacto real.</span></h2>
      <p>Experiencias donde IA, innovación y trabajo con comunidades se conectan con problemas concretos.</p>
    </div>
    <div class="tp-timeline">
      <article class="tp-role">
        <div class="tp-role-index">01</div>
        <div class="tp-role-meta">
          <b>ConsiliumBots</b>
          <span>Embajador de Innovación Educativa</span>
          <small>ONG · US / LATAM</small>
        </div>
        <div class="tp-role-body">
          <h3>Acercar innovación digital a comunidades educativas.</h3>
          <p>Representó y promovió la misión de la organización de fortalecer a los colegios mediante habilidades digitales e innovación. Trabajó con comunidades educativas, apoyó la implementación de herramientas de diagnóstico y fortaleció la presencia digital a través de creación de contenido y acciones de outreach, actuando como puente entre instituciones y la organización para impulsar colaboración e impacto en educación y tecnología.</p>
        </div>
      </article>
    </div>
  </div>
</section>
'''

s = s.replace('</head>', css + '\n</head>', 1)
s = s.replace('<section class="tp-expertise">', experience + '\n<section class="tp-expertise">', 1)

path.write_text(s, encoding='utf-8')
