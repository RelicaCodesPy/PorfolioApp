import streamlit as st

st.markdown("""
<style>
.contact-section {
    margin-top: 20px;
}

.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 18px;
}

.contact-card {
    background: #ffffff;
    padding: 22px;
    border-radius: 18px;

    border: 1px solid rgba(99, 102, 241, 0.15);
    box-shadow: 0 10px 25px rgba(99, 102, 241, 0.10);

    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
}

.contact-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 18px 40px rgba(99, 102, 241, 0.18);
}

.contact-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    width: 100%;
    background: linear-gradient(90deg, #0ea5e9, #6366f1);
}

.contact-card h3 {
    color: #1e1b4b;
    margin-bottom: 8px;
}

.contact-card p {
    color: #475569;
    font-size: 0.95rem;
}

.contact-card a {
    text-decoration: none;
    color: #0ea5e9;
    font-weight: 500;
}

.contact-card a:hover {
    color: #6366f1;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("## 📱 Contact Information")

# GRID CONTAINER
st.markdown('<div class="contact-section">', unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)
