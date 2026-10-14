from pathlib import Path
import subprocess

education = Path('industrias/educacion.html')
text = education.read_text(encoding='utf-8')
replacements = {
    '<li>2 reels o videos mensuales</li>': '<li>1 reel o video mensual</li>',
    '<li>Hasta 8 stories mensuales</li>': '<li>Hasta 4 stories mensuales</li>',
    '<li>Gestión de Low Ads</li>': '<li>Gestión de Ads</li>',
    '<li>Hasta 2 campañas activas</li>': '<li>Hasta 1 campaña activa</li>',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Missing expected text: {old}')
    text = text.replace(old, new, 1)
education.write_text(text, encoding='utf-8')

original_script = '''from pathlib import Path

path = Path('equipo/felipe-quiroz.html')
html = path.read_text(encoding='utf-8')

old = \'\'\'<p>Su trayectoria cruza B2B SaaS, producto, tecnología y educación. Como <strong>Product Manager en GeoVictoria</strong>, lideró pilotos enterprise y showcases de producto que generaron <strong>USD 40K+ en oportunidades comerciales</strong> y contribuyeron a un <strong>crecimiento de 50% YoY en revenue de nuevos productos</strong>. Como <strong>Head of Partnerships en Tether Education</strong>, startup estadounidense de GovTech con operación internacional, desarrolló <strong>14+ alianzas estratégicas</strong> y soluciones junto a gobiernos, instituciones educacionales y empresas tecnológicas, impulsando iniciativas que alcanzaron a <strong>20.000+ familias</strong>.</p>\'\'\'

new = \'\'\'<p>Su trayectoria cruza producto, tecnología, growth y educación. Como <strong>Product Manager en GeoVictoria</strong>, lideró pilotos enterprise y nuevas iniciativas de producto que generaron <strong>USD 40K+ en oportunidades comerciales</strong> y contribuyeron a un <strong>crecimiento de 50% YoY</strong> en revenue de nuevos productos. Previamente, como <strong>Head of Partnerships en Tether Education</strong>, impulsó alianzas y expansión internacional, desarrollando <strong>14+ partnerships estratégicos</strong> con gobiernos, instituciones educacionales y empresas tecnológicas, con iniciativas que alcanzaron a <strong>20.000+ familias</strong>.</p>\'\'\'

if old not in html:
    raise SystemExit('Target bio paragraph not found')

html = html.replace(old, new, 1)
path.write_text(html, encoding='utf-8')
print('Updated Felipe bio')
'''
Path('.github/scripts/update_felipe_bio.py').write_text(original_script, encoding='utf-8')

subprocess.run(['git','config','user.name','lowsignal-bot'], check=True)
subprocess.run(['git','config','user.email','actions@users.noreply.github.com'], check=True)
subprocess.run(['git','add','industrias/educacion.html','.github/scripts/update_felipe_bio.py'], check=True)
subprocess.run(['git','commit','-m','Adjust Education Presence scope'], check=True)
subprocess.run(['git','push','origin','HEAD:education-pricing-v1'], check=True)
