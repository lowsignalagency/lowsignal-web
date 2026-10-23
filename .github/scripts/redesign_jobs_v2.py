from pathlib import Path
import re

p = Path('recursos/jobs.html')
s = p.read_text(encoding='utf-8')

# Move open roles earlier: right after How we work.
roles = re.search(r'\n\s*<section class="jobs26-roles".*?</section>', s, flags=re.S)
work = re.search(r'\n\s*<section class="jobs26-work".*?</section>', s, flags=re.S)
if roles and work and roles.start() > work.end():
    role_block = roles.group(0)
    s = s[:roles.start()] + s[roles.end():]
    work = re.search(r'\n\s*<section class="jobs26-work".*?</section>', s, flags=re.S)
    s = s[:work.end()] + role_block + s[work.end():]

css = r'''
<style id="jobs-editorial-v2">
:root{
  --jobs2-navy:#071022;
  --jobs2-ink:#10182F;
  --jobs2-lav:#8EA3FF;
  --jobs2-lav2:#AFC0FF;
  --jobs2-ice:#F4F7FC;
  --jobs2-line:#DCE3EF;
  --jobs2-muted:#6F7B95;
}

/* Hero: one idea, two calm columns */
.jobs26-hero{
  padding:188px 0 104px!important;
  background:
    radial-gradient(760px 500px at 88% 18%,rgba(142,163,255,.14),transparent 70%),
    linear-gradient(118deg,#071022 0%,#0B142B 64%,#121B3B 100%)!important;
}
.jobs26-hero-grid{gap:94px!important;align-items:center!important}
.jobs26-hero h1{font-size:clamp(60px,6vw,86px)!important;max-width:790px!important}
.jobs26-lead{max-width:660px!important;color:#B3BED6!important;font-size:15px!important;line-height:1.78!important}
.jobs26-hero .jobs26-manifesto{
  min-height:0!important;
  padding:6px 0 6px 34px!important;
  border:0!important;
  border-radius:0!important;
  background:transparent!important;
  box-shadow:none!important;
  gap:18px!important;
}
.jobs26-hero .jobs26-manifesto::before{top:0!important;bottom:0!important}
.jobs26-hero .jobs26-manifesto>strong{font-size:clamp(31px,3vw,44px)!important;max-width:440px!important}
.jobs26-manifesto-signal{max-width:280px!important;opacity:.55!important}

/* How we work: the light editorial anchor */
.jobs26-work{
  padding:110px 0 116px!important;
  background:var(--jobs2-ice)!important;
  color:var(--jobs2-ink)!important;
}
.jobs26-work .jobs26-eyebrow{color:#657BE2!important}
.jobs26-work h2{color:var(--jobs2-ink)!important}
.jobs26-work h2 strong{color:#5C72D8!important}
.jobs26-work p,.jobs26-work-list p{color:var(--jobs2-muted)!important}
.jobs26-work-list,.jobs26-work-list article{border-color:#D6DEEB!important}
.jobs26-work-list h3{color:#17213F!important}
.jobs26-work-list article>span{color:#657BE2!important}

/* Open roles move up and become a clear recruiting moment */
.jobs26-roles{
  padding:102px 0 108px!important;
  background:#fff!important;
  color:var(--jobs2-ink)!important;
}
.jobs26-roles .jobs26-eyebrow-light{color:#657BE2!important}
.jobs26-roles .jobs26-head h2,
.jobs26-roles .jobs26-head h2 strong{color:var(--jobs2-ink)!important}
.jobs26-roles .jobs26-head h2 strong{color:#5C72D8!important}
.jobs26-roles .jobs26-head>p{color:var(--jobs2-muted)!important}
.jobs26-role-card{
  margin-top:44px!important;
  padding:30px 32px!important;
  border:1px solid #DCE3EF!important;
  border-radius:16px!important;
  background:#F8FAFD!important;
  box-shadow:none!important;
}
.jobs26-role-card::after{width:2px!important;background:linear-gradient(180deg,#AFC0FF,#667BE2)!important}
.jobs26-role-card:hover,.jobs26-role-card:focus-visible{
  transform:translateY(-2px)!important;
  background:#F3F6FC!important;
  border-color:#BEC9DF!important;
  box-shadow:0 16px 42px rgba(7,16,34,.07)!important;
}
.jobs26-role-status,.jobs26-role-main>div:first-child>span{color:#657BE2!important}
.jobs26-role-main h3{color:#111A32!important}
.jobs26-role-main p{color:#64708A!important}
.jobs26-role-meta span{border-color:#D5DDEA!important;color:#46516A!important}
.jobs26-role-link{color:#5065CB!important}
.jobs26-open-note{border-color:#DCE3EF!important}
.jobs26-open-note p{color:#64708A!important}
.jobs26-open-note a{color:#5065CB!important}

/* Culture remains dark: the emotional middle of the page */
.jobs26-culture{
  padding:104px 0 112px!important;
  background:linear-gradient(180deg,#071022,#0A1429)!important;
  color:#fff!important;
}
.jobs26-culture .jobs26-eyebrow{color:#AFC0FF!important}
.jobs26-culture .jobs26-head h2{color:#F5F7FF!important}
.jobs26-culture .jobs26-head h2 strong{color:#AFC0FF!important}
.jobs26-culture .jobs26-head>p{color:#AAB5CF!important}
.jobs26-culture-grid{gap:14px!important}
.jobs26-culture-grid article{
  min-height:200px!important;
  border-radius:14px!important;
  border:1px solid rgba(142,163,255,.17)!important;
  background:rgba(255,255,255,.035)!important;
  box-shadow:none!important;
}
.jobs26-culture-grid h3{color:#F5F7FF!important}
.jobs26-culture-grid p{color:#AAB5CF!important}
.jobs26-culture-grid article>span{color:#AFC0FF!important}

/* Gallery stays dark but breathes more */
.jobs26-gallery{padding:86px 0 94px!important;background:#071022!important}
.jobs26-gallery-head h2{color:#F5F7FF!important}
.jobs26-gallery-head h2 strong{color:#AFC0FF!important}
.jobs26-gallery-head>p{color:#AAB5CF!important}

/* Story becomes a compact strip instead of another full chapter */
.jobs26-story{padding:72px 0 70px!important;background:#0A1429!important}
.jobs26-story-layout{grid-template-columns:minmax(230px,.55fr) minmax(0,1.45fr)!important;gap:36px!important}
.jobs26-story-intro h2{font-size:clamp(32px,3.3vw,46px)!important}
.jobs26-story-intro>p:not(.jobs26-eyebrow){margin-top:16px!important}
.jobs26-story-stats{margin-top:22px!important}
.jobs26-story-card{min-height:310px!important;border-radius:16px!important}
.jobs26-story-feature{min-height:310px!important;flex-basis:590px!important}
.jobs26-story-feature figure{height:255px!important}
.jobs26-story-icon{margin:24px 0 20px!important}

/* Process / FAQ return to light surfaces for rhythm */
.jobs26-process,.jobs26-faq-refresh{
  background:#fff!important;
  color:var(--jobs2-ink)!important;
}
.jobs26-process{padding:98px 0 104px!important}
.jobs26-process h2{color:var(--jobs2-ink)!important}
.jobs26-process h2 strong{color:#5C72D8!important}
.jobs26-process-grid{border-color:#D7DFEC!important}
.jobs26-process-grid article{border-color:#D7DFEC!important}
.jobs26-process-grid h3{color:#17213F!important}
.jobs26-process-grid p{color:var(--jobs2-muted)!important}
.jobs26-process-grid span{color:#657BE2!important}
.jobs26-faq-refresh{padding:96px 0 102px!important;border-top:1px solid #E1E7F0!important}
.jobs26-faq-refresh-label{color:#657BE2!important}
.jobs26-faq-refresh-heading h2{color:var(--jobs2-ink)!important}
.jobs26-faq-refresh-heading p:not(.jobs26-faq-refresh-label){color:var(--jobs2-muted)!important}
.jobs26-faq-refresh-list,.jobs26-faq-refresh-item{border-color:#D6DEEA!important}
.jobs26-faq-refresh-item summary{color:#17213F!important}
.jobs26-faq-refresh-answer p{color:#66728A!important}

/* Final CTA */
.jobs26-final-cta{
  padding:96px 0!important;
  background:linear-gradient(118deg,#071022,#101B4A 72%,#182B91)!important;
}
.jobs26-final-cta h2{max-width:900px!important}
.jobs26-final-cta h2 strong{color:#AFC0FF!important}

/* Motion: content moves, containers stay put */
.jobs26-reveal,.jobs26-stagger{transform:none!important;opacity:1!important}
.jobs2-reveal{
  opacity:0;
  transform:translateY(14px);
  transition:opacity .6s ease,transform .66s cubic-bezier(.2,.75,.2,1);
}
.jobs2-reveal.is-visible{opacity:1;transform:none}
.jobs2-stagger>*{opacity:0;transform:translateY(12px);transition:opacity .58s ease,transform .64s cubic-bezier(.2,.75,.2,1)}
.jobs2-stagger.is-visible>*{opacity:1;transform:none}
.jobs2-stagger.is-visible>*:nth-child(2){transition-delay:.05s}
.jobs2-stagger.is-visible>*:nth-child(3){transition-delay:.10s}
.jobs2-stagger.is-visible>*:nth-child(4){transition-delay:.15s}

@media(max-width:980px){
  .jobs26-hero-grid{grid-template-columns:1fr!important;gap:46px!important}
  .jobs26-story-layout{grid-template-columns:1fr!important}
}
@media(max-width:760px){
  .jobs26-hero{padding:142px 0 76px!important}
  .jobs26-hero h1{font-size:clamp(46px,12vw,62px)!important}
  .jobs26-hero .jobs26-manifesto{padding-left:20px!important}
  .jobs26-work,.jobs26-roles,.jobs26-culture,.jobs26-process{padding:76px 0!important}
  .jobs26-gallery{padding:64px 0 70px!important}
  .jobs26-story{padding:62px 0!important}
  .jobs26-role-card{padding:22px!important}
  .jobs26-faq-refresh{padding:72px 0 78px!important}
}
@media(prefers-reduced-motion:reduce){
  .jobs2-reveal,.jobs2-stagger>*{opacity:1!important;transform:none!important;transition:none!important}
}
</style>
'''
pat = re.compile(r'<style id="jobs-editorial-v2">.*?</style>', re.S)
if pat.search(s):
    s = pat.sub(css.strip(), s, count=1)
