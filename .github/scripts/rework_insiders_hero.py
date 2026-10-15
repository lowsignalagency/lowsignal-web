from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')

# Insert a standalone national-network strip after the hero and before How it works.
anchor='''  </section>\n\n  <section class="ins-v2-how" id="como-funciona">'''
if anchor not in s:
    raise SystemExit('Hero/how anchor not found')

section='''  </section>\n\n  <section class="ins-v2-network-strip" aria-label="Red nacional de lowsignal Insiders">\n    <div class="ls-social-shell ins-v2-network-strip-inner">\n      <div>\n        <span class="ins-v2-network-kicker">RED NACIONAL</span>\n        <strong>ARICA → PUNTA ARENAS</strong>\n      </div>\n      <p>Una red distribuida por Chile para detectar buenas oportunidades, abrir conversaciones y conectar empresas con lowsignal.</p>\n    </div>\n  </section>\n\n  <section class="ins-v2-how" id="como-funciona">'''
if 'class="ins-v2-network-strip"' not in s:
    s=s.replace(anchor,section,1)

style='''\n<style id="insiders-v6-hero-fullwidth">\n/* Full-width Insiders hero: keep the headline as the main event */\n.ins-v2-hero-grid{grid-template-columns:1fr!important;gap:0!important}\n.ins-v2-copy{max-width:1120px!important}\n.ins-v2-hero h1{max-width:1120px!important}\n.ins-v2-lead{max-width:860px!important}\n.ins-v2-reward{display:none!important}\n\n.ins-v2-network-strip{background:#0B1430;color:#fff;border-top:1px solid rgba(138,164,255,.14);border-bottom:1px solid rgba(138,164,255,.14)}\n.ins-v2-network-strip-inner{min-height:190px;display:grid;grid-template-columns:1.08fr .92fr;gap:72px;align-items:center}\n.ins-v2-network-kicker{display:block;margin-bottom:16px;color:#8EA3FF;font-size:9px;font-weight:700;letter-spacing:.19em}\n.ins-v2-network-strip strong{display:block;font-size:clamp(34px,4vw,56px);line-height:1;letter-spacing:-.045em;font-weight:300}\n.ins-v2-network-strip p{max-width:560px;margin:0;color:#98A5C5;font-size:14px;line-height:1.72}\n@media(max-width:760px){\n  .ins-v2-hero h1{max-width:360px!important}\n  .ins-v2-network-strip-inner{min-height:0;padding-top:40px;padding-bottom:40px;grid-template-columns:1fr;gap:18px}\n  .ins-v2-network-strip strong{font-size:34px}\n}\n</style>\n'''
if 'insiders-v6-hero-fullwidth' not in s:
    s=s.replace('</head>',style+'</head>',1)

p.write_text(s,encoding='utf-8')
print('Reworked Insiders hero and moved national-network message below hero')
