from pathlib import Path

p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')

repls = {
    '<title>lowsignal Insiders | Programa de referidos</title>': '<title>lowsignal Insiders | La red que mueve oportunidades</title>',
    '<span class="ins-v2-title-desktop">Tu red también<br><strong>hace crecer.</strong></span>': '<span class="ins-v2-title-desktop">Conecta lo que viene.<br><strong>Desde donde estés.</strong></span>',
    '<span class="ins-v2-title-mobile">Tu red también <strong>hace crecer.</strong></span>': '<span class="ins-v2-title-mobile">Conecta lo que viene. <strong>Desde donde estés.</strong></span>',
    'Conecta empresas con lowsignal y recibe una recompensa por cada una\n          que se convierta en cliente. Tú haces la introducción. Nosotros nos encargamos del resto.': 'De Arica a Punta Arenas, estamos construyendo una red de personas inquietas, conectadas y con buen ojo para detectar empresas que pueden crecer mejor. Si eres de los que siempre sabe a quién presentar con quién, queremos conocerte.',
    '<span>RECOMPENSA POR REFERIDO</span>': '<span>RED NACIONAL</span>',
    '<strong class="ins-v2-reward-number">REWARD</strong>': '<strong class="ins-v2-reward-number">ARICA → PUNTA ARENAS</strong>',
    'Recibe una recompensa por cada nueva empresa referida que firme con lowsignal.': 'Una comunidad distribuida por Chile. Tú abres una conversación; si esa conexión se convierte en cliente, compartimos el valor contigo.',
    '<div><strong>4</strong><span>pasos simples</span></div>': '<div><strong>1</strong><span>red nacional</span></div>',
    '<span class="ins-v2-heading-desktop">Tú conectas.<br><strong>Nosotros construimos.</strong></span>': '<span class="ins-v2-heading-desktop">Una buena conexión puede<br><strong>abrir algo grande.</strong></span>',
    '<span class="ins-v2-heading-mobile">Tú conectas. <strong>Nosotros construimos.</strong></span>': '<span class="ins-v2-heading-mobile">Una buena conexión puede <strong>abrir algo grande.</strong></span>',
    'Solo tienes que hacer la introducción. Reunión, propuesta, negociación y cierre corren por nuestra cuenta.': 'Tú detectas la oportunidad y haces la introducción. Nosotros llevamos discovery, propuesta, negociación y cierre. Si se convierte en cliente, tú también ganas.',
    '<h3>Únete</h3>\n            <p>Sigue a @lowsignalagency en Instagram.</p>': '<h3>Entra a la red</h3>\n            <p>Cuéntanos quién eres, dónde estás y qué tipo de conexiones puedes activar.</p>',
    '<h3>Conecta</h3>\n            <p>Preséntanos una empresa que tenga un desafío real de crecimiento.</p>': '<h3>Detecta</h3>\n            <p>Identifica una empresa que podría crecer mejor con marketing, tecnología o automatización.</p>',
    '<h3>Nosotros hacemos el resto</h3>\n            <p>Nos reunimos, entendemos el problema y armamos la propuesta.</p>': '<h3>Abre la conversación</h3>\n            <p>Haz la introducción. Desde ahí, el equipo de lowsignal se hace cargo del proceso comercial.</p>',
    '<h3>Gana</h3>\n            <p>Recibes tu recompensa cuando firma y se confirma el primer pago.</p>': '<h3>Comparte el upside</h3>\n            <p>Cuando la empresa firma y se confirma el primer pago, recibes tu recompensa.</p>',
    '<p class="ins-v2-eyebrow ins-v2-eyebrow-dark">¿A QUIÉN PUEDES REFERIR?</p>': '<p class="ins-v2-eyebrow ins-v2-eyebrow-dark">DÓNDE ESTÁN LAS OPORTUNIDADES</p>',
    '<span class="ins-v2-heading-desktop">A organizaciones que quieran crecer<br><strong>con sistema.</strong></span>': '<span class="ins-v2-heading-desktop">Desde Arica a Punta Arenas.<br><strong>Donde haya potencial.</strong></span>',
    '<span class="ins-v2-heading-mobile">A organizaciones que quieran crecer <strong>con sistema.</strong></span>': '<span class="ins-v2-heading-mobile">Desde Arica a Punta Arenas. <strong>Donde haya potencial.</strong></span>',
    'Empresas con espacio para mejorar cómo atraen, convierten y operan.': 'Buscamos conexiones con organizaciones que quieran atraer mejor, convertir más y operar con menos fricción.',
    '<p class="ins-v2-eyebrow">TU PARTE ES SIMPLE</p>': '<p class="ins-v2-eyebrow">SER INSIDER</p>',
    '<span class="ins-v2-heading-desktop">No necesitas vender.<br><strong>Solo conectar.</strong></span>': '<span class="ins-v2-heading-desktop">Tu ventaja es tu criterio.<br><strong>No vender.</strong></span>',
    '<span class="ins-v2-heading-mobile">No necesitas vender. <strong>Solo conectar.</strong></span>': '<span class="ins-v2-heading-mobile">Tu ventaja es tu criterio. <strong>No vender.</strong></span>',
    '<article><span>01</span><div><h3>Sin horario</h3><p>No hay metas, turnos ni dedicación mínima.</p></div></article>': '<article><span>01</span><div><h3>Desde donde estés</h3><p>No importa si estás en Santiago, Arica, Concepción o Punta Arenas. Lo que importa es tu red y tu criterio.</p></div></article>',
    '<article><span>02</span><div><h3>Sin cierre comercial</h3><p>La reunión, propuesta y seguimiento los hace lowsignal.</p></div></article>': '<article><span>02</span><div><h3>Sin vender</h3><p>No eres ejecutivo comercial. Tú conectas; reunión, propuesta y seguimiento los hace lowsignal.</p></div></article>',
    '<article><span>03</span><div><h3>Sin costo</h3><p>Entrar al programa no tiene costo ni permanencia.</p></div></article>': '<article><span>03</span><div><h3>Con upside real</h3><p>Una buena introducción puede transformarse en una relación de largo plazo y una recompensa para ti.</p></div></article>',
    '<summary>¿Quién puede ser Insider?<span>+</span></summary>\n          <p>Cualquier persona que siga a @lowsignalagency en Instagram. No necesitas ser cliente ni trabajar en marketing.</p>': '<summary>¿Quién puede ser Insider?<span>+</span></summary>\n          <p>Buscamos personas conectadas, curiosas y con buen criterio para detectar oportunidades reales. No necesitas trabajar en marketing ni ser cliente de lowsignal.</p>',
}

for old, new in repls.items():
    if old not in s:
        print('WARN missing:', old[:80])
    else:
        s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
print('Insiders copy refreshed')
