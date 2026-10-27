from pathlib import Path

p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')

old = '''        <div class="insr-people">
          <article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/joaquin.png" alt="Joaquín, miembro de lowsignal Insiders" loading="lazy"></div><b>Joaquín</b><span>INSIDER</span></article>
          <article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/samu.png" alt="Samuel, miembro de lowsignal Insiders" loading="lazy"></div><b>Samuel</b><span>INSIDER</span></article>
          <article><div class="insr-person-photo insr-pablo-photo"><img src="https://lowsignal.cl/assets/pablo-embajador.png" alt="Pablo, miembro de lowsignal Insiders" loading="lazy"></div><b>Pablo</b><span>INSIDER</span></article>
          <article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/martin-insiders.png" alt="Martín, miembro de lowsignal Insiders" loading="lazy"></div><b>Martín</b><span>INSIDER</span></article>
        </div>'''

new = '''        <div class="insr-people" aria-label="Comunidad lowsignal Insiders">
          <article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/joaquin.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>
          <article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/samu.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>
          <article><div class="insr-person-photo insr-pablo-photo"><img src="https://lowsignal.cl/assets/pablo-embajador.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>
          <article><div class="insr-person-photo"><img src="https://lowsignal.cl/assets/martin-insiders.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>
          <article><div class="insr-person-photo insr-ferfeli-photo"><img src="https://lowsignal.cl/assets/ferfeli.png" alt="Miembro de lowsignal Insiders" loading="lazy"></div></article>
        </div>'''

if old not in s:
    raise SystemExit('community block not found')
s = s.replace(old, new, 1)

s = s.replace('Joaquín, Samuel, Pablo y Martín ya son parte de la red. Buscamos a las próximas personas que quieran abrir camino con nosotros.', 'La red ya está creciendo. Buscamos a las próximas personas que quieran abrir camino con nosotros.', 1)

css = '''\n<style id="insiders-circular-community-v1">\n.insr-people{grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:14px!important;align-items:center!important}\n.insr-people article{min-width:0!important;margin:0!important}\n.insr-person-photo{width:100%!important;aspect-ratio:1/1!important;border-radius:50%!important;overflow:hidden!important;border:1px solid #E1E6F1!important;background:#E9EDF5!important;box-shadow:0 10px 26px rgba(7,15,34,.08)!important}\n.insr-person-photo img{width:100%!important;height:100%!important;object-fit:cover!important;object-position:center 20%!important}\n.insr-pablo-photo img{object-position:center 17%!important}\n.insr-ferfeli-photo img{object-position:center 20%!important}\n.insr-people article>b,.insr-people article>span{display:none!important}\n@media(max-width:700px){.insr-people{grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:8px!important}.insr-person-photo{border-radius:50%!important}}\n</style>\n'''

marker = '</head>'
if 'insiders-circular-community-v1' not in s:
    s = s.replace(marker, css + marker, 1)

p.write_text(s, encoding='utf-8')
print('updated insiders community to five circular faces')
