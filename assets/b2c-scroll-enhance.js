document.addEventListener('DOMContentLoaded',()=>{
  const style=document.createElement('style');
  style.id='b2c-scroll-enhance-style';
  style.textContent=`
    html{scroll-behavior:smooth}
    body{overflow-x:hidden}
    #planes-b2c,[id]{scroll-margin-top:118px}
    .b2c-scroll-reveal{opacity:0;transform:translateY(22px);transition:opacity .55s ease,transform .55s ease;will-change:opacity,transform}
    .b2c-scroll-reveal.is-visible{opacity:1;transform:none}
    .b2c-growth-step.b2c-scroll-reveal{transform:translateY(16px)}
    .b2c-growth-step.b2c-scroll-reveal.is-visible{transform:none}
    .b2cr-plan,.b2c-mobile-plan,.b2cr-custom,.b2c-compare,.b2c-growth-method{max-width:100%;min-width:0}
    @media(max-width:760px){
      html,body{width:100%;max-width:100%;overflow-x:hidden!important}
      #planes-b2c,[id]{scroll-margin-top:96px}
      .b2c-scroll-reveal{transform:translateY(16px)}
    }
    @media(prefers-reduced-motion:reduce){
      html{scroll-behavior:auto}
      .b2c-scroll-reveal{opacity:1!important;transform:none!important;transition:none!important}
    }
  `;
  if(!document.getElementById(style.id))document.head.appendChild(style);

  const targets=[
    ...document.querySelectorAll('.b2c-growth-method,.b2c-growth-step,#planes-b2c .b2cr-pricing-head,#planes-b2c .b2cr-plan,#planes-b2c .b2c-compare,#planes-b2c .b2cr-custom')
  ];
  const unique=[...new Set(targets)];
  const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce||!('IntersectionObserver' in window)){
    unique.forEach(el=>el.classList.add('b2c-scroll-reveal','is-visible'));
  }else{
    unique.forEach(el=>el.classList.add('b2c-scroll-reveal'));
    const io=new IntersectionObserver(entries=>{
      entries.forEach(entry=>{
        if(entry.isIntersecting){
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    },{threshold:.12,rootMargin:'0px 0px -6% 0px'});
    unique.forEach((el,i)=>{
      el.style.transitionDelay=`${Math.min((i%4)*55,165)}ms`;
      io.observe(el);
    });
  }

  document.addEventListener('click',e=>{
    const a=e.target.closest('a[href^="#"]');
    if(!a)return;
    const href=a.getAttribute('href');
    if(!href||href==='#')return;
    const target=document.querySelector(href);
    if(!target)return;
    e.preventDefault();
    const nav=document.querySelector('.nav-wrap,.nav');
    const offset=(nav?.getBoundingClientRect().height||76)+28;
    const top=target.getBoundingClientRect().top+window.scrollY-offset;
    window.scrollTo({top,behavior:reduce?'auto':'smooth'});
    history.replaceState(null,'',href);
  });
});
