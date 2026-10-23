from pathlib import Path
import re

p = Path('soluciones/low-social.html')
s = p.read_text()

# Remove the cross-industry cases block now that cases live in Industry pages.
s = re.sub(
    r'\s*<section class="solution-cases" id="casos">.*?</section>\s*',
    '\n',
    s,
    count=1,
    flags=re.S,
)

# Remove duplicated testimonial proof now that testimonials are stronger on Home and Industry pages.
s = re.sub(
    r'\s*<section class="solution-testimonial">.*?</section>\s*',
    '\n',
    s,
    count=1,
    flags=re.S,
)

# Avoid repeating the same idea in the kicker and heading.
s = s.replace('<p class="ls-social-section-kicker">TODO LO QUE INCLUYE</p>\n      <h2 id="ls-social-includes-title">Todo lo que incluye <strong>Low Social.</strong></h2>', '<p class="ls-social-section-kicker">LOW SOCIAL</p>\n      <h2 id="ls-social-includes-title">Todo lo que incluye <strong>Low Social.</strong></h2>', 1)

# Keep the includes section lighter so the FAQ can retain its original ice tone.
s = s.replace('.ls-social-includes{padding:104px 0 108px;background:#F7F8FA;color:#101010}', '.ls-social-includes{padding:112px 0 116px;background:#F7F9FD;color:#101010;border-top:1px solid #E2E8F3;border-bottom:1px solid #E2E8F3}', 1)
s = s.replace('.ls-social-includes{padding:112px 0 116px;background:#EEF3FF;color:#101010;border-top:1px solid #D7E0F2;border-bottom:1px solid #D7E0F2}', '.ls-social-includes{padding:112px 0 116px;background:#F7F9FD;color:#101010;border-top:1px solid #E2E8F3;border-bottom:1px solid #E2E8F3}', 1)
s = s.replace('.ls-social-includes-col li:before{content:"✓";position:absolute;left:0;top:-1px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:#E9F2FF;color:#1682FF;font-size:12px;font-weight:700}', '.ls-social-includes-col li:before{content:"✓";position:absolute;left:0;top:-1px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:#DCE9FF;color:#1419E0;font-size:12px;font-weight:700}', 1)

# Give Content System the strongest light-blue contrast between the content sections.
s = s.replace('.ls-social-smart{\n  background:#F4F6FC;', '.ls-social-smart{\n  background:#DDE6F6;', 1)
s = s.replace('.ls-social-smart{\n  background:#E2E9F8;', '.ls-social-smart{\n  background:#DDE6F6;', 1)

# Restore the FAQ to the original ice background the user preferred.
s = s.replace('.ls-social-faq{padding:78px 0 84px;background:#FFFFFF;border-top:1px solid #D7E0F2}', '.ls-social-faq{padding:78px 0 84px;background:#EEF3FF}', 1)

# Keep mobile spacing proportional after the desktop adjustment.
s = s.replace('@media(max-width:760px){.ls-social-includes{padding:74px 0 78px}', '@media(max-width:760px){.ls-social-includes{padding:80px 0 84px}', 1)

# Ensure every remaining Low Social content block participates in scroll reveal.
scroll_controller = '''
<script id="low-social-scroll-completeness-v1">
(function(){
  function init(){
    const revealSelectors = [
      '.ls-social-includes .ls-social-section-kicker',
      '.ls-social-includes h2',
      '.ls-social-smart-inner',
      '.ls-social-faq-heading',
      '.lsr-band-inner'
    ];
    const staggerSelectors = [
      '.ls-social-includes-grid',
      '.ls-social-faq-list'
    ];
    const targets = [];

    revealSelectors.forEach(function(selector){
      document.querySelectorAll(selector).forEach(function(el){
        el.classList.add('ls-scroll-reveal');
        targets.push(el);
      });
    });

    staggerSelectors.forEach(function(selector){
      document.querySelectorAll(selector).forEach(function(el){
        el.classList.add('ls-scroll-stagger');
        targets.push(el);
      });
    });

    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches){
      targets.forEach(function(el){ el.classList.add('is-visible'); });
      return;
    }

    if (!('IntersectionObserver' in window)){
      targets.forEach(function(el){ el.classList.add('is-visible'); });
      return;
    }

    const observer = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, {threshold:0.12, rootMargin:'0px 0px -8% 0px'});

    targets.forEach(function(el){
      if (!el.classList.contains('is-visible')) observer.observe(el);
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
</script>
'''
if 'low-social-scroll-completeness-v1' not in s:
    s = s.replace('</body>', scroll_controller + '\n</body>', 1)

p.write_text(s)
