from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
style='''\n<style id="home-mobile-industry-pills-v1">\n@media(max-width:620px){\n  .lsr-pills{\n    display:grid !important;\n    grid-template-columns:1fr !important;\n    gap:10px !important;\n    width:100% !important;\n    max-width:100% !important;\n  }\n  .lsr-pills .lsr-pill{\n    width:100% !important;\n    max-width:100% !important;\n    min-width:0 !important;\n    min-height:48px !important;\n    padding:12px 16px !important;\n    display:flex !important;\n    align-items:center !important;\n    justify-content:center !important;\n    text-align:center !important;\n    white-space:normal !important;\n    overflow-wrap:anywhere !important;\n    line-height:1.3 !important;\n    box-sizing:border-box !important;\n  }\n  .lsr-pills .lsr-primary{\n    margin-top:4px !important;\n  }\n}\n</style>\n'''
if 'home-mobile-industry-pills-v1' not in s:
    s=s.replace('</head>',style+'</head>',1)
p.write_text(s,encoding='utf-8')
print('Fixed Home mobile industry pills')
