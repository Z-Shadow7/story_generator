import streamlit as st
from components.story_generator import generate_story
from components.image_generator import render_image
from components.pdf_generator import generate_pdf

GENRES = ["Fantasy", "Horror", "Adventure", "Sci-fi", "Romance", "Mystery", "Comedy"]
LENGTHS = {"Short": 3, "Medium": 5, "Long": 7}

def render_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
            background-color: #0d0d0d;
            color: #f0ece4;
        }

        .stApp { background: #0d0d0d; }

        .hero {
            text-align: center;
            padding: 3rem 1rem 2rem;
        }

        .hero h1 {
            font-family: 'Syne', sans-serif;
            font-size: 3.5rem;
            font-weight: 800;
            letter-spacing: -2px;
            background: linear-gradient(135deg, #f0ece4 30%, #ff6b6b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.3rem;
        }

        .hero p { color: #888; font-size: 1rem; font-weight: 300; }

        .card {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 1.5rem;
        }

        .scene-card {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .scene-number {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #ff6b6b;
            font-weight: 500;
            margin-bottom: 0.3rem;
        }

        .scene-title {
            font-family: 'Syne', sans-serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: #f0ece4;
            margin-bottom: 0.8rem;
        }

        .scene-story {
            font-size: 1rem;
            font-weight: 300;
            color: #ccc;
            line-height: 1.7;
        }

        .character-card {
            background: #111;
            border: 1px solid #2a2a2a;
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.8rem;
        }

        div[data-testid="stSelectbox"] label,
        div[data-testid="stTextArea"] label,
        div[data-testid="stTextInput"] label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #888;
            font-weight: 500;
        }

        div[data-testid="stSelectbox"] > div,
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stTextInput"] input {
            background: #111 !important;
            border: 1px solid #2a2a2a !important;
            border-radius: 10px !important;
            color: #f0ece4 !important;
        }

        .stButton > button {
            background: #ff6b6b;
            color: #0d0d0d;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 0.9rem;
            letter-spacing: 1px;
            border: none;
            border-radius: 10px;
            padding: 0.65rem 2rem;
            width: 100%;
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            background: #ff8585;
            transform: translateY(-1px);
            box-shadow: 0 8px 24px rgba(255, 107, 107, 0.25);
        }

        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def render_header():
    render_styles()
    st.markdown("""
        <div class="hero">
            <h1>📖 Story Generator</h1>
            <p>AI-powered stories with images for every scene</p>
        </div>
    """, unsafe_allow_html=True)

def render_character_creator():
    st.markdown("### 🧑 Characters")
    if "characters" not in st.session_state:
        st.session_state.characters = []

    with st.expander("➕ Add a Character"):
        col1, col2 = st.columns(2)
        with col1:
            char_name = st.text_input("Name", key="char_name")
            char_role = st.selectbox("Role", ["Hero", "Villain", "Sidekick", "Mentor", "Other"], key="char_role")
        with col2:
            char_desc = st.text_area("Description", placeholder="Brave knight with a silver sword...", key="char_desc", height=100)

        if st.button("Add Character", key="add_char_btn"):
            if char_name.strip():
                st.session_state.characters.append({
                    "name": char_name,
                    "role": char_role,
                    "description": char_desc
                })
                st.success(f"Added {char_name}!")

    if st.session_state.characters:
        for i, char in enumerate(st.session_state.characters):
            st.markdown(f"""
                <div class="character-card">
                    <strong>{char['name']}</strong> — <span style="color:#ff6b6b">{char['role']}</span><br>
                    <small style="color:#888">{char['description']}</small>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Remove", key=f"remove_char_{i}"):
                st.session_state.characters.pop(i)
                st.rerun()

    return st.session_state.characters

def render_story(api_key: str, hf_api_key: str):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        prompt = st.text_input("Story Topic", placeholder="A lost astronaut on an unknown planet...")
    with col2:
        genre = st.selectbox("Genre", GENRES)
    with col3:
        length = st.selectbox("Length", list(LENGTHS.keys()))

    characters = render_character_creator()

    if st.button("✦ Generate Story", key="generate_btn"):
        st.session_state.scenes = []
        if prompt.strip():
            with st.spinner("Writing your story..."):
                scenes = generate_story(
                    prompt, genre, api_key,
                    num_scenes=LENGTHS[length],
                    characters=characters
                )
                st.session_state.scenes = scenes
                st.session_state.story_title = prompt
        else:
            st.warning("Please enter a story topic.")

    st.markdown('</div>', unsafe_allow_html=True)

    if "scenes" in st.session_state and st.session_state.scenes:
        for scene in st.session_state.scenes:
            st.markdown('<div class="scene-card">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f'<div class="scene-number">Scene {scene["scene_number"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="scene-title">{scene["title"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="scene-story">{scene["story"]}</div>', unsafe_allow_html=True)
            with col2:
                image_bytes = render_image(scene['image_prompt'], scene['scene_number'], hf_api_key)
                scene['image_bytes'] = image_bytes
            st.markdown('</div>', unsafe_allow_html=True)
            st.divider()

        # PDF download button
        st.markdown("### 📥 Download Story")
        pdf_bytes = generate_pdf(
            st.session_state.scenes,
            title=st.session_state.get("story_title", "My AI Story")
        )
        st.download_button(
            label="📄 Download as PDF",
            data=pdf_bytes,
            file_name=f"{st.session_state.get('story_title', 'story')}.pdf",
            mime="application/pdf",
            key="download_pdf"
        )