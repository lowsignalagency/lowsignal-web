from pathlib import Path

path = Path('equipo/matias-bussinger.html')
s = path.read_text(encoding='utf-8')

summary = '<p class="tp-summary">Construye agentes, automatizaciones e integraciones que conectan datos, procesos comerciales y tecnología para acelerar adquisición, conversión y eficiencia.</p>'
linkedin = '        <a class="tp-linkedin-personal" href="https://www.linkedin.com/in/matias-bussinger-3872b4380/" target="_blank" rel="noopener">LinkedIn ↗</a>'
if 'tp-linkedin-personal' not in s:
    s = s.replace(summary, summary + '\n' + linkedin, 1)

old_consilium = '''<div class="tp-role-meta">
          <b>ConsiliumBots</b>'''
new_consilium = '''<div class="tp-role-meta">
          <div class="tp-role-brand"><img src="https://lowsignal.cl/assets/consiliumbots-logo.svg" alt="ConsiliumBots"><b>ConsiliumBots</b></div>'''
if 'tp-role-brand' not in s:
    s = s.replace(old_consilium, new_consilium, 1)

style = '''
<style id="matias-linkedin-consilium-v2">
.tp-linkedin-personal{display:inline-flex;margin-top:22px;color:#AAB7FF;font-size:12px;font-weight:600;transition:color .18s ease,transform .18s ease}
.tp-linkedin-personal:hover{color:#fff;transform:translateY(-1px)}
.tp-role-brand{display:flex;align-items:center;gap:10px;margin-bottom:4px}
.tp-role-brand img{width:30px;height:30px;object-fit:contain;flex:0 0 30px}
.tp-role-brand b{margin:0}
@media(max-width:760px){.tp-role-brand{gap:8px}.tp-role-brand img{width:26px;height:26px;flex-basis:26px}.tp-linkedin-personal{margin-top:18px}}
</style>
'''
if 'matias-linkedin-consilium-v2' not in s:
    s = s.replace('</head>', style + '\n</head>', 1)

path.write_text(s, encoding='utf-8')
