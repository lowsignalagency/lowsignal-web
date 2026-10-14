from pathlib import Path
p=Path('casos/salvador-dali.html')
s=p.read_text(encoding='utf-8')

anchor='''  <section class="case-new-next">'''
if anchor not in s:
    raise SystemExit('Missing next-case anchor')
if 'case-dali-testimonial' in s:
    raise SystemExit('Testimonial already present')

block='''  <section class="case-dali-testimonial" aria-label="Testimonio de Colegio Salvador Dalí">\n    <div class="container">\n      <div class="case-dali-testimonial-card">\n        <div class="case-dali-testimonial-quote">“</div>\n        <blockquote>Con lowsignal fortalecimos nuestras redes, nos acercamos a la comunidad y potenciamos las habilidades de nuestros estudiantes.</blockquote>\n        <div class="case-dali-testimonial-person">\n          <img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal">\n          <div>\n            <b>Karina Ravanal</b>\n            <span>Directora, Colegio Salvador Dalí</span>\n          </div>\n        </div>\n      </div>\n    </div>\n  </section>\n\n'''
s=s.replace(anchor,block+anchor,1)

style='''\n<style id="case-dali-testimonial-v1">\n.case-dali-testimonial{\n  padding:104px 0;\n  background:#fff;\n}\n.case-dali-testimonial-card{\n  position:relative;\n  overflow:hidden;\n  padding:56px 60px;\n  border-radius:24px;\n  background:#1419E0;\n  color:#fff;\n}\n.case-dali-testimonial-card:after{\n  content:"";\n  position:absolute;\n  inset:0;\n  background:radial-gradient(55% 120% at 100% 0%,rgba(138,164,255,.34),transparent 72%);\n  pointer-events:none;\n}\n.case-dali-testimonial-quote{\n  position:relative;\n  z-index:1;\n  color:#AFC0FF;\n  font-size:52px;\n  line-height:.8;\n  font-weight:300;\n}\n.case-dali-testimonial blockquote{\n  position:relative;\n  z-index:1;\n  max-width:980px;\n  margin:22px 0 0;\n  font-size:clamp(28px,3.25vw,44px);\n  line-height:1.16;\n  letter-spacing:-.035em;\n  font-weight:300;\n}\n.case-dali-testimonial-person{\n  position:relative;\n  z-index:1;\n  display:flex;\n  align-items:center;\n  gap:14px;\n  margin-top:34px;\n}\n.case-dali-testimonial-person img{\n  width:58px;\n  height:58px;\n  border-radius:50%;\n  object-fit:cover;\n  object-position:center 68%;\n}\n.case-dali-testimonial-person b,\n.case-dali-testimonial-person span{display:block}\n.case-dali-testimonial-person b{font-size:13px;font-weight:700}\n.case-dali-testimonial-person span{margin-top:4px;color:#DDE3FF;font-size:11px}\n@media(max-width:620px){\n  .case-dali-testimonial{padding:70px 0}\n  .case-dali-testimonial .container{width:calc(100% - 32px)!important}\n  .case-dali-testimonial-card{padding:34px 26px;border-radius:18px}\n  .case-dali-testimonial blockquote{font-size:27px;line-height:1.2}\n  .case-dali-testimonial-person{margin-top:28px}\n  .case-dali-testimonial-person img{width:52px;height:52px;object-position:center 72%}\n}\n</style>\n'''
s=s.replace('</head>',style+'</head>',1)
p.write_text(s,encoding='utf-8')
print('Added Salvador Dali testimonial')
