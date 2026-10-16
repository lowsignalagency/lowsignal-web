from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')
card='''        <a class="home26-insight-card" href="https://lowsignal.cl/recursos/insights/lowsignal-se-expande-tres-industrias-un-sistema">
          <figure><img src="https://lowsignal.cl/assets/founders_new.jpg" alt="Fundadores de lowsignal" loading="lazy"></figure>
          <div class="home26-insight-meta"><span>EXPANSIÓN</span><b>16 OCT, 2026</b></div>
          <h3>lowsignal se expande: tres industrias, un solo sistema</h3>
          <p>Education, B2B y B2C pasan a ser nuestras tres verticales para crecer con más foco y más impacto.</p>
          <strong>Leer insight →</strong>
        </a>'''
# remove misplaced copy wherever it currently sits
s=s.replace('\n\n'+card,'',1)
# locate Home insights grid and insert after the first actual insight card (FCCT)
start=s.find('<div class="home26-insights-grid">')
if start==-1:
    raise SystemExit('Home insights grid not found')
end=s.find('</section>',start)
block=s[start:end]
first=re.search(r'<a class="home26-insight-card".*?</a>',block,flags=re.S)
if not first:
    raise SystemExit('First Home insight card not found')
insert=first.end()
block=block[:insert]+'\n\n'+card+block[insert:]
s=s[:start]+block+s[end:]
p.write_text(s,encoding='utf-8')
print('Fixed expansion card placement in Home Insights grid')