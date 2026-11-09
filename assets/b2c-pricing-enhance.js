document.addEventListener('DOMContentLoaded',()=>{
  const style=document.createElement('link');
  style.rel='stylesheet';
  style.href='https://lowsignal.cl/assets/b2c-pricing-enhance.css?v=9';
  document.head.appendChild(style);

  const scrollStyle=document.createElement('style');
  scrollStyle.textContent=`html{scroll-behavior:smooth}body{overflow-x:hidden}#planes-b2c,[id]{scroll-margin-top:118px}@media(max-width:760px){#planes-b2c,[id]{scroll-margin-top:96px}}`;
  document.head.appendChild(scrollStyle);

  const pricing=document.querySelector('#planes-b2c');
  if(!pricing)return;

  const title=pricing.querySelector('.b2cr-pricing-head h2');
  const copy=pricing.querySelector('.b2cr-pricing-head>p');



  const plans=[...pricing.querySelectorAll('.b2cr-pricing-grid .b2cr-plan')];
  const names=['Presence','Growth','Scale'];

  const benefitIcons={"camera":"<rect x=\"3\" y=\"6\" width=\"18\" height=\"14\" rx=\"2\"/><path d=\"M8 6l1.5-2h5L16 6\"/><circle cx=\"12\" cy=\"13\" r=\"3\"/>","video":"<rect x=\"3\" y=\"5\" width=\"13\" height=\"14\" rx=\"2\"/><path d=\"m16 10 5-3v10l-5-3\"/>","layers":"<rect x=\"4\" y=\"4\" width=\"16\" height=\"16\" rx=\"2\"/><path d=\"M4 9h16M9 4v16\"/>","story":"<rect x=\"6\" y=\"3\" width=\"12\" height=\"18\" rx=\"2\"/><path d=\"M10 17h4M9 7h6\"/>","social":"<circle cx=\"6\" cy=\"12\" r=\"2\"/><circle cx=\"18\" cy=\"6\" r=\"2\"/><circle cx=\"18\" cy=\"18\" r=\"2\"/><path d=\"m8 11 8-4m-8 6 8 4\"/>","ads":"<path d=\"m3 11 11-5v12L3 14z\"/><path d=\"M7 15l2 5h3l-2-4M17 9a4 4 0 0 1 0 6\"/>","target":"<circle cx=\"12\" cy=\"12\" r=\"9\"/><circle cx=\"12\" cy=\"12\" r=\"5\"/><circle cx=\"12\" cy=\"12\" r=\"1\"/>","calendar":"<rect x=\"3\" y=\"5\" width=\"18\" height=\"16\" rx=\"2\"/><path d=\"M7 3v4m10-4v4M3 10h18\"/>","chart":"<path d=\"M4 20V4m0 16h16M8 15l4-4 3 2 5-7\"/>","web":"<circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18\"/>","workflow":"<rect x=\"2\" y=\"3\" width=\"7\" height=\"6\" rx=\"1\"/><rect x=\"15\" y=\"15\" width=\"7\" height=\"6\" rx=\"1\"/><path d=\"M5.5 9v6h13\"/>","users":"<circle cx=\"9\" cy=\"8\" r=\"3\"/><path d=\"M3 20v-2a6 6 0 0 1 12 0v2M16 5a3 3 0 0 1 0 6m1 4a5 5 0 0 1 4 5\"/>","spark":"<path d=\"m12 2 2.5 7.5L22 12l-7.5 2.5L12 22l-2.5-7.5L2 12l7.5-2.5z\"/>"};
  const iconName=(text)=>{
    const t=text.toLowerCase();
    if(t.includes('jornadas'))return 'camera';
    if(t.includes('reel')||t.includes('video'))return 'video';
    if(t.includes('posts')||t.includes('carrusel'))return 'layers';
    if(t.includes('stories'))return 'story';
    if(t.includes('linkedin')||t.includes('lead generation')||t.includes('prospect'))return 'users';
    if(t.includes('redes sociales'))return 'social';
    if(t.includes('ads'))return 'ads';
    if(t.includes('campaña')||t.includes('admisión'))return 'target';
    if(t.includes('planificación'))return 'calendar';
    if(t.includes('reporte')||t.includes('insight')||t.includes('dashboard')||t.includes('estratégic'))return 'chart';
    if(t.includes('automatiza')||t.includes('seguimiento')||t.includes('crm'))return 'workflow';
    if(t.includes('web')||t.includes('landing'))return 'web';
    return 'spark';
  };
  const decorateBenefits=(plan)=>{
    plan.querySelectorAll('ul > li').forEach(li=>{
      if(li.querySelector('.low-benefit-icon'))return;
      const text=li.textContent.trim();
      const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
      svg.setAttribute('class','low-benefit-icon');
      svg.setAttribute('viewBox','0 0 24 24');
      svg.setAttribute('fill','none');svg.setAttribute('stroke','currentColor');
      svg.setAttribute('stroke-width','1.65');svg.setAttribute('stroke-linecap','round');
      svg.setAttribute('stroke-linejoin','round');svg.setAttribute('aria-hidden','true');
      svg.innerHTML=benefitIcons[iconName(text)];
      const span=document.createElement('span');
      span.textContent=text;
      li.replaceChildren(svg,span);
    });
  };

  plans.forEach((plan,i)=>{
    plan.querySelector(':scope > a:not(.b2c-choose-plan)')?.remove();
    plan.querySelector('.b2c-plan-value')?.remove();
    plan.querySelector('.b2c-includes')?.remove();
    if(!plan.querySelector('.b2c-choose-plan')){
      const a=document.createElement('a');a.className='b2c-choose-plan';
      a.href='https://calendly.com/felipe-lowsignal/30min';a.target='_blank';a.rel='noopener noreferrer';
      a.textContent=`Elegir ${names[i]} →`;plan.appendChild(a);
    }else plan.appendChild(plan.querySelector('.b2c-choose-plan'));
    decorateBenefits(plan);
  });

  const custom=pricing.querySelector('.b2cr-custom');
  if(custom){
    const label=custom.querySelector('span'),h=custom.querySelector('h3'),p=custom.querySelector('p'),a=custom.querySelector('a');
    if(label)label.textContent='PLAN A MEDIDA';
    if(h)h.textContent='¿Tu marca necesita algo distinto?';
    if(p)p.textContent='Armamos un alcance a tu medida según tus objetivos, operación, canales y etapa de crecimiento.';
    if(a)a.textContent='Diseñemos tu plan →';
  }

  pricing.querySelector('.b2c-compare')?.remove();
  const cmp=document.createElement('section');
  cmp.className='b2c-compare';
  cmp.innerHTML=`<div class="b2c-compare-head"><div><p class="b2c-growth-kicker">COMPARA LOS PLANES</p><h3>Todo lo que incluye <span>cada plan.</span></h3></div></div><div class="b2c-compare-desktop"><table><thead><tr><th>Incluye</th><th>Presence<br><span>5 UF + IVA / mes</span></th><th class="featured">Growth<br><span>8 UF + IVA / mes</span><em>RECOMENDADO</em></th><th>Scale<br><span>11 UF + IVA / mes</span></th></tr></thead><tbody><tr class="group"><td colspan="4">CONTENIDO & PRESENCIA</td></tr><tr><td>Jornadas de contenido al año</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Reels o videos mensuales</td><td>1</td><td>4</td><td>6</td></tr><tr><td>Posts o carruseles mensuales</td><td>4</td><td>6</td><td>8</td></tr><tr><td>Stories mensuales</td><td>Hasta 4</td><td>Hasta 8</td><td>Hasta 12</td></tr><tr><td>Gestión de redes sociales</td><td>✓</td><td>✓</td><td>✓</td></tr><tr class="group"><td colspan="4">ADS & PERFORMANCE</td></tr><tr><td>Gestión de Ads</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Campañas activas</td><td>Hasta 1</td><td>Hasta 3</td><td>Hasta 4</td></tr><tr><td>Optimización continua</td><td>—</td><td>✓</td><td>✓</td></tr><tr><td>Campañas promocionales o estacionales</td><td>—</td><td>✓</td><td>✓</td></tr><tr class="group"><td colspan="4">WEB & CONVERSIÓN</td></tr><tr><td>Soporte web prioritario</td><td>—</td><td>—</td><td>✓</td></tr><tr class="group"><td colspan="4">AUTOMATIZACIÓN & SEGUIMIENTO</td></tr><tr><td>Automatizaciones y seguimiento</td><td>—</td><td>—</td><td>Según alcance</td></tr><tr class="group"><td colspan="4">ESTRATEGIA & REPORTING</td></tr><tr><td>Planificación mensual</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Reporte mensual</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Insights y próximos pasos</td><td>—</td><td>✓</td><td>✓</td></tr><tr><td>Dashboard</td><td>—</td><td>—</td><td>✓</td></tr><tr><td>Revisión estratégica</td><td>—</td><td>—</td><td>✓</td></tr></tbody></table></div><div class="b2c-compare-mobile" aria-label="Comparación de planes B2C en móvil"></div><div class="b2c-compare-meta"><span>Valores referenciales 2026 · UF + IVA / mes. Inversión publicitaria y servicios de terceros no incluidos.</span></div>`;

  const note=pricing.querySelector('.b2cr-note');
  if(note)note.remove(); // Comparison includes the consolidated disclaimer, like Education.
  (custom||pricing).insertAdjacentElement('beforebegin',cmp);

  const table=cmp.querySelector('table');
  const mobile=cmp.querySelector('.b2c-compare-mobile');
  const heads=[...table.querySelectorAll('thead th')].slice(1);
  heads.forEach((head,idx)=>{
    const card=document.createElement('article');
    card.className='b2c-mobile-plan'+(idx===1?' featured':'');
    const raw=[...head.childNodes].filter(n=>n.nodeType===Node.TEXT_NODE).map(n=>n.textContent.trim()).filter(Boolean)[0]||names[idx];
    const price=head.querySelector('span')?.textContent?.trim()||'';
    card.innerHTML=`<div class="b2c-mobile-head"><div><h4>${raw}</h4><span>${price}</span></div>${idx===1?'<em>RECOMENDADO</em>':''}</div>`;
    let group=null;
    [...table.querySelectorAll('tbody tr')].forEach(row=>{
      if(row.classList.contains('group')){
        group=document.createElement('div');
        group.className='b2c-mobile-group';
        const b=document.createElement('b');
        b.textContent=row.textContent.trim();
        group.appendChild(b);
        card.appendChild(group);
        return;
      }
      const cells=[...row.querySelectorAll('td')];
      if(!cells.length)return;
      if(!group){group=document.createElement('div');group.className='b2c-mobile-group';card.appendChild(group)}
      const r=document.createElement('div');
      r.className='b2c-mobile-row';
      const label=document.createElement('span');label.textContent=cells[0].textContent.trim();
      const val=document.createElement('span');val.textContent=(cells[idx+1]?.textContent||'—').trim();
      r.append(label,val);group.appendChild(r);
    });
    mobile.appendChild(card);
  });

  const dynamic=[...document.querySelectorAll('.b2c-growth-intro,.b2c-growth-step,#planes-b2c .b2cr-plan,#planes-b2c .b2c-compare,#planes-b2c .b2cr-custom')];
  dynamic.forEach(el=>el.classList.add('b2cr-reveal'));
  if('IntersectionObserver' in window){
    const io=new IntersectionObserver(entries=>entries.forEach(entry=>{
      if(entry.isIntersecting){
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    }),{threshold:.12,rootMargin:'0px 0px -5% 0px'});
    dynamic.forEach(el=>io.observe(el));
  }else{
    dynamic.forEach(el=>el.classList.add('is-visible'));
  }
});