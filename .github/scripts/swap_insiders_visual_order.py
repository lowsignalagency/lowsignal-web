from pathlib import Path

p=Path('recursos/insiders.html')
s=p.read_text(encoding='utf-8')

joaquin='''        <article class="ins-v2-person-card">
          <div class="ins-v2-person-photo">
            <img src="https://lowsignal.cl/assets/joaquin.png" alt="Joaquín, Growth Ambassador de lowsignal" loading="lazy">
            <span>INSIDER / 02</span>
          </div>
          <div class="ins-v2-person-meta">
            <div><h3>Joaquín</h3><p>Growth Ambassador</p></div>
            <b>lowsignal insiders</b>
          </div>
        </article>

'''

samuel='''        <article class="ins-v2-person-card">
          <div class="ins-v2-person-photo">
            <img src="https://lowsignal.cl/assets/samuel.png" alt="Samuel, Growth Ambassador de lowsignal" loading="lazy">
            <span>INSIDER / 01</span>
          </div>
          <div class="ins-v2-person-meta">
            <div><h3>Samuel</h3><p>Growth Ambassador</p></div>
            <b>lowsignal insiders</b>
          </div>
        </article>

'''

old=joaquin+samuel
new=samuel+joaquin
if old not in s:
    raise SystemExit('Expected Joaquin/Samuel order not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Samuel first, Joaquin second')
