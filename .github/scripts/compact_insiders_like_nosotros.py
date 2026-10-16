from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
repls=[
('.ins-v2-people-grid{display:grid;grid-template-columns:minmax(0,300px) minmax(0,300px) minmax(0,280px);gap:16px;margin-top:44px;align-items:start;justify-content:center}', '.ins-v2-people-grid{display:grid;grid-template-columns:minmax(0,260px) minmax(0,260px) minmax(0,250px);gap:22px;margin-top:44px;align-items:start;justify-content:center}'),
('.ins-v2-person-card,.ins-v2-person-join{min-height:360px;border-radius:16px;overflow:hidden}', '.ins-v2-person-card,.ins-v2-person-join{min-height:310px;border-radius:16px;overflow:hidden}'),
('.ins-v2-person-photo{position:relative;height:255px;min-height:255px;overflow:hidden;background:#E8ECF7}', '.ins-v2-person-photo{position:relative;height:220px;min-height:220px;overflow:hidden;background:#E8ECF7}'),
('.ins-v2-person-meta{min-height:82px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:16px}', '.ins-v2-person-meta{min-height:74px;padding:12px 14px;display:flex;align-items:center;justify-content:space-between;gap:14px}'),
('  .ins-v2-people-grid{grid-template-columns:minmax(0,300px) minmax(0,300px);justify-content:center}', '  .ins-v2-people-grid{grid-template-columns:minmax(0,260px) minmax(0,260px);justify-content:center}'),
('  .ins-v2-person-join{grid-column:1/-1;min-height:240px}', '  .ins-v2-person-join{grid-column:1/-1;min-height:220px}'),
('  .ins-v2-person-photo{height:250px;min-height:250px}', '  .ins-v2-person-photo{height:230px;min-height:230px}')
]
for old,new in repls:
    if old not in s:
        raise SystemExit(f'target not found: {old}')
    s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Made Insiders people cards smaller to match Nosotros rhythm')
