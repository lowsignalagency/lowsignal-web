from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
html='''<section class="ins-v2-network-strip" aria-label="Red nacional de lowsignal Insiders">\n  <div class="ls-social-shell ins-v2-network-strip-inner">\n    <div>\n      <span class="ins-v2-network-kicker">RED NACIONAL</span>\n      <strong>ARICA → PUNTA ARENAS</strong>\n    </div>\n    <p>Una red distribuida por Chile para detectar buenas oportunidades, abrir conversaciones y conectar empresas con lowsignal.</p>\n  </div>\n</section>\n'''
if html not in s:
    raise SystemExit('network strip html not found')
s=s.replace(html,'',1)
css='''.ins-v2-network-strip{background:#0B1430;color:#fff;border-top:1px solid rgba(138,164,255,.14);border-bottom:1px solid rgba(138,164,255,.14)}\n.ins-v2-network-strip-inner{min-height:150px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}\n.ins-v2-network-kicker{display:block;margin-bottom:10px;color:#8EA3FF;font-size:8px;font-weight:700;letter-spacing:.19em}\n.ins-v2-network-strip strong{display:block;font-size:clamp(28px,2.5vw,36px);line-height:1.08;letter-spacing:-.035em;font-weight:300}\n.ins-v2-network-strip p{max-width:520px;margin:0;color:#98A5C5;font-size:13px;line-height:1.68}\n'''
s=s.replace(css,'',1)
mobile='''  .ins-v2-network-strip-inner{min-height:0;padding-top:32px;padding-bottom:32px;grid-template-columns:1fr;gap:14px}\n  .ins-v2-network-strip strong{font-size:28px}\n'''
s=s.replace(mobile,'',1)
p.write_text(s,encoding='utf-8')
print('Removed Insiders network strip')
