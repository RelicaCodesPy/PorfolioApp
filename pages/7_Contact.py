import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

# =========================
# CSS THEME (Blue • Violet • White)
# =========================
st.markdown("""
<style>

.main {
    background-color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
    color: #0f172a;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Section Title */
.section-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #1e1b4b;
    margin-bottom: 1rem;
    position: relative;
}

.section-title::after {
    content: "";
    width: 70px;
    height: 3px;
    background: linear-gradient(90deg, #0ea5e9, #6366f1);
    position: absolute;
    left: 0;
    bottom: -6px;
    border-radius: 10px;
}

/* Contact Card */
.contact-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(99, 102, 241, 0.15);
    box-shadow: 0 10px 25px rgba(99, 102, 241, 0.10);
    transition: 0.25s ease;
    height: 100%;
}

.contact-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(99, 102, 241, 0.18);
}

.contact-card h3 {
    color: #1e1b4b;
    margin-bottom: 8px;
}

.contact-card p, .contact-card a {
    color: #475569;
    text-decoration: none;
}

/* Button Styling */
.stButton > button {
    background: linear-gradient(135deg, #0ea5e9, #6366f1);
    color: white !important;
    border-radius: 12px;
    padding: 10px 18px;
    border: none;
    font-weight: 600;
    box-shadow: 0 10px 25px rgba(99, 102, 241, 0.25);
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 15px 35px rgba(99, 102, 241, 0.35);
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown('<div class="section-title">📱 Contact Information</div>', unsafe_allow_html=True)

# =========================
# CONTACT INFO CARDS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="contact-card">
        <h3>📧 Email</h3>
        <p><a href="mailto:relicacodespy@gmail.com">relicacodespy@gmail.com</a></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-card">
        <h3>📘 Facebook</h3>
        <p><a href="https://facebook.com/codespyrelica" target="_blank">
        facebook.com/codespyrelica</a></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="contact-card">
        <h3>💻 GitHub</h3>
        <p><a href="https://github.com/RelicaCodesPy" target="_blank">
        github.com/RelicaCodesPy</a></p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# CONTACT FORM
# =========================
st.markdown("## ✉️ Send Me a Message")

with st.form("contact_form"):

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")

    submitted = st.form_submit_button("🚀 Send Message")

    if submitted:
        if name and email and message:
            st.success("✅ Message sent successfully!")
            st.info("📨 Your message preview:")

            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Subject:** {subject}")
            st.write(f"**Message:** {message}")

        else:
            st.error("❌ Please fill in all required fields")

# =========================
# FOOTER
# =========================
st.markdown("""
<hr>
<div style='text-align:center; color:#64748b;'>
    © 2026 Relica Portfolio | Built with Streamlit 🚀
</div>
""", unsafe_allow_html=True)
