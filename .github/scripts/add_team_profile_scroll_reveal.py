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
  transform:translateY(16px);
  transition:
    opacity .62s ease,
    transform .68s cubic-bezier(.2,.75,.2,1);
  will-change:opacity,transform;
}
html.js-reveal-ready .team-scroll-reveal.is-visible{
  opacity:1;
  transform:translateY(0);
}
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
    '.fq-about-grid > div',
    '.fq-section-head',
    '.fq-timeline',
    '.fq-expertise-grid',
    '.fq-selected-grid > div',
    '.tp-about-grid > div',
    '.tp-head',
    '.tp-expertise-grid',
    '.tp-selected-grid > div',
    '.lsr-band .lsr-wrap',
    '.cta > *',
    '.fq-cta > *'
  ];
  var nodes = [];
  selectors.forEach(function(sel){
    document.querySelectorAll(sel).forEach(function(el){
      if (nodes.indexOf(el) === -1) nodes.push(el);
    });
  });
  nodes.forEach(function(el){
    el.classList.add('team-scroll-reveal');
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
  }, {threshold:0.10, rootMargin:'0px 0px -6% 0px'});

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
        start = s.find('<style id="team-profile-scroll-reveal-v1">')
        end = s.find('</style>', start)
        if start != -1 and end != -1:
            s = s[:start] + css.strip() + s[end + len('</style>'):]

        start = s.find('<script id="team-profile-scroll-reveal-v1-script">')
        end = s.find('</script>', start)
        if start != -1 and end != -1:
            s = s[:start] + js.strip() + s[end + len('</script>'):]
        print(f'Updated scroll reveal in {p}')
    else:
        if '</head>' in s:
            s = s.replace('</head>', css + '\n</head>', 1)
        if '</body>' in s:
            s = s.replace('</body>', js + '\n</body>', 1)
        print(f'Added scroll reveal to {p}')

    p.write_text(s, encoding='utf-8')
