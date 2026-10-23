from pathlib import Path
import re

p = Path('recursos/insiders.html')
s = p.read_text(encoding='utf-8')

marker = 'insiders-editorial-v2'

# Make the hero proposition concrete earlier.
s = s.replace(
    'Queremos llevar lowsignal al siguiente nivel y ser referentes de growth en Latinoamérica. Para hacerlo, buscamos a las personas con más visión, criterio y conexiones para crecer junto a nosotros.',
    'Insiders es la red de personas que detecta buenas oportunidades, conecta compañías con lowsignal y participa del crecimiento que ayuda a abrir. Chile es el comienzo; Latinoamérica es lo que sigue.'
)

# Tighten community framing.
s = s.replace('Los primeros ya están acá.<br><strong>Queremos sumar a más.</strong>', 'La red ya está creciendo.<br><strong>Faltan los que vienen.</strong>')
s = s.replace('LA EXPANSIÓN YA EMPEZÓ', 'ALREADY BUILDING WITH US')

# Reorder the main storytelling after hero: community -> process -> industries -> manifesto -> faq -> final.
section_classes = ['insr-community','insr-process','insr-industries','insr-manifesto','insr-faq','insr-final']
blocks = {}
for cls in section_classes:
    m = re.search(rf'\n\s*<section class="{cls}".*?</section>', s, flags=re.S)
    if not m:
        raise RuntimeError(f'Missing section {cls}')
    blocks[cls] = m.group(0)
    s = s[:m.start()] + s[m.end():]

hero = re.search(r'(\n\s*<section class="insr-hero".*?</section>)', s, flags=re.S)
if not hero:
    raise RuntimeError('Missing hero')
insert_at = hero.end()
new_order = ''.join(blocks[k] for k in ['insr-community','insr-process','insr-industries','insr-manifesto','insr-faq','insr-final'])
s = s[:insert_at] + new_order + s[insert_at:]

