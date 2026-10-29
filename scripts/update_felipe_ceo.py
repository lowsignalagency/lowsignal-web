from pathlib import Path

# Felipe profile page
profile_path = Path("equipo/felipe-quiroz.html")
profile = profile_path.read_text(encoding="utf-8")
profile = profile.replace(
    "<title>Felipe Quiroz | Co-Founder & COO | lowsignal</title>",
    "<title>Felipe Quiroz | Co-Founder & CEO | lowsignal</title>",
)
profile = profile.replace(
    '<p class="fq-editorial-role">Co-Founder &amp; COO, lowsignal</p>',
    '<p class="fq-editorial-role">Co-Founder &amp; CEO, lowsignal</p>',
)
profile = profile.replace(
    '<p class="fq-editorial-bio">Felipe cofundó lowsignal, donde lidera operaciones, estrategia comercial, client delivery y el desarrollo de productos y sistemas internos de growth. Antes fue Head of Partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, una startup GovTech y SaaS basada en Estados Unidos, con presencia en 7+ mercados de Latinoamérica, Estados Unidos y Europa. Luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, una compañía B2B SaaS de Workforce Management con 10.000+ clientes en 40+ países. Su experiencia conecta negocio, producto, tecnología y growth.</p>',
    '<p class="fq-editorial-bio">Felipe cofundó lowsignal, donde lidera la estrategia de la compañía, crecimiento, desarrollo comercial y evolución de sus productos y sistemas internos. Antes fue Head of Partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, una startup GovTech y SaaS basada en Estados Unidos, con presencia en 7+ mercados de Latinoamérica, Estados Unidos y Europa. Luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, una compañía B2B SaaS de Workforce Management con 10.000+ clientes en 40+ países. Su experiencia conecta negocio, producto, tecnología y growth, con foco en construir y escalar compañías, productos y sistemas de crecimiento.</p>',
)
profile_path.write_text(profile, encoding="utf-8")

# Nosotros page: visible team card + JS profile data
about_path = Path("nosotros.html")
about = about_path.read_text(encoding="utf-8")
about = about.replace("Co-Founder & COO", "Co-Founder & CEO")
about = about.replace("Co-Founder &amp; COO", "Co-Founder &amp; CEO")
about_path.write_text(about, encoding="utf-8")

# Jobs page: JS profile data
jobs_path = Path("recursos/jobs.html")
jobs = jobs_path.read_text(encoding="utf-8")
jobs = jobs.replace("Co-Founder & COO", "Co-Founder & CEO")
jobs = jobs.replace("Co-Founder &amp; COO", "Co-Founder &amp; CEO")
jobs_path.write_text(jobs, encoding="utf-8")

# Growth Ambassador page: visible selection copy + JS profile data
growth_ambassador_path = Path("recursos/jobs/growth-ambassador.html")
growth_ambassador = growth_ambassador_path.read_text(encoding="utf-8")
growth_ambassador = growth_ambassador.replace("Co-Founder & COO", "Co-Founder & CEO")
growth_ambassador = growth_ambassador.replace("Co-Founder &amp; COO", "Co-Founder &amp; CEO")
old_marker = "<!-- felipe-role-publish-marker: 2026-10-29-2 -->"
new_marker = "<!-- felipe-role-publish-marker: 2026-10-29-3 -->"
if old_marker in growth_ambassador:
    growth_ambassador = growth_ambassador.replace(old_marker, new_marker, 1)
elif new_marker not in growth_ambassador:
    growth_ambassador = growth_ambassador.replace("</body>", f"  {new_marker}\n</body>", 1)
growth_ambassador_path.write_text(growth_ambassador, encoding="utf-8")

print("Felipe CEO role is consistent across profile, Nosotros, Jobs and Growth Ambassador, including HTML-escaped visible copy")
