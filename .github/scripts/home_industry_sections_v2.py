from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Remove prior showcase CSS if present.
s = re.sub(r'\n?<style id="home-industry-showcase-v1">.*?</style>\n?', '\n', s, flags=re.S)
s = re.sub(r'\n?<style id="home-industry-sections-v2">.*?</style>\n?', '\n', s, flags=re.S)

new_html = '''<section class="low-industry-section low-industry-education" id="industrias">
  <div class="lsr-wrap">
    <div class="low-industry-top">
      <div class="low-industry-copy lsr-reveal">
        <small>FOR SCHOOLS / EDUCATION PROVIDERS</small>
        <h2>Visibilidad, admisión y experiencia digital.</h2>
        <p>Ayudamos a colegios, redes educativas, fundaciones e instituciones a conectar presencia digital, captación y experiencia para crecer con más claridad.</p>
        <div class="low-industry-actions">
          <a class="low-btn-secondary" href="https://lowsignal.cl/industrias/educacion">Ver más</a>
          <a class="low-btn-primary" href="https://lowsignal.cl/industrias/educacion#planes-education">Ver planes</a>
        </div>
      </div>
      <div class="low-industry-features lsr-reveal">
        <span>KEY FEATURES</span>
        <div class="low-feature-list">
          <div>Presencia y contenido institucional</div>
          <div>Campañas de admisión</div>
          <div>Web y experiencia digital</div>
          <div>Automatización y seguimiento</div>
        </div>
      </div>
    </div>
    <div class="low-industry-stats lsr-reveal" id="planes">
      <div><small>PROYECTOS</small><strong>20+</strong><span>iniciativas desarrolladas en educación.</span></div>
      <div><small>REACH</small><strong>100K+</strong><span>personas alcanzadas con contenido y campañas.</span></div>
      <div><small>PLANES</small><strong>Desde 5 UF</strong><span>+ IVA / mes.</span></div>
    </div>
  </div>
</section>

<section class="low-industry-section low-industry-b2b">
  <div class="lsr-wrap">
    <div class="low-industry-top">
      <div class="low-industry-copy lsr-reveal">
        <small>FOR B2B / COMPANIES</small>
        <h2>Demanda, posicionamiento y pipeline conectados.</h2>
        <p>Construimos sistemas de growth para empresas B2B que necesitan convertir contenido, paid media y señales digitales en oportunidades comerciales reales.</p>
        <div class="low-industry-actions">
          <a class="low-btn-secondary" href="https://lowsignal.cl/industrias/b2b">Ver más</a>
          <a class="low-btn-primary" href="https://lowsignal.cl/industrias/b2b#planes-b2b">Ver planes</a>
        </div>
      </div>
      <div class="low-industry-features lsr-reveal">
        <span>KEY FEATURES</span>
        <div class="low-feature-list">
          <div>Posicionamiento y contenido</div>
          <div>Paid media y generación de demanda</div>
          <div>Lead generation</div>
          <div>Web, CRM y automatización</div>
        </div>
      </div>
    </div>
    <div class="low-industry-stats lsr-reveal">
      <div><small>PIPELINE</small><strong>1K+</strong><span>oportunidades generadas.</span></div>
      <div><small>FOCUS</small><strong>SaaS + Tech</strong><span>servicios profesionales e industria.</span></div>
      <div><small>PLANES</small><strong>Desde 6 UF</strong><span>+ IVA / mes.</span></div>
    </div>
  </div>
</section>

<section class="low-industry-section low-industry-b2c">
  <div class="lsr-wrap">
    <div class="low-industry-top">
      <div class="low-industry-copy lsr-reveal">
        <small>FOR BRANDS / B2C</small>
        <h2>Contenido, performance y conversión para marcas que quieren crecer.</h2>
        <p>Ayudamos a marcas de consumo a conectar atención, tráfico y ventas a través de contenido, campañas y sistemas digitales.</p>
        <div class="low-industry-actions">
          <a class="low-btn-secondary" href="https://lowsignal.cl/industrias/marcas-b2c">Ver más</a>
          <a class="low-btn-primary" href="https://lowsignal.cl/industrias/marcas-b2c#planes-b2c">Ver planes</a>
        </div>
      </div>
      <div class="low-industry-features lsr-reveal">
        <span>KEY FEATURES</span>
        <div class="low-feature-list">
          <div>Contenido y social</div>
          <div>Paid media</div>
          <div>Campañas promocionales y estacionales</div>
          <div>Conversión y automatización</div>
        </div>
      </div>
    </div>
    <div class="low-industry-stats lsr-reveal">
      <div><small>CONTENT</small><strong>400+</strong><span>piezas de contenido desarrolladas.</span></div>
      <div><small>PERFORMANCE</small><strong>100+</strong><span>campañas y experimentos ejecutados.</span></div>
      <div><small>PLANES</small><strong>Desde 5 UF</strong><span>+ IVA / mes.</span></div>
    </div>
  </div>
</section>'''

