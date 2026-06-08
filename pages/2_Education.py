import streamlit as st

st.set_page_config(
    page_title="Education",
    page_icon="🎓",
    layout="wide"
)

# LOAD CSS
with open("styles/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# HEADER

st.title("🎓 Educational Journey")

st.markdown("""
My educational journey reflects years of dedication, perseverance,
and continuous growth. From elementary school to pursuing a degree
in Computer Science, each stage has contributed to my academic,
personal, and leadership development.
""")

st.divider()

# TIMELINE

st.subheader("📚 Academic Timeline")

education_data = [
    {
        "year": "2023 - Present",
        "school": "Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (DEBESMSCAT)",
        "level": "Bachelor of Science in Computer Science"
    },
    {
        "year": "2022 - 2023",
        "school": "Federico A. Estipona Memorial High School",
        "level": "Grade 12 - STEM"
    },
    {
        "year": "2021 - 2022",
        "school": "PHINMA Rizal College of Laguna",
        "level": "Grade 11 - STEM"
    },
    {
        "year": "2020 - 2021",
        "school": "Eduardo Barretto Sr. National High School",
        "level": "Grade 10"
    },
    {
        "year": "2019 - 2020",
        "school": "Centro De Naic National High School",
        "level": "Grade 9"
    },
    {
        "year": "2017 - 2019",
        "school": "Bucal National High School",
        "level": "Grades 7-8"
    },
    {
        "year": "2011 - 2017",
        "school": "Guincaiptan Elementary School",
        "level": "Grades 1-6"
    }
]

for item in education_data:

    with st.expander(
        f"📅 {item['year']} | {item['school']}"
    ):

        st.write(
            f"**Program / Level:** {item['level']}"
        )

st.divider()

# EDUCATION SUMMARY

st.subheader("📈 Academic Progress")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Schools Attended",
        "7"
    )

with col2:
    st.metric(
        "Current Program",
        "BSCS"
    )

with col3:
    st.metric(
        "Current Year",
        "3rd Year"
    )

st.divider()

# INTERACTIVE SECTION

st.subheader("🔍 Explore My Educational Stages")

stage = st.selectbox(
    "Select a Stage",
    [
        "Elementary",
        "Junior High School",
        "Senior High School",
        "College"
    ]
)

if stage == "Elementary":

    st.success("""
🏫 Guincaiptan Elementary School

📅 2011 – 2017

This stage laid the foundation for my academic journey.
I consistently earned honors and developed my passion
for learning.
""")

elif stage == "Junior High School":

    st.success("""
🏫 Bucal National High School

🏫 Centro De Naic National High School

🏫 Eduardo Barretto Sr. National High School

📅 2017 – 2021

During these years, I continued achieving academic excellence
and participated in competitions including the Math Quiz Bee.
""")

elif stage == "Senior High School":

    st.success("""
🏫 PHINMA Rizal College of Laguna

🏫 Federico A. Estipona Memorial High School

📅 2021 – 2023

I pursued the STEM strand, strengthening my analytical,
scientific, and technological skills while graduating
with honors.
""")

else:

    st.success("""
🏫 Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology

📅 2023 – Present

Currently pursuing a Bachelor of Science in Computer Science.

Highlights:

🎓 Dean's Lister

🎓 Vice President's Lister

💻 Hackathon Participant

🎨 Graphic Design Festival Awardee

👑 DISCSS President
""")

st.divider()

# FAVORITE SUBJECTS

st.subheader("📖 Academic Interests")

subjects = st.multiselect(
    "Select Academic Areas",
    [
        "Programming",
        "Web Development",
        "Cybersecurity",
        "Artificial Intelligence",
        "Graphic Design",
        "Leadership"
    ]
)

if subjects:

    st.info(
        f"You selected: {', '.join(subjects)}"
    )

st.divider()

st.markdown("""
<div class='footer'>

Education is the foundation of lifelong learning and growth.

</div>
""", unsafe_allow_html=True)
