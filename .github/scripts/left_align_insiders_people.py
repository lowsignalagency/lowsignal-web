from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
old='.ins-v2-people-grid{display:grid;grid-template-columns:minmax(0,260px) minmax(0,260px) minmax(0,250px);gap:22px;margin-top:44px;align-items:start;justify-content:center}'
new='.ins-v2-people-grid{display:grid;grid-template-columns:minmax(0,260px) minmax(0,260px) minmax(0,250px);gap:22px;margin-top:44px;align-items:start;justify-content:start}'
if old not in s:
    raise SystemExit('desktop people grid target not found')
s=s.replace(old,new,1)
old2='  .ins-v2-people-grid{grid-template-columns:minmax(0,260px) minmax(0,260px);justify-content:center}'
new2='  .ins-v2-people-grid{grid-template-columns:minmax(0,260px) minmax(0,260px);justify-content:start}'
if old2 not in s:
    raise SystemExit('tablet people grid target not found')
s=s.replace(old2,new2,1)
p.write_text(s,encoding='utf-8')
print('Left aligned Insiders people grid')
