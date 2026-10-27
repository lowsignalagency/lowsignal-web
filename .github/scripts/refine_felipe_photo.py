from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')
s=s.replace('.fq-editorial-grid{display:grid;grid-template-columns:minmax(0,.93fr) minmax(420px,1.07fr);gap:78px;align-items:center}', '.fq-editorial-grid{display:grid;grid-template-columns:minmax(340px,.72fr) minmax(0,1.28fr);gap:88px;align-items:center}', 1)
s=s.replace('.fq-editorial-photo{margin:0;min-height:660px;border-radius:24px;overflow:hidden;background:#E7EBF2}', '.fq-editorial-photo{margin:0;width:min(100%,430px);min-height:620px;border-radius:22px;overflow:hidden;background:#E7EBF2}', 1)
s=s.replace('.fq-editorial-photo img{width:100%;height:100%;min-height:660px;object-fit:cover;object-position:center top;filter:grayscale(1) contrast(1.03)}', '.fq-editorial-photo img{width:100%;height:100%;min-height:620px;object-fit:cover;object-position:center top;filter:grayscale(1) contrast(1.03)}', 1)
s=s.replace('@media(max-width:900px){.fq-editorial-profile{padding:132px 0 64px}.fq-editorial-shell{width:calc(100% - 48px)}.fq-editorial-grid{grid-template-columns:1fr;gap:38px}.fq-editorial-copy{max-width:720px}.fq-editorial-photo,.fq-editorial-photo img{min-height:520px}.fq-editorial-photo{order:-1}.fq-editorial-back{margin-bottom:28px}}', '@media(max-width:900px){.fq-editorial-profile{padding:132px 0 64px}.fq-editorial-shell{width:calc(100% - 48px)}.fq-editorial-grid{grid-template-columns:1fr;gap:38px}.fq-editorial-copy{max-width:720px}.fq-editorial-photo{width:min(100%,460px)}.fq-editorial-photo,.fq-editorial-photo img{min-height:560px}.fq-editorial-photo{order:-1}}', 1)
p.write_text(s, encoding='utf-8')
print('refined Felipe photo proportions')
