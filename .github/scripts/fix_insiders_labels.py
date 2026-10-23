from pathlib import Path

p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')

s = s.replace('<small>GROWTH SYSTEMS</small>', '<small>LOW FOR B2B</small>')
s = s.replace('<small>DEMAND &amp; BRAND</small>', '<small>LOW FOR B2C</small>')
s = s.replace('        <p class="insr-manifesto-index">01 / 04</p>\n', '')

p.write_text(s, encoding='utf-8')
print('fixed insiders labels and manifesto index')
