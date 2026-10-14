from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
s=s.replace('object-position:center 24% !important;','object-position:center 68% !important;',1)
s=s.replace('object-position:center 20% !important;','object-position:center 72% !important;',1)
p.write_text(s,encoding='utf-8')
print('Raised Karina crop')
# trigger
