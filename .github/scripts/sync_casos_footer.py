from pathlib import Path
import re

home = Path("index.html").read_text(encoding="utf-8")
casos_path = Path("casos.html")
casos = casos_path.read_text(encoding="utf-8")

m = re.search(r"<footer>[\s\S]*?</footer>", home)
if not m:
    raise SystemExit("Home footer not found")

casos, n = re.subn(r"<footer>[\s\S]*?</footer>", m.group(0), casos, count=1)
if n != 1:
    raise SystemExit("Casos footer replacement failed")

casos = re.sub(r'<style id="casos-footer-home-sync">[\s\S]*?</style>\s*', '', casos)

css = '''
<style id="casos-footer-home-sync">
footer{
  background:#050A18 !important;
  color:#A0A9BF !important;
  padding:50px 0 22px !important;
  font-size:14px !important;
  border-top:1px solid rgba(255,255,255,.06) !important;
}
footer .footer-container{
  width:min(1220px,calc(100% - 128px)) !important;
  max-width:1220px !important;
  margin-left:auto !important;
  margin-right:auto !important;
}
footer .footer-main{
  display:grid !important;
  grid-template-columns:1.45fr .8fr .72fr .78fr !important;
  gap:46px !important;
  align-items:start !important;
}
footer .footer-brand img{height:24px !important;width:auto !important}
footer .footer-brand-copy{max-width:350px !important;margin:18px 0 0 !important;font-size:13px !important;line-height:1.65 !important;color:#8E98AE !important}
footer .footer-claim{margin-top:20px !important;font-size:16px !important;color:#F4F6FB !important}
footer .footer-ai{max-width:420px !important;margin-top:24px !important;padding-top:17px !important}
footer .footer-bottom{display:grid !important;grid-template-columns:1fr auto 1fr !important;gap:28px !important;align-items:center !important;padding-top:17px !important}
footer .footer-bottom-links{justify-content:flex-end !important}
@media(max-width:1100px){
  footer .footer-container{width:calc(100% - 48px) !important}
  footer .footer-main{grid-template-columns:1.25fr 1fr !important;gap:46px 60px !important}
  footer .footer-brand{grid-column:1/-1 !important}
}
@media(max-width:900px){
  footer .footer-bottom{grid-template-columns:1fr !important;justify-items:start !important;gap:14px !important}
  footer .footer-bottom-links{justify-content:flex-start !important}
}
@media(max-width:640px){
  footer{padding-top:48px !important}
  footer .footer-container{width:calc(100% - 40px) !important}
  footer .footer-main{grid-template-columns:1fr !important;gap:34px !important}
  footer .footer-brand{grid-column:auto !important}
}
</style>
'''

casos = casos.replace("</head>", css + "\n</head>", 1)
casos_path.write_text(casos, encoding="utf-8")
