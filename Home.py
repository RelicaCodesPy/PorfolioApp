import streamlit as st

st.set_page_config(
    page_title="Relica Malinao Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# LOAD CSS
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================
# HERO SECTION WITH PROFILE
# ======================
col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("assets/profile.png", width=220)
    except:
        st.info("📷 Add your profile image in assets/profile.png")

with col2:
    st.markdown("""
    <div class='hero'>

    <h1>👩‍💻 Relica Malinao</h1>

    <h3>3rd Year Bachelor of Science in Computer Science</h3>

    <p>
    Aspiring Software Developer • Graphic Artist • Student Leader
    </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")

# ======================
# STATS
# ======================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Academic Awards", "20+")

with col2:
    st.metric("Leadership Roles", "8")

with col3:
    st.metric("Graphic Design Awards", "15+")

with col4:
    st.metric("Hackathons", "10+")

st.divider()

# ======================
# ABOUT PREVIEW
# ======================
st.markdown("<h2 class='section-title'>🌟 About Me</h2>", unsafe_allow_html=True)

st.write("""
I am Relica Malinao, a passionate Computer Science student at
Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture
and Technology (DEBESMSCAT).

My journey combines technology, leadership, creativity,
graphic design, and community service.

I continuously develop my knowledge in programming,
cybersecurity, web development, and digital arts while
serving as a student leader and community advocate.
""")

st.divider()

# ======================
# HIGHLIGHTS
# ======================
st.markdown("<h2 class='section-title'>🏆 Featured Highlights</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
🎓 Dean's Lister  
A.Y. 2024-2025  
A.Y. 2025-2026
""")

with col2:
    st.success("""
👑 President  
DISCSS  
A.Y. 2025-2026
""")

with col3:
    st.success("""
🎨 Graphic Design  
Festival Awardee  
GDF 2024
""")

st.divider()

# ======================
# SKILLS
# ======================
st.markdown("<h2 class='section-title'>💡 Current Technical Skills</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("Programming")
    st.progress(70, text="Python")
    st.progress(65, text="Java")
    st.progress(60, text="C++")
    st.progress(60, text="C")

with col2:
    st.write("Web Development")
    st.progress(70, text="HTML")
    st.progress(65, text="CSS")
    st.progress(85, text="Canva")
    st.progress(80, text="Graphic Design")

st.divider()

# ======================
# PORTFOLIO PREVIEW
# ======================
st.markdown("<h2 class='section-title'>🎨 Creative Portfolio</h2>", unsafe_allow_html=True)

st.write("""
Explore my Graphic Arts Projects page to view my
award-winning digital artworks, environmental advocacy
posters, digital illustrations, and graphic design works.
""")

st.info("📌 Use the sidebar to explore Education, Skills, Projects, Achievements, Leadership, and Contact pages.")

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
© 2026 Relica Malinao  
Computer Science Student • Graphic Artist • Student Leader
</div>
""", unsafe_allow_html=True)
