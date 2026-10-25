from pathlib import Path
import re

reference = Path('casos/rech.html').read_text(encoding='utf-8')
target = Path('casos/gets.html')

# Use a current editorial case as the shell so GETS inherits the exact same
# navbar, footer, responsive rules, spacing and editorial case system.
html = reference
html = re.sub(r'<title>.*?</title>', '<title>GETS | Customer Story | lowsignal</title>', html, count=1, flags=re.S)

main = r'''<main id="top" class="rechx">
  <section class="rechx-hero">
    <div class="container rechx-wrap">
      <div class="rechx-hero-grid">
        <div class="rechx-hero-copy">
          <div class="rechx-kicker">CUSTOMER STORY <span>·</span> B2B</div>
          <h1>Hacer visible lo que construyen.<br><strong>Convertir experiencia técnica en confianza.</strong></h1>
          <p>Ayudamos a GETS a traducir su trabajo técnico en una presencia digital más clara, consistente y útil para generar confianza y apoyar nuevas oportunidades comerciales.</p>
          <div class="rechx-meta">
            <div><span>CLIENTE</span><b>GETS</b></div>
            <div><span>TRABAJO</span><b>Social Media · Paid Media</b></div>
          </div>
        </div>
        <div class="rechx-logo-card">
          <img src="https://lowsignal.cl/assets/gets-logo-white.svg" alt="GETS">
          <p>Contenido y campañas para mostrar proyectos reales, explicar una propuesta técnica y fortalecer la presencia comercial de la marca.</p>
        </div>
      </div>
      <figure class="rechx-cover"><img src="https://lowsignal.cl/assets/gets-ninos.png" alt="GETS — Customer Story"></figure>
    </div>
  </section>

  <section class="case-editorial">
    <div class="container rechx-wrap case-editorial-grid">
      <aside class="case-editorial-aside">
        <div class="case-editorial-client">
          <img src="https://lowsignal.cl/assets/gets-logo-white.svg" alt="GETS">
          <h3>GETS</h3>
        </div>
        <div class="case-editorial-meta">
          <div><span>OBJETIVO</span><p>Hacer más visible el trabajo de GETS y convertir su experiencia técnica en contenido que genere confianza y apoye al equipo comercial.</p></div>
          <div><span>TRABAJO</span><p>Social Media · Paid Media</p></div>
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
          <h2>Mucho trabajo técnico.<br>Una marca que debía <strong>mostrarlo mejor.</strong></h2>
          <p class="case-editorial-lead">GETS necesitaba llevar una propuesta técnica a un lenguaje digital más claro. El desafío era mostrar proyectos reales, explicar mejor su experiencia y construir una presencia que ayudara a generar confianza antes de una conversación comercial.</p>
          <figure class="case-editorial-media"><img src="https://lowsignal.cl/assets/gets-ig.jpg" alt="Contenido digital de GETS"></figure>
        </section>

        <section class="case-editorial-block" id="case-finding">
          <div class="case-editorial-number">01</div>
          <h3>Experiencia real, pero difícil de leer desde afuera.</h3>
          <p class="case-editorial-copy">La empresa tenía proyectos, conocimiento y capacidad técnica, pero sus canales digitales no mostraban ese valor con suficiente claridad para nuevos decisores y potenciales clientes.</p>
        </section>

        <section class="case-editorial-block" id="case-build">
          <div class="case-editorial-number">02</div>
          <h3>Contenido que explica. Campañas que amplifican.</h3>
          <p class="case-editorial-copy">Construimos una línea de contenido basada en proyectos reales y la conectamos con campañas pagadas para llevar el trabajo de GETS frente a audiencias relevantes, haciendo la propuesta más entendible y visible.</p>
          <div class="case-editorial-pair">
            <figure><img src="https://lowsignal.cl/assets/gets-ig.jpg" alt="Social Media de GETS"></figure>
            <figure><img src="https://lowsignal.cl/assets/gets-bg.jpg" alt="Proyecto de GETS"></figure>
          </div>
          <div class="case-editorial-callout"><span>Social Media · Paid Media</span><h4>Proyectos reales convertidos en contenido útil para vender mejor.</h4><p>El sistema conecta experiencia técnica, contenido y distribución para que la marca no solo se vea más activa: se entienda mejor y respalde el trabajo comercial.</p></div>
        </section>

        <section class="case-editorial-block" id="case-result">
          <div class="case-editorial-number">03</div>
          <div class="case-editorial-result">
            <p class="case-editorial-eyebrow">LA TRANSFORMACIÓN</p>
            <h3>Una marca más visible, clara y <strong>útil para generar confianza.</strong></h3>
            <p class="case-editorial-copy">El resultado fue una presencia digital que muestra mejor lo que GETS construye, explica con más claridad su propuesta y entrega al equipo comercial un respaldo de marca más consistente.</p>
          </div>
        </section>
      </div>
    </div>
  </section>

  <section class="rechx-quote">
    <div class="container rechx-wrap rechx-quote-inner">
      <div class="rechx-quote-mark">“</div>
      <blockquote>lowsignal se ha convertido en un aliado estratégico. Entendieron nuestra visión y se involucraron de verdad en el proyecto.</blockquote>
      <div class="rechx-person"><span><img src="https://lowsignal.cl/assets/nicolas-munoz.jpg" alt="Nicolás Muñoz"></span><div><b>Nicolás Muñoz</b><span>Director, GETS</span></div></div>
    </div>
  </section>

  <section class="rechx-next">
    <div class="container rechx-wrap">
      <div class="rechx-next-head"><div><div class="rechx-eyebrow">SIGUIENTE CASO</div><h2>Más trabajo.<br>Menos promesas.</h2></div><a href="https://lowsignal.cl/casos">Ver todos los casos</a></div>
      <a class="rechx-next-card" href="https://lowsignal.cl/casos/dimor"><img src="https://lowsignal.cl/assets/dimor-concesionario.png" alt="Dimor"><div class="rechx-next-overlay"></div><div class="rechx-next-copy"><span>B2B · CUSTOMER STORY</span><h3>Dimor</h3><b>Ver caso ↗</b></div></a>
    </div>
  </section>

  <section class="lsr-band"><div class="lsr-wrap lsr-band-inner"><p>¿Construimos lo que viene?</p><a href="https://calendly.com/felipe-lowsignal/30min" target="_blank" rel="noopener noreferrer">Hablemos</a></div></section>
</main>'''

html, n = re.subn(r'<main id="top" class="rechx">[\s\S]*?</main>', main, html, count=1)
if n != 1:
    raise SystemExit('Could not replace current editorial main block')

# GETS should use the current naming in the industry navbar too.
html = html.replace('lowsignal for education', 'lowsignal for Education')

target.write_text(html, encoding='utf-8')
print('updated', target)
