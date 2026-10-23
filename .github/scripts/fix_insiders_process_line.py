from pathlib import Path
p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')
s = s.replace('  border-top:1px solid #CDD6E8!important;\n  border-bottom:1px solid #CDD6E8!important;', '  border-top:0!important;\n  border-bottom:1px solid #CDD6E8!important;')
p.write_text(s, encoding='utf-8')
print('fix-insiders-process-line-v1')
