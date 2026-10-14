from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
needle='<section class="low-industry-section low-industry-education" id="industrias">'
if needle not in s:
    raise SystemExit('Education section anchor not found')
anchor='<div id="planes" class="home-plans-anchor" aria-hidden="true"></div>'
if anchor not in s:
    s=s.replace(needle,anchor+'\n'+needle,1)
style='''\n<style id="home-plans-anchor-v1">\n.home-plans-anchor{height:0;scroll-margin-top:128px}\n</style>\n'''
if 'home-plans-anchor-v1' not in s:
    s=s.replace('</head>',style+'</head>',1)
p.write_text(s,encoding='utf-8')
print('Ensured #planes anchor sits immediately before Education section')
# trigger v2
