from pathlib import Path
from PIL import Image
import pillow_avif  # noqa: F401

assets = Path('assets')

logos = [
    ('ryuki.png', 'ryuki-white.png'),
    ('logo-vandalo.png', 'vandalo-white.png'),
    ('seremonta-logo.png', 'seremonta-white.png'),
]

def make_white_transparent(src_name, dst_name):
    src = assets / src_name
    dst = assets / dst_name
    im = Image.open(src).convert('RGBA')
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            # Remove near-white / light neutral background while preserving anti-aliased edges.
            lightness = (r + g + b) / 3
            spread = max(r, g, b) - min(r, g, b)
            if lightness >= 246 and spread <= 18:
                px[x, y] = (255, 255, 255, 0)
            elif lightness >= 225 and spread <= 22:
                alpha = int(a * max(0, min(1, (246 - lightness) / 21)))
                px[x, y] = (255, 255, 255, alpha)
            else:
                px[x, y] = (255, 255, 255, a)
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    im.save(dst, 'PNG', optimize=True)
    print(f'Created {dst} from {src} ({im.size[0]}x{im.size[1]})')

for src, dst in logos:
    make_white_transparent(src, dst)

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if 'assets/ryuki-white.png' not in s:
    first_anchor = '''        <div class="lsr-trust-logo">\n          <img class="lsr-case-logo-dulce" src="https://lowsignal.cl/assets/dulcereino-logo-trim.png" alt="DulceReino">\n        </div>'''
    addition = first_anchor + '''\n        <div class="lsr-trust-logo">\n          <img src="https://lowsignal.cl/assets/ryuki-white.png" alt="Ryuki">\n        </div>\n        <div class="lsr-trust-logo">\n          <img src="https://lowsignal.cl/assets/vandalo-white.png" alt="Vándalo">\n        </div>\n        <div class="lsr-trust-logo">\n          <img src="https://lowsignal.cl/assets/seremonta-white.png" alt="Se Remonta">\n        </div>'''
    if first_anchor not in s:
        raise SystemExit('Primary client logo anchor not found')
    s = s.replace(first_anchor, addition, 1)

    second_anchor = '''        <div class="lsr-trust-logo">\n          <img class="lsr-case-logo-dulce" src="https://lowsignal.cl/assets/dulcereino-logo-trim.png" alt="">\n        </div>'''
    second_addition = second_anchor + '''\n        <div class="lsr-trust-logo">\n          <img src="https://lowsignal.cl/assets/ryuki-white.png" alt="">\n        </div>\n        <div class="lsr-trust-logo">\n          <img src="https://lowsignal.cl/assets/vandalo-white.png" alt="">\n        </div>\n        <div class="lsr-trust-logo">\n          <img src="https://lowsignal.cl/assets/seremonta-white.png" alt="">\n        </div>'''
    if second_anchor not in s:
        raise SystemExit('Duplicated client logo anchor not found')
    s = s.replace(second_anchor, second_addition, 1)

# The assets are already white/transparent, but keep the global white treatment harmless.
style = '''\n<style id="v68-new-client-logos">\n/* Ryuki, Vándalo and Se Remonta — added to client trust marquee */\n.lsr-trust-marquee .lsr-trust-logos .lsr-trust-logo:nth-child(11) img,\n.lsr-trust-marquee .lsr-trust-logos .lsr-trust-logo:nth-child(12) img,\n.lsr-trust-marquee .lsr-trust-logos .lsr-trust-logo:nth-child(13) img{\n  max-width:138px !important;\n  max-height:31px !important;\n  filter:none !important;\n  opacity:.88 !important;\n}\n@media(max-width:760px){\n  .lsr-trust-marquee .lsr-trust-logos .lsr-trust-logo:nth-child(11) img,\n  .lsr-trust-marquee .lsr-trust-logos .lsr-trust-logo:nth-child(12) img,\n  .lsr-trust-marquee .lsr-trust-logos .lsr-trust-logo:nth-child(13) img{\n    max-width:108px !important;\n    max-height:24px !important;\n  }\n}\n</style>\n'''
if 'v68-new-client-logos' not in s:
    s = s.replace('</head>', style + '</head>', 1)

p.write_text(s, encoding='utf-8')
print('Added 3 client logos to both Home trust marquee tracks')
