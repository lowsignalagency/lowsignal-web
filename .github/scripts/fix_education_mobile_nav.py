from pathlib import Path

p = Path('industrias/educacion.html')
s = p.read_text(encoding='utf-8')

# Remove the leftover Education pricing entry from the Industries mobile submenu.
s = s.replace('<a href="#planes-education"><strong>Planes Education</strong><small>Presence, Growth y Scale</small></a>', '', 1)

style = '''\n<style id="education-mobile-nav-tap-fix-v1">\n@media(max-width:760px){\n  .mobile-bar a,\n  .mobile-toggle,\n  .mobile-nav-panel a,\n  .mobile-nav-summary{\n    -webkit-tap-highlight-color:transparent !important;\n    tap-highlight-color:transparent !important;\n  }\n  .mobile-nav-submenu a:active,\n  .mobile-nav-direct:active,\n  .mobile-nav-plans:active,\n  .mobile-nav-talk:active{\n    background:rgba(138,164,255,.12) !important;\n    color:#fff !important;\n  }\n  .mobile-nav-summary:active{\n    color:#8AA4FF !important;\n    background:transparent !important;\n  }\n}\n</style>\n'''

if 'education-mobile-nav-tap-fix-v1' not in s:
    s = s.replace('</head>', style + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('Fixed Education mobile nav pricing link and tap state')
