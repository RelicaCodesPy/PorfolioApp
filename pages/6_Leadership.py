import streamlit as st

st.set_page_config(
    page_title="Leadership",
    page_icon="👑",
    layout="wide"
)

# LOAD CSS
with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("👑 Leadership Journey")

st.markdown("""
Leadership has been an important part of my personal and academic growth.
Through various organizations and student leadership positions, I have
developed communication, teamwork, decision-making, and organizational skills.
""")

st.divider()

# OVERVIEW

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Leadership Roles", "8")

with col2:
    st.metric("Organizations", "5")

with col3:
    st.metric("Years of Leadership", "8+")

with col4:
    st.metric("Current Position", "President")

st.divider()

# TIMELINE

st.subheader("📅 Leadership Timeline")

leadership_positions = [

    {
        "year": "2018–2019",
        "position": "Grade 8 Representative",
        "organization": "KABAYANI Club"
    },

    {
        "year": "2022–2023",
        "position": "Grade 12 Representative",
        "organization": "YES-O"
    },

    {
        "year": "2023–2024",
        "position": "Class Vice President",
        "organization": "BSCS 1A"
    },

    {
        "year": "2024–2025",
        "position": "Class President",
        "organization": "BSCS 2A"
    },

    {
        "year": "2024–2025",
        "position": "BSCS 2A Representative",
        "organization": "DISCSS"
    },

    {
        "year": "Present",
        "position": "President",
        "organization": "Guincaiptan Katipunan ng Kabataan"
    },

    {
        "year": "2025–2026",
        "position": "President",
        "organization": "DISCSS"
    },

    {
        "year": "2025–2026",
        "position": "Representative of DISCSS",
        "organization": "CASCSC"
    }
]

for item in leadership_positions:

    with st.expander(
        f"👑 {item['year']} | {item['position']}"
    ):

        st.write(
            f"**Organization:** {item['organization']}"
        )

st.divider()

# CURRENT LEADERSHIP ROLES

st.subheader("🌟 Current Leadership Positions")

col1, col2 = st.columns(2)

with col1:

    st.success("""
👑 President

DISCSS

Academic Year 2025–2026
""")

with col2:

    st.success("""
🏛 Representative of DISCSS

CASCSC

Academic Year 2025–2026
""")

st.divider()

# LEADERSHIP SKILLS

st.subheader("💡 Leadership Skills")

col1, col2 = st.columns(2)

with col1:

    st.progress(98, text="Leadership")
    st.progress(95, text="Communication")
    st.progress(95, text="Teamwork")
    st.progress(92, text="Decision Making")

with col2:

    st.progress(90, text="Conflict Resolution")
    st.progress(93, text="Organization")
    st.progress(90, text="Public Speaking")
    st.progress(95, text="Event Management")

st.divider()

# RESPONSIBILITIES

st.subheader("📋 Key Responsibilities")

role = st.selectbox(
    "Select Leadership Position",
    [
        "DISCSS President",
        "CASCSC Representative",
        "Class President",
        "Katipunan ng Kabataan President"
    ]
)

if role == "DISCSS President":

    st.info("""
• Lead the organization and oversee operations

• Represent Computer Science students

• Coordinate programs and activities

• Promote student engagement and development

• Collaborate with college organizations
""")

elif role == "CASCSC Representative":

    st.info("""
• Represent DISCSS in council meetings

• Communicate student concerns

• Participate in planning activities

• Strengthen collaboration among organizations
""")

elif role == "Class President":

    st.info("""
• Lead class activities

• Coordinate with faculty members

• Represent classmates

• Promote teamwork and academic excellence
""")

else:

    st.info("""
• Lead youth-centered community programs

• Organize outreach and development activities

• Promote youth participation

• Strengthen community engagement
""")

st.divider()

# LEADERSHIP PHILOSOPHY

st.subheader("🎯 Leadership Philosophy")

st.markdown("""
> "Leadership is not about authority; it is about service,
> responsibility, and inspiring others to achieve a common goal."

I believe that effective leadership requires empathy,
integrity, accountability, and continuous learning.
By serving others and fostering collaboration,
leaders can create meaningful and lasting impact.
""")

st.divider()

# ACHIEVEMENT HIGHLIGHTS

st.subheader("🏆 Leadership Highlights")

st.success("""
✔ Grade 8 Representative (KABAYANI Club)

✔ Grade 12 Representative (YES-O)

✔ Class Vice President (BSCS 1A)

✔ Class President (BSCS 2A)

✔ DISCSS Representative

✔ President, Guincaiptan Katipunan ng Kabataan

✔ President, DISCSS

✔ Representative of DISCSS, CASCSC
""")

st.divider()

# FOOTER

st.markdown("""
<div class='footer'>

Leadership is about creating opportunities,
empowering others, and making a positive impact.

</div>
""", unsafe_allow_html=True)
