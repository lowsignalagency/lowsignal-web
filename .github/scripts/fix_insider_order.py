from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
s=s.replace('src="https://lowsignal.cl/assets/joaquin.png" alt="Joaquín, Growth Ambassador de lowsignal" loading="lazy">\n            <span>INSIDER / 01</span>','src="https://lowsignal.cl/assets/joaquin.png" alt="Joaquín, Growth Ambassador de lowsignal" loading="lazy">\n            <span>INSIDER / 02</span>',1)
s=s.replace('src="https://lowsignal.cl/assets/samuel.png" alt="Samuel, Growth Ambassador de lowsignal" loading="lazy">\n            <span>INSIDER / 02</span>','src="https://lowsignal.cl/assets/samuel.png" alt="Samuel, Growth Ambassador de lowsignal" loading="lazy">\n            <span>INSIDER / 01</span>',1)
p.write_text(s,encoding='utf-8')
print('Updated Insider numbering: Samuel 01, Joaquin 02')
