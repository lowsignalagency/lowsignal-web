from pathlib import Path

p = Path('casos.html')
s = p.read_text(encoding='utf-8')

# Use the same stronger imagery already used in the B2C testimonial section.
s = s.replace('https://lowsignal.cl/assets/dulce-local.jpg', 'https://lowsignal.cl/assets/dulce-reino-pasteleria.jpg')
s = s.replace('https://lowsignal.cl/assets/dimor-truck.jpg', 'https://lowsignal.cl/assets/dimor-concesionario.png')

style_id = 'cases-showcase-v2'
style = r'''
<style id="cases-showcase-v2">
/* Customer Stories — editorial portfolio treatment */
.stories-new-featured{
  padding:78px 0 92px!important;
  background:#fff!important;
}
.stories-new-feature{
  grid-template-columns:1.08fr .92fr!important;
  min-height:570px!important;
  border:0!important;
  border-radius:26px!important;
  background:#071022!important;
  box-shadow:0 26px 70px rgba(7,15,34,.13)!important;
}
.stories-new-feature-media{min-height:570px!important}
.stories-new-feature-media:after{
  background:linear-gradient(180deg,rgba(7,15,34,.02) 40%,rgba(7,15,34,.68) 100%)!important;
}
.stories-new-feature-copy{
  padding:54px 50px!important;
  background:#071022!important;
  color:#fff!important;
}
.stories-new-feature .stories-new-meta{color:#8D99B6!important}
.stories-new-feature .stories-new-meta b{color:#8AA4FF!important}
.stories-new-feature h2{
  color:#fff!important;
  font-size:clamp(36px,3.35vw,50px)!important;
}
.stories-new-feature h2 strong{color:#A8B8FF!important;font-weight:300!important}
.stories-new-feature blockquote{
  color:#C4CCE0!important;
  border-left-color:#647CFF!important;
  font-size:15px!important;
  line-height:1.72!important;
}
.stories-new-person b{color:#fff!important}
.stories-new-person span{color:#8D99B6!important}
.stories-new-feature-link{color:#A8B8FF!important}

.stories-new-list{
  padding:108px 0 118px!important;
  background:#F6F8FC!important;
}
.stories-new-list-head{margin-bottom:8px!important}
.stories-new-list h2{
  max-width:760px!important;
  font-size:clamp(40px,4vw,58px)!important;
  line-height:1.06!important;
  letter-spacing:-.045em!important;
}
.stories-new-filters{gap:8px!important}
.stories-new-filter{
  padding:10px 15px!important;
  border-color:#DDE4F0!important;
  background:#fff!important;
  color:#52607E!important;
}
.stories-new-filter.is-active{
  background:#071022!important;
  border-color:#071022!important;
  color:#fff!important;
}

body .stories-new-list .container .stories-new-grid{
  grid-template-columns:repeat(2,minmax(0,1fr))!important;
  gap:26px!important;
  margin-top:50px!important;
}
.stories-new-card{
  min-height:590px!important;
  border:1px solid #E0E6F0!important;
  border-radius:24px!important;
  background:#fff!important;
  box-shadow:0 8px 24px rgba(7,15,34,.04)!important;
  overflow:hidden!important;
  transition:transform .28s ease,box-shadow .28s ease,border-color .28s ease!important;
}
.stories-new-card:hover{
  transform:translateY(-7px)!important;
  border-color:#CAD4E7!important;
  box-shadow:0 24px 56px rgba(7,15,34,.11)!important;
}
.stories-new-card-media{
  height:330px!important;
  background:#0A1226!important;
}
.stories-new-photo{
  width:100%!important;
  height:100%!important;
  object-fit:cover!important;
  transition:transform .45s cubic-bezier(.2,.7,.2,1)!important;
}
.stories-new-card:hover .stories-new-photo{transform:scale(1.025)!important}
.stories-new-card-shade{
  background:linear-gradient(180deg,rgba(7,15,34,.04) 38%,rgba(7,15,34,.67) 100%)!important;
}
.stories-new-logo{
  left:24px!important;
  bottom:22px!important;
  max-width:150px!important;
  max-height:48px!important;
}
.stories-new-card-body{
  min-height:258px!important;
  padding:28px 30px 26px!important;
  display:flex!important;
  flex-direction:column!important;
}
.stories-new-meta{font-size:11px!important}
.stories-new-meta b{font-size:9px!important;letter-spacing:.16em!important}
.stories-new-card h3{
  min-height:0!important;
  margin:15px 0 0!important;
  font-size:clamp(23px,2vw,28px)!important;
  line-height:1.19!important;
  letter-spacing:-.035em!important;
  font-weight:400!important;
}
.stories-new-outcome{
  margin-top:20px!important;
  padding-top:17px!important;
  border-top:1px solid #E8ECF3!important;
}
.stories-new-outcome>span{
  display:block!important;
  color:#5365D9!important;
  font-size:8px!important;
  font-weight:700!important;
  letter-spacing:.15em!important;
}
.stories-new-outcome p{
  margin:8px 0 0!important;
  color:#65718C!important;
  font-size:12px!important;
  line-height:1.6!important;
}
.stories-new-link{
  margin-top:auto!important;
  padding-top:20px!important;
  color:#1419E0!important;
  font-size:11px!important;
  font-weight:700!important;
}
.stories-new-link span{transition:transform .18s ease!important}
.stories-new-card:hover .stories-new-link span{display:inline-block;transform:translate(2px,-2px)!important}

.stories-new-cta-card{
  min-height:590px!important;
  border-radius:24px!important;
}

@media(max-width:980px){
  .stories-new-feature{grid-template-columns:1fr!important}
  .stories-new-feature-media{min-height:430px!important}
  .stories-new-feature-copy{padding:38px!important}
  body .stories-new-list .container .stories-new-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:18px!important}
  .stories-new-card-media{height:280px!important}
  .stories-new-card{min-height:540px!important}
}
@media(max-width:700px){
  .stories-new-featured{padding:58px 0 68px!important}
  .stories-new-feature{min-height:0!important;border-radius:20px!important}
  .stories-new-feature-media{min-height:300px!important}
  .stories-new-feature-copy{padding:26px 22px 30px!important}
  .stories-new-feature h2{font-size:34px!important}
  .stories-new-list{padding:76px 0 84px!important}
  body .stories-new-list .container .stories-new-grid{grid-template-columns:1fr!important;gap:20px!important;margin-top:34px!important}
  .stories-new-card{min-height:0!important;border-radius:20px!important}
  .stories-new-card-media{height:260px!important}
  .stories-new-card-body{min-height:0!important;padding:23px 22px 22px!important}
  .stories-new-card h3{font-size:23px!important}
  .stories-new-cta-card{min-height:320px!important;border-radius:20px!important}
}
</style>
'''

if style_id in s:
    start = s.index(f'<style id="{style_id}">')
    end = s.index('</style>', start) + len('</style>')
    s = s[:start] + style.strip() + s[end:]
else:
    s = s.replace('</head>', style + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('Refreshed casos.html')
