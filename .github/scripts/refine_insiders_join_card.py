from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
repls=[
('.ins-v2-people-grid{display:grid;grid-template-columns:minmax(0,260px) minmax(0,260px) minmax(0,250px);gap:22px;margin-top:44px;align-items:start;justify-content:start}', '.ins-v2-people-grid{display:grid;grid-template-columns:repeat(3,minmax(0,260px));gap:22px;margin-top:44px;align-items:start;justify-content:start}'),
('.ins-v2-person-join{padding:28px;background:linear-gradient(145deg,#1419E0 0%,#2447F5 100%);color:#fff;display:flex;flex-direction:column;justify-content:space-between}', '.ins-v2-person-join{padding:20px;background:linear-gradient(145deg,#1419E0 0%,#2447F5 100%);color:#fff;display:flex;flex-direction:column;justify-content:space-between}'),
('.ins-v2-person-join>span{color:#BFC9FF;font-size:9px;font-weight:700;letter-spacing:.18em}', '.ins-v2-person-join>span{color:#C9D2FF;font-size:8px;font-weight:700;letter-spacing:.16em}'),
('.ins-v2-person-join h3{margin:0;font-size:clamp(28px,2.5vw,38px);line-height:1.05;letter-spacing:-.045em;font-weight:300}', '.ins-v2-person-join h3{margin:0;font-size:22px;line-height:1.12;letter-spacing:-.035em;font-weight:400}'),
('.ins-v2-person-join p{margin:18px 0 0;color:#D7DFFF;font-size:13px;line-height:1.68}', '.ins-v2-person-join p{margin:12px 0 0;color:#D7DFFF;font-size:11.5px;line-height:1.6}'),
('.ins-v2-person-join>a{min-height:48px;padding:0 16px;border-radius:999px;background:#fff;color:#17235D;display:flex;align-items:center;justify-content:space-between;gap:16px;font-size:11px;font-weight:700;transition:transform .2s ease,box-shadow .2s ease}', '.ins-v2-person-join>a{min-height:42px;padding:0 14px;border-radius:999px;background:#fff;color:#17235D;display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:10px;font-weight:700;transition:transform .2s ease,box-shadow .2s ease}'),
('  .ins-v2-person-join{grid-column:1/-1;min-height:220px}', '  .ins-v2-person-join{grid-column:auto;min-height:310px}'),
('  .ins-v2-person-join{grid-column:auto;min-height:300px;padding:24px}', '  .ins-v2-person-join{grid-column:auto;min-height:260px;padding:20px}')
]
for old,new in repls:
    if old not in s:
        raise SystemExit(f'target not found: {old}')
    s=s.replace(old,new,1)
old_html='''        <article class="ins-v2-person-join">\n          <span>YOUR SPOT?</span>\n          <div>\n            <h3>Tu nombre podría<br>estar acá.</h3>\n            <p>Si tienes red, criterio y sabes detectar una buena oportunidad cuando la ves, queremos conocerte.</p>\n          </div>\n          <a href="mailto:contacto@lowsignal.cl?subject=Quiero%20ser%20Insider">Quiero ser Insider <span>↗</span></a>'''
new_html='''        <article class="ins-v2-person-join">\n          <span>SÚMATE A LA RED</span>\n          <div>\n            <h3>Tu red puede abrir lo que viene.</h3>\n            <p>Conecta una buena oportunidad con lowsignal y sé parte de Insiders.</p>\n          </div>\n          <a href="mailto:contacto@lowsignal.cl?subject=Quiero%20ser%20Insider">Quiero ser Insider <span>↗</span></a>'''
if old_html not in s:
    raise SystemExit('join card html target not found')
s=s.replace(old_html,new_html,1)
p.write_text(s,encoding='utf-8')
print('Refined Insiders join card')
