from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
repls=[
('.ins-v2-person-card,.ins-v2-person-join{min-height:310px;border-radius:16px;overflow:hidden}', '.ins-v2-person-join{min-height:310px;border-radius:16px;overflow:hidden}'),
('.ins-v2-person-card{border:1px solid #DCE3F2;background:#F8FAFF;display:flex;flex-direction:column}', '.ins-v2-person-card{background:transparent;border:0;display:block;min-height:0;overflow:visible}'),
('.ins-v2-person-photo{position:relative;height:220px;min-height:220px;overflow:hidden;background:#E8ECF7}', '.ins-v2-person-photo{position:relative;aspect-ratio:1 / 1.13;height:auto;min-height:0;overflow:hidden;border-radius:16px;background:#ECEFF4;box-shadow:none}'),
('.ins-v2-person-photo:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 60%,rgba(7,15,34,.32) 100%);pointer-events:none}\n',''),
('.ins-v2-person-photo img{width:100%;height:100%;object-fit:cover;object-position:center 24%;transition:transform .45s cubic-bezier(.2,.75,.2,1)}', '.ins-v2-person-photo img{width:100%;height:100%;object-fit:cover;object-position:center top;transition:transform .45s cubic-bezier(.2,.75,.2,1)}'),
('.ins-v2-person-meta{min-height:74px;padding:12px 14px;display:flex;align-items:center;justify-content:space-between;gap:14px}', '.ins-v2-person-meta{min-height:0;padding:14px 0 0;display:block}'),
('.ins-v2-person-meta h3{margin:0;color:#15204A;font-size:20px;letter-spacing:-.025em}', '.ins-v2-person-meta h3{margin:0;color:#10182A;font-size:16px;line-height:1.25;font-weight:600;letter-spacing:-.02em}'),
('.ins-v2-person-meta p{margin:5px 0 0;color:#7A86A7;font-size:11px}', '.ins-v2-person-meta p{margin:4px 0 0;color:#60708B;font-size:13px;line-height:1.45}'),
('  .ins-v2-people-grid{grid-template-columns:minmax(0,260px) minmax(0,260px);justify-content:start}\n  .ins-v2-person-join{grid-column:auto;min-height:310px}', '  .ins-v2-people-grid{grid-template-columns:repeat(2,minmax(0,260px));justify-content:start}\n  .ins-v2-person-join{grid-column:1/-1;max-width:542px;min-height:220px}'),
('  .ins-v2-people-grid{grid-template-columns:1fr;margin-top:34px;gap:10px;justify-content:stretch}\n  .ins-v2-person-card,.ins-v2-person-join{min-height:0;border-radius:16px}\n  .ins-v2-person-photo{height:230px;min-height:230px}\n  .ins-v2-person-meta{min-height:82px;padding:16px}\n  .ins-v2-person-join{grid-column:auto;min-height:260px;padding:20px}', '  .ins-v2-people-grid{grid-template-columns:repeat(2,minmax(0,1fr));margin-top:34px;gap:34px 16px;justify-content:stretch}\n  .ins-v2-person-photo{aspect-ratio:1 / 1.14;border-radius:14px}\n  .ins-v2-person-meta{padding-top:12px}\n  .ins-v2-person-meta h3{font-size:15px}\n  .ins-v2-person-meta p{font-size:11px}\n  .ins-v2-person-join{grid-column:1/-1;min-height:220px;max-width:none;padding:20px}'),
('</style>\n</head>', '@media(max-width:480px){\n  .ins-v2-people-grid{grid-template-columns:1fr}\n  .ins-v2-person-photo{aspect-ratio:1 / 1.08}\n  .ins-v2-person-join{grid-column:auto}\n}\n</style>\n</head>')
]
for old,new in repls:
    if old not in s:
        raise SystemExit(f'target not found: {old[:160]}')
    s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Matched Insiders profile presentation to Nosotros team cards')
