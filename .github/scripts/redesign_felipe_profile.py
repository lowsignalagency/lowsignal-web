from pathlib import Path
import re

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')

profile_markup = r'''
    <section class="fq-profile" aria-label="Perfil de Felipe Quiroz">
      <div class="fq-shell">
        <a class="fq-back" href="https://lowsignal.cl/nosotros">← Volver al equipo</a>

        <div class="fq-hero-grid">
          <div class="fq-photo-wrap">
            <img class="fq-photo" src="https://lowsignal.cl/assets/team_felipe-1.png" alt="Felipe Quiroz">
            <div class="fq-photo-note">Santiago, Chile · LATAM</div>
          </div>

          <div class="fq-hero-copy">
            <div class="fq-kicker">CO-FOUNDER & COO · LOWSIGNAL</div>
            <h1>Felipe<br><span>Quiroz.</span></h1>
            <p class="fq-positioning">Producto, growth y operaciones para convertir problemas complejos en <strong>sistemas que escalan.</strong></p>
            <p class="fq-summary">Lidera estrategia de negocio, operaciones y nuevas iniciativas en lowsignal, conectando desarrollo comercial, producto digital, automatización e inteligencia artificial.</p>

            <div class="fq-links" aria-label="Enlaces de Felipe">
              <a href="https://www.linkedin.com/in/felipequirozp" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
              <a href="https://felipequirozp.cl" target="_blank" rel="noopener noreferrer">Website ↗</a>
              <a href="https://github.com/felipequirozp" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
            </div>
          </div>
        </div>

        <div class="fq-track" aria-label="Track record">
          <article><strong>USD 40K+</strong><span>oportunidades comerciales desde iniciativas de producto</span></article>
          <article><strong>+50% YoY</strong><span>crecimiento en revenue de nuevos productos</span></article>
          <article><strong>14+</strong><span>partnerships estratégicos desarrollados</span></article>
          <article><strong>20K+</strong><span>familias alcanzadas por iniciativas educativas</span></article>
        </div>
      </div>
    </section>

    <section class="fq-about">
      <div class="fq-shell fq-about-grid">
        <div>
          <div class="fq-eyebrow">ABOUT</div>
          <h2>Opera donde negocio, producto y tecnología <span>se encuentran.</span></h2>
        </div>
        <div class="fq-about-copy">
          <p>Su trayectoria cruza B2B SaaS, EdTech, GovTech y growth. Ha trabajado desde discovery y construcción de producto hasta expansión comercial, partnerships y sistemas de crecimiento.</p>
          <p>Su foco está en conectar señales de negocio con ejecución: entender el problema, ordenar prioridades, construir rápido y convertir aprendizaje en decisiones.</p>
        </div>
      </div>
    </section>

    <section class="fq-experience">
      <div class="fq-shell">
        <div class="fq-section-head">
          <div class="fq-eyebrow">EXPERIENCE</div>
          <h2>Track record.</h2>
          <p>Roles donde estrategia, producto y crecimiento tenían que convertirse en ejecución real.</p>
        </div>

        <div class="fq-timeline">
          <article class="fq-role">
            <div class="fq-role-index">01</div>
            <div class="fq-role-meta"><b>lowsignal</b><span>Co-Founder & COO</span><small>Growth Systems</small></div>
            <div class="fq-role-body">
              <h3>Construir la operación detrás del crecimiento.</h3>
              <p>Lidera estrategia comercial, operaciones, entrega y nuevas iniciativas, conectando marketing, producto, automatización e IA en sistemas de crecimiento para clientes.</p>
            </div>
          </article>

          <article class="fq-role">
            <div class="fq-role-index">02</div>
            <div class="fq-role-meta"><b>GeoVictoria</b><span>Product Manager</span><small>B2B SaaS · Workforce Management</small></div>
            <div class="fq-role-body">
              <h3>Discovery enterprise convertido en producto y revenue.</h3>
              <p>Lideró pilotos y nuevas iniciativas de producto junto a Engineering, Design, Sales y Customer Success, generando USD 40K+ en oportunidades comerciales y contribuyendo a un +50% YoY en revenue de nuevos productos.</p>
            </div>
          </article>

          <article class="fq-role">
            <div class="fq-role-index">03</div>
            <div class="fq-role-meta"><b>Tether Education</b><span>Head of Partnerships</span><small>EdTech · GovTech · LATAM / US / EU</small></div>
            <div class="fq-role-body">
              <h3>Partnerships y expansión en mercados complejos.</h3>
              <p>Impulsó expansión internacional y 14+ partnerships estratégicos con gobiernos, instituciones educacionales y compañías tecnológicas, con iniciativas que alcanzaron a 20.000+ familias.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="fq-expertise">
      <div class="fq-shell">
        <div class="fq-section-head fq-section-head-light">
          <div class="fq-eyebrow">EXPERTISE</div>
          <h2>De la estrategia a <span>la ejecución.</span></h2>
        </div>
        <div class="fq-expertise-grid">
          <article><span>/ 01</span><h3>Growth & Strategy</h3><p>Prioridades, modelos de crecimiento, posicionamiento y sistemas comerciales.</p></article>
          <article><span>/ 02</span><h3>Product</h3><p>Discovery, validación, roadmap, pilotos enterprise y coordinación cross-functional.</p></article>
          <article><span>/ 03</span><h3>Operations</h3><p>Procesos, automatización, métricas y estructuras para hacer que la ejecución escale.</p></article>
          <article><span>/ 04</span><h3>AI & Automation</h3><p>IA aplicada a producto, workflows y herramientas internas con foco en utilidad real.</p></article>
        </div>
      </div>
    </section>

    <section class="fq-selected">
      <div class="fq-shell fq-selected-grid">
        <div>
          <div class="fq-eyebrow">SELECTED WORK</div>
          <h2>Problemas en los que ha trabajado.</h2>
        </div>
        <div class="fq-selected-list">
          <div><b>B2B SaaS</b><span>Producto enterprise, pilotos, adopción y revenue.</span></div>
          <div><b>Education & GovTech</b><span>Admisión, expansión, alianzas y transformación digital.</span></div>
          <div><b>Growth Systems</b><span>Marketing, operaciones, CRM, automatización y datos.</span></div>
          <div><b>AI Products</b><span>Prototipos, asistentes, workflows y nuevas capacidades digitales.</span></div>
        </div>
      </div>
    </section>
'''

