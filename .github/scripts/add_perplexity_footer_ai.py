from pathlib import Path
import re

button_html = '''<button class="footer-ai-button" data-ai-provider="perplexity" aria-label="Preguntar en Perplexity" title="Preguntar en Perplexity">
                <img class="footer-ai-icon" src="https://cdn.simpleicons.org/perplexity/8AA4FF" alt="Perplexity">
              </button>'''

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

    # Add Perplexity to the same provider URL map used by the shared aiPrompt.
    if 'perplexity: `https://www.perplexity.ai/?q=${q}`' not in text:
        exact = 'gemini: `https://gemini.google.com/app?query=${q}`,\n        claude: `https://claude.ai/new?q=${q}`'
        replacement = 'gemini: `https://gemini.google.com/app?query=${q}`,\n        perplexity: `https://www.perplexity.ai/?q=${q}`,\n        claude: `https://claude.ai/new?q=${q}`'
        if exact in text:
            text = text.replace(exact, replacement)
        else:
            # Some files may have spacing/comments that differ slightly.
            text, n = re.subn(
                r'(gemini:\s*`https://gemini\.google\.com/app\?query=\$\{q\}`,\s*)(claude:\s*`https://claude\.ai/new\?q=\$\{q\}`)',
                r'\1perplexity: `https://www.perplexity.ai/?q=${q}`,\n        \2',
                text,
            )
            if n == 0:
                raise SystemExit(f'AI provider URL map not found in {path}')

    if text != original:
        path.write_text(text, encoding='utf-8')
        changed.append(str(path))

print(f'Updated {len(changed)} HTML files')
for item in changed:
    print(item)
