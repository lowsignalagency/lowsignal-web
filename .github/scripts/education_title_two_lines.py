from pathlib import Path
p=Path('industrias/educacion.html')
s=p.read_text(encoding='utf-8')
old='<span class="edu-title-desktop">Presencia digital<br>que genera<br><strong>confianza.</strong></span>'
new='<span class="edu-title-desktop">Presencia digital que genera<br><strong>confianza.</strong></span>'
if old not in s:
    raise SystemExit('Education desktop title pattern not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Education desktop hero title updated to two lines')
