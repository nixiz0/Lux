import streamlit as st
from CONFIG import LANGUAGE, SPEED_VOICE
from configuration.update_config import update_config


def set_speed_voice():
    """
    Configures the speed voice for the application.
    """
    speed_voice = st.number_input("Entrez la vitesse de voix (par défaut 1.8)" if LANGUAGE == 'fr' else
                                  "Enter the voice speed (default 1.8)", min_value=0.5, value=SPEED_VOICE)
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_speed_voice'):
        update_config('SPEED_VOICE', speed_voice)
        st.success(f"Vitesse de la voix mise à jour en {speed_voice}" if LANGUAGE == 'fr' else 
                   f"Voice speed updated in {speed_voice}")