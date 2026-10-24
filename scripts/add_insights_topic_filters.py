from pathlib import Path
import re

path = Path('recursos/insights.html')
s = path.read_text(encoding='utf-8')

# Remove previous generated version if the script is run again.
s = re.sub(r'\n?<style id="insights-topic-filter-v1">.*?</style>\s*', '\n', s, flags=re.S)
s = re.sub(r'\n?<section class="insights-topic-nav"[^>]*>.*?</section>\s*', '\n', s, count=1, flags=re.S)
s = re.sub(r'\n?<script id="insights-topic-filter-script">.*?</script>\s*', '\n', s, flags=re.S)

css = r'''
<style id="insights-topic-filter-v1">
.insights-topic-nav{
  position:sticky;
  top:72px;
  z-index:920;
  background:rgba(255,255,255,.96);
  border-top:1px solid #E7EBF4;
  border-bottom:1px solid #E1E6F0;
  -webkit-backdrop-filter:blur(16px);
  backdrop-filter:blur(16px);
}
.insights-topic-nav .container{
  width:min(var(--insights-content,1480px),calc(100% - 160px))!important;
  max-width:var(--insights-content,1480px)!important;
  min-height:66px;
  margin:auto;
  display:flex;
  align-items:center;
  gap:24px;
}
.insights-topic-label{
  flex:none;
  color:#7B879C;
  font-size:10px;
  font-weight:700;
  letter-spacing:.16em;
  text-transform:uppercase;
}
.insights-topic-scroll{
  min-width:0;
  display:flex;
  align-items:center;
  gap:4px;
  overflow-x:auto;
  scrollbar-width:none;
  -webkit-overflow-scrolling:touch;
}
.insights-topic-scroll::-webkit-scrollbar{display:none}
.insights-topic-filter{
  flex:none;
  min-height:34px;
  padding:0 13px;
  border:0;
  border-radius:999px;
  background:transparent;
  color:#56637D;
  font-size:12px;
  font-weight:500;
  cursor:pointer;
  white-space:nowrap;
  transition:background .18s ease,color .18s ease,transform .18s ease;
}
.insights-topic-filter:hover{color:#1419E0;background:#F2F4FF}
.insights-topic-filter.is-active{
  background:#1419E0;
  color:#fff;
}
.insights-topic-search{
  flex:none;
  width:208px;
  min-height:38px;
  display:flex;
  align-items:center;
  gap:8px;
  padding:0 13px;
  border:1px solid #E1E6F0;
  border-radius:999px;
  background:#F8FAFD;
  transition:border-color .18s ease,background .18s ease,box-shadow .18s ease;
}
.insights-topic-search:focus-within{
  border-color:#BFC8FF;
  background:#fff;
  box-shadow:0 0 0 3px rgba(20,25,224,.06);
}
.insights-topic-search svg{
  width:15px;height:15px;flex:none;
  fill:none;stroke:#8792A8;stroke-width:1.8;stroke-linecap:round;
}
.insights-topic-search input{
  width:100%;min-width:0;border:0;outline:0;background:transparent;
  color:#16213E;font:inherit;font-size:12px;
}
.insights-topic-search input::placeholder{color:#98A2B6}
.insights-new-card[hidden]{display:none!important}
.insights-filter-empty{
  display:none;
  grid-column:1/-1;
  padding:48px 24px;
  border:1px dashed #C8D1E4;
  border-radius:16px;
  color:#66738E;
  text-align:center;
  font-size:14px;
}
.insights-filter-empty.is-visible{display:block}
.insights-filter-count{
  margin:18px 0 0;
  color:#7B879C;
  font-size:12px;
}
@media(max-width:1440px){
  .insights-topic-nav .container{width:calc(100% - 96px)!important}
}
@media(max-width:1100px){
  .insights-topic-nav .container{width:calc(100% - 48px)!important;gap:14px}
  .insights-topic-label{display:none}
  .insights-topic-search{width:180px}
}
@media(max-width:760px){
  .insights-topic-nav{top:78px}
  .insights-topic-nav .container{
    width:100%!important;
    min-height:auto;
    padding:10px 16px 11px;
    display:grid;
    grid-template-columns:1fr;
    gap:8px;
  }
  .insights-topic-scroll{width:100%}
  .insights-topic-filter{min-height:32px;padding:0 12px;font-size:11px}
  .insights-topic-search{width:100%;min-height:36px}
}
</style>
'''

