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
# the source order exactly. No Casos-only sizing, margin or typography overrides.
overrides = []
for m in re.finditer(r'<style([^>]*)>([\s\S]*?)</style>', source, flags=re.I):
    css = m.group(2)
    if re.search(r'footer|\.footer-', css, flags=re.I):
        overrides.append(css)

clone = (
    '\n<style id="casos-footer-nosotros-exact">\n' +
    base_css + '\n' +
    '\n'.join(overrides) + '\n' +
    '</style>\n'
)

# Apply the exact Nosotros footer CSS last so no late Casos rule can change sizes.
if "</body>" not in casos:
    raise SystemExit("Casos closing body not found")
casos = casos.replace("</body>", clone + "\n</body>", 1)

casos_path.write_text(casos, encoding="utf-8")
