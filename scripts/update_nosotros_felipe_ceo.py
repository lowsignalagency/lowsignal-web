from pathlib import Path

path = Path('nosotros.html')
text = path.read_text(encoding='utf-8')
old = 'Co-Founder & COO'
new = 'Co-Founder & CEO'
count = text.count(old)
if count == 0:
    raise SystemExit('No Co-Founder & COO occurrences found in nosotros.html')
text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
print(f'Updated {count} occurrence(s) in nosotros.html')
