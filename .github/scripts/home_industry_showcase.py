from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Remove generic traction block.
s, n1 = re.subn(
    r'\s*<section class="lsr-traction">.*?</section>\s*(?=<section class="lsr-industries-simple" id="industrias">)',
    '\n\n',
    s,
    count=1,
    flags=re.S,
)
if n1 != 1:
    raise SystemExit(f'Expected to remove one traction block, removed {n1}')

showcase = '''<section class="lsr-industry-showcase" id="industrias">
  <div class="lsr-wrap">
    <div class="lsr-industry-showcase-head lsr-reveal">
      <div class="lsr-eyebrow">Where we build</div>
      <h2>Una lógica distinta para cada industria.</h2>
      <p>Education, B2B y B2C necesitan mensajes, canales y sistemas distintos. Por eso construimos una propuesta específica para cada contexto de crecimiento.</p>
    </div>

    <div class="lsr-industry-showcase-stack" id="planes">
      <article class="lsr-industry-panel lsr-reveal">
        <div class="lsr-industry-panel-top">
          <div class="lsr-industry-panel-copy">
            <small>01 · EDUCATION</small>
            <h3>Visibilidad, admisión y experiencia digital.</h3>
            <p>Para colegios, redes educativas, fundaciones e instituciones que necesitan conectar presencia digital, captación y experiencia.</p>
            <div class="lsr-industry-panel-actions">
              <a class="is-secondary" href="https://lowsignal.cl/industrias/educacion">Ver más</a>
              <a class="is-primary" href="https://lowsignal.cl/industrias/educacion#planes-education">Ver planes</a>
            </div>
          </div>
          <div class="lsr-industry-panel-features">
            <span class="lsr-industry-panel-label">Qué construimos</span>
            <div class="lsr-industry-feature-list">
              <div>Presencia y contenido</div>
              <div>Campañas de admisión</div>
              <div>Experiencia web</div>
              <div>Automatización y seguimiento</div>
            </div>
          </div>
        </div>
        <div class="lsr-industry-panel-stats">
          <div><small>PROYECTOS</small><strong>20+</strong><span>iniciativas desarrolladas en educación.</span></div>
          <div><small>REACH</small><strong>100K+</strong><span>personas alcanzadas con contenido y campañas.</span></div>
          <div><small>PLANES</small><strong>Desde 5 UF</strong><span>+ IVA / mes.</span></div>
        </div>
      </article>

      <article class="lsr-industry-panel lsr-reveal">
        <div class="lsr-industry-panel-top">
          <div class="lsr-industry-panel-copy">
            <small>02 · B2B</small>
            <h3>Demanda, posicionamiento y pipeline.</h3>
            <p>Para SaaS, tecnología, servicios profesionales e industria que necesitan convertir señales digitales en oportunidades comerciales.</p>
            <div class="lsr-industry-panel-actions">
              <a class="is-secondary" href="https://lowsignal.cl/industrias/b2b">Ver más</a>
              <a class="is-primary" href="https://lowsignal.cl/industrias/b2b#planes-b2b">Ver planes</a>
            </div>
          </div>
          <div class="lsr-industry-panel-features">
            <span class="lsr-industry-panel-label">Qué construimos</span>
            <div class="lsr-industry-feature-list">
              <div>Posicionamiento y contenido</div>
              <div>Paid media y demanda</div>
              <div>Lead generation</div>
              <div>Web, CRM y automatización</div>
            </div>
          </div>
        </div>
        <div class="lsr-industry-panel-stats">
          <div><small>PIPELINE</small><strong>1K+</strong><span>oportunidades generadas.</span></div>
          <div><small>FOCUS</small><strong>SaaS + Tech</strong><span>servicios e industria.</span></div>
          <div><small>PLANES</small><strong>Desde 6 UF</strong><span>+ IVA / mes.</span></div>
        </div>
      </article>

      <article class="lsr-industry-panel lsr-reveal">
        <div class="lsr-industry-panel-top">
          <div class="lsr-industry-panel-copy">
            <small>03 · B2C</small>
            <h3>Contenido, marca, performance y conversión.</h3>
            <p>Para retail, hospitality, food, lifestyle y marcas de consumo que necesitan conectar atención, tráfico y ventas.</p>
            <div class="lsr-industry-panel-actions">
              <a class="is-secondary" href="https://lowsignal.cl/industrias/marcas-b2c">Ver más</a>
              <a class="is-primary" href="https://lowsignal.cl/industrias/marcas-b2c#planes-b2c">Ver planes</a>
            </div>
          </div>
          <div class="lsr-industry-panel-features">
            <span class="lsr-industry-panel-label">Qué construimos</span>
            <div class="lsr-industry-feature-list">
              <div>Contenido y social</div>
              <div>Paid media</div>
              <div>Campañas estacionales</div>
              <div>Conversión y automatización</div>
            </div>
          </div>
        </div>
        <div class="lsr-industry-panel-stats">
          <div><small>CONTENT</small><strong>400+</strong><span>piezas desarrolladas.</span></div>
          <div><small>PERFORMANCE</small><strong>100+</strong><span>campañas y experimentos ejecutados.</span></div>
          <div><small>PLANES</small><strong>Desde 5 UF</strong><span>+ IVA / mes.</span></div>
        </div>
      </article>
    </div>
  </div>
</section>'''

