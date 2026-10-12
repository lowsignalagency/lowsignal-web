from pathlib import Path
import re

source = Path('nosotros.html').read_text(encoding='utf-8')
case_dir = Path('casos')

header = re.search(r'<header class="lnav"[\s\S]*?</header>', source)
footer = re.search(r'<footer>[\s\S]*?</footer>', source)
if not header or not footer:
    raise SystemExit('Reference navbar/footer not found in nosotros.html')

style_blocks = [m.group(2) for m in re.finditer(r'<style([^>]*)>([\s\S]*?)</style>', source, flags=re.I)]
ref_css = []
for css in style_blocks:
    if re.search(r'\.lnav|\.footer-|footer\{|\.lsr-band', css):
        ref_css.append(css)

cta = '''<section class="lsr-band" id="contacto">
  <div class="lsr-wrap lsr-band-inner">
    <p>¿Construimos lo que viene?</p>
    <a href="https://calendly.com/felipe-lowsignal/30min" target="_blank" rel="noopener noreferrer">Hablemos</a>
  </div>
</section>'''

case_css = r'''
<style id="case-pages-refresh-v1">
/* Individual Customer Stories — current low design system */
:root{--case-content:1220px}

@media(min-width:761px){
  body>.nav-wrap{display:none !important}
  body>.lnav{display:block !important;position:fixed !important;top:0 !important;left:0 !important;right:0 !important;width:100% !important;z-index:2000 !important}
}

.case-new-hero .container,
.case-new-story .container,
.case-new-work .container,
.case-new-system .container,
.case-new-next .container,
.case-new-testimonial .container,
.lsr-band .lsr-wrap,
footer .footer-container{
  width:min(var(--case-content),calc(100% - 128px)) !important;
  max-width:var(--case-content) !important;
  margin-left:auto !important;
  margin-right:auto !important;
}

/* HERO — a little tighter than the first redesign */
.case-new-hero{padding-top:164px !important;padding-bottom:82px !important}
.case-new-hero-grid{gap:52px !important}
.case-new-hero h1{
  font-size:clamp(44px,4.35vw,62px) !important;
  line-height:1.02 !important;
  letter-spacing:-.05em !important;
}
.case-new-hero-grid>div:first-child>p{
  max-width:640px !important;
  font-size:15px !important;
  line-height:1.72 !important;
}
.case-new-cover{margin-top:44px !important;border-radius:18px !important}

/* SECTION RHYTHM */
.case-new-story,.case-new-work,.case-new-system,.case-new-next,.case-new-testimonial{padding:82px 0 !important}
.case-new-story h2,.case-new-work h2,.case-new-system h2{
  font-size:clamp(34px,3.15vw,44px) !important;
  line-height:1.1 !important;
  letter-spacing:-.04em !important;
}
.case-new-story-head,.case-new-work-head{gap:52px !important}
.case-new-story-head>p,.case-new-work-head>p{
  max-width:520px !important;
  font-size:14px !important;
  line-height:1.75 !important;
}
.case-new-eyebrow{font-size:10px !important;letter-spacing:.2em !important}

/* CASE / CHALLENGE / RESULT — more editorial, less text-box heavy */
.case-new-steps{
  margin-top:40px !important;
  gap:14px !important;
}
.case-new-steps article{
  position:relative !important;
  min-height:245px !important;
  padding:24px 24px 26px !important;
  border-radius:16px !important;
  border:1px solid rgba(15,31,140,.10) !important;
  background:linear-gradient(180deg,#FBFCFF 0%,#F5F8FF 100%) !important;
  box-shadow:0 10px 26px rgba(15,31,140,.035) !important;
  overflow:hidden !important;
}
.case-new-steps article::before{
  content:"" !important;
  position:absolute !important;
  width:92px !important;
  height:92px !important;
  right:-34px !important;
  top:-34px !important;
  border-radius:50% !important;
  border:1px solid rgba(20,25,224,.10) !important;
  background:rgba(20,25,224,.025) !important;
}
.case-new-steps article>span{
  position:relative !important;
  z-index:1 !important;
  display:inline-flex !important;
  align-items:center !important;
  min-height:28px !important;
  padding:0 10px !important;
  border-radius:999px !important;
  background:#EEF2FF !important;
  color:#1419E0 !important;
  font-size:10px !important;
  font-weight:700 !important;
  letter-spacing:.03em !important;
}
.case-new-steps small{
  color:#78839B !important;
  font-size:9px !important;
  letter-spacing:.18em !important;
  font-weight:700 !important;
}
.case-new-steps h3{
  max-width:92% !important;
  margin-top:12px !important;
  color:#16235F !important;
  font-size:17px !important;
  line-height:1.52 !important;
  letter-spacing:-.018em !important;
  font-weight:500 !important;
}
.case-new-steps .is-highlight{
  border-color:transparent !important;
  background:linear-gradient(145deg,#1419E0 0%,#2447F5 100%) !important;
  box-shadow:0 18px 38px rgba(20,25,224,.16) !important;
}
.case-new-steps .is-highlight::before{
  width:150px !important;
  height:150px !important;
  right:-54px !important;
  top:-58px !important;
  border-color:rgba(255,255,255,.14) !important;
  background:rgba(255,255,255,.035) !important;
}
.case-new-steps .is-highlight>span{
  background:rgba(255,255,255,.12) !important;
  color:#fff !important;
}
.case-new-steps .is-highlight small{color:#BEC9FF !important}
.case-new-steps .is-highlight h3{color:#fff !important;font-weight:500 !important}

@media(hover:hover){
  .case-new-steps article:hover{
    transform:translateY(-3px) !important;
    border-color:rgba(20,25,224,.18) !important;
    box-shadow:0 16px 36px rgba(15,31,140,.07) !important;
  }
  .case-new-steps .is-highlight:hover{
    border-color:transparent !important;
    box-shadow:0 22px 44px rgba(20,25,224,.20) !important;
  }
}

/* WORK / MEDIA */
.case-new-gallery{margin-top:40px !important;gap:10px !important}
.case-new-gallery figure,.case-new-gallery-copy{border-radius:14px !important}
.case-new-gallery-copy{padding:24px !important}
.case-new-gallery-copy h3{font-size:20px !important;line-height:1.35 !important}
.case-new-gallery-copy p{font-size:12px !important;line-height:1.65 !important}

/* SYSTEM */
.case-new-system-grid{gap:66px !important}
.case-new-system-list article{padding:18px 0 !important}
.case-new-system-list article>span{font-size:24px !important}
.case-new-system-list h3{font-size:17px !important}
.case-new-system-list p{font-size:12px !important;line-height:1.65 !important}

/* NEXT CASE */
.case-new-next-card{margin-top:30px !important;border-radius:18px !important;height:420px !important}
.case-new-next-head h2{font-size:34px !important}
.case-new-next-copy h3{font-size:28px !important;line-height:1.16 !important}

/* Same CTA as Home / Nosotros */
.lsr-band{background:linear-gradient(105deg,#1419E0,#2447F5) !important;color:#fff !important}
.lsr-band-inner{min-height:208px !important;display:flex !important;align-items:center !important;justify-content:space-between !important;gap:40px !important}
.lsr-band-inner p{margin:0 !important;font-size:30px !important;line-height:1.15 !important;letter-spacing:-.035em !important;font-weight:300 !important}
.lsr-band-inner a{display:inline-flex !important;align-items:center !important;justify-content:center !important;min-height:50px !important;padding:0 24px !important;border-radius:999px !important;background:#fff !important;color:#0F1F5C !important;font-size:14px !important;font-weight:650 !important;transition:transform .2s ease,background .2s ease !important}
.lsr-band-inner a:hover{transform:translateY(-2px) !important;background:#F4F6FF !important}

@media(max-width:1100px){
  .case-new-hero .container,.case-new-story .container,.case-new-work .container,.case-new-system .container,.case-new-next .container,.case-new-testimonial .container,.lsr-band .lsr-wrap,footer .footer-container{width:calc(100% - 48px) !important}
}
@media(max-width:760px){
  body>.lnav{display:none !important}
  .case-new-hero{padding-top:136px !important;padding-bottom:62px !important}
  .case-new-hero .container,.case-new-story .container,.case-new-work .container,.case-new-system .container,.case-new-next .container,.case-new-testimonial .container,.lsr-band .lsr-wrap,footer .footer-container{width:calc(100% - 40px) !important}
  .case-new-hero h1{font-size:36px !important}
  .case-new-story,.case-new-work,.case-new-system,.case-new-next,.case-new-testimonial{padding:68px 0 !important}
  .case-new-story h2,.case-new-work h2,.case-new-system h2{font-size:31px !important}
  .case-new-steps{grid-template-columns:1fr !important;gap:10px !important;margin-top:32px !important}
  .case-new-steps article{min-height:180px !important;padding:20px !important}
  .case-new-steps h3{max-width:100% !important;font-size:16px !important}
  .case-new-next-card{height:340px !important}
  .case-new-next-copy h3{font-size:24px !important}
  .lsr-band-inner{min-height:190px !important;flex-direction:column !important;align-items:flex-start !important;justify-content:center !important;gap:24px !important}
  .lsr-band-inner p{font-size:25px !important}
  .lsr-band-inner a{width:100% !important}
}
</style>
'''

