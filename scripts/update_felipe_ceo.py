from pathlib import Path

path = Path("equipo/felipe-quiroz.html")
text = path.read_text(encoding="utf-8")

replacements = {
    "<title>Felipe Quiroz | Co-Founder & COO | lowsignal</title>":
        "<title>Felipe Quiroz | Co-Founder & CEO | lowsignal</title>",
    '<p class="fq-editorial-role">Co-Founder &amp; COO, lowsignal</p>':
        '<p class="fq-editorial-role">Co-Founder &amp; CEO, lowsignal</p>',
    '<p class="fq-editorial-bio">Felipe cofundó lowsignal, donde lidera operaciones, estrategia comercial, client delivery y el desarrollo de productos y sistemas internos de growth. Antes fue Head of Partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, una startup GovTech y SaaS basada en Estados Unidos, con presencia en 7+ mercados de Latinoamérica, Estados Unidos y Europa. Luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, una compañía B2B SaaS de Workforce Management con 10.000+ clientes en 40+ países. Su experiencia conecta negocio, producto, tecnología y growth.</p>':
        '<p class="fq-editorial-bio">Felipe cofundó lowsignal, donde lidera la estrategia de la compañía, crecimiento, desarrollo comercial y evolución de sus productos y sistemas internos. Antes fue Head of Partnerships en <a href="https://tether.education/" target="_blank" rel="noopener noreferrer">Tether Education</a>, una startup GovTech y SaaS basada en Estados Unidos, con presencia en 7+ mercados de Latinoamérica, Estados Unidos y Europa. Luego se desempeñó como Product Manager en <a href="https://www.geovictoria.com/" target="_blank" rel="noopener noreferrer">GeoVictoria</a>, una compañía B2B SaaS de Workforce Management con 10.000+ clientes en 40+ países. Su experiencia conecta negocio, producto, tecnología y growth, con foco en construir y escalar compañías, productos y sistemas de crecimiento.</p>',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"Expected text not found: {old[:100]}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
print("Updated Felipe profile to Co-Founder & CEO")
