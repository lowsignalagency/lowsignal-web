from pathlib import Path

repls = {
    '>Educación</a>': '>Para colegios / Proveedores de educación</a>',
    '>Empresas B2B</a>': '>Para B2B / Empresas</a>',
    '>Marcas B2C</a>': '>Para B2C / Marcas</a>',
    '<strong>Educación</strong>': '<strong>Para colegios / Proveedores de educación</strong>',
    '<strong>Empresas B2B</strong>': '<strong>Para B2B / Empresas</strong>',
    '<strong>Marcas B2C</strong>': '<strong>Para B2C / Marcas</strong>',
}
changed=[]
for p in Path('.').rglob('*.html'):
    s=p.read_text(encoding='utf-8')
    original=s
    for old,new in repls.items():
        s=s.replace(old,new)
    if s!=original:
        p.write_text(s,encoding='utf-8')
        changed.append(str(p))
print(f'Updated navbar industry labels in {len(changed)} files')
for x in changed:
    print(x)
