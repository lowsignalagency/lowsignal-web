from pathlib import Path

p = Path('casos/fcct.html')
s = p.read_text(encoding='utf-8')
old = 'https://lowsignal.cl/assets/web-crecer.jpg'
new = 'https://lowsignal.cl/assets/web-fcct.png'
if old not in s:
    raise SystemExit('Expected FCCT image reference not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
print('Updated FCCT case image reference')
