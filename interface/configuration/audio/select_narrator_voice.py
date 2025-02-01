import streamlit as st
import pyttsx3
from CONFIG import LANGUAGE, NARRATOR_VOICE
from configuration.update_config import update_config


def get_voice_list():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_dict = {i: voice for i, voice in enumerate(voices)}
    return voice_dict

def manage_voice():
    voices = get_voice_list()
    voice_names = [''] + [voices[i].name for i in voices]  # Add an empty string to the top of the list

    st.markdown("<hr style='margin:5px;'>", unsafe_allow_html=True)

    selected_voice_id = None  # Set selected_voice_id to None

    if LANGUAGE == "fr":
        selected_voice_name = st.selectbox('Sélectionnez la voix synthétique à utiliser', voice_names, index=0)
    else:
        selected_voice_name = st.selectbox('Select the synthetic voice to use', voice_names, index=0)

    # If the user has not selected a voice, do nothing
    if selected_voice_name == '':
        return None

    selected_voice_id = [voice.id for voice in voices.values() if voice.name == selected_voice_name][0] if selected_voice_name else ''

    st.markdown("<p style='font-weight: bold; color:#c05bb6;'>ID de la Voix du Narrateur sélectionné: " + NARRATOR_VOICE + "</p>" if LANGUAGE == 'fr' else 
                "<p style='font-weight: bold; color:#c05bb6;'>Selected Narrator Voice ID: " + NARRATOR_VOICE + "</p>", unsafe_allow_html=True)

    # Updates CONFIG.py with the universal update_config function
    update_config('NARRATOR_VOICE', f'"{selected_voice_id}"')

    return selected_voice_id