css = r'''
<style id="insiders-editorial-v2">
/* Insiders v2 — community first, less cards, more editorial hierarchy */
:root{
  --ins2-navy:#071022;
  --ins2-lav:#8AA4FF;
  --ins2-lav2:#A8B8FF;
  --ins2-ice:#F5F7FB;
  --ins2-line:#DCE3F0;
}

.insr-hero{
  padding:188px 0 92px!important;
  background:
    radial-gradient(760px 520px at 88% 18%,rgba(138,164,255,.14),transparent 70%),
    linear-gradient(122deg,#071022 0%,#0A132A 62%,#111A3B 100%)!important;
}
.insr-hero-grid{gap:76px!important}
.insr-hero h1{font-size:clamp(58px,6vw,84px)!important;max-width:760px!important}
.insr-hero h1 strong{color:var(--ins2-lav2)!important}
.insr-lead{max-width:660px!important;color:#B8C2D8!important;font-size:15px!important;line-height:1.78!important}
.insr-kicker,.insr-eyebrow{color:var(--ins2-lav)!important}
.insr-button-light{box-shadow:0 14px 34px rgba(0,0,0,.16)!important}
.insr-map-card{border-color:rgba(168,184,255,.18)!important;background:rgba(255,255,255,.035)!important;box-shadow:0 30px 80px rgba(0,0,0,.18)!important}
.insr-map-route{stroke:#9BADFF!important}

/* Community becomes the first proof point */
.insr-community{padding:112px 0 118px!important;background:#fff!important}
.insr-community-head{align-items:start!important;margin-bottom:46px!important}
.insr-community-head h2{font-size:clamp(44px,4.8vw,64px)!important}
.insr-community-panel{
  padding:0!important;
  border:0!important;
  background:transparent!important;
  box-shadow:none!important;
  grid-template-columns:1.2fr .8fr!important;
  gap:72px!important;
  align-items:center!important;
}
.insr-people{gap:18px!important}
.insr-people article{min-width:0!important}
.insr-person-photo{
  aspect-ratio:1/1.14!important;
  border-radius:20px!important;
  overflow:hidden!important;
  background:#E9EDF5!important;
  box-shadow:0 18px 46px rgba(7,15,34,.08)!important;
}
.insr-person-photo img{width:100%!important;height:100%!important;object-fit:cover!important;transition:transform .45s cubic-bezier(.2,.8,.2,1)!important}
.insr-people article:hover .insr-person-photo img{transform:scale(1.025)!important}
.insr-people b{margin-top:14px!important;font-size:15px!important;color:#111827!important}
.insr-people span{color:#8792A8!important;font-size:8px!important;letter-spacing:.12em!important}
.insr-community-copy{padding:0!important}
.insr-community-copy>span{color:var(--ins2-lav)!important}
.insr-community-copy h3{font-size:clamp(34px,3.8vw,50px)!important;line-height:1.04!important;letter-spacing:-.05em!important;color:#111A3B!important}
.insr-community-copy p{font-size:14px!important;line-height:1.75!important;color:#6D7892!important}
.insr-community-copy>a{background:#101A39!important;color:#fff!important;border-radius:999px!important;padding:14px 18px!important}
.insr-founder-quote{margin-top:58px!important;border-top:1px solid var(--ins2-line)!important;border-bottom:1px solid var(--ins2-line)!important;border-left:0!important;border-radius:0!important;background:transparent!important;padding:34px 0!important;box-shadow:none!important}
.insr-founder-quote>span{color:var(--ins2-lav)!important}

/* Process: connected system, not three floating cards */
.insr-process{padding:108px 0!important;background:var(--ins2-ice)!important}
.insr-process-grid{
  position:relative!important;
  grid-template-columns:repeat(3,1fr)!important;
  gap:0!important;
  margin-top:58px!important;
  border-top:1px solid #CDD6E8!important;
  border-bottom:1px solid #CDD6E8!important;
}
.insr-process-grid:before{content:"";position:absolute;left:0;right:0;top:34px;height:1px;background:linear-gradient(90deg,#A8B8FF,#D9DFEA 50%,#A8B8FF);opacity:.8}
.insr-process-grid article{
  min-height:260px!important;
  padding:54px 32px 34px!important;
  border:0!important;
  border-right:1px solid #D7DEEA!important;
  border-radius:0!important;
  background:transparent!important;
  box-shadow:none!important;
}
.insr-process-grid article:last-child{border-right:0!important}
.insr-process-grid article:hover{transform:none!important;box-shadow:none!important}
.insr-process-feature{background:linear-gradient(180deg,rgba(138,164,255,.10),rgba(138,164,255,.025))!important;color:inherit!important}
.insr-process-feature .insr-step-num,.insr-process-feature .insr-step-label{color:#667AE4!important}
.insr-process-feature h3{color:#131D40!important}
.insr-process-feature>p:last-child{color:#6F7A97!important}
.insr-step-rule{display:none!important}
.insr-step-num{position:relative;z-index:2;display:inline-grid;place-items:center;width:30px;height:30px;margin-top:-35px;border-radius:50%;background:#F5F7FB;border:1px solid #AEBBEB;color:#5F73DE!important}
.insr-step-label{margin-top:34px!important}
.insr-process-note{margin-top:24px!important;color:#8792A8!important}

/* Industries: quieter, wider, less card-y */
.insr-industries{padding:108px 0 116px!important}
.insr-industries-grid{gap:22px!important;margin-top:52px!important}
.insr-industry-card{
  min-height:300px!important;
  padding:26px!important;
  border-radius:18px!important;
  border:1px solid #E2E7F1!important;
  background:#FAFBFD!important;
  box-shadow:none!important;
}
.insr-industry-card:hover{transform:translateY(-3px)!important;box-shadow:0 18px 44px rgba(7,15,34,.06)!important;border-color:#CAD3E6!important}

/* Manifesto becomes a compact transition */
.insr-manifesto{
  padding:70px 0 64px!important;
  background:
    radial-gradient(520px 260px at 84% 20%,rgba(168,184,255,.16),transparent 70%),
    var(--ins2-navy)!important;
}
.insr-manifesto h2{max-width:940px!important;margin-top:30px!important;font-size:clamp(40px,4.7vw,62px)!important}
.insr-manifesto h2 strong{color:var(--ins2-lav2)!important}
.insr-manifesto-bottom{margin-top:22px!important}
.insr-signal-line{margin-top:34px!important;height:22px!important;opacity:.45!important}

/* FAQ + CTA */
.insr-faq{padding:104px 0!important;background:#fff!important}
.insr-final{background:linear-gradient(120deg,#071022,#111A3B)!important}
.insr-final h2 strong{color:var(--ins2-lav2)!important}

/* Softer motion: move content, not sections */
.insr-motion-ready [data-insr-reveal],
.insr-motion-ready [data-insr-stagger]>*{
  transform:translateY(16px)!important;
}
.insr-motion-ready [data-insr-reveal].insr-is-visible,
.insr-motion-ready [data-insr-stagger].insr-is-visible>*{
  transform:translateY(0)!important;
}

@media(max-width:1000px){
  .insr-community-panel{grid-template-columns:1fr!important;gap:40px!important}
  .insr-process-grid article{padding-left:22px!important;padding-right:22px!important}
}
@media(max-width:700px){
  .insr-hero{padding:136px 0 62px!important}
  .insr-hero h1{font-size:clamp(44px,11vw,60px)!important}
  .insr-community{padding:78px 0 82px!important}
  .insr-community-head{margin-bottom:30px!important}
  .insr-community-panel{gap:30px!important}
  .insr-people{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:24px 12px!important}
  .insr-person-photo{border-radius:16px!important}
  .insr-founder-quote{margin-top:42px!important;padding:28px 0!important}
  .insr-process{padding:76px 0!important}
  .insr-process-grid{grid-template-columns:1fr!important;border-top:0!important;border-bottom:0!important}
  .insr-process-grid:before{display:none!important}
  .insr-process-grid article{min-height:0!important;padding:26px 0!important;border-right:0!important;border-top:1px solid #D7DEEA!important}
  .insr-process-grid article:last-child{border-bottom:1px solid #D7DEEA!important}
  .insr-step-num{margin-top:0!important}
  .insr-step-label{margin-top:20px!important}
  .insr-industries{padding:76px 0 82px!important}
  .insr-manifesto{padding:58px 0 52px!important}
  .insr-faq{padding:76px 0!important}
}
</style>
'''

# Replace existing v2 marker if rerun, otherwise inject before </head>.
pat = re.compile(r'<style id="insiders-editorial-v2">.*?</style>', re.S)
if pat.search(s):
    s = pat.sub(css.strip(), s, count=1)
else:
    s = s.replace('</head>', css + '\n</head>', 1)

p.write_text(s, encoding='utf-8')
print('insiders-editorial-v2')
