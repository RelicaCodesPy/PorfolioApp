import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="🎨",
    layout="wide"
)

# LOAD CSS
with open("styles/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🎨 Graphic Arts Projects")

st.markdown("""
### Role: Graphic Artist

This collection showcases my graphic design and digital art projects
developed through competitions, advocacy campaigns, creative challenges,
and personal artistic exploration.

Each artwork demonstrates creativity, visual storytelling,
design thinking, and digital artistry.
""")

st.divider()

# FILTER

category = st.selectbox(
    "Filter Projects",
    [
        "All",
        "Digital Illustration",
        "Advocacy Poster",
        "Typography",
        "Photo Manipulation",
        "Abstract Art"
    ]
)

st.divider()

# PROJECT 1

with st.expander("🧚 Enchanted Whispers"):

    st.image(
        "assets/artwork7.jpg",
        use_container_width=True
    )

    st.markdown("""
### Project Overview

**Role:** Graphic Artist

**Category:** Digital Illustration

**Description:**

A fantasy-inspired artwork portraying a fairy surrounded
by butterflies and floral elements.

The artwork symbolizes imagination, freedom,
and the beauty of nature through elegant composition
and visual harmony.

### Skills Applied

- Digital Illustration
- Creative Composition
- Visual Storytelling
- Color Harmony

### Tools Used

- Canva
""")

# PROJECT 2

with st.expander("❤️ One Chance"):

    st.image(
        "assets/artwork6.jpg",
        use_container_width=True
    )

    st.markdown("""
### Project Overview

**Role:** Graphic Artist

**Category:** Typography Poster

**Description:**

A motivational typography poster emphasizing the importance
of making every opportunity count.

The design combines meaningful messaging and visual hierarchy
to inspire determination and excellence.

### Skills Applied

- Typography Design
- Poster Layout
- Visual Communication
- Creative Thinking

### Tools Used

- Canva
""")

# PROJECT 3

with st.expander("🌍 A Fading World: Our Last Chance"):

    st.image(
        "assets/artwork5.jpg",
        use_container_width=True
    )

    st.markdown("""
### Project Overview

**Role:** Graphic Artist

**Category:** Environmental Advocacy

**Description:**

An environmental awareness poster highlighting climate change,
pollution, and humanity's responsibility to protect the Earth.

The artwork encourages collective action toward sustainability.

### Skills Applied

- Advocacy Design
- Environmental Campaign Design
- Photo Manipulation
- Digital Compositing

### Tools Used

- Canva
""")

# PROJECT 4

with st.expander("🌲 Trees for the Future"):

    st.image(
        "assets/artwork4.jpg",
        use_container_width=True
    )

    st.markdown("""
### Project Overview

**Role:** Graphic Artist

**Category:** Environmental Conservation

**Description:**

A conservation-themed artwork promoting reforestation,
wildlife protection, and environmental sustainability.

The design highlights the importance of preserving forests
for future generations.

### Skills Applied

- Poster Design
- Digital Illustration
- Visual Messaging
- Creative Composition

### Tools Used

- Canva
""")

# PROJECT 5

with st.expander("🎨 Fragments of Imagination"):

    st.image(
        "assets/artwork3.jpg",
        use_container_width=True
    )

    st.markdown("""
### Project Overview

**Role:** Graphic Artist

**Category:** Abstract Art

**Description:**

An abstract digital artwork showcasing creativity through
vibrant colors, flowing patterns, and imaginative forms.

The artwork represents limitless creativity and artistic freedom.

### Skills Applied

- Abstract Art
- Creative Visualization
- Pattern Design
- Digital Art

### Tools Used

- Canva
""")

# PROJECT 6

with st.expander("🌌 Beyond Reality"):

    st.image(
        "assets/artwork2.jpg",
        use_container_width=True
    )

    st.markdown("""
### Project Overview

**Role:** Graphic Artist

**Category:** Photo Manipulation

**Description:**

A surreal double-exposure artwork blending portrait imagery,
nature, and cosmic elements.

The composition explores identity, imagination,
and human connection with nature.

### Skills Applied

- Photo Manipulation
- Double Exposure
- Digital Compositing
- Creative Editing

### Tools Used

- Canva
""")

# PROJECT 7

with st.expander("🌸 Neon Serenity"):

    st.image(
        "assets/artwork1.jpg",
        use_container_width=True
    )

    st.markdown("""
### Project Overview

**Role:** Graphic Artist

**Category:** Digital Illustration

**Description:**

A vibrant anime-inspired digital illustration featuring
detailed line work, expressive colors, and decorative elements.

The artwork celebrates individuality, confidence,
and modern digital art.

### Skills Applied

- Character Illustration
- Digital Drawing
- Color Theory
- Graphic Design

### Tools Used

- Canva
""")

st.divider()

# PROJECT STATISTICS

st.subheader("📊 Portfolio Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Artworks",
        "7"
    )

with col2:
    st.metric(
        "Role",
        "Graphic Artist"
    )

with col3:
    st.metric(
        "Design Awards",
        "10+"
    )

with col4:
    st.metric(
        "GDF Recognition",
        "Multiple"
    )

st.divider()

# GDF ACHIEVEMENTS

st.subheader("🏆 Related Graphic Design Achievements")

st.success("""
🎨 Graphic Design Festival (GDF 2024)

• 1st Runner Up

• Rank 2 – Art Exhibit

• Rank 2 – Semi Finals

• Best in Photo Manipulation

• Best Abstract Art

• Best in One Color Shade Art

• Most Popular Graphic Design

• Nitezen's Choice

• Top Performing Speed Art

• Top Performing Finalist – Fixing a Broken Art Challenge
""")

st.divider()

st.markdown("""
<div class='footer'>

Creativity transforms ideas into impactful visual experiences.

</div>
""", unsafe_allow_html=True)
