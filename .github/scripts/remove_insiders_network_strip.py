from pathlib import Path
import re
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
pattern=r'\n\s*<section class="ins-v2-network-strip" aria-label="Red nacional de lowsignal Insiders">.*?</section>\n'
s2,n=re.subn(pattern,'\n',s,count=1,flags=re.S)
if n!=1:
    raise SystemExit(f'network strip html not removed: {n}')
s=s2
for css in [
'.ins-v2-network-strip{background:#0B1430;color:#fff;border-top:1px solid rgba(138,164,255,.14);border-bottom:1px solid rgba(138,164,255,.14)}\n',
'.ins-v2-network-strip-inner{min-height:150px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}\n',
'.ins-v2-network-kicker{display:block;margin-bottom:10px;color:#8EA3FF;font-size:8px;font-weight:700;letter-spacing:.19em}\n',
'.ins-v2-network-strip strong{display:block;font-size:clamp(28px,2.5vw,36px);line-height:1.08;letter-spacing:-.035em;font-weight:300}\n',
'.ins-v2-network-strip p{max-width:520px;margin:0;color:#98A5C5;font-size:13px;line-height:1.68}\n',
'  .ins-v2-network-strip-inner{min-height:0;padding-top:32px;padding-bottom:32px;grid-template-columns:1fr;gap:14px}\n',
'  .ins-v2-network-strip strong{font-size:28px}\n'
]:
    s=s.replace(css,'')
p.write_text(s,encoding='utf-8')
print('Removed Insiders network strip')
