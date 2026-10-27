from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')

s=s.replace('.fq-editorial-profile{padding:156px 0 84px;background:#fff;color:#0D1420}', '.fq-editorial-profile{padding:112px 0 72px;background:#fff;color:#0D1420}', 1)
s=s.replace('.fq-editorial-bio{margin:30px 0 0;color:#273247;font-size:16px;line-height:1.72;font-weight:400}.fq-editorial-bio a{color:#1419E0;text-decoration:none;font-weight:600}.fq-editorial-bio a:hover{text-decoration:underline}.fq-editorial-cta{display:inline-flex;align-items:center;justify-content:center;margin-top:28px;min-height:48px;padding:0 20px;border-radius:12px;background:#1419E0;color:#fff;font-size:14px;font-weight:650;transition:.2s ease}.fq-editorial-cta:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(20,25,224,.18)}', '.fq-editorial-bio{margin:30px 0 0;color:#273247;font-size:16px;line-height:1.72;font-weight:400}.fq-editorial-bio a{color:#1419E0;text-decoration:none;font-weight:600}.fq-editorial-bio a:hover{text-decoration:underline}', 1)
s=s.replace('@media(max-width:900px){.fq-editorial-profile{padding:132px 0 64px}', '@media(max-width:900px){.fq-editorial-profile{padding:104px 0 60px}', 1)
s=s.replace('@media(max-width:560px){.fq-editorial-shell{width:calc(100% - 32px)}.fq-editorial-profile{padding:116px 0 50px}', '@media(max-width:560px){.fq-editorial-shell{width:calc(100% - 32px)}.fq-editorial-profile{padding:98px 0 48px}', 1)

s=s.replace('          <a class="fq-editorial-cta" href="https://lowsignal.cl/#contacto">Construimos lo que viene ↗</a>\n', '', 1)

old='''  </section>\n</main>'''
new='''  </section>\n  <section class="fq-home-cta" aria-label="Contacto">\n    <div class="fq-home-cta-inner">\n      <p>¿Construimos lo que viene?</p>\n      <a href="https://calendly.com/felipe-lowsignal/30min" target="_blank" rel="noopener noreferrer">Hablemos</a>\n    </div>\n  </section>\n</main>'''
s=s.replace(old,new,1)

band_css='''\n<style id="felipe-home-cta-band-v1">\n.fq-home-cta{background:linear-gradient(105deg,#1419E0,#2447F5);color:#fff}\n.fq-home-cta-inner{width:min(1180px,calc(100% - 96px));min-height:208px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:40px}\n.fq-home-cta p{margin:0;color:#fff;font-size:30px;line-height:1.25;letter-spacing:-.03em;font-weight:300}\n.fq-home-cta a{min-height:50px;padding:0 24px;border-radius:999px;background:#fff;color:#17235D;display:inline-flex;align-items:center;justify-content:center;font-size:14px;font-weight:650;transition:transform .2s ease,box-shadow .2s ease,background-color .2s ease,color .2s ease}\n.fq-home-cta a:hover{background:#F6F8FF;color:#14206A;transform:translateY(-2px);box-shadow:0 14px 32px rgba(9,18,54,.18)}\n@media(max-width:900px){.fq-home-cta-inner{width:calc(100% - 48px);min-height:190px}}\n@media(max-width:560px){.fq-home-cta-inner{width:calc(100% - 32px);min-height:190px;align-items:flex-start;justify-content:center;flex-direction:column}.fq-home-cta p{font-size:25px}.fq-home-cta a{width:100%}}\n</style>\n'''
s=s.replace('</head>', band_css+'\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('refined Felipe profile spacing and added home-style CTA band')