nav = r'''
<section class="insights-topic-nav" aria-label="Filtrar insights por tema">
  <div class="container">
    <span class="insights-topic-label">Explorar</span>
    <div class="insights-topic-scroll" role="group" aria-label="Temas">
      <button class="insights-topic-filter is-active" type="button" data-topic="all">Todos</button>
      <button class="insights-topic-filter" type="button" data-topic="growth">Growth</button>
      <button class="insights-topic-filter" type="button" data-topic="marketing">Marketing</button>
      <button class="insights-topic-filter" type="button" data-topic="ia">IA</button>
      <button class="insights-topic-filter" type="button" data-topic="producto">Producto</button>
      <button class="insights-topic-filter" type="button" data-topic="educacion">Educación</button>
      <button class="insights-topic-filter" type="button" data-topic="b2b">B2B</button>
      <button class="insights-topic-filter" type="button" data-topic="b2c">B2C</button>
      <button class="insights-topic-filter" type="button" data-topic="building">Building</button>
    </div>
    <label class="insights-topic-search" aria-label="Buscar insights">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg>
      <input type="search" placeholder="Buscar insights..." autocomplete="off">
    </label>
  </div>
</section>
'''

script = r'''
<script id="insights-topic-filter-script">
(() => {
  const normalize = (value='') => value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  const buttons = [...document.querySelectorAll('.insights-topic-filter')];
  const search = document.querySelector('.insights-topic-search input');
  const grid = document.querySelector('.insights-new-cards');
  if (!buttons.length || !search || !grid) return;

  const cards = [...grid.querySelectorAll('.insights-new-card')];
  const empty = document.createElement('div');
  empty.className = 'insights-filter-empty';
  empty.textContent = 'No encontramos insights con esos filtros.';
  grid.appendChild(empty);

  const count = document.createElement('p');
  count.className = 'insights-filter-count';
  grid.parentElement.insertBefore(count, grid);

  const classify = card => {
    const text = normalize(card.textContent);
    const tags = new Set();
    if (/growth|crecimiento|escalar|escala|demanda|conversion|pipeline/.test(text)) tags.add('growth');
    if (/marketing|contenido|campana|marca|branding|social|paid|comunic/.test(text)) tags.add('marketing');
    if (/\bia\b|ai |llm|inteligencia artificial|automat|agent|vambe|claude|openai/.test(text)) tags.add('ia');
    if (/producto|product|experiencia digital|plataforma|web|software/.test(text)) tags.add('producto');
    if (/educacion|colegio|sae|fundacion|familia|estudiante|escuela/.test(text)) tags.add('educacion');
    if (/b2b|saas|empresa|empresas|pipeline|ventas|industrial/.test(text)) tags.add('b2b');
    if (/b2c|retail|hospitality|food|consumo|marca|reservas/.test(text)) tags.add('b2c');
    if (/lowsignal|construyendo|building|founder|equipo|hito|primeros meses|6 meses|ideas puestas/.test(text)) tags.add('building');
    card.dataset.topics = [...tags].join(' ');
    return tags;
  };

  cards.forEach(classify);
  let active = 'all';

  const apply = () => {
    const query = normalize(search.value.trim());
    let visible = 0;
    cards.forEach(card => {
      const topics = new Set((card.dataset.topics || '').split(/\s+/).filter(Boolean));
      const matchesTopic = active === 'all' || topics.has(active);
      const matchesSearch = !query || normalize(card.textContent).includes(query);
      const show = matchesTopic && matchesSearch;
      card.hidden = !show;
      if (show) visible++;
    });
    empty.classList.toggle('is-visible', visible === 0);
    count.textContent = visible === cards.length ? `${visible} insights` : `${visible} de ${cards.length} insights`;
  };

  buttons.forEach(button => button.addEventListener('click', () => {
    active = button.dataset.topic;
    buttons.forEach(item => item.classList.toggle('is-active', item === button));
    apply();
  }));
  search.addEventListener('input', apply);
  apply();
})();
</script>
'''

s = s.replace('</head>', css + '\n</head>', 1)
s = s.replace('</section>\n\n  <section class="insights-new-featured">', '</section>\n' + nav + '\n  <section class="insights-new-featured">', 1)
s = s.replace('</body>', script + '\n</body>', 1)

path.write_text(s, encoding='utf-8')
