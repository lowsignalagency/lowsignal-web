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

# Remove every previously injected Casos footer/navbar exact-sync block.
casos = re.sub(r'<style[^>]*id="[^"]*casos[^"]*(?:footer|navbar)[^"]*"[^>]*>[\s\S]*?</style>\s*', '', casos, flags=re.I)

# Copy the base footer CSS from Nosotros.
base_match = re.search(
    r'/\* FOOTER — expanded / editorial \*/([\s\S]*?)(?=/\* DRAWER \*/)',
    source
)
if not base_match:
    raise SystemExit("Nosotros base footer CSS not found")
base_css = "/* FOOTER — expanded / editorial */" + base_match.group(1)

# Copy every later style block from Nosotros that touches the footer, preserving
# the source order exactly. No Casos-only margin, width, padding or sizing tweaks.
overrides = []
for m in re.finditer(r'<style([^>]*)>([\s\S]*?)</style>', source, flags=re.I):
    css = m.group(2)
    if re.search(r'footer|\.footer-', css, flags=re.I):
        overrides.append(css)

footer_clone = (
    '\n<style id="casos-footer-nosotros-exact">\n' +
    base_css + '\n' +
    '\n'.join(overrides) + '\n' +
    '</style>\n'
)

# Exact visible desktop navbar CTA from Nosotros.
navbar_clone = r'''
<style id="casos-navbar-nosotros-exact">
@media(min-width:761px){
  body > .lnav .lnav-contact{
    min-height:44px !important;
    height:auto !important;
    padding:0 22px !important;
    border:0 !important;
    border-radius:999px !important;
    display:inline-flex !important;
    align-items:center !important;
    justify-content:center !important;
    background:#1419E0 !important;
    color:#fff !important;
    font-size:13px !important;
    font-weight:600 !important;
    line-height:1 !important;
    box-shadow:none !important;
    white-space:nowrap !important;
    transition:transform .18s ease,background .18s ease !important;
  }
  body > .lnav .lnav-contact:hover{
    transform:translateY(-1px) !important;
    background:#2832F3 !important;
    color:#fff !important;
    box-shadow:none !important;
  }
}
@media(max-width:1100px) and (min-width:761px){
  body > .lnav .lnav-contact{
    min-height:40px !important;
    padding:0 17px !important;
    font-size:12px !important;
  }
}
</style>
'''

# Apply source-accurate styles LAST so older Casos overrides cannot win.
if "</body>" not in casos:
    raise SystemExit("Casos closing body not found")
casos = casos.replace("</body>", footer_clone + "\n" + navbar_clone + "\n</body>", 1)

casos_path.write_text(casos, encoding="utf-8")
