from pathlib import Path

p = Path('equipo/felipe-quiroz.html')
s = p.read_text(encoding='utf-8')
marker = 'felipe-mobile-back-v1'
if marker not in s:
    css = r'''
<style id="felipe-mobile-back-v1">
@media(max-width:760px){
  .fq-profile{padding-top:146px!important;}
  .fq-back{
    position:relative;
    width:max-content;
    min-height:38px;
    margin-bottom:30px!important;
    padding:0 14px;
    display:inline-flex!important;
    align-items:center;
    border:1px solid rgba(168,184,255,.22);
    border-radius:999px;
    background:rgba(255,255,255,.045);
    color:transparent!important;
    font-size:0!important;
    line-height:1;
    backdrop-filter:blur(8px);
  }
  .fq-back::after{
    content:"← Equipo";
    color:#C6D0EA;
    font-size:12px;
    font-weight:600;
    letter-spacing:.01em;
  }
  .fq-back:hover{transform:none!important;}
}
</style>
'''
    s = s.replace('</head>', css + '\n</head>', 1)
    p.write_text(s, encoding='utf-8')
    print('Refined Felipe mobile back link')
else:
    print('Already refined')
# trigger v2
