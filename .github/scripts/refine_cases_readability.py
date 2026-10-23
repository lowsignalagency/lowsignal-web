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
/* Final readability pass for testimonial-style Customer Stories */
.stories-new-card .stories-new-meta{
  color:#B7C0D4!important;
}
.stories-new-card .stories-new-meta b{
  color:#9BB0FF!important;
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

if style_id not in s:
    s = s.replace('</head>', style + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('Refined Customer Stories readability')
