from pathlib import Path

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')

# Remove the previous mobile-back pill override if present.
start = s.find('<style id="felipe-mobile-back-v1">')
if start != -1:
    end = s.find('</style>', start)
    if end != -1:
        s = s[:start] + s[end + len('</style>'):]

marker = 'felipe-mobile-back-v2'
if marker not in s:
    css = r'''
<style id="felipe-mobile-back-v2">
@media(max-width:760px){
  .fq-profile{padding-top:132px!important;}
  .fq-back{display:none!important;}
}
</style>
'''
    s = s.replace('</head>', css + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('Felipe mobile back link hidden')
