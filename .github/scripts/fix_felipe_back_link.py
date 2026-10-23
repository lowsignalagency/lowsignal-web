from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')
s=s.replace('.fq-profile{margin-top:-100px;padding:162px 0 82px;', '.fq-profile{margin-top:-100px;padding:214px 0 82px;')
s=s.replace('@media(max-width:760px){.fq-shell{width:calc(100% - 40px)}.fq-profile{padding:132px 0 62px}', '@media(max-width:760px){.fq-shell{width:calc(100% - 40px)}.fq-profile{padding:158px 0 62px}')
p.write_text(s,encoding='utf-8')
