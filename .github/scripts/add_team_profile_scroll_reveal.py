from pathlib import Path

files = [
    Path('equipo/felipe-quiroz.html'),
    Path('equipo/damian-aldunate.html'),
    Path('equipo/matias-bussinger.html'),
    Path('equipo/martin-alvarado.html'),
    Path('equipo/jorge-munoz.html'),
    Path('equipo/lia-morice.html'),
]

marker = 'team-profile-scroll-reveal-v1'

css = r'''
<style id="team-profile-scroll-reveal-v1">
html.js-reveal-ready .team-scroll-reveal{
  opacity:0;
  transform:translateY(24px);
  transition:opacity .7s cubic-bezier(.2,.75,.2,1),transform .7s cubic-bezier(.2,.75,.2,1);
  will-change:opacity,transform;
}
html.js-reveal-ready .team-scroll-reveal.is-visible{
  opacity:1;
  transform:none;
}
html.js-reveal-ready .team-scroll-reveal[data-reveal-delay="1"]{transition-delay:.05s}
html.js-reveal-ready .team-scroll-reveal[data-reveal-delay="2"]{transition-delay:.10s}
@media (prefers-reduced-motion: reduce){
  html.js-reveal-ready .team-scroll-reveal,
  html.js-reveal-ready .team-scroll-reveal.is-visible{
    opacity:1!important;
    transform:none!important;
    transition:none!important;
  }
}
</style>
'''

js = r'''
<script id="team-profile-scroll-reveal-v1-script">
(function(){
  document.documentElement.classList.add('js-reveal-ready');
  var selectors = [
    '.fq-about', '.fq-experience', '.fq-expertise', '.fq-selected',
    '.tp-about', '.tp-expertise', '.tp-selected',
    '.cta', '.fq-cta'
  ];
  var nodes = [];
  selectors.forEach(function(sel){
    document.querySelectorAll(sel).forEach(function(el){
      if (nodes.indexOf(el) === -1) nodes.push(el);
    });
  });
  nodes.forEach(function(el, i){
    el.classList.add('team-scroll-reveal');
    el.setAttribute('data-reveal-delay', String((i % 3)));
  });

  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    nodes.forEach(function(el){ el.classList.add('is-visible'); });
    return;
  }

  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, {threshold:0.12, rootMargin:'0px 0px -8% 0px'});

  nodes.forEach(function(el){ observer.observe(el); });
})();
</script>
'''

for p in files:
    if not p.exists():
        print(f'Skipping missing {p}')
        continue
    s = p.read_text(encoding='utf-8')
    if marker in s:
        print(f'Already patched {p}')
        continue
    if '</head>' in s:
        s = s.replace('</head>', css + '\n</head>', 1)
    if '</body>' in s:
        s = s.replace('</body>', js + '\n</body>', 1)
    p.write_text(s, encoding='utf-8')
    print(f'Added scroll reveal to {p}')
