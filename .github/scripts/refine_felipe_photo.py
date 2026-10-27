from pathlib import Path
p=Path('equipo/felipe-quiroz.html')
s=p.read_text(encoding='utf-8')

# Give the profile a little more breathing room below the fixed navbar.
s=s.replace('.fq-editorial-profile{padding:142px 0 82px;background:#fff;color:#0D1420}', '.fq-editorial-profile{padding:166px 0 82px;background:#fff;color:#0D1420}', 1)

p.write_text(s, encoding='utf-8')
print('added subtle breathing room below navbar on Felipe profile')
