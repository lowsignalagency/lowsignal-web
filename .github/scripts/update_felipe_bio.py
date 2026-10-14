from pathlib import Path

path = Path('equipo/felipe-quiroz.html')
html = path.read_text(encoding='utf-8')

old = '''<p>Su trayectoria cruza B2B SaaS, producto, tecnología y educación. Como <strong>Product Manager en GeoVictoria</strong>, lideró pilotos enterprise y showcases de producto que generaron <strong>USD 40K+ en oportunidades comerciales</strong> y contribuyeron a un <strong>crecimiento de 50% YoY en revenue de nuevos productos</strong>. Como <strong>Head of Partnerships en Tether Education</strong>, startup estadounidense de GovTech con operación internacional, desarrolló <strong>14+ alianzas estratégicas</strong> y soluciones junto a gobiernos, instituciones educacionales y empresas tecnológicas, impulsando iniciativas que alcanzaron a <strong>20.000+ familias</strong>.</p>'''

new = '''<p>Su trayectoria cruza producto, tecnología, growth y educación. Como <strong>Product Manager en GeoVictoria</strong>, lideró pilotos enterprise y nuevas iniciativas de producto que generaron <strong>USD 40K+ en oportunidades comerciales</strong> y contribuyeron a un <strong>crecimiento de 50% YoY</strong> en revenue de nuevos productos. Previamente, como <strong>Head of Partnerships en Tether Education</strong>, impulsó alianzas y expansión internacional, desarrollando <strong>14+ partnerships estratégicos</strong> con gobiernos, instituciones educacionales y empresas tecnológicas, con iniciativas que alcanzaron a <strong>20.000+ familias</strong>.</p>'''

if old not in html:
    raise SystemExit('Target bio paragraph not found')

html = html.replace(old, new, 1)
path.write_text(html, encoding='utf-8')
print('Updated Felipe bio')
