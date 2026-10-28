from pathlib import Path
import re

p = Path('nosotros.html')
s = p.read_text(encoding='utf-8')

# Remove all legacy team-profile transition CSS.
s = re.sub(r'\n?<style id="team-profile-exit-transition-v1">.*?</style>\n?', '\n', s, flags=re.S)
s = re.sub(r'\n?<style id="team-profile-link-transition-v1">.*?</style>\n?', '\n', s, flags=re.S)

# Remove every previous team-profile navigation/scroll handler.
for script_id in [
    'team-profile-link-transition-script',
    'team-profile-navigation-v2',
    'team-profile-return-scroll-v1',
    'team-profile-exit-transition-js-v1',
]:
    s = re.sub(
        rf'\n?<script id="{re.escape(script_id)}">.*?</script>\n?',
        '\n',
        s,
        flags=re.S,
    )

# Remove the older anonymous handler that intercepted /equipo/ links.
s = re.sub(
    r'\n?<script>\s*\(function\(\)\{.*?a\[href\*=\\?\"/equipo/\\?\"\].*?</script>\n?',
    '\n',
    s,
    flags=re.S,
)

# Keep navigation fully native. This listener only remembers the scroll position;
# it never prevents the click, delays it, or performs navigation itself.
script = r'''
<script id="team-profile-native-navigation-v1">
(function(){
  var KEY = 'lowsignal:nosotros-team-scroll';

  document.addEventListener('click', function(e){
    var link = e.target.closest('a.profile-link[href*="/equipo/"]');
    if(!link) return;
    try { sessionStorage.setItem(KEY, String(window.scrollY)); } catch(err) {}
  }, true);

  window.addEventListener('pageshow', function(e){
    var nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
    var isBackForward = e.persisted || (nav && nav.type === 'back_forward');
    if(!isBackForward) return;

    var raw = null;
    try { raw = sessionStorage.getItem(KEY); } catch(err) {}
    if(raw === null) return;

    var y = Number(raw);
    if(!Number.isFinite(y)) return;

    requestAnimationFrame(function(){
      requestAnimationFrame(function(){
        window.scrollTo(0, y);
      });
    });
  });
})();
</script>
'''

s = s.replace('</body>', script + '\n</body>', 1)

p.write_text(s, encoding='utf-8')
print('team profile links now use native browser navigation with passive scroll restore')
