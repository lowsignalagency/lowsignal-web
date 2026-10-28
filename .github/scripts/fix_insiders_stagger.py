from pathlib import Path

path = Path('recursos/insiders.html')
text = path.read_text(encoding='utf-8')
old = '''  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(2){transition-delay:.1s}\n  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(3){transition-delay:.2s}\n  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(4){transition-delay:.3s}'''
new = '''  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(2){transition-delay:.1s}\n  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(3){transition-delay:.2s}\n  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(4){transition-delay:.3s}\n  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(5){transition-delay:.4s}\n  .insr-motion-ready [data-insr-stagger].insr-is-visible>*:nth-child(6){transition-delay:.5s}'''
if old not in text:
    raise SystemExit('Target stagger block not found')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
