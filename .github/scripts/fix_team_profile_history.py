from pathlib import Path
import re

p = Path('nosotros.html')
s = p.read_text(encoding='utf-8')

# Remove every previous team-profile click transition handler so one click
# creates exactly one browser-history entry.
s = re.sub(
    r'\n?<script id="team-profile-link-transition-script">.*?</script>\n?',
    '\n',
    s,
    flags=re.S,
)

# Remove the older anonymous handler that also intercepted /equipo/ links.
s = re.sub(
    r'\n?<script>\s*\(function\(\)\{\s*document\.addEventListener\([\'\"]click[\'\"],\s*function\(e\)\{\s*var a=e\.target\.closest\([\'\"]a\[href\*=\\?\"/equipo/\\?\"\][\'\"]\);.*?window\.location\.href=a\.href;.*?\}\);\s*\}\)\(\);\s*</script>\n?',
    '\n',
    s,
    flags=re.S,
)

# Add one canonical handler. Save scroll position before leaving and restore it
# when this history entry is shown again via browser Back / bfcache.
script = r'''
<script id="team-profile-navigation-v2">
(function(){
  var KEY = 'lowsignal:nosotros-team-scroll';

  function restoreTeamScroll(){
    var raw = sessionStorage.getItem(KEY);
    if(raw === null) return;
    var y = Number(raw);
    if(!Number.isFinite(y)) return;
    requestAnimationFrame(function(){ window.scrollTo(0, y); });
  }

  window.addEventListener('pageshow', function(e){
    if(e.persisted || performance.getEntriesByType('navigation')[0]?.type === 'back_forward'){
      restoreTeamScroll();
    }
    document.documentElement.classList.remove('team-profile-leaving');
    document.body.classList.remove('team-profile-leaving');
  });

  document.addEventListener('click', function(e){
    var link = e.target.closest('a.profile-link[href*="/equipo/"]');
    if(!link || e.defaultPrevented || link.target === '_blank' || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    sessionStorage.setItem(KEY, String(window.scrollY));

    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    e.preventDefault();
    document.documentElement.classList.add('team-profile-leaving');
    window.setTimeout(function(){
      // Exactly one navigation => exactly one history entry.
      window.location.assign(link.href);
    }, 180);
  });
})();
</script>
'''

if 'team-profile-navigation-v2' not in s:
    s = s.replace('</body>', script + '\n</body>', 1)

p.write_text(s, encoding='utf-8')
print('fixed duplicate team profile navigation and browser-back restoration')
