from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
needle='<section class="low-industry-section low-industry-education" id="industrias">'
if needle not in s:
    raise SystemExit('Education section anchor not found')
if 'id="planes"' not in s:
    repl='<div id="planes" class="home-plans-anchor" aria-hidden="true"></div>\n'+needle
    s=s.replace(needle,repl,1)
style='''\n<style id="home-plans-anchor-v1">\n.home-plans-anchor{height:0;scroll-margin-top:128px}\n</style>\n'''
if 'home-plans-anchor-v1' not in s:
    s=s.replace('</head>',style+'</head>',1)
p.write_text(s,encoding='utf-8')
print('Added #planes anchor before Education section')