s, n = re.subn(
    r'<section class="lsr-industry-showcase" id="industrias">.*?</section>\s*(?=<section class="lsr-band">)',
    new_html + '\n\n',
    s,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit(f'Expected one showcase section, replaced {n}')

css = '''
<style id="home-industry-sections-v2">
.low-industry-section{padding:118px 0 104px;scroll-margin-top:128px}.low-industry-top{display:grid;grid-template-columns:minmax(0,.92fr) minmax(360px,1.08fr);gap:86px;align-items:start}.low-industry-copy>small,.low-industry-features>span{display:block;font-size:9px;font-weight:800;letter-spacing:.18em}.low-industry-copy h2{max-width:690px;margin:20px 0 0;font-size:clamp(38px,4vw,56px);line-height:1.06;letter-spacing:-.048em;font-weight:300}.low-industry-copy p{max-width:680px;margin:24px 0 0;font-size:15px;line-height:1.72}.low-industry-actions{display:flex;gap:12px;margin-top:28px}.low-industry-actions a{min-height:44px;padding:0 18px;border-radius:999px;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;transition:transform .18s ease,background .18s ease,border-color .18s ease,color .18s ease}.low-industry-actions a:hover{transform:translateY(-2px)}.low-industry-features>span{margin-bottom:20px}.low-feature-list{display:grid;gap:14px}.low-feature-list div{position:relative;min-height:66px;padding:0 20px 0 48px;border-radius:14px;display:flex;align-items:center;font-size:14px;line-height:1.35}.low-feature-list div:before{content:"";position:absolute;left:20px;width:7px;height:7px;border-radius:50%}.low-industry-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:42px;margin-top:62px;padding-top:34px}.low-industry-stats>div{padding-left:20px}.low-industry-stats small{display:block;font-size:8px;font-weight:800;letter-spacing:.17em}.low-industry-stats strong{display:block;margin-top:14px;font-size:31px;line-height:1.05;letter-spacing:-.04em;font-weight:500}.low-industry-stats span{display:block;max-width:310px;margin-top:12px;font-size:12px;line-height:1.55}
.low-industry-education{background:#F4F6FC;color:#0A1230}.low-industry-education .low-industry-copy>small,.low-industry-education .low-industry-features>span,.low-industry-education .low-industry-stats small{color:#1419E0}.low-industry-education .low-industry-copy p,.low-industry-education .low-industry-stats span{color:#66708A}.low-industry-education .low-feature-list div{background:#fff;border:1px solid #D8DFEE;color:#162041}.low-industry-education .low-feature-list div:before{background:#1419E0}.low-industry-education .low-industry-stats{border-top:1px solid #DCE3F0}.low-industry-education .low-industry-stats>div{border-left:2px solid #BFC8FF}.low-industry-education .low-btn-secondary{border:1px solid #CBD4E7;color:#0A1230;background:transparent}.low-industry-education .low-btn-primary{border:1px solid #1419E0;color:#fff;background:#1419E0}.low-industry-education .low-btn-secondary:hover{border-color:#1419E0;color:#1419E0;background:#fff}.low-industry-education .low-btn-primary:hover{background:#2B35F0;border-color:#2B35F0}
.low-industry-b2b{background:#071022;color:#fff}.low-industry-b2b .low-industry-copy>small,.low-industry-b2b .low-industry-features>span,.low-industry-b2b .low-industry-stats small{color:#8EA2FF}.low-industry-b2b .low-industry-copy p,.low-industry-b2b .low-industry-stats span{color:#8C96AF}.low-industry-b2b .low-feature-list div{background:#0B1632;border:1px solid rgba(142,162,255,.18);color:#E9ECF7}.low-industry-b2b .low-feature-list div:before{background:#5B70FF}.low-industry-b2b .low-industry-stats{border-top:1px solid rgba(142,162,255,.15)}.low-industry-b2b .low-industry-stats>div{border-left:2px solid rgba(91,112,255,.65)}.low-industry-b2b .low-btn-secondary{border:1px solid rgba(255,255,255,.22);color:#fff;background:transparent}.low-industry-b2b .low-btn-primary{border:1px solid #5367F2;color:#fff;background:#263BE1}.low-industry-b2b .low-btn-secondary:hover{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.34)}.low-industry-b2b .low-btn-primary:hover{background:#3C51ED;border-color:#3C51ED}
.low-industry-b2c{background:#1419E0;color:#fff}.low-industry-b2c .low-industry-copy>small,.low-industry-b2c .low-industry-features>span,.low-industry-b2c .low-industry-stats small{color:#DCE2FF}.low-industry-b2c .low-industry-copy p,.low-industry-b2c .low-industry-stats span{color:#CDD4FF}.low-industry-b2c .low-feature-list div{background:rgba(7,16,34,.12);border:1px solid rgba(255,255,255,.20);color:#fff}.low-industry-b2c .low-feature-list div:before{background:#fff}.low-industry-b2c .low-industry-stats{border-top:1px solid rgba(255,255,255,.18)}.low-industry-b2c .low-industry-stats>div{border-left:2px solid rgba(255,255,255,.55)}.low-industry-b2c .low-btn-secondary{border:1px solid rgba(255,255,255,.35);color:#fff;background:transparent}.low-industry-b2c .low-btn-primary{border:1px solid #fff;color:#1419E0;background:#fff}.low-industry-b2c .low-btn-secondary:hover{background:rgba(255,255,255,.08)}.low-industry-b2c .low-btn-primary:hover{background:#EEF1FF;border-color:#EEF1FF}
@media(max-width:980px){.low-industry-top{grid-template-columns:1fr;gap:40px}.low-industry-stats{gap:18px}}@media(max-width:620px){.low-industry-section{padding:72px 0 68px}.low-industry-copy h2{font-size:34px}.low-industry-copy p{font-size:13px}.low-industry-actions{display:grid;grid-template-columns:1fr 1fr}.low-industry-actions a{width:100%}.low-feature-list div{min-height:58px;padding:0 16px 0 44px;font-size:12px}.low-feature-list div:before{left:18px}.low-industry-stats{grid-template-columns:1fr;margin-top:40px;padding-top:26px;gap:22px}.low-industry-stats>div{padding-left:14px}.low-industry-stats strong{font-size:26px}}
</style>
'''

s = s.replace('</head>', css + '</head>', 1)
p.write_text(s, encoding='utf-8')
print('Applied Low-branded alternating industry sections')

# trigger v2
