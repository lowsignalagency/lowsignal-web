from pathlib import Path
import re

root=Path('.')
source=root/'recursos/insights/lanzamiento-web-fundacion-crecer-con-todos.html'
article=root/'recursos/insights/lowsignal-se-expande-tres-industrias-un-sistema.html'
insights=root/'recursos/insights.html'
home=root/'index.html'

s=source.read_text(encoding='utf-8')
s=re.sub(r'<title>.*?</title>','<title>lowsignal se expande: tres industrias, un solo sistema | Insights</title>',s,count=1,flags=re.S)

main='''<main>
  <section class="article-new-hero">
    <div class="container">
      <p class="article-new-kicker">WHAT’S NEXT · EXPANSIÓN</p>
      <div class="article-new-hero-grid">
        <div>
          <h1>lowsignal se expande: <strong>tres industrias, un solo sistema.</strong></h1>
          <p>Después de trabajar con instituciones, empresas y marcas, decidimos concentrar nuestro crecimiento donde podemos generar más valor: Educación, B2B y B2C.</p>

          <div class="article-new-meta">
            <span>16 oct, 2026</span>
            <span>Chile</span>
            <span>4 min de lectura</span>
          </div>
          <div class="article-author">
            <img src="https://lowsignal.cl/assets/team_felipe-1.png" alt="Felipe Quiroz">
            <div><strong>Felipe Quiroz</strong><span>Co-Founder & COO · lowsignal</span></div>
          </div>
        </div>

        <aside class="article-new-result">
          <span>NUEVO FOCO</span>
          <strong>3</strong>
          <p>industrias con soluciones especializadas y presencia en todo Chile.</p>
        </aside>
      </div>

      <figure class="article-new-cover">
        <img src="https://lowsignal.cl/assets/founders_new.jpg" alt="Fundadores de lowsignal">
      </figure>
    </div>
  </section>

  <section class="article-new-body">
    <div class="container article-new-body-grid">
      <aside class="article-new-sidebar">
        <div class="article-new-side-block">
          <span>TEMAS</span>
          <div class="article-new-tags">
            <b>Growth</b>
            <b>Expansión</b>
            <b>Education</b>
            <b>B2B</b>
            <b>B2C</b>
          </div>
        </div>

        <div class="article-new-side-block">
          <span>COMPARTIR</span>
          <div class="article-new-share">
            <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Flowsignal.cl%2Frecursos%2Finsights%2Flowsignal-se-expande-tres-industrias-un-sistema" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Flowsignal.cl%2Frecursos%2Finsights%2Flowsignal-se-expande-tres-industrias-un-sistema&amp;text=lowsignal%20se%20expande%3A%20tres%20industrias%2C%20un%20solo%20sistema" target="_blank" rel="noopener noreferrer">X</a>
            <a href="https://lowsignal.cl/recursos/insights/lowsignal-se-expande-tres-industrias-un-sistema">Copiar link</a>
          </div>
        </div>
      </aside>

      <article class="article-new-content">
        <p class="article-new-lead">Crecer también significa elegir dónde poner el foco. Después de trabajar con organizaciones de distintos tamaños e industrias, entendimos con mayor claridad dónde nuestro sistema puede generar <strong>más impacto.</strong></p>

        <p>Hasta ahora construimos junto a colegios, fundaciones, empresas de servicios, tecnología, industria y marcas de consumo. Esa experiencia nos permitió ver algo en común: los desafíos cambian según el negocio, pero la necesidad de conectar estrategia, presencia digital, captación, tecnología y automatización se repite.</p>

        <h2>Más foco. Más impacto.</h2>
        <p>Por eso, la siguiente etapa de lowsignal se organiza en tres verticales. No como tres agencias distintas, sino como tres formas especializadas de aplicar un mismo sistema de growth a problemas diferentes.</p>

        <div class="article-new-process">
          <article>
            <span>/ 01 · EDUCATION</span>
            <h3>lowsignal for Education</h3>
            <p>Colegios, fundaciones y proveedores de educación que quieren atraer familias, fortalecer comunidad y construir una presencia digital que genere confianza.</p>
          </article>
          <article>
            <span>/ 02 · B2B</span>
            <h3>lowsignal for B2B</h3>
            <p>Empresas de servicios, tecnología e industria que quieren convertir presencia digital en oportunidades comerciales, demanda y conversaciones de negocio.</p>
          </article>
          <article>
            <span>/ 03 · B2C</span>
            <h3>lowsignal for B2C</h3>
            <p>Marcas de consumo, locales y experiencias que quieren convertir atención en clientes, recurrencia y relaciones que vuelven.</p>
          </article>
          <article>
            <span>/ SISTEMA</span>
            <h3>Una misma infraestructura de growth</h3>
            <p>Estrategia, contenido, paid media, web, automatización, tecnología e IA conectadas según lo que cada negocio necesita para crecer.</p>
          </article>
        </div>

        <blockquote class="article-new-quote">
          <p><strong>Tres industrias.</strong> Un solo sistema.</p>
          <cite>lowsignal · Less noise. More growth.</cite>
        </blockquote>

        <h2>Especialización sin perder amplitud</h2>
        <p>El objetivo de este cambio no es hacer menos. Es entender mejor. Cuando conocemos con profundidad cómo una institución educativa capta familias, cómo una empresa B2B genera pipeline o cómo una marca B2C convierte atención en recurrencia, podemos diseñar soluciones más precisas y movernos más rápido.</p>

        <p>Seguiremos trabajando desde estrategia hasta ejecución, pero con propuestas, mensajes y sistemas pensados para cada una de estas realidades. Ese foco también nos permite construir conocimiento, procesos y tecnología reutilizable dentro de cada vertical.</p>

        <h2>De Santiago a todo Chile</h2>
        <p>Esta nueva etapa también amplía nuestra forma de operar. Queremos trabajar con organizaciones en todo Chile, combinando un equipo distribuido, una red de partners e Insiders y procesos diseñados para colaborar sin importar la ciudad.</p>

        <p>Education, B2B y B2C son hoy nuestras tres apuestas. El sistema sigue siendo el mismo: menos ruido, más claridad y crecimiento que se pueda sostener.</p>

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
        <a href="https://lowsignal.cl/recursos/insights/lanzamiento-web-fundacion-crecer-con-todos">
          <img src="https://lowsignal.cl/assets/lanzamiento-web_fcct.jpg" alt="Nueva web de Fundación Crecer con Todos">
          <div>
            <span>LANZAMIENTO · 16 OCT, 2026</span>
            <h3>Nueva web de Fundación Crecer con Todos</h3>
            <b>Leer más ↗</b>
          </div>
        </a>

        <a href="https://lowsignal.cl/recursos/insights/tech-founders-ama">
          <img src="https://lowsignal.cl/assets/tech-founders-ama.jpg" alt="Tech Founders AMA en Buk">
          <div>
            <span>EVENTO · 30 SEP, 2026</span>
            <h3>Tech Founders AMA — escalar tecnología sin perder velocidad</h3>
            <b>Leer más ↗</b>
          </div>
        </a>
      </div>
    </div>
  </section>
</main>'''

