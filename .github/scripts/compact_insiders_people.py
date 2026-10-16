from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
s=s.replace('.ins-v2-person-card,.ins-v2-person-join{min-height:520px;', '.ins-v2-person-card,.ins-v2-person-join{min-height:460px;', 1)
s=s.replace('.ins-v2-person-photo{position:relative;flex:1;min-height:410px;', '.ins-v2-person-photo{position:relative;flex:1;min-height:340px;', 1)
s=s.replace('  .ins-v2-person-photo{min-height:380px}', '  .ins-v2-person-photo{min-height:320px}', 1)
p.write_text(s,encoding='utf-8')
print('Compacted Insiders people cards')
