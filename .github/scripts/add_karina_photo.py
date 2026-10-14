from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
old = '''          <div class="lsr-case-person">\n            <div>\n              <b>Karina Ravanal</b>\n              <span>Directora, Colegio Salvador Dalí</span>\n            </div>\n          </div>'''
new = '''          <div class="lsr-case-person">\n            <img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal">\n            <div>\n              <b>Karina Ravanal</b>\n              <span>Directora, Colegio Salvador Dalí</span>\n            </div>\n          </div>'''
if old not in s:
    raise SystemExit('Karina testimonial block not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
print('Added Karina photo to Home testimonial')
# trigger
