from pathlib import Path

p = Path('industrias/educacion.html')
s = p.read_text(encoding='utf-8')
old = '<div class="right">LINKEDIN · INSTAGRAM · GITHUB</div>'
new = '''<div class="right footer-meta-social" aria-label="Social">
  <a href="https://cl.linkedin.com/company/lowsignalagency" target="_blank" rel="noopener" aria-label="LinkedIn" title="LinkedIn">
    <svg class="brand-svg" viewBox="0 0 24 24" aria-hidden="true">
      <rect x="3" y="3" width="18" height="18" rx="3.5" fill="none" stroke="currentColor" stroke-width="1.8"/>
      <circle cx="8" cy="8.2" r="1.15" fill="currentColor"/>
      <path d="M6.9 10.7h2.2V17H6.9v-6.3Zm4.05 0h2.1v.86c.72-.77 1.54-1.12 2.5-1.12 1.97 0 3.05 1.3 3.05 3.55V17h-2.2v-2.72c0-1.15-.38-1.87-1.4-1.87-1.04 0-1.75.7-1.75 2.16V17h-2.3v-6.3Z" fill="currentColor"/>
    </svg>
  </a>
  <a href="https://instagram.com/lowsignalagency" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">
    <svg class="brand-svg" viewBox="0 0 24 24" aria-hidden="true">
      <rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/>
      <circle cx="12" cy="12" r="4.1" fill="none" stroke="currentColor" stroke-width="1.8"/>
      <circle cx="17.4" cy="6.7" r="1.1" fill="currentColor"/>
    </svg>
  </a>
  <a href="https://github.com/lowsignalagency" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub">
    <svg class="brand-svg" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M12 3.2a8.8 8.8 0 0 0-2.78 17.15c.44.08.6-.19.6-.42v-1.68c-2.45.53-2.97-1.04-2.97-1.04-.4-1.02-.98-1.29-.98-1.29-.8-.55.06-.54.06-.54.89.06 1.36.91 1.36.91.79 1.35 2.07.96 2.58.73.08-.57.31-.96.56-1.18-1.95-.22-4-0.98-4-4.35 0-.96.34-1.75.91-2.36-.09-.22-.4-1.12.09-2.33 0 0 .74-.24 2.42.9A8.4 8.4 0 0 1 12 7.43a8.4 8.4 0 0 1 2.2.3c1.68-1.14 2.42-.9 2.42-.9.49 1.21.18 2.11.09 2.33.57.61.91 1.4.91 2.36 0 3.38-2.06 4.13-4.01 4.35.32.27.6.8.6 1.61v2.45c0 .23.16.51.6.42A8.8 8.8 0 0 0 12 3.2Z" fill="currentColor"/>
    </svg>
  </a>
</div>'''
if old not in s:
    raise SystemExit('Old footer social text not found')
s = s.replace(old, new, 1)
style = '''\n<style id="education-footer-social-icons-v1">\n.footer-meta-social{display:flex!important;align-items:center!important;justify-content:flex-end!important;gap:10px!important}\n.footer-meta-social a{width:34px;height:34px;display:inline-flex;align-items:center;justify-content:center;border:1px solid rgba(138,164,255,.18);border-radius:9px;color:#8AA4FF;transition:background .2s ease,color .2s ease,border-color .2s ease,transform .2s ease}\n.footer-meta-social a:hover{background:rgba(138,164,255,.08);border-color:rgba(138,164,255,.34);color:#fff;transform:translateY(-1px)}\n.footer-meta-social .brand-svg{width:16px;height:16px;flex:0 0 16px}\n@media(max-width:760px){.footer-meta-social{justify-content:flex-start!important}}\n</style>\n'''
if 'education-footer-social-icons-v1' not in s:
    s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')
print('Education footer social icons updated')
