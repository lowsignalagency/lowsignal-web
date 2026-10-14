from pathlib import Path
import subprocess

path = Path('index.html')
html = path.read_text(encoding='utf-8')
old = 'KEY FEATURES'
count = html.count(old)
if count != 3:
    raise SystemExit(f'Expected 3 KEY FEATURES labels, found {count}')
html = html.replace(old, 'CARACTERÍSTICAS PRINCIPALES')
path.write_text(html, encoding='utf-8')

subprocess.run(['git','config','user.name','lowsignal-bot'], check=True)
subprocess.run(['git','config','user.email','actions@users.noreply.github.com'], check=True)
subprocess.run(['git','add','index.html'], check=True)
subprocess.run(['git','commit','-m','Translate Home feature labels'], check=True)
subprocess.run(['git','push'], check=True)
print('Updated 3 Home feature labels')
