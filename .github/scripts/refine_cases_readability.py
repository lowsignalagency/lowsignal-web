from pathlib import Path

p = Path('casos.html')
s = p.read_text(encoding='utf-8')

old = '<h2>Estrategia que se ejecuta.<br><strong>Crecimiento que se sostiene.</strong></h2>'
new = '''<h2>Estrategia que se ejecuta.</h2>
          <p class="stories-new-proof-intro-v3">Conectamos estrategia, ejecución, aprendizaje y mejora continua para construir crecimiento que se sostiene en el tiempo.</p>'''
if old in s:
    s = s.replace(old, new, 1)

style_id = 'cases-readability-v3'
style = r'''
<style id="cases-readability-v3">
/* Final readability + color refinement for testimonial-style Customer Stories */
.stories-new-card .stories-new-meta{
  color:#B7C0D4!important;
}
.stories-new-card .stories-new-meta b{
  color:#AFC0FF!important;
}
.stories-new-card .stories-new-meta span:before{
  background:#77839E!important;
}
.stories-new-outcome{
  background:transparent!important;
  border-radius:0!important;
  padding:15px 0 0!important;
  border-top:1px solid rgba(255,255,255,.15)!important;
  box-shadow:none!important;
}
.stories-new-outcome>span{
  color:#AFC0FF!important;
  font-size:9px!important;
}
.stories-new-outcome>p{
  color:#D7DDEC!important;
  font-size:12px!important;
  line-height:1.58!important;
}
.stories-new-link{
  color:#FFFFFF!important;
  opacity:1!important;
}

/* Softer testimonial-style accent instead of electric blue */
.stories-new-list .stories-new-eyebrow,
.stories-new-list h2 strong{
  color:#8AA4FF!important;
}
.stories-new-list h2 strong{
  font-weight:600!important;
}
.stories-new-filter.is-active{
  background:#2435C7!important;
  border-color:#4358E8!important;
  color:#FFFFFF!important;
}

/* CTA card: dark premium treatment, not saturated blue */
.stories-new-cta-card{
  background:
    radial-gradient(80% 90% at 100% 0%,rgba(138,164,255,.22),transparent 68%),
    linear-gradient(145deg,#111A39 0%,#18265A 100%)!important;
  border:1px solid rgba(138,164,255,.24)!important;
  box-shadow:0 20px 50px rgba(0,0,0,.20)!important;
}
.stories-new-cta-card:after{
  background:radial-gradient(60% 70% at 100% 0%,rgba(138,164,255,.12),transparent 72%)!important;
}
.stories-new-cta-card>span{
  color:#AFC0FF!important;
}
.stories-new-cta-card h3{
  color:#FFFFFF!important;
}
.stories-new-cta-card h3 strong{
  color:#A8B8FF!important;
  font-weight:600!important;
}
.stories-new-cta-card b{
  display:inline-flex!important;
  width:auto!important;
  margin-top:24px!important;
  padding:12px 16px!important;
  border-radius:10px!important;
  background:#A8B8FF!important;
  color:#071022!important;
  border:1px solid #BBC8FF!important;
  font-size:11px!important;
  font-weight:700!important;
  box-shadow:none!important;
}
.stories-new-cta-card:hover b{
  background:#BDC9FF!important;
}
/* Override broad inherited CTA color rule */
.stories-new-cta-card b,
.stories-new-cta-card b *{
  color:#071022!important;
}

.stories-new-proof-head{
  max-width:680px!important;
}
.stories-new-proof h2{
  max-width:640px!important;
  margin-top:16px!important;
  font-size:clamp(42px,4.6vw,60px)!important;
  line-height:1.04!important;
  letter-spacing:-.05em!important;
}
.stories-new-proof-intro-v3{
  max-width:580px!important;
  margin:24px 0 0!important;
  color:#AAB5CE!important;
  font-size:15px!important;
  line-height:1.75!important;
}
@media(max-width:680px){
  .stories-new-proof h2{font-size:40px!important}
  .stories-new-proof-intro-v3{font-size:14px!important;line-height:1.68!important}
}
</style>
'''

if f'<style id="{style_id}">' in s:
    start = s.index(f'<style id="{style_id}">')
    end = s.index('</style>', start) + len('</style>')
    s = s[:start] + style.strip() + s[end:]
else:
    s = s.replace('</head>', style + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('Refined Customer Stories readability and colors')
