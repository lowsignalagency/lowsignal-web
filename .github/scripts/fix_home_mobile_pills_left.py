from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
style='''\n<style id="home-mobile-industry-pills-v4">\n@media(max-width:760px){\n  .lsr-home .lsr-hero .lsr-pills{\n    justify-content:flex-start !important;\n  }\n}\n</style>\n'''
if 'home-mobile-industry-pills-v4' not in s:
    s=s.replace('</body>',style+'\n</body>',1)
p.write_text(s,encoding='utf-8')
print('Left-aligned compact mobile pills')
