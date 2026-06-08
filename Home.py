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
# HERO SECTION
# ======================
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image("assets/profile.png", width=220)

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

st.divider()

# ======================
# METRICS (RESPONSIVE GRID)
# ======================
col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("Academic Awards", "20+"),
    ("Leadership Roles", "8"),
    ("Graphic Design Awards", "15+"),
    ("Hackathons", "10+")
]

for col, (label, value) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.metric(label, value)
        st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# ABOUT SECTION
# ======================
st.markdown("<h2 class='section-title'>🌟 About Me</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
I am Relica Malinao, a passionate Computer Science student at
Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture
and Technology (DEBESMSCAT).

My journey combines technology, leadership, creativity,
graphic design, and community service.

I continuously develop my knowledge in programming,
cybersecurity, web development, and digital arts while
serving as a student leader and community advocate.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# HIGHLIGHTS
# ======================
st.markdown("<h2 class='section-title'>🏆 Featured Highlights</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
🎓 Dean's Lister  
A.Y. 2024-2025  
A.Y. 2025-2026
""")

with c2:
    st.success("""
👑 President  
DISCSS  
A.Y. 2025-2026
""")

with c3:
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
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Programming")
    st.progress(70, text="Python")
    st.progress(65, text="Java")
    st.progress(60, text="C++")
    st.progress(60, text="C")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Web Development")
    st.progress(70, text="HTML")
    st.progress(65, text="CSS")
    st.progress(85, text="Canva")
    st.progress(80, text="Graphic Design")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
© 2026 Relica Malinao • Computer Science Student • Graphic Artist • Student Leader
</div>
""", unsafe_allow_html=True)
