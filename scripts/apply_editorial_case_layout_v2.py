from pathlib import Path
import ast
import re

# Reuse the design/config already defined in v1, but replace the central case
# block using explicit start/end markers instead of a fragile nested regex.
source = Path('scripts/apply_editorial_case_layout.py').read_text(encoding='utf-8')

style_match = re.search(r"style = r'''(.*?)'''\n\nscript = r'''", source, re.S)
script_match = re.search(r"script = r'''(.*?)'''\n\nconfigs = ", source, re.S)
configs_match = re.search(r"configs = (\{.*?\})\n\nfor file_path", source, re.S)
if not (style_match and script_match and configs_match):
    raise RuntimeError('Could not read editorial layout definitions from v1')

style = style_match.group(1)
script = script_match.group(1)
configs = ast.literal_eval(configs_match.group(1))

for file_path, c in configs.items():
    p = Path(file_path)
    s = p.read_text(encoding='utf-8')

    # Clean previous editorial layer if this is rerun.
    s = re.sub(r'\n?<style id="case-editorial-layout-v1">.*?</style>\s*', '\n', s, flags=re.S)
    s = re.sub(r'\n?<script id="case-editorial-scrollspy-v1">.*?</script>\s*', '\n', s, flags=re.S)
    s = s.replace('</head>', style + '\n</head>', 1)

    editorial = f'''
  <section class="case-editorial">
    <div class="container rechx-wrap case-editorial-grid">
      <aside class="case-editorial-aside">
        <div class="case-editorial-client">
          <img src="{c['logo']}" alt="{c['client']}">
          <h3>{c['client']}</h3>
        </div>
        <div class="case-editorial-meta">
          <div><span>OBJETIVO</span><p>{c['objective']}</p></div>
          <div><span>TRABAJO</span><p>{c['work']}</p></div>
        </div>
        <nav class="case-editorial-nav" aria-label="Contenido del caso">
          <div class="case-editorial-nav-label">CONTENIDOS</div>
          <a href="#case-context">Contexto</a>
          <a href="#case-finding">Lo que encontramos</a>
          <a href="#case-build">Lo que construimos</a>
          <a href="#case-result">Resultado</a>
        </nav>
      </aside>

      <div class="case-editorial-content">
        <section class="case-editorial-block" id="case-context">
          <p class="case-editorial-eyebrow">EL CASO</p>
          <h2>{c['context_title']}</h2>
          <p class="case-editorial-lead">{c['context_copy']}</p>
          <figure class="case-editorial-media"><img src="{c['context_image']}" alt="{c['client']}"></figure>
        </section>

        <section class="case-editorial-block" id="case-finding">
          <div class="case-editorial-number">01</div>
          <h3>{c['finding_title']}</h3>
          <p class="case-editorial-copy">{c['finding_copy']}</p>
        </section>

        <section class="case-editorial-block" id="case-build">
          <div class="case-editorial-number">02</div>
          <h3>{c['build_title']}</h3>
          <p class="case-editorial-copy">{c['build_copy']}</p>
          <div class="case-editorial-pair">
            <figure><img src="{c['image1']}" alt="{c['client']}"></figure>
            <figure><img src="{c['image2']}" alt="{c['client']}"></figure>
          </div>
          <div class="case-editorial-callout"><span>{c['work']}</span><h4>{c['callout']}</h4><p>{c['callout_copy']}</p></div>
        </section>

        <section class="case-editorial-block" id="case-result">
          <div class="case-editorial-number">03</div>
          <div class="case-editorial-result">
            <p class="case-editorial-eyebrow">LA TRANSFORMACIÓN</p>
            <h3>{c['result_title']}</h3>
            <p class="case-editorial-copy">{c['result_copy']}</p>
          </div>
        </section>
      </div>
    </div>
  </section>
'''

    start_marker = '<section class="rechx-intro">'
    end_marker = '<section class="rechx-quote">'
    start = s.find(start_marker)
    end = s.find(end_marker)
    if start == -1 or end == -1 or end <= start:
        raise RuntimeError(f'Could not locate central case block in {file_path}')

    # Preserve indentation/newline around quote section.
    s = s[:start] + editorial + '\n  ' + s[end:]
    s = s.replace('</body>', script + '\n</body>', 1)
    p.write_text(s, encoding='utf-8')
