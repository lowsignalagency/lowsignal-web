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

.case-new-hero{padding-top:166px !important;padding-bottom:88px !important}
.case-new-hero-grid{gap:54px !important}
.case-new-hero h1{font-size:clamp(46px,4.7vw,68px) !important;line-height:1.01 !important;letter-spacing:-.052em !important}
.case-new-hero-grid>div:first-child>p{font-size:16px !important;line-height:1.65 !important}
.case-new-cover{margin-top:48px !important;border-radius:20px !important}

.case-new-story,.case-new-work,.case-new-system,.case-new-next,.case-new-testimonial{padding:88px 0 !important}
.case-new-story h2,.case-new-work h2,.case-new-system h2{font-size:clamp(38px,3.6vw,50px) !important;line-height:1.08 !important}
.case-new-story-head,.case-new-work-head{gap:54px !important}
.case-new-story-head>p,.case-new-work-head>p{font-size:14px !important;line-height:1.7 !important}
.case-new-steps{margin-top:44px !important;gap:12px !important}
.case-new-steps article{padding:24px !important;border-radius:16px !important}
.case-new-steps h3{font-size:19px !important}

.case-new-gallery{margin-top:44px !important;gap:10px !important}
.case-new-gallery figure,.case-new-gallery-copy{border-radius:14px !important}
.case-new-gallery-copy{padding:24px !important}
.case-new-gallery-copy h3{font-size:22px !important}
.case-new-system-grid{gap:70px !important}
.case-new-system-list article{padding:20px 0 !important}
.case-new-system-list article>span{font-size:26px !important}
.case-new-system-list h3{font-size:18px !important}
.case-new-next-card{margin-top:32px !important;border-radius:18px !important;height:440px !important}
.case-new-next-head h2{font-size:38px !important}
.case-new-next-copy h3{font-size:31px !important}

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
  .case-new-hero{padding-top:136px !important;padding-bottom:64px !important}
  .case-new-hero .container,.case-new-story .container,.case-new-work .container,.case-new-system .container,.case-new-next .container,.case-new-testimonial .container,.lsr-band .lsr-wrap,footer .footer-container{width:calc(100% - 40px) !important}
  .case-new-hero h1{font-size:38px !important}
  .case-new-story,.case-new-work,.case-new-system,.case-new-next,.case-new-testimonial{padding:72px 0 !important}
  .case-new-story h2,.case-new-work h2,.case-new-system h2{font-size:34px !important}
  .case-new-next-card{height:350px !important}
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
