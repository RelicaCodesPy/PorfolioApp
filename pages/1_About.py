import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon="👩‍💻",
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
st.title("👩‍💻 About Me")

st.markdown("""
<div class='card'>
<h3>Hello, I'm Relica Malinao!</h3>

A passionate <b>3rd Year Bachelor of Science in Computer Science student</b>
at <b>DEBESMSCAT</b>.

I am dedicated to continuously improving my knowledge in technology,
graphic design, cybersecurity, and leadership.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# PROFILE SECTION
# ======================
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image("assets/profile.png", use_container_width=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📌 Professional Profile")

    st.write("""
I am a Computer Science student who enjoys combining technology,
creativity, and leadership.

My academic journey includes:
• Software Development  
• Web Development  
• Graphic Design  
• Cybersecurity  
• Artificial Intelligence  
• Student Leadership  

Through competitions, hackathons, and leadership experiences,
I continue to grow both technically and personally.
""")

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# CAREER GOALS
# ======================
st.markdown("<h2 class='section-title'>🎯 Career Goals</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
My goal is to become a skilled technology professional capable of creating
innovative solutions that positively impact communities and organizations.

I aspire to strengthen my expertise in software development, web technologies,
cybersecurity, and digital design while maintaining leadership and lifelong learning.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# INTERACTIVE SECTION
# ======================
st.markdown("<h2 class='section-title'>💡 Areas of Interest</h2>", unsafe_allow_html=True)

interest = st.selectbox(
    "Select an area you would like to know about:",
    [
        "Software Development",
        "Web Development",
        "Graphic Design",
        "Cybersecurity",
        "Leadership"
    ]
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if interest == "Software Development":
    st.info("I enjoy building programs and solving problems using code.")

elif interest == "Web Development":
    st.info("I create responsive and user-friendly web applications.")

elif interest == "Graphic Design":
    st.info("I express creativity through visual storytelling and design.")

elif interest == "Cybersecurity":
    st.info("I explore digital security and protection systems.")

else:
    st.info("Leadership helps me develop communication and teamwork skills.")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# STRENGTHS
# ======================
st.markdown("<h2 class='section-title'>🌟 Personal Strengths</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.success("✔ Leadership")
    st.success("✔ Creativity")
    st.success("✔ Adaptability")
    st.success("✔ Teamwork")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.success("✔ Communication")
    st.success("✔ Problem Solving")
    st.success("✔ Time Management")
    st.success("✔ Continuous Learning")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# QUICK FACTS
# ======================
st.markdown("<h2 class='section-title'>📊 Quick Facts</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Current Year Level", "3rd Year")

with c2:
    st.metric("Leadership Positions", "8")

with c3:
    st.metric("Major Interests", "5")

st.divider()

# ======================
# QUOTE
# ======================
st.markdown("""
<div class='card'>
<h3>💬 Personal Motto</h3>

<blockquote>
"Success is achieved through continuous learning, perseverance,
leadership, and the courage to embrace new opportunities."
</blockquote>
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
Thank you for visiting my portfolio. Let's continue learning, creating, and leading.
</div>
""", unsafe_allow_html=True)
