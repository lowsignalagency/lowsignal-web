from pathlib import Path
import re

files = [
    'soluciones/low-social.html',
    'soluciones/low-ads.html',
    'soluciones/low-web.html',
    'soluciones/low-flow.html',
    'soluciones/low-apps.html',
    'soluciones/low-scale.html',
]

style = '''
<style id="solution-family-color-rhythm-v2">
/* Keep the System block visually identical across every solution page. */
body .ls-social-smart,
body .ls-social-smart.ads-new-system,
body .ls-social-smart.web-new-system,
body .ls-social-smart.flow-new-system,
body .ls-social-smart.apps-new-system,
body .ls-social-smart.scale-new-system{
  background:#DDE6F6 !important;
  background-color:#DDE6F6 !important;
}
body .ls-social-faq{
  background:#EEF3FF !important;
  background-color:#EEF3FF !important;
}
</style>
'''

for filename in files:
    p = Path(filename)
    s = p.read_text(encoding='utf-8')

    # Remove any previous family color override so there is one authoritative block.
    s = re.sub(
        r'\n?<style id="solution-family-color-rhythm-v[12]">[\s\S]*?</style>\n?',
        '\n',
        s,
        count=1,
    )

    # Place the override at the very end of <head>, after all inherited page CSS.
    s = s.replace('</head>', style + '\n</head>', 1)
    p.write_text(s, encoding='utf-8')
