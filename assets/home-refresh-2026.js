(()=> {
 const home=document.querySelector('.lsr-home'),trust=document.querySelector('.lsr-trust');
 if(!home||!trust||document.querySelector('.low26-ai'))return;
 const block=document.createElement('div');block.className='low26-new';
 block.innerHTML=`
 <section class="low26-ai" id="lowsignal-ai">
  <div class="lsr-wrap low26-ai-grid">
   <div class="low26-ai-art" aria-hidden="true"><span class="low26-orbit low26-orbit-one"></span><span class="low26-orbit low26-orbit-two"></span><div class="low26-ai-core">low<span>signal</span><b>AI</b></div><span class="low26-ai-glow"></span></div>
   <div class="low26-ai-copy"><span class="low26-kicker">INTRODUCING · LOWSIGNAL AI</span><h2>El siguiente paso del crecimiento es <em>inteligente.</em></h2><p>Conectamos agentes de IA, automatizaciones y productos digitales para que tus sistemas trabajen mejor, todos los días.</p><div class="low26-actions"><a class="low26-button" href="/soluciones/low-flow">Descubre Low Flow <span aria-hidden="true">↗</span></a><a class="low26-link" href="/soluciones/low-apps">Explora Low Apps <span aria-hidden="true">↗</span></a></div></div>
  </div>
 </section>
 `;

 trust.after(block);
 // Restore the three original industry showcases (including their proven
 // content, features, plan links and figures) instead of duplicating solutions.
 const originalIndustries=Array.from(home.querySelectorAll('.low-industry-section'));
 if(originalIndustries.length===3){
   block.after(...originalIndustries);
   originalIndustries.forEach((section,i)=>{
     section.classList.add('low27-industry-showcase');
     const labels=['EDUCATION','B2B','B2C'];
     section.setAttribute('aria-label','Soluciones para '+labels[i]);
     if(i<=2){
       const classes=['low28-education-preview','low28-b2b-preview','low28-b2c-preview'];
       const titles=['01 / EDUCACIÓN','02 / B2B','03 / B2C'];
       section.classList.add(classes[i]);
       const eyebrow=section.querySelector('.low-industry-copy>small');
       if(eyebrow)eyebrow.textContent=titles[i];
       const mainAction=section.querySelector('.low-btn-secondary');
       if(mainAction)mainAction.textContent='Explorar industria';
     }
   });
 }
 for(const el of home.querySelectorAll('.lsr-strip,.lsr-mission'))el.remove();
 for(const el of home.querySelectorAll('.lsr-band'))if(!el.querySelector('a[href*="calendly"]'))el.remove();
 const stories=home.querySelector('.lsr-testimonials');if(stories)stories.classList.add('low26-testimonials');
 const partners=home.querySelector('.lsr-tech-partners');
 if(partners)partners.classList.add('low27-home-partners');
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
  cta.innerHTML='<div class="lsr-wrap lsr-band-inner lf26-cta-inner"><div class="lf26-cta-copy"><p class="lf26-cta-kicker">LOWSIGNAL · LESS NOISE. MORE GROWTH.</p><h2>¿Construimos lo que viene?</h2><p>Conversemos sobre cómo podemos construir juntos tu próximo proyecto.</p></div><a href="https://lowsignal.cl/contacto">Hablemos <span aria-hidden="true">↗</span></a></div>';
 }
 // Keep pre-existing visitor anchors stable.
 const industryAnchor=document.getElementById('industrias');
 if(industryAnchor)industryAnchor.id='industrias';

})();
/* home-motion-unified-20261108: applied after the DOM reshuffle above. */
(function(){
  function init(){
    var home=document.querySelector('.lsr-home');
    if(!home)return;
    var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var selectors=[
      '.low26-ai .low26-ai-art',
      '.low26-ai .low26-ai-copy',
      '.home26-insights .home26-insights-head',
      '.home26-insights .home26-insight-card figure',
      '.home26-insights .home26-insight-card h3',
      '.lsr-tech-partners .lsr-tech-head',
      '.lsr-tech-partners .lsr-tech-grid',
      '.low26-final-cta .lf26-cta-copy',
      '.low26-final-cta .lf26-cta-inner > a'
    ];
    var items=[];
    selectors.forEach(function(selector){
      document.querySelectorAll(selector).forEach(function(el){
        if(!items.includes(el))items.push(el);
      });
    });
    if(reduced || !('IntersectionObserver' in window))return;
    var observer=new IntersectionObserver(function(entries,obs){
      entries.forEach(function(entry){
        if(!entry.isIntersecting)return;
        entry.target.classList.add('low-home-motion-visible');
        obs.unobserve(entry.target);
      });
    },{threshold:.04,rootMargin:'0px 0px -2% 0px'});
    items.forEach(function(el){
      var rect=el.getBoundingClientRect();
      // Skip content already in the viewport: never flash or hide the opening screen.
      if(rect.top<window.innerHeight&&rect.bottom>0)return;
      el.classList.add('low-home-motion-pending');
      observer.observe(el);
    });
    function revealOnScreen(){
      document.querySelectorAll('.low-home-motion-pending:not(.low-home-motion-visible)').forEach(function(el){
        var rect=el.getBoundingClientRect();
        if(rect.top<window.innerHeight*.99 && rect.bottom>0)el.classList.add('low-home-motion-visible');
      });
      // Safety for prior-generation scroll effects, but never touch inactive carousel slides.
      home.querySelectorAll('.lsr-reveal:not(.lsr-visible)').forEach(function(el){
        if(el.closest('.home-story-v2:not(.is-active)'))return;
        var rect=el.getBoundingClientRect();
        if(rect.top<window.innerHeight*.99&&rect.bottom>0)el.classList.add('lsr-visible');
      });
    }
    window.addEventListener('scroll',revealOnScreen,{passive:true});
    window.addEventListener('resize',revealOnScreen,{passive:true});
    window.addEventListener('pageshow',revealOnScreen);
    requestAnimationFrame(revealOnScreen);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});
  else init();
})();
