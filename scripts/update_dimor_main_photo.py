from pathlib import Path

p = Path('casos/dimor.html')
s = p.read_text(encoding='utf-8')
s = s.replace('https://lowsignal.cl/assets/dimor-truck.jpg', 'https://lowsignal.cl/assets/dimor-concesionario.png')
s = s.replace('alt="Vehículos de Dimor en terreno"', 'alt="Automotora Dimor"')
p.write_text(s, encoding='utf-8')
