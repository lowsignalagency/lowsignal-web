from pathlib import Path

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')

# Remove prior mobile-back overrides if present.
for marker in ('felipe-mobile-back-v1','felipe-mobile-back-v2','felipe-mobile-back-v3'):
    start = s.find(f'<style id="{marker}">')
    if start != -1:
        end = s.find('</style>', start)
        if end != -1:
            s = s[:start] + s[end + len('</style>'):]

css = r'''
<style id="felipe-mobile-back-v3">
@media(max-width:760px){
  /* Keep the mobile hero clearly below the floating navbar. */
  .fq-profile{padding-top:172px!important;}
  .fq-back{display:none!important;}
}
</style>
'''
s = s.replace('</head>', css + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('Felipe mobile hero offset refined')
