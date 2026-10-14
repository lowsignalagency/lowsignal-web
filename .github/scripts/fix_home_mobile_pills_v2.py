from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
style='''\n<style id="home-mobile-industry-pills-v2">\n@media(max-width:760px){\n  .lsr-home .lsr-hero .lsr-pills{\n    display:flex !important;\n    flex-direction:column !important;\n    align-items:stretch !important;\n    gap:10px !important;\n    width:100% !important;\n    max-width:100% !important;\n    overflow:visible !important;\n  }\n  .lsr-home .lsr-hero .lsr-pills > .lsr-pill{\n    flex:0 0 auto !important;\n    width:100% !important;\n    max-width:100% !important;\n    min-width:0 !important;\n    margin:0 !important;\n    min-height:48px !important;\n    padding:12px 16px !important;\n    display:flex !important;\n    align-items:center !important;\n    justify-content:center !important;\n    text-align:center !important;\n    white-space:normal !important;\n    overflow:visible !important;\n    overflow-wrap:anywhere !important;\n    word-break:normal !important;\n    line-height:1.28 !important;\n    box-sizing:border-box !important;\n    transform:none !important;\n  }\n  .lsr-home .lsr-hero .lsr-pills > .lsr-primary{\n    margin-top:4px !important;\n  }\n}\n</style>\n'''
if 'home-mobile-industry-pills-v2' not in s:
    s=s.replace('</body>',style+'\n</body>',1)
p.write_text(s,encoding='utf-8')
print('Applied final mobile pill override at end of body')
