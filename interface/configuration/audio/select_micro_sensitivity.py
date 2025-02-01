import streamlit as st
from CONFIG import LANGUAGE, AUDIO_THRESHOLD
from configuration.update_config import update_config


def set_audio_threshold():
    """
    Configures the threshold for the application.
    """
    threshold = st.number_input("Entrez la sensibilité du microphone (par défaut 500)" if LANGUAGE == 'fr' else
                                "Enter the microphone sensitivity (default 500)", min_value=0, value=AUDIO_THRESHOLD)
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_audio_threshold'):
        update_config('AUDIO_THRESHOLD', threshold)
        st.success(f"Sensibilité du microphone mise à jour en {threshold}" if LANGUAGE == 'fr' else 
                   f"Microphone sensitivity updated to {threshold}")