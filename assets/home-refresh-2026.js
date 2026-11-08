(()=> {
 const home=document.querySelector('.lsr-home'),trust=document.querySelector('.lsr-trust');
 if(!home||!trust||document.querySelector('.low26-ai'))return;
 const block=document.createElement('div');block.className='low26-new';
 block.innerHTML=`
 <section class="low26-ai" id="lowsignal-ai">
  <div class="lsr-wrap low26-ai-grid">
   <div class="low26-ai-art" aria-hidden="true"><span class="low26-orbit low26-orbit-one"></span><span class="low26-orbit low26-orbit-two"></span><div class="low26-ai-core">low<span>signal</span><b>AI</b></div><span class="low26-ai-glow"></span></div>
   <div class="low26-ai-copy"><span class="low26-kicker">INTRODUCING · LOWSIGNAL AI</span><h2>El siguiente paso del crecimiento es <em>inteligente.</em></h2><p>Conectamos agentes de IA, automatizaciones y productos digitales para que tus sistemas trabajen mejor, todos los días.</p><div class="low26-actions"><a class="low26-button" href="/soluciones/low-flow">Descubre Low AI <span aria-hidden="true">↗</span></a><a class="low26-link" href="/soluciones/low-apps">Explora Low Apps <span aria-hidden="true">↗</span></a></div></div>
  </div>
 </section>
 <section class="low26-system" id="ecosistema"><div class="lsr-wrap"><div class="low26-sectionhead"><span class="low26-kicker">UN SOLO ECOSISTEMA</span><h2>Una forma más inteligente de <em>hacer crecer tu negocio.</em></h2><p>Menos herramientas desconectadas. Más estrategia, creatividad, tecnología y datos trabajando juntos.</p></div><div class="low26-system-panel"><div class="low26-system-copy"><span class="low26-label">GROWTH SYSTEMS</span><h3>Todo conectado. Todo con un propósito.</h3><p>Desde la primera interacción hasta la conversión y la fidelización, diseñamos sistemas para que cada acción aporte al crecimiento.</p><a href="/soluciones/low-scale">Conoce Low Scale <span aria-hidden="true">↗</span></a></div><div class="low26-system-visual" aria-label="Estrategia conectada a contenido, tecnología y resultados"><div class="low26-node low26-node-center">Growth<span>System</span></div><div class="low26-node low26-node-a">Estrategia</div><div class="low26-node low26-node-b">Creatividad</div><div class="low26-node low26-node-c">Tecnología + IA</div><div class="low26-node low26-node-d">Datos</div></div></div></div></section>
 <section class="low26-solutions ls26-featured-solutions" id="soluciones-home"><div class="lsr-wrap"><div class="low26-sectionhead"><span class="low26-kicker">SOLUCIONES</span><h2>Todo lo que necesitas para <em>hacer crecer tu negocio.</em></h2><p>Estrategia, creatividad y tecnología conectadas en un mismo sistema.</p></div><div class="ls26-featured-stack">
<article class="ls26-featured-card "><div class="ls26-featured-copy"><span class="ls26-featured-kicker">01 / CONTENIDO Y COMUNIDAD</span><h3>Contenido que conecta con las personas.</h3><p>Creamos contenido, estrategias sociales y comunidades que transforman la atención en relaciones de valor.</p><a href="/soluciones/low-social" aria-label="Conocer Low Social">Conoce Low Social <span aria-hidden="true">↗</span></a></div><div class="ls26-featured-art ls26-art-low-social" aria-label="Representación conceptual de Low Social"><div class="ls26-social-ui"><div class="ls26-ui-top"><span class="ls26-ui-dot"></span> Social workspace <span>● Publicado</span></div><div class="ls26-social-post"><div class="ls26-post-img"><span>Less noise.<br>More growth.</span></div><div class="ls26-post-lines"><span></span><span></span><span></span></div></div><div class="ls26-social-stat">↗ <strong>Engagement</strong><span>Comunidad en movimiento</span></div></div></div></article>
<article class="ls26-featured-card ls26-image-first"><div class="ls26-featured-copy"><span class="ls26-featured-kicker">02 / CAMPAÑAS Y PERFORMANCE</span><h3>Cada campaña con un objetivo claro.</h3><p>Conectamos creatividad, inversión y datos para convertir oportunidades en resultados medibles.</p><a href="/soluciones/low-ads" aria-label="Conocer Low Ads">Conoce Low Ads <span aria-hidden="true">↗</span></a></div><div class="ls26-featured-art ls26-art-low-ads" aria-label="Representación conceptual de Low Ads"><div class="ls26-ads-ui"><div class="ls26-ui-top"><span class="ls26-ui-dot"></span> Campaign overview <span>● Activa</span></div><div class="ls26-ads-metrics"><div><small>Conversiones</small><strong>↗</strong><span>En crecimiento</span></div><div><small>Optimización</small><strong>AI</strong><span>Datos conectados</span></div></div><div class="ls26-ads-chart"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="ls26-ads-footer"><span>Campañas</span><b>● En seguimiento</b></div></div></div></article>
<article class="ls26-featured-card "><div class="ls26-featured-copy"><span class="ls26-featured-kicker">03 / DISEÑO Y DESARROLLO WEB</span><h3>Experiencias digitales que hacen crecer tu negocio.</h3><p>Diseñamos y desarrollamos sitios rápidos, claros y conectados a tus objetivos de negocio.</p><a href="/soluciones/low-web" aria-label="Conocer Low Web">Conoce Low Web <span aria-hidden="true">↗</span></a></div><div class="ls26-featured-art ls26-art-low-web" aria-label="Representación conceptual de Low Web"><div class="ls26-web-ui"><div class="ls26-ui-top"><span class="ls26-ui-dot"></span> Web experience <span>↗</span></div><div class="ls26-web-preview"><div class="ls26-web-nav"><b>brand.</b><span>Inicio　 Soluciones　 Contacto</span></div><div class="ls26-web-hero"><div><small>BUILT FOR GROWTH</small><strong>Build what’s<br>next.</strong><span class="ls26-web-cta">Conoce más ↗</span></div><div class="ls26-web-shape"></div></div><div class="ls26-web-lines"><i></i><i></i><i></i></div></div></div></div></article>
<article class="ls26-featured-card ls26-image-first"><div class="ls26-featured-copy"><span class="ls26-featured-kicker">04 / IA Y AUTOMATIZACIÓN</span><h3>Deja que los sistemas hagan el trabajo repetitivo.</h3><p>Conectamos herramientas, datos y agentes de IA para automatizar procesos sin perder el control.</p><a href="/soluciones/low-flow" aria-label="Conocer Low Flow">Conoce Low Flow <span aria-hidden="true">↗</span></a></div><div class="ls26-featured-art ls26-art-low-flow" aria-label="Representación conceptual de Low Flow"><div class="ls26-flow-ui"><div class="ls26-ui-top"><span class="ls26-ui-dot"></span> Workflow automation <span>● Activo</span></div><div class="ls26-flow-chain"><div><span>01</span><b>Nuevo lead</b><small>Trigger</small></div><i></i><div class="ls26-flow-active"><span>02</span><b>AI Agent</b><small>Procesar</small></div><i></i><div><span>03</span><b>CRM</b><small>Actualizar</small></div></div><div class="ls26-flow-status"><span>✓</span> Flujo ejecutado correctamente</div></div></div></article>
</div><div class="ls26-more-solutions"><div><span>EL ECOSISTEMA CONTINÚA</span><h3>Todo conectado, de principio a fin.</h3></div><div class="ls26-more-links"><a href="/soluciones/low-scale">Low Scale <span aria-hidden="true">↗</span></a><a href="/soluciones/low-apps">Low Apps <span aria-hidden="true">↗</span></a></div></div></div></section>
 <section class="low26-industries" id="industrias"><div class="lsr-wrap"><div class="low26-sectionhead"><span class="low26-kicker">INDUSTRIAS</span><h2>Cada industria tiene sus desafíos. <em>Nosotros construimos soluciones.</em></h2><p>Experiencia y sistemas de growth adaptados a cada modelo de negocio.</p></div><div class="low26-industries-grid">
 <a href="/industrias/educacion" class="low26-industry-card low26-edu"><div class="low26-industry-art"><img src="/assets/comunidad-rech.jpg" alt="Comunidad educativa" loading="lazy"></div><div class="low26-industry-text"><span>01 / EDUCATION</span><h3>Educación</h3><p>Admisión, posicionamiento y comunidades educativas.</p><b>Explorar industria ↗</b></div></a>
 <a href="/industrias/b2b" id="industria-b2b" class="low26-industry-card low26-b2b"><div class="low26-industry-art"><img src="/assets/galpon-merk.jpg" alt="Proyecto empresarial Rikdom" loading="lazy"></div><div class="low26-industry-text"><span>02 / B2B</span><h3>Empresas</h3><p>Generación de demanda, pipeline y crecimiento comercial.</p><b>Explorar industria ↗</b></div></a>
 <a href="/industrias/marcas-b2c" id="industria-b2c" class="low26-industry-card low26-b2c"><div class="low26-industry-art"><img src="/assets/dulce-reino-pasteleria.jpg" alt="Marca de consumo Dulce Reino" loading="lazy"></div><div class="low26-industry-text"><span>03 / B2C</span><h3>Marcas</h3><p>Contenido, performance y experiencias que convierten.</p><b>Explorar industria ↗</b></div></a>
 </div></div></section>`;
 trust.after(block);
 for(const el of home.querySelectorAll('.lsr-strip,.low-industry-section,.lsr-mission'))el.remove();
 for(const el of home.querySelectorAll('.lsr-band'))if(!el.querySelector('a[href*="calendly"]'))el.remove();
 const stories=home.querySelector('.lsr-testimonials');if(stories)stories.classList.add('low26-testimonials');
 const partners=home.querySelector('.lsr-tech-partners');
 const insights=document.querySelector('.home26-insights');
 const cta=[...home.querySelectorAll('.lsr-band')].find(el=>el.querySelector('a[href*="calendly"]'));
 if(partners&&insights)insights.before(partners);
 if(cta&&insights)insights.after(cta);
 if(cta)cta.classList.add('low26-final-cta');
 if(insights){const eyebrow=insights.querySelector('.home26-eyebrow');if(eyebrow)eyebrow.textContent='BLOG / INSIGHTS';}

 // Match existing Education testimonial treatment: full-bleed stage, one quote at a time.
 const testimonial=home.querySelector('.low26-testimonials');
 if(testimonial){
  const cards=Array.from(testimonial.querySelectorAll('.home-story-v2'));
  const heading=testimonial.querySelector('.home-stories-v2-head');
  if(heading)heading.remove();
  const grid=testimonial.querySelector('.home-stories-v2-grid');
  if(grid){
   grid.classList.add('low26-story-stage');
   cards.forEach((card,i)=>{
    card.classList.toggle('is-active',i===0);
    card.setAttribute('aria-hidden',i===0?'false':'true');
    const panel=card.querySelector('.home-story-v2-panel');
    const person=card.querySelector('.home-story-v2-person');
    if(panel && person && !panel.querySelector('.low26-story-controls')){
      const nav=document.createElement('div');nav.className='low26-story-controls testimonial-controls';
      nav.innerHTML='<button class="testimonial-control testimonial-prev low26-prev" type="button" aria-label="Testimonio anterior"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5 5 12l7 7"/><path d="M5 12h14"/></svg></button><button class="testimonial-control testimonial-next low26-next" type="button" aria-label="Siguiente testimonio"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 5 7 7-7 7"/><path d="M5 12h14"/></svg></button>';
      panel.append(nav);
    }
   });
   let active=0;
   const advance=(dir)=>{active=(active+dir+cards.length)%cards.length;cards.forEach((card,i)=>{card.classList.toggle('is-active',i===active);card.setAttribute('aria-hidden',i===active?'false':'true')});};
   grid.addEventListener('click',(ev)=>{if(ev.target.closest('.low26-prev'))advance(-1);else if(ev.target.closest('.low26-next'))advance(1);});
  }
 }
 // Use the same CTA composition, copy scale, button and destination as Low Web.
 if(cta){
  cta.classList.add('lf26-cta');
  cta.innerHTML='<div class="lsr-wrap lsr-band-inner lf26-cta-inner"><div class="lf26-cta-copy"><p class="lf26-cta-kicker">LOWSIGNAL · LESS NOISE. MORE GROWTH.</p><h2>Construyamos lo que viene. <span>Hagámoslo crecer juntos.</span></h2><p>Conversemos sobre los desafíos y oportunidades de tu negocio.</p></div><a href="https://lowsignal.cl/contacto">Hablemos <span aria-hidden="true">↗</span></a></div>';
 }
 // Keep pre-existing visitor anchors stable.
 const industryAnchor=document.getElementById('industrias');
 if(industryAnchor)industryAnchor.id='industrias';

})();