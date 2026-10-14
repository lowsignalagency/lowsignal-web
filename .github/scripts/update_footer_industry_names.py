from pathlib import Path

replacements = {
    '<a href="https://lowsignal.cl/industrias/educacion">Educación</a>': '<a href="https://lowsignal.cl/industrias/educacion">Para colegios / Proveedores de educación</a>',
    '<a href="https://lowsignal.cl/industrias/b2b">B2B</a>': '<a href="https://lowsignal.cl/industrias/b2b">Para B2B / Empresas</a>',
    '<a href="https://lowsignal.cl/industrias/marcas-b2c">B2C</a>': '<a href="https://lowsignal.cl/industrias/marcas-b2c">Para B2C / Marcas</a>',
}

changed=[]
for p in Path('.').rglob('*.html'):
    s=p.read_text(encoding='utf-8')
    start=s.find('<footer')
    end=s.find('</footer>', start)
    if start == -1 or end == -1:
        continue
    end += len('</footer>')
    before=s[:start]
    footer=s[start:end]
    after=s[end:]
    original=footer
    for old,new in replacements.items():
        footer=footer.replace(old,new)
    if footer != original:
        p.write_text(before+footer+after,encoding='utf-8')
        changed.append(str(p))

print(f'Updated footer industry names in {len(changed)} files')
for x in changed:
    print(x)
