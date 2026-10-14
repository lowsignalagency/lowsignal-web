from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Remove previous override if this script is ever re-run.
s = re.sub(r'\n?<style id="home-b2c-soft-v1">.*?</style>\n?', '\n', s, flags=re.S)

override = '''
<style id="home-b2c-soft-v1">
.low-industry-b2c{background:#E9EDFF;color:#0A1230}
.low-industry-b2c .low-industry-copy>small,
.low-industry-b2c .low-industry-features>span,
.low-industry-b2c .low-industry-stats small{color:#1419E0}
.low-industry-b2c .low-industry-copy p,
.low-industry-b2c .low-industry-stats span{color:#66708A}
.low-industry-b2c .low-feature-list div{background:rgba(255,255,255,.72);border:1px solid #C9D2F3;color:#111A3A}
.low-industry-b2c .low-feature-list div:before{background:#1419E0}
.low-industry-b2c .low-industry-stats{border-top:1px solid #CAD2EE}
.low-industry-b2c .low-industry-stats>div{border-left:2px solid #AEB9F4}
.low-industry-b2c .low-btn-secondary{border:1px solid #B8C3EA;color:#0A1230;background:transparent}
.low-industry-b2c .low-btn-primary{border:1px solid #1419E0;color:#fff;background:#1419E0}
.low-industry-b2c .low-btn-secondary:hover{border-color:#1419E0;color:#1419E0;background:#F7F8FF}
.low-industry-b2c .low-btn-primary:hover{background:#2B35F0;border-color:#2B35F0}
</style>
'''

s = s.replace('</head>', override + '</head>', 1)
p.write_text(s, encoding='utf-8')
print('Softened Home B2C section')
# trigger
