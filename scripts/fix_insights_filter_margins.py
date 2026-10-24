from pathlib import Path

path = Path('recursos/insights.html')
s = path.read_text(encoding='utf-8')
s = s.replace(
    'width:min(var(--insights-content,1480px),calc(100% - 160px))!important;\n  max-width:var(--insights-content,1480px)!important;',
    'width:min(1360px,calc(100% - 160px))!important;\n  max-width:1360px!important;'
)
path.write_text(s, encoding='utf-8')
