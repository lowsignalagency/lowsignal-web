from pathlib import Path

p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')

if 'ins-v2-people' in s:
    raise SystemExit('People section already exists')

anchor = '  <section class="ins-v2-audience">'
if anchor not in s:
    raise SystemExit('Audience anchor not found')

section = '''  <section class="ins-v2-people" aria-labelledby="insiders-people-title">
    <div class="ls-social-shell">
      <div class="ins-v2-people-head">
        <div>
          <p class="ins-v2-eyebrow">THE NETWORK</p>
          <h2 id="insiders-people-title">Esto recién empieza.<br><strong>Súmate a la red.</strong></h2>
        </div>
        <p>Joaquín y Samuel ya son parte de lowsignal Insiders. Estamos sumando personas de todo Chile con criterio, buenas conexiones y ganas de mover oportunidades.</p>
      </div>

      <div class="ins-v2-people-grid">
        <article class="ins-v2-person-card">
          <div class="ins-v2-person-photo">
            <img src="https://lowsignal.cl/assets/joaquin.png" alt="Joaquín, Growth Ambassador de lowsignal" loading="lazy">
            <span>INSIDER / 01</span>
          </div>
          <div class="ins-v2-person-meta">
            <div><h3>Joaquín</h3><p>Growth Ambassador</p></div>
            <b>lowsignal insiders</b>
          </div>
        </article>

        <article class="ins-v2-person-card">
          <div class="ins-v2-person-photo">
            <img src="https://lowsignal.cl/assets/samuel.png" alt="Samuel, Growth Ambassador de lowsignal" loading="lazy">
            <span>INSIDER / 02</span>
          </div>
          <div class="ins-v2-person-meta">
            <div><h3>Samuel</h3><p>Growth Ambassador</p></div>
            <b>lowsignal insiders</b>
          </div>
        </article>

        <article class="ins-v2-person-join">
          <span>YOUR SPOT?</span>
          <div>
            <h3>Tu nombre podría<br>estar acá.</h3>
            <p>Si tienes red, criterio y sabes detectar una buena oportunidad cuando la ves, queremos conocerte.</p>
          </div>
          <a href="mailto:contacto@lowsignal.cl?subject=Quiero%20ser%20Insider">Quiero ser Insider <span>↗</span></a>
        </article>
      </div>
    </div>
  </section>\n\n'''

s = s.replace(anchor, section + anchor, 1)

style = '''\n<style id="insiders-v7-ambassadors">\n.ins-v2-people{padding:108px 0 116px;background:#fff}\n.ins-v2-people-head{display:grid;grid-template-columns:1fr .72fr;gap:72px;align-items:end}\n.ins-v2-people-head h2{margin:20px 0 0;color:#10193C;font-size:clamp(36px,3.9vw,54px);line-height:1.09;letter-spacing:-.043em;font-weight:300}\n.ins-v2-people-head h2 strong{color:#1419E0;font-weight:300}\n.ins-v2-people-head>p{max-width:520px;margin:0;color:#7A86A7;font-size:14px;line-height:1.72}\n.ins-v2-people-grid{display:grid;grid-template-columns:1fr 1fr .82fr;gap:14px;margin-top:52px;align-items:stretch}\n.ins-v2-person-card,.ins-v2-person-join{min-height:520px;border-radius:20px;overflow:hidden}\n.ins-v2-person-card{border:1px solid #DCE3F2;background:#F8FAFF;display:flex;flex-direction:column}\n.ins-v2-person-photo{position:relative;flex:1;min-height:410px;overflow:hidden;background:#E8ECF7}\n.ins-v2-person-photo:after{content:\"\";position:absolute;inset:0;background:linear-gradient(180deg,transparent 60%,rgba(7,15,34,.32) 100%);pointer-events:none}\n.ins-v2-person-photo img{width:100%;height:100%;object-fit:cover;object-position:center top;transition:transform .45s cubic-bezier(.2,.75,.2,1)}\n.ins-v2-person-photo>span{position:absolute;z-index:2;left:18px;top:18px;padding:7px 9px;border:1px solid rgba(255,255,255,.28);border-radius:999px;background:rgba(7,15,34,.34);backdrop-filter:blur(8px);color:#fff;font-size:8px;font-weight:700;letter-spacing:.14em}\n.ins-v2-person-card:hover .ins-v2-person-photo img{transform:scale(1.025)}\n.ins-v2-person-meta{min-height:104px;padding:20px 22px;display:flex;align-items:center;justify-content:space-between;gap:20px}\n.ins-v2-person-meta h3{margin:0;color:#15204A;font-size:20px;letter-spacing:-.025em}\n.ins-v2-person-meta p{margin:5px 0 0;color:#7A86A7;font-size:11px}\n.ins-v2-person-meta b{color:#5365D9;font-size:8px;font-weight:700;letter-spacing:.13em;text-transform:uppercase}\n.ins-v2-person-join{padding:28px;background:linear-gradient(145deg,#1419E0 0%,#2447F5 100%);color:#fff;display:flex;flex-direction:column;justify-content:space-between}\n.ins-v2-person-join>span{color:#BFC9FF;font-size:9px;font-weight:700;letter-spacing:.18em}\n.ins-v2-person-join h3{margin:0;font-size:clamp(28px,2.5vw,38px);line-height:1.05;letter-spacing:-.045em;font-weight:300}\n.ins-v2-person-join p{margin:18px 0 0;color:#D7DFFF;font-size:13px;line-height:1.68}\n.ins-v2-person-join>a{min-height:48px;padding:0 16px;border-radius:999px;background:#fff;color:#17235D;display:flex;align-items:center;justify-content:space-between;gap:16px;font-size:11px;font-weight:700;transition:transform .2s ease,box-shadow .2s ease}\n.ins-v2-person-join>a:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(0,0,0,.16)}\n.ins-v2-person-join>a span{font-size:15px}\n@media(max-width:980px){\n  .ins-v2-people-head{grid-template-columns:1fr;gap:26px}\n  .ins-v2-people-grid{grid-template-columns:1fr 1fr}\n  .ins-v2-person-join{grid-column:1/-1;min-height:300px}\n}\n@media(max-width:760px){\n  .ins-v2-people{padding:72px 0}\n  .ins-v2-people-head h2{max-width:340px;font-size:30px;line-height:1.1;letter-spacing:-.038em}\n  .ins-v2-people-grid{grid-template-columns:1fr;margin-top:34px;gap:10px}\n  .ins-v2-person-card,.ins-v2-person-join{min-height:0;border-radius:16px}\n  .ins-v2-person-photo{min-height:380px}\n  .ins-v2-person-meta{min-height:92px;padding:18px}\n  .ins-v2-person-meta b{display:none}\n  .ins-v2-person-join{grid-column:auto;min-height:300px;padding:24px}\n}\n</style>\n'''

s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')
print('Added Insiders ambassadors section')