s,n=re.subn(r'<main[^>]*>.*?</main>',main,s,count=1,flags=re.S)
if n!=1:
    raise SystemExit(f'Could not replace article main: {n}')
article.write_text(s,encoding='utf-8')

# Add newest card to Insights grid (keep FCCT featured)
i=insights.read_text(encoding='utf-8')
card='''        <a class="insights-new-card" href="https://lowsignal.cl/recursos/insights/lowsignal-se-expande-tres-industrias-un-sistema">
          <div class="insights-new-card-image">
            <img src="https://lowsignal.cl/assets/founders_new.jpg" alt="Fundadores de lowsignal">
          </div>
          <div class="insights-new-card-body">
            <div class="insights-new-meta"><b>EXPANSIÓN</b><span>16 oct, 2026</span><span class="insights-meta-author">Felipe Quiroz</span><span>4 min</span></div>
            <h3>lowsignal se expande: tres industrias, un solo sistema</h3>
            <p>Más foco para generar más impacto: Education, B2B y B2C pasan a ser nuestras tres verticales de crecimiento.</p>
            <div class="insights-new-read">Leer más<svg class="insights-arrow-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.5 15.5L15.5 8.5M15.5 8.5H10.5M15.5 8.5V13.5"/></svg></div>
          </div>
        </a>

'''
marker='      <div class="insights-new-cards">\n'
if marker not in i:
    raise SystemExit('Insights grid marker not found')
if 'lowsignal-se-expande-tres-industrias-un-sistema' not in i:
    i=i.replace(marker,marker+card,1)
insights.write_text(i,encoding='utf-8')

# Put expansion into Home as second card, preserving FCCT first
h=home.read_text(encoding='utf-8')
section_start=h.find('<section class="home26-insights"')
if section_start==-1:
    raise SystemExit('Home insights section not found')
section_end=h.find('</section>',section_start)
block=h[section_start:section_end]
if 'lowsignal-se-expande-tres-industrias-un-sistema' not in block:
    first_end=block.find('</a>')
    if first_end==-1:
        raise SystemExit('First Home insight card end not found')
    first_end+=4
    home_card='''

        <a class="home26-insight-card" href="https://lowsignal.cl/recursos/insights/lowsignal-se-expande-tres-industrias-un-sistema">
          <figure><img src="https://lowsignal.cl/assets/founders_new.jpg" alt="Fundadores de lowsignal" loading="lazy"></figure>
          <div class="home26-insight-meta"><span>EXPANSIÓN</span><b>16 OCT, 2026</b></div>
          <h3>lowsignal se expande: tres industrias, un solo sistema</h3>
          <p>Education, B2B y B2C pasan a ser nuestras tres verticales para crecer con más foco y más impacto.</p>
          <strong>Leer insight →</strong>
        </a>'''
    block=block[:first_end]+home_card+block[first_end:]
    # Keep Home at three cards: remove the old last +100 ideas card if now four
    cards=list(re.finditer(r'<a class="home26-insight-card".*?</a>',block,flags=re.S))
    if len(cards)>3:
        m=cards[-1]
        block=block[:m.start()]+block[m.end():]
    h=h[:section_start]+block+h[section_end:]
home.write_text(h,encoding='utf-8')

print('Created expansion insight and updated Insights + Home')