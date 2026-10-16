from pathlib import Path
import re

root=Path('.')
source=root/'recursos/insights/6-meses-construyendo-lowsignal.html'
article=root/'recursos/insights/lanzamiento-web-fundacion-crecer-con-todos.html'
insights=root/'recursos/insights.html'
home=root/'index.html'

# --- Create article from current article shell ---
s=source.read_text(encoding='utf-8')
s=s.replace('<title>6 meses construyendo lowsignal | Insights</title>','<title>Lanzamos la nueva web de Fundación Crecer con Todos | Insights</title>',1)

main='''<main>
  <section class="article-new-hero">
    <div class="container">
      <p class="article-new-kicker">LANZAMIENTO · LOW WEB</p>
      <div class="article-new-hero-grid">
        <div>
          <h1>Lanzamos la nueva web de <strong>Fundación Crecer con Todos.</strong></h1>
          <p>Una nueva plataforma digital para mostrar con claridad el impacto de una organización que ha acompañado a más de 80.000 niños y niñas.</p>

          <div class="article-new-meta">
            <span>16 oct, 2026</span>
            <span>Santiago</span>
            <span>3 min de lectura</span>
          </div>
          <div class="article-author">
            <img src="https://lowsignal.cl/assets/team_felipe-1.png" alt="Felipe Quiroz">
            <div><strong>Felipe Quiroz</strong><span>Co-Founder & COO · lowsignal</span></div>
          </div>
        </div>

        <aside class="article-new-result">
          <span>IMPACTO</span>
          <strong>+80.000</strong>
          <p>niños y niñas alcanzados por Fundación Crecer con Todos.</p>
        </aside>
      </div>

      <figure class="article-new-cover">
        <img src="https://lowsignal.cl/assets/lanzamiento-web_fcct.jpg" alt="Lanzamiento de la nueva web de Fundación Crecer con Todos">
      </figure>
    </div>
  </section>

  <section class="article-new-body">
    <div class="container article-new-body-grid">
      <aside class="article-new-sidebar">
        <div class="article-new-side-block">
          <span>TEMAS</span>
          <div class="article-new-tags">
            <b>Educación</b>
            <b>Web</b>
            <b>Impacto</b>
          </div>
        </div>

        <div class="article-new-side-block">
          <span>COMPARTIR</span>
          <div class="article-new-share">
            <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Flowsignal.cl%2Frecursos%2Finsights%2Flanzamiento-web-fundacion-crecer-con-todos" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Flowsignal.cl%2Frecursos%2Finsights%2Flanzamiento-web-fundacion-crecer-con-todos&amp;text=Lanzamos%20la%20nueva%20web%20de%20Fundaci%C3%B3n%20Crecer%20con%20Todos" target="_blank" rel="noopener noreferrer">X</a>
            <a href="https://lowsignal.cl/recursos/insights/lanzamiento-web-fundacion-crecer-con-todos">Copiar link</a>
          </div>
        </div>
      </aside>

      <article class="article-new-content">
        <p class="article-new-lead">Una presencia digital también puede ser parte del impacto. Junto a Fundación Crecer con Todos construimos una web pensada para <strong>contar mejor su misión, ordenar su historia y conectar con su comunidad.</strong></p>

        <p>La Fundación lleva años trabajando para fortalecer los aprendizajes de niños y niñas en Chile. El desafío digital era simple de explicar, pero importante de resolver: que ese trabajo, su alcance y sus programas pudieran entenderse con la misma claridad con la que se viven en terreno.</p>

        <h2>Una web a la altura de su misión</h2>
        <p>Desde lowsignal trabajamos una nueva experiencia digital enfocada en claridad, navegación y contenido. La plataforma organiza la información para que familias, docentes, aliados y organizaciones puedan entender rápidamente qué hace la Fundación, cuál ha sido su impacto y cómo vincularse con su trabajo.</p>

        <div class="article-new-process">
          <article><span>/ 01</span><h3>Claridad primero.</h3><p>Ordenamos la información y la jerarquía de contenidos para hacer la propuesta de la Fundación más fácil de entender.</p></article>
          <article><span>/ 02</span><h3>Impacto visible.</h3><p>Diseñamos una experiencia donde los programas, cifras y resultados tienen un lugar central.</p></article>
          <article><span>/ 03</span><h3>Experiencia consistente.</h3><p>Trabajamos una interfaz responsive y un sistema visual coherente en desktop y mobile.</p></article>
          <article><span>/ 04</span><h3>Una base para crecer.</h3><p>La nueva web queda preparada para seguir incorporando contenidos, proyectos y nuevas historias.</p></article>
        </div>

        <blockquote class="article-new-quote">
          <p>“Entendieron nuestra misión <strong>desde el inicio.</strong>”</p>
          <cite>Valentina Wagenreld — Directora Ejecutiva, Fundación Crecer con Todos</cite>
        </blockquote>

        <h2>Más que un rediseño</h2>
        <p>Para nosotros, construir una web para una organización educativa no se trata solo de renovar su apariencia. Se trata de transformar su presencia digital en una herramienta que ayude a comunicar, generar confianza y amplificar el trabajo que ya está ocurriendo.</p>

        <p>Este lanzamiento es parte de lowsignal for education: nuestra línea de trabajo para instituciones educativas y organizaciones que quieren crecer a través de una mejor presencia digital, captación y tecnología.</p>

        <div class="article-new-signoff">build what’s <strong>next.</strong></div>
      </article>
    </div>
  </section>

  <section class="article-new-more">
    <div class="container">
      <div class="article-new-more-head">
        <div>
          <p>MÁS INSIGHTS</p>
          <h2>Sigue <strong>explorando.</strong></h2>
        </div>
        <a href="https://lowsignal.cl/recursos/insights">Ver todos</a>
      </div>

      <div class="article-new-more-grid">
        <a href="https://lowsignal.cl/recursos/insights/tech-founders-ama">
          <img src="https://lowsignal.cl/assets/tech-founders-ama.jpg" alt="Tech Founders AMA en Buk">
          <div>
            <span>EVENTO · 30 SEP, 2026</span>
            <h3>Tech Founders AMA — escalar tecnología sin perder velocidad</h3>
            <b>Leer más ↗</b>
          </div>
        </a>

        <a href="https://lowsignal.cl/recursos/insights/6-meses-construyendo-lowsignal">
          <img src="https://lowsignal.cl/assets/reunion-oficina2.jpg" alt="6 meses construyendo lowsignal">
          <div>
            <span>LOWSIGNAL · 22 JUL, 2026</span>
            <h3>6 meses construyendo lowsignal</h3>
            <b>Leer más ↗</b>
          </div>
        </a>
      </div>
    </div>
  </section>
</main>'''

