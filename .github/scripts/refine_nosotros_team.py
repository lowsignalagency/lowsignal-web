from pathlib import Path

p = Path('nosotros.html')
s = p.read_text(encoding='utf-8')
marker = 'nosotros-team-editorial-v1'
if marker not in s:
    css = r'''
<style id="nosotros-team-editorial-v1">
/* Team directory refinement — balanced 3x2 editorial grid */
.team{padding:104px 0 116px!important;background:#fff!important}
.team .container{width:min(1180px,calc(100% - 96px))!important;max-width:1180px!important}
.team-grid{
  margin-top:0!important;
  display:grid!important;
  grid-template-columns:repeat(3,minmax(0,1fr))!important;
  gap:58px 30px!important;
  max-width:none!important;
}
.person{min-width:0!important}
.person-photo{
  aspect-ratio:1 / 1.16!important;
  border-radius:20px!important;
  background:#E9EDF5!important;
  box-shadow:0 16px 42px rgba(7,15,34,.07)!important;
}
.person-photo img{transition:transform .5s cubic-bezier(.2,.8,.2,1),filter .3s ease!important}
.person:hover .person-photo img{transform:scale(1.028)!important}
.person-meta{padding-top:20px!important}
.person-name{font-size:18px!important;font-weight:650!important;letter-spacing:-.025em!important;color:#111827!important}
.person-role{margin-top:5px!important;min-height:auto!important;color:#6F7B92!important;font-size:13px!important;line-height:1.5!important}
.profile-link{
  margin-top:14px!important;
  display:inline-flex!important;
  align-items:center!important;
  gap:9px!important;
  color:#7187E8!important;
  font-size:11px!important;
  font-weight:650!important;
  letter-spacing:.01em!important;
  transition:color .22s ease!important;
}
.profile-link .circle{
  width:30px!important;
  height:30px!important;
  border:1px solid rgba(138,164,255,.34)!important;
  background:#F6F8FF!important;
  color:#7187E8!important;
  box-shadow:none!important;
}
.profile-link:hover{color:#506DD8!important}
.profile-link:hover .circle{
  transform:translateX(3px)!important;
  background:#E9EEFF!important;
  border-color:#8AA4FF!important;
  color:#506DD8!important;
}
@media(max-width:980px){
  .team .container{width:calc(100% - 56px)!important}
  .team-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:46px 22px!important}
}
@media(max-width:560px){
  .team{padding:78px 0 88px!important}
  .team .container{width:calc(100% - 40px)!important}
  .team-grid{grid-template-columns:1fr!important;gap:38px!important;max-width:380px!important;margin-left:auto!important;margin-right:auto!important}
  .person-photo{aspect-ratio:1 / 1.12!important;border-radius:18px!important}
  .person-meta{padding-top:16px!important}
}
</style>
'''
    s = s.replace('</head>', css + '\n</head>', 1)
    p.write_text(s, encoding='utf-8')
    print('Refined nosotros team grid')
else:
    print('Already refined')
# trigger refinement
