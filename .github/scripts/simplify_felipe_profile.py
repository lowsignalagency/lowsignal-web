from pathlib import Path

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')

start = s.find('<main id="top">')
end = s.find('</main>', start)
if start == -1 or end == -1:
    raise SystemExit('main block not found')
end += len('</main>')

main = '''<main id="top" class="fq-editorial-page">
  <section class="fq-editorial-profile" aria-label="Perfil de Felipe Quiroz">
    <div class="fq-editorial-shell">
      <a class="fq-editorial-back" href="https://lowsignal.cl/nosotros">← Equipo</a>
      <div class="fq-editorial-grid">
        <div class="fq-editorial-copy">
          <p class="fq-editorial-kicker">TEAM</p>
          <h1>Felipe Quiroz</h1>
          <p class="fq-editorial-role">Co-Founder &amp; COO, lowsignal</p>
          <p class="fq-editorial-bio">Felipe cofundó lowsignal, donde lidera operaciones, estrategia comercial, client delivery y el desarrollo de productos y sistemas internos de growth. Antes lideró partnerships en Tether Education, trabajando en iniciativas de tecnología y educación pública que alcanzaron a 20.000+ familias y 35.000+ estudiantes, y luego se desempeñó como Product Manager en GeoVictoria, desarrollando productos de workforce management para clientes enterprise en Latinoamérica. Su trabajo conecta negocio, producto, tecnología y ejecución.</p>
          <div class="fq-editorial-links" aria-label="Enlaces de Felipe Quiroz">
            <a href="https://www.linkedin.com/in/felipequirozp" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
            <a href="https://github.com/felipequirozp" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
            <a href="https://felipequirozp.cl" target="_blank" rel="noopener noreferrer">Personal site ↗</a>
          </div>
        </div>
        <figure class="fq-editorial-photo">
          <img src="https://lowsignal.cl/assets/team_felipe-1.png" alt="Felipe Quiroz" loading="eager">
        </figure>
      </div>
    </div>
  </section>
</main>'''

s = s[:start] + main + s[end:]

css = '''\n<style id="felipe-editorial-profile-v1">\n.fq-editorial-page{background:#fff}\n.fq-editorial-profile{padding:156px 0 84px;background:#fff;color:#0D1420}\n.fq-editorial-shell{width:min(1180px,calc(100% - 96px));margin:0 auto}\n.fq-editorial-back{display:inline-flex;margin-bottom:42px;color:#77839A;font-size:12px;font-weight:500;transition:.2s ease}\n.fq-editorial-back:hover{color:#1419E0;transform:translateX(-2px)}\n.fq-editorial-grid{display:grid;grid-template-columns:minmax(0,.93fr) minmax(420px,1.07fr);gap:78px;align-items:center}\n.fq-editorial-copy{max-width:590px}\n.fq-editorial-kicker{margin:0 0 16px;color:#1419E0;font-size:11px;font-weight:700;letter-spacing:.16em}\n.fq-editorial-copy h1{margin:0;font-size:clamp(48px,6vw,82px);line-height:.98;letter-spacing:-.055em;font-weight:500;color:#0D1420}\n.fq-editorial-role{margin:20px 0 0;color:#5F6D86;font-size:17px;line-height:1.5}\n.fq-editorial-bio{margin:34px 0 0;color:#273247;font-size:16px;line-height:1.8;font-weight:400}\n.fq-editorial-links{display:flex;flex-wrap:wrap;gap:24px;margin-top:34px;padding-top:22px;border-top:1px solid #E3E8F0}\n.fq-editorial-links a{color:#1419E0;font-size:13px;font-weight:600;transition:.2s ease}\n.fq-editorial-links a:hover{opacity:.72;transform:translateY(-1px)}\n.fq-editorial-photo{margin:0;min-height:660px;border-radius:24px;overflow:hidden;background:#E7EBF2}\n.fq-editorial-photo img{width:100%;height:100%;min-height:660px;object-fit:cover;object-position:center top;filter:grayscale(1) contrast(1.03)}\n@media(max-width:900px){.fq-editorial-profile{padding:132px 0 64px}.fq-editorial-shell{width:calc(100% - 48px)}.fq-editorial-grid{grid-template-columns:1fr;gap:38px}.fq-editorial-copy{max-width:720px}.fq-editorial-photo,.fq-editorial-photo img{min-height:520px}.fq-editorial-photo{order:-1}.fq-editorial-back{margin-bottom:28px}}\n@media(max-width:560px){.fq-editorial-shell{width:calc(100% - 32px)}.fq-editorial-profile{padding:116px 0 50px}.fq-editorial-back{display:none}.fq-editorial-photo,.fq-editorial-photo img{min-height:430px}.fq-editorial-photo{border-radius:18px}.fq-editorial-copy h1{font-size:46px}.fq-editorial-role{font-size:15px}.fq-editorial-bio{margin-top:26px;font-size:15px;line-height:1.72}.fq-editorial-links{gap:18px}}\n</style>\n'''

if 'felipe-editorial-profile-v1' not in s:
    s = s.replace('</head>', css + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('simplified Felipe profile to editorial layout')
