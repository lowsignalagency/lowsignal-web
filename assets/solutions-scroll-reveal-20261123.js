/* lowsignal · subtle on-scroll entrances, solutions only */
(function () {
  'use strict';
  function start() {
    const root = document.querySelector('main');
    if (!root || !('IntersectionObserver' in window) ||
        window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const sections = [...root.querySelectorAll('section')];
    if (!sections.length) return;
    const targets = [];
    const seen = new Set();
    sections.forEach(section => {
      // Preserve page-specific hero animation and interactive components.
      if (section === sections[0]) return;
      const candidates = [
        ...section.querySelectorAll('h2, h3'),
        ...section.querySelectorAll('p')
      ];
      candidates.forEach(el => {
        if (seen.has(el) || el.closest('nav, footer, header, dialog, details, button, [aria-hidden="true"], [hidden]')) return;
        if (el.closest('.mobile-nav-panel, .site-nav, .low-footer')) return;
        if (!el.textContent.trim() || el.getClientRects().length === 0) return;
        if (el.closest('[class*="carousel"], [class*="slider"], [class*="marquee"], [class*="ticker"]')) return;
        seen.add(el);
        targets.push(el);
      });
    });
    if (!targets.length) return;
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('ls-solutions-visible');
        observer.unobserve(entry.target);
      });
    }, {threshold: 0.06, rootMargin: '0px 0px -20px 0px'});
    targets.forEach((el, i) => {
      el.style.setProperty('--ls-solutions-delay', ((i % 3) * 55) + 'ms');
      el.classList.add('ls-solutions-reveal');
    });
    document.documentElement.classList.add('ls-solutions-motion');
    targets.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom >= 0) {
        el.classList.add('ls-solutions-visible');
      } else {
        observer.observe(el);
      }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, {once: true});
  else start();
})();
