from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
old='.ins-v2-person-photo img{width:100%;height:100%;object-fit:cover;object-position:center top;transition:transform .45s cubic-bezier(.2,.75,.2,1)}'
new='.ins-v2-person-photo img{width:100%;height:100%;object-fit:contain;object-position:center bottom;transition:transform .45s cubic-bezier(.2,.75,.2,1)}'
if old not in s:
    raise SystemExit('photo img css target not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Zoomed out Insiders portraits')
