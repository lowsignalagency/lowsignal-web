from pathlib import Path

p = Path('casos/rech.html')
s = p.read_text(encoding='utf-8')
old = '<div class="case-editorial-client">\n          <img src="https://lowsignal.cl/assets/rech-logo-full-white-trim.png" alt="Red Educacional Camilo Henríquez">'
new = '<div class="case-editorial-client">\n          <img src="https://lowsignal.cl/assets/rech-logo-full.png" alt="Red Educacional Camilo Henríquez">'
if old not in s:
    raise RuntimeError('Editorial RECH logo block not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')

# trigger workflow
