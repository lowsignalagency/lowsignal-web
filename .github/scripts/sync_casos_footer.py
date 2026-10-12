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

# Copy every later style block from Nosotros that touches the footer, preserving
# the source order exactly.
overrides = []
for m in re.finditer(r'<style([^>]*)>([\s\S]*?)</style>', source, flags=re.I):
    css = m.group(2)
    if re.search(r'footer|\.footer-', css, flags=re.I):
        overrides.append(css)

# Final lower-footer lock. These are the exact dimensions used by Nosotros for
# the location/social row and the copyright/LATAM/legal row. Keeping them last
# prevents old Casos rules from making this part of the footer look smaller.
lower_footer_lock = r'''
@media(min-width:901px){
  footer .footer-meta{
    margin-top:34px !important;
    padding:17px 0 !important;
    grid-template-columns:1fr 1fr 1fr !important;
    gap:20px !important;
    font-size:11px !important;
  }
  footer .footer-bottom{
    display:grid !important;
    grid-template-columns:1fr auto 1fr !important;
    gap:28px !important;
    align-items:center !important;
    padding-top:17px !important;
    color:#68758E !important;
    font-size:11px !important;
  }
  footer .footer-bottom-links{
    display:flex !important;
    gap:24px !important;
    justify-content:flex-end !important;
    flex-wrap:wrap !important;
  }
  footer .footer-made-latam{
    display:flex !important;
    align-items:center !important;
    gap:10px !important;
    color:#8994AA !important;
    font-size:10px !important;
  }
  footer .footer-made-line{
    color:#AEB7CA !important;
    font-size:12px !important;
    line-height:1 !important;
  }
  footer .footer-made-country{
    display:inline-flex !important;
    align-items:center !important;
    padding-left:12px !important;
    border-left:1px solid rgba(137,148,170,.28) !important;
  }
  footer .footer-made-country img{
    display:block !important;
    width:40px !important;
    height:auto !important;
    object-fit:contain !important;
    opacity:.92 !important;
  }
}
'''

clone = (
    '\n<style id="casos-footer-nosotros-exact">\n' +
    base_css + '\n' +
    '\n'.join(overrides) + '\n' +
    lower_footer_lock + '\n' +
    '</style>\n'
)

# Apply Nosotros footer CSS LAST in the document so Casos cannot override it.
if "</body>" not in casos:
    raise SystemExit("Casos closing body not found")
casos = casos.replace("</body>", clone + "\n</body>", 1)

casos_path.write_text(casos, encoding="utf-8")
