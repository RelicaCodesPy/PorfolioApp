import streamlit as st

st.set_page_config(
    page_title="Skills",
    page_icon="💡",
    layout="wide"
)

# LOAD CSS
with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("💡 Skills & Competencies")

st.markdown("""
My skills continue to grow through academic learning,
leadership experiences, competitions, workshops,
hackathons, and personal projects.

As a Computer Science student, I continuously improve
both my technical and creative abilities.
""")

st.divider()

# TABS

tab1, tab2, tab3, tab4 = st.tabs([
    "💻 Programming",
    "🌐 Web Development",
    "🎨 Design",
    "👑 Leadership"
])

# PROGRAMMING

with tab1:

    st.subheader("Programming Languages")

    st.progress(70, text="Python")
    st.progress(65, text="Java")
    st.progress(60, text="C++")
    st.progress(60, text="C")

    st.info("""
Current Level: Basic to Intermediate

I continue improving my programming skills through
coursework, coding exercises, and practical applications.
""")

# WEB

with tab2:

    st.subheader("Web Development")

    st.progress(70, text="HTML")
    st.progress(65, text="CSS")

    st.info("""
I have foundational knowledge in web development
and continue exploring modern web technologies
and user-centered design principles.
""")

# DESIGN

with tab3:

    st.subheader("Graphic Design & Creativity")

    st.progress(95, text="Canva")
    st.progress(90, text="Photo Manipulation")
    st.progress(90, text="Poster Design")
    st.progress(88, text="Digital Illustration")
    st.progress(85, text="UI/UX Design")

    st.success("""
🏆 Multiple Graphic Design Festival (GDF) Awards

🏆 Best in Photo Manipulation

🏆 Best Abstract Art

🏆 Most Popular Graphic Design

🏆 Nitezen's Choice
""")

# LEADERSHIP

with tab4:

    st.subheader("Leadership & Soft Skills")

    st.progress(98, text="Leadership")
    st.progress(95, text="Communication")
    st.progress(95, text="Teamwork")
    st.progress(90, text="Event Management")
    st.progress(90, text="Public Speaking")
    st.progress(95, text="Problem Solving")

st.divider()

# TECH STACK

st.subheader("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
### Programming

- Python
- Java
- C++
- C
""")

with col2:

    st.markdown("""
### Web Technologies

- HTML
- CSS
- Streamlit
""")

with col3:

    st.markdown("""
### Design Tools

- Canva
- Photo Editing Tools
- Digital Art Tools
""")

st.divider()

# INTERACTIVE SELF-ASSESSMENT

st.subheader("📊 Skill Confidence Assessment")

skill = st.selectbox(
    "Choose a Skill",
    [
        "Python",
        "Java",
        "C++",
        "C",
        "HTML",
        "CSS",
        "Graphic Design",
        "Leadership"
    ]
)

confidence = st.slider(
    f"Confidence Level in {skill}",
    0,
    100,
    80
)

st.success(
    f"Confidence Level in {skill}: {confidence}%"
)

st.divider()

# LEARNING JOURNEY

st.subheader("🚀 Currently Learning")

st.markdown("""
- Advanced Python Programming
- Web Application Development
- Cybersecurity Concepts
- UI/UX Design Principles
- Artificial Intelligence Fundamentals
- Software Development Best Practices
""")

st.divider()

# CAREER INTERESTS

st.subheader("🎯 Career Interests")

interests = st.multiselect(
    "Select Career Areas",
    [
        "Software Development",
        "Web Development",
        "Cybersecurity",
        "Artificial Intelligence",
        "Graphic Design",
        "UI/UX Design",
        "Project Management"
    ]
)

if interests:
    st.info(
        f"Selected Interests: {', '.join(interests)}"
    )

st.divider()

# SUMMARY

st.markdown("""
<div class='card'>

<h3>🌟 Skills Summary</h3>

I combine technical knowledge, creativity,
and leadership to continuously improve
as a future technology professional.

My strengths include programming fundamentals,
graphic design, communication, teamwork,
and student leadership.

</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class='footer'>

Learning never stops. Every project,
competition, and leadership experience
is an opportunity for growth.

</div>
""", unsafe_allow_html=True)
