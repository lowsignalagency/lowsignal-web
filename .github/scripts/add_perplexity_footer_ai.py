from pathlib import Path
import re

button_html = '''<button class="footer-ai-button" data-ai-provider="perplexity" aria-label="Preguntar en Perplexity" title="Preguntar en Perplexity">
                <img class="footer-ai-icon" src="https://cdn.simpleicons.org/perplexity/8AA4FF" alt="Perplexity">
              </button>'''

fallback_script = r'''
<script id="footer-perplexity-ai-fallback">
(() => {
  const aiPrompt = `¿Cómo puede lowsignal ayudar a mi empresa en Chile?
Busca en la web y analiza lowsignal como Growth Company. Resume:
- su propuesta de valor;
- Low Social, Low Ads, Low Web, Low Scale, Low Apps y Low Flow;
- cómo puede ayudar a Education, empresas B2B y marcas B2C;
- casos de uso concretos;
- cómo empezar a trabajar con lowsignal.
Usa https://lowsignal.cl como fuente principal y revisa sus recursos públicos cuando sea útil.`;
  const q = encodeURIComponent(aiPrompt);
  document.querySelectorAll('[data-ai-provider="perplexity"]').forEach((button) => {
    button.addEventListener('click', () => {
      window.open(`https://www.perplexity.ai/?q=${q}`, '_blank', 'noopener,noreferrer');
    });
  });
})();
</script>
'''

changed = []
for path in Path('.').rglob('*.html'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    if 'data-ai-provider="gemini"' not in text:
        continue

    original = text

    # Insert Perplexity directly after every Gemini button in footer AI groups.
    if 'data-ai-provider="perplexity"' not in text:
        pattern = re.compile(
            r'(<button class="footer-ai-button" data-ai-provider="gemini"[\s\S]*?</button>)'
        )
        text, n = pattern.subn(r'\1\n              ' + button_html, text)
        if n == 0:
            raise SystemExit(f'Gemini footer button pattern not found in {path}')

    # Prefer the existing shared aiPrompt/provider map when present.
    provider_added = 'perplexity: `https://www.perplexity.ai/?q=${q}`' in text
    if not provider_added:
        exact = 'gemini: `https://gemini.google.com/app?query=${q}`,\n        claude: `https://claude.ai/new?q=${q}`'
        replacement = 'gemini: `https://gemini.google.com/app?query=${q}`,\n        perplexity: `https://www.perplexity.ai/?q=${q}`,\n        claude: `https://claude.ai/new?q=${q}`'
        if exact in text:
            text = text.replace(exact, replacement)
            provider_added = True
        else:
            text, n = re.subn(
                r'(gemini:\s*`https://gemini\.google\.com/app\?query=\$\{q\}`,\s*)(claude:\s*`https://claude\.ai/new\?q=\$\{q\}`)',
                r'\1perplexity: `https://www.perplexity.ai/?q=${q}`,\n        \2',
                text,
            )
            provider_added = n > 0

    # Some legacy/team pages have the visual footer but not the provider URL map.
    # Give Perplexity its own minimal handler with the exact same lowsignal prompt.
    if not provider_added and 'footer-perplexity-ai-fallback' not in text:
        if '</body>' not in text:
            raise SystemExit(f'Closing body not found in {path}')
        text = text.replace('</body>', fallback_script + '\n</body>', 1)

    if text != original:
        path.write_text(text, encoding='utf-8')
        changed.append(str(path))

print(f'Updated {len(changed)} HTML files')
for item in changed:
    print(item)
