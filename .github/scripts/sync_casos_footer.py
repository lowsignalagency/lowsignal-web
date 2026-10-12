from pathlib import Path
import re

source = Path("nosotros.html").read_text(encoding="utf-8")
casos_path = Path("casos.html")
casos = casos_path.read_text(encoding="utf-8")

# 1) Copy the exact current footer markup from Nosotros.
footer = re.search(r"<footer>[\s\S]*?</footer>", source)
if not footer:
    raise SystemExit("Nosotros footer not found")
casos, n = re.subn(r"<footer>[\s\S]*?</footer>", footer.group(0), casos, count=1)
if n != 1:
    raise SystemExit("Casos footer replacement failed")

# 2) Remove all previously injected Casos footer styles so nothing competes.
casos = re.sub(r'<style[^>]*id="[^"]*casos[^"]*footer[^"]*"[^>]*>[\s\S]*?</style>\s*', '', casos, flags=re.I)

# 3) Copy the footer base CSS from Nosotros' main stylesheet.
base_match = re.search(
    r'/\* FOOTER — expanded / editorial \*/([\s\S]*?)(?=/\* DRAWER \*/)',
    source
)
if not base_match:
    raise SystemExit("Nosotros base footer CSS not found")
base_css = "/* FOOTER — expanded / editorial */" + base_match.group(1)

# 4) Copy every later style block in Nosotros that explicitly touches the footer.
overrides = []
for m in re.finditer(r'<style([^>]*)>([\s\S]*?)</style>', source, flags=re.I):
    attrs, css = m.group(1), m.group(2)
    if re.search(r'footer|\.footer-', css, flags=re.I):
        overrides.append(css)

# 5) Final margin lock: use exactly the same visible width as the Casos CTA.
# No inner padding/gutter tricks — the footer container itself matches the CTA.
final_margin_css = r'''
/* CASOS — exact CTA/footer horizontal alignment */
footer .footer-container{
  width:min(1220px, calc(100% - 128px)) !important;
  max-width:1220px !important;
  margin-left:auto !important;
  margin-right:auto !important;
  padding-left:0 !important;
  padding-right:0 !important;
  box-sizing:border-box !important;
}
@media(max-width:1100px){
  footer .footer-container{
    width:calc(100% - 48px) !important;
    max-width:none !important;
    padding-left:0 !important;
    padding-right:0 !important;
  }
}
@media(max-width:620px){
  footer .footer-container{
    width:calc(100% - 40px) !important;
    padding-left:0 !important;
    padding-right:0 !important;
  }
}
'''

clone = (
    '\n<style id="casos-footer-nosotros-exact">\n' +
    base_css + '\n' +
    '\n'.join(overrides) + '\n' +
    final_margin_css +
    '\n</style>\n'
)

casos = casos.replace("</head>", clone + "</head>", 1)
casos_path.write_text(casos, encoding="utf-8")
