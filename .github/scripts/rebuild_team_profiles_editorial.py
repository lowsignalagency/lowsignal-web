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

/* Same subtle entrance used on Felipe */
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


def clean_inner(value: str) -> str:
    value = re.sub(r'\s+', ' ', value or '').strip()
    return value


def find_class_inner(section: str, class_name: str):
    # common block tags used by the existing profile pages
    m = re.search(rf'<(?:div|p|span)[^>]*class=["\'][^"\']*\b{re.escape(class_name)}\b[^"\']*["\'][^>]*>(.*?)</(?:div|p|span)>', section, re.S | re.I)
    return clean_inner(m.group(1)) if m else ''


def strip_block_markup(value: str) -> str:
    value = re.sub(r'</?(?:div|section|article|ul|li)[^>]*>', ' ', value, flags=re.I)
    value = re.sub(r'<br\s*/?>', ' ', value, flags=re.I)
    return clean_inner(value)


for filename in FILES:
    path = Path(filename)
    s = path.read_text(encoding='utf-8')

    section_match = re.search(r'<section[^>]*class=["\'][^"\']*\bprofile-hero\b[^"\']*["\'][^>]*>.*?</section>', s, re.S | re.I)
    if not section_match:
        raise SystemExit(f'profile-hero section not found in {filename}')
    section = section_match.group(0)

    name_m = re.search(r'<h1[^>]*>(.*?)</h1>', section, re.S | re.I)
    if not name_m:
        raise SystemExit(f'name not found in {filename}')
    name = strip_block_markup(name_m.group(1))

    role = find_class_inner(section, 'role')
    if not role:
        raise SystemExit(f'role not found in {filename}')

    photo_block = re.search(r'<(?:figure|div)[^>]*class=["\'][^"\']*\bprofile-photo\b[^"\']*["\'][^>]*>(.*?)</(?:figure|div)>', section, re.S | re.I)
    if not photo_block:
        raise SystemExit(f'profile photo block not found in {filename}')
    img_m = re.search(r'<img\b[^>]*>', photo_block.group(1), re.S | re.I)
    if not img_m:
        raise SystemExit(f'profile image not found in {filename}')
    img_tag = img_m.group(0)

    intro = find_class_inner(section, 'intro')

    bio_m = re.search(r'<div[^>]*class=["\'][^"\']*\bbio\b[^"\']*["\'][^>]*>(.*?)</div>', section, re.S | re.I)
    bio_parts = []
    if intro:
        bio_parts.append(intro)
    if bio_m:
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', bio_m.group(1), re.S | re.I)
        if paragraphs:
            bio_parts.extend(strip_block_markup(p) for p in paragraphs if clean_inner(p))
        else:
            raw = strip_block_markup(bio_m.group(1))
            if raw:
                bio_parts.append(raw)
    if not bio_parts:
        raise SystemExit(f'bio/intro not found in {filename}')

    # De-duplicate exact repeated snippets and turn them into one editorial paragraph.
    deduped = []
    for part in bio_parts:
        part = clean_inner(part)
        if part and part not in deduped:
            deduped.append(part)
    bio = ' '.join(deduped)

    links_m = re.search(r'<div[^>]*class=["\'][^"\']*\bprofile-links\b[^"\']*["\'][^>]*>(.*?)</div>', section, re.S | re.I)
    links = clean_inner(links_m.group(1)) if links_m else ''

    new_section = f'''<main class="team-editorial-page">\n  <section class="team-editorial-profile">\n    <div class="team-editorial-shell">\n      <div class="team-editorial-grid">\n        <figure class="team-editorial-photo">\n          {img_tag}\n        </figure>\n        <div class="team-editorial-copy">\n          <p class="team-editorial-kicker">TEAM</p>\n          <h1>{name}</h1>\n          <p class="team-editorial-role">{role}</p>\n          <p class="team-editorial-bio">{bio}</p>\n          {f'<div class="team-editorial-links">{links}</div>' if links else ''}\n        </div>\n      </div>\n    </div>\n  </section>\n</main>'''

    s = s[:section_match.start()] + new_section + s[section_match.end():]

    if 'id="team-editorial-profile-v1"' not in s:
        s = s.replace('</head>', STYLE + '\n</head>', 1)
    if 'id="team-editorial-motion-v1"' not in s:
        s = s.replace('</body>', SCRIPT + '\n</body>', 1)

    path.write_text(s, encoding='utf-8')
    print('rebuilt', filename)
