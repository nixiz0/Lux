import streamlit as st
from CONFIG import LANGUAGE
from configuration.update_config import update_config


def set_lang():
    language = st.selectbox("Choisissez la langue" if LANGUAGE == 'fr' else "Choose language", ["fr", "en"], key='selectbox_lang')
    if st.button("Mettre à jour" if LANGUAGE == 'fr' else "Update", key='btn_set_lang'):
        update_config('LANGUAGE', f"'{language}'")
        st.success(f"Langue mise à jour en {language}" if LANGUAGE == 'fr' else f"Language updated to {language}")