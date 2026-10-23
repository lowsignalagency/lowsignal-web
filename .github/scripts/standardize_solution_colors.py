from pathlib import Path

files = [
    'soluciones/low-ads.html',
    'soluciones/low-web.html',
    'soluciones/low-flow.html',
    'soluciones/low-apps.html',
    'soluciones/low-scale.html',
]

style = '''
<style id="solution-family-color-rhythm-v1">
.ads-new-system,
.web-new-system,
.flow-new-system,
.apps-new-system,
.scale-new-system{
  background:#DDE6F6 !important;
}
.ls-social-faq{
  background:#EEF3FF !important;
}
</style>
'''

for filename in files:
    p = Path(filename)
    s = p.read_text()
    if 'solution-family-color-rhythm-v1' not in s:
        s = s.replace('</head>', style + '\n</head>', 1)
    p.write_text(s)
