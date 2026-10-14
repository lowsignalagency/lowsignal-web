from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
original = text

text = text.replace('<span>01 / 03</span>', '<span>01 / 04</span>', 1)
text = text.replace('<span>02 / 03</span>', '<span>02 / 04</span>', 1)
text = text.replace('<span>03 / 03</span>', '<span>03 / 04</span>', 1)

marker = '''      <a class="lsr-case-card lsr-reveal" href="https://lowsignal.cl/casos/dulce-reino">
        <div class="lsr-case-top">
          <img class="lsr-case-logo lsr-case-logo-dulce" src="https://lowsignal.cl/assets/dulcereino-logo-trim.png" alt="DulceReino">
          <span>03 / 04</span>
        </div>
        <div class="lsr-case-quote">“</div>
        <blockquote>
          En lowsignal encontré versatilidad, compromiso y un equipo que realmente se involucra. No solo ejecutan, entienden el negocio y se involucran de verdad.
        </blockquote>
        <div class="lsr-case-bottom">
          <div class="lsr-case-person">
            <img src="https://lowsignal.cl/assets/david-suazo.jpg" alt="David Suazo">
            <div>
              <b>David Suazo</b>
              <span>Founder, DulceReino</span>
            </div>
          </div>
          <div class="lsr-case-link">Ver caso ↗</div>
        </div>
      </a>
'''

new_card = marker + '''

      <a class="lsr-case-card lsr-reveal" href="https://lowsignal.cl/casos/salvador-dali">
        <div class="lsr-case-top">
          <img class="lsr-case-logo lsr-case-logo-csd" src="https://lowsignal.cl/assets/CSD-Logo.png" alt="Colegio Salvador Dalí">
          <span>04 / 04</span>
        </div>
        <div class="lsr-case-quote">“</div>
        <blockquote>
          Con lowsignal fortalecimos nuestras redes, nos acercamos a la comunidad y potenciamos las habilidades de nuestros estudiantes.
        </blockquote>
        <div class="lsr-case-bottom">
          <div class="lsr-case-person">
            <div>
              <b>Karina Ravanal</b>
              <span>Directora, Colegio Salvador Dalí</span>
            </div>
          </div>
          <div class="lsr-case-link">Ver caso ↗</div>
        </div>
      </a>
'''

if 'Karina Ravanal' not in text:
    if marker not in text:
        raise SystemExit('DulceReino testimonial marker not found')
    text = text.replace(marker, new_card, 1)

if text == original:
    raise SystemExit('No changes made')

path.write_text(text, encoding='utf-8')
print('Updated index.html with Salvador Dalí testimonial')
