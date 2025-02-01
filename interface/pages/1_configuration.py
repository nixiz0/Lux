import streamlit as st
import os
from CONFIG import LANGUAGE, TEMP_TOOLS_DB_PATH
from configuration._ui_custom.page_title import set_page_title
from configuration._ui_custom.custom_ui import custom_ui
from configuration.select_language import set_lang
from configuration.audio.select_microphone import set_micro
from configuration.audio.select_micro_sensitivity import set_audio_threshold
from configuration.audio.select_speed_voice import set_speed_voice
from configuration.audio.select_audio_rate import set_audio_rate
from configuration.audio.select_audio_chunk import set_audio_chunk
from configuration.audio.select_buffer_length import set_buffer_length
from configuration.llm.select_llm_max_history import set_llm_history_length
from configuration.llm.select_build_model import set_build_model
from configuration.rag.select_similarity import set_similarity
from configuration.cam.select_cam import set_video_device
from configuration.upload_tools import adding_tool
from kernel.agent_llm.vectorization_tools import vectorize_tool
# ---Be careful to leave voice management as the last import---
from configuration.audio.change_synthetic_voice import manage_voice


set_page_title("Lux-Configuration")
custom_ui()

# Check if the folder exists, if not create it and vectorize tools
if not os.path.exists(TEMP_TOOLS_DB_PATH):
    os.makedirs(TEMP_TOOLS_DB_PATH)
    vectorize_tool()

set_build_model()


# ----[CONFIGURATION]----
st.sidebar.title("⚙️​ Configuration")

st.sidebar.subheader("🎙️ Langue et Microphone" if LANGUAGE == 'fr' else "🎙️ Language and Microphone")
if st.sidebar.checkbox("Langue" if LANGUAGE == 'fr' else "Language", key='config_lang'):
    set_lang()

if st.sidebar.checkbox("Microphone" if LANGUAGE == 'fr' else "Microphone", key='config_micro'):
    mic_index = set_micro()

if st.sidebar.checkbox("Sensibilité du microphone" if LANGUAGE == 'fr' else "Microphone sensitivity", key='config_threshold'):
    set_audio_threshold()

st.sidebar.subheader("📸​ Caméra" if LANGUAGE == 'fr' else "📸​ Camera")
if st.sidebar.checkbox("Caméra" if LANGUAGE == 'fr' else "Camera", key='config_camera'):
    set_video_device()

# ----[CONFIGURATION AVANCÉE]----
st.sidebar.title("🛠️​ Configuration Avancée" if LANGUAGE == 'fr' else "🛠️​ Advanced Configuration")

st.sidebar.subheader("🗣️​ Voix Synthétique" if LANGUAGE == 'fr' else "🗣️ Synthetic Voice")
if st.sidebar.checkbox("Gérer la voix synthétique actuelle" if LANGUAGE == 'fr' else "Manage current synthetic voice", key='replace_synthetic_voice'):
    manage_voice()

if st.sidebar.checkbox("Vitesse de la voix" if LANGUAGE == 'fr' else "Voice speed", key='config_speed'):
    set_speed_voice()

st.sidebar.subheader("🎧​ Audio")
if st.sidebar.checkbox("Débit Audio" if LANGUAGE == 'fr' else "Audio rate", key='config_audio_rate'):
    set_audio_rate()

if st.sidebar.checkbox("Chunk Audio" if LANGUAGE == 'fr' else "Audio Chunk", key='config_audio_chunk'):
    set_audio_chunk()

if st.sidebar.checkbox("Buffer Audio" if LANGUAGE == 'fr' else "Audio Buffer", key='config_buffer_length'):
    set_buffer_length()

st.sidebar.subheader("📚​ Historique" if LANGUAGE == 'fr' else "📚​ History")
if st.sidebar.checkbox("Historique de conversation LLM" if LANGUAGE == 'fr' else "Conversation LLM history", key='config_llm_history_length'):
    set_llm_history_length()

st.sidebar.subheader("➗​ Seuil déclenchement outils" if LANGUAGE == 'fr' else "➗ Tool trigger threshold")
if st.sidebar.checkbox("Similarité" if LANGUAGE == 'fr' else "Similarity", key='config_similarity'):
    set_similarity()

# ----[ADD TOOLS]----
st.sidebar.title("🛠️​ Ajout d'Outils" if LANGUAGE == 'fr' else "🛠️​ Adding Tools")

if st.sidebar.checkbox("Importer Outils" if LANGUAGE == 'fr' else "Import Tools", key='upload_tools'):
    adding_tool()
