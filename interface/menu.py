import streamlit as st
import base64
from PIL import Image
from io import BytesIO
from CONFIG import LANGUAGE
from configuration._ui_custom.page_title import set_page_title
from configuration._ui_custom.custom_ui import custom_ui


set_page_title("Lux-Interface")
custom_ui()

# Open image
logo_entreprise = Image.open('./interface/ressources/logo-lux.png')

# Convert image to base64 to display in markdown
buffered = BytesIO()
logo_entreprise.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Show image centered with reduced top margin
st.markdown(
    f"""
    <div style='text-align: center; margin-top: -60px;'>
        <img src='data:image/png;base64,{img_str}' width='300'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Center title and description
intro_content = {
    "fr": {
        "title": "Bienvenue sur l'interface Lux",
        "description": "Votre assistant personnalisable."
    },
    "en": {
        "title": "Welcome to the Lux interface",
        "description": "Your customizable assistant."
    }
}

# Select intro_content based on language
selected_intro_content = intro_content[LANGUAGE]

# Render Markdown
st.markdown(
    f"""
    <div style='text-align: center; margin-bottom: 5em;'>
        <h1>{selected_intro_content['title']}</h1>
        <h3>{selected_intro_content['description']}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Tools descriptions
tools = [
    {"name": "Tool hello", "description_fr": "Dit bonjour pour saluer", "description_en": "Says hello to greet", "emoji": "👋"},
    {"name": "Tool pause_running", "description_fr": "Met en pause le système, mode pause", "description_en": "Pauses the system, pause mode", "emoji": "⏸️"},
    {"name": "Tool exit_system", "description_fr": "Arrête le système, met à l'arrêt, stop tout", "description_en": "Shut down the system, shut down, stop everything", "emoji": "🛑"},
    {"name": "Tool time_in_locale", "description_fr": "Il est quelle heure", "description_en": "What time is it", "emoji": "⏰"},
    {"name": "Tool date_in_locale", "description_fr": "Quelle est la date actuelle", "description_en": "What is the current date", "emoji": "📅"},
    {"name": "Tool screen_with_cam", "description_fr": "Screen avec la caméra", "description_en": "Screen with the camera", "emoji": "📸"},
    {"name": "Tool screen", "description_fr": "Prends un screenshot, prends une capture d'écran", "description_en": "Take a screenshot", "emoji": "🖼️"},
    {"name": "Tool vocal_note", "description_fr": "Prends note", "description_en": "Take note", "emoji": "🗒️"},
    {"name": "Tool search_ytb", "description_fr": "Recherche sur youtube, cherche sur youtube", "description_en": "Search on youtube", "emoji": "🎥"},
    {"name": "Tool search_google", "description_fr": "Cherche sur google, recherche sur google", "description_en": "Search on google", "emoji": "🌐"},
    {"name": "Tool search_wikipedia", "description_fr": "Cherche sur wikipédia, recherche sur wikipédia", "description_en": "Search on wikipedia", "emoji": "🧠"},
    {"name": "Tool search_bing", "description_fr": "Cherche sur bing, recherche sur bing", "description_en": "Search on bing", "emoji": "🔍"},
]

# Generate Markdown content based on selected language with margin-top
markdown_content = "## 🌟 Standard Tools in Lux-Interface 🌟\n\n"
for tool in tools:
    description = tool[f"description_{LANGUAGE}"]
    markdown_content += f"<div style='margin-top: 1em; font-size: 1.25em;'><b>{tool['name']}</b>:</div>\n"
    markdown_content += f"    - <i>Description</i>: \"{description}\" {tool['emoji']}\n\n"

st.markdown(markdown_content, unsafe_allow_html=True)
