document.addEventListener('DOMContentLoaded',()=>{const style=document.createElement('link');style.rel='stylesheet';style.href='https://lowsignal.cl/assets/b2b-pricing-enhance.css?v=8';document.head.appendChild(style);const align=document.createElement('link');align.rel='stylesheet';align.href='https://lowsignal.cl/assets/b2b-pricing-align-v7.css?v=2';document.head.appendChild(align);const pricing=document.querySelector('.pricing');const plans=[...document.querySelectorAll('.pricing-grid .plan')];const names=['Presence','Growth','Scale'];const pricingPlans=plans;
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
    plan.querySelector('.plan-cta')?.remove();
    plan.querySelector('.plan-value')?.remove();
    plan.querySelector('.plan-includes')?.remove();
    const price=plan.querySelector('.price');
    if(price&&!plan.querySelector('.choose-plan')){
      const a=document.createElement('a');a.className='choose-plan';
      a.href='https://calendly.com/felipe-lowsignal/30min';a.target='_blank';a.rel='noopener noreferrer';
      a.textContent=`Elegir ${names[i]} →`;plan.appendChild(a);
    }else if(plan.querySelector('.choose-plan'))plan.appendChild(plan.querySelector('.choose-plan'));
    decorateBenefits(plan);
  });const pHead=document.querySelector('.pricing .section-title');const pCopy=document.querySelector('.pricing .section-copy');const custom=document.querySelector('.custom');if(custom){const label=custom.querySelector('span'),title=custom.querySelector('h3'),copy=custom.querySelector('p'),cta=custom.querySelector('a');if(label)label.textContent='PLAN A MEDIDA';if(title)title.textContent='¿No encajas en estos planes?';if(copy)copy.textContent='Armamos un alcance a tu medida según tus objetivos, equipo y etapa de crecimiento.';if(cta)cta.textContent='Diseñemos tu plan →'}const compareHead=document.querySelector('.compare-head');if(compareHead){compareHead.innerHTML=`<div><p class="compare-kicker">COMPARA LOS PLANES</p><h3>Todo lo que incluye <strong>cada plan.</strong></h3></div>`}const table=document.querySelector('.compare-table'),wrap=document.querySelector('.compare-plans');if(table&&wrap&&!wrap.querySelector('.compare-mobile')){const heads=[...table.querySelectorAll('thead th')].slice(1);const mobile=document.createElement('div');mobile.className='compare-mobile';mobile.setAttribute('aria-label','Comparación de planes B2B en móvil');heads.forEach((head,idx)=>{const card=document.createElement('article');card.className='compare-mobile-plan'+(idx===1?' featured-mobile':'');const name=head.querySelector('.compare-plan-name')?.textContent?.trim()||names[idx];const price=head.querySelector('.compare-plan-price')?.textContent?.trim()||'';card.innerHTML=`<div class="compare-mobile-head"><div><strong>${name}</strong><span>${price}</span></div>${idx===1?'<span class="compare-mobile-badge">RECOMENDADO</span>':''}</div>`;let currentGroup=null;[...table.querySelectorAll('tbody tr')].forEach(row=>{if(row.classList.contains('compare-category')){currentGroup=document.createElement('div');currentGroup.className='compare-mobile-group';const b=document.createElement('b');b.textContent=row.textContent.trim();currentGroup.appendChild(b);card.appendChild(currentGroup);return}const cells=[...row.querySelectorAll('td')];if(!cells.length)return;if(!currentGroup){currentGroup=document.createElement('div');currentGroup.className='compare-mobile-group';card.appendChild(currentGroup)}const r=document.createElement('div');r.className='compare-mobile-row';const label=document.createElement('span');label.textContent=cells[0].textContent.trim();const value=document.createElement('span');value.textContent=(cells[idx+1]?.textContent||'—').trim();r.append(label,value);currentGroup.appendChild(r)});mobile.appendChild(card)});const scroller=wrap.querySelector('.compare-scroll');scroller.insertAdjacentElement('afterend',mobile)}});