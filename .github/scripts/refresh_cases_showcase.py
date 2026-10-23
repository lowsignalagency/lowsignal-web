from pathlib import Path

p = Path('casos.html')
s = p.read_text(encoding='utf-8')

# Keep the stronger imagery already used in the testimonial sections.
s = s.replace('https://lowsignal.cl/assets/dulce-local.jpg', 'https://lowsignal.cl/assets/dulce-reino-pasteleria.jpg')
s = s.replace('https://lowsignal.cl/assets/dimor-truck.jpg', 'https://lowsignal.cl/assets/dimor-concesionario.png')

style_id = 'cases-showcase-v2'
style = r'''
<style id="cases-showcase-v2">
/* Customer Stories — testimonial-style, full-bleed portfolio treatment */
.stories-new-featured{
  padding:78px 0 96px!important;
  background:#fff!important;
}
.stories-new-feature{
  position:relative!important;
  display:block!important;
  min-height:640px!important;
  overflow:hidden!important;
  border:0!important;
  border-radius:28px!important;
  background:#071022!important;
  box-shadow:0 30px 80px rgba(7,15,34,.18)!important;
}
.stories-new-feature-media{
  position:absolute!important;
  inset:0!important;
  min-height:0!important;
  height:100%!important;
}
.stories-new-feature-media>img:first-child{
  width:100%!important;
  height:100%!important;
  object-fit:cover!important;
  object-position:center 42%!important;
  transition:transform .55s cubic-bezier(.2,.7,.2,1)!important;
}
.stories-new-feature:hover .stories-new-feature-media>img:first-child{transform:scale(1.025)!important}
.stories-new-feature-media:after{
  background:linear-gradient(90deg,rgba(5,10,24,.16) 0%,rgba(5,10,24,.24) 40%,rgba(5,10,24,.54) 68%,rgba(5,10,24,.76) 100%)!important;
}
.stories-new-feature-media>span{
  left:26px!important;
  top:26px!important;
  padding:9px 13px!important;
  border-radius:999px!important;
  background:rgba(7,15,34,.78)!important;
  border:1px solid rgba(255,255,255,.16)!important;
  color:#fff!important;
  backdrop-filter:blur(10px)!important;
}
.stories-new-feature-logo{
  left:30px!important;
  bottom:30px!important;
  height:58px!important;
  max-width:34%!important;
  filter:drop-shadow(0 8px 22px rgba(0,0,0,.28))!important;
}
.stories-new-feature-copy{
  position:absolute!important;
  z-index:4!important;
  top:34px!important;
  right:34px!important;
  bottom:34px!important;
  width:min(540px,45%)!important;
  padding:40px 40px 36px!important;
  border:1px solid rgba(255,255,255,.09)!important;
  border-radius:20px!important;
  background:rgba(5,10,24,.90)!important;
  color:#fff!important;
  box-shadow:0 26px 70px rgba(0,0,0,.22)!important;
  backdrop-filter:blur(12px)!important;
  display:flex!important;
  flex-direction:column!important;
  justify-content:center!important;
}
.stories-new-feature .stories-new-meta{color:#9AA7C3!important}
.stories-new-feature .stories-new-meta b{color:#8AA4FF!important}
.stories-new-feature h2{
  margin-top:20px!important;
  color:#fff!important;
  font-size:clamp(34px,3.1vw,47px)!important;
  line-height:1.06!important;
  letter-spacing:-.045em!important;
}
.stories-new-feature h2 strong{color:#A8B8FF!important;font-weight:300!important}
.stories-new-feature blockquote{
  margin-top:24px!important;
  color:#C9D1E4!important;
  border-left-color:#7188FF!important;
  font-size:14px!important;
  line-height:1.72!important;
}
.stories-new-person{margin-top:24px!important}
.stories-new-person b{color:#fff!important}
.stories-new-person span{color:#97A3BE!important}
.stories-new-feature-link{margin-top:26px!important;color:#A8B8FF!important}

/* Main case archive: dark, image-led, testimonial-like */
.stories-new-list{
  padding:108px 0 122px!important;
  background:#070F22!important;
  color:#fff!important;
}
.stories-new-list-head{margin-bottom:6px!important}
.stories-new-list .stories-new-eyebrow{color:#8AA4FF!important}
.stories-new-list h2{
  max-width:800px!important;
  color:#fff!important;
  font-size:clamp(40px,4vw,58px)!important;
  line-height:1.04!important;
  letter-spacing:-.045em!important;
}
.stories-new-list-head>div>p:last-child{color:#8D99B6!important}
.stories-new-filters{gap:8px!important}
.stories-new-filter{
  padding:10px 15px!important;
  border:1px solid rgba(255,255,255,.14)!important;
  background:rgba(255,255,255,.045)!important;
  color:#B6C0D6!important;
  backdrop-filter:blur(8px)!important;
}
.stories-new-filter:hover{border-color:rgba(138,164,255,.46)!important;color:#fff!important}
.stories-new-filter.is-active{
  background:#1419E0!important;
  border-color:#1419E0!important;
  color:#fff!important;
}
body .stories-new-list .container .stories-new-grid{
  grid-template-columns:repeat(2,minmax(0,1fr))!important;
  gap:24px!important;
  margin-top:48px!important;
}
.stories-new-card{
  position:relative!important;
  display:block!important;
  min-height:570px!important;
  overflow:hidden!important;
  border:1px solid rgba(255,255,255,.10)!important;
  border-radius:24px!important;
  background:#0A1226!important;
  box-shadow:0 18px 44px rgba(0,0,0,.18)!important;
  transition:transform .3s ease,border-color .3s ease,box-shadow .3s ease!important;
}
.stories-new-card:hover{
  transform:translateY(-7px)!important;
  border-color:rgba(138,164,255,.30)!important;
  box-shadow:0 30px 68px rgba(0,0,0,.32)!important;
}
.stories-new-card-media{
  position:absolute!important;
  inset:0!important;
  width:100%!important;
  height:100%!important;
  background:#0A1226!important;
}
.stories-new-photo{
  position:absolute!important;
  inset:0!important;
  width:100%!important;
  height:100%!important;
  object-fit:cover!important;
  transition:transform .55s cubic-bezier(.2,.7,.2,1),filter .35s ease!important;
}
.stories-new-card:hover .stories-new-photo{transform:scale(1.035)!important}
.stories-new-card-shade{
  position:absolute!important;
  inset:0!important;
  background:linear-gradient(180deg,rgba(5,10,24,.08) 0%,rgba(5,10,24,.14) 33%,rgba(5,10,24,.72) 70%,rgba(5,10,24,.95) 100%)!important;
}
.stories-new-logo{
  position:absolute!important;
  z-index:3!important;
  left:26px!important;
  top:25px!important;
  bottom:auto!important;
  width:auto!important;
  max-width:150px!important;
  max-height:50px!important;
  object-fit:contain!important;
  object-position:left center!important;
  filter:drop-shadow(0 6px 18px rgba(0,0,0,.32))!important;
}
.stories-new-card-body{
  position:absolute!important;
  z-index:4!important;
  left:22px!important;
  right:22px!important;
  bottom:22px!important;
  min-height:0!important;
  padding:24px 25px 22px!important;
  border:1px solid rgba(255,255,255,.09)!important;
  border-radius:17px!important;
  background:rgba(5,10,24,.90)!important;
  color:#fff!important;
  box-shadow:0 18px 48px rgba(0,0,0,.18)!important;
  backdrop-filter:blur(11px)!important;
}
.stories-new-card .stories-new-meta{color:#9BA7C1!important;font-size:10px!important}
.stories-new-card .stories-new-meta b{color:#8AA4FF!important;font-size:8px!important;letter-spacing:.16em!important}
.stories-new-card .stories-new-meta span:before{background:#5D6983!important}
.stories-new-card h3{
  min-height:0!important;
  margin:13px 0 0!important;
  color:#fff!important;
  font-size:clamp(22px,1.9vw,27px)!important;
  line-height:1.16!important;
  letter-spacing:-.035em!important;
  font-weight:400!important;
}
.stories-new-outcome{
  min-height:0!important;
  margin-top:17px!important;
  padding-top:15px!important;
  border-top:1px solid rgba(255,255,255,.10)!important;
}
.stories-new-outcome>span{
  display:block!important;
  color:#8AA4FF!important;
  font-size:8px!important;
  font-weight:700!important;
  letter-spacing:.16em!important;
}
.stories-new-outcome p{
  margin:7px 0 0!important;
  color:#C4CCE0!important;
  font-size:11px!important;
  line-height:1.55!important;
}
.stories-new-link{
  margin-top:16px!important;
  padding-top:0!important;
  color:#fff!important;
  font-size:10px!important;
  font-weight:700!important;
}
.stories-new-link span{display:inline-block!important;transition:transform .18s ease!important}
.stories-new-card:hover .stories-new-link span{transform:translate(2px,-2px)!important}
.stories-new-cta-card{
  min-height:570px!important;
  border:1px solid rgba(138,164,255,.22)!important;
  border-radius:24px!important;
  background:linear-gradient(145deg,#121A3B 0%,#1419E0 100%)!important;
  color:#fff!important;
}
.stories-new-cta-card *{color:#fff!important}

@media(max-width:980px){
  .stories-new-feature{min-height:590px!important}
  .stories-new-feature-copy{top:28px!important;right:28px!important;bottom:28px!important;width:min(500px,52%)!important;padding:34px!important}
  .stories-new-feature-logo{max-width:30%!important}
  body .stories-new-list .container .stories-new-grid{gap:18px!important}
  .stories-new-card{min-height:530px!important}
}
@media(max-width:760px){
  .stories-new-featured{padding:58px 0 70px!important}
  .stories-new-feature{min-height:620px!important;border-radius:20px!important}
  .stories-new-feature-media:after{background:linear-gradient(180deg,rgba(5,10,24,.08) 0%,rgba(5,10,24,.20) 42%,rgba(5,10,24,.82) 100%)!important}
  .stories-new-feature-logo{left:22px!important;top:72px!important;bottom:auto!important;height:46px!important;max-width:56%!important}
  .stories-new-feature-copy{left:16px!important;right:16px!important;top:auto!important;bottom:16px!important;width:auto!important;padding:24px 22px!important;border-radius:16px!important}
  .stories-new-feature h2{font-size:31px!important}
  .stories-new-feature blockquote{font-size:12px!important;line-height:1.6!important}
  .stories-new-person{margin-top:18px!important}
  .stories-new-list{padding:76px 0 86px!important}
  body .stories-new-list .container .stories-new-grid{grid-template-columns:1fr!important;gap:20px!important;margin-top:34px!important}
  .stories-new-card{min-height:520px!important;border-radius:20px!important}
  .stories-new-logo{left:22px!important;top:22px!important;max-width:130px!important;max-height:44px!important}
  .stories-new-card-body{left:14px!important;right:14px!important;bottom:14px!important;padding:21px 20px 19px!important;border-radius:15px!important}
  .stories-new-card h3{font-size:22px!important}
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
