from pathlib import Path

# Fix current CSD page
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')
s = s.replace(
    '<div class="case-editorial-client">\n          <img src="https://lowsignal.cl/assets/logo-dali-darkbg.png" alt="Colegio Salvador Dalí">',
    '<div class="case-editorial-client">\n          <img src="https://lowsignal.cl/assets/logo-dali-maipu.png" alt="Colegio Salvador Dalí">',
    1
)
s = s.replace(
    'Un colegio con mucho que mostrar.<br><strong>Una experiencia digital que debía hacerlo visible.</strong>',
    'Un colegio con mucho que mostrar. <strong>Una experiencia digital que debía hacerlo visible.</strong>',
    1
)
p.write_text(s, encoding='utf-8')

# Persist the same fixes in the editorial template config
for path in ['scripts/apply_editorial_case_layout.py']:
    q = Path(path)
    if not q.exists():
        continue
    t = q.read_text(encoding='utf-8')
    t = t.replace(
        "'logo': 'https://lowsignal.cl/assets/logo-dali-darkbg.png'",
        "'logo': 'https://lowsignal.cl/assets/logo-dali-maipu.png'",
        1
    )
    t = t.replace(
        "'context_title': 'Un colegio con mucho que mostrar.<br><strong>Una experiencia digital que debía hacerlo visible.</strong>'",
        "'context_title': 'Un colegio con mucho que mostrar. <strong>Una experiencia digital que debía hacerlo visible.</strong>'",
        1
    )
    q.write_text(t, encoding='utf-8')
