import streamlit as st

st.set_page_config(
    page_title="Contact",
    page_icon="📬",
    layout="wide"
)

# ======================
# LOAD CSS
# ======================
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown("""
<div class="header">
    <h1>📬 Contact Me</h1>
    <p>Let’s connect, collaborate, and build something meaningful.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# CONTACT CARDS
# ======================
st.subheader("📱 Contact Information")

col1, col2, col3 = st.columns(3)

card_style = """
<div style="
    padding:20px;
    border-radius:15px;
    background:#0f172a;
    color:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.2);
    text-align:center;
">
"""

with col1:
    st.markdown(card_style + """
        <h3>📧 Email</h3>
        <p>relicacodespy@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(card_style + """
        <h3>📘 Facebook</h3>
        <p>facebook.com/codespyrelica</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(card_style + """
        <h3>💻 GitHub</h3>
        <p>github.com/RelicaCodesPy</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ======================
# PROFILE
# ======================
st.subheader("👩‍💻 Professional Profile")

st.info("""
🎓 3rd Year Bachelor of Science in Computer Science  
🏫 Dr. Emilio B. Espinosa Sr. Memorial State College  
💻 Aspiring Software Developer  
🎨 Graphic Artist  
👑 Student Leader  
🔐 Cybersecurity Enthusiast  
""")

st.divider()

# ======================
# CONTACT FORM (MODERN)
# ======================
st.subheader("✉ Send a Message")

with st.form("contact_form", clear_on_submit=True):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email Address")

    with col2:
        subject = st.text_input("📌 Subject")

    message = st.text_area("💬 Message", height=150)

    submit = st.form_submit_button("🚀 Send Message")

    if submit:
        if name and email and message:
            st.success("✅ Message sent successfully! I’ll get back to you soon.")

        else:
            st.error("⚠ Please fill in all required fields.")

st.divider()

# ======================
# COLLABORATION AREAS
# ======================
st.subheader("🤝 Areas Open for Collaboration")

st.markdown("""
- 💻 Software Development  
- 🌐 Web Development  
- 🎨 Graphic Design  
- 🧠 UI/UX Design  
- 🔐 Cybersecurity  
- 👑 Leadership Projects  
- 🤝 Community Service  
- 📚 Academic Research  
""")

st.divider()

# ======================
# SOCIAL LINKS
# ======================
st.subheader("🌐 Connect Online")

st.markdown("""
🔗 Facebook: facebook.com/codespyrelica 
💻 GitHub: github.com/RelicaCodesPy  
📧 Email: relicacodespy@gmail.com  
""")

st.divider()

# ======================
# QUICK STATS
# ======================
st.subheader("📊 Quick Facts")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Year Level", "3rd")
c2.metric("Leadership Roles", "8")
c3.metric("Design Projects", "10+")
c4.metric("Hackathons", "5+")

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class="footer">
    © 2026 Relica Malinao • Built with Streamlit • Portfolio Contact Page
</div>
""", unsafe_allow_html=True)
