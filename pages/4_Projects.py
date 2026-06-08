import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="🎨",
    layout="wide"
)

# ======================
# LOAD CSS
# ======================
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown("""
<div class="hero-card">

<h1 style="color:#0ea5e9;">🎨 Graphic Arts Projects</h1>

<p style="color:#e0e7ff; font-size:16px;">
Role: <b>Graphic Artist</b><br><br>
A curated collection of creative works showcasing digital illustration,
poster design, environmental advocacy, typography, and visual storytelling.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ======================
# FILTER (UI ONLY IMPROVED LOOK)
# ======================
category = st.selectbox(
    "Filter Projects",
    [
        "All",
        "Digital Illustration",
        "Advocacy Poster",
        "Typography",
        "Photo Manipulation",
        "Abstract Art"
    ]
)

st.markdown("<br>", unsafe_allow_html=True)

# ======================
# PROJECT CARD FUNCTION STYLE
# ======================
def project(title, image, category_text, description, skills):
    st.markdown(f"""
    <div class="project-card">

        <h3 style="color:#0ea5e9;">{title}</h3>

        <p style="color:#6366f1;"><b>Category:</b> {category_text}</p>

        <img src="{image}" style="width:100%; border-radius:12px; margin:10px 0;">

        <p style="color:#334155; line-height:1.6;">
        {description}
        </p>

        <p style="color:#1e1b4b;"><b>Skills:</b> {skills}</p>

    </div>
    """, unsafe_allow_html=True)

# ======================
# PROJECTS (ELITE CARDS)
# ======================

project(
    "🧚 Enchanted Whispers",
    "assets/artwork7.jpg",
    "Digital Illustration",
    "A fantasy-inspired artwork portraying a fairy surrounded by butterflies and floral elements.",
    "Illustration • Composition • Color Harmony"
)

project(
    "❤️ One Chance",
    "assets/artwork6.jpg",
    "Typography Poster",
    "A motivational typography poster emphasizing the importance of opportunities.",
    "Typography • Layout • Visual Communication"
)

project(
    "🌍 A Fading World: Our Last Chance",
    "assets/artwork5.jpg",
    "Environmental Advocacy",
    "An awareness poster about climate change and environmental responsibility.",
    "Photo Manipulation • Advocacy Design"
)

project(
    "🌲 Trees for the Future",
    "assets/artwork4.jpg",
    "Environmental Design",
    "A conservation-themed artwork promoting reforestation and sustainability.",
    "Poster Design • Visual Messaging"
)

project(
    "🎨 Fragments of Imagination",
    "assets/artwork3.jpg",
    "Abstract Art",
    "An abstract piece expressing creativity through color and form.",
    "Abstract Design • Creative Visualization"
)

project(
    "🌌 Beyond Reality",
    "assets/artwork2.jpg",
    "Photo Manipulation",
    "A surreal double exposure artwork blending identity and nature.",
    "Photo Manipulation • Digital Compositing"
)

project(
    "🌸 Neon Serenity",
    "assets/artwork1.jpg",
    "Digital Illustration",
    "An anime-inspired illustration with vibrant expressive colors.",
    "Illustration • Color Theory"
)

# ======================
# STATS SECTION
# ======================
st.markdown("## 📊 Portfolio Highlights")

col1, col2, col3, col4 = st.columns(4)

col1.markdown("<div class='stat-card'><h2 style='color:#0ea5e9;'>7</h2><p>Artworks</p></div>", unsafe_allow_html=True)
col2.markdown("<div class='stat-card'><h2 style='color:#6366f1;'>Graphic Artist</h2><p>Role</p></div>", unsafe_allow_html=True)
col3.markdown("<div class='stat-card'><h2 style='color:#0ea5e9;'>10+</h2><p>Awards</p></div>", unsafe_allow_html=True)
col4.markdown("<div class='stat-card'><h2 style='color:#6366f1;'>GDF</h2><p>Recognition</p></div>", unsafe_allow_html=True)

# ======================
# ACHIEVEMENTS
# ======================
st.markdown("## 🏆 Graphic Design Achievements")

st.markdown("""
<div class="project-card">

🎨 <b>Graphic Design Festival (GDF 2024)</b>

<br><br>

• 1st Runner Up<br>
• Rank 2 – Art Exhibit<br>
• Rank 2 – Semi Finals<br>
• Best in Photo Manipulation<br>
• Best Abstract Art<br>
• Best One Color Shade Art<br>
• Most Popular Graphic Design<br>
• Netizen's Choice<br>
• Top Speed Art Performer<br>
• Finalist – Fixing a Broken Art Challenge

</div>
""", unsafe_allow_html=True)

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
Creativity is the bridge between imagination and impact.
</div>
""", unsafe_allow_html=True)
