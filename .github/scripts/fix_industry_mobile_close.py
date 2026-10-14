from pathlib import Path

files = [
    Path('industrias/educacion.html'),
    Path('industrias/b2b.html'),
    Path('industrias/marcas-b2c.html'),
]

style = r'''
<style id="industry-mobile-close-fix-v1">
@media(max-width:760px){
  .mobile-toggle,
  .mobile-nav-toggle{
    position:relative !important;
    overflow:visible !important;
  }
  .mobile-toggle > span,
  .mobile-nav-toggle > span{
    opacity:0 !important;
  }
  .mobile-toggle::before,
  .mobile-toggle::after,
  .mobile-nav-toggle::before,
  .mobile-nav-toggle::after{
    content:"" !important;
    position:absolute !important;
    left:50% !important;
    top:50% !important;
    width:22px !important;
    height:1.5px !important;
    border-radius:999px !important;
    background:#fff !important;
    transform-origin:center !important;
    transition:transform .2s ease !important;
  }
  .mobile-toggle::before,
  .mobile-nav-toggle::before{
    transform:translate(-50%,-6px) !important;
  }
  .mobile-toggle::after,
  .mobile-nav-toggle::after{
    transform:translate(-50%,5px) !important;
  }
  .mobile-toggle[aria-expanded="true"]::before,
  .mobile-nav-toggle[aria-expanded="true"]::before{
    transform:translate(-50%,-50%) rotate(45deg) !important;
  }
  .mobile-toggle[aria-expanded="true"]::after,
  .mobile-nav-toggle[aria-expanded="true"]::after{
    transform:translate(-50%,-50%) rotate(-45deg) !important;
  }
  .mobile-nav-summary .industry-mobile-chevron{
    width:13px !important;
    height:9px !important;
    fill:none !important;
    stroke:currentColor !important;
    stroke-width:2 !important;
    stroke-linecap:round !important;
    stroke-linejoin:round !important;
    transition:transform .2s ease !important;
    flex:none !important;
  }
  .mobile-nav-summary[aria-expanded="true"] .industry-mobile-chevron{
    transform:rotate(180deg) !important;
  }
}
</style>
'''

chevron = '<svg class="industry-mobile-chevron" viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5 6 6.5 11 1.5"/></svg>'

for path in files:
    text = path.read_text(encoding='utf-8')
    original = text
    text = text.replace('<span>⌄</span>', chevron)
    if 'industry-mobile-close-fix-v1' not in text:
        text = text.replace('</head>', style + '</head>', 1)
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'updated {path}')
    else:
        print(f'no changes {path}')
