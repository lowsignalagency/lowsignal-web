from pathlib import Path

p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')

s=s.replace('      <a class="fq-editorial-back" href="https://lowsignal.cl/nosotros">← Equipo</a>\n','',1)

old='''      <div class="fq-editorial-grid">\n        <div class="fq-editorial-copy">'''
new='''      <div class="fq-editorial-grid">\n        <figure class="fq-editorial-photo">\n          <img src="https://lowsignal.cl/assets/team_felipe-1.png" alt="Felipe Quiroz" loading="eager">\n        </figure>\n        <div class="fq-editorial-copy">'''
if old not in s: raise SystemExit('grid start not found')
s=s.replace(old,new,1)

old_photo='''        </div>\n        <figure class="fq-editorial-photo">\n          <img src="https://lowsignal.cl/assets/team_felipe-1.png" alt="Felipe Quiroz" loading="eager">\n        </figure>\n      </div>'''
new_photo='''        </div>\n      </div>'''
if old_photo not in s: raise SystemExit('old photo block not found')
s=s.replace(old_photo,new_photo,1)

s=s.replace('.fq-editorial-grid{display:grid;grid-template-columns:minmax(0,.93fr) minmax(420px,1.07fr);gap:78px;align-items:center}', '.fq-editorial-grid{display:grid;grid-template-columns:minmax(420px,1.07fr) minmax(0,.93fr);gap:78px;align-items:center}', 1)
s=s.replace('.fq-editorial-back{display:inline-flex;margin-bottom:42px;color:#77839A;font-size:12px;font-weight:500;transition:.2s ease}\n.fq-editorial-back:hover{color:#1419E0;transform:translateX(-2px)}\n','',1)
s=s.replace('.fq-editorial-photo{order:-1}','',1)
s=s.replace('.fq-editorial-back{display:none}','',1)

p.write_text(s,encoding='utf-8')
print('moved Felipe photo left and removed back link')
