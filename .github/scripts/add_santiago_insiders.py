from pathlib import Path

p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')

s = s.replace('.insr-people{grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:14px!important;align-items:center!important}', '.insr-people{grid-template-columns:repeat(6,minmax(0,1fr))!important;gap:14px!important;align-items:center!important}', 1)
s = s.replace('@media(max-width:700px){.insr-people{grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:8px!important}', '@media(max-width:700px){.insr-people{grid-template-columns:repeat(6,minmax(0,1fr))!important;gap:8px!important}', 1)

needle = '          <article><div class="insr-person-photo insr-ferfeli-photo"><img src="https://lowsignal.cl/assets/ferfeli.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>\n'
insert = needle + '          <article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/santiago.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>\n'
if needle not in s:
    raise SystemExit('Insiders people block not found')
s = s.replace(needle, insert, 1)

p.write_text(s, encoding='utf-8')
print('added Santiago to Insiders')
