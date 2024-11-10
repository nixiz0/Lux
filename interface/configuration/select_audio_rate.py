import streamlit as st
from CONFIG import LANGUAGE, AUDIO_RATE
from configuration.update_config import update_config


def set_audio_rate():
    audio_rate = st.number_input("Configurer votre débit Audio (par défaut 44100)" if LANGUAGE == 'fr' else
                                 "Configure your Audio rate (default 44100)", value=AUDIO_RATE)
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_audio_rate'):
        update_config('AUDIO_RATE', audio_rate)
        st.success(f"Débit audio mise à jour en {audio_rate}" if LANGUAGE == 'fr' else 
                   f"Audio rate updated in {audio_rate}")