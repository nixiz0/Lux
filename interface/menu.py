import streamlit as st
from CONFIG import LANGUAGE
from configuration.page_title import set_page_title
from configuration.select_language import set_lang
from configuration.select_microphone import set_micro
from configuration.select_micro_sensitivity import set_audio_threshold
from configuration.select_speed_voice import set_speed_voice
from configuration.select_similarity import set_similarity
from configuration.select_cam import set_video_device
from configuration.select_audio_rate import set_audio_rate
from configuration.select_audio_chunk import set_audio_chunk
from configuration.select_buffer_length import set_buffer_length
from configuration.select_llm_max_history import set_llm_history_length
from configuration.select_build_model import set_build_model
from kernel.agent_llm.vectorization_tools import tools_vectorization
from kernel.kernel import start_lux


set_page_title("Lux-Interface")

activate_configuration  = st.sidebar.checkbox("Configuration")

st.sidebar.markdown("<hr style='margin:0px;'>", unsafe_allow_html=True)

if activate_configuration:
    st.sidebar.title("⚙️​Configuration")
    if st.sidebar.checkbox("Langue" if LANGUAGE == 'fr' else "Language", key='config_lang'):
        set_lang()

    if st.sidebar.checkbox("Microphone" if LANGUAGE == 'fr' else "Microphone", key='config_micro'):
        mic_index = set_micro()

    if st.sidebar.checkbox("Sensibilité du microphone" if LANGUAGE == 'fr' else "Microphone sensitivity", key='config_threshold'):
        set_audio_threshold()

    if st.sidebar.checkbox("Caméra" if LANGUAGE == 'fr' else "Camera", key='config_camera'):
        set_video_device()

    if st.sidebar.checkbox("Vectoriser les outils" if LANGUAGE == 'fr' else "Vectorize tools", key='config_vectorize_tools'):
        tools_vectorization()

    if st.sidebar.checkbox("Construction modèles LLMs" if LANGUAGE == 'fr' else "Building LLMs Models", key='config_build_model'):
        set_build_model()

    st.sidebar.title("🛠️​Configuration Avancée" if LANGUAGE == 'fr' else "🛠️​Advanced Configuration")
    if st.sidebar.checkbox("Vitesse de la voix" if LANGUAGE == 'fr' else "Voice speed", key='config_speed'):
        set_speed_voice()

    if st.sidebar.checkbox("Similarité" if LANGUAGE == 'fr' else "Similarity", key='config_similarity'):
        set_similarity()

    if st.sidebar.checkbox("Débit Audio" if LANGUAGE == 'fr' else "Audio rate", key='config_audio_rate'):
        set_audio_rate()

    if st.sidebar.checkbox("Chunk Audio" if LANGUAGE == 'fr' else "Audio Chunk", key='config_audio_chunk'):
        set_audio_chunk()

    if st.sidebar.checkbox("Buffer Audio" if LANGUAGE == 'fr' else "Audio Buffer", key='config_buffer_length'):
        set_buffer_length()

    if st.sidebar.checkbox("Historique de conversation LLM" if LANGUAGE == 'fr' else "Conversation LLM history", key='config_llm_history_length'):
        set_llm_history_length()
else: 
    if st.sidebar.checkbox("🤖​Start Lux", key='start_lux'):
        start_lux()