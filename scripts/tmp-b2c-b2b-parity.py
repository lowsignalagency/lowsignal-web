from pathlib import Path

p = Path('industrias/marcas-b2c.html')
s = p.read_text(encoding='utf-8')

old = '<h1>Marcas que la gente elige <strong>y vuelve a elegir.</strong></h1>'
new = '<h1>Growth para marcas que quieren <strong>ser elegidas.</strong></h1>'
if old not in s:
    raise SystemExit('Hero title pattern not found')
s = s.replace(old, new, 1)

marker = '</head>'
if marker not in s:
    raise SystemExit('head marker not found')

css = r'''
<style id="b2c-b2b-parity-final-v2">
/* Final parity pass: mirror the effective B2B industry system */
.b2cr-hero h1{max-width:1060px!important;margin:23px 0 0!important;font-size:clamp(52px,5.2vw,74px)!important;line-height:1.01!important;letter-spacing:-.058em!important;font-weight:300!important}
.b2cr-hero h1 strong{color:#A8B8FF!important;font-weight:300!important}
.b2cr-trust-grid img{transition:opacity .2s ease,transform .2s ease!important}
.b2cr-trust-grid img:hover{opacity:1!important;transform:translateY(-2px)!important}
.b2cr-journey-grid article{transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease!important}
.b2cr-journey-grid article:hover{transform:translateY(-4px)!important;border-color:#C9D4F1!important;box-shadow:0 18px 40px rgba(20,25,224,.07)!important}
.b2cr-segments-grid article:hover h3{color:#1419E0!important}

/* Testimonials: exact B2B dimensions, overlay, panel and controls */
.b2cr-stage{position:relative!important;margin-top:42px!important;min-height:540px!important;border-radius:22px!important;overflow:hidden!important;background:#071022!important}
.b2cr-slide{position:absolute!important;inset:0!important;opacity:0!important;visibility:hidden!important;transition:opacity .45s ease,visibility .45s ease!important;background-size:cover!important;background-position:center!important}
.b2cr-slide.is-active{opacity:1!important;visibility:visible!important}
.b2cr-slide:before{content:""!important;position:absolute!important;inset:0!important;background:linear-gradient(90deg,rgba(5,10,24,.62) 0%,rgba(5,10,24,.20) 50%,rgba(5,10,24,.07) 100%)!important}
.b2cr-slide.dulce{background-image:url('https://lowsignal.cl/assets/dulce-local.jpg')!important;background-position:center center!important}
.b2cr-slide.dimor{background-image:url('https://lowsignal.cl/assets/dimor-concesionario.png')!important;background-position:center center!important}
.b2cr-panel{position:absolute!important;left:42px!important;top:50%!important;transform:translateY(-50%)!important;width:min(560px,calc(100% - 84px))!important;min-height:392px!important;padding:34px!important;background:rgba(5,10,24,.91)!important;color:#fff!important;border:1px solid rgba(255,255,255,.08)!important;box-shadow:0 24px 70px rgba(0,0,0,.18)!important;display:flex!important;flex-direction:column!important}
.b2cr-client-logo{height:34px!important;width:auto!important;max-width:150px!important;object-fit:contain!important;object-position:left center!important;margin-bottom:28px!important}
.b2cr-panel blockquote{margin:0!important;font-size:17px!important;line-height:1.52!important;font-weight:300!important;max-width:470px!important}
.b2cr-person{display:flex!important;align-items:center!important;gap:12px!important;margin-top:auto!important;padding-top:28px!important}
.b2cr-person>img{width:48px!important;height:48px!important;border-radius:50%!important;object-fit:cover!important;border:1px solid rgba(255,255,255,.18)!important}
.b2cr-person b{display:block!important;font-size:12px!important}
.b2cr-person span{display:block!important;margin-top:4px!important;color:#A7B1CB!important;font-size:10px!important;line-height:1.4!important}
.b2cr-testimonial-case{margin-left:auto!important;color:#A8B8FF!important;font-size:10px!important;font-weight:700!important;white-space:nowrap!important;line-height:normal!important}
.b2cr-controls{position:absolute!important;left:76px!important;bottom:54px!important;top:auto!important;right:auto!important;z-index:5!important;display:flex!important;gap:10px!important}
.b2cr-control{width:46px!important;height:46px!important;padding:0!important;border-radius:50%!important;border:1px solid rgba(255,255,255,.28)!important;background:rgba(5,10,24,.30)!important;color:#fff!important;display:grid!important;place-items:center!important;cursor:pointer!important;transition:background .2s ease,border-color .2s ease,transform .2s ease!important}
.b2cr-control:hover{background:rgba(255,255,255,.10)!important;border-color:rgba(255,255,255,.55)!important;transform:translateY(-1px)!important}
.b2cr-control svg{width:18px!important;height:18px!important;fill:none!important;stroke:currentColor!important;stroke-width:1.8!important;stroke-linecap:round!important;stroke-linejoin:round!important}

/* Pricing: exact B2B behavior and featured slash treatment */
.b2cr-plan{transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease!important}
.b2cr-plan:hover{transform:translateY(-4px)!important;border-color:#C7D2EC!important;box-shadow:0 18px 42px rgba(20,25,224,.07)!important}
.b2cr-plan.featured{background:#071022!important;border-color:#071022!important;color:#fff!important}
.b2cr-plan .badge{letter-spacing:.14em!important}
.b2cr-plan h3{font-weight:500!important}
.b2cr-plan.featured .price{border-bottom-color:rgba(138,164,255,.16)!important}
.b2cr-plan.featured li:before{color:#8EA3FF!important}
.b2cr-plan>a{transition:color .2s ease!important}
.b2cr-custom>a{transition:transform .2s ease,background .2s ease,color .2s ease!important}
.b2cr-custom>a:hover{transform:translateY(-2px)!important;background:#1419E0!important;color:#fff!important}

/* FAQ: same thin plus/minus control as B2B */
.b2cr-faq{padding:78px 0 84px!important;background:#EEF3FF!important}
.b2cr-faq-grid{display:grid!important;grid-template-columns:.78fr 1.22fr!important;gap:clamp(48px,8vw,112px)!important;align-items:start!important}
.b2cr-faq .b2cr-eyebrow{margin:0 0 14px!important;color:#1419E0!important;font-size:10px!important;font-weight:600!important;letter-spacing:.16em!important;line-height:1.2!important}
.b2cr-faq h2{max-width:340px!important;margin:0!important;color:#071022!important;font-size:clamp(26px,2.3vw,32px)!important;font-weight:400!important;line-height:1.18!important;letter-spacing:-.045em!important}
.b2cr-faq-grid>div:first-child>p:last-child{max-width:310px!important;margin:11px 0 0!important;color:#65738F!important;font-size:12px!important;line-height:1.55!important}
.b2cr-faq-list{border-top:1px solid #D4DDF0!important}
.b2cr-faq-list details{border-bottom:1px solid #D4DDF0!important}
.b2cr-faq-list summary{min-height:54px!important;display:flex!important;align-items:center!important;justify-content:space-between!important;gap:22px!important;padding:13px 0!important;color:#111827!important;font-size:13px!important;font-weight:500!important;line-height:1.45!important;list-style:none!important;cursor:pointer!important}
.b2cr-faq-list summary>span{position:relative!important;flex:0 0 16px!important;width:16px!important;height:16px!important;color:#7C8799!important;font-size:0!important;transform:none!important}
.b2cr-faq-list summary>span:before,.b2cr-faq-list summary>span:after{content:""!important;position:absolute!important;left:50%!important;top:50%!important;width:10px!important;height:1px!important;background:currentColor!important;transform:translate(-50%,-50%)!important;transition:transform .2s ease!important}
.b2cr-faq-list summary>span:after{transform:translate(-50%,-50%) rotate(90deg)!important}
.b2cr-faq-list details[open] summary>span{transform:none!important}
.b2cr-faq-list details[open] summary>span:after{transform:translate(-50%,-50%) rotate(0)!important}
.b2cr-faq-list details>p{margin:0!important;padding:0 34px 18px 0!important;max-width:640px!important;color:#667085!important;font-size:12px!important;line-height:1.7!important}

/* CTA hover parity */
.b2cr-cta a{transition:transform .2s ease,background .2s ease,box-shadow .2s ease!important}
.b2cr-cta a:hover{transform:translateY(-2px)!important;background:#F4F6FF!important;box-shadow:0 12px 28px rgba(9,18,54,.18)!important}

@media(max-width:1100px){
  .b2cr-stage{min-height:500px!important}
  .b2cr-panel{left:28px!important;width:min(520px,calc(100% - 56px))!important}
  .b2cr-controls{left:60px!important;bottom:42px!important}
}
@media(max-width:760px){
  .b2cr-hero h1{font-size:43px!important}
  .b2cr-trust-grid{grid-template-columns:repeat(3,1fr)!important;gap:24px 18px!important;justify-items:start!important;align-items:center!important}
  .b2cr-stage{min-height:540px!important;border-radius:18px!important}
  .b2cr-slide:before{background:linear-gradient(180deg,rgba(5,10,24,.10),rgba(5,10,24,.54))!important}
  .b2cr-panel{left:16px!important;right:16px!important;top:auto!important;bottom:16px!important;transform:none!important;width:auto!important;min-height:0!important;padding:24px!important}
  .b2cr-client-logo{height:28px!important;margin-bottom:20px!important}
  .b2cr-panel blockquote{font-size:15px!important}
  .b2cr-person{padding-top:22px!important}
  .b2cr-person>img{width:42px!important;height:42px!important}
  .b2cr-testimonial-case{display:none!important}
  .b2cr-controls{left:auto!important;right:24px!important;top:24px!important;bottom:auto!important}
  .b2cr-control{width:40px!important;height:40px!important}
  .b2cr-control svg{width:18px!important;height:18px!important}
  .b2cr-faq{padding:62px 0 68px!important}
  .b2cr-faq-grid{grid-template-columns:1fr!important;gap:26px!important}
  .b2cr-faq h2{max-width:330px!important;font-size:29px!important}
  .b2cr-faq-list summary{min-height:54px!important;font-size:13px!important}
  .b2cr-faq-list details>p{padding-right:24px!important}
}
</style>
'''

s = s.replace(marker, css + marker, 1)
p.write_text(s, encoding='utf-8')
