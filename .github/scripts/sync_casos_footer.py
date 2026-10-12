from pathlib import Path
import re

home = Path("index.html").read_text(encoding="utf-8")
casos_path = Path("casos.html")
casos = casos_path.read_text(encoding="utf-8")

# 1) Copy the exact current Home footer markup.
m = re.search(r"<footer>[\s\S]*?</footer>", home)
if not m:
    raise SystemExit("Home footer not found")

casos, n = re.subn(r"<footer>[\s\S]*?</footer>", m.group(0), casos, count=1)
if n != 1:
    raise SystemExit("Casos footer replacement failed")

# 2) Remove any previous Casos-only footer override.
casos = re.sub(r'<style id="casos-footer-home-sync">[\s\S]*?</style>\s*', '', casos)

# 3) Apply the exact footer sizing/spacing system currently used on Home.
css = r'''
<style id="casos-footer-home-sync">
.footer-container{max-width:1180px}
footer{
  background:#050A18;
  color:#A0A9BF;
  padding:50px 0 22px;
  font-size:14px;
  border-top:1px solid rgba(255,255,255,.06)
}
.footer-main{
  display:grid;
  grid-template-columns:1.45fr .8fr .72fr .78fr;
  gap:46px;
  align-items:start
}
.footer-brand img{height:24px;width:auto}
.footer-brand-copy{
  max-width:350px;
  margin:18px 0 0;
  font-size:13px;
  line-height:1.65;
  color:#8E98AE
}
.footer-claim{margin-top:20px;font-size:16px;color:#F4F6FB}
.footer-claim strong{color:#7690FF}
.footer-ai{
  max-width:420px;
  margin-top:24px;
  padding-top:17px;
  border-top:1px solid rgba(150,175,255,.14)
}
.footer-ai-title{margin:0 0 12px;color:#AEB7CA;font-size:13px}
.ai-links{display:flex;gap:10px}
.ai-link{
  width:40px;height:40px;
  display:grid;place-items:center;
  border:1px solid rgba(150,175,255,.22);
  border-radius:9px;
  color:#7690FF;
  font-weight:700;
  font-size:10px;
  transition:.2s ease;
  overflow:hidden
}
.ai-link img{width:24px!important;height:24px!important;object-fit:contain;display:block}
.ai-link:hover{border-color:#7690FF;background:rgba(118,144,255,.08);transform:translateY(-2px)}
.footer-title{margin:2px 0 16px;color:#7690FF;font-size:10px;font-weight:700;letter-spacing:.2em}
.footer-links{display:flex;flex-direction:column;gap:10px}
.footer-links a{
  color:#C5CCDA;
  font-size:13px;
  display:inline-flex;
  align-items:center;
  width:fit-content;
  transition:color .2s ease,transform .2s ease,opacity .2s ease
}
.footer-links a:hover{color:#8AA4FF;transform:translateX(2px)}
.footer-links a:active{color:#6F86F5;transform:translateX(1px)}
.footer-links a:focus-visible{outline:2px solid rgba(138,164,255,.45);outline-offset:4px;border-radius:4px}
.footer-social a{display:flex;align-items:center;gap:12px}
.footer-location{display:flex;align-items:center;gap:9px}
.location-icon{width:15px;height:15px;color:#7690FF;flex:0 0 15px}
.footer-meta{
  margin-top:34px;
  padding:17px 0;
  border-top:1px solid rgba(150,175,255,.14);
  border-bottom:1px solid rgba(150,175,255,.14);
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  gap:20px;
  align-items:center;
  color:#8994AA;
  font-size:11px
}
.footer-mail{color:#B4BED0;transition:color .2s ease,opacity .2s ease}
.footer-mail:hover{color:#FFFFFF}
.footer-meta .center{text-align:center;color:#B4BED0}
.footer-meta .right{text-align:right;letter-spacing:.18em;font-size:10px}
.footer-bottom{
  display:flex;
  justify-content:space-between;
  gap:28px;
  align-items:center;
  padding-top:17px;
  color:#68758E;
  font-size:11px
}
.footer-bottom-links{display:flex;gap:24px;flex-wrap:wrap}
.footer-bottom a{color:#68758E}
.footer-bottom a:hover{color:#AEB7CA}

/* exact Home footer width */
footer .footer-container{
  width:min(1220px,calc(100% - 128px))!important;
  max-width:1220px!important;
  margin-left:auto!important;
  margin-right:auto!important
}

@media(max-width:980px){
  .footer-main{grid-template-columns:1.25fr 1fr;gap:46px 60px}
  .footer-brand{grid-column:1/-1}
}
@media(max-width:640px){
  footer{padding-top:48px}
  footer .footer-container{width:calc(100% - 40px)!important}
  .footer-main{grid-template-columns:1fr;gap:34px}
  .footer-brand{grid-column:auto}
  .footer-meta{grid-template-columns:1fr;gap:12px}
  .footer-meta .center,.footer-meta .right{text-align:left}
  .footer-bottom{align-items:flex-start;flex-direction:column}
  .footer-bottom-links{gap:12px;flex-direction:column}
}
</style>
'''

casos = casos.replace("</head>", css + "\n</head>", 1)
casos_path.write_text(casos, encoding="utf-8")
