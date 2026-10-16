from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
repls=[
('.ins-v2-people-grid{display:grid;grid-template-columns:1fr 1fr .82fr;gap:14px;margin-top:52px;align-items:stretch}', '.ins-v2-people-grid{display:grid;grid-template-columns:minmax(0,300px) minmax(0,300px) minmax(0,280px);gap:16px;margin-top:44px;align-items:start;justify-content:center}'),
('.ins-v2-person-card,.ins-v2-person-join{min-height:400px;border-radius:16px;overflow:hidden}', '.ins-v2-person-card,.ins-v2-person-join{min-height:360px;border-radius:16px;overflow:hidden}'),
('.ins-v2-person-photo{position:relative;flex:1;min-height:285px;overflow:hidden;background:#E8ECF7}', '.ins-v2-person-photo{position:relative;height:255px;min-height:255px;overflow:hidden;background:#E8ECF7}'),
('.ins-v2-person-meta{min-height:88px;padding:16px 18px;display:flex;align-items:center;justify-content:space-between;gap:18px}', '.ins-v2-person-meta{min-height:82px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:16px}'),
('  .ins-v2-people-grid{grid-template-columns:1fr 1fr}', '  .ins-v2-people-grid{grid-template-columns:minmax(0,300px) minmax(0,300px);justify-content:center}'),
('  .ins-v2-person-join{grid-column:1/-1;min-height:300px}', '  .ins-v2-person-join{grid-column:1/-1;min-height:240px}'),
('  .ins-v2-people-grid{grid-template-columns:1fr;margin-top:34px;gap:10px}', '  .ins-v2-people-grid{grid-template-columns:1fr;margin-top:34px;gap:10px;justify-content:stretch}'),
('  .ins-v2-person-photo{min-height:270px}', '  .ins-v2-person-photo{height:250px;min-height:250px}')
]
for old,new in repls:
    if old not in s:
        raise SystemExit(f'target not found: {old}')
    s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Compacted Insiders cards width and height')
