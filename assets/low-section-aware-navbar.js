(function(){
'use strict';
if(window.__lowSectionAwareNav)return;
window.__lowSectionAwareNav=true;
var root=document.documentElement;
var style=document.createElement('style');
style.textContent=[
'@media(min-width:761px){body .lnav{background:var(--low-section-nav-bg,#070F22)!important;transition:background-color .24s ease!important}body.low-nav-on-light .lnav .lnav-logo img{filter:brightness(0)!important}body.low-nav-on-light .lnav .lnav-trigger,body.low-nav-on-light .lnav .lnav-direct{color:#111827!important}body.low-nav-on-light .lnav{border-bottom-color:rgba(12,22,44,.12)!important}}',
'@media(max-width:760px){body .nav-wrap .nav{background:var(--low-section-nav-bg,#070F22)!important;transition:background-color .24s ease!important}body.low-nav-on-light .nav-wrap .brand img{filter:brightness(0)!important}body.low-nav-on-light .nav-wrap .mobile-nav-toggle span{background:#111827!important}}',
'@media(prefers-reduced-motion:reduce){body .lnav,body .nav-wrap .nav{transition:none!important}}'
].join('');
document.head.appendChild(style);
function rgb(color){
 var m=color&&color.match(/^rgba?\(\s*(\d+)[, ]+\s*(\d+)[, ]+\s*(\d+)/i);
 return m?[+m[1],+m[2],+m[3]]:null;
}
function findBg(el){
 var current=el;
 while(current&&current!==document.body){
  var cs=getComputedStyle(current),v=rgb(cs.backgroundColor);
  if(v&&v.some(function(n){return n!==0;})&&parseFloat((cs.backgroundColor.match(/,\s*([\d.]+)\)$/)||[])[1]||'1')>.3)return v;
  if(v&&cs.backgroundColor.indexOf('rgb(')===0)return v;
  current=current.parentElement;
 }
 return null;
}
function colorOf(el){
 var cs=getComputedStyle(el);
 var c=findBg(el);
 if(c)return c;
 if(cs.backgroundImage&&cs.backgroundImage!=='none'){
  var matches=[...cs.backgroundImage.matchAll(/rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/g)];
  if(matches.length){var m=matches[matches.length-1];return [+m[1],+m[2],+m[3]];}
 }
 return null;
}
function update(){
 if(document.body.classList.contains('mobile-menu-open'))return;
 var targets=[...document.querySelectorAll('main > section,main > div,body > section')].filter(function(e){return e.getBoundingClientRect().height>40});
 var nav=document.querySelector(window.innerWidth<=760?'.nav-wrap .nav':'.lnav');
 if(!nav||!targets.length)return;
 var probe=Math.max(85,Math.round(nav.getBoundingClientRect().bottom+6));
 var target=targets.find(function(e){var r=e.getBoundingClientRect();return r.top<=probe&&r.bottom>probe;});
 if(!target)target=targets.find(function(e){return e.getBoundingClientRect().bottom>probe;})||targets[targets.length-1];
 var bg=colorOf(target);
 if(!bg){var v=getComputedStyle(target).backgroundImage;var matches=[...v.matchAll(/rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/g)];if(matches.length){var a=matches[matches.length-1];bg=[+a[1],+a[2],+a[3]];}}
 if(!bg)bg=[7,15,34];
 var luminance=(bg[0]*299+bg[1]*587+bg[2]*114)/1000;
 var light=luminance>160;
 document.body.classList.toggle('low-nav-on-light',light);
 root.style.setProperty('--low-section-nav-bg','rgb('+bg.join(',')+')');
}
var pending=false;function schedule(){if(pending)return;pending=true;requestAnimationFrame(function(){pending=false;update();});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){update();},{once:true});else update();
window.addEventListener('scroll',schedule,{passive:true});
window.addEventListener('resize',schedule,{passive:true});
})();