else:
    s = s.replace('</head>', css + '\n</head>', 1)

# Replace the old section-level reveal controller with a content-level controller.
new_js = r'''<script id="jobs26-scroll-controller-v1">
(function(){
  function init(){
    document.querySelectorAll('.jobs26-reveal,.jobs26-stagger').forEach(function(el){el.classList.remove('jobs26-reveal','jobs26-stagger','is-visible')});
    var simple=[
      '.jobs26-copy > *','.jobs26-manifesto > *',
      '.jobs26-work-grid > div > *','.jobs26-head > *',
      '.jobs26-gallery-head > *','.jobs26-story-intro > *',
      '.jobs26-role-main > *','.jobs26-open-note > *',
      '.jobs26-faq-refresh-heading > *','.jobs26-final-cta .container > *'
    ];
    var stagger=['.jobs26-work-list','.jobs26-culture-grid','.jobs26-faq-refresh-list'];
    var els=[];
    simple.forEach(function(sel){document.querySelectorAll(sel).forEach(function(el){if(!el.classList.contains('jobs2-reveal')){el.classList.add('jobs2-reveal');els.push(el)}})});
    stagger.forEach(function(sel){document.querySelectorAll(sel).forEach(function(el){el.classList.add('jobs2-stagger');els.push(el)})});
    if(!('IntersectionObserver' in window)||window.matchMedia('(prefers-reduced-motion: reduce)').matches){els.forEach(function(el){el.classList.add('is-visible')});return}
    var io=new IntersectionObserver(function(entries,obs){entries.forEach(function(e){if(!e.isIntersecting)return;e.target.classList.add('is-visible');obs.unobserve(e.target)})},{threshold:.1,rootMargin:'0px 0px -5% 0px'});
    els.forEach(function(el){io.observe(el)});
  }
  document.readyState==='loading'?document.addEventListener('DOMContentLoaded',init,{once:true}):init();
})();
</script>'''
s = re.sub(r'<script id="jobs26-scroll-controller-v1">.*?</script>', new_js, s, count=1, flags=re.S)

p.write_text(s, encoding='utf-8')
print('jobs-editorial-v2')