pattern = re.compile(r'\s*<section class="profile-hero">.*?</section>\s*(?=<section class="lsr-band" id="contacto">)', re.S)
if not pattern.search(s):
    raise SystemExit('profile hero block not found')
s = pattern.sub('\n' + profile_markup + '\n', s, count=1)

style_id = 'felipe-founder-profile-v2'
style = r'''
<style id="felipe-founder-profile-v2">
:root{--fq-navy:#070F22;--fq-navy2:#0B1429;--fq-lav:#8AA4FF;--fq-lav2:#A8B8FF;--fq-text:#F6F8FC;--fq-muted:#9CA8C1;--fq-line:rgba(180,196,230,.16)}
.fq-profile,.fq-about,.fq-experience,.fq-expertise,.fq-selected{font-family:"Be Vietnam Pro",system-ui,sans-serif}
.fq-shell{width:min(1220px,calc(100% - 128px));margin:0 auto}
.fq-profile{margin-top:-100px;padding:162px 0 82px;background:radial-gradient(720px 480px at 78% 18%,rgba(138,164,255,.08),transparent 68%),var(--fq-navy);color:var(--fq-text)}
.fq-back{display:inline-flex;margin-bottom:42px;color:#8D99B6;font-size:12px;font-weight:500;transition:.2s ease}.fq-back:hover{color:#fff;transform:translateX(-2px)}
.fq-hero-grid{display:grid;grid-template-columns:minmax(360px,.86fr) minmax(0,1.14fr);gap:76px;align-items:center}
.fq-photo-wrap{position:relative;min-height:610px;border-radius:28px;overflow:hidden;background:#0B1220;border:1px solid rgba(255,255,255,.08);box-shadow:0 30px 80px rgba(0,0,0,.28)}
.fq-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top;filter:grayscale(100%) contrast(1.04)}
.fq-photo-wrap:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 58%,rgba(7,15,34,.78) 100%)}
.fq-photo-note{position:absolute;z-index:2;left:26px;bottom:24px;color:#BBC5D9;font-size:10px;letter-spacing:.12em;text-transform:uppercase}
.fq-kicker,.fq-eyebrow{color:var(--fq-lav);font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase}
.fq-hero-copy h1{margin:20px 0 0;font-size:clamp(64px,7vw,96px);line-height:.92;letter-spacing:-.065em;font-weight:300}.fq-hero-copy h1 span{color:var(--fq-lav2);font-weight:500}
.fq-positioning{max-width:650px;margin:32px 0 0;color:#E8ECF5;font-size:clamp(22px,2.15vw,30px);line-height:1.35;letter-spacing:-.025em;font-weight:300}.fq-positioning strong{color:#fff;font-weight:600}
.fq-summary{max-width:610px;margin:24px 0 0;color:var(--fq-muted);font-size:14px;line-height:1.75}
.fq-links{display:flex;flex-wrap:wrap;gap:10px 24px;margin-top:32px;padding-top:24px;border-top:1px solid var(--fq-line)}.fq-links a{color:#C2CBE0;font-size:11px;font-weight:600}.fq-links a:hover{color:#fff}
.fq-track{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:78px;border-top:1px solid var(--fq-line);border-bottom:1px solid var(--fq-line)}
.fq-track article{padding:28px 28px 30px 0;border-right:1px solid var(--fq-line)}.fq-track article+article{padding-left:28px}.fq-track article:last-child{border-right:0}
.fq-track strong{display:block;color:#fff;font-size:clamp(30px,3vw,44px);letter-spacing:-.055em;font-weight:500}.fq-track span{display:block;max-width:210px;margin-top:8px;color:#8F9AB3;font-size:11px;line-height:1.55}

.fq-about{padding:112px 0;background:#F5F7FB;color:#0D1420}.fq-about-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:110px;align-items:start}.fq-about h2,.fq-section-head h2,.fq-selected h2{margin:18px 0 0;font-size:clamp(42px,4.6vw,62px);line-height:1.04;letter-spacing:-.05em;font-weight:300}.fq-about h2 span,.fq-section-head h2 span{color:#5E73D8;font-weight:500}.fq-about-copy{padding-top:34px}.fq-about-copy p{margin:0 0 22px;color:#53617A;font-size:16px;line-height:1.8}.fq-about-copy p:last-child{margin-bottom:0}

.fq-experience{padding:118px 0 126px;background:#fff}.fq-section-head{max-width:760px}.fq-section-head>p{max-width:600px;margin:20px 0 0;color:#6B7890;font-size:14px;line-height:1.7}.fq-timeline{margin-top:64px;border-top:1px solid #DDE4F0}.fq-role{display:grid;grid-template-columns:70px 260px minmax(0,1fr);gap:34px;padding:34px 0;border-bottom:1px solid #DDE4F0;transition:.22s ease}.fq-role:hover{background:#F9FAFD}.fq-role-index{color:#8393B1;font-size:11px;padding-top:4px}.fq-role-meta b{display:block;color:#101827;font-size:19px}.fq-role-meta span{display:block;margin-top:6px;color:#53617A;font-size:12px}.fq-role-meta small{display:block;margin-top:10px;color:#8490A7;font-size:9px;letter-spacing:.08em;text-transform:uppercase}.fq-role-body h3{margin:0;color:#111A2B;font-size:24px;line-height:1.22;letter-spacing:-.035em;font-weight:400}.fq-role-body p{max-width:690px;margin:12px 0 0;color:#647087;font-size:13px;line-height:1.72}

.fq-expertise{padding:116px 0 124px;background:var(--fq-navy);color:#fff}.fq-section-head-light h2{color:#fff}.fq-section-head-light h2 span{color:var(--fq-lav2)}.fq-expertise-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:58px}.fq-expertise-grid article{min-height:250px;padding:25px 22px;border-top:1px solid rgba(138,164,255,.32);background:rgba(255,255,255,.025);transition:.22s ease}.fq-expertise-grid article:hover{transform:translateY(-4px);background:rgba(255,255,255,.05);border-color:rgba(138,164,255,.65)}.fq-expertise-grid article>span{color:var(--fq-lav);font-size:10px}.fq-expertise-grid h3{margin:48px 0 0;color:#fff;font-size:20px;letter-spacing:-.025em}.fq-expertise-grid p{margin:12px 0 0;color:#9DA9C2;font-size:12px;line-height:1.65}

.fq-selected{padding:108px 0;background:#F5F7FB}.fq-selected-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:90px}.fq-selected-list{border-top:1px solid #D7DFEB}.fq-selected-list>div{display:grid;grid-template-columns:180px 1fr;gap:30px;padding:23px 0;border-bottom:1px solid #D7DFEB}.fq-selected-list b{color:#121A2A;font-size:14px}.fq-selected-list span{color:#647087;font-size:13px;line-height:1.6}

@media(max-width:1050px){.fq-shell{width:calc(100% - 64px)}.fq-hero-grid{grid-template-columns:.9fr 1.1fr;gap:48px}.fq-photo-wrap{min-height:540px}.fq-track{grid-template-columns:repeat(2,1fr)}.fq-track article:nth-child(2){border-right:0}.fq-track article:nth-child(-n+2){border-bottom:1px solid var(--fq-line)}.fq-about-grid,.fq-selected-grid{gap:60px}.fq-expertise-grid{grid-template-columns:repeat(2,1fr)}.fq-role{grid-template-columns:50px 220px 1fr}}
@media(max-width:760px){.fq-shell{width:calc(100% - 40px)}.fq-profile{padding:132px 0 62px}.fq-back{margin-bottom:28px}.fq-hero-grid{grid-template-columns:1fr;gap:34px}.fq-photo-wrap{min-height:480px;border-radius:20px}.fq-hero-copy h1{font-size:64px}.fq-positioning{font-size:22px}.fq-track{grid-template-columns:1fr;margin-top:52px}.fq-track article,.fq-track article+article{padding:22px 0;border-right:0;border-bottom:1px solid var(--fq-line)}.fq-track article:last-child{border-bottom:0}.fq-about,.fq-experience,.fq-expertise,.fq-selected{padding:78px 0}.fq-about-grid,.fq-selected-grid{grid-template-columns:1fr;gap:34px}.fq-about-copy{padding-top:0}.fq-about h2,.fq-section-head h2,.fq-selected h2{font-size:40px}.fq-role{grid-template-columns:34px 1fr;gap:18px;padding:28px 0}.fq-role-body{grid-column:2}.fq-role-body h3{font-size:21px}.fq-expertise-grid{grid-template-columns:1fr;gap:12px}.fq-expertise-grid article{min-height:210px}.fq-selected-list>div{grid-template-columns:1fr;gap:8px}}
</style>
'''

if style_id in s:
    a = s.index(f'<style id="{style_id}">')
    b = s.index('</style>', a) + len('</style>')
    s = s[:a] + style.strip() + s[b:]
else:
    s = s.replace('</head>', style + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('Redesigned Felipe profile')
