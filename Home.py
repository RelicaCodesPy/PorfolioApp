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
# HERO SECTION (BLUE–VIOLET FOCUS)
# ======================
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    st.image("assets/profile.png", width=230)

with col2:
    st.markdown("""
    <div class="hero-card">

        <h1>👩‍💻 Relica Malinao</h1>

        <h3 style="color: #dbeafe;">
            Computer Science Student • Graphic Artist • Student Leader
        </h3>

        <p style="color: #e0e7ff;">
            Passionate developer building modern systems, creative designs,
            and innovative digital solutions using technology.
        </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ======================
# ACHIEVEMENTS (BLUE–VIOLET EMPHASIS)
# ======================
st.markdown("## 📊 Achievements Overview")

col1, col2, col3, col4 = st.columns(4)

col1.markdown("""
<div class="stat-card">
    <h2 style="color:#0ea5e9;">20+</h2>
    <p>Academic Awards</p>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class="stat-card">
    <h2 style="color:#6366f1;">8</h2>
    <p>Leadership Roles</p>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class="stat-card">
    <h2 style="color:#0ea5e9;">15+</h2>
    <p>Design Awards</p>
</div>
""", unsafe_allow_html=True)

col4.markdown("""
<div class="stat-card">
    <h2 style="color:#6366f1;">10+</h2>
    <p>Hackathons</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ======================
# ABOUT SECTION
# ======================
st.markdown("## 🌟 About Me")

st.markdown("""
<div class="project-card">

<p style="font-size:16px; line-height:1.8; color:#1e1b4b;">
I am <b style="color:#0ea5e9;">Relica Malinao</b>, a Computer Science student at <b>DEBESMSCAT</b>.
</p>

<p style="font-size:16px; line-height:1.8; color:#334155;">
I specialize in <b style="color:#6366f1;">software development</b>,
<b style="color:#0ea5e9;">graphic design</b>, and <b>leadership</b>.
</p>

<p style="font-size:16px; line-height:1.8; color:#334155;">
I enjoy building modern systems, designing creative visuals,
and solving real-world problems using technology.
</p>

</div>
""", unsafe_allow_html=True)

# ======================
# HIGHLIGHTS (COLOR BALANCED)
# ======================
st.markdown("## 🏆 Featured Highlights")

col1, col2, col3 = st.columns(3)

col1.markdown("""
<div class="stat-card">
<h3 style="color:#0ea5e9;">🎓 Dean's Lister</h3>
<p>A.Y. 2024–2025<br>A.Y. 2025–2026</p>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class="stat-card">
<h3 style="color:#6366f1;">👑 President</h3>
<p>DISCSS Organization<br>A.Y. 2025–2026</p>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class="stat-card">
<h3 style="color:#0ea5e9;">🎨 Graphic Design</h3>
<p>Festival Awardee<br>GDF 2024</p>
</div>
""", unsafe_allow_html=True)

# ======================
# SKILLS SECTION (BLUE & VIOLET SPLIT)
# ======================
st.markdown("## 💡 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔵 Programming Skills")
    st.progress(70, text="Python")
    st.progress(65, text="Java")
    st.progress(60, text="C++")
    st.progress(60, text="C")

with col2:
    st.markdown("### 🟣 Design & Web Skills")
    st.progress(70, text="HTML")
    st.progress(65, text="CSS")
    st.progress(85, text="Canva")
    st.progress(80, text="Graphic Design")

# ======================
# FOOTER
# ======================
st.markdown("""
<br><br>
<div class="footer">
© 2026 Relica Malinao • Blue & Violet Elite Portfolio
</div>
""", unsafe_allow_html=True)
