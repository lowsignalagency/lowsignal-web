from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
old='KEY FEATURES'
count=s.count(old)
if count != 3:
    raise SystemExit(f'Expected 3 KEY FEATURES labels, found {count}')
s=s.replace(old,'CARACTERÍSTICAS PRINCIPALES')
p.write_text(s,encoding='utf-8')
print('Updated 3 feature labels')
