from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
repls=[
('.ins-v2-person-card,.ins-v2-person-join{min-height:460px;border-radius:20px;overflow:hidden}', '.ins-v2-person-card,.ins-v2-person-join{min-height:400px;border-radius:16px;overflow:hidden}'),
('.ins-v2-person-photo{position:relative;flex:1;min-height:340px;overflow:hidden;background:#E8ECF7}', '.ins-v2-person-photo{position:relative;flex:1;min-height:285px;overflow:hidden;background:#E8ECF7}'),
('.ins-v2-person-meta{min-height:104px;padding:20px 22px;display:flex;align-items:center;justify-content:space-between;gap:20px}', '.ins-v2-person-meta{min-height:88px;padding:16px 18px;display:flex;align-items:center;justify-content:space-between;gap:18px}'),
('  .ins-v2-person-photo{min-height:320px}', '  .ins-v2-person-photo{min-height:270px}'),
('  .ins-v2-person-meta{min-height:92px;padding:18px}', '  .ins-v2-person-meta{min-height:82px;padding:16px}')
]
for old,new in repls:
    if old not in s:
        raise SystemExit(f'target not found: {old}')
    s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Compacted Insiders people cards v2')
