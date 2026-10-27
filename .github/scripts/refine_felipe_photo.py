from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')
s=s.replace('.fq-editorial-grid{display:grid;grid-template-columns:minmax(420px,1.07fr) minmax(0,.93fr);gap:78px;align-items:center}', '.fq-editorial-grid{display:grid;grid-template-columns:minmax(340px,.72fr) minmax(0,1.28fr);gap:88px;align-items:center}', 1)
s=s.replace('.fq-editorial-copy{max-width:590px}', '.fq-editorial-copy{max-width:650px}', 1)
s=s.replace('.fq-editorial-bio{margin:34px 0 0;color:#273247;font-size:16px;line-height:1.8;font-weight:400}', '.fq-editorial-bio{margin:30px 0 0;color:#273247;font-size:16px;line-height:1.72;font-weight:400}.fq-editorial-bio a{color:#1419E0;text-decoration:none;font-weight:600}.fq-editorial-bio a:hover{text-decoration:underline}.fq-editorial-cta{display:inline-flex;align-items:center;justify-content:center;margin-top:28px;min-height:48px;padding:0 20px;border-radius:12px;background:#1419E0;color:#fff;font-size:14px;font-weight:650;transition:.2s ease}.fq-editorial-cta:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(20,25,224,.18)}', 1)
old='Felipe cofundó lowsignal, donde lidera operaciones, estrategia comercial, client delivery y el desarrollo de productos y sistemas internos de growth. Antes lideró partnerships en Tether Education, trabajando en iniciativas de tecnología y educación pública que alcanzaron a 20.000+ familias y 35.000+ estudiantes, y luego se desempeñó como Product Manager en GeoVictoria, desarrollando productos de workforce management para clientes enterprise en Latinoamérica. Su trabajo conecta negocio, producto, tecnología y ejecución.'
new='Felipe cofundó lowsignal, donde lidera operaciones, estrategia comercial, client delivery y el desarrollo de productos y sistemas internos de growth. Antes lideró partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, trabajando en iniciativas de tecnología y educación pública que alcanzaron a 20.000+ familias y 35.000+ estudiantes, y luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, desarrollando productos de workforce management para clientes enterprise en Latinoamérica. Su trabajo conecta negocio, producto, tecnología y ejecución.'
s=s.replace(old,new,1)
needle='''          <div class="fq-editorial-links" aria-label="Enlaces de Felipe Quiroz">'''
cta='''          <a class="fq-editorial-cta" href="https://lowsignal.cl/#contacto">Construimos lo que viene ↗</a>\n'''
s=s.replace(needle,cta+needle,1)
p.write_text(s, encoding='utf-8')
print('refined Felipe copy, links and CTA')
