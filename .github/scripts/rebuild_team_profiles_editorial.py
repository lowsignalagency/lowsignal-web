from pathlib import Path
import re

FILES = [
    'equipo/damian-aldunate.html',
    'equipo/jorge-munoz.html',
    'equipo/lia-morice.html',
    'equipo/marco-kroeger.html',
    'equipo/martin-alvarado.html',
    'equipo/matias-bussinger.html',
]

STYLE = r'''<style id="team-editorial-profile-v1">
.team-editorial-page{background:#fff}
.team-editorial-profile{padding:166px 0 82px;background:#fff;color:#0D1420}
.team-editorial-shell{width:min(1220px,calc(100% - 128px));margin:0 auto}
.team-editorial-grid{display:grid;grid-template-columns:minmax(380px,.82fr) minmax(0,1.18fr);gap:76px;align-items:center}
.team-editorial-copy{max-width:650px}
.team-editorial-kicker{margin:0 0 16px;color:#1419E0;font-size:11px;font-weight:700;letter-spacing:.16em}
.team-editorial-copy h1{margin:0;font-size:clamp(48px,6vw,82px);line-height:.98;letter-spacing:-.055em;font-weight:500;color:#0D1420}
.team-editorial-role{margin:20px 0 0;color:#5F6D86;font-size:17px;line-height:1.5}
.team-editorial-bio{margin:30px 0 0;color:#273247;font-size:16px;line-height:1.72;font-weight:400}
.team-editorial-bio a{color:#1419E0;text-decoration:none;font-weight:600}
.team-editorial-bio a:hover{text-decoration:underline}
.team-editorial-links{display:flex;flex-wrap:wrap;gap:24px;margin-top:34px;padding-top:22px;border-top:1px solid #E3E8F0}
.team-editorial-links a{color:#1419E0;font-size:13px;font-weight:600;transition:.2s ease}
.team-editorial-links a:hover{opacity:.72;transform:translateY(-1px)}
.team-editorial-photo{margin:0;width:min(100%,470px);aspect-ratio:4/5;border-radius:22px;overflow:hidden;background:#E7EBF2}
.team-editorial-photo img{width:100%;height:100%;object-fit:cover;object-position:center top;filter:grayscale(1) contrast(1.03)}
@media(max-width:1100px) and (min-width:761px){.team-editorial-shell{width:calc(100% - 48px)}}
@media(max-width:900px){.team-editorial-profile{padding:124px 0 68px}.team-editorial-shell{width:calc(100% - 48px)}.team-editorial-grid{grid-template-columns:1fr;gap:38px}.team-editorial-copy{max-width:720px}.team-editorial-photo{width:min(100%,460px);aspect-ratio:4/5}}
@media(max-width:560px){.team-editorial-shell{width:calc(100% - 40px)}.team-editorial-profile{padding:112px 0 54px}.team-editorial-photo{width:100%;aspect-ratio:4/5;border-radius:18px}.team-editorial-copy h1{font-size:46px}.team-editorial-role{font-size:15px}.team-editorial-bio{margin-top:26px;font-size:15px;line-height:1.72}.team-editorial-links{gap:18px}}
html:not(.team-editorial-motion-ready) .team-editorial-photo{opacity:0;transform:translateY(18px) scale(.992)}
html:not(.team-editorial-motion-ready) .team-editorial-copy{opacity:0;transform:translateY(14px)}
.team-editorial-photo{transition:opacity .48s ease,transform .58s cubic-bezier(.2,.75,.25,1)}
.team-editorial-copy{transition:opacity .46s ease .08s,transform .58s cubic-bezier(.2,.75,.25,1) .08s}
html.team-editorial-motion-ready .team-editorial-photo,html.team-editorial-motion-ready .team-editorial-copy{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.team-editorial-photo,.team-editorial-copy{transition:none!important;opacity:1!important;transform:none!important}}
</style>'''

SCRIPT = r'''<script id="team-editorial-motion-v1">
(function(){
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    document.documentElement.classList.add('team-editorial-motion-ready');
    return;
  }
  requestAnimationFrame(function(){requestAnimationFrame(function(){
    document.documentElement.classList.add('team-editorial-motion-ready');
  });});
})();
</script>'''

def clean(v):
    return re.sub(r'\s+', ' ', v or '').strip()

def text_only(v):
    v = re.sub(r'<br\s*/?>', ' ', v or '', flags=re.I)
    v = re.sub(r'<[^>]+>', ' ', v)
    return clean(v)

def section_by_class(s, cls):
    return re.search(rf'<section[^>]*class=["\'][^"\']*\b{cls}\b[^"\']*["\'][^>]*>.*?</section>', s, re.S|re.I)

