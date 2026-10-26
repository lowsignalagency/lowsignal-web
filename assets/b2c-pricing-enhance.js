document.addEventListener('DOMContentLoaded',()=>{
  const style=document.createElement('link');
  style.rel='stylesheet';
  style.href='https://lowsignal.cl/assets/b2c-pricing-enhance.css?v=2';
  document.head.appendChild(style);

  const pricing=document.querySelector('#planes-b2c');
  if(!pricing)return;

  if(!document.querySelector('.b2c-growth-method')){
    const method=document.createElement('section');
    method.className='b2c-growth-method';
    method.innerHTML=`<div class="b2c-growth-shell"><div class="b2c-growth-intro"><p class="b2c-growth-kicker">CÓMO TRABAJAMOS</p><h2>Una estrategia que acompaña <strong>todo el ciclo de compra.</strong></h2><p>Partimos por entender cómo te descubren, por qué te eligen y qué mueve una acción. Desde ahí conectamos marca, contenido, performance, conversión y seguimiento.</p></div><div class="b2c-growth-flow"><div class="b2c-growth-step"><span>01</span><div><h3>Entendemos la oportunidad</h3><p>Marca, tráfico, reservas, ventas, recurrencia o una campaña específica.</p></div></div><div class="b2c-growth-step"><span>02</span><div><h3>Diseñamos el sistema</h3><p>Definimos mensajes, canales, contenido, campañas y puntos de conversión.</p></div></div><div class="b2c-growth-step"><span>03</span><div><h3>Ejecutamos</h3><p>Contenido, Ads, promociones, web y seguimiento trabajando coordinados.</p></div></div><div class="b2c-growth-step"><span>04</span><div><h3>Medimos y ajustamos</h3><p>Revisamos señales reales y reforzamos lo que mueve atención, intención y acción.</p></div></div></div></div>`;
    pricing.insertAdjacentElement('beforebegin',method);
  }

  const title=pricing.querySelector('.b2cr-pricing-head h2');
  const copy=pricing.querySelector('.b2cr-pricing-head>p');
  if(title)title.innerHTML='Tres niveles. <strong>Un mismo enfoque.</strong>';
  if(copy)copy.textContent='Desde mantener una presencia B2C consistente hasta conectar contenido, performance, web y automatización en un sistema más completo.';

  const plans=[...pricing.querySelectorAll('.b2cr-pricing-grid .b2cr-plan')];
  const names=['Presence','Growth','Scale'];
  const values=['Presencia y contenido para mantener tu marca activa','Contenido + performance para mover tráfico y conversión','Sistema conectado de marketing, web y automatización'];
  const includes=['Base de presencia B2C','Incluye todo lo de Presence','Incluye todo lo de Growth'];

  plans.forEach((plan,i)=>{
    const old=plan.querySelector(':scope > a');
    if(old)old.remove();
    const price=plan.querySelector('.price');
    const list=plan.querySelector('ul');
    if(price&&!plan.querySelector('.b2c-plan-value')){
      const value=document.createElement('div');
      value.className='b2c-plan-value';
      value.textContent=values[i];
      price.insertAdjacentElement('beforebegin',value);
    }
    if(price&&!plan.querySelector('.b2c-choose-plan')){
      const a=document.createElement('a');
      a.className='b2c-choose-plan';
      a.href='https://calendly.com/felipe-lowsignal/30min';
      a.target='_blank';
      a.rel='noopener noreferrer';
      a.textContent=`Elegir ${names[i]} →`;
      price.insertAdjacentElement('afterend',a);
    }
    if(list&&!plan.querySelector('.b2c-includes')){
      const band=document.createElement('div');
      band.className='b2c-includes';
      band.innerHTML=`<span>✓</span>${includes[i]}`;
      list.insertAdjacentElement('beforebegin',band);
    }
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
  cmp.innerHTML=`<div class="b2c-compare-head"><div><p class="b2c-growth-kicker">COMPARA LOS PLANES</p><h3>Compara los planes en detalle</h3></div><p>Una vista clara para entender qué cambia entre Presence, Growth y Scale.</p></div><div class="b2c-compare-desktop"><table><thead><tr><th>Incluye</th><th>Presence<br><span>5 UF + IVA / mes</span></th><th class="featured">Growth<br><span>8 UF + IVA / mes</span><em>RECOMENDADO</em></th><th>Scale<br><span>11 UF + IVA / mes</span></th></tr></thead><tbody><tr class="group"><td colspan="4">CONTENIDO & PRESENCIA</td></tr><tr><td>Jornadas de contenido al año</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Reels o videos mensuales</td><td>1</td><td>4</td><td>6</td></tr><tr><td>Posts o carruseles mensuales</td><td>4</td><td>6</td><td>8</td></tr><tr><td>Stories mensuales</td><td>Hasta 4</td><td>Hasta 8</td><td>Hasta 12</td></tr><tr><td>Gestión de redes sociales</td><td>✓</td><td>✓</td><td>✓</td></tr><tr class="group"><td colspan="4">ADS & PERFORMANCE</td></tr><tr><td>Gestión de Ads</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Campañas activas</td><td>Hasta 1</td><td>Hasta 3</td><td>Hasta 4</td></tr><tr><td>Optimización continua</td><td>—</td><td>✓</td><td>✓</td></tr><tr><td>Campañas promocionales o estacionales</td><td>—</td><td>✓</td><td>✓</td></tr><tr class="group"><td colspan="4">WEB & CONVERSIÓN</td></tr><tr><td>Soporte web prioritario</td><td>—</td><td>—</td><td>✓</td></tr><tr class="group"><td colspan="4">AUTOMATIZACIÓN & SEGUIMIENTO</td></tr><tr><td>Automatizaciones y seguimiento</td><td>—</td><td>—</td><td>Según alcance</td></tr><tr class="group"><td colspan="4">ESTRATEGIA & REPORTING</td></tr><tr><td>Planificación mensual</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Reporte mensual</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Insights y próximos pasos</td><td>—</td><td>✓</td><td>✓</td></tr><tr><td>Dashboard</td><td>—</td><td>—</td><td>✓</td></tr><tr><td>Revisión estratégica</td><td>—</td><td>—</td><td>✓</td></tr></tbody></table></div><div class="b2c-compare-mobile" aria-label="Comparación de planes B2C en móvil"></div><div class="b2c-compare-meta"><strong>Planes y valores vigentes · 2026</strong><span>Inversión publicitaria y servicios de terceros no incluidos.</span></div>`;

  const note=pricing.querySelector('.b2cr-note');
  (note||custom).insertAdjacentElement('beforebegin',cmp);

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
});