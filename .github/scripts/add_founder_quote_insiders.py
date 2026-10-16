from pathlib import Path
p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')

css_anchor='''@media(max-width:480px){\n  .ins-v2-people-grid{grid-template-columns:1fr}\n  .ins-v2-person-photo{aspect-ratio:1 / 1.08}\n  .ins-v2-person-join{grid-column:auto}\n}\n'''
css_insert='''@media(max-width:480px){\n  .ins-v2-people-grid{grid-template-columns:1fr}\n  .ins-v2-person-photo{aspect-ratio:1 / 1.08}\n  .ins-v2-person-join{grid-column:auto}\n}\n\n.ins-v2-founder-quote{\n  margin-top:54px;\n  padding-top:30px;\n  border-top:1px solid #DCE3F2;\n  max-width:860px;\n}\n.ins-v2-founder-quote blockquote{\n  margin:0;\n  max-width:820px;\n  color:#10193C;\n  font-size:clamp(26px,3vw,40px);\n  line-height:1.18;\n  letter-spacing:-.035em;\n  font-weight:300;\n}\n.ins-v2-founder-quote blockquote strong{\n  color:#1419E0;\n  font-weight:300;\n}\n.ins-v2-founder-signature{\n  margin-top:24px;\n  display:flex;\n  align-items:center;\n  gap:12px;\n}\n.ins-v2-founder-signature:before{\n  content:\"\";\n  width:28px;\n  height:1px;\n  background:#1419E0;\n  flex:0 0 auto;\n}\n.ins-v2-founder-signature div{display:flex;flex-direction:column;gap:3px}\n.ins-v2-founder-signature b{color:#10182A;font-size:12px;font-weight:600}\n.ins-v2-founder-signature span{color:#7A86A7;font-size:10px}\n@media(max-width:760px){\n  .ins-v2-founder-quote{margin-top:42px;padding-top:24px}\n  .ins-v2-founder-quote blockquote{font-size:26px;line-height:1.2}\n}\n'''
if css_anchor not in s:
    raise SystemExit('CSS anchor not found')
s=s.replace(css_anchor,css_insert,1)

html_anchor='''      </div>\n    </div>\n  </section>'''
quote='''      </div>\n\n      <div class="ins-v2-founder-quote">\n        <blockquote>“Creemos en el <strong>talento joven</strong>, en las buenas conexiones y en la gente que mueve oportunidades.”</blockquote>\n        <div class="ins-v2-founder-signature">\n          <div>\n            <b>Felipe Quiroz</b>\n            <span>Co-Founder & COO, lowsignal</span>\n          </div>\n        </div>\n      </div>\n    </div>\n  </section>'''
# target the people section by using the first closing after the people grid block marker
marker='<section class="ins-v2-people"'
start=s.find(marker)
if start==-1:
    raise SystemExit('People section not found')
pos=s.find(html_anchor,start)
if pos==-1:
    raise SystemExit('People section closing anchor not found')
s=s[:pos]+s[pos:].replace(html_anchor,quote,1)

p.write_text(s,encoding='utf-8')
print('Added founder quote to Insiders section')
