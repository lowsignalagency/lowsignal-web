from pathlib import Path
import re

p = Path('nosotros.html')
s = p.read_text(encoding='utf-8')

# Remove the old body-based exit transition. The current v2 navigation uses
# the html class handled by team-profile-link-transition-v1 instead.
s = re.sub(
    r'\n?<style id="team-profile-exit-transition-v1">.*?</style>\n?',
    '\n',
    s,
    count=1,
    flags=re.S,
)

# Remove the legacy anonymous click handler that navigates after 220 ms.
legacy_nav = re.compile(
    r'\n?<script>\s*\(function\(\)\{\s*'
    r"document\.addEventListener\('click',function\(e\)\{\s*"
    r'var a=e\.target\.closest\(\'a\[href\*="/equipo/"\]\'\);.*?'
    r"document\.body\.classList\.add\('team-profile-leaving'\);\s*"
    r'setTimeout\(function\(\)\{window\.location\.href=a\.href;\},220\);\s*'
    r'\}\);\s*\}\)\(\);\s*</script>\n?',
    re.S,
)
s, removed_legacy = legacy_nav.subn('\n', s, count=1)
if removed_legacy != 1:
    raise SystemExit(f'legacy navigation handler removal count={removed_legacy}')

# Remove the first scroll-restoration experiment; v2 owns both navigation and
# restoration now, so there must be only one source of truth.
s = re.sub(
    r'\n?<script id="team-profile-return-scroll-v1">.*?</script>\n?',
    '\n',
    s,
    count=1,
    flags=re.S,
)

if s.count('id="team-profile-navigation-v2"') != 1:
    raise SystemExit('expected exactly one team-profile-navigation-v2 script')

p.write_text(s, encoding='utf-8')
print('removed legacy team navigation; v2 is now the only profile click handler')
