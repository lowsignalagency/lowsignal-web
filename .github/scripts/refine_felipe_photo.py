from pathlib import Path

# Target profile: cinematic but subtle entrance.
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')

profile_css='''
<style id="felipe-profile-transition-v1">
@media (prefers-reduced-motion:no-preference){
  .fq-editorial-photo,
  .fq-editorial-copy{
    opacity:0;
    transform:translateY(18px);
    will-change:transform,opacity;
  }
  .fq-editorial-photo{transform:translateY(20px) scale(.985)}
  body.profile-entered .fq-editorial-photo{
    opacity:1;
    transform:translateY(0) scale(1);
    transition:opacity .58s ease,transform .72s cubic-bezier(.2,.75,.2,1);
  }
  body.profile-entered .fq-editorial-copy{
    opacity:1;
    transform:translateY(0);
    transition:opacity .58s ease .10s,transform .72s cubic-bezier(.2,.75,.2,1) .10s;
  }
  body.profile-entered .fq-home-cta{
    animation:fqCtaIn .65s ease .18s both;
  }
  @keyframes fqCtaIn{from{opacity:0}to{opacity:1}}
}
</style>
'''
profile_js='''
<script id="felipe-profile-transition-js-v1">
(function(){
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    document.body.classList.add('profile-entered');
    return;
  }
  requestAnimationFrame(function(){
    requestAnimationFrame(function(){document.body.classList.add('profile-entered');});
  });
})();
</script>
'''
if 'felipe-profile-transition-v1' not in s:
    s=s.replace('</head>',profile_css+'\n</head>',1)
if 'felipe-profile-transition-js-v1' not in s:
    s=s.replace('</body>',profile_js+'\n</body>',1)
p.write_text(s,encoding='utf-8')

# Nosotros: soften the hand-off when opening any team profile.
p=Path('nosotros.html')
s=p.read_text(encoding='utf-8')
source_css='''
<style id="team-profile-exit-transition-v1">
@media (prefers-reduced-motion:no-preference){
  body{transition:opacity .22s ease,transform .28s cubic-bezier(.2,.75,.2,1)}
  body.team-profile-leaving{opacity:.72;transform:translateY(-4px)}
}
</style>
'''
source_js='''
<script id="team-profile-exit-transition-js-v1">
(function(){
  document.addEventListener('click',function(e){
    var a=e.target.closest('a[href*="/equipo/"]');
    if(!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target==='_blank') return;
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    e.preventDefault();
    document.body.classList.add('team-profile-leaving');
    setTimeout(function(){window.location.href=a.href;},220);
  });
})();
</script>
'''
if 'team-profile-exit-transition-v1' not in s:
    s=s.replace('</head>',source_css+'\n</head>',1)
if 'team-profile-exit-transition-js-v1' not in s:
    s=s.replace('</body>',source_js+'\n</body>',1)
p.write_text(s,encoding='utf-8')

print('added subtle Nosotros -> team profile transitions')
