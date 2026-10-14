from pathlib import Path
import re

ROOT = Path('.')
PLANS_URL = 'https://lowsignal.cl/#planes'
STYLE_ID = 'global-plans-nav-button-v1'

style = '''
<style id="global-plans-nav-button-v1">
/* Global secondary CTA: Ver planes */
.lnav-plans{
  min-height:44px;
  padding:0 20px;
  border:1px solid rgba(255,255,255,.24);
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  color:#fff;
  background:transparent;
  font-size:12px;
  font-weight:600;
  white-space:nowrap;
  transition:background .18s ease,border-color .18s ease,transform .18s ease;
}
.lnav-plans:hover{
  background:rgba(255,255,255,.08);
  border-color:rgba(255,255,255,.40);
  transform:translateY(-1px);
}
.nav-plans{
  min-height:40px;
  padding:0 16px;
  border:1px solid rgba(10,10,10,.18);
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  color:#0A0A0A;
  background:transparent;
  font-size:12px;
  font-weight:600;
  white-space:nowrap;
}
.nav-plans:hover{border-color:#1419E0;color:#1419E0;background:#F5F7FF}
@media(max-width:1100px) and (min-width:761px){
  .lnav-plans{min-height:40px;padding:0 15px;font-size:11px}
}
@media(max-width:760px){
  .mobile-nav-plans{
    min-height:48px !important;
    margin-top:14px !important;
    border:1px solid rgba(20,25,224,.18) !important;
    border-radius:12px !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    color:#1419E0 !important;
    background:#F4F6FF !important;
    font-size:13px !important;
    font-weight:650 !important;
    text-decoration:none !important;
    width:100% !important;
    max-width:100% !important;
    box-sizing:border-box !important;
  }
  .mobile-nav-plans:hover{background:#EAEEFF !important}
}
</style>
'''

changed = []
for path in sorted(ROOT.rglob('*.html')):
    # Ignore anything inside .git-like hidden folders, if present.
    if any(part.startswith('.') for part in path.parts[:-1]):
        continue
    text = path.read_text(encoding='utf-8')
    if 'Hablemos' not in text:
        continue
    original = text

    # Modern visible desktop navbar.
    if 'class="lnav-contact"' in text and 'class="lnav-plans"' not in text:
        text = re.sub(
            r'(?P<indent>^[ \t]*)<a class="lnav-contact"',
            lambda m: f'{m.group("indent")}<a class="lnav-plans" href="{PLANS_URL}">Ver planes</a>\n{m.group("indent")}<a class="lnav-contact"',
            text,
            count=1,
            flags=re.M,
        )

    # Legacy desktop navbar fallback.
    if 'class="nav-talk"' in text and 'class="nav-plans"' not in text:
        text = re.sub(
            r'(?P<indent>^[ \t]*)<a class="nav-talk"',
            lambda m: f'{m.group("indent")}<a class="nav-plans" href="{PLANS_URL}">Ver planes</a>\n{m.group("indent")}<a class="nav-talk"',
            text,
            count=1,
            flags=re.M,
        )

    # Mobile menu: keep the CTA inside the expanded panel so the top bar stays compact.
    if 'class="mobile-nav-talk"' in text:
        if 'class="mobile-nav-plans"' not in text:
            text = re.sub(
                r'(?P<indent>^[ \t]*)<a class="mobile-nav-talk"',
                lambda m: f'{m.group("indent")}<a class="mobile-nav-plans" href="{PLANS_URL}">Ver planes</a>\n{m.group("indent")}<a class="mobile-nav-talk"',
                text,
                count=1,
                flags=re.M,
            )
        else:
            text = re.sub(
                r'(<a class="mobile-nav-plans" href=")[^"]*(")',
                rf'\1{PLANS_URL}\2',
                text,
            )

    # One global style block per page.
    if STYLE_ID not in text and '</head>' in text:
        text = text.replace('</head>', style + '</head>', 1)

    if text != original:
        path.write_text(text, encoding='utf-8')
        changed.append(str(path))

print(f'Updated {len(changed)} HTML files')
for p in changed:
    print(p)
