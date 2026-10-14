from pathlib import Path

repls = {
    '>Para colegios / Proveedores de educación</a>': '>Colegios / Proveedores de educación</a>',
    '>Para B2B / Empresas</a>': '>B2B / Empresas</a>',
    '>Para B2C / Marcas</a>': '>B2C / Marcas</a>',
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
    for old,new in repls.items():
        footer=footer.replace(old,new)
    if footer != original:
        p.write_text(before+footer+after,encoding='utf-8')
        changed.append(str(p))

print(f'Updated footer labels in {len(changed)} files')
for x in changed:
    print(x)
