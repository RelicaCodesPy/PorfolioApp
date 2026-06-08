import streamlit as st

st.set_page_config(
    page_title="Relica Malinao Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# ======================
# LOAD CSS
# ======================
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================
# HERO SECTION (IMPROVED)
# ======================
col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("assets/profile.png", width=220)
    except:
        st.info("📷 Add your profile image in assets/profile.png")

with col2:
    st.markdown("""
    <div class='hero-card'>

        <h1>👩‍💻 Relica Malinao</h1>

        <h3>3rd Year Bachelor of Science in Computer Science</h3>

        <p>
        Aspiring Software Developer • Graphic Artist • Student Leader
        </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")

# ======================
# STATS (UPGRADED TO CARDS)
# ======================
st.markdown("<h2 class='section-title'>📊 Achievements Overview</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='stat-card'>
        <h2>20+</h2>
        <p>Academic Awards</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='stat-card'>
        <h2>8</h2>
        <p>Leadership Roles</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='stat-card'>
        <h2>15+</h2>
        <p>Design Awards</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='stat-card'>
        <h2>10+</h2>
        <p>Hackathons</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ======================
# ABOUT SECTION
# ======================
st.markdown("<h2 class='section-title'>🌟 About Me</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='project-card'>

I am <b>Relica Malinao</b>, a passionate Computer Science student at  
<b>DEBESMSCAT</b>.

<br><br>

My journey combines <b>technology, leadership, creativity, graphic design,</b>  
and <b>community service</b>.

<br><br>

I continuously develop my skills in programming, cybersecurity,  
web development, and digital arts while serving as a student leader.

</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# HIGHLIGHTS
# ======================
st.markdown("<h2 class='section-title'>🏆 Featured Highlights</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='stat-card'>
        <h3>🎓 Dean's Lister</h3>
        <p>A.Y. 2024–2025<br>A.Y. 2025–2026</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='stat-card'>
        <h3>👑 President</h3>
        <p>DISCSS<br>A.Y. 2025–2026</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='stat-card'>
        <h3>🎨 Graphic Design</h3>
        <p>Festival Awardee<br>GDF 2024</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ======================
# SKILLS SECTION
# ======================
st.markdown("<h2 class='section-title'>💡 Technical Skills</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Programming")
    st.progress(70, text="Python")
    st.progress(65, text="Java")
    st.progress(60, text="C++")
    st.progress(60, text="C")

with col2:
    st.markdown("### Web & Design")
    st.progress(70, text="HTML")
    st.progress(65, text="CSS")
    st.progress(85, text="Canva")
    st.progress(80, text="Graphic Design")

st.divider()

# ======================
# PORTFOLIO PREVIEW
# ======================
st.markdown("<h2 class='section-title'>🎨 Creative Portfolio</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='project-card'>

Explore my Graphic Arts Projects page to view my award-winning digital artworks,  
environmental advocacy posters, and creative design works.

</div>
""", unsafe_allow_html=True)

st.info("📌 Use the sidebar to explore Projects, Skills, Achievements, Leadership, and Contact pages.")

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
© 2026 Relica Malinao • Computer Science Student • Graphic Artist • Student Leader
</div>
""", unsafe_allow_html=True)
