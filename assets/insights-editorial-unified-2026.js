(function(){
  "use strict";
  function init(){
    /* Direct standalone articles and wrapped articles share one related-card layout. */
    var legacy=document.querySelector(".article-new-more");
    if(legacy&&!document.querySelector(".article-related-unified")){
      var items=[].slice.call(legacy.querySelectorAll(".article-new-more-grid>a")).map(function(a){
        var p=(a.querySelector("span")?.textContent||"INSIGHT").trim().split("·");
        return {url:a.href,img:a.querySelector("img")?.getAttribute("src")||"",alt:a.querySelector("img")?.alt||"",category:(p[0]||"INSIGHT").trim(),date:p.slice(1).join("·").trim(),title:(a.querySelector("h3")?.textContent||"").trim()};
      });
      if(items.length){
        var el=document.createElement("section");el.className="article-related-unified";
        var wrap=document.createElement("div");wrap.className="aru-container";
        var head=document.createElement("div");head.className="aru-head";
        head.innerHTML='<h2>Más insights de lowsignal</h2><a href="/recursos/insights">Ver todos los insights ↗</a>';
        wrap.appendChild(head);
        var grid=document.createElement("div");grid.className="aru-grid";
        items.forEach(function(it){
          var card=document.createElement("a");card.className="aru-card";card.href=it.url;
          var fig=document.createElement("figure");var img=document.createElement("img");
          img.src=it.img;img.alt=it.alt;img.loading="lazy";fig.appendChild(img);card.appendChild(fig);
          var meta=document.createElement("div");meta.className="aru-meta";
          var cat=document.createElement("span");cat.textContent=it.category;
          var date=document.createElement("b");date.textContent=it.date;
          meta.append(cat,date);card.appendChild(meta);
          var h=document.createElement("h3");h.textContent=it.title;card.appendChild(h);
          var read=document.createElement("strong");read.textContent="Leer artículo ↗";card.appendChild(read);
          grid.appendChild(card);
        });
        wrap.appendChild(grid);el.appendChild(wrap);legacy.replaceWith(el);
      }
    }
    var links=[].slice.call(document.querySelectorAll(".article-editorial-toc a[href^='#']"));
    var sections=links.map(function(a){return document.getElementById(a.getAttribute("href").slice(1))}).filter(Boolean);
    if("IntersectionObserver" in window&&sections.length){
      var tocObserver=new IntersectionObserver(function(entries){
        entries.forEach(function(e){if(e.isIntersecting)links.forEach(function(a){a.classList.toggle("is-active",a.hash==="#"+e.target.id)})});
      },{rootMargin:"-12% 0px -65% 0px",threshold:0});
      sections.forEach(function(x){tocObserver.observe(x)});
    }
    document.querySelectorAll(".article-editorial-share .article-copy-link").forEach(function(btn){
      if(btn.hasAttribute("onclick")||btn.dataset.copyLink||btn.dataset.copyUrl)return;
      btn.addEventListener("click",function(){if(navigator.clipboard)navigator.clipboard.writeText(location.href).then(function(){btn.textContent="Enlace copiado"})});
    });
    if(!("IntersectionObserver" in window)||window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;
    var targets=[],selectors=[".article-new-content>h2",".article-new-content>.article-new-process",".article-new-content>figure",".article-related-unified .aru-head",".article-related-unified .aru-card"];
    selectors.forEach(function(sel){document.querySelectorAll(sel).forEach(function(el){if(targets.indexOf(el)<0)targets.push(el)})});
    var io=new IntersectionObserver(function(entries,obs){entries.forEach(function(entry){if(entry.isIntersecting){entry.target.classList.add("insight-scroll-reveal-visible");obs.unobserve(entry.target)}})},{threshold:.08,rootMargin:"0px 0px -5% 0px"});
    targets.forEach(function(el){if(el.getBoundingClientRect().top<window.innerHeight)return;el.classList.add("insight-scroll-reveal-pending");io.observe(el)});
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init,{once:true});else init();
})();