s, n2 = re.subn(
    r'<section class="lsr-industries-simple" id="industrias">.*?</section>\s*(?=<section class="lsr-band">)',
    showcase + '\n\n',
    s,
    count=1,
    flags=re.S,
)
if n2 != 1:
    raise SystemExit(f'Expected to replace one industry section, replaced {n2}')

# Remove earlier showcase override if script is rerun.
s = re.sub(r'\n?<style id="home-industry-showcase-v1">.*?</style>\n?', '\n', s, flags=re.S)

css = '''
<style id="home-industry-showcase-v1">
.lsr-industry-showcase{padding:112px 0 118px;background:#071022;color:#fff;scroll-margin-top:130px}.lsr-industry-showcase-head{max-width:900px}.lsr-industry-showcase-head h2{margin:14px 0 0;color:#fff;font-size:clamp(42px,4.5vw,62px);line-height:1.03;letter-spacing:-.05em;font-weight:300}.lsr-industry-showcase-head p{max-width:760px;margin:22px 0 0;color:#8D97B3;font-size:14px;line-height:1.75}.lsr-industry-showcase-stack{display:grid;gap:22px;margin-top:54px}.lsr-industry-panel{padding:34px 34px 30px;border:1px solid rgba(138,164,255,.14);border-radius:22px;background:linear-gradient(180deg,rgba(16,27,67,.78),rgba(10,18,48,.94));box-shadow:0 20px 60px rgba(0,0,0,.12)}.lsr-industry-panel-top{display:grid;grid-template-columns:minmax(0,.9fr) minmax(360px,1.1fr);gap:72px;align-items:start}.lsr-industry-panel-copy>small{display:block;color:#62E6D0;font-size:9px;font-weight:800;letter-spacing:.18em}.lsr-industry-panel-copy h3{max-width:620px;margin:18px 0 0;color:#fff;font-size:clamp(30px,3vw,42px);line-height:1.12;letter-spacing:-.04em;font-weight:400}.lsr-industry-panel-copy p{max-width:620px;margin:18px 0 0;color:#99A3BF;font-size:14px;line-height:1.72}.lsr-industry-panel-actions{display:flex;gap:10px;margin-top:26px}.lsr-industry-panel-actions a{min-height:44px;padding:0 18px;border-radius:999px;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;transition:transform .18s ease,background .18s ease,border-color .18s ease}.lsr-industry-panel-actions a:hover{transform:translateY(-2px)}.lsr-industry-panel-actions .is-secondary{border:1px solid rgba(255,255,255,.20);color:#F2F5FF;background:transparent}.lsr-industry-panel-actions .is-secondary:hover{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.32)}.lsr-industry-panel-actions .is-primary{border:1px solid #4057F3;color:#fff;background:#2C43E8}.lsr-industry-panel-actions .is-primary:hover{background:#4259F5}.lsr-industry-panel-label{display:block;margin-bottom:18px;color:#707A9B;font-size:9px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}.lsr-industry-feature-list{display:grid;gap:12px}.lsr-industry-feature-list div{position:relative;min-height:58px;padding:0 18px 0 46px;border:1px solid rgba(138,164,255,.15);border-radius:13px;background:rgba(255,255,255,.025);display:flex;align-items:center;color:#D8DDEF;font-size:13px}.lsr-industry-feature-list div:before{content:"";position:absolute;left:20px;width:7px;height:7px;border-radius:50%;background:#62E6D0}.lsr-industry-panel-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:42px;padding-top:30px;border-top:1px solid rgba(138,164,255,.12)}.lsr-industry-panel-stats>div{min-height:108px;padding-left:18px;border-left:2px solid rgba(98,230,208,.55)}.lsr-industry-panel-stats small{display:block;color:#62E6D0;font-size:8px;font-weight:800;letter-spacing:.16em}.lsr-industry-panel-stats strong{display:block;margin-top:12px;color:#fff;font-size:28px;line-height:1.08;letter-spacing:-.035em;font-weight:500}.lsr-industry-panel-stats span{display:block;margin-top:10px;color:#828DAA;font-size:11px;line-height:1.55}@media(max-width:980px){.lsr-industry-panel-top{grid-template-columns:1fr;gap:34px}.lsr-industry-panel-stats{grid-template-columns:1fr 1fr 1fr;gap:14px}}@media(max-width:620px){.lsr-industry-showcase{padding:68px 0 72px}.lsr-industry-showcase-head h2{font-size:34px}.lsr-industry-showcase-head p{font-size:13px}.lsr-industry-showcase-stack{margin-top:34px;gap:16px}.lsr-industry-panel{padding:24px 20px 22px;border-radius:18px}.lsr-industry-panel-top{gap:28px}.lsr-industry-panel-copy h3{font-size:29px}.lsr-industry-panel-copy p{font-size:13px}.lsr-industry-panel-actions{display:grid;grid-template-columns:1fr 1fr}.lsr-industry-panel-actions a{width:100%}.lsr-industry-feature-list div{min-height:52px;padding-left:42px;font-size:12px}.lsr-industry-panel-stats{grid-template-columns:1fr;margin-top:30px;padding-top:24px;gap:18px}.lsr-industry-panel-stats>div{min-height:0;padding-left:14px}.lsr-industry-panel-stats strong{font-size:24px}}
</style>
'''

s = s.replace('</head>', css + '</head>', 1)
p.write_text(s, encoding='utf-8')
print('Home industry showcase applied')
