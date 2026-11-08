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
`;

 trust.after(block);
 // Restore the three original industry showcases (including their proven
 // content, features, plan links and figures) instead of duplicating solutions.
 const originalIndustries=Array.from(home.querySelectorAll('.low-industry-section'));
 const ecosystem=block.querySelector('.low26-system');
 if(ecosystem && originalIndustries.length===3){
   ecosystem.after(...originalIndustries);
   originalIndustries.forEach((section,i)=>{
     section.classList.add('low27-industry-showcase');
     const labels=['EDUCATION','B2B','B2C'];
     section.setAttribute('aria-label','Soluciones para '+labels[i]);
   });
 }
 for(const el of home.querySelectorAll('.lsr-strip,.lsr-mission'))el.remove();
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