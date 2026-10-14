from pathlib import Path
import re

# --- Salvador Dali case: use the same testimonial structure/design as RECH ---
p = Path('casos/salvador-dali.html')
s = p.read_text(encoding='utf-8')

new_block = '''  <section class="case-new-testimonial case-dali-testimonial-rech" aria-label="Testimonio de Colegio Salvador Dalí">\n    <div class="container case-new-testimonial-inner">\n      <div class="case-new-quote-mark">“</div>\n      <blockquote>Con lowsignal fortalecimos nuestras redes, nos acercamos a la comunidad y potenciamos las habilidades de nuestros estudiantes.</blockquote>\n      <div class="case-new-person">\n        <img src="https://lowsignal.cl/assets/karina-csd.jpg" alt="Karina Ravanal">\n        <div>\n          <b>Karina Ravanal</b>\n          <span>Directora, Colegio Salvador Dalí</span>\n        </div>\n      </div>\n    </div>\n  </section>'''

pattern = re.compile(r'  <section class="case-dali-testimonial"[^>]*>.*?</section>', re.S)
s, n = pattern.subn(new_block, s, count=1)
if n != 1:
    raise SystemExit(f'Expected one Dali testimonial section, replaced {n}')

style = '''\n<style id="dali-testimonial-rech-match-v2">\n/* Match the RECH customer-story testimonial treatment exactly. */\n.case-new-testimonial.case-dali-testimonial-rech{\n  position:relative;\n  overflow:hidden;\n  background:#070F22;\n  padding:104px 0;\n}\n.case-new-testimonial.case-dali-testimonial-rech:before{\n  content:"";\n  position:absolute;\n  inset:0;\n  background:radial-gradient(45% 55% at 0% 100%,rgba(20,74,224,.26),transparent 70%);\n}\n.case-dali-testimonial-rech .case-new-testimonial-inner{\n  position:relative;\n  max-width:980px;\n}\n.case-dali-testimonial-rech .case-new-quote-mark{\n  color:#1419E0;\n  font-size:92px;\n  line-height:.7;\n  font-weight:700;\n}\n.case-dali-testimonial-rech blockquote{\n  margin:22px 0 0;\n  color:#F8F8F8;\n  font-size:clamp(30px,3.6vw,44px);\n  line-height:1.26;\n  letter-spacing:-.03em;\n  font-weight:300;\n}\n.case-dali-testimonial-rech .case-new-person{\n  display:flex;\n  align-items:center;\n  gap:15px;\n  margin-top:34px;\n  padding-top:24px;\n  border-top:1px solid rgba(150,175,255,.16);\n}\n.case-dali-testimonial-rech .case-new-person img{\n  width:58px;\n  height:58px;\n  border-radius:50%;\n  object-fit:cover;\n  object-position:center 88% !important;\n}\n.case-dali-testimonial-rech .case-new-person b{\n  display:block;\n  color:#fff;\n  font-size:15px;\n}\n.case-dali-testimonial-rech .case-new-person span{\n  display:block;\n  margin-top:4px;\n  color:#8B92A8;\n  font-size:12px;\n}\n@media(max-width:620px){\n  .case-new-testimonial.case-dali-testimonial-rech{padding:74px 0}\n  .case-dali-testimonial-rech blockquote{font-size:28px}\n  .case-dali-testimonial-rech .case-new-quote-mark{font-size:72px}\n  .case-dali-testimonial-rech .case-new-person img{object-position:center 90% !important}\n}\n</style>\n'''
if 'dali-testimonial-rech-match-v2' not in s:
    s = s.replace('</head>', style + '</head>', 1)
p.write_text(s, encoding='utf-8')

# --- Home: raise Karina substantially inside the circular crop ---
p = Path('index.html')
s = p.read_text(encoding='utf-8')
home_style = '''\n<style id="karina-home-crop-v2">\n/* Karina Ravanal — keep the face high in the circular testimonial crop. */\n.lsr-case-person img[src*="karina-csd.jpg"],\n.home26-person img[src*="karina-csd.jpg"]{\n  object-fit:cover !important;\n  object-position:center 88% !important;\n}\n@media(max-width:760px){\n  .lsr-case-person img[src*="karina-csd.jpg"],\n  .home26-person img[src*="karina-csd.jpg"]{\n    object-position:center 90% !important;\n  }\n}\n</style>\n'''
if 'karina-home-crop-v2' not in s:
    s = s.replace('</body>', home_style + '\n</body>', 1)
p.write_text(s, encoding='utf-8')

print('Matched Dali testimonial to RECH and raised Karina crop on case + Home')
