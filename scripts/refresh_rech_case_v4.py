from pathlib import Path
import re

p = Path('casos/rech.html')
s = p.read_text(encoding='utf-8')

# Remove the over-designed 4-card build grid.
s = re.sub(r'\s*<div class="rech-v4-build-grid".*?</div>\s*(?=<div class="[^"]*case-new-gallery)', '\n      ', s, flags=re.S)

# Keep the stronger narrative, but make the three moments editorial instead of card-heavy.
s = s.replace('De una red dispersa<br><strong>a un sistema que se entiende.</strong>', 'El desafío no era verse mejor.<br><strong>Era hacer visible la red.</strong>')
s = s.replace('No diseñamos una página.<br><strong>Construimos un sistema digital.</strong>', 'Una identidad compartida.<br><strong>Muchas formas de vivirla.</strong>')
s = s.replace('Cada pieza tenía que cumplir un rol: explicar la red, representar a sus colegios, ordenar la información y hacer visible la vida que ocurre dentro de sus comunidades.', 'Trabajamos la experiencia digital como una sola historia: una red reconocible, colegios con identidad propia y contenido capaz de mostrar lo que pasa dentro de cada comunidad.')

# Replace previous v4 styling with a quieter editorial system.
css = '''
<style id="rech-story-refresh-v4">
.case-rech-hero h1{max-width:1020px!important}
.case-rech-hero .case-new-hero-grid>div:first-child>p{max-width:760px!important;color:#C7D0E2!important}
.case-rech-story{padding-top:138px!important;padding-bottom:108px!important;background:#fff!important}
.case-rech-story .case-new-story-head{grid-template-columns:1fr .72fr!important;gap:86px!important;align-items:start!important}
.case-rech-story .case-new-steps.rech-v4-steps{display:block!important;margin-top:64px!important;border-top:1px solid #DDE3ED!important}
.case-rech-story .rech-v4-steps article,.case-rech-story .rech-v4-steps .is-highlight{display:grid!important;grid-template-columns:90px 1fr!important;gap:34px!important;min-height:0!important;padding:34px 0!important;border:0!important;border-bottom:1px solid #DDE3ED!important;border-radius:0!important;background:transparent!important;box-shadow:none!important;overflow:visible!important}
.case-rech-story .rech-v4-steps article:after{display:none!important}
.case-rech-story .rech-v4-steps article>span,.case-rech-story .rech-v4-steps .is-highlight>span{display:block!important;width:auto!important;height:auto!important;padding:0!important;background:transparent!important;color:#1419E0!important;font-size:11px!important;font-weight:600!important;line-height:1.5!important}
.case-rech-story .rech-v4-steps article>div{margin:0!important}
.case-rech-story .rech-v4-steps small,.case-rech-story .rech-v4-steps .is-highlight small{display:block!important;margin:0 0 10px!important;color:#7C879D!important;font-size:9px!important;letter-spacing:.16em!important}
.case-rech-story .rech-v4-steps h3,.case-rech-story .rech-v4-steps .is-highlight h3{max-width:920px!important;margin:0!important;color:#17224F!important;font-size:clamp(20px,2vw,28px)!important;line-height:1.45!important;letter-spacing:-.025em!important;font-weight:400!important}
.case-rech-work.case-new-work{padding-top:108px!important;padding-bottom:118px!important}
.case-rech-work .case-new-work-head{grid-template-columns:1fr .7fr!important;gap:78px!important}
.case-rech-work .case-new-gallery{margin-top:52px!important;gap:14px!important}.case-rech-work .case-new-gallery figure,.case-rech-work .case-new-gallery-copy{border-radius:14px!important}.case-rech-work .case-new-gallery-main{box-shadow:none!important}
.rech-v4-outcome-band{padding:104px 0;background:#fff;border-bottom:1px solid #E6EAF2}.rech-v4-outcome-inner{display:grid;grid-template-columns:.28fr 1.25fr;gap:70px;align-items:start;max-width:1100px}.rech-v4-outcome-inner .case-new-eyebrow{margin:10px 0 0;color:#1419E0!important}.rech-v4-outcome-inner h2{margin:0;color:#071022;font-size:clamp(38px,4.2vw,58px);line-height:1.07;letter-spacing:-.05em;font-weight:300}.rech-v4-outcome-inner h2 strong{display:block;margin-top:10px;color:#1419E0;font-weight:300}.rech-v4-outcome-inner>p:last-child{grid-column:2;margin:22px 0 0;max-width:720px;color:#68748C;font-size:15px;line-height:1.8}
.case-rech-testimonial{margin-top:0!important}
@media(max-width:980px){.rech-v4-outcome-inner{grid-template-columns:1fr;gap:18px}.rech-v4-outcome-inner>p:last-child{grid-column:auto}.case-rech-story .case-new-story-head,.case-rech-work .case-new-work-head{grid-template-columns:1fr!important;gap:28px!important}}
@media(max-width:760px){.case-rech-story{padding-top:100px!important;padding-bottom:72px!important}.case-rech-story .case-new-steps.rech-v4-steps{margin-top:38px!important}.case-rech-story .rech-v4-steps article,.case-rech-story .rech-v4-steps .is-highlight{grid-template-columns:52px 1fr!important;gap:16px!important;padding:24px 0!important}.case-rech-story .rech-v4-steps h3,.case-rech-story .rech-v4-steps .is-highlight h3{font-size:18px!important}.rech-v4-outcome-band{padding:72px 0}.rech-v4-outcome-inner h2{font-size:34px}}
</style>
'''
s = re.sub(r'<style id="rech-story-refresh-v4">.*?</style>\s*', '', s, flags=re.S)
s = s.replace('</head>', css + '\n</head>', 1)
p.write_text(s, encoding='utf-8')
