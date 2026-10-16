from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
s=s.replace('  .ins-v2-network-strip-inner{min-height:0;padding-top:40px;padding-bottom:40px;grid-template-columns:1fr;gap:18px}\n','')
p.write_text(s,encoding='utf-8')
print('Cleaned remaining network strip CSS')
