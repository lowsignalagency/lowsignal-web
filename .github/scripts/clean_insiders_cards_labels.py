from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
for token in [
'            <span>INSIDER / 01</span>\n',
'            <span>INSIDER / 02</span>\n',
'          <b>lowsignal insiders</b>\n',
'.ins-v2-person-photo>span{position:absolute;z-index:2;left:18px;top:18px;padding:7px 9px;border:1px solid rgba(255,255,255,.28);border-radius:999px;background:rgba(7,15,34,.34);backdrop-filter:blur(8px);color:#fff;font-size:8px;font-weight:700;letter-spacing:.14em}\n',
'.ins-v2-person-meta b{color:#5365D9;font-size:8px;font-weight:700;letter-spacing:.13em;text-transform:uppercase}\n',
'  .ins-v2-person-meta b{display:none}\n'
]:
    s=s.replace(token,'')
p.write_text(s,encoding='utf-8')
print('Cleaned all Insiders profile labels')
