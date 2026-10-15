from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')
anchor='''  <section class="ins-v2-audience">'''
if anchor not in s:
    raise SystemExit('audience anchor not found')
section='''  <section class="ins-v2-benefits">
    <div class="ls-social-shell">
      <div class="ins-v2-benefits-head">
        <div>
          <p class="ins-v2-eyebrow">POR QUÉ SER INSIDER</p>
          <h2>Tu red puede abrir puertas.<br><strong>Y también devolverte valor.</strong></h2>
        </div>
        <p>No se trata de vender por vender. Se trata de detectar buenas oportunidades, conectarlas con el equipo correcto y ser parte del upside cuando funcionan.</p>
      </div>

      <div class="ins-v2-benefits-grid">
        <article class="is-featured">
          <span>/ 01</span>
          <div>
            <small>GOOD CONNECTIONS SHOULD HAVE UPSIDE.</small>
            <h3>Tu red vale.</h3>
            <p>Si una conexión termina convirtiéndose en cliente, participas del valor que ayudaste a generar.</p>
          </div>
        </article>
        <article>
          <span>/ 02</span>
          <div>
            <h3>Acceso directo.</h3>
            <p>Conectas oportunidades con el equipo de lowsignal sin tener que vender, negociar ni perseguir el cierre.</p>
          </div>
        </article>
        <article>
          <span>/ 03</span>
          <div>
            <h3>Desde cualquier parte.</h3>
            <p>Arica, Santiago, Concepción o Punta Arenas. Tu ubicación no limita tu capacidad de mover una buena oportunidad.</p>
          </div>
        </article>
        <article>
          <span>/ 04</span>
          <div>
            <h3>Ser parte de la red.</h3>
            <p>Una comunidad de personas conectadas, curiosas y con criterio para detectar dónde puede pasar algo grande.</p>
          </div>
        </article>
      </div>
    </div>
  </section>\n\n'''
s=s.replace(anchor,section+anchor,1)
style='''\n<style id="insiders-v5-value-cards">\n.ins-v2-benefits{padding:108px 0 112px;background:#F4F6FC}\n.ins-v2-benefits-head{display:grid;grid-template-columns:1fr .72fr;gap:72px;align-items:end}\n.ins-v2-benefits-head h2{margin:20px 0 0;color:#10193C;font-size:clamp(36px,3.9vw,54px);line-height:1.09;letter-spacing:-.043em;font-weight:300}\n.ins-v2-benefits-head h2 strong{color:#1419E0;font-weight:300}\n.ins-v2-benefits-head>p{margin:0;color:#7A86A7;font-size:14px;line-height:1.7}\n.ins-v2-benefits-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:52px}\n.ins-v2-benefits-grid article{min-height:250px;padding:26px;border:1px solid #DCE3F2;border-radius:18px;background:#fff;display:flex;flex-direction:column;justify-content:space-between;transition:.2s ease}\n.ins-v2-benefits-grid article:hover{transform:translateY(-3px);border-color:#C9D3EC;box-shadow:0 16px 34px rgba(20,25,224,.06)}\n.ins-v2-benefits-grid article>span{color:#5365D9;font-size:10px;font-weight:700}\n.ins-v2-benefits-grid h3{margin:10px 0 0;color:#15204A;font-size:24px;letter-spacing:-.03em}\n.ins-v2-benefits-grid p{max-width:520px;margin:10px 0 0;color:#7A86A7;font-size:13px;line-height:1.65}\n.ins-v2-benefits-grid small{display:block;margin-bottom:24px;color:#8EA3FF;font-size:9px;font-weight:700;letter-spacing:.16em}\n.ins-v2-benefits-grid .is-featured{background:linear-gradient(135deg,#1419E0,#2447F5);border-color:transparent;color:#fff}\n.ins-v2-benefits-grid .is-featured>span,.ins-v2-benefits-grid .is-featured h3{color:#fff}\n.ins-v2-benefits-grid .is-featured p{color:#D7DFFF}\n@media(max-width:980px){.ins-v2-benefits-head{grid-template-columns:1fr;gap:26px}}\n@media(max-width:760px){\n  .ins-v2-benefits{padding:72px 0}\n  .ins-v2-benefits-head h2{max-width:340px;font-size:30px;line-height:1.10;letter-spacing:-.038em}\n  .ins-v2-benefits-grid{grid-template-columns:1fr;margin-top:34px;gap:10px}\n  .ins-v2-benefits-grid article{min-height:190px;padding:22px;border-radius:15px}\n}\n</style>\n'''
s=s.replace('</head>',style+'</head>',1)
p.write_text(s,encoding='utf-8')
print('Added Insiders value cards')
