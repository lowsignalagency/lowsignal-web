from pathlib import Path

path = Path("recursos/jobs.html")
text = path.read_text(encoding="utf-8")
old = "felipe:{name:'Felipe Quiroz',role:'Co-Founder & COO'"
new = "felipe:{name:'Felipe Quiroz',role:'Co-Founder & CEO'"
if old not in text:
    raise SystemExit("Expected Felipe COO role not found in recursos/jobs.html")
text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
print("Updated Felipe role to Co-Founder & CEO in Jobs")
