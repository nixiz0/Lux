import streamlit as st
from CONFIG import LANGUAGE, AUDIO_BUFFER_LENGTH
from configuration.update_config import update_config


def set_buffer_length():
    buffer_length = st.number_input("Configurer votre buffer Audio (par défaut 2)" if LANGUAGE == 'fr' else
                                    "Configure your Audio buffer (default 2)", min_value=1,value=AUDIO_BUFFER_LENGTH)
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_buffer_length'):
        update_config('AUDIO_BUFFER_LENGTH', buffer_length)
        st.success(f"Audio buffer mise à jour en {buffer_length}" if LANGUAGE == 'fr' else 
                   f"Buffer audio updated in {buffer_length}")