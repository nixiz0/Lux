import streamlit as st
from CONFIG import LANGUAGE, AUDIO_CHUNK
from configuration.update_config import update_config


def set_audio_chunk():
    audio_chunk = st.number_input("Configurer votre chunk Audio (par défaut 1024)" if LANGUAGE == 'fr' else
                                  "Configure your Audio chunk (default 1024)", value=AUDIO_CHUNK)
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_audio_chunk'):
        update_config('AUDIO_CHUNK', audio_chunk)
        st.success(f"Audio chunk mise à jour en {audio_chunk}" if LANGUAGE == 'fr' else 
                   f"Audio chunk updated in {audio_chunk}")