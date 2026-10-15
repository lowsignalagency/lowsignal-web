from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
old='''.ins-v2-network-strip-inner{min-height:190px;display:grid;grid-template-columns:1.08fr .92fr;gap:72px;align-items:center}\n.ins-v2-network-kicker{display:block;margin-bottom:16px;color:#8EA3FF;font-size:9px;font-weight:700;letter-spacing:.19em}\n.ins-v2-network-strip strong{display:block;font-size:clamp(34px,4vw,56px);line-height:1;letter-spacing:-.045em;font-weight:300}\n.ins-v2-network-strip p{max-width:560px;margin:0;color:#98A5C5;font-size:14px;line-height:1.72}'''
new='''.ins-v2-network-strip-inner{min-height:150px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}\n.ins-v2-network-kicker{display:block;margin-bottom:10px;color:#8EA3FF;font-size:8px;font-weight:700;letter-spacing:.19em}\n.ins-v2-network-strip strong{display:block;font-size:clamp(28px,2.5vw,36px);line-height:1.08;letter-spacing:-.035em;font-weight:300}\n.ins-v2-network-strip p{max-width:520px;margin:0;color:#98A5C5;font-size:13px;line-height:1.68}'''
if old not in s:
    raise SystemExit('target styles not found')
s=s.replace(old,new,1)
s=s.replace('  .ins-v2-network-strip strong{font-size:34px}','  .ins-v2-network-strip strong{font-size:28px}',1)
p.write_text(s,encoding='utf-8')
print('Reduced Insiders network strip')
