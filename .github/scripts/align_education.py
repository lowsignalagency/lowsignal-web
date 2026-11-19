#!/usr/bin/env python3
"""Align LowSignal Education's bundled page to the site's shared type rhythm."""
from pathlib import Path
import json, re, subprocess

path = Path("industrias/educacion.html")
# Recover the known-good bundled HTML before the prior serialization bug.
# Never reprocess the currently broken embedded JSON.
source = subprocess.check_output(
    ["git", "show", "1a6b583a095aefeb682ee54af6449f03a318776b:industrias/educacion.html"],
    text=True
)
match = re.search(r'(<script\s+type="__bundler/template"\s*>)(.*?)(</script>)', source, re.S)
if not match:
    raise SystemExit("Bundle template missing. No changes made.")
template = json.loads(match.group(2))
start = "<!-- lowsignal-education-alignment-v1 -->"
end = "<!-- /lowsignal-education-alignment-v1 -->"
template = re.sub(re.escape(start) + r".*?" + re.escape(end), "", template, flags=re.S)

# These source sizes are much larger than the scale used on Low Social.
# Change only heading style attributes, leaving cards, graphics, and UI state alone.
def heading_size(m):
    tag = m.group(0)
    tag = re.sub(r'font-size:\s*(?:96|84|80)px', 'font-size:64px', tag)
    tag = re.sub(r'font-size:\s*72px', 'font-size:48px', tag)
    tag = re.sub(r'font-size:\s*(?:60|56)px', 'font-size:42px', tag)
    tag = re.sub(r'font-size:\s*52px', 'font-size:40px', tag)
    return tag
template = re.sub(r'<h[12]\b[^>]*>', heading_size, template, flags=re.S)

style = """
<style id="ls-education-shared-scale">
/* Typography and visual rhythm shared with the updated Low Social pages */
html {scroll-behavior:smooth}
body {font-family:'Be Vietnam Pro',sans-serif;overflow-x:hidden}
section h1 {font-size:clamp(40px,4.6vw,64px)!important;line-height:1.09!important;letter-spacing:-.035em!important}
section h2 {font-size:clamp(30px,3.2vw,42px)!important;line-height:1.16!important;letter-spacing:-.028em!important}
section h3 {font-size:clamp(22px,2vw,28px)!important;line-height:1.22!important}
section p {font-size:clamp(15px,1.15vw,17px);line-height:1.65}
section[style*="padding:110px"] {padding-top:82px!important;padding-bottom:82px!important}
section[style*="padding:140px"] {padding-top:96px!important;padding-bottom:86px!important}
section a,section button {transition:transform .23s ease,background-color .23s ease,color .23s ease,box-shadow .23s ease}
section a:hover,section button:hover {transform:translateY(-2px)}
.ls-edu-scroll-in {animation:lsEduEnter .65s cubic-bezier(.22,1,.36,1) both}
@keyframes lsEduEnter {from{opacity:.55;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:767px) {
  section h1 {font-size:clamp(35px,9vw,44px)!important;line-height:1.1!important}
  section h2 {font-size:clamp(27px,7.2vw,34px)!important;line-height:1.18!important}
  section h3 {font-size:22px!important}
  section p {font-size:15px!important;line-height:1.65!important}
  section[style*="padding:110px"],section[style*="padding:140px"] {padding-top:60px!important;padding-bottom:60px!important}
  section {max-width:100%;box-sizing:border-box}
}
@media(prefers-reduced-motion:reduce) {
  html{scroll-behavior:auto}
  .ls-edu-scroll-in{animation:none!important}
  section a,section button{transition:none!important}
}
</style>
<script>
(function(){
  if(!('IntersectionObserver' in window))return;
  function init(){
    var seen=new WeakSet();
    var sections=document.querySelectorAll('section');
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting && !seen.has(e.target)){
          seen.add(e.target);
          e.target.classList.add('ls-edu-scroll-in');
          observer.unobserve(e.target);
        }
      });
    },{threshold:0.1});
    sections.forEach(function(s,i){if(i>0)observer.observe(s)});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
  else setTimeout(init,0);
})();
</script>
"""
# Preserve the original reference and all React-bound interactions.
injection = start + style + end
if "</helmet>" in template:
    template = template.replace("</helmet>", injection + "</helmet>", 1)
else:
    template = template.replace("</head>", injection + "</head>", 1)
# An embedded JSON script must NEVER contain literal </script>.
# Otherwise the browser closes the JSON payload early and the whole page fails.
encoded = json.dumps(template, ensure_ascii=False).replace("</", r"\u003c/")
assert json.loads(encoded) == template
updated = source[:match.start(2)] + encoded + source[match.end(2):]
check = re.search(r'(<script\s+type="__bundler/template"\s*>)(.*?)(</script>)', updated, re.S)
assert check and json.loads(check.group(2)) == template, "Embedded template JSON failed validation"
if updated != source:
    path.write_text(updated,encoding="utf-8")
    print("Education typography and motion aligned; original interactive components retained")
else:
    print("No changes needed")
