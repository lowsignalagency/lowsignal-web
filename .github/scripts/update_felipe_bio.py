from pathlib import Path
import subprocess

p=Path('industrias/b2b.html')
s=p.read_text(encoding='utf-8')
old='<h2>Una base clara para crecer.<br><strong>Elige cuánto quieres acelerar.</strong></h2>'
new='<h2>Una base clara para crecer.<br><strong>Elige cuánto quieres<br class="b2b-pricing-title-break">acelerar.</strong></h2>'
if old not in s:
    raise SystemExit('Expected B2B pricing title not found')
s=s.replace(old,new,1)
style='''\n<style id="b2b-pricing-title-three-lines-v3">\n@media(min-width:981px){\n  .b2b-pricing-head{\n    grid-template-columns:minmax(0,1.42fr) minmax(270px,.58fr) !important;\n    gap:48px !important;\n  }\n  .b2b-pricing-head h2{\n    max-width:820px !important;\n    font-size:clamp(42px,3.45vw,52px) !important;\n    white-space:normal !important;\n  }\n}\n@media(max-width:980px){\n  .b2b-pricing-title-break{display:none}\n}\n</style>\n'''
if 'b2b-pricing-title-three-lines-v3' not in s:
    s=s.replace('</head>',style+'</head>',1)
p.write_text(s,encoding='utf-8')

subprocess.run(['git','config','user.name','lowsignal-bot'],check=True)
subprocess.run(['git','config','user.email','actions@users.noreply.github.com'],check=True)
subprocess.run(['git','add','industrias/b2b.html'],check=True)
subprocess.run(['git','commit','-m','Keep B2B pricing title to three lines'],check=True)
subprocess.run(['git','push'],check=True)
print('B2B pricing title set to three lines on desktop')
