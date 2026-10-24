from pathlib import Path
import re

p = Path('casos/rech.html')
s = p.read_text(encoding='utf-8')

# Keep RECH aligned 1:1 with the desktop navbar rhythm.
s = re.sub(
    r'\.rechx-wrap\{[^}]*\}',
    '.rechx-wrap{width:min(1220px,calc(100% - 128px))!important;max-width:1220px!important;margin-inline:auto!important}',
    s,
    count=1
)
s = s.replace(
    '@media(max-width:1000px){.rechx-wrap{width:calc(100% - 56px)}',
    '@media(max-width:1000px){.rechx-wrap{width:calc(100% - 48px)!important}'
)
s = s.replace(
    '@media(max-width:1000px){.rechx-wrap{width:calc(100% - 48px)!important}',
    '@media(max-width:1000px){.rechx-wrap{width:calc(100% - 48px)!important}'
)
s = s.replace(
    '@media(max-width:760px){.rechx-wrap{width:calc(100% - 40px)}',
    '@media(max-width:760px){.rechx-wrap{width:calc(100% - 24px)!important}'
)
s = s.replace(
    '@media(max-width:760px){.rechx-wrap{width:calc(100% - 40px)!important}',
    '@media(max-width:760px){.rechx-wrap{width:calc(100% - 24px)!important}'
)

# Remove top back link if an older build brought it back.
s = re.sub(r'\s*<a class="rechx-back"[^>]*>← Customer Stories</a>\s*', '\n      ', s, count=1)

# Hover polish + native scrolling + viewport reveal motion.
s = re.sub(r'<style id="rech-interaction-polish">.*?</style>\s*', '', s, flags=re.S)
polish = r'''
<style id="rech-interaction-polish">
html{scroll-behavior:smooth!important}

.rechx-next-card{
  transform:translateY(0);
  box-shadow:0 14px 36px rgba(7,15,34,.08);
  transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s ease!important;
}
.rechx-next-card img{transition:transform .65s cubic-bezier(.2,.7,.2,1),filter .45s ease!important}
.rechx-next-overlay{transition:background .4s ease!important}
.rechx-next-copy{transition:transform .35s cubic-bezier(.2,.7,.2,1)!important}
.rechx-next-copy b{display:inline-block;transition:transform .3s ease,opacity .3s ease!important}

/* Scroll reveal: visual motion only. Native wheel/trackpad scrolling stays untouched. */
.rech-reveal{
  opacity:0;
  transform:translate3d(0,28px,0);
  transition:
    opacity .72s cubic-bezier(.2,.7,.2,1),
    transform .72s cubic-bezier(.2,.7,.2,1);
  transition-delay:var(--rech-delay,0ms);
  will-change:opacity,transform;
}
.rech-reveal.rech-reveal-soft{transform:translate3d(0,18px,0)}
.rech-reveal.is-visible{opacity:1;transform:translate3d(0,0,0)}
.rechx-gallery figure.rech-reveal{overflow:hidden}
.rechx-gallery figure.rech-reveal img{
  transform:scale(1.025);
  transition:transform .95s cubic-bezier(.2,.7,.2,1);
}
.rechx-gallery figure.rech-reveal.is-visible img{transform:scale(1)}

@media(hover:hover){
  .rechx-next-card:hover{transform:translateY(-6px);box-shadow:0 28px 64px rgba(7,15,34,.18)}
  .rechx-next-card:hover img{transform:scale(1.035);filter:saturate(1.04) contrast(1.02)}
  .rechx-next-card:hover .rechx-next-overlay{background:linear-gradient(180deg,rgba(7,15,34,.03) 24%,rgba(7,15,34,.90) 100%)}
  .rechx-next-card:hover .rechx-next-copy{transform:translateY(-5px)}
  .rechx-next-card:hover .rechx-next-copy b{transform:translateX(5px)}
  .rechx-next-head>a{transition:color .2s ease,transform .2s ease}
  .rechx-next-head>a:hover{color:#0D13B9;transform:translateX(3px)}
}

@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto!important}
  .rech-reveal{opacity:1!important;transform:none!important;transition:none!important}
  .rechx-gallery figure.rech-reveal img{transform:none!important;transition:none!important}
  .rechx-next-card,.rechx-next-card img,.rechx-next-copy,.rechx-next-copy b{transition:none!important}
}
</style>
'''
s = s.replace('</head>', polish + '\n</head>', 1)

# Remove any previous custom wheel interception so scrolling stays fully native.
s = re.sub(r'<script id="rech-inertial-scroll">.*?</script>\s*', '', s, flags=re.S)
s = re.sub(r'<script id="rech-scroll-reveal">.*?</script>\s*', '', s, flags=re.S)

reveal = r'''
<script id="rech-scroll-reveal">
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const targets = [
    ...document.querySelectorAll('.rechx-intro-grid'),
    ...document.querySelectorAll('.rechx-row'),
    ...document.querySelectorAll('.rechx-work-head'),
    ...document.querySelectorAll('.rechx-gallery > *'),
    ...document.querySelectorAll('.rechx-outcome-grid'),
    ...document.querySelectorAll('.rechx-quote-inner'),
    ...document.querySelectorAll('.rechx-next-head'),
    ...document.querySelectorAll('.rechx-next-card')
  ];

  if (!targets.length) return;

  targets.forEach((el, index) => {
    el.classList.add('rech-reveal');
    if (el.matches('.rechx-row, .rechx-gallery > *')) {
      el.style.setProperty('--rech-delay', `${Math.min(index % 3, 2) * 85}ms`);
    }
    if (el.matches('.rechx-outcome-grid, .rechx-quote-inner')) {
      el.classList.add('rech-reveal-soft');
    }
  });

  if (reduceMotion || !('IntersectionObserver' in window)) {
    targets.forEach(el => el.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, {
    threshold:0.14,
    rootMargin:'0px 0px -8% 0px'
  });

  targets.forEach(el => observer.observe(el));
})();
</script>
'''
s = s.replace('</body>', reveal + '\n</body>', 1)

p.write_text(s, encoding='utf-8')
