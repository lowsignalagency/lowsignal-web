from pathlib import Path

p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')

old = '<article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/santiago.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>'
new = '<article><div class="insr-person-photo insr-santiago-photo"><img src="https://lowsignal.cl/assets/santiago.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>'
if old in s:
    s = s.replace(old, new, 1)
elif 'insr-santiago-photo' not in s:
    raise SystemExit('Santiago portrait not found')

css = '''\n<style id="insiders-santiago-framing-v1">\n.insr-santiago-photo img{transform:scale(1.09)!important;object-position:center 18%!important}\n.insr-people article:hover .insr-santiago-photo img{transform:scale(1.115)!important}\n</style>\n'''
if 'insiders-santiago-framing-v1' not in s:
    s = s.replace('</head>', css + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('tuned Santiago portrait framing')
