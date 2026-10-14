from pathlib import Path

p = Path('industrias/educacion.html')
s = p.read_text(encoding='utf-8')
needle = '''  <a href="https://instagram.com/lowsignalagency" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">
    <svg class="brand-svg" viewBox="0 0 24 24" aria-hidden="true">
      <rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/>
      <circle cx="12" cy="12" r="4.1" fill="none" stroke="currentColor" stroke-width="1.8"/>
      <circle cx="17.4" cy="6.7" r="1.1" fill="currentColor"/>
    </svg>
  </a>
'''
insert = needle + '''  <a href="https://www.facebook.com/lowsignalagency" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook">
    <svg class="brand-svg" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M13.7 21v-8h2.7l.4-3h-3.1V8.1c0-.87.24-1.46 1.52-1.46H16.9V4.02A22.4 22.4 0 0 0 14.52 3.9c-2.35 0-3.96 1.43-3.96 4.06V10H8v3h2.56v8h3.14Z" fill="currentColor"/>
    </svg>
  </a>
'''
if 'aria-label="Facebook"' in s:
    print('Facebook icon already present')
elif needle not in s:
    raise SystemExit('Instagram icon block not found')
else:
    s = s.replace(needle, insert, 1)
    p.write_text(s, encoding='utf-8')
    print('Added Facebook icon to Education footer')
