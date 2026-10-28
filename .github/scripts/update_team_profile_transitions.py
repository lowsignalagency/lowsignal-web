from pathlib import Path

profiles = [
    Path('equipo/damian-aldunate.html'),
    Path('equipo/felipe-quiroz.html'),
    Path('equipo/jorge-munoz.html'),
    Path('equipo/lia-morice.html'),
    Path('equipo/marco-kroeger.html'),
    Path('equipo/martin-alvarado.html'),
    Path('equipo/matias-bussinger.html'),
]

profile_head = '''\n<script id="team-profile-motion-init">document.documentElement.classList.add('team-profile-motion')</script>\n<style id="team-profile-motion-v1">\n.team-profile-motion .profile-photo,\n.team-profile-motion .profile-copy,\n.team-profile-motion .fq-editorial-photo,\n.team-profile-motion .fq-editorial-copy{\n  opacity:0;\n  transform:translateY(20px);\n}\n.team-profile-motion.team-profile-motion-ready .profile-photo,\n.team-profile-motion.team-profile-motion-ready .fq-editorial-photo{\n  opacity:1;\n  transform:none;\n  transition:opacity .46s ease,transform .52s cubic-bezier(.2,.75,.2,1);\n}\n.team-profile-motion.team-profile-motion-ready .profile-copy,\n.team-profile-motion.team-profile-motion-ready .fq-editorial-copy{\n  opacity:1;\n  transform:none;\n  transition:opacity .5s ease .08s,transform .56s cubic-bezier(.2,.75,.2,1) .08s;\n}\n@media(prefers-reduced-motion:reduce){\n  .team-profile-motion .profile-photo,\n  .team-profile-motion .profile-copy,\n  .team-profile-motion .fq-editorial-photo,\n  .team-profile-motion .fq-editorial-copy{opacity:1 !important;transform:none !important;transition:none !important}\n}\n</style>\n'''

profile_script = '''\n<script id="team-profile-motion-script">\n(function(){\n  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){\n    document.documentElement.classList.add('team-profile-motion-ready');\n    return;\n  }\n  requestAnimationFrame(function(){\n    requestAnimationFrame(function(){\n      document.documentElement.classList.add('team-profile-motion-ready');\n    });\n  });\n})();\n</script>\n'''

for path in profiles:
    s = path.read_text(encoding='utf-8')
    if 'team-profile-motion-v1' not in s:
        s = s.replace('</head>', profile_head + '\n</head>', 1)
    if 'team-profile-motion-script' not in s:
        s = s.replace('</body>', profile_script + '\n</body>', 1)
    path.write_text(s, encoding='utf-8')

nosotros = Path('nosotros.html')
s = nosotros.read_text(encoding='utf-8')

nosotros_css = '''\n<style id="team-profile-link-transition-v1">\nhtml.team-profile-leaving body{opacity:.72;transition:opacity .22s ease}\n@media(prefers-reduced-motion:reduce){html.team-profile-leaving body{opacity:1;transition:none}}\n</style>\n'''
if 'team-profile-link-transition-v1' not in s:
    s = s.replace('</head>', nosotros_css + '\n</head>', 1)

nosotros_js = '''\n<script id="team-profile-link-transition-script">\n(function(){\n  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;\n  document.addEventListener('click', function(e){\n    var link = e.target.closest('a[href*="/equipo/"]');\n    if(!link || link.target === '_blank' || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;\n    var href = link.href;\n    if(!href) return;\n    e.preventDefault();\n    document.documentElement.classList.add('team-profile-leaving');\n    window.setTimeout(function(){ window.location.href = href; }, 180);\n  });\n})();\n</script>\n'''
if 'team-profile-link-transition-script' not in s:
    s = s.replace('</body>', nosotros_js + '\n</body>', 1)

nosotros.write_text(s, encoding='utf-8')
print('updated team profile transitions across all profiles and Nosotros')