ref_style = '\n<style id="case-pages-reference-v1">\n' + '\n'.join(ref_css) + '\n</style>\n'

for path in sorted(case_dir.glob('*.html')):
    html = path.read_text(encoding='utf-8')

    # Remove prior injected refresh blocks.
    html = re.sub(r'<style[^>]*id="case-pages-(?:refresh|reference)-v1"[^>]*>[\s\S]*?</style>\s*', '', html, flags=re.I)

    # Add the current desktop navbar exactly once; legacy mobile navbar remains for mobile.
    html = re.sub(r'<header class="lnav"[\s\S]*?</header>\s*', '', html, flags=re.I)
    html = html.replace('<body>', '<body>\n\n' + header.group(0), 1)

    # Standard CTA on every case page.
    html, _ = re.subn(r'<section class="case-new-final"[\s\S]*?</section>', cta, html, count=1, flags=re.I)

    # Exact current footer markup.
    html, n = re.subn(r'<footer>[\s\S]*?</footer>', footer.group(0), html, count=1, flags=re.I)
    if n != 1:
        raise SystemExit(f'Footer replacement failed for {path}')

    # Reference navbar/footer CSS plus case-specific system must win last.
    html = html.replace('</body>', ref_style + case_css + '\n</body>', 1)
    path.write_text(html, encoding='utf-8')
    print('updated', path)
