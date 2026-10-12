from pathlib import Path
import re

source = Path("nosotros.html").read_text(encoding="utf-8")
casos_path = Path("casos.html")
casos = casos_path.read_text(encoding="utf-8")

# Copy the exact current footer markup from Nosotros.
footer = re.search(r"<footer>[\s\S]*?</footer>", source)
if not footer:
    raise SystemExit("Nosotros footer not found")
casos, n = re.subn(r"<footer>[\s\S]*?</footer>", footer.group(0), casos, count=1)
if n != 1:
    raise SystemExit("Casos footer replacement failed")

# Remove every previously injected Casos footer block.
casos = re.sub(r'<style[^>]*id="[^"]*casos[^"]*footer[^"]*"[^>]*>[\s\S]*?</style>\s*', '', casos, flags=re.I)

# Copy the base footer CSS from Nosotros.
base_match = re.search(
    r'/\* FOOTER — expanded / editorial \*/([\s\S]*?)(?=/\* DRAWER \*/)',
    source
)
if not base_match:
    raise SystemExit("Nosotros base footer CSS not found")
base_css = "/* FOOTER — expanded / editorial */" + base_match.group(1)

# Copy every later footer-related style block from Nosotros in source order.
overrides = []
for m in re.finditer(r'<style([^>]*)>([\s\S]*?)</style>', source, flags=re.I):
    css = m.group(2)
    if re.search(r'footer|\.footer-', css, flags=re.I):
        overrides.append(css)

# Final sizing lock to visually match the current Nosotros footer at desktop.
# Casos had been rendering the lower rows slightly smaller despite sharing the
# same base rules, so these values are applied last.
size_lock = r'''
@media(min-width:901px){
  footer{font-size:14px !important;}
  footer .footer-brand img{height:24px !important;width:auto !important;}
  footer .footer-brand-copy{font-size:13px !important;line-height:1.65 !important;}
  footer .footer-claim{font-size:16px !important;}
  footer .footer-title{font-size:10px !important;}
  footer .footer-links a{font-size:13px !important;}
  footer .footer-ai-label{font-size:13px !important;}
  footer .footer-ai-button{width:42px !important;height:42px !important;}
  footer .footer-meta{font-size:12px !important;}
  footer .footer-meta-social a{width:38px !important;height:38px !important;}
  footer .footer-bottom{font-size:12px !important;}
  footer .footer-made-latam{font-size:11px !important;}
  footer .footer-made-line{font-size:13px !important;}
  footer .footer-made-country img{width:44px !important;}
  footer .footer-bottom-links{font-size:12px !important;}
}
'''

clone = (
    '\n<style id="casos-footer-nosotros-exact">\n' +
    base_css + '\n' +
    '\n'.join(overrides) + '\n' +
    size_lock + '\n' +
    '</style>\n'
)

# Apply the footer CSS last so no Casos rule can shrink it afterwards.
if "</body>" not in casos:
    raise SystemExit("Casos closing body not found")
casos = casos.replace("</body>", clone + "\n</body>", 1)

casos_path.write_text(casos, encoding="utf-8")
