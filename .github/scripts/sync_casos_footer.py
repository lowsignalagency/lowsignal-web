from pathlib import Path
import re

home = Path("index.html").read_text(encoding="utf-8")
casos_path = Path("casos.html")
casos = casos_path.read_text(encoding="utf-8")

# Exact current Home footer markup.
footer = re.search(r"<footer>[\s\S]*?</footer>", home)
if not footer:
    raise SystemExit("Home footer not found")
casos, n = re.subn(r"<footer>[\s\S]*?</footer>", footer.group(0), casos, count=1)
if n != 1:
    raise SystemExit("Casos footer replacement failed")

# Remove every previous Casos footer sync/override so nothing can fight the Home styles.
casos = re.sub(r'<style[^>]*id="[^"]*casos[^"]*footer[^"]*"[^>]*>[\s\S]*?</style>\s*', '', casos, flags=re.I)

# Extract the exact base footer CSS from Home's main stylesheet.
base_match = re.search(
    r'/\* FOOTER — expanded / editorial \*/([\s\S]*?)(?=/\* DRAWER \*/)',
    home
)
if not base_match:
    raise SystemExit("Home base footer CSS not found")
base_footer_css = "/* FOOTER — expanded / editorial */" + base_match.group(1)

# Copy every later Home-only footer override block verbatim and in the same order.
footer_override_blocks = []
for m in re.finditer(r'<style([^>]*)>([\s\S]*?)</style>', home, flags=re.I):
    attrs, css = m.group(1), m.group(2)
    style_id = re.search(r'id="([^"]+)"', attrs, flags=re.I)
    sid = style_id.group(1) if style_id else ""
    if "footer" in sid.lower():
        footer_override_blocks.append(m.group(0))

# Install Home's footer CSS LAST in Casos so its visual result is identical.
clone_css = (
    '\n<style id="casos-home-footer-base-exact">\n' +
    base_footer_css +
    '\n</style>\n' +
    '\n'.join(footer_override_blocks) +
    '\n'
)

casos = casos.replace("</head>", clone_css + "</head>", 1)
casos_path.write_text(casos, encoding="utf-8")