def div_inner(section, cls):
    m = re.search(rf'<div[^>]*class=["\'][^"\']*\b{cls}\b[^"\']*["\'][^>]*>(.*?)</div>', section, re.S|re.I)
    return m.group(1) if m else ''

def p_inner(section, cls):
    m = re.search(rf'<p[^>]*class=["\'][^"\']*\b{cls}\b[^"\']*["\'][^>]*>(.*?)</p>', section, re.S|re.I)
    return m.group(1) if m else ''

def build_section(name, role, img_tag, bio, links):
    links_html = f'<div class="team-editorial-links">{links}</div>' if links else ''
    return f'''<section class="team-editorial-profile">\n  <div class="team-editorial-shell">\n    <div class="team-editorial-grid">\n      <figure class="team-editorial-photo">\n        {img_tag}\n      </figure>\n      <div class="team-editorial-copy">\n        <p class="team-editorial-kicker">TEAM</p>\n        <h1>{name}</h1>\n        <p class="team-editorial-role">{role}</p>\n        <p class="team-editorial-bio">{bio}</p>\n        {links_html}\n      </div>\n    </div>\n  </div>\n</section>'''

for filename in FILES:
    path = Path(filename)
    s = path.read_text(encoding='utf-8')
    title_m = re.search(r'<title>(.*?)\|\s*(.*?)\|\s*lowsignal</title>', s, re.S|re.I)
    if not title_m:
        raise SystemExit(f'title/role not found in {filename}')
    name_title = clean(title_m.group(1))
    role_title = clean(title_m.group(2))

    section_match = section_by_class(s, 'tp-profile')
    mode = 'tp'
    if not section_match:
        section_match = section_by_class(s, 'profile-hero')
        mode = 'profile'
    if not section_match:
        raise SystemExit(f'profile section not found in {filename}')
    section = section_match.group(0)

    if mode == 'tp':
        name_m = re.search(r'<h1[^>]*>(.*?)</h1>', section, re.S|re.I)
        name = text_only(name_m.group(1)) if name_m else name_title
        img_m = re.search(r'<img[^>]*class=["\'][^"\']*\btp-photo\b[^"\']*["\'][^>]*>', section, re.S|re.I)
        if not img_m:
            raise SystemExit(f'tp-photo image not found in {filename}')
        img_tag = re.sub(r'\sclass=["\'][^"\']*\btp-photo\b[^"\']*["\']', '', img_m.group(0), count=1, flags=re.I)
        parts = [text_only(p_inner(section,'tp-positioning')), text_only(p_inner(section,'tp-summary'))]
        parts = [p for i,p in enumerate(parts) if p and p not in parts[:i]]
        bio = ' '.join(parts)
        links = clean(div_inner(section,'tp-profile-links'))
    else:
        name_m = re.search(r'<h1[^>]*>(.*?)</h1>', section, re.S|re.I)
        name = text_only(name_m.group(1)) if name_m else name_title
        role_m = re.search(r'<div[^>]*class=["\'][^"\']*\brole\b[^"\']*["\'][^>]*>(.*?)</div>', section, re.S|re.I)
        role_title = text_only(role_m.group(1)) if role_m else role_title
        photo_block = re.search(r'<div[^>]*class=["\'][^"\']*\bprofile-photo\b[^"\']*["\'][^>]*>(.*?)</div>', section, re.S|re.I)
        if not photo_block:
            raise SystemExit(f'profile-photo not found in {filename}')
        img_m = re.search(r'<img\b[^>]*>', photo_block.group(1), re.S|re.I)
        if not img_m:
            raise SystemExit(f'profile image not found in {filename}')
        img_tag = img_m.group(0)
        parts = [text_only(p_inner(section,'intro'))]
        bio_block = div_inner(section,'bio')
        parts += [text_only(x) for x in re.findall(r'<p[^>]*>(.*?)</p>', bio_block, re.S|re.I)]
        parts = [p for i,p in enumerate(parts) if p and p not in parts[:i]]
        bio = ' '.join(parts)
        links = clean(div_inner(section,'profile-links'))

    if not bio:
        raise SystemExit(f'bio not found in {filename}')
    role = role_title + ', lowsignal'
    new_section = build_section(name, role, img_tag, bio, links)
    s = s[:section_match.start()] + new_section + s[section_match.end():]

    for cls in ('tp-about','tp-expertise','tp-selected'):
        s = re.sub(rf'<section[^>]*class=["\'][^"\']*\b{cls}\b[^"\']*["\'][^>]*>.*?</section>', '', s, count=1, flags=re.S|re.I)

    if 'id="team-editorial-profile-v1"' not in s:
        s = s.replace('</head>', STYLE+'\n</head>', 1)
    if 'id="team-editorial-motion-v1"' not in s:
        s = s.replace('</body>', SCRIPT+'\n</body>', 1)

    path.write_text(s, encoding='utf-8')
    print('rebuilt', filename, mode)
