from pathlib import Path

path = Path('nosotros.html')
s = path.read_text(encoding='utf-8')

s = s.replace(
    '<div class="person-meta"><div class="person-name">Matías Bussinger</div><div class="person-role">AI Engineer</div>',
    '<div class="person-meta"><div class="person-name">Matías Bussinger</div><div class="person-role">AI Revenue Engineer</div>'
)

s = s.replace(
    "matias:{name:'Matías Bussinger',role:'AI Engineer',photo:'https://lowsignal.cl/assets/team-matias.png',bio:'Matías desarrolla soluciones con IA, creando agentes, automatizaciones e integraciones para simplificar procesos, mejorar operaciones y escalar de forma más eficiente.',tags:['AI','Automation','AI Agents']",
    "matias:{name:'Matías Bussinger',role:'AI Revenue Engineer',photo:'https://lowsignal.cl/assets/team-matias.png',bio:'Matías conecta IA, automatización y revenue para construir sistemas que ayuden a generar más oportunidades y convertir mejor. Diseña agentes, integraciones y workflows que conectan datos, procesos comerciales y tecnología para acelerar adquisición, ventas y eficiencia operativa.',tags:['AI','Revenue','Automation','AI Agents','Growth Systems']"
)

path.write_text(s, encoding='utf-8')
