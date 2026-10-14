from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Force fresh load of the already-correct CSD logo asset.
s = s.replace(
    'src="https://lowsignal.cl/assets/CSD-Logo.png" alt="Colegio Salvador Dalí"',
    'src="https://lowsignal.cl/assets/CSD-Logo.png?v=2" alt="Colegio Salvador Dalí"',
    1,
)

style = '''\n<style id="csd-testimonial-fix-v1">\n/* Colegio Salvador Dalí testimonial */\n.lsr-case-top .lsr-case-logo-csd{\n  height:52px !important;\n  width:auto !important;\n  max-width:250px !important;\n  object-fit:contain !important;\n  object-position:left center !important;\n  filter:none !important;\n}\n.lsr-case-person img[src*="karina-csd.jpg"]{\n  object-position:center 24% !important;\n}\n@media(max-width:760px){\n  .lsr-case-top .lsr-case-logo-csd{\n    height:46px !important;\n    max-width:210px !important;\n  }\n  .lsr-case-person img[src*="karina-csd.jpg"]{\n    object-position:center 20% !important;\n  }\n}\n</style>\n'''

if 'csd-testimonial-fix-v1' not in s:
    s = s.replace('</head>', style + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('Fixed CSD testimonial logo and Karina crop')
