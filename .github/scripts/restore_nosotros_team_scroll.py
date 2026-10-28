from pathlib import Path

p = Path('nosotros.html')
s = p.read_text(encoding='utf-8')

marker = '</body>'
script = r'''
<script id="team-profile-return-scroll-v1">
(function(){
  var KEY='lowsignal-nosotros-team-scroll';

  document.addEventListener('click', function(e){
    var link=e.target.closest('a.profile-link[href*="/equipo/"]');
    if(!link) return;
    try{
      sessionStorage.setItem(KEY, String(window.scrollY));
    }catch(err){}
  }, true);

  window.addEventListener('pageshow', function(){
    var nav=performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
    var isBackForward=nav && nav.type==='back_forward';
    if(!isBackForward) return;

    var saved=null;
    try{ saved=sessionStorage.getItem(KEY); }catch(err){}
    if(saved===null) return;

    var y=parseFloat(saved);
    if(!Number.isFinite(y)) return;

    requestAnimationFrame(function(){
      requestAnimationFrame(function(){
        window.scrollTo({top:y,left:0,behavior:'auto'});
        try{ sessionStorage.removeItem(KEY); }catch(err){}
      });
    });
  });
})();
</script>
'''

if 'team-profile-return-scroll-v1' not in s:
    if marker not in s:
        raise SystemExit('body marker not found')
    s = s.replace(marker, script + '\n' + marker, 1)

p.write_text(s, encoding='utf-8')
print('added explicit Nosotros team scroll restoration')