s,n=re.subn(r'<main>.*?</main>',main,s,count=1,flags=re.S)
if n!=1:
    raise SystemExit(f'Could not replace article main: {n}')
article.write_text(s,encoding='utf-8')

# --- Update Insights landing: make FCCT the featured story and keep Tech Founders in latest grid ---
i=insights.read_text(encoding='utf-8')
featured='''<a class="insights-new-feature-card" href="https://lowsignal.cl/recursos/insights/lanzamiento-web-fundacion-crecer-con-todos">
        <div class="insights-new-feature-image">
          <img src="https://lowsignal.cl/assets/lanzamiento-web_fcct.jpg" alt="Lanzamiento de la nueva web de Fundación Crecer con Todos">
          <span>DESTACADO</span>
        </div>
        <div class="insights-new-feature-copy">
          <div class="insights-new-meta"><b>LANZAMIENTO</b><span>16 oct, 2026</span><span class="insights-meta-author">Felipe Quiroz</span><span>3 min de lectura</span></div>
          <h2>Nueva web de Fundación Crecer con Todos <em>— una presencia digital a la altura de su impacto.</em></h2>
          <p>Diseñamos una nueva plataforma para mostrar con claridad su misión, sus programas y el impacto de más de 80.000 niños y niñas.</p>
          <div class="insights-new-read">Leer artículo<svg class="insights-arrow-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.5 15.5L15.5 8.5M15.5 8.5H10.5M15.5 8.5V13.5"/></svg></div>
        </div>
      </a>'''
i,n=re.subn(r'<a class="insights-new-feature-card".*?</a>',featured,i,count=1,flags=re.S)
if n!=1:
    raise SystemExit(f'Could not replace Insights featured card: {n}')

tech_card='''        <a class="insights-new-card" href="https://lowsignal.cl/recursos/insights/tech-founders-ama">
          <div class="insights-new-card-image">
            <img src="https://lowsignal.cl/assets/tech-founders-ama.jpg" alt="Tech Founders AMA en Buk">
          </div>
          <div class="insights-new-card-body">
            <div class="insights-new-meta"><b>EVENTO</b><span>30 sep, 2026</span><span class="insights-meta-author">Felipe Quiroz</span><span>4 min</span></div>
            <h3>Tech Founders AMA — escalar tecnología sin perder velocidad</h3>
            <p>Escalabilidad, deuda técnica, liderazgo de ingeniería e IA junto a líderes de Buk, Fintoc y AgendaPro.</p>
            <div class="insights-new-read">Leer más<svg class="insights-arrow-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.5 15.5L15.5 8.5M15.5 8.5H10.5M15.5 8.5V13.5"/></svg></div>
          </div>
        </a>

'''
marker='      <div class="insights-new-cards">\n'
if marker not in i:
    raise SystemExit('Insights cards marker not found')
if 'class="insights-new-card" href="https://lowsignal.cl/recursos/insights/tech-founders-ama"' not in i:
    i=i.replace(marker,marker+tech_card,1)
insights.write_text(i,encoding='utf-8')

# --- Update Home title + newest card ---
h=home.read_text(encoding='utf-8')
h=h.replace('Ideas que estamos <strong>poniendo en práctica.</strong>','Ideas, eventos y <strong>señales de lo que viene.</strong>',1)
section_start=h.find('<section class="home26-insights"')
if section_start==-1:
    raise SystemExit('Home insights section not found')
section_end=h.find('</section>',section_start)
if section_end==-1:
    raise SystemExit('Home insights section end not found')
block=h[section_start:section_end]
new_card='''<a class="home26-insight-card" href="https://lowsignal.cl/recursos/insights/lanzamiento-web-fundacion-crecer-con-todos">
          <figure><img src="https://lowsignal.cl/assets/lanzamiento-web_fcct.jpg" alt="Lanzamiento de la nueva web de Fundación Crecer con Todos" loading="lazy"></figure>
          <div class="home26-insight-meta"><span>LANZAMIENTO</span><b>16 OCT, 2026</b></div>
          <h3>Nueva web de Fundación Crecer con Todos</h3>
          <p>Una plataforma pensada para mostrar su impacto con claridad y conectar con familias, docentes y partners.</p>
          <strong>Leer insight →</strong>
        </a>'''
block2,n=re.subn(r'<a class="home26-insight-card".*?</a>',new_card,block,count=1,flags=re.S)
if n!=1:
    raise SystemExit(f'Could not replace first Home insight card: {n}')
h=h[:section_start]+block2+h[section_end:]
home.write_text(h,encoding='utf-8')

print('Created FCCT launch insight and updated Home + Insights')